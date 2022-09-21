# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetAccountsResult',
    'AwaitableGetAccountsResult',
    'get_accounts',
    'get_accounts_output',
]

@pulumi.output_type
class GetAccountsResult:
    """
    A collection of values returned by getAccounts.
    """
    def __init__(__self__, accounts=None, id=None, name=None):
        if accounts and not isinstance(accounts, list):
            raise TypeError("Expected argument 'accounts' to be a list")
        pulumi.set(__self__, "accounts", accounts)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def accounts(self) -> Sequence['outputs.GetAccountsAccountResult']:
        return pulumi.get(self, "accounts")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The account name to target for the resource.
        """
        return pulumi.get(self, "name")


class AwaitableGetAccountsResult(GetAccountsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountsResult(
            accounts=self.accounts,
            id=self.id,
            name=self.name)


def get_accounts(name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountsResult:
    """
    Data source for looking up Cloudflare Accounts.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cloudflare as cloudflare

    example = cloudflare.get_accounts(name="example account")
    ```


    :param str name: The account name to target for the resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getAccounts:getAccounts', __args__, opts=opts, typ=GetAccountsResult).value

    return AwaitableGetAccountsResult(
        accounts=__ret__.accounts,
        id=__ret__.id,
        name=__ret__.name)


@_utilities.lift_output_func(get_accounts)
def get_accounts_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccountsResult]:
    """
    Data source for looking up Cloudflare Accounts.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cloudflare as cloudflare

    example = cloudflare.get_accounts(name="example account")
    ```


    :param str name: The account name to target for the resource.
    """
    ...
