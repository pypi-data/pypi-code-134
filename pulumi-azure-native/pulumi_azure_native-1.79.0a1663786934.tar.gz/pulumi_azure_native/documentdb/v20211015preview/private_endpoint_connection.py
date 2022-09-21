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

__all__ = ['PrivateEndpointConnectionArgs', 'PrivateEndpointConnection']

@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 group_id: Optional[pulumi.Input[str]] = None,
                 private_endpoint: Optional[pulumi.Input['PrivateEndpointPropertyArgs']] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input['PrivateLinkServiceConnectionStatePropertyArgs']] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PrivateEndpointConnection resource.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] group_id: Group id of the private endpoint.
        :param pulumi.Input['PrivateEndpointPropertyArgs'] private_endpoint: Private endpoint which the connection belongs to.
        :param pulumi.Input[str] private_endpoint_connection_name: The name of the private endpoint connection.
        :param pulumi.Input['PrivateLinkServiceConnectionStatePropertyArgs'] private_link_service_connection_state: Connection State of the Private Endpoint Connection.
        :param pulumi.Input[str] provisioning_state: Provisioning state of the private endpoint.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if private_endpoint is not None:
            pulumi.set(__self__, "private_endpoint", private_endpoint)
        if private_endpoint_connection_name is not None:
            pulumi.set(__self__, "private_endpoint_connection_name", private_endpoint_connection_name)
        if private_link_service_connection_state is not None:
            pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        Cosmos DB database account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Group id of the private endpoint.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input['PrivateEndpointPropertyArgs']]:
        """
        Private endpoint which the connection belongs to.
        """
        return pulumi.get(self, "private_endpoint")

    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input['PrivateEndpointPropertyArgs']]):
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

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[pulumi.Input['PrivateLinkServiceConnectionStatePropertyArgs']]:
        """
        Connection State of the Private Endpoint Connection.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: Optional[pulumi.Input['PrivateLinkServiceConnectionStatePropertyArgs']]):
        pulumi.set(self, "private_link_service_connection_state", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        Provisioning state of the private endpoint.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)


class PrivateEndpointConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 private_endpoint: Optional[pulumi.Input[pulumi.InputType['PrivateEndpointPropertyArgs']]] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionStatePropertyArgs']]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A private endpoint connection

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input[str] group_id: Group id of the private endpoint.
        :param pulumi.Input[pulumi.InputType['PrivateEndpointPropertyArgs']] private_endpoint: Private endpoint which the connection belongs to.
        :param pulumi.Input[str] private_endpoint_connection_name: The name of the private endpoint connection.
        :param pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionStatePropertyArgs']] private_link_service_connection_state: Connection State of the Private Endpoint Connection.
        :param pulumi.Input[str] provisioning_state: Provisioning state of the private endpoint.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
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
                 account_name: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 private_endpoint: Optional[pulumi.Input[pulumi.InputType['PrivateEndpointPropertyArgs']]] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionStatePropertyArgs']]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrivateEndpointConnectionArgs.__new__(PrivateEndpointConnectionArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["group_id"] = group_id
            __props__.__dict__["private_endpoint"] = private_endpoint
            __props__.__dict__["private_endpoint_connection_name"] = private_endpoint_connection_name
            __props__.__dict__["private_link_service_connection_state"] = private_link_service_connection_state
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:documentdb:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:documentdb/v20190801preview:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:documentdb/v20210115:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:documentdb/v20210301preview:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:documentdb/v20210315:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:documentdb/v20210401preview:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:documentdb/v20210415:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:documentdb/v20210515:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:documentdb/v20210615:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:documentdb/v20210701preview:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:documentdb/v20211015:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:documentdb/v20211115preview:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:documentdb/v20220215preview:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:documentdb/v20220515:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:documentdb/v20220515preview:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:documentdb/v20220815:PrivateEndpointConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateEndpointConnection, __self__).__init__(
            'azure-native:documentdb/v20211015preview:PrivateEndpointConnection',
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

        __props__.__dict__["group_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint"] = None
        __props__.__dict__["private_link_service_connection_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return PrivateEndpointConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[Optional[str]]:
        """
        Group id of the private endpoint.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> pulumi.Output[Optional['outputs.PrivateEndpointPropertyResponse']]:
        """
        Private endpoint which the connection belongs to.
        """
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> pulumi.Output[Optional['outputs.PrivateLinkServiceConnectionStatePropertyResponse']]:
        """
        Connection State of the Private Endpoint Connection.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Provisioning state of the private endpoint.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

