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

__all__ = ['DscpConfigurationArgs', 'DscpConfiguration']

@pulumi.input_type
class DscpConfigurationArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 destination_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['QosIpRangeArgs']]]] = None,
                 destination_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['QosPortRangeArgs']]]] = None,
                 dscp_configuration_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 markings: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 protocol: Optional[pulumi.Input[Union[str, 'ProtocolType']]] = None,
                 source_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['QosIpRangeArgs']]]] = None,
                 source_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['QosPortRangeArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DscpConfiguration resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input['QosIpRangeArgs']]] destination_ip_ranges: Destination IP ranges.
        :param pulumi.Input[Sequence[pulumi.Input['QosPortRangeArgs']]] destination_port_ranges: Destination port ranges.
        :param pulumi.Input[str] dscp_configuration_name: The name of the resource.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] markings: List of markings to be used in the configuration.
        :param pulumi.Input[Union[str, 'ProtocolType']] protocol: RNM supported protocol types.
        :param pulumi.Input[Sequence[pulumi.Input['QosIpRangeArgs']]] source_ip_ranges: Source IP ranges.
        :param pulumi.Input[Sequence[pulumi.Input['QosPortRangeArgs']]] source_port_ranges: Sources port ranges.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if destination_ip_ranges is not None:
            pulumi.set(__self__, "destination_ip_ranges", destination_ip_ranges)
        if destination_port_ranges is not None:
            pulumi.set(__self__, "destination_port_ranges", destination_port_ranges)
        if dscp_configuration_name is not None:
            pulumi.set(__self__, "dscp_configuration_name", dscp_configuration_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if markings is not None:
            pulumi.set(__self__, "markings", markings)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if source_ip_ranges is not None:
            pulumi.set(__self__, "source_ip_ranges", source_ip_ranges)
        if source_port_ranges is not None:
            pulumi.set(__self__, "source_port_ranges", source_port_ranges)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="destinationIpRanges")
    def destination_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['QosIpRangeArgs']]]]:
        """
        Destination IP ranges.
        """
        return pulumi.get(self, "destination_ip_ranges")

    @destination_ip_ranges.setter
    def destination_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['QosIpRangeArgs']]]]):
        pulumi.set(self, "destination_ip_ranges", value)

    @property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['QosPortRangeArgs']]]]:
        """
        Destination port ranges.
        """
        return pulumi.get(self, "destination_port_ranges")

    @destination_port_ranges.setter
    def destination_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['QosPortRangeArgs']]]]):
        pulumi.set(self, "destination_port_ranges", value)

    @property
    @pulumi.getter(name="dscpConfigurationName")
    def dscp_configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "dscp_configuration_name")

    @dscp_configuration_name.setter
    def dscp_configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dscp_configuration_name", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def markings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        List of markings to be used in the configuration.
        """
        return pulumi.get(self, "markings")

    @markings.setter
    def markings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "markings", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[Union[str, 'ProtocolType']]]:
        """
        RNM supported protocol types.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[Union[str, 'ProtocolType']]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['QosIpRangeArgs']]]]:
        """
        Source IP ranges.
        """
        return pulumi.get(self, "source_ip_ranges")

    @source_ip_ranges.setter
    def source_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['QosIpRangeArgs']]]]):
        pulumi.set(self, "source_ip_ranges", value)

    @property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['QosPortRangeArgs']]]]:
        """
        Sources port ranges.
        """
        return pulumi.get(self, "source_port_ranges")

    @source_port_ranges.setter
    def source_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['QosPortRangeArgs']]]]):
        pulumi.set(self, "source_port_ranges", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class DscpConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QosIpRangeArgs']]]]] = None,
                 destination_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QosPortRangeArgs']]]]] = None,
                 dscp_configuration_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 markings: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 protocol: Optional[pulumi.Input[Union[str, 'ProtocolType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QosIpRangeArgs']]]]] = None,
                 source_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QosPortRangeArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        DSCP Configuration in a resource group.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QosIpRangeArgs']]]] destination_ip_ranges: Destination IP ranges.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QosPortRangeArgs']]]] destination_port_ranges: Destination port ranges.
        :param pulumi.Input[str] dscp_configuration_name: The name of the resource.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] markings: List of markings to be used in the configuration.
        :param pulumi.Input[Union[str, 'ProtocolType']] protocol: RNM supported protocol types.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QosIpRangeArgs']]]] source_ip_ranges: Source IP ranges.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QosPortRangeArgs']]]] source_port_ranges: Sources port ranges.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DscpConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        DSCP Configuration in a resource group.

        :param str resource_name: The name of the resource.
        :param DscpConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DscpConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QosIpRangeArgs']]]]] = None,
                 destination_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QosPortRangeArgs']]]]] = None,
                 dscp_configuration_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 markings: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 protocol: Optional[pulumi.Input[Union[str, 'ProtocolType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QosIpRangeArgs']]]]] = None,
                 source_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QosPortRangeArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DscpConfigurationArgs.__new__(DscpConfigurationArgs)

            __props__.__dict__["destination_ip_ranges"] = destination_ip_ranges
            __props__.__dict__["destination_port_ranges"] = destination_port_ranges
            __props__.__dict__["dscp_configuration_name"] = dscp_configuration_name
            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            __props__.__dict__["markings"] = markings
            __props__.__dict__["protocol"] = protocol
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["source_ip_ranges"] = source_ip_ranges
            __props__.__dict__["source_port_ranges"] = source_port_ranges
            __props__.__dict__["tags"] = tags
            __props__.__dict__["associated_network_interfaces"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["qos_collection_id"] = None
            __props__.__dict__["resource_guid"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:DscpConfiguration"), pulumi.Alias(type_="azure-native:network/v20200601:DscpConfiguration"), pulumi.Alias(type_="azure-native:network/v20200801:DscpConfiguration"), pulumi.Alias(type_="azure-native:network/v20201101:DscpConfiguration"), pulumi.Alias(type_="azure-native:network/v20210201:DscpConfiguration"), pulumi.Alias(type_="azure-native:network/v20210301:DscpConfiguration"), pulumi.Alias(type_="azure-native:network/v20210501:DscpConfiguration"), pulumi.Alias(type_="azure-native:network/v20210801:DscpConfiguration"), pulumi.Alias(type_="azure-native:network/v20220101:DscpConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DscpConfiguration, __self__).__init__(
            'azure-native:network/v20200701:DscpConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DscpConfiguration':
        """
        Get an existing DscpConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DscpConfigurationArgs.__new__(DscpConfigurationArgs)

        __props__.__dict__["associated_network_interfaces"] = None
        __props__.__dict__["destination_ip_ranges"] = None
        __props__.__dict__["destination_port_ranges"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["markings"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["protocol"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["qos_collection_id"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["source_ip_ranges"] = None
        __props__.__dict__["source_port_ranges"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return DscpConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="associatedNetworkInterfaces")
    def associated_network_interfaces(self) -> pulumi.Output[Sequence['outputs.NetworkInterfaceResponse']]:
        """
        Associated Network Interfaces to the DSCP Configuration.
        """
        return pulumi.get(self, "associated_network_interfaces")

    @property
    @pulumi.getter(name="destinationIpRanges")
    def destination_ip_ranges(self) -> pulumi.Output[Optional[Sequence['outputs.QosIpRangeResponse']]]:
        """
        Destination IP ranges.
        """
        return pulumi.get(self, "destination_ip_ranges")

    @property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> pulumi.Output[Optional[Sequence['outputs.QosPortRangeResponse']]]:
        """
        Destination port ranges.
        """
        return pulumi.get(self, "destination_port_ranges")

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
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def markings(self) -> pulumi.Output[Optional[Sequence[int]]]:
        """
        List of markings to be used in the configuration.
        """
        return pulumi.get(self, "markings")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional[str]]:
        """
        RNM supported protocol types.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the DSCP Configuration resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="qosCollectionId")
    def qos_collection_id(self) -> pulumi.Output[str]:
        """
        Qos Collection ID generated by RNM.
        """
        return pulumi.get(self, "qos_collection_id")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[str]:
        """
        The resource GUID property of the DSCP Configuration resource.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(self) -> pulumi.Output[Optional[Sequence['outputs.QosIpRangeResponse']]]:
        """
        Source IP ranges.
        """
        return pulumi.get(self, "source_ip_ranges")

    @property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> pulumi.Output[Optional[Sequence['outputs.QosPortRangeResponse']]]:
        """
        Sources port ranges.
        """
        return pulumi.get(self, "source_port_ranges")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

