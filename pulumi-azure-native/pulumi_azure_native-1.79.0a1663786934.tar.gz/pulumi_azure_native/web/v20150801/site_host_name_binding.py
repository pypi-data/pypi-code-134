# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['SiteHostNameBindingArgs', 'SiteHostNameBinding']

@pulumi.input_type
class SiteHostNameBindingArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 azure_resource_name: Optional[pulumi.Input[str]] = None,
                 azure_resource_type: Optional[pulumi.Input['AzureResourceType']] = None,
                 custom_host_name_dns_record_type: Optional[pulumi.Input['CustomHostNameDnsRecordType']] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 host_name_type: Optional[pulumi.Input['HostNameType']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SiteHostNameBinding resource.
        :param pulumi.Input[str] name: Resource Name
        :param pulumi.Input[str] resource_group_name: Name of resource group
        :param pulumi.Input[str] azure_resource_name: Azure resource name
        :param pulumi.Input['AzureResourceType'] azure_resource_type: Azure resource type
        :param pulumi.Input['CustomHostNameDnsRecordType'] custom_host_name_dns_record_type: Custom DNS record type
        :param pulumi.Input[str] domain_id: Fully qualified ARM domain resource URI
        :param pulumi.Input[str] host_name: Name of host
        :param pulumi.Input['HostNameType'] host_name_type: Host name type
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[str] kind: Kind of resource
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[str] site_name: Web app name
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] type: Resource type
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if azure_resource_name is not None:
            pulumi.set(__self__, "azure_resource_name", azure_resource_name)
        if azure_resource_type is not None:
            pulumi.set(__self__, "azure_resource_type", azure_resource_type)
        if custom_host_name_dns_record_type is not None:
            pulumi.set(__self__, "custom_host_name_dns_record_type", custom_host_name_dns_record_type)
        if domain_id is not None:
            pulumi.set(__self__, "domain_id", domain_id)
        if host_name is not None:
            pulumi.set(__self__, "host_name", host_name)
        if host_name_type is not None:
            pulumi.set(__self__, "host_name_type", host_name_type)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if site_name is not None:
            pulumi.set(__self__, "site_name", site_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of resource group
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="azureResourceName")
    def azure_resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        Azure resource name
        """
        return pulumi.get(self, "azure_resource_name")

    @azure_resource_name.setter
    def azure_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "azure_resource_name", value)

    @property
    @pulumi.getter(name="azureResourceType")
    def azure_resource_type(self) -> Optional[pulumi.Input['AzureResourceType']]:
        """
        Azure resource type
        """
        return pulumi.get(self, "azure_resource_type")

    @azure_resource_type.setter
    def azure_resource_type(self, value: Optional[pulumi.Input['AzureResourceType']]):
        pulumi.set(self, "azure_resource_type", value)

    @property
    @pulumi.getter(name="customHostNameDnsRecordType")
    def custom_host_name_dns_record_type(self) -> Optional[pulumi.Input['CustomHostNameDnsRecordType']]:
        """
        Custom DNS record type
        """
        return pulumi.get(self, "custom_host_name_dns_record_type")

    @custom_host_name_dns_record_type.setter
    def custom_host_name_dns_record_type(self, value: Optional[pulumi.Input['CustomHostNameDnsRecordType']]):
        pulumi.set(self, "custom_host_name_dns_record_type", value)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[str]]:
        """
        Fully qualified ARM domain resource URI
        """
        return pulumi.get(self, "domain_id")

    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_id", value)

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of host
        """
        return pulumi.get(self, "host_name")

    @host_name.setter
    def host_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_name", value)

    @property
    @pulumi.getter(name="hostNameType")
    def host_name_type(self) -> Optional[pulumi.Input['HostNameType']]:
        """
        Host name type
        """
        return pulumi.get(self, "host_name_type")

    @host_name_type.setter
    def host_name_type(self, value: Optional[pulumi.Input['HostNameType']]):
        pulumi.set(self, "host_name_type", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="siteName")
    def site_name(self) -> Optional[pulumi.Input[str]]:
        """
        Web app name
        """
        return pulumi.get(self, "site_name")

    @site_name.setter
    def site_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "site_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


warnings.warn("""Version 2015-08-01 will be removed in v2 of the provider.""", DeprecationWarning)


class SiteHostNameBinding(pulumi.CustomResource):
    warnings.warn("""Version 2015-08-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_resource_name: Optional[pulumi.Input[str]] = None,
                 azure_resource_type: Optional[pulumi.Input['AzureResourceType']] = None,
                 custom_host_name_dns_record_type: Optional[pulumi.Input['CustomHostNameDnsRecordType']] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 host_name_type: Optional[pulumi.Input['HostNameType']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A host name binding object

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] azure_resource_name: Azure resource name
        :param pulumi.Input['AzureResourceType'] azure_resource_type: Azure resource type
        :param pulumi.Input['CustomHostNameDnsRecordType'] custom_host_name_dns_record_type: Custom DNS record type
        :param pulumi.Input[str] domain_id: Fully qualified ARM domain resource URI
        :param pulumi.Input[str] host_name: Name of host
        :param pulumi.Input['HostNameType'] host_name_type: Host name type
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[str] kind: Kind of resource
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[str] name: Resource Name
        :param pulumi.Input[str] resource_group_name: Name of resource group
        :param pulumi.Input[str] site_name: Web app name
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] type: Resource type
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SiteHostNameBindingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A host name binding object

        :param str resource_name: The name of the resource.
        :param SiteHostNameBindingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SiteHostNameBindingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_resource_name: Optional[pulumi.Input[str]] = None,
                 azure_resource_type: Optional[pulumi.Input['AzureResourceType']] = None,
                 custom_host_name_dns_record_type: Optional[pulumi.Input['CustomHostNameDnsRecordType']] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 host_name_type: Optional[pulumi.Input['HostNameType']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""SiteHostNameBinding is deprecated: Version 2015-08-01 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SiteHostNameBindingArgs.__new__(SiteHostNameBindingArgs)

            __props__.__dict__["azure_resource_name"] = azure_resource_name
            __props__.__dict__["azure_resource_type"] = azure_resource_type
            __props__.__dict__["custom_host_name_dns_record_type"] = custom_host_name_dns_record_type
            __props__.__dict__["domain_id"] = domain_id
            __props__.__dict__["host_name"] = host_name
            __props__.__dict__["host_name_type"] = host_name_type
            __props__.__dict__["id"] = id
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["site_name"] = site_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = type
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:web:SiteHostNameBinding"), pulumi.Alias(type_="azure-native:web/v20160801:SiteHostNameBinding"), pulumi.Alias(type_="azure-native:web/v20180201:SiteHostNameBinding"), pulumi.Alias(type_="azure-native:web/v20181101:SiteHostNameBinding"), pulumi.Alias(type_="azure-native:web/v20190801:SiteHostNameBinding"), pulumi.Alias(type_="azure-native:web/v20200601:SiteHostNameBinding"), pulumi.Alias(type_="azure-native:web/v20200901:SiteHostNameBinding"), pulumi.Alias(type_="azure-native:web/v20201001:SiteHostNameBinding"), pulumi.Alias(type_="azure-native:web/v20201201:SiteHostNameBinding"), pulumi.Alias(type_="azure-native:web/v20210101:SiteHostNameBinding"), pulumi.Alias(type_="azure-native:web/v20210115:SiteHostNameBinding"), pulumi.Alias(type_="azure-native:web/v20210201:SiteHostNameBinding"), pulumi.Alias(type_="azure-native:web/v20210301:SiteHostNameBinding"), pulumi.Alias(type_="azure-native:web/v20220301:SiteHostNameBinding")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SiteHostNameBinding, __self__).__init__(
            'azure-native:web/v20150801:SiteHostNameBinding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SiteHostNameBinding':
        """
        Get an existing SiteHostNameBinding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SiteHostNameBindingArgs.__new__(SiteHostNameBindingArgs)

        __props__.__dict__["azure_resource_name"] = None
        __props__.__dict__["azure_resource_type"] = None
        __props__.__dict__["custom_host_name_dns_record_type"] = None
        __props__.__dict__["domain_id"] = None
        __props__.__dict__["host_name_type"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["site_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return SiteHostNameBinding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureResourceName")
    def azure_resource_name(self) -> pulumi.Output[Optional[str]]:
        """
        Azure resource name
        """
        return pulumi.get(self, "azure_resource_name")

    @property
    @pulumi.getter(name="azureResourceType")
    def azure_resource_type(self) -> pulumi.Output[Optional[str]]:
        """
        Azure resource type
        """
        return pulumi.get(self, "azure_resource_type")

    @property
    @pulumi.getter(name="customHostNameDnsRecordType")
    def custom_host_name_dns_record_type(self) -> pulumi.Output[Optional[str]]:
        """
        Custom DNS record type
        """
        return pulumi.get(self, "custom_host_name_dns_record_type")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[Optional[str]]:
        """
        Fully qualified ARM domain resource URI
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="hostNameType")
    def host_name_type(self) -> pulumi.Output[Optional[str]]:
        """
        Host name type
        """
        return pulumi.get(self, "host_name_type")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="siteName")
    def site_name(self) -> pulumi.Output[Optional[str]]:
        """
        Web app name
        """
        return pulumi.get(self, "site_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

