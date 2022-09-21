# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetAddonResult',
    'AwaitableGetAddonResult',
    'get_addon',
    'get_addon_output',
]

@pulumi.output_type
class GetAddonResult:
    """
    An addon resource
    """
    def __init__(__self__, addon_type=None, id=None, license_key=None, name=None, provisioning_state=None, type=None):
        if addon_type and not isinstance(addon_type, str):
            raise TypeError("Expected argument 'addon_type' to be a str")
        pulumi.set(__self__, "addon_type", addon_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if license_key and not isinstance(license_key, str):
            raise TypeError("Expected argument 'license_key' to be a str")
        pulumi.set(__self__, "license_key", license_key)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="addonType")
    def addon_type(self) -> Optional[str]:
        """
        The type of private cloud addon
        """
        return pulumi.get(self, "addon_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> Optional[str]:
        """
        The SRM license
        """
        return pulumi.get(self, "license_key")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The state of the addon provisioning
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetAddonResult(GetAddonResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAddonResult(
            addon_type=self.addon_type,
            id=self.id,
            license_key=self.license_key,
            name=self.name,
            provisioning_state=self.provisioning_state,
            type=self.type)


def get_addon(addon_name: Optional[str] = None,
              private_cloud_name: Optional[str] = None,
              resource_group_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAddonResult:
    """
    An addon resource


    :param str addon_name: Name of the addon for the private cloud
    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['addonName'] = addon_name
    __args__['privateCloudName'] = private_cloud_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:avs/v20210101preview:getAddon', __args__, opts=opts, typ=GetAddonResult).value

    return AwaitableGetAddonResult(
        addon_type=__ret__.addon_type,
        id=__ret__.id,
        license_key=__ret__.license_key,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        type=__ret__.type)


@_utilities.lift_output_func(get_addon)
def get_addon_output(addon_name: Optional[pulumi.Input[str]] = None,
                     private_cloud_name: Optional[pulumi.Input[str]] = None,
                     resource_group_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAddonResult]:
    """
    An addon resource


    :param str addon_name: Name of the addon for the private cloud
    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
