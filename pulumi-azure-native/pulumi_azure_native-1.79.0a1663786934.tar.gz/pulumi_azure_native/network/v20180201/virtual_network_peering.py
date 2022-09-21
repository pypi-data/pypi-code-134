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

__all__ = ['VirtualNetworkPeeringInitArgs', 'VirtualNetworkPeering']

@pulumi.input_type
class VirtualNetworkPeeringInitArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 virtual_network_name: pulumi.Input[str],
                 allow_forwarded_traffic: Optional[pulumi.Input[bool]] = None,
                 allow_gateway_transit: Optional[pulumi.Input[bool]] = None,
                 allow_virtual_network_access: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peering_state: Optional[pulumi.Input[Union[str, 'VirtualNetworkPeeringState']]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 remote_address_space: Optional[pulumi.Input['AddressSpaceArgs']] = None,
                 remote_virtual_network: Optional[pulumi.Input['SubResourceArgs']] = None,
                 use_remote_gateways: Optional[pulumi.Input[bool]] = None,
                 virtual_network_peering_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VirtualNetworkPeering resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] virtual_network_name: The name of the virtual network.
        :param pulumi.Input[bool] allow_forwarded_traffic: Whether the forwarded traffic from the VMs in the remote virtual network will be allowed/disallowed.
        :param pulumi.Input[bool] allow_gateway_transit: If gateway links can be used in remote virtual networking to link to this virtual network.
        :param pulumi.Input[bool] allow_virtual_network_access: Whether the VMs in the linked virtual network space would be able to access all the VMs in local Virtual network space.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: The name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[Union[str, 'VirtualNetworkPeeringState']] peering_state: The status of the virtual network peering. Possible values are 'Initiated', 'Connected', and 'Disconnected'.
        :param pulumi.Input[str] provisioning_state: The provisioning state of the resource.
        :param pulumi.Input['AddressSpaceArgs'] remote_address_space: The reference of the remote virtual network address space.
        :param pulumi.Input['SubResourceArgs'] remote_virtual_network: The reference of the remote virtual network. The remote virtual network can be in the same or different region (preview). See here to register for the preview and learn more (https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-create-peering).
        :param pulumi.Input[bool] use_remote_gateways: If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.
        :param pulumi.Input[str] virtual_network_peering_name: The name of the peering.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "virtual_network_name", virtual_network_name)
        if allow_forwarded_traffic is not None:
            pulumi.set(__self__, "allow_forwarded_traffic", allow_forwarded_traffic)
        if allow_gateway_transit is not None:
            pulumi.set(__self__, "allow_gateway_transit", allow_gateway_transit)
        if allow_virtual_network_access is not None:
            pulumi.set(__self__, "allow_virtual_network_access", allow_virtual_network_access)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if peering_state is not None:
            pulumi.set(__self__, "peering_state", peering_state)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if remote_address_space is not None:
            pulumi.set(__self__, "remote_address_space", remote_address_space)
        if remote_virtual_network is not None:
            pulumi.set(__self__, "remote_virtual_network", remote_virtual_network)
        if use_remote_gateways is not None:
            pulumi.set(__self__, "use_remote_gateways", use_remote_gateways)
        if virtual_network_peering_name is not None:
            pulumi.set(__self__, "virtual_network_peering_name", virtual_network_peering_name)

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
    @pulumi.getter(name="virtualNetworkName")
    def virtual_network_name(self) -> pulumi.Input[str]:
        """
        The name of the virtual network.
        """
        return pulumi.get(self, "virtual_network_name")

    @virtual_network_name.setter
    def virtual_network_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_network_name", value)

    @property
    @pulumi.getter(name="allowForwardedTraffic")
    def allow_forwarded_traffic(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the forwarded traffic from the VMs in the remote virtual network will be allowed/disallowed.
        """
        return pulumi.get(self, "allow_forwarded_traffic")

    @allow_forwarded_traffic.setter
    def allow_forwarded_traffic(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_forwarded_traffic", value)

    @property
    @pulumi.getter(name="allowGatewayTransit")
    def allow_gateway_transit(self) -> Optional[pulumi.Input[bool]]:
        """
        If gateway links can be used in remote virtual networking to link to this virtual network.
        """
        return pulumi.get(self, "allow_gateway_transit")

    @allow_gateway_transit.setter
    def allow_gateway_transit(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_gateway_transit", value)

    @property
    @pulumi.getter(name="allowVirtualNetworkAccess")
    def allow_virtual_network_access(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the VMs in the linked virtual network space would be able to access all the VMs in local Virtual network space.
        """
        return pulumi.get(self, "allow_virtual_network_access")

    @allow_virtual_network_access.setter
    def allow_virtual_network_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_virtual_network_access", value)

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
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="peeringState")
    def peering_state(self) -> Optional[pulumi.Input[Union[str, 'VirtualNetworkPeeringState']]]:
        """
        The status of the virtual network peering. Possible values are 'Initiated', 'Connected', and 'Disconnected'.
        """
        return pulumi.get(self, "peering_state")

    @peering_state.setter
    def peering_state(self, value: Optional[pulumi.Input[Union[str, 'VirtualNetworkPeeringState']]]):
        pulumi.set(self, "peering_state", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="remoteAddressSpace")
    def remote_address_space(self) -> Optional[pulumi.Input['AddressSpaceArgs']]:
        """
        The reference of the remote virtual network address space.
        """
        return pulumi.get(self, "remote_address_space")

    @remote_address_space.setter
    def remote_address_space(self, value: Optional[pulumi.Input['AddressSpaceArgs']]):
        pulumi.set(self, "remote_address_space", value)

    @property
    @pulumi.getter(name="remoteVirtualNetwork")
    def remote_virtual_network(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The reference of the remote virtual network. The remote virtual network can be in the same or different region (preview). See here to register for the preview and learn more (https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-create-peering).
        """
        return pulumi.get(self, "remote_virtual_network")

    @remote_virtual_network.setter
    def remote_virtual_network(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "remote_virtual_network", value)

    @property
    @pulumi.getter(name="useRemoteGateways")
    def use_remote_gateways(self) -> Optional[pulumi.Input[bool]]:
        """
        If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.
        """
        return pulumi.get(self, "use_remote_gateways")

    @use_remote_gateways.setter
    def use_remote_gateways(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_remote_gateways", value)

    @property
    @pulumi.getter(name="virtualNetworkPeeringName")
    def virtual_network_peering_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the peering.
        """
        return pulumi.get(self, "virtual_network_peering_name")

    @virtual_network_peering_name.setter
    def virtual_network_peering_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_network_peering_name", value)


warnings.warn("""Version 2018-02-01 will be removed in v2 of the provider.""", DeprecationWarning)


class VirtualNetworkPeering(pulumi.CustomResource):
    warnings.warn("""Version 2018-02-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_forwarded_traffic: Optional[pulumi.Input[bool]] = None,
                 allow_gateway_transit: Optional[pulumi.Input[bool]] = None,
                 allow_virtual_network_access: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peering_state: Optional[pulumi.Input[Union[str, 'VirtualNetworkPeeringState']]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 remote_address_space: Optional[pulumi.Input[pulumi.InputType['AddressSpaceArgs']]] = None,
                 remote_virtual_network: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 use_remote_gateways: Optional[pulumi.Input[bool]] = None,
                 virtual_network_name: Optional[pulumi.Input[str]] = None,
                 virtual_network_peering_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Peerings in a virtual network resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_forwarded_traffic: Whether the forwarded traffic from the VMs in the remote virtual network will be allowed/disallowed.
        :param pulumi.Input[bool] allow_gateway_transit: If gateway links can be used in remote virtual networking to link to this virtual network.
        :param pulumi.Input[bool] allow_virtual_network_access: Whether the VMs in the linked virtual network space would be able to access all the VMs in local Virtual network space.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: The name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[Union[str, 'VirtualNetworkPeeringState']] peering_state: The status of the virtual network peering. Possible values are 'Initiated', 'Connected', and 'Disconnected'.
        :param pulumi.Input[str] provisioning_state: The provisioning state of the resource.
        :param pulumi.Input[pulumi.InputType['AddressSpaceArgs']] remote_address_space: The reference of the remote virtual network address space.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] remote_virtual_network: The reference of the remote virtual network. The remote virtual network can be in the same or different region (preview). See here to register for the preview and learn more (https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-create-peering).
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[bool] use_remote_gateways: If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.
        :param pulumi.Input[str] virtual_network_name: The name of the virtual network.
        :param pulumi.Input[str] virtual_network_peering_name: The name of the peering.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualNetworkPeeringInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Peerings in a virtual network resource.

        :param str resource_name: The name of the resource.
        :param VirtualNetworkPeeringInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualNetworkPeeringInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_forwarded_traffic: Optional[pulumi.Input[bool]] = None,
                 allow_gateway_transit: Optional[pulumi.Input[bool]] = None,
                 allow_virtual_network_access: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peering_state: Optional[pulumi.Input[Union[str, 'VirtualNetworkPeeringState']]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 remote_address_space: Optional[pulumi.Input[pulumi.InputType['AddressSpaceArgs']]] = None,
                 remote_virtual_network: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 use_remote_gateways: Optional[pulumi.Input[bool]] = None,
                 virtual_network_name: Optional[pulumi.Input[str]] = None,
                 virtual_network_peering_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""VirtualNetworkPeering is deprecated: Version 2018-02-01 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualNetworkPeeringInitArgs.__new__(VirtualNetworkPeeringInitArgs)

            __props__.__dict__["allow_forwarded_traffic"] = allow_forwarded_traffic
            __props__.__dict__["allow_gateway_transit"] = allow_gateway_transit
            __props__.__dict__["allow_virtual_network_access"] = allow_virtual_network_access
            __props__.__dict__["id"] = id
            __props__.__dict__["name"] = name
            __props__.__dict__["peering_state"] = peering_state
            __props__.__dict__["provisioning_state"] = provisioning_state
            __props__.__dict__["remote_address_space"] = remote_address_space
            __props__.__dict__["remote_virtual_network"] = remote_virtual_network
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["use_remote_gateways"] = use_remote_gateways
            if virtual_network_name is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_network_name'")
            __props__.__dict__["virtual_network_name"] = virtual_network_name
            __props__.__dict__["virtual_network_peering_name"] = virtual_network_peering_name
            __props__.__dict__["etag"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20160601:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20160901:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20161201:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20170301:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20170601:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20170801:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20170901:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20171001:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20171101:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20180101:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20180401:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20180601:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20180701:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20180801:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20181001:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20181101:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20181201:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20190201:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20190401:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20190601:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20190701:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20190801:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20190901:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20191101:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20191201:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20200301:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20200401:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20200501:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20200601:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20200701:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20200801:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20201101:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20210201:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20210301:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20210501:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20210801:VirtualNetworkPeering"), pulumi.Alias(type_="azure-native:network/v20220101:VirtualNetworkPeering")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualNetworkPeering, __self__).__init__(
            'azure-native:network/v20180201:VirtualNetworkPeering',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualNetworkPeering':
        """
        Get an existing VirtualNetworkPeering resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualNetworkPeeringInitArgs.__new__(VirtualNetworkPeeringInitArgs)

        __props__.__dict__["allow_forwarded_traffic"] = None
        __props__.__dict__["allow_gateway_transit"] = None
        __props__.__dict__["allow_virtual_network_access"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peering_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["remote_address_space"] = None
        __props__.__dict__["remote_virtual_network"] = None
        __props__.__dict__["use_remote_gateways"] = None
        return VirtualNetworkPeering(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowForwardedTraffic")
    def allow_forwarded_traffic(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the forwarded traffic from the VMs in the remote virtual network will be allowed/disallowed.
        """
        return pulumi.get(self, "allow_forwarded_traffic")

    @property
    @pulumi.getter(name="allowGatewayTransit")
    def allow_gateway_transit(self) -> pulumi.Output[Optional[bool]]:
        """
        If gateway links can be used in remote virtual networking to link to this virtual network.
        """
        return pulumi.get(self, "allow_gateway_transit")

    @property
    @pulumi.getter(name="allowVirtualNetworkAccess")
    def allow_virtual_network_access(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the VMs in the linked virtual network space would be able to access all the VMs in local Virtual network space.
        """
        return pulumi.get(self, "allow_virtual_network_access")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peeringState")
    def peering_state(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the virtual network peering. Possible values are 'Initiated', 'Connected', and 'Disconnected'.
        """
        return pulumi.get(self, "peering_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="remoteAddressSpace")
    def remote_address_space(self) -> pulumi.Output[Optional['outputs.AddressSpaceResponse']]:
        """
        The reference of the remote virtual network address space.
        """
        return pulumi.get(self, "remote_address_space")

    @property
    @pulumi.getter(name="remoteVirtualNetwork")
    def remote_virtual_network(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The reference of the remote virtual network. The remote virtual network can be in the same or different region (preview). See here to register for the preview and learn more (https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-create-peering).
        """
        return pulumi.get(self, "remote_virtual_network")

    @property
    @pulumi.getter(name="useRemoteGateways")
    def use_remote_gateways(self) -> pulumi.Output[Optional[bool]]:
        """
        If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.
        """
        return pulumi.get(self, "use_remote_gateways")

