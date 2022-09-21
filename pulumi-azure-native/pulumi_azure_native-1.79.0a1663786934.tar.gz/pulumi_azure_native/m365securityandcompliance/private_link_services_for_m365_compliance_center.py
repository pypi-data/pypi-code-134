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
from ._enums import *
from ._inputs import *

__all__ = ['PrivateLinkServicesForM365ComplianceCenterArgs', 'PrivateLinkServicesForM365ComplianceCenter']

@pulumi.input_type
class PrivateLinkServicesForM365ComplianceCenterArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input['Kind'],
                 resource_group_name: pulumi.Input[str],
                 identity: Optional[pulumi.Input['ServicesResourceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['ServicesPropertiesArgs']] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a PrivateLinkServicesForM365ComplianceCenter resource.
        :param pulumi.Input['Kind'] kind: The kind of the service.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the service instance.
        :param pulumi.Input['ServicesResourceIdentityArgs'] identity: Setting indicating whether the service has a managed identity associated with it.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input['ServicesPropertiesArgs'] properties: The common properties of a service.
        :param pulumi.Input[str] resource_name: The name of the service instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input['Kind']:
        """
        The kind of the service.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input['Kind']):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the service instance.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ServicesResourceIdentityArgs']]:
        """
        Setting indicating whether the service has a managed identity associated with it.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ServicesResourceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['ServicesPropertiesArgs']]:
        """
        The common properties of a service.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['ServicesPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service instance.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

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


class PrivateLinkServicesForM365ComplianceCenter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ServicesResourceIdentityArgs']]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['ServicesPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The description of the service.
        API Version: 2021-03-25-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ServicesResourceIdentityArgs']] identity: Setting indicating whether the service has a managed identity associated with it.
        :param pulumi.Input['Kind'] kind: The kind of the service.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[pulumi.InputType['ServicesPropertiesArgs']] properties: The common properties of a service.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the service instance.
        :param pulumi.Input[str] resource_name_: The name of the service instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateLinkServicesForM365ComplianceCenterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The description of the service.
        API Version: 2021-03-25-preview.

        :param str resource_name: The name of the resource.
        :param PrivateLinkServicesForM365ComplianceCenterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateLinkServicesForM365ComplianceCenterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ServicesResourceIdentityArgs']]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['ServicesPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrivateLinkServicesForM365ComplianceCenterArgs.__new__(PrivateLinkServicesForM365ComplianceCenterArgs)

            __props__.__dict__["identity"] = identity
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:m365securityandcompliance/v20210325preview:privateLinkServicesForM365ComplianceCenter")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateLinkServicesForM365ComplianceCenter, __self__).__init__(
            'azure-native:m365securityandcompliance:privateLinkServicesForM365ComplianceCenter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateLinkServicesForM365ComplianceCenter':
        """
        Get an existing PrivateLinkServicesForM365ComplianceCenter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrivateLinkServicesForM365ComplianceCenterArgs.__new__(PrivateLinkServicesForM365ComplianceCenterArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return PrivateLinkServicesForM365ComplianceCenter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        An etag associated with the resource, used for optimistic concurrency when editing it.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ServicesResourceResponseIdentity']]:
        """
        Setting indicating whether the service has a managed identity associated with it.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of the service.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.ServicesPropertiesResponse']:
        """
        The common properties of a service.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Required property for system data
        """
        return pulumi.get(self, "system_data")

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
        The resource type.
        """
        return pulumi.get(self, "type")

