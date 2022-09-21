# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetRolloutResult',
    'AwaitableGetRolloutResult',
    'get_rollout',
    'get_rollout_output',
]

@pulumi.output_type
class GetRolloutResult:
    """
    Defines the rollout.
    """
    def __init__(__self__, artifact_source_id=None, build_version=None, id=None, identity=None, location=None, name=None, operation_info=None, services=None, status=None, step_groups=None, tags=None, target_service_topology_id=None, total_retry_attempts=None, type=None):
        if artifact_source_id and not isinstance(artifact_source_id, str):
            raise TypeError("Expected argument 'artifact_source_id' to be a str")
        pulumi.set(__self__, "artifact_source_id", artifact_source_id)
        if build_version and not isinstance(build_version, str):
            raise TypeError("Expected argument 'build_version' to be a str")
        pulumi.set(__self__, "build_version", build_version)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if operation_info and not isinstance(operation_info, dict):
            raise TypeError("Expected argument 'operation_info' to be a dict")
        pulumi.set(__self__, "operation_info", operation_info)
        if services and not isinstance(services, list):
            raise TypeError("Expected argument 'services' to be a list")
        pulumi.set(__self__, "services", services)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if step_groups and not isinstance(step_groups, list):
            raise TypeError("Expected argument 'step_groups' to be a list")
        pulumi.set(__self__, "step_groups", step_groups)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if target_service_topology_id and not isinstance(target_service_topology_id, str):
            raise TypeError("Expected argument 'target_service_topology_id' to be a str")
        pulumi.set(__self__, "target_service_topology_id", target_service_topology_id)
        if total_retry_attempts and not isinstance(total_retry_attempts, int):
            raise TypeError("Expected argument 'total_retry_attempts' to be a int")
        pulumi.set(__self__, "total_retry_attempts", total_retry_attempts)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="artifactSourceId")
    def artifact_source_id(self) -> Optional[str]:
        """
        The reference to the artifact source resource Id where the payload is located.
        """
        return pulumi.get(self, "artifact_source_id")

    @property
    @pulumi.getter(name="buildVersion")
    def build_version(self) -> str:
        """
        The version of the build being deployed.
        """
        return pulumi.get(self, "build_version")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityResponse']:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationInfo")
    def operation_info(self) -> 'outputs.RolloutOperationInfoResponse':
        """
        Operational information of the rollout.
        """
        return pulumi.get(self, "operation_info")

    @property
    @pulumi.getter
    def services(self) -> Sequence['outputs.ServiceResponse']:
        """
        The detailed information on the services being deployed.
        """
        return pulumi.get(self, "services")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The current status of the rollout.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="stepGroups")
    def step_groups(self) -> Sequence['outputs.StepGroupResponse']:
        """
        The list of step groups that define the orchestration.
        """
        return pulumi.get(self, "step_groups")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetServiceTopologyId")
    def target_service_topology_id(self) -> str:
        """
        The resource Id of the service topology from which service units are being referenced in step groups to be deployed.
        """
        return pulumi.get(self, "target_service_topology_id")

    @property
    @pulumi.getter(name="totalRetryAttempts")
    def total_retry_attempts(self) -> int:
        """
        The cardinal count of total number of retries performed on the rollout at a given time.
        """
        return pulumi.get(self, "total_retry_attempts")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetRolloutResult(GetRolloutResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRolloutResult(
            artifact_source_id=self.artifact_source_id,
            build_version=self.build_version,
            id=self.id,
            identity=self.identity,
            location=self.location,
            name=self.name,
            operation_info=self.operation_info,
            services=self.services,
            status=self.status,
            step_groups=self.step_groups,
            tags=self.tags,
            target_service_topology_id=self.target_service_topology_id,
            total_retry_attempts=self.total_retry_attempts,
            type=self.type)


def get_rollout(resource_group_name: Optional[str] = None,
                retry_attempt: Optional[int] = None,
                rollout_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRolloutResult:
    """
    Defines the PUT rollout request body.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param int retry_attempt: Rollout retry attempt ordinal to get the result of. If not specified, result of the latest attempt will be returned.
    :param str rollout_name: The rollout name.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['retryAttempt'] = retry_attempt
    __args__['rolloutName'] = rollout_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:deploymentmanager/v20191101preview:getRollout', __args__, opts=opts, typ=GetRolloutResult).value

    return AwaitableGetRolloutResult(
        artifact_source_id=__ret__.artifact_source_id,
        build_version=__ret__.build_version,
        id=__ret__.id,
        identity=__ret__.identity,
        location=__ret__.location,
        name=__ret__.name,
        operation_info=__ret__.operation_info,
        services=__ret__.services,
        status=__ret__.status,
        step_groups=__ret__.step_groups,
        tags=__ret__.tags,
        target_service_topology_id=__ret__.target_service_topology_id,
        total_retry_attempts=__ret__.total_retry_attempts,
        type=__ret__.type)


@_utilities.lift_output_func(get_rollout)
def get_rollout_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                       retry_attempt: Optional[pulumi.Input[Optional[int]]] = None,
                       rollout_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRolloutResult]:
    """
    Defines the PUT rollout request body.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param int retry_attempt: Rollout retry attempt ordinal to get the result of. If not specified, result of the latest attempt will be returned.
    :param str rollout_name: The rollout name.
    """
    ...
