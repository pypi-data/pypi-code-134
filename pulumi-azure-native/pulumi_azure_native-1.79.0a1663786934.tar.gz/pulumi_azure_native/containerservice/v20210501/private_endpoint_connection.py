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

__all__ = ['PrivateEndpointConnectionArgs', 'PrivateEndpointConnection']

@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(__self__, *,
                 private_link_service_connection_state: pulumi.Input['PrivateLinkServiceConnectionStateArgs'],
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 private_endpoint: Optional[pulumi.Input['PrivateEndpointArgs']] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PrivateEndpointConnection resource.
        :param pulumi.Input['PrivateLinkServiceConnectionStateArgs'] private_link_service_connection_state: A collection of information about the state of the connection between service consumer and provider.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_name: The name of the managed cluster resource.
        :param pulumi.Input['PrivateEndpointArgs'] private_endpoint: The resource of private endpoint.
        :param pulumi.Input[str] private_endpoint_connection_name: The name of the private endpoint connection.
        """
        pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        if private_endpoint is not None:
            pulumi.set(__self__, "private_endpoint", private_endpoint)
        if private_endpoint_connection_name is not None:
            pulumi.set(__self__, "private_endpoint_connection_name", private_endpoint_connection_name)

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> pulumi.Input['PrivateLinkServiceConnectionStateArgs']:
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: pulumi.Input['PrivateLinkServiceConnectionStateArgs']):
        pulumi.set(self, "private_link_service_connection_state", value)

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
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        The name of the managed cluster resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input['PrivateEndpointArgs']]:
        """
        The resource of private endpoint.
        """
        return pulumi.get(self, "private_endpoint")

    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input['PrivateEndpointArgs']]):
        pulumi.set(self, "private_endpoint", value)

    @property
    @pulumi.getter(name="privateEndpointConnectionName")
    def private_endpoint_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the private endpoint connection.
        """
        return pulumi.get(self, "private_endpoint_connection_name")

    @private_endpoint_connection_name.setter
    def private_endpoint_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_endpoint_connection_name", value)


class PrivateEndpointConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 private_endpoint: Optional[pulumi.Input[pulumi.InputType['PrivateEndpointArgs']]] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionStateArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A private endpoint connection

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['PrivateEndpointArgs']] private_endpoint: The resource of private endpoint.
        :param pulumi.Input[str] private_endpoint_connection_name: The name of the private endpoint connection.
        :param pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionStateArgs']] private_link_service_connection_state: A collection of information about the state of the connection between service consumer and provider.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_name_: The name of the managed cluster resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateEndpointConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A private endpoint connection

        :param str resource_name: The name of the resource.
        :param PrivateEndpointConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateEndpointConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 private_endpoint: Optional[pulumi.Input[pulumi.InputType['PrivateEndpointArgs']]] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionStateArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrivateEndpointConnectionArgs.__new__(PrivateEndpointConnectionArgs)

            __props__.__dict__["private_endpoint"] = private_endpoint
            __props__.__dict__["private_endpoint_connection_name"] = private_endpoint_connection_name
            if private_link_service_connection_state is None and not opts.urn:
                raise TypeError("Missing required property 'private_link_service_connection_state'")
            __props__.__dict__["private_link_service_connection_state"] = private_link_service_connection_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerservice:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20200601:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20200701:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20200901:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20201101:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20201201:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20210201:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20210301:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20210701:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20210801:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20210901:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20211001:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20211101preview:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20220101:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20220102preview:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20220201:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20220202preview:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20220301:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20220302preview:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20220401:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20220402preview:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20220502preview:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20220601:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20220602preview:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20220701:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20220702preview:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:containerservice/v20220802preview:PrivateEndpointConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateEndpointConnection, __self__).__init__(
            'azure-native:containerservice/v20210501:PrivateEndpointConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateEndpointConnection':
        """
        Get an existing PrivateEndpointConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrivateEndpointConnectionArgs.__new__(PrivateEndpointConnectionArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint"] = None
        __props__.__dict__["private_link_service_connection_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return PrivateEndpointConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the private endpoint connection.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> pulumi.Output[Optional['outputs.PrivateEndpointResponse']]:
        """
        The resource of private endpoint.
        """
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> pulumi.Output['outputs.PrivateLinkServiceConnectionStateResponse']:
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The current provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

