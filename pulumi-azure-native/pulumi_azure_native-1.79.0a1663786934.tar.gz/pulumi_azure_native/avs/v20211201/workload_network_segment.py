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
from ._inputs import *

__all__ = ['WorkloadNetworkSegmentArgs', 'WorkloadNetworkSegment']

@pulumi.input_type
class WorkloadNetworkSegmentArgs:
    def __init__(__self__, *,
                 private_cloud_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 connected_gateway: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 revision: Optional[pulumi.Input[float]] = None,
                 segment_id: Optional[pulumi.Input[str]] = None,
                 subnet: Optional[pulumi.Input['WorkloadNetworkSegmentSubnetArgs']] = None):
        """
        The set of arguments for constructing a WorkloadNetworkSegment resource.
        :param pulumi.Input[str] private_cloud_name: Name of the private cloud
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] connected_gateway: Gateway which to connect segment to.
        :param pulumi.Input[str] display_name: Display name of the segment.
        :param pulumi.Input[float] revision: NSX revision number.
        :param pulumi.Input[str] segment_id: NSX Segment identifier. Generally the same as the Segment's display name
        :param pulumi.Input['WorkloadNetworkSegmentSubnetArgs'] subnet: Subnet which to connect segment to.
        """
        pulumi.set(__self__, "private_cloud_name", private_cloud_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if connected_gateway is not None:
            pulumi.set(__self__, "connected_gateway", connected_gateway)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if revision is not None:
            pulumi.set(__self__, "revision", revision)
        if segment_id is not None:
            pulumi.set(__self__, "segment_id", segment_id)
        if subnet is not None:
            pulumi.set(__self__, "subnet", subnet)

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
    @pulumi.getter(name="connectedGateway")
    def connected_gateway(self) -> Optional[pulumi.Input[str]]:
        """
        Gateway which to connect segment to.
        """
        return pulumi.get(self, "connected_gateway")

    @connected_gateway.setter
    def connected_gateway(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connected_gateway", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the segment.
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

    @property
    @pulumi.getter(name="segmentId")
    def segment_id(self) -> Optional[pulumi.Input[str]]:
        """
        NSX Segment identifier. Generally the same as the Segment's display name
        """
        return pulumi.get(self, "segment_id")

    @segment_id.setter
    def segment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "segment_id", value)

    @property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input['WorkloadNetworkSegmentSubnetArgs']]:
        """
        Subnet which to connect segment to.
        """
        return pulumi.get(self, "subnet")

    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input['WorkloadNetworkSegmentSubnetArgs']]):
        pulumi.set(self, "subnet", value)


class WorkloadNetworkSegment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connected_gateway: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 revision: Optional[pulumi.Input[float]] = None,
                 segment_id: Optional[pulumi.Input[str]] = None,
                 subnet: Optional[pulumi.Input[pulumi.InputType['WorkloadNetworkSegmentSubnetArgs']]] = None,
                 __props__=None):
        """
        NSX Segment

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connected_gateway: Gateway which to connect segment to.
        :param pulumi.Input[str] display_name: Display name of the segment.
        :param pulumi.Input[str] private_cloud_name: Name of the private cloud
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[float] revision: NSX revision number.
        :param pulumi.Input[str] segment_id: NSX Segment identifier. Generally the same as the Segment's display name
        :param pulumi.Input[pulumi.InputType['WorkloadNetworkSegmentSubnetArgs']] subnet: Subnet which to connect segment to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkloadNetworkSegmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        NSX Segment

        :param str resource_name: The name of the resource.
        :param WorkloadNetworkSegmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkloadNetworkSegmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connected_gateway: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 revision: Optional[pulumi.Input[float]] = None,
                 segment_id: Optional[pulumi.Input[str]] = None,
                 subnet: Optional[pulumi.Input[pulumi.InputType['WorkloadNetworkSegmentSubnetArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkloadNetworkSegmentArgs.__new__(WorkloadNetworkSegmentArgs)

            __props__.__dict__["connected_gateway"] = connected_gateway
            __props__.__dict__["display_name"] = display_name
            if private_cloud_name is None and not opts.urn:
                raise TypeError("Missing required property 'private_cloud_name'")
            __props__.__dict__["private_cloud_name"] = private_cloud_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["revision"] = revision
            __props__.__dict__["segment_id"] = segment_id
            __props__.__dict__["subnet"] = subnet
            __props__.__dict__["name"] = None
            __props__.__dict__["port_vif"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:avs:WorkloadNetworkSegment"), pulumi.Alias(type_="azure-native:avs/v20200717preview:WorkloadNetworkSegment"), pulumi.Alias(type_="azure-native:avs/v20210101preview:WorkloadNetworkSegment"), pulumi.Alias(type_="azure-native:avs/v20210601:WorkloadNetworkSegment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkloadNetworkSegment, __self__).__init__(
            'azure-native:avs/v20211201:WorkloadNetworkSegment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkloadNetworkSegment':
        """
        Get an existing WorkloadNetworkSegment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkloadNetworkSegmentArgs.__new__(WorkloadNetworkSegmentArgs)

        __props__.__dict__["connected_gateway"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["port_vif"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["revision"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["subnet"] = None
        __props__.__dict__["type"] = None
        return WorkloadNetworkSegment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectedGateway")
    def connected_gateway(self) -> pulumi.Output[Optional[str]]:
        """
        Gateway which to connect segment to.
        """
        return pulumi.get(self, "connected_gateway")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Display name of the segment.
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
    @pulumi.getter(name="portVif")
    def port_vif(self) -> pulumi.Output[Sequence['outputs.WorkloadNetworkSegmentPortVifResponse']]:
        """
        Port Vif which segment is associated with.
        """
        return pulumi.get(self, "port_vif")

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
    def status(self) -> pulumi.Output[str]:
        """
        Segment status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def subnet(self) -> pulumi.Output[Optional['outputs.WorkloadNetworkSegmentSubnetResponse']]:
        """
        Subnet which to connect segment to.
        """
        return pulumi.get(self, "subnet")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

