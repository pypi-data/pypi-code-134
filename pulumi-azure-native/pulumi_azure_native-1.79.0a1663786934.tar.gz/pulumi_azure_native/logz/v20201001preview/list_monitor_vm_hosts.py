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
    'ListMonitorVMHostsResult',
    'AwaitableListMonitorVMHostsResult',
    'list_monitor_vm_hosts',
    'list_monitor_vm_hosts_output',
]

@pulumi.output_type
class ListMonitorVMHostsResult:
    """
    Response of a list VM Host Update Operation.
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
        Link to the next set of results, if any.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.VMResourcesResponse']]:
        """
        Response of a list vm host update operation.
        """
        return pulumi.get(self, "value")


class AwaitableListMonitorVMHostsResult(ListMonitorVMHostsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListMonitorVMHostsResult(
            next_link=self.next_link,
            value=self.value)


def list_monitor_vm_hosts(monitor_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListMonitorVMHostsResult:
    """
    Response of a list VM Host Update Operation.


    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['monitorName'] = monitor_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:logz/v20201001preview:listMonitorVMHosts', __args__, opts=opts, typ=ListMonitorVMHostsResult).value

    return AwaitableListMonitorVMHostsResult(
        next_link=__ret__.next_link,
        value=__ret__.value)


@_utilities.lift_output_func(list_monitor_vm_hosts)
def list_monitor_vm_hosts_output(monitor_name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListMonitorVMHostsResult]:
    """
    Response of a list VM Host Update Operation.


    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
