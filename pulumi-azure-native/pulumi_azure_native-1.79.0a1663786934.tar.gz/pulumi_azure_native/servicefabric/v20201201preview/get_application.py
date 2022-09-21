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
    'GetApplicationResult',
    'AwaitableGetApplicationResult',
    'get_application',
    'get_application_output',
]

@pulumi.output_type
class GetApplicationResult:
    """
    The application resource.
    """
    def __init__(__self__, etag=None, id=None, identity=None, location=None, managed_identities=None, maximum_nodes=None, metrics=None, minimum_nodes=None, name=None, parameters=None, provisioning_state=None, remove_application_capacity=None, system_data=None, tags=None, type=None, type_name=None, type_version=None, upgrade_policy=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_identities and not isinstance(managed_identities, list):
            raise TypeError("Expected argument 'managed_identities' to be a list")
        pulumi.set(__self__, "managed_identities", managed_identities)
        if maximum_nodes and not isinstance(maximum_nodes, float):
            raise TypeError("Expected argument 'maximum_nodes' to be a float")
        pulumi.set(__self__, "maximum_nodes", maximum_nodes)
        if metrics and not isinstance(metrics, list):
            raise TypeError("Expected argument 'metrics' to be a list")
        pulumi.set(__self__, "metrics", metrics)
        if minimum_nodes and not isinstance(minimum_nodes, float):
            raise TypeError("Expected argument 'minimum_nodes' to be a float")
        pulumi.set(__self__, "minimum_nodes", minimum_nodes)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if remove_application_capacity and not isinstance(remove_application_capacity, bool):
            raise TypeError("Expected argument 'remove_application_capacity' to be a bool")
        pulumi.set(__self__, "remove_application_capacity", remove_application_capacity)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if type_name and not isinstance(type_name, str):
            raise TypeError("Expected argument 'type_name' to be a str")
        pulumi.set(__self__, "type_name", type_name)
        if type_version and not isinstance(type_version, str):
            raise TypeError("Expected argument 'type_version' to be a str")
        pulumi.set(__self__, "type_version", type_version)
        if upgrade_policy and not isinstance(upgrade_policy, dict):
            raise TypeError("Expected argument 'upgrade_policy' to be a dict")
        pulumi.set(__self__, "upgrade_policy", upgrade_policy)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Azure resource etag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ManagedIdentityResponse']:
        """
        Describes the managed identities for an Azure resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        It will be deprecated in New API, resource location depends on the parent resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedIdentities")
    def managed_identities(self) -> Optional[Sequence['outputs.ApplicationUserAssignedIdentityResponse']]:
        """
        List of user assigned identities for the application, each mapped to a friendly name.
        """
        return pulumi.get(self, "managed_identities")

    @property
    @pulumi.getter(name="maximumNodes")
    def maximum_nodes(self) -> Optional[float]:
        """
        The maximum number of nodes where Service Fabric will reserve capacity for this application. Note that this does not mean that the services of this application will be placed on all of those nodes. By default, the value of this property is zero and it means that the services can be placed on any node.
        """
        return pulumi.get(self, "maximum_nodes")

    @property
    @pulumi.getter
    def metrics(self) -> Optional[Sequence['outputs.ApplicationMetricDescriptionResponse']]:
        """
        List of application capacity metric description.
        """
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter(name="minimumNodes")
    def minimum_nodes(self) -> Optional[float]:
        """
        The minimum number of nodes where Service Fabric will reserve capacity for this application. Note that this does not mean that the services of this application will be placed on all of those nodes. If this property is set to zero, no capacity will be reserved. The value of this property cannot be more than the value of the MaximumNodes property.
        """
        return pulumi.get(self, "minimum_nodes")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, str]]:
        """
        List of application parameters with overridden values from their default values specified in the application manifest.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current deployment or provisioning state, which only appears in the response
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="removeApplicationCapacity")
    def remove_application_capacity(self) -> Optional[bool]:
        """
        Remove the current application capacity settings.
        """
        return pulumi.get(self, "remove_application_capacity")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Azure resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[str]:
        """
        The application type name as defined in the application manifest.
        """
        return pulumi.get(self, "type_name")

    @property
    @pulumi.getter(name="typeVersion")
    def type_version(self) -> Optional[str]:
        """
        The version of the application type as defined in the application manifest.
        """
        return pulumi.get(self, "type_version")

    @property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> Optional['outputs.ApplicationUpgradePolicyResponse']:
        """
        Describes the policy for a monitored application upgrade.
        """
        return pulumi.get(self, "upgrade_policy")


class AwaitableGetApplicationResult(GetApplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationResult(
            etag=self.etag,
            id=self.id,
            identity=self.identity,
            location=self.location,
            managed_identities=self.managed_identities,
            maximum_nodes=self.maximum_nodes,
            metrics=self.metrics,
            minimum_nodes=self.minimum_nodes,
            name=self.name,
            parameters=self.parameters,
            provisioning_state=self.provisioning_state,
            remove_application_capacity=self.remove_application_capacity,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            type_name=self.type_name,
            type_version=self.type_version,
            upgrade_policy=self.upgrade_policy)


def get_application(application_name: Optional[str] = None,
                    cluster_name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationResult:
    """
    The application resource.


    :param str application_name: The name of the application resource.
    :param str cluster_name: The name of the cluster resource.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['applicationName'] = application_name
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicefabric/v20201201preview:getApplication', __args__, opts=opts, typ=GetApplicationResult).value

    return AwaitableGetApplicationResult(
        etag=__ret__.etag,
        id=__ret__.id,
        identity=__ret__.identity,
        location=__ret__.location,
        managed_identities=__ret__.managed_identities,
        maximum_nodes=__ret__.maximum_nodes,
        metrics=__ret__.metrics,
        minimum_nodes=__ret__.minimum_nodes,
        name=__ret__.name,
        parameters=__ret__.parameters,
        provisioning_state=__ret__.provisioning_state,
        remove_application_capacity=__ret__.remove_application_capacity,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type,
        type_name=__ret__.type_name,
        type_version=__ret__.type_version,
        upgrade_policy=__ret__.upgrade_policy)


@_utilities.lift_output_func(get_application)
def get_application_output(application_name: Optional[pulumi.Input[str]] = None,
                           cluster_name: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationResult]:
    """
    The application resource.


    :param str application_name: The name of the application resource.
    :param str cluster_name: The name of the cluster resource.
    :param str resource_group_name: The name of the resource group.
    """
    ...
