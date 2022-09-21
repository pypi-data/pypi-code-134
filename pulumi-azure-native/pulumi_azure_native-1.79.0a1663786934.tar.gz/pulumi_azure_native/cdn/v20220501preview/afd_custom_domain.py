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

__all__ = ['AFDCustomDomainArgs', 'AFDCustomDomain']

@pulumi.input_type
class AFDCustomDomainArgs:
    def __init__(__self__, *,
                 host_name: pulumi.Input[str],
                 profile_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 azure_dns_zone: Optional[pulumi.Input['ResourceReferenceArgs']] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 extended_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 pre_validated_custom_domain_resource_id: Optional[pulumi.Input['ResourceReferenceArgs']] = None,
                 tls_settings: Optional[pulumi.Input['AFDDomainHttpsParametersArgs']] = None):
        """
        The set of arguments for constructing a AFDCustomDomain resource.
        :param pulumi.Input[str] host_name: The host name of the domain. Must be a domain name.
        :param pulumi.Input[str] profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input['ResourceReferenceArgs'] azure_dns_zone: Resource reference to the Azure DNS zone
        :param pulumi.Input[str] custom_domain_name: Name of the domain under the profile which is unique globally
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] extended_properties: Key-Value pair representing migration properties for domains.
        :param pulumi.Input['ResourceReferenceArgs'] pre_validated_custom_domain_resource_id: Resource reference to the Azure resource where custom domain ownership was prevalidated
        :param pulumi.Input['AFDDomainHttpsParametersArgs'] tls_settings: The configuration specifying how to enable HTTPS for the domain - using AzureFrontDoor managed certificate or user's own certificate. If not specified, enabling ssl uses AzureFrontDoor managed certificate by default.
        """
        pulumi.set(__self__, "host_name", host_name)
        pulumi.set(__self__, "profile_name", profile_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if azure_dns_zone is not None:
            pulumi.set(__self__, "azure_dns_zone", azure_dns_zone)
        if custom_domain_name is not None:
            pulumi.set(__self__, "custom_domain_name", custom_domain_name)
        if extended_properties is not None:
            pulumi.set(__self__, "extended_properties", extended_properties)
        if pre_validated_custom_domain_resource_id is not None:
            pulumi.set(__self__, "pre_validated_custom_domain_resource_id", pre_validated_custom_domain_resource_id)
        if tls_settings is not None:
            pulumi.set(__self__, "tls_settings", tls_settings)

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Input[str]:
        """
        The host name of the domain. Must be a domain name.
        """
        return pulumi.get(self, "host_name")

    @host_name.setter
    def host_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "host_name", value)

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[str]:
        """
        Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
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
    @pulumi.getter(name="azureDnsZone")
    def azure_dns_zone(self) -> Optional[pulumi.Input['ResourceReferenceArgs']]:
        """
        Resource reference to the Azure DNS zone
        """
        return pulumi.get(self, "azure_dns_zone")

    @azure_dns_zone.setter
    def azure_dns_zone(self, value: Optional[pulumi.Input['ResourceReferenceArgs']]):
        pulumi.set(self, "azure_dns_zone", value)

    @property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the domain under the profile which is unique globally
        """
        return pulumi.get(self, "custom_domain_name")

    @custom_domain_name.setter
    def custom_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_domain_name", value)

    @property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-Value pair representing migration properties for domains.
        """
        return pulumi.get(self, "extended_properties")

    @extended_properties.setter
    def extended_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "extended_properties", value)

    @property
    @pulumi.getter(name="preValidatedCustomDomainResourceId")
    def pre_validated_custom_domain_resource_id(self) -> Optional[pulumi.Input['ResourceReferenceArgs']]:
        """
        Resource reference to the Azure resource where custom domain ownership was prevalidated
        """
        return pulumi.get(self, "pre_validated_custom_domain_resource_id")

    @pre_validated_custom_domain_resource_id.setter
    def pre_validated_custom_domain_resource_id(self, value: Optional[pulumi.Input['ResourceReferenceArgs']]):
        pulumi.set(self, "pre_validated_custom_domain_resource_id", value)

    @property
    @pulumi.getter(name="tlsSettings")
    def tls_settings(self) -> Optional[pulumi.Input['AFDDomainHttpsParametersArgs']]:
        """
        The configuration specifying how to enable HTTPS for the domain - using AzureFrontDoor managed certificate or user's own certificate. If not specified, enabling ssl uses AzureFrontDoor managed certificate by default.
        """
        return pulumi.get(self, "tls_settings")

    @tls_settings.setter
    def tls_settings(self, value: Optional[pulumi.Input['AFDDomainHttpsParametersArgs']]):
        pulumi.set(self, "tls_settings", value)


class AFDCustomDomain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_dns_zone: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 extended_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 pre_validated_custom_domain_resource_id: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tls_settings: Optional[pulumi.Input[pulumi.InputType['AFDDomainHttpsParametersArgs']]] = None,
                 __props__=None):
        """
        Friendly domain name mapping to the endpoint hostname that the customer provides for branding purposes, e.g. www.contoso.com.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ResourceReferenceArgs']] azure_dns_zone: Resource reference to the Azure DNS zone
        :param pulumi.Input[str] custom_domain_name: Name of the domain under the profile which is unique globally
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] extended_properties: Key-Value pair representing migration properties for domains.
        :param pulumi.Input[str] host_name: The host name of the domain. Must be a domain name.
        :param pulumi.Input[pulumi.InputType['ResourceReferenceArgs']] pre_validated_custom_domain_resource_id: Resource reference to the Azure resource where custom domain ownership was prevalidated
        :param pulumi.Input[str] profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[pulumi.InputType['AFDDomainHttpsParametersArgs']] tls_settings: The configuration specifying how to enable HTTPS for the domain - using AzureFrontDoor managed certificate or user's own certificate. If not specified, enabling ssl uses AzureFrontDoor managed certificate by default.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AFDCustomDomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Friendly domain name mapping to the endpoint hostname that the customer provides for branding purposes, e.g. www.contoso.com.

        :param str resource_name: The name of the resource.
        :param AFDCustomDomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AFDCustomDomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_dns_zone: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 extended_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 pre_validated_custom_domain_resource_id: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tls_settings: Optional[pulumi.Input[pulumi.InputType['AFDDomainHttpsParametersArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AFDCustomDomainArgs.__new__(AFDCustomDomainArgs)

            __props__.__dict__["azure_dns_zone"] = azure_dns_zone
            __props__.__dict__["custom_domain_name"] = custom_domain_name
            __props__.__dict__["extended_properties"] = extended_properties
            if host_name is None and not opts.urn:
                raise TypeError("Missing required property 'host_name'")
            __props__.__dict__["host_name"] = host_name
            __props__.__dict__["pre_validated_custom_domain_resource_id"] = pre_validated_custom_domain_resource_id
            if profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'profile_name'")
            __props__.__dict__["profile_name"] = profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tls_settings"] = tls_settings
            __props__.__dict__["deployment_status"] = None
            __props__.__dict__["domain_validation_state"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["validation_properties"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cdn:AFDCustomDomain"), pulumi.Alias(type_="azure-native:cdn/v20200901:AFDCustomDomain"), pulumi.Alias(type_="azure-native:cdn/v20210601:AFDCustomDomain")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AFDCustomDomain, __self__).__init__(
            'azure-native:cdn/v20220501preview:AFDCustomDomain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AFDCustomDomain':
        """
        Get an existing AFDCustomDomain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AFDCustomDomainArgs.__new__(AFDCustomDomainArgs)

        __props__.__dict__["azure_dns_zone"] = None
        __props__.__dict__["deployment_status"] = None
        __props__.__dict__["domain_validation_state"] = None
        __props__.__dict__["extended_properties"] = None
        __props__.__dict__["host_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["pre_validated_custom_domain_resource_id"] = None
        __props__.__dict__["profile_name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tls_settings"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["validation_properties"] = None
        return AFDCustomDomain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureDnsZone")
    def azure_dns_zone(self) -> pulumi.Output[Optional['outputs.ResourceReferenceResponse']]:
        """
        Resource reference to the Azure DNS zone
        """
        return pulumi.get(self, "azure_dns_zone")

    @property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "deployment_status")

    @property
    @pulumi.getter(name="domainValidationState")
    def domain_validation_state(self) -> pulumi.Output[str]:
        """
        Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step. DCV stands for DomainControlValidation.
        """
        return pulumi.get(self, "domain_validation_state")

    @property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-Value pair representing migration properties for domains.
        """
        return pulumi.get(self, "extended_properties")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[str]:
        """
        The host name of the domain. Must be a domain name.
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
    @pulumi.getter(name="preValidatedCustomDomainResourceId")
    def pre_validated_custom_domain_resource_id(self) -> pulumi.Output[Optional['outputs.ResourceReferenceResponse']]:
        """
        Resource reference to the Azure resource where custom domain ownership was prevalidated
        """
        return pulumi.get(self, "pre_validated_custom_domain_resource_id")

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Output[str]:
        """
        The name of the profile which holds the domain.
        """
        return pulumi.get(self, "profile_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning status
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tlsSettings")
    def tls_settings(self) -> pulumi.Output[Optional['outputs.AFDDomainHttpsParametersResponse']]:
        """
        The configuration specifying how to enable HTTPS for the domain - using AzureFrontDoor managed certificate or user's own certificate. If not specified, enabling ssl uses AzureFrontDoor managed certificate by default.
        """
        return pulumi.get(self, "tls_settings")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="validationProperties")
    def validation_properties(self) -> pulumi.Output['outputs.DomainValidationPropertiesResponse']:
        """
        Values the customer needs to validate domain ownership
        """
        return pulumi.get(self, "validation_properties")

