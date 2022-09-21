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
    'GetUserResult',
    'AwaitableGetUserResult',
    'get_user',
    'get_user_output',
]

warnings.warn("""Version 2019-07-01 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetUserResult:
    """
    Represents a user who has access to one or more shares on the Data Box Edge/Gateway device.
    """
    def __init__(__self__, encrypted_password=None, id=None, name=None, share_access_rights=None, type=None):
        if encrypted_password and not isinstance(encrypted_password, dict):
            raise TypeError("Expected argument 'encrypted_password' to be a dict")
        pulumi.set(__self__, "encrypted_password", encrypted_password)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if share_access_rights and not isinstance(share_access_rights, list):
            raise TypeError("Expected argument 'share_access_rights' to be a list")
        pulumi.set(__self__, "share_access_rights", share_access_rights)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="encryptedPassword")
    def encrypted_password(self) -> Optional['outputs.AsymmetricEncryptedSecretResponse']:
        """
        The password details.
        """
        return pulumi.get(self, "encrypted_password")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="shareAccessRights")
    def share_access_rights(self) -> Optional[Sequence['outputs.ShareAccessRightResponse']]:
        """
        List of shares that the user has rights on. This field should not be specified during user creation.
        """
        return pulumi.get(self, "share_access_rights")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")


class AwaitableGetUserResult(GetUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserResult(
            encrypted_password=self.encrypted_password,
            id=self.id,
            name=self.name,
            share_access_rights=self.share_access_rights,
            type=self.type)


def get_user(device_name: Optional[str] = None,
             name: Optional[str] = None,
             resource_group_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserResult:
    """
    Represents a user who has access to one or more shares on the Data Box Edge/Gateway device.


    :param str device_name: The device name.
    :param str name: The user name.
    :param str resource_group_name: The resource group name.
    """
    pulumi.log.warn("""get_user is deprecated: Version 2019-07-01 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:databoxedge/v20190701:getUser', __args__, opts=opts, typ=GetUserResult).value

    return AwaitableGetUserResult(
        encrypted_password=__ret__.encrypted_password,
        id=__ret__.id,
        name=__ret__.name,
        share_access_rights=__ret__.share_access_rights,
        type=__ret__.type)


@_utilities.lift_output_func(get_user)
def get_user_output(device_name: Optional[pulumi.Input[str]] = None,
                    name: Optional[pulumi.Input[str]] = None,
                    resource_group_name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserResult]:
    """
    Represents a user who has access to one or more shares on the Data Box Edge/Gateway device.


    :param str device_name: The device name.
    :param str name: The user name.
    :param str resource_group_name: The resource group name.
    """
    pulumi.log.warn("""get_user is deprecated: Version 2019-07-01 will be removed in v2 of the provider.""")
    ...
