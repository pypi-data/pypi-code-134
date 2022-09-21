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

__all__ = ['ApiManagementServiceArgs', 'ApiManagementService']

@pulumi.input_type
class ApiManagementServiceArgs:
    def __init__(__self__, *,
                 publisher_email: pulumi.Input[str],
                 publisher_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['ApiManagementServiceSkuPropertiesArgs'],
                 additional_locations: Optional[pulumi.Input[Sequence[pulumi.Input['AdditionalLocationArgs']]]] = None,
                 certificates: Optional[pulumi.Input[Sequence[pulumi.Input['CertificateConfigurationArgs']]]] = None,
                 custom_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 hostname_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['HostnameConfigurationArgs']]]] = None,
                 identity: Optional[pulumi.Input['ApiManagementServiceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 notification_sender_email: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_network_configuration: Optional[pulumi.Input['VirtualNetworkConfigurationArgs']] = None,
                 virtual_network_type: Optional[pulumi.Input[Union[str, 'VirtualNetworkType']]] = None):
        """
        The set of arguments for constructing a ApiManagementService resource.
        :param pulumi.Input[str] publisher_email: Publisher email.
        :param pulumi.Input[str] publisher_name: Publisher name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['ApiManagementServiceSkuPropertiesArgs'] sku: SKU properties of the API Management service.
        :param pulumi.Input[Sequence[pulumi.Input['AdditionalLocationArgs']]] additional_locations: Additional datacenter locations of the API Management service.
        :param pulumi.Input[Sequence[pulumi.Input['CertificateConfigurationArgs']]] certificates: List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_properties: Custom properties of the API Management service. Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168` will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2). Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11` can be used to disable just TLS 1.1 and setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10` can be used to disable TLS 1.0 on an API Management service.
        :param pulumi.Input[Sequence[pulumi.Input['HostnameConfigurationArgs']]] hostname_configurations: Custom hostname configuration of the API Management service.
        :param pulumi.Input['ApiManagementServiceIdentityArgs'] identity: Managed service identity of the Api Management service.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] notification_sender_email: Email address from which the notification will be sent.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input['VirtualNetworkConfigurationArgs'] virtual_network_configuration: Virtual network configuration of the API Management service.
        :param pulumi.Input[Union[str, 'VirtualNetworkType']] virtual_network_type: The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only.
        """
        pulumi.set(__self__, "publisher_email", publisher_email)
        pulumi.set(__self__, "publisher_name", publisher_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        if additional_locations is not None:
            pulumi.set(__self__, "additional_locations", additional_locations)
        if certificates is not None:
            pulumi.set(__self__, "certificates", certificates)
        if custom_properties is not None:
            pulumi.set(__self__, "custom_properties", custom_properties)
        if hostname_configurations is not None:
            pulumi.set(__self__, "hostname_configurations", hostname_configurations)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if notification_sender_email is not None:
            pulumi.set(__self__, "notification_sender_email", notification_sender_email)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if virtual_network_configuration is not None:
            pulumi.set(__self__, "virtual_network_configuration", virtual_network_configuration)
        if virtual_network_type is None:
            virtual_network_type = 'None'
        if virtual_network_type is not None:
            pulumi.set(__self__, "virtual_network_type", virtual_network_type)

    @property
    @pulumi.getter(name="publisherEmail")
    def publisher_email(self) -> pulumi.Input[str]:
        """
        Publisher email.
        """
        return pulumi.get(self, "publisher_email")

    @publisher_email.setter
    def publisher_email(self, value: pulumi.Input[str]):
        pulumi.set(self, "publisher_email", value)

    @property
    @pulumi.getter(name="publisherName")
    def publisher_name(self) -> pulumi.Input[str]:
        """
        Publisher name.
        """
        return pulumi.get(self, "publisher_name")

    @publisher_name.setter
    def publisher_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "publisher_name", value)

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
    @pulumi.getter
    def sku(self) -> pulumi.Input['ApiManagementServiceSkuPropertiesArgs']:
        """
        SKU properties of the API Management service.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['ApiManagementServiceSkuPropertiesArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="additionalLocations")
    def additional_locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AdditionalLocationArgs']]]]:
        """
        Additional datacenter locations of the API Management service.
        """
        return pulumi.get(self, "additional_locations")

    @additional_locations.setter
    def additional_locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AdditionalLocationArgs']]]]):
        pulumi.set(self, "additional_locations", value)

    @property
    @pulumi.getter
    def certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CertificateConfigurationArgs']]]]:
        """
        List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10.
        """
        return pulumi.get(self, "certificates")

    @certificates.setter
    def certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CertificateConfigurationArgs']]]]):
        pulumi.set(self, "certificates", value)

    @property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Custom properties of the API Management service. Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168` will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2). Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11` can be used to disable just TLS 1.1 and setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10` can be used to disable TLS 1.0 on an API Management service.
        """
        return pulumi.get(self, "custom_properties")

    @custom_properties.setter
    def custom_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "custom_properties", value)

    @property
    @pulumi.getter(name="hostnameConfigurations")
    def hostname_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['HostnameConfigurationArgs']]]]:
        """
        Custom hostname configuration of the API Management service.
        """
        return pulumi.get(self, "hostname_configurations")

    @hostname_configurations.setter
    def hostname_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['HostnameConfigurationArgs']]]]):
        pulumi.set(self, "hostname_configurations", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ApiManagementServiceIdentityArgs']]:
        """
        Managed service identity of the Api Management service.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ApiManagementServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="notificationSenderEmail")
    def notification_sender_email(self) -> Optional[pulumi.Input[str]]:
        """
        Email address from which the notification will be sent.
        """
        return pulumi.get(self, "notification_sender_email")

    @notification_sender_email.setter
    def notification_sender_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notification_sender_email", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="virtualNetworkConfiguration")
    def virtual_network_configuration(self) -> Optional[pulumi.Input['VirtualNetworkConfigurationArgs']]:
        """
        Virtual network configuration of the API Management service.
        """
        return pulumi.get(self, "virtual_network_configuration")

    @virtual_network_configuration.setter
    def virtual_network_configuration(self, value: Optional[pulumi.Input['VirtualNetworkConfigurationArgs']]):
        pulumi.set(self, "virtual_network_configuration", value)

    @property
    @pulumi.getter(name="virtualNetworkType")
    def virtual_network_type(self) -> Optional[pulumi.Input[Union[str, 'VirtualNetworkType']]]:
        """
        The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only.
        """
        return pulumi.get(self, "virtual_network_type")

    @virtual_network_type.setter
    def virtual_network_type(self, value: Optional[pulumi.Input[Union[str, 'VirtualNetworkType']]]):
        pulumi.set(self, "virtual_network_type", value)


class ApiManagementService(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_locations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AdditionalLocationArgs']]]]] = None,
                 certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CertificateConfigurationArgs']]]]] = None,
                 custom_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 hostname_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HostnameConfigurationArgs']]]]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ApiManagementServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 notification_sender_email: Optional[pulumi.Input[str]] = None,
                 publisher_email: Optional[pulumi.Input[str]] = None,
                 publisher_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['ApiManagementServiceSkuPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_network_configuration: Optional[pulumi.Input[pulumi.InputType['VirtualNetworkConfigurationArgs']]] = None,
                 virtual_network_type: Optional[pulumi.Input[Union[str, 'VirtualNetworkType']]] = None,
                 __props__=None):
        """
        A single API Management service resource in List or Get response.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AdditionalLocationArgs']]]] additional_locations: Additional datacenter locations of the API Management service.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CertificateConfigurationArgs']]]] certificates: List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_properties: Custom properties of the API Management service. Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168` will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2). Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11` can be used to disable just TLS 1.1 and setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10` can be used to disable TLS 1.0 on an API Management service.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HostnameConfigurationArgs']]]] hostname_configurations: Custom hostname configuration of the API Management service.
        :param pulumi.Input[pulumi.InputType['ApiManagementServiceIdentityArgs']] identity: Managed service identity of the Api Management service.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] notification_sender_email: Email address from which the notification will be sent.
        :param pulumi.Input[str] publisher_email: Publisher email.
        :param pulumi.Input[str] publisher_name: Publisher name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[pulumi.InputType['ApiManagementServiceSkuPropertiesArgs']] sku: SKU properties of the API Management service.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[pulumi.InputType['VirtualNetworkConfigurationArgs']] virtual_network_configuration: Virtual network configuration of the API Management service.
        :param pulumi.Input[Union[str, 'VirtualNetworkType']] virtual_network_type: The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiManagementServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A single API Management service resource in List or Get response.

        :param str resource_name: The name of the resource.
        :param ApiManagementServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiManagementServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_locations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AdditionalLocationArgs']]]]] = None,
                 certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CertificateConfigurationArgs']]]]] = None,
                 custom_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 hostname_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HostnameConfigurationArgs']]]]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ApiManagementServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 notification_sender_email: Optional[pulumi.Input[str]] = None,
                 publisher_email: Optional[pulumi.Input[str]] = None,
                 publisher_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['ApiManagementServiceSkuPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_network_configuration: Optional[pulumi.Input[pulumi.InputType['VirtualNetworkConfigurationArgs']]] = None,
                 virtual_network_type: Optional[pulumi.Input[Union[str, 'VirtualNetworkType']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiManagementServiceArgs.__new__(ApiManagementServiceArgs)

            __props__.__dict__["additional_locations"] = additional_locations
            __props__.__dict__["certificates"] = certificates
            __props__.__dict__["custom_properties"] = custom_properties
            __props__.__dict__["hostname_configurations"] = hostname_configurations
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["notification_sender_email"] = notification_sender_email
            if publisher_email is None and not opts.urn:
                raise TypeError("Missing required property 'publisher_email'")
            __props__.__dict__["publisher_email"] = publisher_email
            if publisher_name is None and not opts.urn:
                raise TypeError("Missing required property 'publisher_name'")
            __props__.__dict__["publisher_name"] = publisher_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["service_name"] = service_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["virtual_network_configuration"] = virtual_network_configuration
            if virtual_network_type is None:
                virtual_network_type = 'None'
            __props__.__dict__["virtual_network_type"] = virtual_network_type
            __props__.__dict__["created_at_utc"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["gateway_regional_url"] = None
            __props__.__dict__["gateway_url"] = None
            __props__.__dict__["management_api_url"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["portal_url"] = None
            __props__.__dict__["private_ip_addresses"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["public_ip_addresses"] = None
            __props__.__dict__["scm_url"] = None
            __props__.__dict__["target_provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement:ApiManagementService"), pulumi.Alias(type_="azure-native:apimanagement/v20160707:ApiManagementService"), pulumi.Alias(type_="azure-native:apimanagement/v20161010:ApiManagementService"), pulumi.Alias(type_="azure-native:apimanagement/v20170301:ApiManagementService"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:ApiManagementService"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:ApiManagementService"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:ApiManagementService"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:ApiManagementService"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:ApiManagementService"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:ApiManagementService"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:ApiManagementService"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:ApiManagementService"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:ApiManagementService"), pulumi.Alias(type_="azure-native:apimanagement/v20211201preview:ApiManagementService")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ApiManagementService, __self__).__init__(
            'azure-native:apimanagement/v20180101:ApiManagementService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApiManagementService':
        """
        Get an existing ApiManagementService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApiManagementServiceArgs.__new__(ApiManagementServiceArgs)

        __props__.__dict__["additional_locations"] = None
        __props__.__dict__["certificates"] = None
        __props__.__dict__["created_at_utc"] = None
        __props__.__dict__["custom_properties"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["gateway_regional_url"] = None
        __props__.__dict__["gateway_url"] = None
        __props__.__dict__["hostname_configurations"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["management_api_url"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notification_sender_email"] = None
        __props__.__dict__["portal_url"] = None
        __props__.__dict__["private_ip_addresses"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_ip_addresses"] = None
        __props__.__dict__["publisher_email"] = None
        __props__.__dict__["publisher_name"] = None
        __props__.__dict__["scm_url"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_provisioning_state"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_network_configuration"] = None
        __props__.__dict__["virtual_network_type"] = None
        return ApiManagementService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalLocations")
    def additional_locations(self) -> pulumi.Output[Optional[Sequence['outputs.AdditionalLocationResponse']]]:
        """
        Additional datacenter locations of the API Management service.
        """
        return pulumi.get(self, "additional_locations")

    @property
    @pulumi.getter
    def certificates(self) -> pulumi.Output[Optional[Sequence['outputs.CertificateConfigurationResponse']]]:
        """
        List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10.
        """
        return pulumi.get(self, "certificates")

    @property
    @pulumi.getter(name="createdAtUtc")
    def created_at_utc(self) -> pulumi.Output[str]:
        """
        Creation UTC date of the API Management service.The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.
        """
        return pulumi.get(self, "created_at_utc")

    @property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Custom properties of the API Management service. Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168` will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2). Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11` can be used to disable just TLS 1.1 and setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10` can be used to disable TLS 1.0 on an API Management service.
        """
        return pulumi.get(self, "custom_properties")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        ETag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="gatewayRegionalUrl")
    def gateway_regional_url(self) -> pulumi.Output[str]:
        """
        Gateway URL of the API Management service in the Default Region.
        """
        return pulumi.get(self, "gateway_regional_url")

    @property
    @pulumi.getter(name="gatewayUrl")
    def gateway_url(self) -> pulumi.Output[str]:
        """
        Gateway URL of the API Management service.
        """
        return pulumi.get(self, "gateway_url")

    @property
    @pulumi.getter(name="hostnameConfigurations")
    def hostname_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.HostnameConfigurationResponse']]]:
        """
        Custom hostname configuration of the API Management service.
        """
        return pulumi.get(self, "hostname_configurations")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ApiManagementServiceIdentityResponse']]:
        """
        Managed service identity of the Api Management service.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managementApiUrl")
    def management_api_url(self) -> pulumi.Output[str]:
        """
        Management API endpoint URL of the API Management service.
        """
        return pulumi.get(self, "management_api_url")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationSenderEmail")
    def notification_sender_email(self) -> pulumi.Output[Optional[str]]:
        """
        Email address from which the notification will be sent.
        """
        return pulumi.get(self, "notification_sender_email")

    @property
    @pulumi.getter(name="portalUrl")
    def portal_url(self) -> pulumi.Output[str]:
        """
        Publisher portal endpoint Url of the API Management service.
        """
        return pulumi.get(self, "portal_url")

    @property
    @pulumi.getter(name="privateIPAddresses")
    def private_ip_addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        Private Static Load Balanced IP addresses of the API Management service in Primary region which is deployed in an Internal Virtual Network. Available only for Basic, Standard and Premium SKU.
        """
        return pulumi.get(self, "private_ip_addresses")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The current provisioning state of the API Management service which can be one of the following: Created/Activating/Succeeded/Updating/Failed/Stopped/Terminating/TerminationFailed/Deleted.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicIPAddresses")
    def public_ip_addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        Public Static Load Balanced IP addresses of the API Management service in Primary region. Available only for Basic, Standard and Premium SKU.
        """
        return pulumi.get(self, "public_ip_addresses")

    @property
    @pulumi.getter(name="publisherEmail")
    def publisher_email(self) -> pulumi.Output[str]:
        """
        Publisher email.
        """
        return pulumi.get(self, "publisher_email")

    @property
    @pulumi.getter(name="publisherName")
    def publisher_name(self) -> pulumi.Output[str]:
        """
        Publisher name.
        """
        return pulumi.get(self, "publisher_name")

    @property
    @pulumi.getter(name="scmUrl")
    def scm_url(self) -> pulumi.Output[str]:
        """
        SCM endpoint URL of the API Management service.
        """
        return pulumi.get(self, "scm_url")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.ApiManagementServiceSkuPropertiesResponse']:
        """
        SKU properties of the API Management service.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetProvisioningState")
    def target_provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the API Management service, which is targeted by the long running operation started on the service.
        """
        return pulumi.get(self, "target_provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type for API Management resource is set to Microsoft.ApiManagement.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetworkConfiguration")
    def virtual_network_configuration(self) -> pulumi.Output[Optional['outputs.VirtualNetworkConfigurationResponse']]:
        """
        Virtual network configuration of the API Management service.
        """
        return pulumi.get(self, "virtual_network_configuration")

    @property
    @pulumi.getter(name="virtualNetworkType")
    def virtual_network_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only.
        """
        return pulumi.get(self, "virtual_network_type")

