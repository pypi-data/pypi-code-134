# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ListDelegationSettingSecretsResult',
    'AwaitableListDelegationSettingSecretsResult',
    'list_delegation_setting_secrets',
    'list_delegation_setting_secrets_output',
]

@pulumi.output_type
class ListDelegationSettingSecretsResult:
    """
    Client or app secret used in IdentityProviders, Aad, OpenID or OAuth.
    """
    def __init__(__self__, validation_key=None):
        if validation_key and not isinstance(validation_key, str):
            raise TypeError("Expected argument 'validation_key' to be a str")
        pulumi.set(__self__, "validation_key", validation_key)

    @property
    @pulumi.getter(name="validationKey")
    def validation_key(self) -> Optional[str]:
        """
        This is secret value of the validation key in portal settings.
        """
        return pulumi.get(self, "validation_key")


class AwaitableListDelegationSettingSecretsResult(ListDelegationSettingSecretsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListDelegationSettingSecretsResult(
            validation_key=self.validation_key)


def list_delegation_setting_secrets(resource_group_name: Optional[str] = None,
                                    service_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListDelegationSettingSecretsResult:
    """
    Client or app secret used in IdentityProviders, Aad, OpenID or OAuth.
    API Version: 2020-12-01.


    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement:listDelegationSettingSecrets', __args__, opts=opts, typ=ListDelegationSettingSecretsResult).value

    return AwaitableListDelegationSettingSecretsResult(
        validation_key=__ret__.validation_key)


@_utilities.lift_output_func(list_delegation_setting_secrets)
def list_delegation_setting_secrets_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                           service_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListDelegationSettingSecretsResult]:
    """
    Client or app secret used in IdentityProviders, Aad, OpenID or OAuth.
    API Version: 2020-12-01.


    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    ...
