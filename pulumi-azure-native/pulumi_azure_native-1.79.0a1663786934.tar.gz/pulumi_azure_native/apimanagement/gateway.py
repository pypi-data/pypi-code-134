# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['GatewayArgs', 'Gateway']

@pulumi.input_type
class GatewayArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 location_data: Optional[pulumi.Input['ResourceLocationDataContractArgs']] = None):
        """
        The set of arguments for constructing a Gateway resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] description: Gateway description
        :param pulumi.Input[str] gateway_id: Gateway entity identifier. Must be unique in the current API Management service instance. Must not have value 'managed'
        :param pulumi.Input['ResourceLocationDataContractArgs'] location_data: Gateway location.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if gateway_id is not None:
            pulumi.set(__self__, "gateway_id", gateway_id)
        if location_data is not None:
            pulumi.set(__self__, "location_data", location_data)

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
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Gateway description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gateway entity identifier. Must be unique in the current API Management service instance. Must not have value 'managed'
        """
        return pulumi.get(self, "gateway_id")

    @gateway_id.setter
    def gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_id", value)

    @property
    @pulumi.getter(name="locationData")
    def location_data(self) -> Optional[pulumi.Input['ResourceLocationDataContractArgs']]:
        """
        Gateway location.
        """
        return pulumi.get(self, "location_data")

    @location_data.setter
    def location_data(self, value: Optional[pulumi.Input['ResourceLocationDataContractArgs']]):
        pulumi.set(self, "location_data", value)


class Gateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 location_data: Optional[pulumi.Input[pulumi.InputType['ResourceLocationDataContractArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Gateway details.
        API Version: 2020-12-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Gateway description
        :param pulumi.Input[str] gateway_id: Gateway entity identifier. Must be unique in the current API Management service instance. Must not have value 'managed'
        :param pulumi.Input[pulumi.InputType['ResourceLocationDataContractArgs']] location_data: Gateway location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Gateway details.
        API Version: 2020-12-01.

        :param str resource_name: The name of the resource.
        :param GatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 location_data: Optional[pulumi.Input[pulumi.InputType['ResourceLocationDataContractArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GatewayArgs.__new__(GatewayArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["gateway_id"] = gateway_id
            __props__.__dict__["location_data"] = location_data
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement/v20191201:Gateway"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:Gateway"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:Gateway"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:Gateway"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:Gateway"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:Gateway"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:Gateway"), pulumi.Alias(type_="azure-native:apimanagement/v20211201preview:Gateway")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Gateway, __self__).__init__(
            'azure-native:apimanagement:Gateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Gateway':
        """
        Get an existing Gateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GatewayArgs.__new__(GatewayArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["location_data"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return Gateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Gateway description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="locationData")
    def location_data(self) -> pulumi.Output[Optional['outputs.ResourceLocationDataContractResponse']]:
        """
        Gateway location.
        """
        return pulumi.get(self, "location_data")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

