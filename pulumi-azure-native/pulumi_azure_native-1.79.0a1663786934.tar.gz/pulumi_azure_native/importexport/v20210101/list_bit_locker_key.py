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
    'ListBitLockerKeyResult',
    'AwaitableListBitLockerKeyResult',
    'list_bit_locker_key',
    'list_bit_locker_key_output',
]

@pulumi.output_type
class ListBitLockerKeyResult:
    """
    GetBitLockerKeys response
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.DriveBitLockerKeyResponse']]:
        """
        drive status
        """
        return pulumi.get(self, "value")


class AwaitableListBitLockerKeyResult(ListBitLockerKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListBitLockerKeyResult(
            value=self.value)


def list_bit_locker_key(job_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListBitLockerKeyResult:
    """
    GetBitLockerKeys response


    :param str job_name: The name of the import/export job.
    :param str resource_group_name: The resource group name uniquely identifies the resource group within the user subscription.
    """
    __args__ = dict()
    __args__['jobName'] = job_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:importexport/v20210101:listBitLockerKey', __args__, opts=opts, typ=ListBitLockerKeyResult).value

    return AwaitableListBitLockerKeyResult(
        value=__ret__.value)


@_utilities.lift_output_func(list_bit_locker_key)
def list_bit_locker_key_output(job_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListBitLockerKeyResult]:
    """
    GetBitLockerKeys response


    :param str job_name: The name of the import/export job.
    :param str resource_group_name: The resource group name uniquely identifies the resource group within the user subscription.
    """
    ...
