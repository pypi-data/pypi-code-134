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
from ._enums import *
from ._inputs import *

__all__ = ['ConnectionMonitorArgs', 'ConnectionMonitor']

@pulumi.input_type
class ConnectionMonitorArgs:
    def __init__(__self__, *,
                 network_watcher_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 auto_start: Optional[pulumi.Input[bool]] = None,
                 connection_monitor_name: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input['ConnectionMonitorDestinationArgs']] = None,
                 endpoints: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorEndpointArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 migrate: Optional[pulumi.Input[str]] = None,
                 monitoring_interval_in_seconds: Optional[pulumi.Input[int]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 outputs: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorOutputArgs']]]] = None,
                 source: Optional[pulumi.Input['ConnectionMonitorSourceArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 test_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorTestConfigurationArgs']]]] = None,
                 test_groups: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorTestGroupArgs']]]] = None):
        """
        The set of arguments for constructing a ConnectionMonitor resource.
        :param pulumi.Input[str] network_watcher_name: The name of the Network Watcher resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing Network Watcher.
        :param pulumi.Input[bool] auto_start: Determines if the connection monitor will start automatically once created.
        :param pulumi.Input[str] connection_monitor_name: The name of the connection monitor.
        :param pulumi.Input['ConnectionMonitorDestinationArgs'] destination: Describes the destination of connection monitor.
        :param pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorEndpointArgs']]] endpoints: List of connection monitor endpoints.
        :param pulumi.Input[str] location: Connection monitor location.
        :param pulumi.Input[str] migrate: Value indicating whether connection monitor V1 should be migrated to V2 format.
        :param pulumi.Input[int] monitoring_interval_in_seconds: Monitoring interval in seconds.
        :param pulumi.Input[str] notes: Optional notes to be associated with the connection monitor.
        :param pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorOutputArgs']]] outputs: List of connection monitor outputs.
        :param pulumi.Input['ConnectionMonitorSourceArgs'] source: Describes the source of connection monitor.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Connection monitor tags.
        :param pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorTestConfigurationArgs']]] test_configurations: List of connection monitor test configurations.
        :param pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorTestGroupArgs']]] test_groups: List of connection monitor test groups.
        """
        pulumi.set(__self__, "network_watcher_name", network_watcher_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if auto_start is None:
            auto_start = True
        if auto_start is not None:
            pulumi.set(__self__, "auto_start", auto_start)
        if connection_monitor_name is not None:
            pulumi.set(__self__, "connection_monitor_name", connection_monitor_name)
        if destination is not None:
            pulumi.set(__self__, "destination", destination)
        if endpoints is not None:
            pulumi.set(__self__, "endpoints", endpoints)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if migrate is not None:
            pulumi.set(__self__, "migrate", migrate)
        if monitoring_interval_in_seconds is None:
            monitoring_interval_in_seconds = 60
        if monitoring_interval_in_seconds is not None:
            pulumi.set(__self__, "monitoring_interval_in_seconds", monitoring_interval_in_seconds)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if outputs is not None:
            pulumi.set(__self__, "outputs", outputs)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if test_configurations is not None:
            pulumi.set(__self__, "test_configurations", test_configurations)
        if test_groups is not None:
            pulumi.set(__self__, "test_groups", test_groups)

    @property
    @pulumi.getter(name="networkWatcherName")
    def network_watcher_name(self) -> pulumi.Input[str]:
        """
        The name of the Network Watcher resource.
        """
        return pulumi.get(self, "network_watcher_name")

    @network_watcher_name.setter
    def network_watcher_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_watcher_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group containing Network Watcher.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="autoStart")
    def auto_start(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines if the connection monitor will start automatically once created.
        """
        return pulumi.get(self, "auto_start")

    @auto_start.setter
    def auto_start(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_start", value)

    @property
    @pulumi.getter(name="connectionMonitorName")
    def connection_monitor_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the connection monitor.
        """
        return pulumi.get(self, "connection_monitor_name")

    @connection_monitor_name.setter
    def connection_monitor_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_monitor_name", value)

    @property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input['ConnectionMonitorDestinationArgs']]:
        """
        Describes the destination of connection monitor.
        """
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: Optional[pulumi.Input['ConnectionMonitorDestinationArgs']]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter
    def endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorEndpointArgs']]]]:
        """
        List of connection monitor endpoints.
        """
        return pulumi.get(self, "endpoints")

    @endpoints.setter
    def endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorEndpointArgs']]]]):
        pulumi.set(self, "endpoints", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Connection monitor location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def migrate(self) -> Optional[pulumi.Input[str]]:
        """
        Value indicating whether connection monitor V1 should be migrated to V2 format.
        """
        return pulumi.get(self, "migrate")

    @migrate.setter
    def migrate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "migrate", value)

    @property
    @pulumi.getter(name="monitoringIntervalInSeconds")
    def monitoring_interval_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Monitoring interval in seconds.
        """
        return pulumi.get(self, "monitoring_interval_in_seconds")

    @monitoring_interval_in_seconds.setter
    def monitoring_interval_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "monitoring_interval_in_seconds", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        """
        Optional notes to be associated with the connection monitor.
        """
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter
    def outputs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorOutputArgs']]]]:
        """
        List of connection monitor outputs.
        """
        return pulumi.get(self, "outputs")

    @outputs.setter
    def outputs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorOutputArgs']]]]):
        pulumi.set(self, "outputs", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input['ConnectionMonitorSourceArgs']]:
        """
        Describes the source of connection monitor.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input['ConnectionMonitorSourceArgs']]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Connection monitor tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="testConfigurations")
    def test_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorTestConfigurationArgs']]]]:
        """
        List of connection monitor test configurations.
        """
        return pulumi.get(self, "test_configurations")

    @test_configurations.setter
    def test_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorTestConfigurationArgs']]]]):
        pulumi.set(self, "test_configurations", value)

    @property
    @pulumi.getter(name="testGroups")
    def test_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorTestGroupArgs']]]]:
        """
        List of connection monitor test groups.
        """
        return pulumi.get(self, "test_groups")

    @test_groups.setter
    def test_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionMonitorTestGroupArgs']]]]):
        pulumi.set(self, "test_groups", value)


class ConnectionMonitor(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_start: Optional[pulumi.Input[bool]] = None,
                 connection_monitor_name: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[pulumi.InputType['ConnectionMonitorDestinationArgs']]] = None,
                 endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionMonitorEndpointArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 migrate: Optional[pulumi.Input[str]] = None,
                 monitoring_interval_in_seconds: Optional[pulumi.Input[int]] = None,
                 network_watcher_name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 outputs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionMonitorOutputArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['ConnectionMonitorSourceArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 test_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionMonitorTestConfigurationArgs']]]]] = None,
                 test_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionMonitorTestGroupArgs']]]]] = None,
                 __props__=None):
        """
        Information about the connection monitor.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_start: Determines if the connection monitor will start automatically once created.
        :param pulumi.Input[str] connection_monitor_name: The name of the connection monitor.
        :param pulumi.Input[pulumi.InputType['ConnectionMonitorDestinationArgs']] destination: Describes the destination of connection monitor.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionMonitorEndpointArgs']]]] endpoints: List of connection monitor endpoints.
        :param pulumi.Input[str] location: Connection monitor location.
        :param pulumi.Input[str] migrate: Value indicating whether connection monitor V1 should be migrated to V2 format.
        :param pulumi.Input[int] monitoring_interval_in_seconds: Monitoring interval in seconds.
        :param pulumi.Input[str] network_watcher_name: The name of the Network Watcher resource.
        :param pulumi.Input[str] notes: Optional notes to be associated with the connection monitor.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionMonitorOutputArgs']]]] outputs: List of connection monitor outputs.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing Network Watcher.
        :param pulumi.Input[pulumi.InputType['ConnectionMonitorSourceArgs']] source: Describes the source of connection monitor.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Connection monitor tags.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionMonitorTestConfigurationArgs']]]] test_configurations: List of connection monitor test configurations.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionMonitorTestGroupArgs']]]] test_groups: List of connection monitor test groups.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectionMonitorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Information about the connection monitor.

        :param str resource_name: The name of the resource.
        :param ConnectionMonitorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectionMonitorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_start: Optional[pulumi.Input[bool]] = None,
                 connection_monitor_name: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[pulumi.InputType['ConnectionMonitorDestinationArgs']]] = None,
                 endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionMonitorEndpointArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 migrate: Optional[pulumi.Input[str]] = None,
                 monitoring_interval_in_seconds: Optional[pulumi.Input[int]] = None,
                 network_watcher_name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 outputs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionMonitorOutputArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['ConnectionMonitorSourceArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 test_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionMonitorTestConfigurationArgs']]]]] = None,
                 test_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionMonitorTestGroupArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectionMonitorArgs.__new__(ConnectionMonitorArgs)

            if auto_start is None:
                auto_start = True
            __props__.__dict__["auto_start"] = auto_start
            __props__.__dict__["connection_monitor_name"] = connection_monitor_name
            __props__.__dict__["destination"] = destination
            __props__.__dict__["endpoints"] = endpoints
            __props__.__dict__["location"] = location
            __props__.__dict__["migrate"] = migrate
            if monitoring_interval_in_seconds is None:
                monitoring_interval_in_seconds = 60
            __props__.__dict__["monitoring_interval_in_seconds"] = monitoring_interval_in_seconds
            if network_watcher_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_watcher_name'")
            __props__.__dict__["network_watcher_name"] = network_watcher_name
            __props__.__dict__["notes"] = notes
            __props__.__dict__["outputs"] = outputs
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["source"] = source
            __props__.__dict__["tags"] = tags
            __props__.__dict__["test_configurations"] = test_configurations
            __props__.__dict__["test_groups"] = test_groups
            __props__.__dict__["connection_monitor_type"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["monitoring_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["start_time"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20171001:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20171101:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20180101:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20180201:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20180401:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20180601:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20180701:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20180801:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20181001:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20181101:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20181201:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20190201:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20190401:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20190601:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20190701:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20190801:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20190901:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20191101:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20191201:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20200301:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20200401:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20200501:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20200601:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20200701:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20200801:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20210201:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20210301:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20210501:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20210801:ConnectionMonitor"), pulumi.Alias(type_="azure-native:network/v20220101:ConnectionMonitor")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ConnectionMonitor, __self__).__init__(
            'azure-native:network/v20201101:ConnectionMonitor',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConnectionMonitor':
        """
        Get an existing ConnectionMonitor resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectionMonitorArgs.__new__(ConnectionMonitorArgs)

        __props__.__dict__["auto_start"] = None
        __props__.__dict__["connection_monitor_type"] = None
        __props__.__dict__["destination"] = None
        __props__.__dict__["endpoints"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["monitoring_interval_in_seconds"] = None
        __props__.__dict__["monitoring_status"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notes"] = None
        __props__.__dict__["outputs"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["start_time"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["test_configurations"] = None
        __props__.__dict__["test_groups"] = None
        __props__.__dict__["type"] = None
        return ConnectionMonitor(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoStart")
    def auto_start(self) -> pulumi.Output[Optional[bool]]:
        """
        Determines if the connection monitor will start automatically once created.
        """
        return pulumi.get(self, "auto_start")

    @property
    @pulumi.getter(name="connectionMonitorType")
    def connection_monitor_type(self) -> pulumi.Output[str]:
        """
        Type of connection monitor.
        """
        return pulumi.get(self, "connection_monitor_type")

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Output[Optional['outputs.ConnectionMonitorDestinationResponse']]:
        """
        Describes the destination of connection monitor.
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[Optional[Sequence['outputs.ConnectionMonitorEndpointResponse']]]:
        """
        List of connection monitor endpoints.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Connection monitor location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="monitoringIntervalInSeconds")
    def monitoring_interval_in_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        Monitoring interval in seconds.
        """
        return pulumi.get(self, "monitoring_interval_in_seconds")

    @property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(self) -> pulumi.Output[str]:
        """
        The monitoring status of the connection monitor.
        """
        return pulumi.get(self, "monitoring_status")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the connection monitor.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[str]]:
        """
        Optional notes to be associated with the connection monitor.
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def outputs(self) -> pulumi.Output[Optional[Sequence['outputs.ConnectionMonitorOutputResponse']]]:
        """
        List of connection monitor outputs.
        """
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the connection monitor.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional['outputs.ConnectionMonitorSourceResponse']]:
        """
        Describes the source of connection monitor.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[str]:
        """
        The date and time when the connection monitor was started.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Connection monitor tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="testConfigurations")
    def test_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.ConnectionMonitorTestConfigurationResponse']]]:
        """
        List of connection monitor test configurations.
        """
        return pulumi.get(self, "test_configurations")

    @property
    @pulumi.getter(name="testGroups")
    def test_groups(self) -> pulumi.Output[Optional[Sequence['outputs.ConnectionMonitorTestGroupResponse']]]:
        """
        List of connection monitor test groups.
        """
        return pulumi.get(self, "test_groups")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Connection monitor type.
        """
        return pulumi.get(self, "type")

