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
    'GetActiveSessionsResult',
    'AwaitableGetActiveSessionsResult',
    'get_active_sessions',
    'get_active_sessions_output',
]

@pulumi.output_type
class GetActiveSessionsResult:
    """
    Response for GetActiveSessions.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        The URL to get the next set of results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.BastionActiveSessionResponse']]:
        """
        List of active sessions on the bastion.
        """
        return pulumi.get(self, "value")


class AwaitableGetActiveSessionsResult(GetActiveSessionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetActiveSessionsResult(
            next_link=self.next_link,
            value=self.value)


def get_active_sessions(bastion_host_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetActiveSessionsResult:
    """
    Response for GetActiveSessions.


    :param str bastion_host_name: The name of the Bastion Host.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['bastionHostName'] = bastion_host_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20200701:getActiveSessions', __args__, opts=opts, typ=GetActiveSessionsResult).value

    return AwaitableGetActiveSessionsResult(
        next_link=__ret__.next_link,
        value=__ret__.value)


@_utilities.lift_output_func(get_active_sessions)
def get_active_sessions_output(bastion_host_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetActiveSessionsResult]:
    """
    Response for GetActiveSessions.


    :param str bastion_host_name: The name of the Bastion Host.
    :param str resource_group_name: The name of the resource group.
    """
    ...
