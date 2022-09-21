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

__all__ = ['WorkloadNetworkDhcpArgs', 'WorkloadNetworkDhcp']

@pulumi.input_type
class WorkloadNetworkDhcpArgs:
    def __init__(__self__, *,
                 dhcp_type: pulumi.Input[Union[str, 'DhcpTypeEnum']],
                 private_cloud_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 dhcp_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 revision: Optional[pulumi.Input[float]] = None):
        """
        The set of arguments for constructing a WorkloadNetworkDhcp resource.
        :param pulumi.Input[Union[str, 'DhcpTypeEnum']] dhcp_type: Type of DHCP: SERVER or RELAY.
        :param pulumi.Input[str] private_cloud_name: Name of the private cloud
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] dhcp_id: NSX DHCP identifier. Generally the same as the DHCP display name
        :param pulumi.Input[str] display_name: Display name of the DHCP entity.
        :param pulumi.Input[float] revision: NSX revision number.
        """
        pulumi.set(__self__, "dhcp_type", dhcp_type)
        pulumi.set(__self__, "private_cloud_name", private_cloud_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if dhcp_id is not None:
            pulumi.set(__self__, "dhcp_id", dhcp_id)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if revision is not None:
            pulumi.set(__self__, "revision", revision)

    @property
    @pulumi.getter(name="dhcpType")
    def dhcp_type(self) -> pulumi.Input[Union[str, 'DhcpTypeEnum']]:
        """
        Type of DHCP: SERVER or RELAY.
        """
        return pulumi.get(self, "dhcp_type")

    @dhcp_type.setter
    def dhcp_type(self, value: pulumi.Input[Union[str, 'DhcpTypeEnum']]):
        pulumi.set(self, "dhcp_type", value)

    @property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Input[str]:
        """
        Name of the private cloud
        """
        return pulumi.get(self, "private_cloud_name")

    @private_cloud_name.setter
    def private_cloud_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_cloud_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="dhcpId")
    def dhcp_id(self) -> Optional[pulumi.Input[str]]:
        """
        NSX DHCP identifier. Generally the same as the DHCP display name
        """
        return pulumi.get(self, "dhcp_id")

    @dhcp_id.setter
    def dhcp_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dhcp_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the DHCP entity.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[float]]:
        """
        NSX revision number.
        """
        return pulumi.get(self, "revision")

    @revision.setter
    def revision(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "revision", value)


class WorkloadNetworkDhcp(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dhcp_id: Optional[pulumi.Input[str]] = None,
                 dhcp_type: Optional[pulumi.Input[Union[str, 'DhcpTypeEnum']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 revision: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        """
        NSX DHCP

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dhcp_id: NSX DHCP identifier. Generally the same as the DHCP display name
        :param pulumi.Input[Union[str, 'DhcpTypeEnum']] dhcp_type: Type of DHCP: SERVER or RELAY.
        :param pulumi.Input[str] display_name: Display name of the DHCP entity.
        :param pulumi.Input[str] private_cloud_name: Name of the private cloud
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[float] revision: NSX revision number.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkloadNetworkDhcpArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        NSX DHCP

        :param str resource_name: The name of the resource.
        :param WorkloadNetworkDhcpArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkloadNetworkDhcpArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dhcp_id: Optional[pulumi.Input[str]] = None,
                 dhcp_type: Optional[pulumi.Input[Union[str, 'DhcpTypeEnum']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 revision: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkloadNetworkDhcpArgs.__new__(WorkloadNetworkDhcpArgs)

            __props__.__dict__["dhcp_id"] = dhcp_id
            if dhcp_type is None and not opts.urn:
                raise TypeError("Missing required property 'dhcp_type'")
            __props__.__dict__["dhcp_type"] = dhcp_type
            __props__.__dict__["display_name"] = display_name
            if private_cloud_name is None and not opts.urn:
                raise TypeError("Missing required property 'private_cloud_name'")
            __props__.__dict__["private_cloud_name"] = private_cloud_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["revision"] = revision
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["segments"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:avs:WorkloadNetworkDhcp"), pulumi.Alias(type_="azure-native:avs/v20210101preview:WorkloadNetworkDhcp"), pulumi.Alias(type_="azure-native:avs/v20210601:WorkloadNetworkDhcp"), pulumi.Alias(type_="azure-native:avs/v20211201:WorkloadNetworkDhcp")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkloadNetworkDhcp, __self__).__init__(
            'azure-native:avs/v20200717preview:WorkloadNetworkDhcp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkloadNetworkDhcp':
        """
        Get an existing WorkloadNetworkDhcp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkloadNetworkDhcpArgs.__new__(WorkloadNetworkDhcpArgs)

        __props__.__dict__["dhcp_type"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["revision"] = None
        __props__.__dict__["segments"] = None
        __props__.__dict__["type"] = None
        return WorkloadNetworkDhcp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dhcpType")
    def dhcp_type(self) -> pulumi.Output[str]:
        """
        Type of DHCP: SERVER or RELAY.
        """
        return pulumi.get(self, "dhcp_type")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Display name of the DHCP entity.
        """
        return pulumi.get(self, "display_name")

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
        The provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def revision(self) -> pulumi.Output[Optional[float]]:
        """
        NSX revision number.
        """
        return pulumi.get(self, "revision")

    @property
    @pulumi.getter
    def segments(self) -> pulumi.Output[Sequence[str]]:
        """
        NSX Segments consuming DHCP.
        """
        return pulumi.get(self, "segments")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

