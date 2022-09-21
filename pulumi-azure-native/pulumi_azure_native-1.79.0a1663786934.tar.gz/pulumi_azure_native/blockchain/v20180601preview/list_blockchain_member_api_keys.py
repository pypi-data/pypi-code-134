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
    'ListBlockchainMemberApiKeysResult',
    'AwaitableListBlockchainMemberApiKeysResult',
    'list_blockchain_member_api_keys',
    'list_blockchain_member_api_keys_output',
]

@pulumi.output_type
class ListBlockchainMemberApiKeysResult:
    """
    Collection of the API key payload which is exposed in the response of the resource provider.
    """
    def __init__(__self__, keys=None):
        if keys and not isinstance(keys, list):
            raise TypeError("Expected argument 'keys' to be a list")
        pulumi.set(__self__, "keys", keys)

    @property
    @pulumi.getter
    def keys(self) -> Optional[Sequence['outputs.ApiKeyResponse']]:
        """
        Gets or sets the collection of API key.
        """
        return pulumi.get(self, "keys")


class AwaitableListBlockchainMemberApiKeysResult(ListBlockchainMemberApiKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListBlockchainMemberApiKeysResult(
            keys=self.keys)


def list_blockchain_member_api_keys(blockchain_member_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListBlockchainMemberApiKeysResult:
    """
    Collection of the API key payload which is exposed in the response of the resource provider.


    :param str blockchain_member_name: Blockchain member name.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    __args__ = dict()
    __args__['blockchainMemberName'] = blockchain_member_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:blockchain/v20180601preview:listBlockchainMemberApiKeys', __args__, opts=opts, typ=ListBlockchainMemberApiKeysResult).value

    return AwaitableListBlockchainMemberApiKeysResult(
        keys=__ret__.keys)


@_utilities.lift_output_func(list_blockchain_member_api_keys)
def list_blockchain_member_api_keys_output(blockchain_member_name: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListBlockchainMemberApiKeysResult]:
    """
    Collection of the API key payload which is exposed in the response of the resource provider.


    :param str blockchain_member_name: Blockchain member name.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    ...
