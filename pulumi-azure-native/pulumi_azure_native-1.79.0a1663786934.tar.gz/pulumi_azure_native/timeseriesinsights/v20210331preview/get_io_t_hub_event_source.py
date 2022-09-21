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
    'GetIoTHubEventSourceResult',
    'AwaitableGetIoTHubEventSourceResult',
    'get_io_t_hub_event_source',
    'get_io_t_hub_event_source_output',
]

@pulumi.output_type
class GetIoTHubEventSourceResult:
    """
    An event source that receives its data from an Azure IoTHub.
    """
    def __init__(__self__, consumer_group_name=None, creation_time=None, event_source_resource_id=None, id=None, iot_hub_name=None, key_name=None, kind=None, local_timestamp=None, location=None, name=None, provisioning_state=None, tags=None, time=None, timestamp_property_name=None, type=None):
        if consumer_group_name and not isinstance(consumer_group_name, str):
            raise TypeError("Expected argument 'consumer_group_name' to be a str")
        pulumi.set(__self__, "consumer_group_name", consumer_group_name)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if event_source_resource_id and not isinstance(event_source_resource_id, str):
            raise TypeError("Expected argument 'event_source_resource_id' to be a str")
        pulumi.set(__self__, "event_source_resource_id", event_source_resource_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if iot_hub_name and not isinstance(iot_hub_name, str):
            raise TypeError("Expected argument 'iot_hub_name' to be a str")
        pulumi.set(__self__, "iot_hub_name", iot_hub_name)
        if key_name and not isinstance(key_name, str):
            raise TypeError("Expected argument 'key_name' to be a str")
        pulumi.set(__self__, "key_name", key_name)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if local_timestamp and not isinstance(local_timestamp, dict):
            raise TypeError("Expected argument 'local_timestamp' to be a dict")
        pulumi.set(__self__, "local_timestamp", local_timestamp)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if time and not isinstance(time, str):
            raise TypeError("Expected argument 'time' to be a str")
        pulumi.set(__self__, "time", time)
        if timestamp_property_name and not isinstance(timestamp_property_name, str):
            raise TypeError("Expected argument 'timestamp_property_name' to be a str")
        pulumi.set(__self__, "timestamp_property_name", timestamp_property_name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="consumerGroupName")
    def consumer_group_name(self) -> str:
        """
        The name of the iot hub's consumer group that holds the partitions from which events will be read.
        """
        return pulumi.get(self, "consumer_group_name")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        The time the resource was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="eventSourceResourceId")
    def event_source_resource_id(self) -> str:
        """
        The resource id of the event source in Azure Resource Manager.
        """
        return pulumi.get(self, "event_source_resource_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="iotHubName")
    def iot_hub_name(self) -> str:
        """
        The name of the iot hub.
        """
        return pulumi.get(self, "iot_hub_name")

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> str:
        """
        The name of the Shared Access Policy key that grants the Time Series Insights service access to the iot hub. This shared access policy key must grant 'service connect' permissions to the iot hub.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of the event source.
        Expected value is 'Microsoft.IoTHub'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="localTimestamp")
    def local_timestamp(self) -> Optional['outputs.LocalTimestampResponse']:
        """
        An object that represents the local timestamp property. It contains the format of local timestamp that needs to be used and the corresponding timezone offset information. If a value isn't specified for localTimestamp, or if null, then the local timestamp will not be ingressed with the events.
        """
        return pulumi.get(self, "local_timestamp")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def time(self) -> Optional[str]:
        """
        ISO8601 UTC datetime with seconds precision (milliseconds are optional), specifying the date and time that will be the starting point for Events to be consumed.
        """
        return pulumi.get(self, "time")

    @property
    @pulumi.getter(name="timestampPropertyName")
    def timestamp_property_name(self) -> Optional[str]:
        """
        The event property that will be used as the event source's timestamp. If a value isn't specified for timestampPropertyName, or if null or empty-string is specified, the event creation time will be used.
        """
        return pulumi.get(self, "timestamp_property_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetIoTHubEventSourceResult(GetIoTHubEventSourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIoTHubEventSourceResult(
            consumer_group_name=self.consumer_group_name,
            creation_time=self.creation_time,
            event_source_resource_id=self.event_source_resource_id,
            id=self.id,
            iot_hub_name=self.iot_hub_name,
            key_name=self.key_name,
            kind=self.kind,
            local_timestamp=self.local_timestamp,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            time=self.time,
            timestamp_property_name=self.timestamp_property_name,
            type=self.type)


def get_io_t_hub_event_source(environment_name: Optional[str] = None,
                              event_source_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIoTHubEventSourceResult:
    """
    An event source that receives its data from an Azure IoTHub.


    :param str environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :param str event_source_name: The name of the Time Series Insights event source associated with the specified environment.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    __args__ = dict()
    __args__['environmentName'] = environment_name
    __args__['eventSourceName'] = event_source_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:timeseriesinsights/v20210331preview:getIoTHubEventSource', __args__, opts=opts, typ=GetIoTHubEventSourceResult).value

    return AwaitableGetIoTHubEventSourceResult(
        consumer_group_name=__ret__.consumer_group_name,
        creation_time=__ret__.creation_time,
        event_source_resource_id=__ret__.event_source_resource_id,
        id=__ret__.id,
        iot_hub_name=__ret__.iot_hub_name,
        key_name=__ret__.key_name,
        kind=__ret__.kind,
        local_timestamp=__ret__.local_timestamp,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        tags=__ret__.tags,
        time=__ret__.time,
        timestamp_property_name=__ret__.timestamp_property_name,
        type=__ret__.type)


@_utilities.lift_output_func(get_io_t_hub_event_source)
def get_io_t_hub_event_source_output(environment_name: Optional[pulumi.Input[str]] = None,
                                     event_source_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIoTHubEventSourceResult]:
    """
    An event source that receives its data from an Azure IoTHub.


    :param str environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :param str event_source_name: The name of the Time Series Insights event source associated with the specified environment.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    ...
