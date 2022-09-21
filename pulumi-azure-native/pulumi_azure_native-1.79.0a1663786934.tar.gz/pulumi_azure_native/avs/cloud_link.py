# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CloudLinkArgs', 'CloudLink']

@pulumi.input_type
class CloudLinkArgs:
    def __init__(__self__, *,
                 private_cloud_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 cloud_link_name: Optional[pulumi.Input[str]] = None,
                 linked_cloud: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CloudLink resource.
        :param pulumi.Input[str] private_cloud_name: The name of the private cloud.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] cloud_link_name: Name of the cloud link resource
        :param pulumi.Input[str] linked_cloud: Identifier of the other private cloud participating in the link.
        """
        pulumi.set(__self__, "private_cloud_name", private_cloud_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if cloud_link_name is not None:
            pulumi.set(__self__, "cloud_link_name", cloud_link_name)
        if linked_cloud is not None:
            pulumi.set(__self__, "linked_cloud", linked_cloud)

    @property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Input[str]:
        """
        The name of the private cloud.
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
    @pulumi.getter(name="cloudLinkName")
    def cloud_link_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the cloud link resource
        """
        return pulumi.get(self, "cloud_link_name")

    @cloud_link_name.setter
    def cloud_link_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_link_name", value)

    @property
    @pulumi.getter(name="linkedCloud")
    def linked_cloud(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the other private cloud participating in the link.
        """
        return pulumi.get(self, "linked_cloud")

    @linked_cloud.setter
    def linked_cloud(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "linked_cloud", value)


class CloudLink(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_link_name: Optional[pulumi.Input[str]] = None,
                 linked_cloud: Optional[pulumi.Input[str]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A cloud link resource
        API Version: 2021-06-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloud_link_name: Name of the cloud link resource
        :param pulumi.Input[str] linked_cloud: Identifier of the other private cloud participating in the link.
        :param pulumi.Input[str] private_cloud_name: The name of the private cloud.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CloudLinkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A cloud link resource
        API Version: 2021-06-01.

        :param str resource_name: The name of the resource.
        :param CloudLinkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudLinkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_link_name: Optional[pulumi.Input[str]] = None,
                 linked_cloud: Optional[pulumi.Input[str]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CloudLinkArgs.__new__(CloudLinkArgs)

            __props__.__dict__["cloud_link_name"] = cloud_link_name
            __props__.__dict__["linked_cloud"] = linked_cloud
            if private_cloud_name is None and not opts.urn:
                raise TypeError("Missing required property 'private_cloud_name'")
            __props__.__dict__["private_cloud_name"] = private_cloud_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:avs/v20210601:CloudLink"), pulumi.Alias(type_="azure-native:avs/v20211201:CloudLink")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CloudLink, __self__).__init__(
            'azure-native:avs:CloudLink',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CloudLink':
        """
        Get an existing CloudLink resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CloudLinkArgs.__new__(CloudLinkArgs)

        __props__.__dict__["linked_cloud"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["type"] = None
        return CloudLink(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="linkedCloud")
    def linked_cloud(self) -> pulumi.Output[Optional[str]]:
        """
        Identifier of the other private cloud participating in the link.
        """
        return pulumi.get(self, "linked_cloud")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The state of the cloud link.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

