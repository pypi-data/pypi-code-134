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
    'GetInstanceResult',
    'AwaitableGetInstanceResult',
    'get_instance',
    'get_instance_output',
]

@pulumi.output_type
class GetInstanceResult:
    """
    Device Update instance details.
    """
    def __init__(__self__, account_name=None, diagnostic_storage_properties=None, enable_diagnostics=None, id=None, iot_hubs=None, location=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if account_name and not isinstance(account_name, str):
            raise TypeError("Expected argument 'account_name' to be a str")
        pulumi.set(__self__, "account_name", account_name)
        if diagnostic_storage_properties and not isinstance(diagnostic_storage_properties, dict):
            raise TypeError("Expected argument 'diagnostic_storage_properties' to be a dict")
        pulumi.set(__self__, "diagnostic_storage_properties", diagnostic_storage_properties)
        if enable_diagnostics and not isinstance(enable_diagnostics, bool):
            raise TypeError("Expected argument 'enable_diagnostics' to be a bool")
        pulumi.set(__self__, "enable_diagnostics", enable_diagnostics)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if iot_hubs and not isinstance(iot_hubs, list):
            raise TypeError("Expected argument 'iot_hubs' to be a list")
        pulumi.set(__self__, "iot_hubs", iot_hubs)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> str:
        """
        Parent Device Update Account name which Instance belongs to.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="diagnosticStorageProperties")
    def diagnostic_storage_properties(self) -> Optional['outputs.DiagnosticStoragePropertiesResponse']:
        """
        Customer-initiated diagnostic log collection storage properties
        """
        return pulumi.get(self, "diagnostic_storage_properties")

    @property
    @pulumi.getter(name="enableDiagnostics")
    def enable_diagnostics(self) -> Optional[bool]:
        """
        Enables or Disables the diagnostic logs collection
        """
        return pulumi.get(self, "enable_diagnostics")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="iotHubs")
    def iot_hubs(self) -> Optional[Sequence['outputs.IotHubSettingsResponse']]:
        """
        List of IoT Hubs associated with the account.
        """
        return pulumi.get(self, "iot_hubs")

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state.
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
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetInstanceResult(GetInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceResult(
            account_name=self.account_name,
            diagnostic_storage_properties=self.diagnostic_storage_properties,
            enable_diagnostics=self.enable_diagnostics,
            id=self.id,
            iot_hubs=self.iot_hubs,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_instance(account_name: Optional[str] = None,
                 instance_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceResult:
    """
    Device Update instance details.


    :param str account_name: Account name.
    :param str instance_name: Instance name.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['instanceName'] = instance_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:deviceupdate/v20220401preview:getInstance', __args__, opts=opts, typ=GetInstanceResult).value

    return AwaitableGetInstanceResult(
        account_name=__ret__.account_name,
        diagnostic_storage_properties=__ret__.diagnostic_storage_properties,
        enable_diagnostics=__ret__.enable_diagnostics,
        id=__ret__.id,
        iot_hubs=__ret__.iot_hubs,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_instance)
def get_instance_output(account_name: Optional[pulumi.Input[str]] = None,
                        instance_name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceResult]:
    """
    Device Update instance details.


    :param str account_name: Account name.
    :param str instance_name: Instance name.
    :param str resource_group_name: The resource group name.
    """
    ...
