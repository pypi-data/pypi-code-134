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

__all__ = ['ChannelArgs', 'Channel']

@pulumi.input_type
class ChannelArgs:
    def __init__(__self__, *,
                 partner_namespace_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 channel_name: Optional[pulumi.Input[str]] = None,
                 channel_type: Optional[pulumi.Input[Union[str, 'ChannelType']]] = None,
                 expiration_time_if_not_activated_utc: Optional[pulumi.Input[str]] = None,
                 message_for_activation: Optional[pulumi.Input[str]] = None,
                 partner_topic_info: Optional[pulumi.Input['PartnerTopicInfoArgs']] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ChannelProvisioningState']]] = None,
                 readiness_state: Optional[pulumi.Input[Union[str, 'ReadinessState']]] = None):
        """
        The set of arguments for constructing a Channel resource.
        :param pulumi.Input[str] partner_namespace_name: Name of the partner namespace.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the partners subscription.
        :param pulumi.Input[str] channel_name: Name of the channel.
        :param pulumi.Input[Union[str, 'ChannelType']] channel_type: The type of the event channel which represents the direction flow of events.
        :param pulumi.Input[str] expiration_time_if_not_activated_utc: Expiration time of the channel. If this timer expires while the corresponding partner topic is never activated,
               the channel and corresponding partner topic are deleted.
        :param pulumi.Input[str] message_for_activation: Context or helpful message that can be used during the approval process by the subscriber.
        :param pulumi.Input['PartnerTopicInfoArgs'] partner_topic_info: This property should be populated when channelType is PartnerTopic and represents information about the partner topic resource corresponding to the channel.
        :param pulumi.Input[Union[str, 'ChannelProvisioningState']] provisioning_state: Provisioning state of the channel.
        :param pulumi.Input[Union[str, 'ReadinessState']] readiness_state: The readiness state of the corresponding partner topic.
        """
        pulumi.set(__self__, "partner_namespace_name", partner_namespace_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if channel_name is not None:
            pulumi.set(__self__, "channel_name", channel_name)
        if channel_type is not None:
            pulumi.set(__self__, "channel_type", channel_type)
        if expiration_time_if_not_activated_utc is not None:
            pulumi.set(__self__, "expiration_time_if_not_activated_utc", expiration_time_if_not_activated_utc)
        if message_for_activation is not None:
            pulumi.set(__self__, "message_for_activation", message_for_activation)
        if partner_topic_info is not None:
            pulumi.set(__self__, "partner_topic_info", partner_topic_info)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if readiness_state is not None:
            pulumi.set(__self__, "readiness_state", readiness_state)

    @property
    @pulumi.getter(name="partnerNamespaceName")
    def partner_namespace_name(self) -> pulumi.Input[str]:
        """
        Name of the partner namespace.
        """
        return pulumi.get(self, "partner_namespace_name")

    @partner_namespace_name.setter
    def partner_namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "partner_namespace_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the partners subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the channel.
        """
        return pulumi.get(self, "channel_name")

    @channel_name.setter
    def channel_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel_name", value)

    @property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> Optional[pulumi.Input[Union[str, 'ChannelType']]]:
        """
        The type of the event channel which represents the direction flow of events.
        """
        return pulumi.get(self, "channel_type")

    @channel_type.setter
    def channel_type(self, value: Optional[pulumi.Input[Union[str, 'ChannelType']]]):
        pulumi.set(self, "channel_type", value)

    @property
    @pulumi.getter(name="expirationTimeIfNotActivatedUtc")
    def expiration_time_if_not_activated_utc(self) -> Optional[pulumi.Input[str]]:
        """
        Expiration time of the channel. If this timer expires while the corresponding partner topic is never activated,
        the channel and corresponding partner topic are deleted.
        """
        return pulumi.get(self, "expiration_time_if_not_activated_utc")

    @expiration_time_if_not_activated_utc.setter
    def expiration_time_if_not_activated_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_time_if_not_activated_utc", value)

    @property
    @pulumi.getter(name="messageForActivation")
    def message_for_activation(self) -> Optional[pulumi.Input[str]]:
        """
        Context or helpful message that can be used during the approval process by the subscriber.
        """
        return pulumi.get(self, "message_for_activation")

    @message_for_activation.setter
    def message_for_activation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message_for_activation", value)

    @property
    @pulumi.getter(name="partnerTopicInfo")
    def partner_topic_info(self) -> Optional[pulumi.Input['PartnerTopicInfoArgs']]:
        """
        This property should be populated when channelType is PartnerTopic and represents information about the partner topic resource corresponding to the channel.
        """
        return pulumi.get(self, "partner_topic_info")

    @partner_topic_info.setter
    def partner_topic_info(self, value: Optional[pulumi.Input['PartnerTopicInfoArgs']]):
        pulumi.set(self, "partner_topic_info", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'ChannelProvisioningState']]]:
        """
        Provisioning state of the channel.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'ChannelProvisioningState']]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="readinessState")
    def readiness_state(self) -> Optional[pulumi.Input[Union[str, 'ReadinessState']]]:
        """
        The readiness state of the corresponding partner topic.
        """
        return pulumi.get(self, "readiness_state")

    @readiness_state.setter
    def readiness_state(self, value: Optional[pulumi.Input[Union[str, 'ReadinessState']]]):
        pulumi.set(self, "readiness_state", value)


class Channel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 channel_type: Optional[pulumi.Input[Union[str, 'ChannelType']]] = None,
                 expiration_time_if_not_activated_utc: Optional[pulumi.Input[str]] = None,
                 message_for_activation: Optional[pulumi.Input[str]] = None,
                 partner_namespace_name: Optional[pulumi.Input[str]] = None,
                 partner_topic_info: Optional[pulumi.Input[pulumi.InputType['PartnerTopicInfoArgs']]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ChannelProvisioningState']]] = None,
                 readiness_state: Optional[pulumi.Input[Union[str, 'ReadinessState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Channel info.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] channel_name: Name of the channel.
        :param pulumi.Input[Union[str, 'ChannelType']] channel_type: The type of the event channel which represents the direction flow of events.
        :param pulumi.Input[str] expiration_time_if_not_activated_utc: Expiration time of the channel. If this timer expires while the corresponding partner topic is never activated,
               the channel and corresponding partner topic are deleted.
        :param pulumi.Input[str] message_for_activation: Context or helpful message that can be used during the approval process by the subscriber.
        :param pulumi.Input[str] partner_namespace_name: Name of the partner namespace.
        :param pulumi.Input[pulumi.InputType['PartnerTopicInfoArgs']] partner_topic_info: This property should be populated when channelType is PartnerTopic and represents information about the partner topic resource corresponding to the channel.
        :param pulumi.Input[Union[str, 'ChannelProvisioningState']] provisioning_state: Provisioning state of the channel.
        :param pulumi.Input[Union[str, 'ReadinessState']] readiness_state: The readiness state of the corresponding partner topic.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the partners subscription.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ChannelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Channel info.

        :param str resource_name: The name of the resource.
        :param ChannelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ChannelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 channel_type: Optional[pulumi.Input[Union[str, 'ChannelType']]] = None,
                 expiration_time_if_not_activated_utc: Optional[pulumi.Input[str]] = None,
                 message_for_activation: Optional[pulumi.Input[str]] = None,
                 partner_namespace_name: Optional[pulumi.Input[str]] = None,
                 partner_topic_info: Optional[pulumi.Input[pulumi.InputType['PartnerTopicInfoArgs']]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ChannelProvisioningState']]] = None,
                 readiness_state: Optional[pulumi.Input[Union[str, 'ReadinessState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ChannelArgs.__new__(ChannelArgs)

            __props__.__dict__["channel_name"] = channel_name
            __props__.__dict__["channel_type"] = channel_type
            __props__.__dict__["expiration_time_if_not_activated_utc"] = expiration_time_if_not_activated_utc
            __props__.__dict__["message_for_activation"] = message_for_activation
            if partner_namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'partner_namespace_name'")
            __props__.__dict__["partner_namespace_name"] = partner_namespace_name
            __props__.__dict__["partner_topic_info"] = partner_topic_info
            __props__.__dict__["provisioning_state"] = provisioning_state
            __props__.__dict__["readiness_state"] = readiness_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventgrid:Channel"), pulumi.Alias(type_="azure-native:eventgrid/v20211015preview:Channel")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Channel, __self__).__init__(
            'azure-native:eventgrid/v20220615:Channel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Channel':
        """
        Get an existing Channel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ChannelArgs.__new__(ChannelArgs)

        __props__.__dict__["channel_type"] = None
        __props__.__dict__["expiration_time_if_not_activated_utc"] = None
        __props__.__dict__["message_for_activation"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["partner_topic_info"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["readiness_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Channel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the event channel which represents the direction flow of events.
        """
        return pulumi.get(self, "channel_type")

    @property
    @pulumi.getter(name="expirationTimeIfNotActivatedUtc")
    def expiration_time_if_not_activated_utc(self) -> pulumi.Output[Optional[str]]:
        """
        Expiration time of the channel. If this timer expires while the corresponding partner topic is never activated,
        the channel and corresponding partner topic are deleted.
        """
        return pulumi.get(self, "expiration_time_if_not_activated_utc")

    @property
    @pulumi.getter(name="messageForActivation")
    def message_for_activation(self) -> pulumi.Output[Optional[str]]:
        """
        Context or helpful message that can be used during the approval process by the subscriber.
        """
        return pulumi.get(self, "message_for_activation")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerTopicInfo")
    def partner_topic_info(self) -> pulumi.Output[Optional['outputs.PartnerTopicInfoResponse']]:
        """
        This property should be populated when channelType is PartnerTopic and represents information about the partner topic resource corresponding to the channel.
        """
        return pulumi.get(self, "partner_topic_info")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Provisioning state of the channel.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="readinessState")
    def readiness_state(self) -> pulumi.Output[Optional[str]]:
        """
        The readiness state of the corresponding partner topic.
        """
        return pulumi.get(self, "readiness_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to Channel resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")

