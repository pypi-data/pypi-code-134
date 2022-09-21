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
from ._inputs import *

__all__ = ['ExpressRouteGatewayArgs', 'ExpressRouteGateway']

@pulumi.input_type
class ExpressRouteGatewayArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 virtual_hub: pulumi.Input['VirtualHubIdArgs'],
                 auto_scale_configuration: Optional[pulumi.Input['ExpressRouteGatewayPropertiesAutoScaleConfigurationArgs']] = None,
                 express_route_gateway_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ExpressRouteGateway resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['VirtualHubIdArgs'] virtual_hub: The Virtual Hub where the ExpressRoute gateway is or will be deployed.
        :param pulumi.Input['ExpressRouteGatewayPropertiesAutoScaleConfigurationArgs'] auto_scale_configuration: Configuration for auto scaling.
        :param pulumi.Input[str] express_route_gateway_name: The name of the ExpressRoute gateway.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "virtual_hub", virtual_hub)
        if auto_scale_configuration is not None:
            pulumi.set(__self__, "auto_scale_configuration", auto_scale_configuration)
        if express_route_gateway_name is not None:
            pulumi.set(__self__, "express_route_gateway_name", express_route_gateway_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
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
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> pulumi.Input['VirtualHubIdArgs']:
        """
        The Virtual Hub where the ExpressRoute gateway is or will be deployed.
        """
        return pulumi.get(self, "virtual_hub")

    @virtual_hub.setter
    def virtual_hub(self, value: pulumi.Input['VirtualHubIdArgs']):
        pulumi.set(self, "virtual_hub", value)

    @property
    @pulumi.getter(name="autoScaleConfiguration")
    def auto_scale_configuration(self) -> Optional[pulumi.Input['ExpressRouteGatewayPropertiesAutoScaleConfigurationArgs']]:
        """
        Configuration for auto scaling.
        """
        return pulumi.get(self, "auto_scale_configuration")

    @auto_scale_configuration.setter
    def auto_scale_configuration(self, value: Optional[pulumi.Input['ExpressRouteGatewayPropertiesAutoScaleConfigurationArgs']]):
        pulumi.set(self, "auto_scale_configuration", value)

    @property
    @pulumi.getter(name="expressRouteGatewayName")
    def express_route_gateway_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ExpressRoute gateway.
        """
        return pulumi.get(self, "express_route_gateway_name")

    @express_route_gateway_name.setter
    def express_route_gateway_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "express_route_gateway_name", value)

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


class ExpressRouteGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_scale_configuration: Optional[pulumi.Input[pulumi.InputType['ExpressRouteGatewayPropertiesAutoScaleConfigurationArgs']]] = None,
                 express_route_gateway_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub: Optional[pulumi.Input[pulumi.InputType['VirtualHubIdArgs']]] = None,
                 __props__=None):
        """
        ExpressRoute gateway resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ExpressRouteGatewayPropertiesAutoScaleConfigurationArgs']] auto_scale_configuration: Configuration for auto scaling.
        :param pulumi.Input[str] express_route_gateway_name: The name of the ExpressRoute gateway.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[pulumi.InputType['VirtualHubIdArgs']] virtual_hub: The Virtual Hub where the ExpressRoute gateway is or will be deployed.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExpressRouteGatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ExpressRoute gateway resource.

        :param str resource_name: The name of the resource.
        :param ExpressRouteGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExpressRouteGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_scale_configuration: Optional[pulumi.Input[pulumi.InputType['ExpressRouteGatewayPropertiesAutoScaleConfigurationArgs']]] = None,
                 express_route_gateway_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub: Optional[pulumi.Input[pulumi.InputType['VirtualHubIdArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExpressRouteGatewayArgs.__new__(ExpressRouteGatewayArgs)

            __props__.__dict__["auto_scale_configuration"] = auto_scale_configuration
            __props__.__dict__["express_route_gateway_name"] = express_route_gateway_name
            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            if virtual_hub is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_hub'")
            __props__.__dict__["virtual_hub"] = virtual_hub
            __props__.__dict__["etag"] = None
            __props__.__dict__["express_route_connections"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20180801:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20181001:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20181101:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20181201:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20190201:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20190401:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20190601:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20190801:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20190901:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20191101:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20191201:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20200301:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20200401:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20200501:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20200601:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20200701:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20200801:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20201101:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20210201:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20210301:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20210501:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20210801:ExpressRouteGateway"), pulumi.Alias(type_="azure-native:network/v20220101:ExpressRouteGateway")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ExpressRouteGateway, __self__).__init__(
            'azure-native:network/v20190701:ExpressRouteGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ExpressRouteGateway':
        """
        Get an existing ExpressRouteGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExpressRouteGatewayArgs.__new__(ExpressRouteGatewayArgs)

        __props__.__dict__["auto_scale_configuration"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["express_route_connections"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_hub"] = None
        return ExpressRouteGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoScaleConfiguration")
    def auto_scale_configuration(self) -> pulumi.Output[Optional['outputs.ExpressRouteGatewayPropertiesResponseAutoScaleConfiguration']]:
        """
        Configuration for auto scaling.
        """
        return pulumi.get(self, "auto_scale_configuration")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="expressRouteConnections")
    def express_route_connections(self) -> pulumi.Output[Sequence['outputs.ExpressRouteConnectionResponse']]:
        """
        List of ExpressRoute connections to the ExpressRoute gateway.
        """
        return pulumi.get(self, "express_route_connections")

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
        The provisioning state of the express route gateway resource.
        """
        return pulumi.get(self, "provisioning_state")

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
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> pulumi.Output['outputs.VirtualHubIdResponse']:
        """
        The Virtual Hub where the ExpressRoute gateway is or will be deployed.
        """
        return pulumi.get(self, "virtual_hub")

