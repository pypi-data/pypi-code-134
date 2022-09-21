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

__all__ = ['ScheduleArgs', 'Schedule']

@pulumi.input_type
class ScheduleArgs:
    def __init__(__self__, *,
                 automation_account_name: pulumi.Input[str],
                 frequency: pulumi.Input[Union[str, 'ScheduleFrequency']],
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 start_time: pulumi.Input[str],
                 advanced_schedule: Optional[pulumi.Input['AdvancedScheduleArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expiry_time: Optional[pulumi.Input[str]] = None,
                 interval: Optional[Any] = None,
                 schedule_name: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Schedule resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[Union[str, 'ScheduleFrequency']] frequency: Gets or sets the frequency of the schedule.
        :param pulumi.Input[str] name: Gets or sets the name of the Schedule.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[str] start_time: Gets or sets the start time of the schedule.
        :param pulumi.Input['AdvancedScheduleArgs'] advanced_schedule: Gets or sets the AdvancedSchedule.
        :param pulumi.Input[str] description: Gets or sets the description of the schedule.
        :param pulumi.Input[str] expiry_time: Gets or sets the end time of the schedule.
        :param Any interval: Gets or sets the interval of the schedule.
        :param pulumi.Input[str] schedule_name: The schedule name.
        :param pulumi.Input[str] time_zone: Gets or sets the time zone of the schedule.
        """
        pulumi.set(__self__, "automation_account_name", automation_account_name)
        pulumi.set(__self__, "frequency", frequency)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "start_time", start_time)
        if advanced_schedule is not None:
            pulumi.set(__self__, "advanced_schedule", advanced_schedule)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expiry_time is not None:
            pulumi.set(__self__, "expiry_time", expiry_time)
        if interval is not None:
            pulumi.set(__self__, "interval", interval)
        if schedule_name is not None:
            pulumi.set(__self__, "schedule_name", schedule_name)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[str]:
        """
        The name of the automation account.
        """
        return pulumi.get(self, "automation_account_name")

    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "automation_account_name", value)

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[Union[str, 'ScheduleFrequency']]:
        """
        Gets or sets the frequency of the schedule.
        """
        return pulumi.get(self, "frequency")

    @frequency.setter
    def frequency(self, value: pulumi.Input[Union[str, 'ScheduleFrequency']]):
        pulumi.set(self, "frequency", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Gets or sets the name of the Schedule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of an Azure Resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[str]:
        """
        Gets or sets the start time of the schedule.
        """
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: pulumi.Input[str]):
        pulumi.set(self, "start_time", value)

    @property
    @pulumi.getter(name="advancedSchedule")
    def advanced_schedule(self) -> Optional[pulumi.Input['AdvancedScheduleArgs']]:
        """
        Gets or sets the AdvancedSchedule.
        """
        return pulumi.get(self, "advanced_schedule")

    @advanced_schedule.setter
    def advanced_schedule(self, value: Optional[pulumi.Input['AdvancedScheduleArgs']]):
        pulumi.set(self, "advanced_schedule", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the description of the schedule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the end time of the schedule.
        """
        return pulumi.get(self, "expiry_time")

    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiry_time", value)

    @property
    @pulumi.getter
    def interval(self) -> Optional[Any]:
        """
        Gets or sets the interval of the schedule.
        """
        return pulumi.get(self, "interval")

    @interval.setter
    def interval(self, value: Optional[Any]):
        pulumi.set(self, "interval", value)

    @property
    @pulumi.getter(name="scheduleName")
    def schedule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The schedule name.
        """
        return pulumi.get(self, "schedule_name")

    @schedule_name.setter
    def schedule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schedule_name", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the time zone of the schedule.
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone", value)


class Schedule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advanced_schedule: Optional[pulumi.Input[pulumi.InputType['AdvancedScheduleArgs']]] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expiry_time: Optional[pulumi.Input[str]] = None,
                 frequency: Optional[pulumi.Input[Union[str, 'ScheduleFrequency']]] = None,
                 interval: Optional[Any] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schedule_name: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Definition of the schedule.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AdvancedScheduleArgs']] advanced_schedule: Gets or sets the AdvancedSchedule.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[str] description: Gets or sets the description of the schedule.
        :param pulumi.Input[str] expiry_time: Gets or sets the end time of the schedule.
        :param pulumi.Input[Union[str, 'ScheduleFrequency']] frequency: Gets or sets the frequency of the schedule.
        :param Any interval: Gets or sets the interval of the schedule.
        :param pulumi.Input[str] name: Gets or sets the name of the Schedule.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[str] schedule_name: The schedule name.
        :param pulumi.Input[str] start_time: Gets or sets the start time of the schedule.
        :param pulumi.Input[str] time_zone: Gets or sets the time zone of the schedule.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScheduleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the schedule.

        :param str resource_name: The name of the resource.
        :param ScheduleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advanced_schedule: Optional[pulumi.Input[pulumi.InputType['AdvancedScheduleArgs']]] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expiry_time: Optional[pulumi.Input[str]] = None,
                 frequency: Optional[pulumi.Input[Union[str, 'ScheduleFrequency']]] = None,
                 interval: Optional[Any] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schedule_name: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScheduleArgs.__new__(ScheduleArgs)

            __props__.__dict__["advanced_schedule"] = advanced_schedule
            if automation_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__.__dict__["automation_account_name"] = automation_account_name
            __props__.__dict__["description"] = description
            __props__.__dict__["expiry_time"] = expiry_time
            if frequency is None and not opts.urn:
                raise TypeError("Missing required property 'frequency'")
            __props__.__dict__["frequency"] = frequency
            __props__.__dict__["interval"] = interval
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["schedule_name"] = schedule_name
            if start_time is None and not opts.urn:
                raise TypeError("Missing required property 'start_time'")
            __props__.__dict__["start_time"] = start_time
            __props__.__dict__["time_zone"] = time_zone
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["expiry_time_offset_minutes"] = None
            __props__.__dict__["is_enabled"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["next_run"] = None
            __props__.__dict__["next_run_offset_minutes"] = None
            __props__.__dict__["start_time_offset_minutes"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:automation:Schedule"), pulumi.Alias(type_="azure-native:automation/v20151031:Schedule"), pulumi.Alias(type_="azure-native:automation/v20190601:Schedule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Schedule, __self__).__init__(
            'azure-native:automation/v20200113preview:Schedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Schedule':
        """
        Get an existing Schedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScheduleArgs.__new__(ScheduleArgs)

        __props__.__dict__["advanced_schedule"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["expiry_time"] = None
        __props__.__dict__["expiry_time_offset_minutes"] = None
        __props__.__dict__["frequency"] = None
        __props__.__dict__["interval"] = None
        __props__.__dict__["is_enabled"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["next_run"] = None
        __props__.__dict__["next_run_offset_minutes"] = None
        __props__.__dict__["start_time"] = None
        __props__.__dict__["start_time_offset_minutes"] = None
        __props__.__dict__["time_zone"] = None
        __props__.__dict__["type"] = None
        return Schedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="advancedSchedule")
    def advanced_schedule(self) -> pulumi.Output[Optional['outputs.AdvancedScheduleResponse']]:
        """
        Gets or sets the advanced schedule.
        """
        return pulumi.get(self, "advanced_schedule")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the end time of the schedule.
        """
        return pulumi.get(self, "expiry_time")

    @property
    @pulumi.getter(name="expiryTimeOffsetMinutes")
    def expiry_time_offset_minutes(self) -> pulumi.Output[Optional[float]]:
        """
        Gets or sets the expiry time's offset in minutes.
        """
        return pulumi.get(self, "expiry_time_offset_minutes")

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the frequency of the schedule.
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter
    def interval(self) -> pulumi.Output[Optional[Any]]:
        """
        Gets or sets the interval of the schedule.
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Gets or sets a value indicating whether this schedule is enabled.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nextRun")
    def next_run(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the next run time of the schedule.
        """
        return pulumi.get(self, "next_run")

    @property
    @pulumi.getter(name="nextRunOffsetMinutes")
    def next_run_offset_minutes(self) -> pulumi.Output[Optional[float]]:
        """
        Gets or sets the next run time's offset in minutes.
        """
        return pulumi.get(self, "next_run_offset_minutes")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the start time of the schedule.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter(name="startTimeOffsetMinutes")
    def start_time_offset_minutes(self) -> pulumi.Output[float]:
        """
        Gets the start time's offset in minutes.
        """
        return pulumi.get(self, "start_time_offset_minutes")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the time zone of the schedule.
        """
        return pulumi.get(self, "time_zone")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

