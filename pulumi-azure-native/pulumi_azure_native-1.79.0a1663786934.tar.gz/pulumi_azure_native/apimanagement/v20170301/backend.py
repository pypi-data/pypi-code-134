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

__all__ = ['BackendArgs', 'Backend']

@pulumi.input_type
class BackendArgs:
    def __init__(__self__, *,
                 protocol: pulumi.Input[Union[str, 'BackendProtocol']],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 url: pulumi.Input[str],
                 backendid: Optional[pulumi.Input[str]] = None,
                 credentials: Optional[pulumi.Input['BackendCredentialsContractArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['BackendPropertiesArgs']] = None,
                 proxy: Optional[pulumi.Input['BackendProxyContractArgs']] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 tls: Optional[pulumi.Input['BackendTlsPropertiesArgs']] = None):
        """
        The set of arguments for constructing a Backend resource.
        :param pulumi.Input[Union[str, 'BackendProtocol']] protocol: Backend communication protocol.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] url: Runtime Url of the Backend.
        :param pulumi.Input[str] backendid: Identifier of the Backend entity. Must be unique in the current API Management service instance.
        :param pulumi.Input['BackendCredentialsContractArgs'] credentials: Backend Credentials Contract Properties
        :param pulumi.Input[str] description: Backend Description.
        :param pulumi.Input['BackendPropertiesArgs'] properties: Backend Properties contract
        :param pulumi.Input['BackendProxyContractArgs'] proxy: Backend Proxy Contract Properties
        :param pulumi.Input[str] resource_id: Management Uri of the Resource in External System. This url can be the Arm Resource Id of Logic Apps, Function Apps or Api Apps.
        :param pulumi.Input[str] title: Backend Title.
        :param pulumi.Input['BackendTlsPropertiesArgs'] tls: Backend TLS Properties
        """
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "url", url)
        if backendid is not None:
            pulumi.set(__self__, "backendid", backendid)
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if proxy is not None:
            pulumi.set(__self__, "proxy", proxy)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if tls is not None:
            pulumi.set(__self__, "tls", tls)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[Union[str, 'BackendProtocol']]:
        """
        Backend communication protocol.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[Union[str, 'BackendProtocol']]):
        pulumi.set(self, "protocol", value)

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
    def url(self) -> pulumi.Input[str]:
        """
        Runtime Url of the Backend.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def backendid(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the Backend entity. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "backendid")

    @backendid.setter
    def backendid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backendid", value)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input['BackendCredentialsContractArgs']]:
        """
        Backend Credentials Contract Properties
        """
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input['BackendCredentialsContractArgs']]):
        pulumi.set(self, "credentials", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Backend Description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['BackendPropertiesArgs']]:
        """
        Backend Properties contract
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['BackendPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def proxy(self) -> Optional[pulumi.Input['BackendProxyContractArgs']]:
        """
        Backend Proxy Contract Properties
        """
        return pulumi.get(self, "proxy")

    @proxy.setter
    def proxy(self, value: Optional[pulumi.Input['BackendProxyContractArgs']]):
        pulumi.set(self, "proxy", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Management Uri of the Resource in External System. This url can be the Arm Resource Id of Logic Apps, Function Apps or Api Apps.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        Backend Title.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def tls(self) -> Optional[pulumi.Input['BackendTlsPropertiesArgs']]:
        """
        Backend TLS Properties
        """
        return pulumi.get(self, "tls")

    @tls.setter
    def tls(self, value: Optional[pulumi.Input['BackendTlsPropertiesArgs']]):
        pulumi.set(self, "tls", value)


class Backend(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backendid: Optional[pulumi.Input[str]] = None,
                 credentials: Optional[pulumi.Input[pulumi.InputType['BackendCredentialsContractArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['BackendPropertiesArgs']]] = None,
                 protocol: Optional[pulumi.Input[Union[str, 'BackendProtocol']]] = None,
                 proxy: Optional[pulumi.Input[pulumi.InputType['BackendProxyContractArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 tls: Optional[pulumi.Input[pulumi.InputType['BackendTlsPropertiesArgs']]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Backend details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backendid: Identifier of the Backend entity. Must be unique in the current API Management service instance.
        :param pulumi.Input[pulumi.InputType['BackendCredentialsContractArgs']] credentials: Backend Credentials Contract Properties
        :param pulumi.Input[str] description: Backend Description.
        :param pulumi.Input[pulumi.InputType['BackendPropertiesArgs']] properties: Backend Properties contract
        :param pulumi.Input[Union[str, 'BackendProtocol']] protocol: Backend communication protocol.
        :param pulumi.Input[pulumi.InputType['BackendProxyContractArgs']] proxy: Backend Proxy Contract Properties
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_id: Management Uri of the Resource in External System. This url can be the Arm Resource Id of Logic Apps, Function Apps or Api Apps.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] title: Backend Title.
        :param pulumi.Input[pulumi.InputType['BackendTlsPropertiesArgs']] tls: Backend TLS Properties
        :param pulumi.Input[str] url: Runtime Url of the Backend.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BackendArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Backend details.

        :param str resource_name: The name of the resource.
        :param BackendArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BackendArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backendid: Optional[pulumi.Input[str]] = None,
                 credentials: Optional[pulumi.Input[pulumi.InputType['BackendCredentialsContractArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['BackendPropertiesArgs']]] = None,
                 protocol: Optional[pulumi.Input[Union[str, 'BackendProtocol']]] = None,
                 proxy: Optional[pulumi.Input[pulumi.InputType['BackendProxyContractArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 tls: Optional[pulumi.Input[pulumi.InputType['BackendTlsPropertiesArgs']]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BackendArgs.__new__(BackendArgs)

            __props__.__dict__["backendid"] = backendid
            __props__.__dict__["credentials"] = credentials
            __props__.__dict__["description"] = description
            __props__.__dict__["properties"] = properties
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            __props__.__dict__["proxy"] = proxy
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_id"] = resource_id
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["title"] = title
            __props__.__dict__["tls"] = tls
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement:Backend"), pulumi.Alias(type_="azure-native:apimanagement/v20160707:Backend"), pulumi.Alias(type_="azure-native:apimanagement/v20161010:Backend"), pulumi.Alias(type_="azure-native:apimanagement/v20180101:Backend"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:Backend"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:Backend"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:Backend"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:Backend"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:Backend"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:Backend"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:Backend"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:Backend"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:Backend"), pulumi.Alias(type_="azure-native:apimanagement/v20211201preview:Backend")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Backend, __self__).__init__(
            'azure-native:apimanagement/v20170301:Backend',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Backend':
        """
        Get an existing Backend resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BackendArgs.__new__(BackendArgs)

        __props__.__dict__["credentials"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["protocol"] = None
        __props__.__dict__["proxy"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["title"] = None
        __props__.__dict__["tls"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["url"] = None
        return Backend(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional['outputs.BackendCredentialsContractResponse']]:
        """
        Backend Credentials Contract Properties
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Backend Description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.BackendPropertiesResponse']:
        """
        Backend Properties contract
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        Backend communication protocol.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def proxy(self) -> pulumi.Output[Optional['outputs.BackendProxyContractResponse']]:
        """
        Backend Proxy Contract Properties
        """
        return pulumi.get(self, "proxy")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        Management Uri of the Resource in External System. This url can be the Arm Resource Id of Logic Apps, Function Apps or Api Apps.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[str]]:
        """
        Backend Title.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def tls(self) -> pulumi.Output[Optional['outputs.BackendTlsPropertiesResponse']]:
        """
        Backend TLS Properties
        """
        return pulumi.get(self, "tls")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        Runtime Url of the Backend.
        """
        return pulumi.get(self, "url")

