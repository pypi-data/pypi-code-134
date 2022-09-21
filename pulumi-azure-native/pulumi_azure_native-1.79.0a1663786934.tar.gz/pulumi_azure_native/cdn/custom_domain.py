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

__all__ = ['CustomDomainArgs', 'CustomDomain']

@pulumi.input_type
class CustomDomainArgs:
    def __init__(__self__, *,
                 endpoint_name: pulumi.Input[str],
                 host_name: pulumi.Input[str],
                 profile_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 custom_domain_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CustomDomain resource.
        :param pulumi.Input[str] endpoint_name: Name of the endpoint under the profile which is unique globally.
        :param pulumi.Input[str] host_name: The host name of the custom domain. Must be a domain name.
        :param pulumi.Input[str] profile_name: Name of the CDN profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] custom_domain_name: Name of the custom domain within an endpoint.
        """
        pulumi.set(__self__, "endpoint_name", endpoint_name)
        pulumi.set(__self__, "host_name", host_name)
        pulumi.set(__self__, "profile_name", profile_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if custom_domain_name is not None:
            pulumi.set(__self__, "custom_domain_name", custom_domain_name)

    @property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Input[str]:
        """
        Name of the endpoint under the profile which is unique globally.
        """
        return pulumi.get(self, "endpoint_name")

    @endpoint_name.setter
    def endpoint_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_name", value)

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Input[str]:
        """
        The host name of the custom domain. Must be a domain name.
        """
        return pulumi.get(self, "host_name")

    @host_name.setter
    def host_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "host_name", value)

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[str]:
        """
        Name of the CDN profile which is unique within the resource group.
        """
        return pulumi.get(self, "profile_name")

    @profile_name.setter
    def profile_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "profile_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the custom domain within an endpoint.
        """
        return pulumi.get(self, "custom_domain_name")

    @custom_domain_name.setter
    def custom_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_domain_name", value)


class CustomDomain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Friendly domain name mapping to the endpoint hostname that the customer provides for branding purposes, e.g. www.contoso.com.
        API Version: 2020-09-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] custom_domain_name: Name of the custom domain within an endpoint.
        :param pulumi.Input[str] endpoint_name: Name of the endpoint under the profile which is unique globally.
        :param pulumi.Input[str] host_name: The host name of the custom domain. Must be a domain name.
        :param pulumi.Input[str] profile_name: Name of the CDN profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomDomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Friendly domain name mapping to the endpoint hostname that the customer provides for branding purposes, e.g. www.contoso.com.
        API Version: 2020-09-01.

        :param str resource_name: The name of the resource.
        :param CustomDomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomDomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomDomainArgs.__new__(CustomDomainArgs)

            __props__.__dict__["custom_domain_name"] = custom_domain_name
            if endpoint_name is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_name'")
            __props__.__dict__["endpoint_name"] = endpoint_name
            if host_name is None and not opts.urn:
                raise TypeError("Missing required property 'host_name'")
            __props__.__dict__["host_name"] = host_name
            if profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'profile_name'")
            __props__.__dict__["profile_name"] = profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["custom_https_parameters"] = None
            __props__.__dict__["custom_https_provisioning_state"] = None
            __props__.__dict__["custom_https_provisioning_substate"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["validation_data"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cdn/v20150601:CustomDomain"), pulumi.Alias(type_="azure-native:cdn/v20160402:CustomDomain"), pulumi.Alias(type_="azure-native:cdn/v20161002:CustomDomain"), pulumi.Alias(type_="azure-native:cdn/v20170402:CustomDomain"), pulumi.Alias(type_="azure-native:cdn/v20171012:CustomDomain"), pulumi.Alias(type_="azure-native:cdn/v20190415:CustomDomain"), pulumi.Alias(type_="azure-native:cdn/v20190615:CustomDomain"), pulumi.Alias(type_="azure-native:cdn/v20190615preview:CustomDomain"), pulumi.Alias(type_="azure-native:cdn/v20191231:CustomDomain"), pulumi.Alias(type_="azure-native:cdn/v20200331:CustomDomain"), pulumi.Alias(type_="azure-native:cdn/v20200415:CustomDomain"), pulumi.Alias(type_="azure-native:cdn/v20200901:CustomDomain"), pulumi.Alias(type_="azure-native:cdn/v20210601:CustomDomain"), pulumi.Alias(type_="azure-native:cdn/v20220501preview:CustomDomain")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CustomDomain, __self__).__init__(
            'azure-native:cdn:CustomDomain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CustomDomain':
        """
        Get an existing CustomDomain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CustomDomainArgs.__new__(CustomDomainArgs)

        __props__.__dict__["custom_https_parameters"] = None
        __props__.__dict__["custom_https_provisioning_state"] = None
        __props__.__dict__["custom_https_provisioning_substate"] = None
        __props__.__dict__["host_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["validation_data"] = None
        return CustomDomain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customHttpsParameters")
    def custom_https_parameters(self) -> pulumi.Output[Optional[Any]]:
        """
        Certificate parameters for securing custom HTTPS
        """
        return pulumi.get(self, "custom_https_parameters")

    @property
    @pulumi.getter(name="customHttpsProvisioningState")
    def custom_https_provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning status of Custom Https of the custom domain.
        """
        return pulumi.get(self, "custom_https_provisioning_state")

    @property
    @pulumi.getter(name="customHttpsProvisioningSubstate")
    def custom_https_provisioning_substate(self) -> pulumi.Output[str]:
        """
        Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step.
        """
        return pulumi.get(self, "custom_https_provisioning_substate")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[str]:
        """
        The host name of the custom domain. Must be a domain name.
        """
        return pulumi.get(self, "host_name")

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
        Provisioning status of the custom domain.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[str]:
        """
        Resource status of the custom domain.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> pulumi.Output[Optional[str]]:
        """
        Special validation or data may be required when delivering CDN to some regions due to local compliance reasons. E.g. ICP license number of a custom domain is required to deliver content in China.
        """
        return pulumi.get(self, "validation_data")

