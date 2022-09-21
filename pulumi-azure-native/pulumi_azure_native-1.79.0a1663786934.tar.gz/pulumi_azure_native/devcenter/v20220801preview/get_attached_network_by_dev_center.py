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
    'GetAttachedNetworkByDevCenterResult',
    'AwaitableGetAttachedNetworkByDevCenterResult',
    'get_attached_network_by_dev_center',
    'get_attached_network_by_dev_center_output',
]

@pulumi.output_type
class GetAttachedNetworkByDevCenterResult:
    """
    Represents an attached NetworkConnection.
    """
    def __init__(__self__, domain_join_type=None, health_check_status=None, id=None, name=None, network_connection_id=None, network_connection_location=None, provisioning_state=None, system_data=None, type=None):
        if domain_join_type and not isinstance(domain_join_type, str):
            raise TypeError("Expected argument 'domain_join_type' to be a str")
        pulumi.set(__self__, "domain_join_type", domain_join_type)
        if health_check_status and not isinstance(health_check_status, str):
            raise TypeError("Expected argument 'health_check_status' to be a str")
        pulumi.set(__self__, "health_check_status", health_check_status)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_connection_id and not isinstance(network_connection_id, str):
            raise TypeError("Expected argument 'network_connection_id' to be a str")
        pulumi.set(__self__, "network_connection_id", network_connection_id)
        if network_connection_location and not isinstance(network_connection_location, str):
            raise TypeError("Expected argument 'network_connection_location' to be a str")
        pulumi.set(__self__, "network_connection_location", network_connection_location)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="domainJoinType")
    def domain_join_type(self) -> str:
        """
        AAD Join type of the network. This is populated based on the referenced Network Connection.
        """
        return pulumi.get(self, "domain_join_type")

    @property
    @pulumi.getter(name="healthCheckStatus")
    def health_check_status(self) -> str:
        """
        Health check status values
        """
        return pulumi.get(self, "health_check_status")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkConnectionId")
    def network_connection_id(self) -> str:
        """
        The resource ID of the NetworkConnection you want to attach.
        """
        return pulumi.get(self, "network_connection_id")

    @property
    @pulumi.getter(name="networkConnectionLocation")
    def network_connection_location(self) -> str:
        """
        The geo-location where the NetworkConnection resource specified in 'networkConnectionResourceId' property lives.
        """
        return pulumi.get(self, "network_connection_location")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAttachedNetworkByDevCenterResult(GetAttachedNetworkByDevCenterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAttachedNetworkByDevCenterResult(
            domain_join_type=self.domain_join_type,
            health_check_status=self.health_check_status,
            id=self.id,
            name=self.name,
            network_connection_id=self.network_connection_id,
            network_connection_location=self.network_connection_location,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_attached_network_by_dev_center(attached_network_connection_name: Optional[str] = None,
                                       dev_center_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAttachedNetworkByDevCenterResult:
    """
    Represents an attached NetworkConnection.


    :param str attached_network_connection_name: The name of the attached NetworkConnection.
    :param str dev_center_name: The name of the devcenter.
    :param str resource_group_name: Name of the resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['attachedNetworkConnectionName'] = attached_network_connection_name
    __args__['devCenterName'] = dev_center_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devcenter/v20220801preview:getAttachedNetworkByDevCenter', __args__, opts=opts, typ=GetAttachedNetworkByDevCenterResult).value

    return AwaitableGetAttachedNetworkByDevCenterResult(
        domain_join_type=__ret__.domain_join_type,
        health_check_status=__ret__.health_check_status,
        id=__ret__.id,
        name=__ret__.name,
        network_connection_id=__ret__.network_connection_id,
        network_connection_location=__ret__.network_connection_location,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_attached_network_by_dev_center)
def get_attached_network_by_dev_center_output(attached_network_connection_name: Optional[pulumi.Input[str]] = None,
                                              dev_center_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAttachedNetworkByDevCenterResult]:
    """
    Represents an attached NetworkConnection.


    :param str attached_network_connection_name: The name of the attached NetworkConnection.
    :param str dev_center_name: The name of the devcenter.
    :param str resource_group_name: Name of the resource group within the Azure subscription.
    """
    ...
