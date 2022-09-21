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
    'GetManagedInstanceKeyResult',
    'AwaitableGetManagedInstanceKeyResult',
    'get_managed_instance_key',
    'get_managed_instance_key_output',
]

@pulumi.output_type
class GetManagedInstanceKeyResult:
    """
    A managed instance key.
    """
    def __init__(__self__, auto_rotation_enabled=None, creation_date=None, id=None, kind=None, name=None, thumbprint=None, type=None):
        if auto_rotation_enabled and not isinstance(auto_rotation_enabled, bool):
            raise TypeError("Expected argument 'auto_rotation_enabled' to be a bool")
        pulumi.set(__self__, "auto_rotation_enabled", auto_rotation_enabled)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if thumbprint and not isinstance(thumbprint, str):
            raise TypeError("Expected argument 'thumbprint' to be a str")
        pulumi.set(__self__, "thumbprint", thumbprint)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="autoRotationEnabled")
    def auto_rotation_enabled(self) -> bool:
        """
        Key auto rotation opt-in flag. Either true or false.
        """
        return pulumi.get(self, "auto_rotation_enabled")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> str:
        """
        The key creation date.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of encryption protector. This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def thumbprint(self) -> str:
        """
        Thumbprint of the key.
        """
        return pulumi.get(self, "thumbprint")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetManagedInstanceKeyResult(GetManagedInstanceKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedInstanceKeyResult(
            auto_rotation_enabled=self.auto_rotation_enabled,
            creation_date=self.creation_date,
            id=self.id,
            kind=self.kind,
            name=self.name,
            thumbprint=self.thumbprint,
            type=self.type)


def get_managed_instance_key(key_name: Optional[str] = None,
                             managed_instance_name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedInstanceKeyResult:
    """
    A managed instance key.


    :param str key_name: The name of the managed instance key to be retrieved.
    :param str managed_instance_name: The name of the managed instance.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    __args__ = dict()
    __args__['keyName'] = key_name
    __args__['managedInstanceName'] = managed_instance_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20210501preview:getManagedInstanceKey', __args__, opts=opts, typ=GetManagedInstanceKeyResult).value

    return AwaitableGetManagedInstanceKeyResult(
        auto_rotation_enabled=__ret__.auto_rotation_enabled,
        creation_date=__ret__.creation_date,
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        thumbprint=__ret__.thumbprint,
        type=__ret__.type)


@_utilities.lift_output_func(get_managed_instance_key)
def get_managed_instance_key_output(key_name: Optional[pulumi.Input[str]] = None,
                                    managed_instance_name: Optional[pulumi.Input[str]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedInstanceKeyResult]:
    """
    A managed instance key.


    :param str key_name: The name of the managed instance key to be retrieved.
    :param str managed_instance_name: The name of the managed instance.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    ...
