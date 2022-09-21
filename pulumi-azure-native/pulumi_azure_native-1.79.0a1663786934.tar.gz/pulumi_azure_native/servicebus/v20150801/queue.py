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

__all__ = ['QueueArgs', 'Queue']

@pulumi.input_type
class QueueArgs:
    def __init__(__self__, *,
                 namespace_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 auto_delete_on_idle: Optional[pulumi.Input[str]] = None,
                 dead_lettering_on_message_expiration: Optional[pulumi.Input[bool]] = None,
                 default_message_time_to_live: Optional[pulumi.Input[str]] = None,
                 duplicate_detection_history_time_window: Optional[pulumi.Input[str]] = None,
                 enable_batched_operations: Optional[pulumi.Input[bool]] = None,
                 enable_express: Optional[pulumi.Input[bool]] = None,
                 enable_partitioning: Optional[pulumi.Input[bool]] = None,
                 entity_availability_status: Optional[pulumi.Input['EntityAvailabilityStatus']] = None,
                 is_anonymous_accessible: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 lock_duration: Optional[pulumi.Input[str]] = None,
                 max_delivery_count: Optional[pulumi.Input[int]] = None,
                 max_size_in_megabytes: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 queue_name: Optional[pulumi.Input[str]] = None,
                 requires_duplicate_detection: Optional[pulumi.Input[bool]] = None,
                 requires_session: Optional[pulumi.Input[bool]] = None,
                 status: Optional[pulumi.Input['EntityStatus']] = None,
                 support_ordering: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Queue resource.
        :param pulumi.Input[str] namespace_name: The namespace name
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] auto_delete_on_idle: the TimeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes.
        :param pulumi.Input[bool] dead_lettering_on_message_expiration: A value that indicates whether this queue has dead letter support when a message expires.
        :param pulumi.Input[str] default_message_time_to_live: The default message time to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
        :param pulumi.Input[str] duplicate_detection_history_time_window: TimeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
        :param pulumi.Input[bool] enable_batched_operations: A value that indicates whether server-side batched operations are enabled.
        :param pulumi.Input[bool] enable_express: A value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage.
        :param pulumi.Input[bool] enable_partitioning: A value that indicates whether the queue is to be partitioned across multiple message brokers.
        :param pulumi.Input['EntityAvailabilityStatus'] entity_availability_status: Entity availability status for the queue.
        :param pulumi.Input[bool] is_anonymous_accessible: A value that indicates whether the message is accessible anonymously.
        :param pulumi.Input[str] location: location of the resource.
        :param pulumi.Input[str] lock_duration: The duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute.
        :param pulumi.Input[int] max_delivery_count: The maximum delivery count. A message is automatically deadlettered after this number of deliveries.
        :param pulumi.Input[float] max_size_in_megabytes: The maximum size of the queue in megabytes, which is the size of memory allocated for the queue.
        :param pulumi.Input[str] name: Queue name.
        :param pulumi.Input[str] queue_name: The queue name.
        :param pulumi.Input[bool] requires_duplicate_detection: A value indicating if this queue requires duplicate detection.
        :param pulumi.Input[bool] requires_session: A value that indicates whether the queue supports the concept of sessions.
        :param pulumi.Input['EntityStatus'] status: Enumerates the possible values for the status of a messaging entity.
        :param pulumi.Input[bool] support_ordering: A value that indicates whether the queue supports ordering.
        """
        pulumi.set(__self__, "namespace_name", namespace_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if auto_delete_on_idle is not None:
            pulumi.set(__self__, "auto_delete_on_idle", auto_delete_on_idle)
        if dead_lettering_on_message_expiration is not None:
            pulumi.set(__self__, "dead_lettering_on_message_expiration", dead_lettering_on_message_expiration)
        if default_message_time_to_live is not None:
            pulumi.set(__self__, "default_message_time_to_live", default_message_time_to_live)
        if duplicate_detection_history_time_window is not None:
            pulumi.set(__self__, "duplicate_detection_history_time_window", duplicate_detection_history_time_window)
        if enable_batched_operations is not None:
            pulumi.set(__self__, "enable_batched_operations", enable_batched_operations)
        if enable_express is not None:
            pulumi.set(__self__, "enable_express", enable_express)
        if enable_partitioning is not None:
            pulumi.set(__self__, "enable_partitioning", enable_partitioning)
        if entity_availability_status is not None:
            pulumi.set(__self__, "entity_availability_status", entity_availability_status)
        if is_anonymous_accessible is not None:
            pulumi.set(__self__, "is_anonymous_accessible", is_anonymous_accessible)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if lock_duration is not None:
            pulumi.set(__self__, "lock_duration", lock_duration)
        if max_delivery_count is not None:
            pulumi.set(__self__, "max_delivery_count", max_delivery_count)
        if max_size_in_megabytes is not None:
            pulumi.set(__self__, "max_size_in_megabytes", max_size_in_megabytes)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if queue_name is not None:
            pulumi.set(__self__, "queue_name", queue_name)
        if requires_duplicate_detection is not None:
            pulumi.set(__self__, "requires_duplicate_detection", requires_duplicate_detection)
        if requires_session is not None:
            pulumi.set(__self__, "requires_session", requires_session)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if support_ordering is not None:
            pulumi.set(__self__, "support_ordering", support_ordering)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        The namespace name
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="autoDeleteOnIdle")
    def auto_delete_on_idle(self) -> Optional[pulumi.Input[str]]:
        """
        the TimeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes.
        """
        return pulumi.get(self, "auto_delete_on_idle")

    @auto_delete_on_idle.setter
    def auto_delete_on_idle(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auto_delete_on_idle", value)

    @property
    @pulumi.getter(name="deadLetteringOnMessageExpiration")
    def dead_lettering_on_message_expiration(self) -> Optional[pulumi.Input[bool]]:
        """
        A value that indicates whether this queue has dead letter support when a message expires.
        """
        return pulumi.get(self, "dead_lettering_on_message_expiration")

    @dead_lettering_on_message_expiration.setter
    def dead_lettering_on_message_expiration(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dead_lettering_on_message_expiration", value)

    @property
    @pulumi.getter(name="defaultMessageTimeToLive")
    def default_message_time_to_live(self) -> Optional[pulumi.Input[str]]:
        """
        The default message time to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
        """
        return pulumi.get(self, "default_message_time_to_live")

    @default_message_time_to_live.setter
    def default_message_time_to_live(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_message_time_to_live", value)

    @property
    @pulumi.getter(name="duplicateDetectionHistoryTimeWindow")
    def duplicate_detection_history_time_window(self) -> Optional[pulumi.Input[str]]:
        """
        TimeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
        """
        return pulumi.get(self, "duplicate_detection_history_time_window")

    @duplicate_detection_history_time_window.setter
    def duplicate_detection_history_time_window(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "duplicate_detection_history_time_window", value)

    @property
    @pulumi.getter(name="enableBatchedOperations")
    def enable_batched_operations(self) -> Optional[pulumi.Input[bool]]:
        """
        A value that indicates whether server-side batched operations are enabled.
        """
        return pulumi.get(self, "enable_batched_operations")

    @enable_batched_operations.setter
    def enable_batched_operations(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_batched_operations", value)

    @property
    @pulumi.getter(name="enableExpress")
    def enable_express(self) -> Optional[pulumi.Input[bool]]:
        """
        A value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage.
        """
        return pulumi.get(self, "enable_express")

    @enable_express.setter
    def enable_express(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_express", value)

    @property
    @pulumi.getter(name="enablePartitioning")
    def enable_partitioning(self) -> Optional[pulumi.Input[bool]]:
        """
        A value that indicates whether the queue is to be partitioned across multiple message brokers.
        """
        return pulumi.get(self, "enable_partitioning")

    @enable_partitioning.setter
    def enable_partitioning(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_partitioning", value)

    @property
    @pulumi.getter(name="entityAvailabilityStatus")
    def entity_availability_status(self) -> Optional[pulumi.Input['EntityAvailabilityStatus']]:
        """
        Entity availability status for the queue.
        """
        return pulumi.get(self, "entity_availability_status")

    @entity_availability_status.setter
    def entity_availability_status(self, value: Optional[pulumi.Input['EntityAvailabilityStatus']]):
        pulumi.set(self, "entity_availability_status", value)

    @property
    @pulumi.getter(name="isAnonymousAccessible")
    def is_anonymous_accessible(self) -> Optional[pulumi.Input[bool]]:
        """
        A value that indicates whether the message is accessible anonymously.
        """
        return pulumi.get(self, "is_anonymous_accessible")

    @is_anonymous_accessible.setter
    def is_anonymous_accessible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_anonymous_accessible", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="lockDuration")
    def lock_duration(self) -> Optional[pulumi.Input[str]]:
        """
        The duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute.
        """
        return pulumi.get(self, "lock_duration")

    @lock_duration.setter
    def lock_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lock_duration", value)

    @property
    @pulumi.getter(name="maxDeliveryCount")
    def max_delivery_count(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum delivery count. A message is automatically deadlettered after this number of deliveries.
        """
        return pulumi.get(self, "max_delivery_count")

    @max_delivery_count.setter
    def max_delivery_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_delivery_count", value)

    @property
    @pulumi.getter(name="maxSizeInMegabytes")
    def max_size_in_megabytes(self) -> Optional[pulumi.Input[float]]:
        """
        The maximum size of the queue in megabytes, which is the size of memory allocated for the queue.
        """
        return pulumi.get(self, "max_size_in_megabytes")

    @max_size_in_megabytes.setter
    def max_size_in_megabytes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "max_size_in_megabytes", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Queue name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> Optional[pulumi.Input[str]]:
        """
        The queue name.
        """
        return pulumi.get(self, "queue_name")

    @queue_name.setter
    def queue_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "queue_name", value)

    @property
    @pulumi.getter(name="requiresDuplicateDetection")
    def requires_duplicate_detection(self) -> Optional[pulumi.Input[bool]]:
        """
        A value indicating if this queue requires duplicate detection.
        """
        return pulumi.get(self, "requires_duplicate_detection")

    @requires_duplicate_detection.setter
    def requires_duplicate_detection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "requires_duplicate_detection", value)

    @property
    @pulumi.getter(name="requiresSession")
    def requires_session(self) -> Optional[pulumi.Input[bool]]:
        """
        A value that indicates whether the queue supports the concept of sessions.
        """
        return pulumi.get(self, "requires_session")

    @requires_session.setter
    def requires_session(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "requires_session", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['EntityStatus']]:
        """
        Enumerates the possible values for the status of a messaging entity.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['EntityStatus']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="supportOrdering")
    def support_ordering(self) -> Optional[pulumi.Input[bool]]:
        """
        A value that indicates whether the queue supports ordering.
        """
        return pulumi.get(self, "support_ordering")

    @support_ordering.setter
    def support_ordering(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "support_ordering", value)


warnings.warn("""Version 2015-08-01 will be removed in v2 of the provider.""", DeprecationWarning)


class Queue(pulumi.CustomResource):
    warnings.warn("""Version 2015-08-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_delete_on_idle: Optional[pulumi.Input[str]] = None,
                 dead_lettering_on_message_expiration: Optional[pulumi.Input[bool]] = None,
                 default_message_time_to_live: Optional[pulumi.Input[str]] = None,
                 duplicate_detection_history_time_window: Optional[pulumi.Input[str]] = None,
                 enable_batched_operations: Optional[pulumi.Input[bool]] = None,
                 enable_express: Optional[pulumi.Input[bool]] = None,
                 enable_partitioning: Optional[pulumi.Input[bool]] = None,
                 entity_availability_status: Optional[pulumi.Input['EntityAvailabilityStatus']] = None,
                 is_anonymous_accessible: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 lock_duration: Optional[pulumi.Input[str]] = None,
                 max_delivery_count: Optional[pulumi.Input[int]] = None,
                 max_size_in_megabytes: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 queue_name: Optional[pulumi.Input[str]] = None,
                 requires_duplicate_detection: Optional[pulumi.Input[bool]] = None,
                 requires_session: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['EntityStatus']] = None,
                 support_ordering: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Description of queue Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auto_delete_on_idle: the TimeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes.
        :param pulumi.Input[bool] dead_lettering_on_message_expiration: A value that indicates whether this queue has dead letter support when a message expires.
        :param pulumi.Input[str] default_message_time_to_live: The default message time to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
        :param pulumi.Input[str] duplicate_detection_history_time_window: TimeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
        :param pulumi.Input[bool] enable_batched_operations: A value that indicates whether server-side batched operations are enabled.
        :param pulumi.Input[bool] enable_express: A value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage.
        :param pulumi.Input[bool] enable_partitioning: A value that indicates whether the queue is to be partitioned across multiple message brokers.
        :param pulumi.Input['EntityAvailabilityStatus'] entity_availability_status: Entity availability status for the queue.
        :param pulumi.Input[bool] is_anonymous_accessible: A value that indicates whether the message is accessible anonymously.
        :param pulumi.Input[str] location: location of the resource.
        :param pulumi.Input[str] lock_duration: The duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute.
        :param pulumi.Input[int] max_delivery_count: The maximum delivery count. A message is automatically deadlettered after this number of deliveries.
        :param pulumi.Input[float] max_size_in_megabytes: The maximum size of the queue in megabytes, which is the size of memory allocated for the queue.
        :param pulumi.Input[str] name: Queue name.
        :param pulumi.Input[str] namespace_name: The namespace name
        :param pulumi.Input[str] queue_name: The queue name.
        :param pulumi.Input[bool] requires_duplicate_detection: A value indicating if this queue requires duplicate detection.
        :param pulumi.Input[bool] requires_session: A value that indicates whether the queue supports the concept of sessions.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input['EntityStatus'] status: Enumerates the possible values for the status of a messaging entity.
        :param pulumi.Input[bool] support_ordering: A value that indicates whether the queue supports ordering.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: QueueArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Description of queue Resource.

        :param str resource_name: The name of the resource.
        :param QueueArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(QueueArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_delete_on_idle: Optional[pulumi.Input[str]] = None,
                 dead_lettering_on_message_expiration: Optional[pulumi.Input[bool]] = None,
                 default_message_time_to_live: Optional[pulumi.Input[str]] = None,
                 duplicate_detection_history_time_window: Optional[pulumi.Input[str]] = None,
                 enable_batched_operations: Optional[pulumi.Input[bool]] = None,
                 enable_express: Optional[pulumi.Input[bool]] = None,
                 enable_partitioning: Optional[pulumi.Input[bool]] = None,
                 entity_availability_status: Optional[pulumi.Input['EntityAvailabilityStatus']] = None,
                 is_anonymous_accessible: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 lock_duration: Optional[pulumi.Input[str]] = None,
                 max_delivery_count: Optional[pulumi.Input[int]] = None,
                 max_size_in_megabytes: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 queue_name: Optional[pulumi.Input[str]] = None,
                 requires_duplicate_detection: Optional[pulumi.Input[bool]] = None,
                 requires_session: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['EntityStatus']] = None,
                 support_ordering: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        pulumi.log.warn("""Queue is deprecated: Version 2015-08-01 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = QueueArgs.__new__(QueueArgs)

            __props__.__dict__["auto_delete_on_idle"] = auto_delete_on_idle
            __props__.__dict__["dead_lettering_on_message_expiration"] = dead_lettering_on_message_expiration
            __props__.__dict__["default_message_time_to_live"] = default_message_time_to_live
            __props__.__dict__["duplicate_detection_history_time_window"] = duplicate_detection_history_time_window
            __props__.__dict__["enable_batched_operations"] = enable_batched_operations
            __props__.__dict__["enable_express"] = enable_express
            __props__.__dict__["enable_partitioning"] = enable_partitioning
            __props__.__dict__["entity_availability_status"] = entity_availability_status
            __props__.__dict__["is_anonymous_accessible"] = is_anonymous_accessible
            __props__.__dict__["location"] = location
            __props__.__dict__["lock_duration"] = lock_duration
            __props__.__dict__["max_delivery_count"] = max_delivery_count
            __props__.__dict__["max_size_in_megabytes"] = max_size_in_megabytes
            __props__.__dict__["name"] = name
            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__.__dict__["namespace_name"] = namespace_name
            __props__.__dict__["queue_name"] = queue_name
            __props__.__dict__["requires_duplicate_detection"] = requires_duplicate_detection
            __props__.__dict__["requires_session"] = requires_session
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["status"] = status
            __props__.__dict__["support_ordering"] = support_ordering
            __props__.__dict__["accessed_at"] = None
            __props__.__dict__["count_details"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["message_count"] = None
            __props__.__dict__["size_in_bytes"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_at"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:servicebus:Queue"), pulumi.Alias(type_="azure-native:servicebus/v20140901:Queue"), pulumi.Alias(type_="azure-native:servicebus/v20170401:Queue"), pulumi.Alias(type_="azure-native:servicebus/v20180101preview:Queue"), pulumi.Alias(type_="azure-native:servicebus/v20210101preview:Queue"), pulumi.Alias(type_="azure-native:servicebus/v20210601preview:Queue"), pulumi.Alias(type_="azure-native:servicebus/v20211101:Queue"), pulumi.Alias(type_="azure-native:servicebus/v20220101preview:Queue")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Queue, __self__).__init__(
            'azure-native:servicebus/v20150801:Queue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Queue':
        """
        Get an existing Queue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = QueueArgs.__new__(QueueArgs)

        __props__.__dict__["accessed_at"] = None
        __props__.__dict__["auto_delete_on_idle"] = None
        __props__.__dict__["count_details"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["dead_lettering_on_message_expiration"] = None
        __props__.__dict__["default_message_time_to_live"] = None
        __props__.__dict__["duplicate_detection_history_time_window"] = None
        __props__.__dict__["enable_batched_operations"] = None
        __props__.__dict__["enable_express"] = None
        __props__.__dict__["enable_partitioning"] = None
        __props__.__dict__["entity_availability_status"] = None
        __props__.__dict__["is_anonymous_accessible"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["lock_duration"] = None
        __props__.__dict__["max_delivery_count"] = None
        __props__.__dict__["max_size_in_megabytes"] = None
        __props__.__dict__["message_count"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["requires_duplicate_detection"] = None
        __props__.__dict__["requires_session"] = None
        __props__.__dict__["size_in_bytes"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["support_ordering"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_at"] = None
        return Queue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessedAt")
    def accessed_at(self) -> pulumi.Output[str]:
        """
        Last time a message was sent, or the last time there was a receive request to this queue.
        """
        return pulumi.get(self, "accessed_at")

    @property
    @pulumi.getter(name="autoDeleteOnIdle")
    def auto_delete_on_idle(self) -> pulumi.Output[Optional[str]]:
        """
        the TimeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes.
        """
        return pulumi.get(self, "auto_delete_on_idle")

    @property
    @pulumi.getter(name="countDetails")
    def count_details(self) -> pulumi.Output['outputs.MessageCountDetailsResponse']:
        """
        Message Count Details.
        """
        return pulumi.get(self, "count_details")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The exact time the message was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="deadLetteringOnMessageExpiration")
    def dead_lettering_on_message_expiration(self) -> pulumi.Output[Optional[bool]]:
        """
        A value that indicates whether this queue has dead letter support when a message expires.
        """
        return pulumi.get(self, "dead_lettering_on_message_expiration")

    @property
    @pulumi.getter(name="defaultMessageTimeToLive")
    def default_message_time_to_live(self) -> pulumi.Output[Optional[str]]:
        """
        The default message time to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
        """
        return pulumi.get(self, "default_message_time_to_live")

    @property
    @pulumi.getter(name="duplicateDetectionHistoryTimeWindow")
    def duplicate_detection_history_time_window(self) -> pulumi.Output[Optional[str]]:
        """
        TimeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
        """
        return pulumi.get(self, "duplicate_detection_history_time_window")

    @property
    @pulumi.getter(name="enableBatchedOperations")
    def enable_batched_operations(self) -> pulumi.Output[Optional[bool]]:
        """
        A value that indicates whether server-side batched operations are enabled.
        """
        return pulumi.get(self, "enable_batched_operations")

    @property
    @pulumi.getter(name="enableExpress")
    def enable_express(self) -> pulumi.Output[Optional[bool]]:
        """
        A value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage.
        """
        return pulumi.get(self, "enable_express")

    @property
    @pulumi.getter(name="enablePartitioning")
    def enable_partitioning(self) -> pulumi.Output[Optional[bool]]:
        """
        A value that indicates whether the queue is to be partitioned across multiple message brokers.
        """
        return pulumi.get(self, "enable_partitioning")

    @property
    @pulumi.getter(name="entityAvailabilityStatus")
    def entity_availability_status(self) -> pulumi.Output[Optional[str]]:
        """
        Entity availability status for the queue.
        """
        return pulumi.get(self, "entity_availability_status")

    @property
    @pulumi.getter(name="isAnonymousAccessible")
    def is_anonymous_accessible(self) -> pulumi.Output[Optional[bool]]:
        """
        A value that indicates whether the message is accessible anonymously.
        """
        return pulumi.get(self, "is_anonymous_accessible")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="lockDuration")
    def lock_duration(self) -> pulumi.Output[Optional[str]]:
        """
        The duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute.
        """
        return pulumi.get(self, "lock_duration")

    @property
    @pulumi.getter(name="maxDeliveryCount")
    def max_delivery_count(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum delivery count. A message is automatically deadlettered after this number of deliveries.
        """
        return pulumi.get(self, "max_delivery_count")

    @property
    @pulumi.getter(name="maxSizeInMegabytes")
    def max_size_in_megabytes(self) -> pulumi.Output[Optional[float]]:
        """
        The maximum size of the queue in megabytes, which is the size of memory allocated for the queue.
        """
        return pulumi.get(self, "max_size_in_megabytes")

    @property
    @pulumi.getter(name="messageCount")
    def message_count(self) -> pulumi.Output[float]:
        """
        The number of messages in the queue.
        """
        return pulumi.get(self, "message_count")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="requiresDuplicateDetection")
    def requires_duplicate_detection(self) -> pulumi.Output[Optional[bool]]:
        """
        A value indicating if this queue requires duplicate detection.
        """
        return pulumi.get(self, "requires_duplicate_detection")

    @property
    @pulumi.getter(name="requiresSession")
    def requires_session(self) -> pulumi.Output[Optional[bool]]:
        """
        A value that indicates whether the queue supports the concept of sessions.
        """
        return pulumi.get(self, "requires_session")

    @property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> pulumi.Output[float]:
        """
        The size of the queue, in bytes.
        """
        return pulumi.get(self, "size_in_bytes")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Enumerates the possible values for the status of a messaging entity.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="supportOrdering")
    def support_ordering(self) -> pulumi.Output[Optional[bool]]:
        """
        A value that indicates whether the queue supports ordering.
        """
        return pulumi.get(self, "support_ordering")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The exact time the message was updated.
        """
        return pulumi.get(self, "updated_at")

