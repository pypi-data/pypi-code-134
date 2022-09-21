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

__all__ = ['PeeringArgs', 'Peering']

@pulumi.input_type
class PeeringArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[Union[str, 'Kind']],
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['PeeringSkuArgs'],
                 direct: Optional[pulumi.Input['PeeringPropertiesDirectArgs']] = None,
                 exchange: Optional[pulumi.Input['PeeringPropertiesExchangeArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 peering_location: Optional[pulumi.Input[str]] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Peering resource.
        :param pulumi.Input[Union[str, 'Kind']] kind: The kind of the peering.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['PeeringSkuArgs'] sku: The SKU that defines the tier and kind of the peering.
        :param pulumi.Input['PeeringPropertiesDirectArgs'] direct: The properties that define a direct peering.
        :param pulumi.Input['PeeringPropertiesExchangeArgs'] exchange: The properties that define an exchange peering.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] peering_location: The location of the peering.
        :param pulumi.Input[str] peering_name: The name of the peering.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        if direct is not None:
            pulumi.set(__self__, "direct", direct)
        if exchange is not None:
            pulumi.set(__self__, "exchange", exchange)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if peering_location is not None:
            pulumi.set(__self__, "peering_location", peering_location)
        if peering_name is not None:
            pulumi.set(__self__, "peering_name", peering_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[Union[str, 'Kind']]:
        """
        The kind of the peering.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[Union[str, 'Kind']]):
        pulumi.set(self, "kind", value)

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
    def sku(self) -> pulumi.Input['PeeringSkuArgs']:
        """
        The SKU that defines the tier and kind of the peering.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['PeeringSkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def direct(self) -> Optional[pulumi.Input['PeeringPropertiesDirectArgs']]:
        """
        The properties that define a direct peering.
        """
        return pulumi.get(self, "direct")

    @direct.setter
    def direct(self, value: Optional[pulumi.Input['PeeringPropertiesDirectArgs']]):
        pulumi.set(self, "direct", value)

    @property
    @pulumi.getter
    def exchange(self) -> Optional[pulumi.Input['PeeringPropertiesExchangeArgs']]:
        """
        The properties that define an exchange peering.
        """
        return pulumi.get(self, "exchange")

    @exchange.setter
    def exchange(self, value: Optional[pulumi.Input['PeeringPropertiesExchangeArgs']]):
        pulumi.set(self, "exchange", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="peeringLocation")
    def peering_location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the peering.
        """
        return pulumi.get(self, "peering_location")

    @peering_location.setter
    def peering_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peering_location", value)

    @property
    @pulumi.getter(name="peeringName")
    def peering_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the peering.
        """
        return pulumi.get(self, "peering_name")

    @peering_name.setter
    def peering_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peering_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""Version 2019-09-01-preview will be removed in v2 of the provider.""", DeprecationWarning)


class Peering(pulumi.CustomResource):
    warnings.warn("""Version 2019-09-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 direct: Optional[pulumi.Input[pulumi.InputType['PeeringPropertiesDirectArgs']]] = None,
                 exchange: Optional[pulumi.Input[pulumi.InputType['PeeringPropertiesExchangeArgs']]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 peering_location: Optional[pulumi.Input[str]] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['PeeringSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Peering is a logical representation of a set of connections to the Microsoft Cloud Edge at a location.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['PeeringPropertiesDirectArgs']] direct: The properties that define a direct peering.
        :param pulumi.Input[pulumi.InputType['PeeringPropertiesExchangeArgs']] exchange: The properties that define an exchange peering.
        :param pulumi.Input[Union[str, 'Kind']] kind: The kind of the peering.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] peering_location: The location of the peering.
        :param pulumi.Input[str] peering_name: The name of the peering.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['PeeringSkuArgs']] sku: The SKU that defines the tier and kind of the peering.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PeeringArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Peering is a logical representation of a set of connections to the Microsoft Cloud Edge at a location.

        :param str resource_name: The name of the resource.
        :param PeeringArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PeeringArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 direct: Optional[pulumi.Input[pulumi.InputType['PeeringPropertiesDirectArgs']]] = None,
                 exchange: Optional[pulumi.Input[pulumi.InputType['PeeringPropertiesExchangeArgs']]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 peering_location: Optional[pulumi.Input[str]] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['PeeringSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        pulumi.log.warn("""Peering is deprecated: Version 2019-09-01-preview will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PeeringArgs.__new__(PeeringArgs)

            __props__.__dict__["direct"] = direct
            __props__.__dict__["exchange"] = exchange
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["peering_location"] = peering_location
            __props__.__dict__["peering_name"] = peering_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:peering:Peering"), pulumi.Alias(type_="azure-native:peering/v20190801preview:Peering"), pulumi.Alias(type_="azure-native:peering/v20200101preview:Peering"), pulumi.Alias(type_="azure-native:peering/v20200401:Peering"), pulumi.Alias(type_="azure-native:peering/v20201001:Peering"), pulumi.Alias(type_="azure-native:peering/v20210101:Peering"), pulumi.Alias(type_="azure-native:peering/v20210601:Peering"), pulumi.Alias(type_="azure-native:peering/v20220101:Peering"), pulumi.Alias(type_="azure-native:peering/v20220601:Peering")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Peering, __self__).__init__(
            'azure-native:peering/v20190901preview:Peering',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Peering':
        """
        Get an existing Peering resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PeeringArgs.__new__(PeeringArgs)

        __props__.__dict__["direct"] = None
        __props__.__dict__["exchange"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peering_location"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Peering(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def direct(self) -> pulumi.Output[Optional['outputs.PeeringPropertiesDirectResponse']]:
        """
        The properties that define a direct peering.
        """
        return pulumi.get(self, "direct")

    @property
    @pulumi.getter
    def exchange(self) -> pulumi.Output[Optional['outputs.PeeringPropertiesExchangeResponse']]:
        """
        The properties that define an exchange peering.
        """
        return pulumi.get(self, "exchange")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of the peering.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peeringLocation")
    def peering_location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the peering.
        """
        return pulumi.get(self, "peering_location")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.PeeringSkuResponse']:
        """
        The SKU that defines the tier and kind of the peering.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

