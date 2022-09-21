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

__all__ = ['NetworkInterfaceArgs', 'NetworkInterface']

@pulumi.input_type
class NetworkInterfaceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 dns_settings: Optional[pulumi.Input['NetworkInterfaceDnsSettingsArgs']] = None,
                 enable_accelerated_networking: Optional[pulumi.Input[bool]] = None,
                 enable_ip_forwarding: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceIPConfigurationArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mac_address: Optional[pulumi.Input[str]] = None,
                 network_interface_name: Optional[pulumi.Input[str]] = None,
                 network_security_group: Optional[pulumi.Input['NetworkSecurityGroupArgs']] = None,
                 primary: Optional[pulumi.Input[bool]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tap_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceTapConfigurationArgs']]]] = None):
        """
        The set of arguments for constructing a NetworkInterface resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['NetworkInterfaceDnsSettingsArgs'] dns_settings: The DNS settings in network interface.
        :param pulumi.Input[bool] enable_accelerated_networking: If the network interface is accelerated networking enabled.
        :param pulumi.Input[bool] enable_ip_forwarding: Indicates whether IP forwarding is enabled on this network interface.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceIPConfigurationArgs']]] ip_configurations: A list of IPConfigurations of the network interface.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] mac_address: The MAC address of the network interface.
        :param pulumi.Input[str] network_interface_name: The name of the network interface.
        :param pulumi.Input['NetworkSecurityGroupArgs'] network_security_group: The reference of the NetworkSecurityGroup resource.
        :param pulumi.Input[bool] primary: Gets whether this is a primary network interface on a virtual machine.
        :param pulumi.Input[str] provisioning_state: The provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        :param pulumi.Input[str] resource_guid: The resource GUID property of the network interface resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceTapConfigurationArgs']]] tap_configurations: A list of TapConfigurations of the network interface.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if dns_settings is not None:
            pulumi.set(__self__, "dns_settings", dns_settings)
        if enable_accelerated_networking is not None:
            pulumi.set(__self__, "enable_accelerated_networking", enable_accelerated_networking)
        if enable_ip_forwarding is not None:
            pulumi.set(__self__, "enable_ip_forwarding", enable_ip_forwarding)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if ip_configurations is not None:
            pulumi.set(__self__, "ip_configurations", ip_configurations)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mac_address is not None:
            pulumi.set(__self__, "mac_address", mac_address)
        if network_interface_name is not None:
            pulumi.set(__self__, "network_interface_name", network_interface_name)
        if network_security_group is not None:
            pulumi.set(__self__, "network_security_group", network_security_group)
        if primary is not None:
            pulumi.set(__self__, "primary", primary)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_guid is not None:
            pulumi.set(__self__, "resource_guid", resource_guid)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tap_configurations is not None:
            pulumi.set(__self__, "tap_configurations", tap_configurations)

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
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[pulumi.Input['NetworkInterfaceDnsSettingsArgs']]:
        """
        The DNS settings in network interface.
        """
        return pulumi.get(self, "dns_settings")

    @dns_settings.setter
    def dns_settings(self, value: Optional[pulumi.Input['NetworkInterfaceDnsSettingsArgs']]):
        pulumi.set(self, "dns_settings", value)

    @property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(self) -> Optional[pulumi.Input[bool]]:
        """
        If the network interface is accelerated networking enabled.
        """
        return pulumi.get(self, "enable_accelerated_networking")

    @enable_accelerated_networking.setter
    def enable_accelerated_networking(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_accelerated_networking", value)

    @property
    @pulumi.getter(name="enableIPForwarding")
    def enable_ip_forwarding(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether IP forwarding is enabled on this network interface.
        """
        return pulumi.get(self, "enable_ip_forwarding")

    @enable_ip_forwarding.setter
    def enable_ip_forwarding(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_ip_forwarding", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceIPConfigurationArgs']]]]:
        """
        A list of IPConfigurations of the network interface.
        """
        return pulumi.get(self, "ip_configurations")

    @ip_configurations.setter
    def ip_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceIPConfigurationArgs']]]]):
        pulumi.set(self, "ip_configurations", value)

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
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[pulumi.Input[str]]:
        """
        The MAC address of the network interface.
        """
        return pulumi.get(self, "mac_address")

    @mac_address.setter
    def mac_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac_address", value)

    @property
    @pulumi.getter(name="networkInterfaceName")
    def network_interface_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the network interface.
        """
        return pulumi.get(self, "network_interface_name")

    @network_interface_name.setter
    def network_interface_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_interface_name", value)

    @property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> Optional[pulumi.Input['NetworkSecurityGroupArgs']]:
        """
        The reference of the NetworkSecurityGroup resource.
        """
        return pulumi.get(self, "network_security_group")

    @network_security_group.setter
    def network_security_group(self, value: Optional[pulumi.Input['NetworkSecurityGroupArgs']]):
        pulumi.set(self, "network_security_group", value)

    @property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[bool]]:
        """
        Gets whether this is a primary network interface on a virtual machine.
        """
        return pulumi.get(self, "primary")

    @primary.setter
    def primary(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "primary", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        The provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> Optional[pulumi.Input[str]]:
        """
        The resource GUID property of the network interface resource.
        """
        return pulumi.get(self, "resource_guid")

    @resource_guid.setter
    def resource_guid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_guid", value)

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
    @pulumi.getter(name="tapConfigurations")
    def tap_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceTapConfigurationArgs']]]]:
        """
        A list of TapConfigurations of the network interface.
        """
        return pulumi.get(self, "tap_configurations")

    @tap_configurations.setter
    def tap_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceTapConfigurationArgs']]]]):
        pulumi.set(self, "tap_configurations", value)


class NetworkInterface(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_settings: Optional[pulumi.Input[pulumi.InputType['NetworkInterfaceDnsSettingsArgs']]] = None,
                 enable_accelerated_networking: Optional[pulumi.Input[bool]] = None,
                 enable_ip_forwarding: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfaceIPConfigurationArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mac_address: Optional[pulumi.Input[str]] = None,
                 network_interface_name: Optional[pulumi.Input[str]] = None,
                 network_security_group: Optional[pulumi.Input[pulumi.InputType['NetworkSecurityGroupArgs']]] = None,
                 primary: Optional[pulumi.Input[bool]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tap_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfaceTapConfigurationArgs']]]]] = None,
                 __props__=None):
        """
        A network interface in a resource group.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['NetworkInterfaceDnsSettingsArgs']] dns_settings: The DNS settings in network interface.
        :param pulumi.Input[bool] enable_accelerated_networking: If the network interface is accelerated networking enabled.
        :param pulumi.Input[bool] enable_ip_forwarding: Indicates whether IP forwarding is enabled on this network interface.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfaceIPConfigurationArgs']]]] ip_configurations: A list of IPConfigurations of the network interface.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] mac_address: The MAC address of the network interface.
        :param pulumi.Input[str] network_interface_name: The name of the network interface.
        :param pulumi.Input[pulumi.InputType['NetworkSecurityGroupArgs']] network_security_group: The reference of the NetworkSecurityGroup resource.
        :param pulumi.Input[bool] primary: Gets whether this is a primary network interface on a virtual machine.
        :param pulumi.Input[str] provisioning_state: The provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_guid: The resource GUID property of the network interface resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfaceTapConfigurationArgs']]]] tap_configurations: A list of TapConfigurations of the network interface.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkInterfaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A network interface in a resource group.

        :param str resource_name: The name of the resource.
        :param NetworkInterfaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkInterfaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_settings: Optional[pulumi.Input[pulumi.InputType['NetworkInterfaceDnsSettingsArgs']]] = None,
                 enable_accelerated_networking: Optional[pulumi.Input[bool]] = None,
                 enable_ip_forwarding: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfaceIPConfigurationArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mac_address: Optional[pulumi.Input[str]] = None,
                 network_interface_name: Optional[pulumi.Input[str]] = None,
                 network_security_group: Optional[pulumi.Input[pulumi.InputType['NetworkSecurityGroupArgs']]] = None,
                 primary: Optional[pulumi.Input[bool]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tap_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfaceTapConfigurationArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkInterfaceArgs.__new__(NetworkInterfaceArgs)

            __props__.__dict__["dns_settings"] = dns_settings
            __props__.__dict__["enable_accelerated_networking"] = enable_accelerated_networking
            __props__.__dict__["enable_ip_forwarding"] = enable_ip_forwarding
            __props__.__dict__["id"] = id
            __props__.__dict__["ip_configurations"] = ip_configurations
            __props__.__dict__["location"] = location
            __props__.__dict__["mac_address"] = mac_address
            __props__.__dict__["network_interface_name"] = network_interface_name
            __props__.__dict__["network_security_group"] = network_security_group
            __props__.__dict__["primary"] = primary
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_guid"] = resource_guid
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tap_configurations"] = tap_configurations
            __props__.__dict__["etag"] = None
            __props__.__dict__["hosted_workloads"] = None
            __props__.__dict__["interface_endpoint"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["virtual_machine"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20150501preview:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20150615:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20160330:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20160601:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20160901:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20161201:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20170301:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20170601:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20170801:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20170901:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20171001:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20171101:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20180101:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20180201:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20180401:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20180601:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20180701:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20181001:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20181101:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20181201:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20190201:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20190401:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20190601:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20190701:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20190801:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20190901:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20191101:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20191201:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20200301:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20200401:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20200501:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20200601:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20200701:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20200801:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20201101:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20210201:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20210301:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20210501:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20210801:NetworkInterface"), pulumi.Alias(type_="azure-native:network/v20220101:NetworkInterface")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NetworkInterface, __self__).__init__(
            'azure-native:network/v20180801:NetworkInterface',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkInterface':
        """
        Get an existing NetworkInterface resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkInterfaceArgs.__new__(NetworkInterfaceArgs)

        __props__.__dict__["dns_settings"] = None
        __props__.__dict__["enable_accelerated_networking"] = None
        __props__.__dict__["enable_ip_forwarding"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["hosted_workloads"] = None
        __props__.__dict__["interface_endpoint"] = None
        __props__.__dict__["ip_configurations"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mac_address"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_security_group"] = None
        __props__.__dict__["primary"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["tap_configurations"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_machine"] = None
        return NetworkInterface(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> pulumi.Output[Optional['outputs.NetworkInterfaceDnsSettingsResponse']]:
        """
        The DNS settings in network interface.
        """
        return pulumi.get(self, "dns_settings")

    @property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(self) -> pulumi.Output[Optional[bool]]:
        """
        If the network interface is accelerated networking enabled.
        """
        return pulumi.get(self, "enable_accelerated_networking")

    @property
    @pulumi.getter(name="enableIPForwarding")
    def enable_ip_forwarding(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether IP forwarding is enabled on this network interface.
        """
        return pulumi.get(self, "enable_ip_forwarding")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="hostedWorkloads")
    def hosted_workloads(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of references to linked BareMetal resources
        """
        return pulumi.get(self, "hosted_workloads")

    @property
    @pulumi.getter(name="interfaceEndpoint")
    def interface_endpoint(self) -> pulumi.Output['outputs.InterfaceEndpointResponse']:
        """
        A reference to the interface endpoint to which the network interface is linked.
        """
        return pulumi.get(self, "interface_endpoint")

    @property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.NetworkInterfaceIPConfigurationResponse']]]:
        """
        A list of IPConfigurations of the network interface.
        """
        return pulumi.get(self, "ip_configurations")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> pulumi.Output[Optional[str]]:
        """
        The MAC address of the network interface.
        """
        return pulumi.get(self, "mac_address")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> pulumi.Output[Optional['outputs.NetworkSecurityGroupResponse']]:
        """
        The reference of the NetworkSecurityGroup resource.
        """
        return pulumi.get(self, "network_security_group")

    @property
    @pulumi.getter
    def primary(self) -> pulumi.Output[Optional[bool]]:
        """
        Gets whether this is a primary network interface on a virtual machine.
        """
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[Optional[str]]:
        """
        The resource GUID property of the network interface resource.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tapConfigurations")
    def tap_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.NetworkInterfaceTapConfigurationResponse']]]:
        """
        A list of TapConfigurations of the network interface.
        """
        return pulumi.get(self, "tap_configurations")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(self) -> pulumi.Output['outputs.SubResourceResponse']:
        """
        The reference of a virtual machine.
        """
        return pulumi.get(self, "virtual_machine")

