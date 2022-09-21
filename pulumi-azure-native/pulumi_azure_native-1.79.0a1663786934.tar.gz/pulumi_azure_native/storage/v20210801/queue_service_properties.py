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

__all__ = ['QueueServicePropertiesArgs', 'QueueServiceProperties']

@pulumi.input_type
class QueueServicePropertiesArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 cors: Optional[pulumi.Input['CorsRulesArgs']] = None,
                 queue_service_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a QueueServiceProperties resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input['CorsRulesArgs'] cors: Specifies CORS rules for the Queue service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the Queue service.
        :param pulumi.Input[str] queue_service_name: The name of the Queue Service within the specified storage account. Queue Service Name must be 'default'
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if cors is not None:
            pulumi.set(__self__, "cors", cors)
        if queue_service_name is not None:
            pulumi.set(__self__, "queue_service_name", queue_service_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def cors(self) -> Optional[pulumi.Input['CorsRulesArgs']]:
        """
        Specifies CORS rules for the Queue service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the Queue service.
        """
        return pulumi.get(self, "cors")

    @cors.setter
    def cors(self, value: Optional[pulumi.Input['CorsRulesArgs']]):
        pulumi.set(self, "cors", value)

    @property
    @pulumi.getter(name="queueServiceName")
    def queue_service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Queue Service within the specified storage account. Queue Service Name must be 'default'
        """
        return pulumi.get(self, "queue_service_name")

    @queue_service_name.setter
    def queue_service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "queue_service_name", value)


class QueueServiceProperties(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 cors: Optional[pulumi.Input[pulumi.InputType['CorsRulesArgs']]] = None,
                 queue_service_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The properties of a storage account’s Queue service.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[pulumi.InputType['CorsRulesArgs']] cors: Specifies CORS rules for the Queue service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the Queue service.
        :param pulumi.Input[str] queue_service_name: The name of the Queue Service within the specified storage account. Queue Service Name must be 'default'
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: QueueServicePropertiesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The properties of a storage account’s Queue service.

        :param str resource_name: The name of the resource.
        :param QueueServicePropertiesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(QueueServicePropertiesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 cors: Optional[pulumi.Input[pulumi.InputType['CorsRulesArgs']]] = None,
                 queue_service_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = QueueServicePropertiesArgs.__new__(QueueServicePropertiesArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["cors"] = cors
            __props__.__dict__["queue_service_name"] = queue_service_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storage:QueueServiceProperties"), pulumi.Alias(type_="azure-native:storage/v20190601:QueueServiceProperties"), pulumi.Alias(type_="azure-native:storage/v20200801preview:QueueServiceProperties"), pulumi.Alias(type_="azure-native:storage/v20210101:QueueServiceProperties"), pulumi.Alias(type_="azure-native:storage/v20210201:QueueServiceProperties"), pulumi.Alias(type_="azure-native:storage/v20210401:QueueServiceProperties"), pulumi.Alias(type_="azure-native:storage/v20210601:QueueServiceProperties"), pulumi.Alias(type_="azure-native:storage/v20210901:QueueServiceProperties"), pulumi.Alias(type_="azure-native:storage/v20220501:QueueServiceProperties")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(QueueServiceProperties, __self__).__init__(
            'azure-native:storage/v20210801:QueueServiceProperties',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'QueueServiceProperties':
        """
        Get an existing QueueServiceProperties resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = QueueServicePropertiesArgs.__new__(QueueServicePropertiesArgs)

        __props__.__dict__["cors"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return QueueServiceProperties(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cors(self) -> pulumi.Output[Optional['outputs.CorsRulesResponse']]:
        """
        Specifies CORS rules for the Queue service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the Queue service.
        """
        return pulumi.get(self, "cors")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

