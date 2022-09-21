"""Utilities to assemble effective with MLCube configuration.

- `IOType`: Input/output type of MLCube task parameter.
- `ParameterType`: Type of MLCube task parameter.
- `MLCubeConfig`: Utilities to assemble effective MLCube configuration.
"""
import logging
import os
import typing as t

from mlcube.runner import Runner

from omegaconf import (DictConfig, OmegaConf)


logger = logging.getLogger(__name__)

__all__ = ['IOType', 'ParameterType', 'MLCubeConfig']


class IOType(object):
    """Input/output type of MLCube task parameter."""

    INPUT = 'input'
    """This parameter is input parameter (e.g., path to data)."""

    OUTPUT = 'output'
    """This parameter is output parameter (e.g., path to trained model)."""

    @staticmethod
    def is_valid(io: str) -> bool:
        """Return true if string `io` contain valid IO type."""
        return io in (IOType.INPUT, IOType.OUTPUT)


class ParameterType(object):
    """Type of MLCube task parameter."""

    FILE = 'file'
    """This parameter is a file."""

    DIRECTORY = 'directory'
    """This parameter is a directory."""

    UNKNOWN = 'unknown'
    """Type is unknown (only used internally)."""

    @staticmethod
    def is_valid(io: str) -> bool:
        """Return true if string `io` contain valid parameter type."""
        return io in (ParameterType.FILE, ParameterType.DIRECTORY, ParameterType.UNKNOWN)


class MountType(object):
    """Read-Write (rw) or Read-Only type of MLCube mount parameter."""

    RW = 'rw'
    """This parameter is reads-write parameter (e.g., path to data)."""

    RO = 'ro'
    """This parameter is read-only parameter"""

    @staticmethod
    def is_valid(io: str) -> bool:
        """Return true if string `opts` contain valid MountType type."""
        return io in (MountType.RW, MountType.RO)


class MLCubeConfig(object):
    """Utilities to assemble effective MLCube configuration."""

    @staticmethod
    def ensure_values_exist(config: DictConfig, keys: t.Union[str, t.List], constructor: t.Callable) -> t.List:
        """Make sure the `config` dictionary contains specified keys.

        Args:
            config: Dictionary.
            keys: Keys that must exist in this dictionary.
            constructor: Factory function to create values for keys in `keys` that are not in `config`.
        """
        if isinstance(keys, str):
            keys = [keys]
        for key in keys:
            if config.get(key, None) is None:
                config[key] = constructor()
        return [config[key] for key in keys]

    @staticmethod
    def get_uri(value: str) -> str:
        """Validate `value` is a valid URI."""
        if value.startswith('storage:'):
            raise ValueError("Storage schema is not yet supported")
        return os.path.abspath(os.path.expanduser(value))

    @staticmethod
    def create_mlcube_config(mlcube_config_file: str, mlcube_cli_args: t.Optional[DictConfig] = None,
                             task_cli_args: t.Optional[t.Dict] = None, runner_config: t.Optional[DictConfig] = None,
                             workspace: t.Optional[str] = None, resolve: bool = True,
                             runner_cls: t.Optional[t.Type[Runner]] = None) -> DictConfig:
        """Create MLCube configuration merging different configs - base, global, local and cli.

        Args:
            mlcube_config_file: Path to mlcube.yaml file.
            mlcube_cli_args: MLCube parameters from command line.
            task_cli_args: Task parameters from command line.
            runner_config: MLCube runner configuration, usually comes from system settings file.
            workspace: Workspace path to use in this MLCube run.
            resolve: If true, compute all values (some of them may reference other parameters or environmental
                variables).
            runner_cls: A python class for the runner type specified in `runner_config`.
        """
        if mlcube_cli_args is None:
            mlcube_cli_args = OmegaConf.create({})
        if task_cli_args is None:
            task_cli_args = {}
        if runner_config is None:
            runner_config = OmegaConf.create({})
        logger.debug("mlcube_config_file = %s", mlcube_config_file)
        logger.debug("mlcube_cli_args = %s", mlcube_cli_args)
        logger.debug("task_cli_args = %s", task_cli_args)
        logger.debug("runner_config = %s", str(runner_config))
        logger.debug("workspace = %s", workspace)

        # Load MLCube configuration and maybe override parameters from command line (like -Pdocker.build_strategy=...).
        actual_workspace = '${runtime.root}/workspace' if workspace is None else MLCubeConfig.get_uri(workspace)
        mlcube_config = OmegaConf.merge(
            OmegaConf.load(mlcube_config_file),
            mlcube_cli_args,
            OmegaConf.create({
                'runtime': {
                    'root': os.path.dirname(mlcube_config_file),
                    'workspace': actual_workspace
                },
                'runner': runner_config
            })
        )
        # Maybe this is not the best idea, but originally MLCube used $WORKSPACE token to refer to the internal
        # workspace. So, this value is here to simplify access to workspace value. BTW, in general, if files are to be
        # located inside workspace (internal or custom), users are encouraged not to use ${runtime.workspace} or
        # ${workspace} in their MLCube configuration files.
        mlcube_config['workspace'] = actual_workspace
        # Merge, for instance, docker runner config from system settings with docker config from MLCube config.
        if runner_cls:
            runner_cls.CONFIG.merge(mlcube_config)
        # Need to apply CLI arguments again just in case users provided something like -Prunner.build_strategy=...
        mlcube_config = OmegaConf.merge(mlcube_config, mlcube_cli_args)
        if runner_cls:
            runner_cls.CONFIG.validate(mlcube_config)

        for task_name in mlcube_config.tasks.keys():
            [task] = MLCubeConfig.ensure_values_exist(mlcube_config.tasks, task_name, dict)
            if 'entrypoint' in task and task['entrypoint'] is None:
                logger.warning(
                    "MLCube task (%s) specifies an entrypoint that is None: removing it (a default "
                    "entrypoint will be used).", task_name
                )
                task.pop('entrypoint')
            [parameters] = MLCubeConfig.ensure_values_exist(task, 'parameters', dict)
            [inputs, outputs] = MLCubeConfig.ensure_values_exist(parameters, ['inputs', 'outputs'], dict)

            MLCubeConfig.check_parameters(inputs, task_cli_args)
            MLCubeConfig.check_parameters(outputs, task_cli_args)

        if resolve:
            OmegaConf.resolve(mlcube_config)
        return mlcube_config

    @staticmethod
    def check_parameters(parameters: DictConfig, task_cli_args: t.Dict) -> None:
        """Check that task parameters are defined according to MLCube schema.

        Args:
            parameters: Task parameters (`inputs` or `outputs`).
            task_cli_args: Task parameters from command line.
        This function does not set `type` of parameters (if not present) in all cases.
        """
        for name in parameters.keys():
            # The `_param_name` is anyway there, so check it's not None.
            [param_def] = MLCubeConfig.ensure_values_exist(parameters, name, dict)
            # Deal with the case when value is a string (default value).
            if isinstance(param_def, str):
                parameters[name] = {'default': param_def}
                param_def = parameters[name]
            # If `default` key is not present, use parameter name as value.
            _ = MLCubeConfig.ensure_values_exist(param_def, 'default', lambda: name)
            # One challenge is how to identify type (file, directory) of input/output parameters if users have
            # not provided these types. The below is a kind of rule-based system that tries to infer types.

            # Make sure every parameter definition contains 'type' field. Also, if it's unknown, we can assume it's a
            # directory if a value ends with forward/backward slash.
            _ = MLCubeConfig.ensure_values_exist(param_def, 'type', lambda: ParameterType.UNKNOWN)
            if param_def.type == ParameterType.UNKNOWN and param_def.default.endswith(os.sep):
                param_def.type = ParameterType.DIRECTORY
            # See if there is value on a command line
            param_def.default = task_cli_args.get(name, param_def.default)
            # Check again parameter type. Users in certain number of cases will not be providing final slash on a
            # command line for directories, so we tried to infer types above using default values. Just in case, see
            # if we can do the same with user-provided values.
            # TODO: what if a parameter in mlcube.yaml is declared to be a file, but users provided something with
            #       slash at the end.
            if param_def.type == ParameterType.UNKNOWN and param_def.default.endswith(os.sep):
                param_def.type = ParameterType.DIRECTORY

            # TODO: For some input parameters, that generally speaking must exist, we can figure out types later,
            #       when we actually use them (in one of the runners). One problem is when inputs are optional. In this
            #       case, we need to know their type in advance.

            # It probably does not make too much sense to see, let's say, if an input parameter exists and set its
            # type at this moment, because MLCube can run on remote hosts.
