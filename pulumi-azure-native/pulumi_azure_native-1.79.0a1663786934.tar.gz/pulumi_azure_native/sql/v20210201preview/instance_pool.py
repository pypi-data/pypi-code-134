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

__all__ = ['InstancePoolArgs', 'InstancePool']

@pulumi.input_type
class InstancePoolArgs:
    def __init__(__self__, *,
                 license_type: pulumi.Input[Union[str, 'InstancePoolLicenseType']],
                 resource_group_name: pulumi.Input[str],
                 subnet_id: pulumi.Input[str],
                 v_cores: pulumi.Input[int],
                 instance_pool_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a InstancePool resource.
        :param pulumi.Input[Union[str, 'InstancePoolLicenseType']] license_type: The license type. Possible values are 'LicenseIncluded' (price for SQL license is included) and 'BasePrice' (without SQL license price).
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] subnet_id: Resource ID of the subnet to place this instance pool in.
        :param pulumi.Input[int] v_cores: Count of vCores belonging to this instance pool.
        :param pulumi.Input[str] instance_pool_name: The name of the instance pool to be created or updated.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input['SkuArgs'] sku: The name and tier of the SKU.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "license_type", license_type)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "subnet_id", subnet_id)
        pulumi.set(__self__, "v_cores", v_cores)
        if instance_pool_name is not None:
            pulumi.set(__self__, "instance_pool_name", instance_pool_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Input[Union[str, 'InstancePoolLicenseType']]:
        """
        The license type. Possible values are 'LicenseIncluded' (price for SQL license is included) and 'BasePrice' (without SQL license price).
        """
        return pulumi.get(self, "license_type")

    @license_type.setter
    def license_type(self, value: pulumi.Input[Union[str, 'InstancePoolLicenseType']]):
        pulumi.set(self, "license_type", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        Resource ID of the subnet to place this instance pool in.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="vCores")
    def v_cores(self) -> pulumi.Input[int]:
        """
        Count of vCores belonging to this instance pool.
        """
        return pulumi.get(self, "v_cores")

    @v_cores.setter
    def v_cores(self, value: pulumi.Input[int]):
        pulumi.set(self, "v_cores", value)

    @property
    @pulumi.getter(name="instancePoolName")
    def instance_pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the instance pool to be created or updated.
        """
        return pulumi.get(self, "instance_pool_name")

    @instance_pool_name.setter
    def instance_pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_pool_name", value)

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
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        The name and tier of the SKU.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

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


class InstancePool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_pool_name: Optional[pulumi.Input[str]] = None,
                 license_type: Optional[pulumi.Input[Union[str, 'InstancePoolLicenseType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 v_cores: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        An Azure SQL instance pool.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_pool_name: The name of the instance pool to be created or updated.
        :param pulumi.Input[Union[str, 'InstancePoolLicenseType']] license_type: The license type. Possible values are 'LicenseIncluded' (price for SQL license is included) and 'BasePrice' (without SQL license price).
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The name and tier of the SKU.
        :param pulumi.Input[str] subnet_id: Resource ID of the subnet to place this instance pool in.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[int] v_cores: Count of vCores belonging to this instance pool.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstancePoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure SQL instance pool.

        :param str resource_name: The name of the resource.
        :param InstancePoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstancePoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_pool_name: Optional[pulumi.Input[str]] = None,
                 license_type: Optional[pulumi.Input[Union[str, 'InstancePoolLicenseType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 v_cores: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstancePoolArgs.__new__(InstancePoolArgs)

            __props__.__dict__["instance_pool_name"] = instance_pool_name
            if license_type is None and not opts.urn:
                raise TypeError("Missing required property 'license_type'")
            __props__.__dict__["license_type"] = license_type
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__.__dict__["subnet_id"] = subnet_id
            __props__.__dict__["tags"] = tags
            if v_cores is None and not opts.urn:
                raise TypeError("Missing required property 'v_cores'")
            __props__.__dict__["v_cores"] = v_cores
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:InstancePool"), pulumi.Alias(type_="azure-native:sql/v20180601preview:InstancePool"), pulumi.Alias(type_="azure-native:sql/v20200202preview:InstancePool"), pulumi.Alias(type_="azure-native:sql/v20200801preview:InstancePool"), pulumi.Alias(type_="azure-native:sql/v20201101preview:InstancePool"), pulumi.Alias(type_="azure-native:sql/v20210501preview:InstancePool"), pulumi.Alias(type_="azure-native:sql/v20210801preview:InstancePool"), pulumi.Alias(type_="azure-native:sql/v20211101:InstancePool"), pulumi.Alias(type_="azure-native:sql/v20211101preview:InstancePool"), pulumi.Alias(type_="azure-native:sql/v20220201preview:InstancePool")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(InstancePool, __self__).__init__(
            'azure-native:sql/v20210201preview:InstancePool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InstancePool':
        """
        Get an existing InstancePool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InstancePoolArgs.__new__(InstancePoolArgs)

        __props__.__dict__["license_type"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["subnet_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["v_cores"] = None
        return InstancePool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Output[str]:
        """
        The license type. Possible values are 'LicenseIncluded' (price for SQL license is included) and 'BasePrice' (without SQL license price).
        """
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The name and tier of the SKU.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        Resource ID of the subnet to place this instance pool in.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vCores")
    def v_cores(self) -> pulumi.Output[int]:
        """
        Count of vCores belonging to this instance pool.
        """
        return pulumi.get(self, "v_cores")

