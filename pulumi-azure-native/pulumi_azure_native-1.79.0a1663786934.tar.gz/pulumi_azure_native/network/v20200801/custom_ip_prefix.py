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

__all__ = ['CustomIPPrefixArgs', 'CustomIPPrefix']

@pulumi.input_type
class CustomIPPrefixArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 cidr: Optional[pulumi.Input[str]] = None,
                 commissioned_state: Optional[pulumi.Input[Union[str, 'CommissionedState']]] = None,
                 custom_ip_prefix_name: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a CustomIPPrefix resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] cidr: The prefix range in CIDR notation. Should include the start address and the prefix length.
        :param pulumi.Input[Union[str, 'CommissionedState']] commissioned_state: The commissioned state of the Custom IP Prefix.
        :param pulumi.Input[str] custom_ip_prefix_name: The name of the custom IP prefix.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extended location of the custom IP prefix.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: A list of availability zones denoting the IP allocated for the resource needs to come from.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if cidr is not None:
            pulumi.set(__self__, "cidr", cidr)
        if commissioned_state is not None:
            pulumi.set(__self__, "commissioned_state", commissioned_state)
        if custom_ip_prefix_name is not None:
            pulumi.set(__self__, "custom_ip_prefix_name", custom_ip_prefix_name)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zones is not None:
            pulumi.set(__self__, "zones", zones)

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
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[str]]:
        """
        The prefix range in CIDR notation. Should include the start address and the prefix length.
        """
        return pulumi.get(self, "cidr")

    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr", value)

    @property
    @pulumi.getter(name="commissionedState")
    def commissioned_state(self) -> Optional[pulumi.Input[Union[str, 'CommissionedState']]]:
        """
        The commissioned state of the Custom IP Prefix.
        """
        return pulumi.get(self, "commissioned_state")

    @commissioned_state.setter
    def commissioned_state(self, value: Optional[pulumi.Input[Union[str, 'CommissionedState']]]):
        pulumi.set(self, "commissioned_state", value)

    @property
    @pulumi.getter(name="customIpPrefixName")
    def custom_ip_prefix_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the custom IP prefix.
        """
        return pulumi.get(self, "custom_ip_prefix_name")

    @custom_ip_prefix_name.setter
    def custom_ip_prefix_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_ip_prefix_name", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        The extended location of the custom IP prefix.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of availability zones denoting the IP allocated for the resource needs to come from.
        """
        return pulumi.get(self, "zones")

    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "zones", value)


class CustomIPPrefix(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr: Optional[pulumi.Input[str]] = None,
                 commissioned_state: Optional[pulumi.Input[Union[str, 'CommissionedState']]] = None,
                 custom_ip_prefix_name: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Custom IP prefix resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cidr: The prefix range in CIDR notation. Should include the start address and the prefix length.
        :param pulumi.Input[Union[str, 'CommissionedState']] commissioned_state: The commissioned state of the Custom IP Prefix.
        :param pulumi.Input[str] custom_ip_prefix_name: The name of the custom IP prefix.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extended location of the custom IP prefix.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: A list of availability zones denoting the IP allocated for the resource needs to come from.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomIPPrefixArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Custom IP prefix resource.

        :param str resource_name: The name of the resource.
        :param CustomIPPrefixArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomIPPrefixArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr: Optional[pulumi.Input[str]] = None,
                 commissioned_state: Optional[pulumi.Input[Union[str, 'CommissionedState']]] = None,
                 custom_ip_prefix_name: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomIPPrefixArgs.__new__(CustomIPPrefixArgs)

            __props__.__dict__["cidr"] = cidr
            __props__.__dict__["commissioned_state"] = commissioned_state
            __props__.__dict__["custom_ip_prefix_name"] = custom_ip_prefix_name
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zones"] = zones
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["public_ip_prefixes"] = None
            __props__.__dict__["resource_guid"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:CustomIPPrefix"), pulumi.Alias(type_="azure-native:network/v20200601:CustomIPPrefix"), pulumi.Alias(type_="azure-native:network/v20200701:CustomIPPrefix"), pulumi.Alias(type_="azure-native:network/v20201101:CustomIPPrefix"), pulumi.Alias(type_="azure-native:network/v20210201:CustomIPPrefix"), pulumi.Alias(type_="azure-native:network/v20210301:CustomIPPrefix"), pulumi.Alias(type_="azure-native:network/v20210501:CustomIPPrefix"), pulumi.Alias(type_="azure-native:network/v20210801:CustomIPPrefix"), pulumi.Alias(type_="azure-native:network/v20220101:CustomIPPrefix")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CustomIPPrefix, __self__).__init__(
            'azure-native:network/v20200801:CustomIPPrefix',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CustomIPPrefix':
        """
        Get an existing CustomIPPrefix resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CustomIPPrefixArgs.__new__(CustomIPPrefixArgs)

        __props__.__dict__["cidr"] = None
        __props__.__dict__["commissioned_state"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_ip_prefixes"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["zones"] = None
        return CustomIPPrefix(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cidr(self) -> pulumi.Output[Optional[str]]:
        """
        The prefix range in CIDR notation. Should include the start address and the prefix length.
        """
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter(name="commissionedState")
    def commissioned_state(self) -> pulumi.Output[Optional[str]]:
        """
        The commissioned state of the Custom IP Prefix.
        """
        return pulumi.get(self, "commissioned_state")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        The extended location of the custom IP prefix.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the custom IP prefix resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicIpPrefixes")
    def public_ip_prefixes(self) -> pulumi.Output[Sequence['outputs.SubResourceResponse']]:
        """
        The list of all referenced PublicIpPrefixes.
        """
        return pulumi.get(self, "public_ip_prefixes")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[str]:
        """
        The resource GUID property of the custom IP prefix resource.
        """
        return pulumi.get(self, "resource_guid")

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

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of availability zones denoting the IP allocated for the resource needs to come from.
        """
        return pulumi.get(self, "zones")

