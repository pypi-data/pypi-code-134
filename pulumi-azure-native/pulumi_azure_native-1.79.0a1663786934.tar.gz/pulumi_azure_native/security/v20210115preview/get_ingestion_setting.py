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
    'GetIngestionSettingResult',
    'AwaitableGetIngestionSettingResult',
    'get_ingestion_setting',
    'get_ingestion_setting_output',
]

@pulumi.output_type
class GetIngestionSettingResult:
    """
    Configures how to correlate scan data and logs with resources associated with the subscription.
    """
    def __init__(__self__, id=None, name=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetIngestionSettingResult(GetIngestionSettingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIngestionSettingResult(
            id=self.id,
            name=self.name,
            type=self.type)


def get_ingestion_setting(ingestion_setting_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIngestionSettingResult:
    """
    Configures how to correlate scan data and logs with resources associated with the subscription.


    :param str ingestion_setting_name: Name of the ingestion setting
    """
    __args__ = dict()
    __args__['ingestionSettingName'] = ingestion_setting_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:security/v20210115preview:getIngestionSetting', __args__, opts=opts, typ=GetIngestionSettingResult).value

    return AwaitableGetIngestionSettingResult(
        id=__ret__.id,
        name=__ret__.name,
        type=__ret__.type)


@_utilities.lift_output_func(get_ingestion_setting)
def get_ingestion_setting_output(ingestion_setting_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIngestionSettingResult]:
    """
    Configures how to correlate scan data and logs with resources associated with the subscription.


    :param str ingestion_setting_name: Name of the ingestion setting
    """
    ...
