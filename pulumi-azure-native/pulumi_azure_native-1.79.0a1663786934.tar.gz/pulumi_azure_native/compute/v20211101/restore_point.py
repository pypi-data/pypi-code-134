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

__all__ = ['RestorePointArgs', 'RestorePoint']

@pulumi.input_type
class RestorePointArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 restore_point_collection_name: pulumi.Input[str],
                 exclude_disks: Optional[pulumi.Input[Sequence[pulumi.Input['ApiEntityReferenceArgs']]]] = None,
                 restore_point_name: Optional[pulumi.Input[str]] = None,
                 source_restore_point: Optional[pulumi.Input['ApiEntityReferenceArgs']] = None,
                 time_created: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RestorePoint resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] restore_point_collection_name: The name of the restore point collection.
        :param pulumi.Input[Sequence[pulumi.Input['ApiEntityReferenceArgs']]] exclude_disks: List of disk resource ids that the customer wishes to exclude from the restore point. If no disks are specified, all disks will be included.
        :param pulumi.Input[str] restore_point_name: The name of the restore point.
        :param pulumi.Input['ApiEntityReferenceArgs'] source_restore_point: Resource Id of the source restore point from which a copy needs to be created.
        :param pulumi.Input[str] time_created: Gets the creation time of the restore point.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "restore_point_collection_name", restore_point_collection_name)
        if exclude_disks is not None:
            pulumi.set(__self__, "exclude_disks", exclude_disks)
        if restore_point_name is not None:
            pulumi.set(__self__, "restore_point_name", restore_point_name)
        if source_restore_point is not None:
            pulumi.set(__self__, "source_restore_point", source_restore_point)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)

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
    @pulumi.getter(name="restorePointCollectionName")
    def restore_point_collection_name(self) -> pulumi.Input[str]:
        """
        The name of the restore point collection.
        """
        return pulumi.get(self, "restore_point_collection_name")

    @restore_point_collection_name.setter
    def restore_point_collection_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "restore_point_collection_name", value)

    @property
    @pulumi.getter(name="excludeDisks")
    def exclude_disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApiEntityReferenceArgs']]]]:
        """
        List of disk resource ids that the customer wishes to exclude from the restore point. If no disks are specified, all disks will be included.
        """
        return pulumi.get(self, "exclude_disks")

    @exclude_disks.setter
    def exclude_disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApiEntityReferenceArgs']]]]):
        pulumi.set(self, "exclude_disks", value)

    @property
    @pulumi.getter(name="restorePointName")
    def restore_point_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the restore point.
        """
        return pulumi.get(self, "restore_point_name")

    @restore_point_name.setter
    def restore_point_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restore_point_name", value)

    @property
    @pulumi.getter(name="sourceRestorePoint")
    def source_restore_point(self) -> Optional[pulumi.Input['ApiEntityReferenceArgs']]:
        """
        Resource Id of the source restore point from which a copy needs to be created.
        """
        return pulumi.get(self, "source_restore_point")

    @source_restore_point.setter
    def source_restore_point(self, value: Optional[pulumi.Input['ApiEntityReferenceArgs']]):
        pulumi.set(self, "source_restore_point", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        Gets the creation time of the restore point.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)


class RestorePoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 exclude_disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApiEntityReferenceArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restore_point_collection_name: Optional[pulumi.Input[str]] = None,
                 restore_point_name: Optional[pulumi.Input[str]] = None,
                 source_restore_point: Optional[pulumi.Input[pulumi.InputType['ApiEntityReferenceArgs']]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Restore Point details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApiEntityReferenceArgs']]]] exclude_disks: List of disk resource ids that the customer wishes to exclude from the restore point. If no disks are specified, all disks will be included.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] restore_point_collection_name: The name of the restore point collection.
        :param pulumi.Input[str] restore_point_name: The name of the restore point.
        :param pulumi.Input[pulumi.InputType['ApiEntityReferenceArgs']] source_restore_point: Resource Id of the source restore point from which a copy needs to be created.
        :param pulumi.Input[str] time_created: Gets the creation time of the restore point.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RestorePointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Restore Point details.

        :param str resource_name: The name of the resource.
        :param RestorePointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RestorePointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 exclude_disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApiEntityReferenceArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restore_point_collection_name: Optional[pulumi.Input[str]] = None,
                 restore_point_name: Optional[pulumi.Input[str]] = None,
                 source_restore_point: Optional[pulumi.Input[pulumi.InputType['ApiEntityReferenceArgs']]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RestorePointArgs.__new__(RestorePointArgs)

            __props__.__dict__["exclude_disks"] = exclude_disks
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if restore_point_collection_name is None and not opts.urn:
                raise TypeError("Missing required property 'restore_point_collection_name'")
            __props__.__dict__["restore_point_collection_name"] = restore_point_collection_name
            __props__.__dict__["restore_point_name"] = restore_point_name
            __props__.__dict__["source_restore_point"] = source_restore_point
            __props__.__dict__["time_created"] = time_created
            __props__.__dict__["consistency_mode"] = None
            __props__.__dict__["instance_view"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["source_metadata"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:compute:RestorePoint"), pulumi.Alias(type_="azure-native:compute/v20210301:RestorePoint"), pulumi.Alias(type_="azure-native:compute/v20210401:RestorePoint"), pulumi.Alias(type_="azure-native:compute/v20210701:RestorePoint"), pulumi.Alias(type_="azure-native:compute/v20220301:RestorePoint")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RestorePoint, __self__).__init__(
            'azure-native:compute/v20211101:RestorePoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RestorePoint':
        """
        Get an existing RestorePoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RestorePointArgs.__new__(RestorePointArgs)

        __props__.__dict__["consistency_mode"] = None
        __props__.__dict__["exclude_disks"] = None
        __props__.__dict__["instance_view"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["source_metadata"] = None
        __props__.__dict__["source_restore_point"] = None
        __props__.__dict__["time_created"] = None
        __props__.__dict__["type"] = None
        return RestorePoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="consistencyMode")
    def consistency_mode(self) -> pulumi.Output[str]:
        """
        Gets the consistency mode for the restore point. Please refer to https://aka.ms/RestorePoints for more details.
        """
        return pulumi.get(self, "consistency_mode")

    @property
    @pulumi.getter(name="excludeDisks")
    def exclude_disks(self) -> pulumi.Output[Optional[Sequence['outputs.ApiEntityReferenceResponse']]]:
        """
        List of disk resource ids that the customer wishes to exclude from the restore point. If no disks are specified, all disks will be included.
        """
        return pulumi.get(self, "exclude_disks")

    @property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> pulumi.Output['outputs.RestorePointInstanceViewResponse']:
        """
        The restore point instance view.
        """
        return pulumi.get(self, "instance_view")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets the provisioning state of the restore point.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sourceMetadata")
    def source_metadata(self) -> pulumi.Output['outputs.RestorePointSourceMetadataResponse']:
        """
        Gets the details of the VM captured at the time of the restore point creation.
        """
        return pulumi.get(self, "source_metadata")

    @property
    @pulumi.getter(name="sourceRestorePoint")
    def source_restore_point(self) -> pulumi.Output[Optional['outputs.ApiEntityReferenceResponse']]:
        """
        Resource Id of the source restore point from which a copy needs to be created.
        """
        return pulumi.get(self, "source_restore_point")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[Optional[str]]:
        """
        Gets the creation time of the restore point.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

