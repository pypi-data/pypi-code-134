# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['AppServiceEnvironmentAseCustomDnsSuffixConfigurationArgs', 'AppServiceEnvironmentAseCustomDnsSuffixConfiguration']

@pulumi.input_type
class AppServiceEnvironmentAseCustomDnsSuffixConfigurationArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 certificate_url: Optional[pulumi.Input[str]] = None,
                 dns_suffix: Optional[pulumi.Input[str]] = None,
                 key_vault_reference_identity: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AppServiceEnvironmentAseCustomDnsSuffixConfiguration resource.
        :param pulumi.Input[str] name: Name of the App Service Environment.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] certificate_url: The URL referencing the Azure Key Vault certificate secret that should be used as the default SSL/TLS certificate for sites with the custom domain suffix.
        :param pulumi.Input[str] dns_suffix: The default custom domain suffix to use for all sites deployed on the ASE.
        :param pulumi.Input[str] key_vault_reference_identity: The user-assigned identity to use for resolving the key vault certificate reference. If not specified, the system-assigned ASE identity will be used if available.
        :param pulumi.Input[str] kind: Kind of resource.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if certificate_url is not None:
            pulumi.set(__self__, "certificate_url", certificate_url)
        if dns_suffix is not None:
            pulumi.set(__self__, "dns_suffix", dns_suffix)
        if key_vault_reference_identity is not None:
            pulumi.set(__self__, "key_vault_reference_identity", key_vault_reference_identity)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the App Service Environment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL referencing the Azure Key Vault certificate secret that should be used as the default SSL/TLS certificate for sites with the custom domain suffix.
        """
        return pulumi.get(self, "certificate_url")

    @certificate_url.setter
    def certificate_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_url", value)

    @property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> Optional[pulumi.Input[str]]:
        """
        The default custom domain suffix to use for all sites deployed on the ASE.
        """
        return pulumi.get(self, "dns_suffix")

    @dns_suffix.setter
    def dns_suffix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_suffix", value)

    @property
    @pulumi.getter(name="keyVaultReferenceIdentity")
    def key_vault_reference_identity(self) -> Optional[pulumi.Input[str]]:
        """
        The user-assigned identity to use for resolving the key vault certificate reference. If not specified, the system-assigned ASE identity will be used if available.
        """
        return pulumi.get(self, "key_vault_reference_identity")

    @key_vault_reference_identity.setter
    def key_vault_reference_identity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_vault_reference_identity", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)


class AppServiceEnvironmentAseCustomDnsSuffixConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_url: Optional[pulumi.Input[str]] = None,
                 dns_suffix: Optional[pulumi.Input[str]] = None,
                 key_vault_reference_identity: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Full view of the custom domain suffix configuration for ASEv3.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_url: The URL referencing the Azure Key Vault certificate secret that should be used as the default SSL/TLS certificate for sites with the custom domain suffix.
        :param pulumi.Input[str] dns_suffix: The default custom domain suffix to use for all sites deployed on the ASE.
        :param pulumi.Input[str] key_vault_reference_identity: The user-assigned identity to use for resolving the key vault certificate reference. If not specified, the system-assigned ASE identity will be used if available.
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] name: Name of the App Service Environment.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppServiceEnvironmentAseCustomDnsSuffixConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Full view of the custom domain suffix configuration for ASEv3.

        :param str resource_name: The name of the resource.
        :param AppServiceEnvironmentAseCustomDnsSuffixConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppServiceEnvironmentAseCustomDnsSuffixConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_url: Optional[pulumi.Input[str]] = None,
                 dns_suffix: Optional[pulumi.Input[str]] = None,
                 key_vault_reference_identity: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AppServiceEnvironmentAseCustomDnsSuffixConfigurationArgs.__new__(AppServiceEnvironmentAseCustomDnsSuffixConfigurationArgs)

            __props__.__dict__["certificate_url"] = certificate_url
            __props__.__dict__["dns_suffix"] = dns_suffix
            __props__.__dict__["key_vault_reference_identity"] = key_vault_reference_identity
            __props__.__dict__["kind"] = kind
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["provisioning_details"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:web:AppServiceEnvironmentAseCustomDnsSuffixConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AppServiceEnvironmentAseCustomDnsSuffixConfiguration, __self__).__init__(
            'azure-native:web/v20220301:AppServiceEnvironmentAseCustomDnsSuffixConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AppServiceEnvironmentAseCustomDnsSuffixConfiguration':
        """
        Get an existing AppServiceEnvironmentAseCustomDnsSuffixConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AppServiceEnvironmentAseCustomDnsSuffixConfigurationArgs.__new__(AppServiceEnvironmentAseCustomDnsSuffixConfigurationArgs)

        __props__.__dict__["certificate_url"] = None
        __props__.__dict__["dns_suffix"] = None
        __props__.__dict__["key_vault_reference_identity"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_details"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return AppServiceEnvironmentAseCustomDnsSuffixConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> pulumi.Output[Optional[str]]:
        """
        The URL referencing the Azure Key Vault certificate secret that should be used as the default SSL/TLS certificate for sites with the custom domain suffix.
        """
        return pulumi.get(self, "certificate_url")

    @property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> pulumi.Output[Optional[str]]:
        """
        The default custom domain suffix to use for all sites deployed on the ASE.
        """
        return pulumi.get(self, "dns_suffix")

    @property
    @pulumi.getter(name="keyVaultReferenceIdentity")
    def key_vault_reference_identity(self) -> pulumi.Output[Optional[str]]:
        """
        The user-assigned identity to use for resolving the key vault certificate reference. If not specified, the system-assigned ASE identity will be used if available.
        """
        return pulumi.get(self, "key_vault_reference_identity")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningDetails")
    def provisioning_details(self) -> pulumi.Output[str]:
        return pulumi.get(self, "provisioning_details")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

