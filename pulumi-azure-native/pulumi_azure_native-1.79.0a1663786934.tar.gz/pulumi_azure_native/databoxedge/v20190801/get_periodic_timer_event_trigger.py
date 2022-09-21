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
    'GetPeriodicTimerEventTriggerResult',
    'AwaitableGetPeriodicTimerEventTriggerResult',
    'get_periodic_timer_event_trigger',
    'get_periodic_timer_event_trigger_output',
]

@pulumi.output_type
class GetPeriodicTimerEventTriggerResult:
    """
    Trigger details.
    """
    def __init__(__self__, custom_context_tag=None, id=None, kind=None, name=None, sink_info=None, source_info=None, type=None):
        if custom_context_tag and not isinstance(custom_context_tag, str):
            raise TypeError("Expected argument 'custom_context_tag' to be a str")
        pulumi.set(__self__, "custom_context_tag", custom_context_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sink_info and not isinstance(sink_info, dict):
            raise TypeError("Expected argument 'sink_info' to be a dict")
        pulumi.set(__self__, "sink_info", sink_info)
        if source_info and not isinstance(source_info, dict):
            raise TypeError("Expected argument 'source_info' to be a dict")
        pulumi.set(__self__, "source_info", source_info)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="customContextTag")
    def custom_context_tag(self) -> Optional[str]:
        """
        A custom context tag typically used to correlate the trigger against its usage. For example, if a periodic timer trigger is intended for certain specific IoT modules in the device, the tag can be the name or the image URL of the module.
        """
        return pulumi.get(self, "custom_context_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Trigger Kind.
        Expected value is 'PeriodicTimerEvent'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sinkInfo")
    def sink_info(self) -> 'outputs.RoleSinkInfoResponse':
        """
        Role Sink information.
        """
        return pulumi.get(self, "sink_info")

    @property
    @pulumi.getter(name="sourceInfo")
    def source_info(self) -> 'outputs.PeriodicTimerSourceInfoResponse':
        """
        Periodic timer details.
        """
        return pulumi.get(self, "source_info")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")


class AwaitableGetPeriodicTimerEventTriggerResult(GetPeriodicTimerEventTriggerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPeriodicTimerEventTriggerResult(
            custom_context_tag=self.custom_context_tag,
            id=self.id,
            kind=self.kind,
            name=self.name,
            sink_info=self.sink_info,
            source_info=self.source_info,
            type=self.type)


def get_periodic_timer_event_trigger(device_name: Optional[str] = None,
                                     name: Optional[str] = None,
                                     resource_group_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPeriodicTimerEventTriggerResult:
    """
    Trigger details.


    :param str device_name: The device name.
    :param str name: The trigger name.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:databoxedge/v20190801:getPeriodicTimerEventTrigger', __args__, opts=opts, typ=GetPeriodicTimerEventTriggerResult).value

    return AwaitableGetPeriodicTimerEventTriggerResult(
        custom_context_tag=__ret__.custom_context_tag,
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        sink_info=__ret__.sink_info,
        source_info=__ret__.source_info,
        type=__ret__.type)


@_utilities.lift_output_func(get_periodic_timer_event_trigger)
def get_periodic_timer_event_trigger_output(device_name: Optional[pulumi.Input[str]] = None,
                                            name: Optional[pulumi.Input[str]] = None,
                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPeriodicTimerEventTriggerResult]:
    """
    Trigger details.


    :param str device_name: The device name.
    :param str name: The trigger name.
    :param str resource_group_name: The resource group name.
    """
    ...
