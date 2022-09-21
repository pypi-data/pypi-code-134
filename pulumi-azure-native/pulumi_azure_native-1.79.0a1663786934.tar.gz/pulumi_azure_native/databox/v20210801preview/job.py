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

__all__ = ['JobArgs', 'Job']

@pulumi.input_type
class JobArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['SkuArgs'],
                 transfer_type: pulumi.Input[Union[str, 'TransferType']],
                 delivery_info: Optional[pulumi.Input['JobDeliveryInfoArgs']] = None,
                 delivery_type: Optional[pulumi.Input[Union[str, 'JobDeliveryType']]] = None,
                 details: Optional[pulumi.Input[Union['DataBoxCustomerDiskJobDetailsArgs', 'DataBoxDiskJobDetailsArgs', 'DataBoxHeavyJobDetailsArgs', 'DataBoxJobDetailsArgs']]] = None,
                 identity: Optional[pulumi.Input['ResourceIdentityArgs']] = None,
                 job_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Job resource.
        :param pulumi.Input[str] resource_group_name: The Resource Group Name
        :param pulumi.Input['SkuArgs'] sku: The sku type.
        :param pulumi.Input[Union[str, 'TransferType']] transfer_type: Type of the data transfer.
        :param pulumi.Input['JobDeliveryInfoArgs'] delivery_info: Delivery Info of Job.
        :param pulumi.Input[Union[str, 'JobDeliveryType']] delivery_type: Delivery type of Job.
        :param pulumi.Input[Union['DataBoxCustomerDiskJobDetailsArgs', 'DataBoxDiskJobDetailsArgs', 'DataBoxHeavyJobDetailsArgs', 'DataBoxJobDetailsArgs']] details: Details of a job run. This field will only be sent for expand details filter.
        :param pulumi.Input['ResourceIdentityArgs'] identity: Msi identity of the resource
        :param pulumi.Input[str] job_name: The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
        :param pulumi.Input[str] location: The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups).
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        pulumi.set(__self__, "transfer_type", transfer_type)
        if delivery_info is not None:
            pulumi.set(__self__, "delivery_info", delivery_info)
        if delivery_type is None:
            delivery_type = 'NonScheduled'
        if delivery_type is not None:
            pulumi.set(__self__, "delivery_type", delivery_type)
        if details is not None:
            pulumi.set(__self__, "details", details)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if job_name is not None:
            pulumi.set(__self__, "job_name", job_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The Resource Group Name
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['SkuArgs']:
        """
        The sku type.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['SkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="transferType")
    def transfer_type(self) -> pulumi.Input[Union[str, 'TransferType']]:
        """
        Type of the data transfer.
        """
        return pulumi.get(self, "transfer_type")

    @transfer_type.setter
    def transfer_type(self, value: pulumi.Input[Union[str, 'TransferType']]):
        pulumi.set(self, "transfer_type", value)

    @property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> Optional[pulumi.Input['JobDeliveryInfoArgs']]:
        """
        Delivery Info of Job.
        """
        return pulumi.get(self, "delivery_info")

    @delivery_info.setter
    def delivery_info(self, value: Optional[pulumi.Input['JobDeliveryInfoArgs']]):
        pulumi.set(self, "delivery_info", value)

    @property
    @pulumi.getter(name="deliveryType")
    def delivery_type(self) -> Optional[pulumi.Input[Union[str, 'JobDeliveryType']]]:
        """
        Delivery type of Job.
        """
        return pulumi.get(self, "delivery_type")

    @delivery_type.setter
    def delivery_type(self, value: Optional[pulumi.Input[Union[str, 'JobDeliveryType']]]):
        pulumi.set(self, "delivery_type", value)

    @property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[Union['DataBoxCustomerDiskJobDetailsArgs', 'DataBoxDiskJobDetailsArgs', 'DataBoxHeavyJobDetailsArgs', 'DataBoxJobDetailsArgs']]]:
        """
        Details of a job run. This field will only be sent for expand details filter.
        """
        return pulumi.get(self, "details")

    @details.setter
    def details(self, value: Optional[pulumi.Input[Union['DataBoxCustomerDiskJobDetailsArgs', 'DataBoxDiskJobDetailsArgs', 'DataBoxHeavyJobDetailsArgs', 'DataBoxJobDetailsArgs']]]):
        pulumi.set(self, "details", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ResourceIdentityArgs']]:
        """
        Msi identity of the resource
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ResourceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="jobName")
    def job_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
        """
        return pulumi.get(self, "job_name")

    @job_name.setter
    def job_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups).
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Job(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delivery_info: Optional[pulumi.Input[pulumi.InputType['JobDeliveryInfoArgs']]] = None,
                 delivery_type: Optional[pulumi.Input[Union[str, 'JobDeliveryType']]] = None,
                 details: Optional[pulumi.Input[Union[pulumi.InputType['DataBoxCustomerDiskJobDetailsArgs'], pulumi.InputType['DataBoxDiskJobDetailsArgs'], pulumi.InputType['DataBoxHeavyJobDetailsArgs'], pulumi.InputType['DataBoxJobDetailsArgs']]]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ResourceIdentityArgs']]] = None,
                 job_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 transfer_type: Optional[pulumi.Input[Union[str, 'TransferType']]] = None,
                 __props__=None):
        """
        Job Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['JobDeliveryInfoArgs']] delivery_info: Delivery Info of Job.
        :param pulumi.Input[Union[str, 'JobDeliveryType']] delivery_type: Delivery type of Job.
        :param pulumi.Input[Union[pulumi.InputType['DataBoxCustomerDiskJobDetailsArgs'], pulumi.InputType['DataBoxDiskJobDetailsArgs'], pulumi.InputType['DataBoxHeavyJobDetailsArgs'], pulumi.InputType['DataBoxJobDetailsArgs']]] details: Details of a job run. This field will only be sent for expand details filter.
        :param pulumi.Input[pulumi.InputType['ResourceIdentityArgs']] identity: Msi identity of the resource
        :param pulumi.Input[str] job_name: The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
        :param pulumi.Input[str] location: The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed.
        :param pulumi.Input[str] resource_group_name: The Resource Group Name
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The sku type.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups).
        :param pulumi.Input[Union[str, 'TransferType']] transfer_type: Type of the data transfer.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: JobArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Job Resource.

        :param str resource_name: The name of the resource.
        :param JobArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(JobArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delivery_info: Optional[pulumi.Input[pulumi.InputType['JobDeliveryInfoArgs']]] = None,
                 delivery_type: Optional[pulumi.Input[Union[str, 'JobDeliveryType']]] = None,
                 details: Optional[pulumi.Input[Union[pulumi.InputType['DataBoxCustomerDiskJobDetailsArgs'], pulumi.InputType['DataBoxDiskJobDetailsArgs'], pulumi.InputType['DataBoxHeavyJobDetailsArgs'], pulumi.InputType['DataBoxJobDetailsArgs']]]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ResourceIdentityArgs']]] = None,
                 job_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 transfer_type: Optional[pulumi.Input[Union[str, 'TransferType']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = JobArgs.__new__(JobArgs)

            __props__.__dict__["delivery_info"] = delivery_info
            if delivery_type is None:
                delivery_type = 'NonScheduled'
            __props__.__dict__["delivery_type"] = delivery_type
            __props__.__dict__["details"] = details
            __props__.__dict__["identity"] = identity
            __props__.__dict__["job_name"] = job_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            if transfer_type is None and not opts.urn:
                raise TypeError("Missing required property 'transfer_type'")
            __props__.__dict__["transfer_type"] = transfer_type
            __props__.__dict__["cancellation_reason"] = None
            __props__.__dict__["error"] = None
            __props__.__dict__["is_cancellable"] = None
            __props__.__dict__["is_cancellable_without_fee"] = None
            __props__.__dict__["is_deletable"] = None
            __props__.__dict__["is_prepare_to_ship_enabled"] = None
            __props__.__dict__["is_shipping_address_editable"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["start_time"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:databox:Job"), pulumi.Alias(type_="azure-native:databox/v20180101:Job"), pulumi.Alias(type_="azure-native:databox/v20190901:Job"), pulumi.Alias(type_="azure-native:databox/v20200401:Job"), pulumi.Alias(type_="azure-native:databox/v20201101:Job"), pulumi.Alias(type_="azure-native:databox/v20210301:Job"), pulumi.Alias(type_="azure-native:databox/v20210501:Job"), pulumi.Alias(type_="azure-native:databox/v20211201:Job"), pulumi.Alias(type_="azure-native:databox/v20220201:Job")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Job, __self__).__init__(
            'azure-native:databox/v20210801preview:Job',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Job':
        """
        Get an existing Job resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = JobArgs.__new__(JobArgs)

        __props__.__dict__["cancellation_reason"] = None
        __props__.__dict__["delivery_info"] = None
        __props__.__dict__["delivery_type"] = None
        __props__.__dict__["details"] = None
        __props__.__dict__["error"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["is_cancellable"] = None
        __props__.__dict__["is_cancellable_without_fee"] = None
        __props__.__dict__["is_deletable"] = None
        __props__.__dict__["is_prepare_to_ship_enabled"] = None
        __props__.__dict__["is_shipping_address_editable"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["start_time"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["transfer_type"] = None
        __props__.__dict__["type"] = None
        return Job(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cancellationReason")
    def cancellation_reason(self) -> pulumi.Output[str]:
        """
        Reason for cancellation.
        """
        return pulumi.get(self, "cancellation_reason")

    @property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> pulumi.Output[Optional['outputs.JobDeliveryInfoResponse']]:
        """
        Delivery Info of Job.
        """
        return pulumi.get(self, "delivery_info")

    @property
    @pulumi.getter(name="deliveryType")
    def delivery_type(self) -> pulumi.Output[Optional[str]]:
        """
        Delivery type of Job.
        """
        return pulumi.get(self, "delivery_type")

    @property
    @pulumi.getter
    def details(self) -> pulumi.Output[Optional[Any]]:
        """
        Details of a job run. This field will only be sent for expand details filter.
        """
        return pulumi.get(self, "details")

    @property
    @pulumi.getter
    def error(self) -> pulumi.Output['outputs.CloudErrorResponse']:
        """
        Top level error for the job.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ResourceIdentityResponse']]:
        """
        Msi identity of the resource
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="isCancellable")
    def is_cancellable(self) -> pulumi.Output[bool]:
        """
        Describes whether the job is cancellable or not.
        """
        return pulumi.get(self, "is_cancellable")

    @property
    @pulumi.getter(name="isCancellableWithoutFee")
    def is_cancellable_without_fee(self) -> pulumi.Output[bool]:
        """
        Flag to indicate cancellation of scheduled job.
        """
        return pulumi.get(self, "is_cancellable_without_fee")

    @property
    @pulumi.getter(name="isDeletable")
    def is_deletable(self) -> pulumi.Output[bool]:
        """
        Describes whether the job is deletable or not.
        """
        return pulumi.get(self, "is_deletable")

    @property
    @pulumi.getter(name="isPrepareToShipEnabled")
    def is_prepare_to_ship_enabled(self) -> pulumi.Output[bool]:
        """
        Is Prepare To Ship Enabled on this job
        """
        return pulumi.get(self, "is_prepare_to_ship_enabled")

    @property
    @pulumi.getter(name="isShippingAddressEditable")
    def is_shipping_address_editable(self) -> pulumi.Output[bool]:
        """
        Describes whether the shipping address is editable or not.
        """
        return pulumi.get(self, "is_shipping_address_editable")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.SkuResponse']:
        """
        The sku type.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[str]:
        """
        Time at which the job was started in UTC ISO 8601 format.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Name of the stage which is in progress.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups).
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="transferType")
    def transfer_type(self) -> pulumi.Output[str]:
        """
        Type of the data transfer.
        """
        return pulumi.get(self, "transfer_type")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the object.
        """
        return pulumi.get(self, "type")

