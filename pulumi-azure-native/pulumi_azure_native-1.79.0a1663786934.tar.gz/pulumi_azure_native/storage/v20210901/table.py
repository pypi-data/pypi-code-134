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

__all__ = ['TableArgs', 'Table']

@pulumi.input_type
class TableArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 signed_identifiers: Optional[pulumi.Input[Sequence[pulumi.Input['TableSignedIdentifierArgs']]]] = None,
                 table_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Table resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['TableSignedIdentifierArgs']]] signed_identifiers: List of stored access policies specified on the table.
        :param pulumi.Input[str] table_name: A table name must be unique within a storage account and must be between 3 and 63 characters.The name must comprise of only alphanumeric characters and it cannot begin with a numeric character.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if signed_identifiers is not None:
            pulumi.set(__self__, "signed_identifiers", signed_identifiers)
        if table_name is not None:
            pulumi.set(__self__, "table_name", table_name)

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
    @pulumi.getter(name="signedIdentifiers")
    def signed_identifiers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableSignedIdentifierArgs']]]]:
        """
        List of stored access policies specified on the table.
        """
        return pulumi.get(self, "signed_identifiers")

    @signed_identifiers.setter
    def signed_identifiers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableSignedIdentifierArgs']]]]):
        pulumi.set(self, "signed_identifiers", value)

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[str]]:
        """
        A table name must be unique within a storage account and must be between 3 and 63 characters.The name must comprise of only alphanumeric characters and it cannot begin with a numeric character.
        """
        return pulumi.get(self, "table_name")

    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table_name", value)


class Table(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 signed_identifiers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableSignedIdentifierArgs']]]]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Properties of the table, including Id, resource name, resource type.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableSignedIdentifierArgs']]]] signed_identifiers: List of stored access policies specified on the table.
        :param pulumi.Input[str] table_name: A table name must be unique within a storage account and must be between 3 and 63 characters.The name must comprise of only alphanumeric characters and it cannot begin with a numeric character.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Properties of the table, including Id, resource name, resource type.

        :param str resource_name: The name of the resource.
        :param TableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 signed_identifiers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableSignedIdentifierArgs']]]]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TableArgs.__new__(TableArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["signed_identifiers"] = signed_identifiers
            __props__.__dict__["table_name"] = table_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storage:Table"), pulumi.Alias(type_="azure-native:storage/v20190601:Table"), pulumi.Alias(type_="azure-native:storage/v20200801preview:Table"), pulumi.Alias(type_="azure-native:storage/v20210101:Table"), pulumi.Alias(type_="azure-native:storage/v20210201:Table"), pulumi.Alias(type_="azure-native:storage/v20210401:Table"), pulumi.Alias(type_="azure-native:storage/v20210601:Table"), pulumi.Alias(type_="azure-native:storage/v20210801:Table"), pulumi.Alias(type_="azure-native:storage/v20220501:Table")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Table, __self__).__init__(
            'azure-native:storage/v20210901:Table',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Table':
        """
        Get an existing Table resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TableArgs.__new__(TableArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["signed_identifiers"] = None
        __props__.__dict__["table_name"] = None
        __props__.__dict__["type"] = None
        return Table(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="signedIdentifiers")
    def signed_identifiers(self) -> pulumi.Output[Optional[Sequence['outputs.TableSignedIdentifierResponse']]]:
        """
        List of stored access policies specified on the table.
        """
        return pulumi.get(self, "signed_identifiers")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[str]:
        """
        Table name under the specified account
        """
        return pulumi.get(self, "table_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

