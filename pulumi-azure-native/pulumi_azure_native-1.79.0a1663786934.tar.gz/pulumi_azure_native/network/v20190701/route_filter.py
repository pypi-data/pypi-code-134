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

__all__ = ['RouteFilterArgs', 'RouteFilter']

@pulumi.input_type
class RouteFilterArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 id: Optional[pulumi.Input[str]] = None,
                 ipv6_peerings: Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitPeeringArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 peerings: Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitPeeringArgs']]]] = None,
                 route_filter_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['RouteFilterRuleArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a RouteFilter resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitPeeringArgs']]] ipv6_peerings: A collection of references to express route circuit ipv6 peerings.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitPeeringArgs']]] peerings: A collection of references to express route circuit peerings.
        :param pulumi.Input[str] route_filter_name: The name of the route filter.
        :param pulumi.Input[Sequence[pulumi.Input['RouteFilterRuleArgs']]] rules: Collection of RouteFilterRules contained within a route filter.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if ipv6_peerings is not None:
            pulumi.set(__self__, "ipv6_peerings", ipv6_peerings)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if peerings is not None:
            pulumi.set(__self__, "peerings", peerings)
        if route_filter_name is not None:
            pulumi.set(__self__, "route_filter_name", route_filter_name)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
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
    @pulumi.getter(name="ipv6Peerings")
    def ipv6_peerings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitPeeringArgs']]]]:
        """
        A collection of references to express route circuit ipv6 peerings.
        """
        return pulumi.get(self, "ipv6_peerings")

    @ipv6_peerings.setter
    def ipv6_peerings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitPeeringArgs']]]]):
        pulumi.set(self, "ipv6_peerings", value)

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
    def peerings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitPeeringArgs']]]]:
        """
        A collection of references to express route circuit peerings.
        """
        return pulumi.get(self, "peerings")

    @peerings.setter
    def peerings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitPeeringArgs']]]]):
        pulumi.set(self, "peerings", value)

    @property
    @pulumi.getter(name="routeFilterName")
    def route_filter_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the route filter.
        """
        return pulumi.get(self, "route_filter_name")

    @route_filter_name.setter
    def route_filter_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "route_filter_name", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RouteFilterRuleArgs']]]]:
        """
        Collection of RouteFilterRules contained within a route filter.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RouteFilterRuleArgs']]]]):
        pulumi.set(self, "rules", value)

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


class RouteFilter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 ipv6_peerings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExpressRouteCircuitPeeringArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 peerings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExpressRouteCircuitPeeringArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 route_filter_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouteFilterRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Route Filter Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExpressRouteCircuitPeeringArgs']]]] ipv6_peerings: A collection of references to express route circuit ipv6 peerings.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExpressRouteCircuitPeeringArgs']]]] peerings: A collection of references to express route circuit peerings.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] route_filter_name: The name of the route filter.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouteFilterRuleArgs']]]] rules: Collection of RouteFilterRules contained within a route filter.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RouteFilterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Route Filter Resource.

        :param str resource_name: The name of the resource.
        :param RouteFilterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RouteFilterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 ipv6_peerings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExpressRouteCircuitPeeringArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 peerings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExpressRouteCircuitPeeringArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 route_filter_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouteFilterRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RouteFilterArgs.__new__(RouteFilterArgs)

            __props__.__dict__["id"] = id
            __props__.__dict__["ipv6_peerings"] = ipv6_peerings
            __props__.__dict__["location"] = location
            __props__.__dict__["peerings"] = peerings
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["route_filter_name"] = route_filter_name
            __props__.__dict__["rules"] = rules
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20161201:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20170301:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20170601:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20170801:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20170901:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20171001:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20171101:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20180101:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20180201:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20180401:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20180601:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20180701:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20180801:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20181001:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20181101:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20181201:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20190201:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20190401:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20190601:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20190801:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20190901:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20191101:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20191201:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20200301:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20200401:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20200501:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20200601:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20200701:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20200801:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20201101:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20210201:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20210301:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20210501:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20210801:RouteFilter"), pulumi.Alias(type_="azure-native:network/v20220101:RouteFilter")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RouteFilter, __self__).__init__(
            'azure-native:network/v20190701:RouteFilter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RouteFilter':
        """
        Get an existing RouteFilter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RouteFilterArgs.__new__(RouteFilterArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["ipv6_peerings"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peerings"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["rules"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return RouteFilter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="ipv6Peerings")
    def ipv6_peerings(self) -> pulumi.Output[Optional[Sequence['outputs.ExpressRouteCircuitPeeringResponse']]]:
        """
        A collection of references to express route circuit ipv6 peerings.
        """
        return pulumi.get(self, "ipv6_peerings")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
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
    @pulumi.getter
    def peerings(self) -> pulumi.Output[Optional[Sequence['outputs.ExpressRouteCircuitPeeringResponse']]]:
        """
        A collection of references to express route circuit peerings.
        """
        return pulumi.get(self, "peerings")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the route filter resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence['outputs.RouteFilterRuleResponse']]]:
        """
        Collection of RouteFilterRules contained within a route filter.
        """
        return pulumi.get(self, "rules")

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

