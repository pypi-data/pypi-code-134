# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['OpenIdConnectProviderArgs', 'OpenIdConnectProvider']

@pulumi.input_type
class OpenIdConnectProviderArgs:
    def __init__(__self__, *,
                 client_id: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 metadata_endpoint: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 client_secret: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 opid: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OpenIdConnectProvider resource.
        :param pulumi.Input[str] client_id: Client ID of developer console which is the client application.
        :param pulumi.Input[str] display_name: User-friendly OpenID Connect Provider name.
        :param pulumi.Input[str] metadata_endpoint: Metadata endpoint URI.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] client_secret: Client Secret of developer console which is the client application.
        :param pulumi.Input[str] description: User-friendly description of OpenID Connect Provider.
        :param pulumi.Input[str] opid: Identifier of the OpenID Connect Provider.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "metadata_endpoint", metadata_endpoint)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if client_secret is not None:
            pulumi.set(__self__, "client_secret", client_secret)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if opid is not None:
            pulumi.set(__self__, "opid", opid)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[str]:
        """
        Client ID of developer console which is the client application.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        User-friendly OpenID Connect Provider name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="metadataEndpoint")
    def metadata_endpoint(self) -> pulumi.Input[str]:
        """
        Metadata endpoint URI.
        """
        return pulumi.get(self, "metadata_endpoint")

    @metadata_endpoint.setter
    def metadata_endpoint(self, value: pulumi.Input[str]):
        pulumi.set(self, "metadata_endpoint", value)

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
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[str]]:
        """
        Client Secret of developer console which is the client application.
        """
        return pulumi.get(self, "client_secret")

    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_secret", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        User-friendly description of OpenID Connect Provider.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def opid(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the OpenID Connect Provider.
        """
        return pulumi.get(self, "opid")

    @opid.setter
    def opid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "opid", value)


class OpenIdConnectProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 metadata_endpoint: Optional[pulumi.Input[str]] = None,
                 opid: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        OpenId Connect Provider details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_id: Client ID of developer console which is the client application.
        :param pulumi.Input[str] client_secret: Client Secret of developer console which is the client application.
        :param pulumi.Input[str] description: User-friendly description of OpenID Connect Provider.
        :param pulumi.Input[str] display_name: User-friendly OpenID Connect Provider name.
        :param pulumi.Input[str] metadata_endpoint: Metadata endpoint URI.
        :param pulumi.Input[str] opid: Identifier of the OpenID Connect Provider.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OpenIdConnectProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        OpenId Connect Provider details.

        :param str resource_name: The name of the resource.
        :param OpenIdConnectProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OpenIdConnectProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 metadata_endpoint: Optional[pulumi.Input[str]] = None,
                 opid: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OpenIdConnectProviderArgs.__new__(OpenIdConnectProviderArgs)

            if client_id is None and not opts.urn:
                raise TypeError("Missing required property 'client_id'")
            __props__.__dict__["client_id"] = client_id
            __props__.__dict__["client_secret"] = client_secret
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            if metadata_endpoint is None and not opts.urn:
                raise TypeError("Missing required property 'metadata_endpoint'")
            __props__.__dict__["metadata_endpoint"] = metadata_endpoint
            __props__.__dict__["opid"] = opid
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement:OpenIdConnectProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20160707:OpenIdConnectProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20161010:OpenIdConnectProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20170301:OpenIdConnectProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20180101:OpenIdConnectProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:OpenIdConnectProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:OpenIdConnectProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:OpenIdConnectProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:OpenIdConnectProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:OpenIdConnectProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:OpenIdConnectProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:OpenIdConnectProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:OpenIdConnectProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:OpenIdConnectProvider")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(OpenIdConnectProvider, __self__).__init__(
            'azure-native:apimanagement/v20211201preview:OpenIdConnectProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OpenIdConnectProvider':
        """
        Get an existing OpenIdConnectProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OpenIdConnectProviderArgs.__new__(OpenIdConnectProviderArgs)

        __props__.__dict__["client_id"] = None
        __props__.__dict__["client_secret"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["metadata_endpoint"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return OpenIdConnectProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[str]:
        """
        Client ID of developer console which is the client application.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Output[Optional[str]]:
        """
        Client Secret of developer console which is the client application.
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        User-friendly description of OpenID Connect Provider.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        User-friendly OpenID Connect Provider name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="metadataEndpoint")
    def metadata_endpoint(self) -> pulumi.Output[str]:
        """
        Metadata endpoint URI.
        """
        return pulumi.get(self, "metadata_endpoint")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

