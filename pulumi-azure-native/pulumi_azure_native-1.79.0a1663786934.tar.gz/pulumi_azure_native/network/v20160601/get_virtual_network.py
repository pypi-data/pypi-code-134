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

__all__ = [
    'GetVirtualNetworkResult',
    'AwaitableGetVirtualNetworkResult',
    'get_virtual_network',
    'get_virtual_network_output',
]

warnings.warn("""Version 2016-06-01 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetVirtualNetworkResult:
    """
    Virtual Network resource
    """
    def __init__(__self__, address_space=None, dhcp_options=None, etag=None, id=None, location=None, name=None, provisioning_state=None, resource_guid=None, subnets=None, tags=None, type=None, virtual_network_peerings=None):
        if address_space and not isinstance(address_space, dict):
            raise TypeError("Expected argument 'address_space' to be a dict")
        pulumi.set(__self__, "address_space", address_space)
        if dhcp_options and not isinstance(dhcp_options, dict):
            raise TypeError("Expected argument 'dhcp_options' to be a dict")
        pulumi.set(__self__, "dhcp_options", dhcp_options)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_guid and not isinstance(resource_guid, str):
            raise TypeError("Expected argument 'resource_guid' to be a str")
        pulumi.set(__self__, "resource_guid", resource_guid)
        if subnets and not isinstance(subnets, list):
            raise TypeError("Expected argument 'subnets' to be a list")
        pulumi.set(__self__, "subnets", subnets)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_network_peerings and not isinstance(virtual_network_peerings, list):
            raise TypeError("Expected argument 'virtual_network_peerings' to be a list")
        pulumi.set(__self__, "virtual_network_peerings", virtual_network_peerings)

    @property
    @pulumi.getter(name="addressSpace")
    def address_space(self) -> Optional['outputs.AddressSpaceResponse']:
        """
        Gets or sets AddressSpace that contains an array of IP address ranges that can be used by subnets
        """
        return pulumi.get(self, "address_space")

    @property
    @pulumi.getter(name="dhcpOptions")
    def dhcp_options(self) -> Optional['outputs.DhcpOptionsResponse']:
        """
        Gets or sets DHCPOptions that contains an array of DNS servers available to VMs deployed in the virtual network
        """
        return pulumi.get(self, "dhcp_options")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Gets a unique read-only string that changes whenever the resource is updated
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        Gets provisioning state of the PublicIP resource Updating/Deleting/Failed
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> Optional[str]:
        """
        Gets or sets resource guid property of the VirtualNetwork resource
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence['outputs.SubnetResponse']]:
        """
        Gets or sets list of subnets in a VirtualNetwork
        """
        return pulumi.get(self, "subnets")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetworkPeerings")
    def virtual_network_peerings(self) -> Optional[Sequence['outputs.VirtualNetworkPeeringResponse']]:
        """
        Gets or sets list of peerings in a VirtualNetwork
        """
        return pulumi.get(self, "virtual_network_peerings")


class AwaitableGetVirtualNetworkResult(GetVirtualNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualNetworkResult(
            address_space=self.address_space,
            dhcp_options=self.dhcp_options,
            etag=self.etag,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            resource_guid=self.resource_guid,
            subnets=self.subnets,
            tags=self.tags,
            type=self.type,
            virtual_network_peerings=self.virtual_network_peerings)


def get_virtual_network(expand: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        virtual_network_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualNetworkResult:
    """
    Virtual Network resource


    :param str expand: expand references resources.
    :param str resource_group_name: The name of the resource group.
    :param str virtual_network_name: The name of the virtual network.
    """
    pulumi.log.warn("""get_virtual_network is deprecated: Version 2016-06-01 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualNetworkName'] = virtual_network_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20160601:getVirtualNetwork', __args__, opts=opts, typ=GetVirtualNetworkResult).value

    return AwaitableGetVirtualNetworkResult(
        address_space=__ret__.address_space,
        dhcp_options=__ret__.dhcp_options,
        etag=__ret__.etag,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        resource_guid=__ret__.resource_guid,
        subnets=__ret__.subnets,
        tags=__ret__.tags,
        type=__ret__.type,
        virtual_network_peerings=__ret__.virtual_network_peerings)


@_utilities.lift_output_func(get_virtual_network)
def get_virtual_network_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               virtual_network_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualNetworkResult]:
    """
    Virtual Network resource


    :param str expand: expand references resources.
    :param str resource_group_name: The name of the resource group.
    :param str virtual_network_name: The name of the virtual network.
    """
    pulumi.log.warn("""get_virtual_network is deprecated: Version 2016-06-01 will be removed in v2 of the provider.""")
    ...
