# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['ImportPipelineArgs', 'ImportPipeline']

@pulumi.input_type
class ImportPipelineArgs:
    def __init__(__self__, *,
                 registry_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 source: pulumi.Input['ImportPipelineSourcePropertiesArgs'],
                 identity: Optional[pulumi.Input['IdentityPropertiesArgs']] = None,
                 import_pipeline_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'PipelineOptions']]]]] = None,
                 trigger: Optional[pulumi.Input['PipelineTriggerPropertiesArgs']] = None):
        """
        The set of arguments for constructing a ImportPipeline resource.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        :param pulumi.Input['ImportPipelineSourcePropertiesArgs'] source: The source properties of the import pipeline.
        :param pulumi.Input['IdentityPropertiesArgs'] identity: The identity of the import pipeline.
        :param pulumi.Input[str] import_pipeline_name: The name of the import pipeline.
        :param pulumi.Input[str] location: The location of the import pipeline.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'PipelineOptions']]]] options: The list of all options configured for the pipeline.
        :param pulumi.Input['PipelineTriggerPropertiesArgs'] trigger: The properties that describe the trigger of the import pipeline.
        """
        pulumi.set(__self__, "registry_name", registry_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "source", source)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if import_pipeline_name is not None:
            pulumi.set(__self__, "import_pipeline_name", import_pipeline_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if options is not None:
            pulumi.set(__self__, "options", options)
        if trigger is not None:
            pulumi.set(__self__, "trigger", trigger)

    @property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[str]:
        """
        The name of the container registry.
        """
        return pulumi.get(self, "registry_name")

    @registry_name.setter
    def registry_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "registry_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group to which the container registry belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input['ImportPipelineSourcePropertiesArgs']:
        """
        The source properties of the import pipeline.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input['ImportPipelineSourcePropertiesArgs']):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityPropertiesArgs']]:
        """
        The identity of the import pipeline.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityPropertiesArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="importPipelineName")
    def import_pipeline_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the import pipeline.
        """
        return pulumi.get(self, "import_pipeline_name")

    @import_pipeline_name.setter
    def import_pipeline_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "import_pipeline_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the import pipeline.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'PipelineOptions']]]]]:
        """
        The list of all options configured for the pipeline.
        """
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'PipelineOptions']]]]]):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter
    def trigger(self) -> Optional[pulumi.Input['PipelineTriggerPropertiesArgs']]:
        """
        The properties that describe the trigger of the import pipeline.
        """
        return pulumi.get(self, "trigger")

    @trigger.setter
    def trigger(self, value: Optional[pulumi.Input['PipelineTriggerPropertiesArgs']]):
        pulumi.set(self, "trigger", value)


class ImportPipeline(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityPropertiesArgs']]] = None,
                 import_pipeline_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'PipelineOptions']]]]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['ImportPipelineSourcePropertiesArgs']]] = None,
                 trigger: Optional[pulumi.Input[pulumi.InputType['PipelineTriggerPropertiesArgs']]] = None,
                 __props__=None):
        """
        An object that represents an import pipeline for a container registry.
        API Version: 2020-11-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['IdentityPropertiesArgs']] identity: The identity of the import pipeline.
        :param pulumi.Input[str] import_pipeline_name: The name of the import pipeline.
        :param pulumi.Input[str] location: The location of the import pipeline.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'PipelineOptions']]]] options: The list of all options configured for the pipeline.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        :param pulumi.Input[pulumi.InputType['ImportPipelineSourcePropertiesArgs']] source: The source properties of the import pipeline.
        :param pulumi.Input[pulumi.InputType['PipelineTriggerPropertiesArgs']] trigger: The properties that describe the trigger of the import pipeline.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ImportPipelineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An object that represents an import pipeline for a container registry.
        API Version: 2020-11-01-preview.

        :param str resource_name: The name of the resource.
        :param ImportPipelineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ImportPipelineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityPropertiesArgs']]] = None,
                 import_pipeline_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'PipelineOptions']]]]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['ImportPipelineSourcePropertiesArgs']]] = None,
                 trigger: Optional[pulumi.Input[pulumi.InputType['PipelineTriggerPropertiesArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ImportPipelineArgs.__new__(ImportPipelineArgs)

            __props__.__dict__["identity"] = identity
            __props__.__dict__["import_pipeline_name"] = import_pipeline_name
            __props__.__dict__["location"] = location
            __props__.__dict__["options"] = options
            if registry_name is None and not opts.urn:
                raise TypeError("Missing required property 'registry_name'")
            __props__.__dict__["registry_name"] = registry_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            __props__.__dict__["trigger"] = trigger
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerregistry/v20191201preview:ImportPipeline"), pulumi.Alias(type_="azure-native:containerregistry/v20201101preview:ImportPipeline"), pulumi.Alias(type_="azure-native:containerregistry/v20210601preview:ImportPipeline"), pulumi.Alias(type_="azure-native:containerregistry/v20210801preview:ImportPipeline"), pulumi.Alias(type_="azure-native:containerregistry/v20211201preview:ImportPipeline"), pulumi.Alias(type_="azure-native:containerregistry/v20220201preview:ImportPipeline")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ImportPipeline, __self__).__init__(
            'azure-native:containerregistry:ImportPipeline',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ImportPipeline':
        """
        Get an existing ImportPipeline resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ImportPipelineArgs.__new__(ImportPipelineArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["options"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["trigger"] = None
        __props__.__dict__["type"] = None
        return ImportPipeline(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityPropertiesResponse']]:
        """
        The identity of the import pipeline.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the import pipeline.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def options(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of all options configured for the pipeline.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the pipeline at the time the operation was called.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output['outputs.ImportPipelineSourcePropertiesResponse']:
        """
        The source properties of the import pipeline.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def trigger(self) -> pulumi.Output[Optional['outputs.PipelineTriggerPropertiesResponse']]:
        """
        The properties that describe the trigger of the import pipeline.
        """
        return pulumi.get(self, "trigger")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

