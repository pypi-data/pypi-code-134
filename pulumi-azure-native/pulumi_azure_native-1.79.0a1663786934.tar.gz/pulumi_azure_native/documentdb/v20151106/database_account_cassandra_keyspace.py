# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._inputs import *

__all__ = ['DatabaseAccountCassandraKeyspaceArgs', 'DatabaseAccountCassandraKeyspace']

@pulumi.input_type
class DatabaseAccountCassandraKeyspaceArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 options: pulumi.Input[Mapping[str, pulumi.Input[str]]],
                 resource: pulumi.Input['CassandraKeyspaceResourceArgs'],
                 resource_group_name: pulumi.Input[str],
                 keyspace_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DatabaseAccountCassandraKeyspace resource.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] options: A key-value pair of options to be applied for the request. This corresponds to the headers sent with the request.
        :param pulumi.Input['CassandraKeyspaceResourceArgs'] resource: The standard JSON format of a Cassandra keyspace
        :param pulumi.Input[str] resource_group_name: Name of an Azure resource group.
        :param pulumi.Input[str] keyspace_name: Cosmos DB keyspace name.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "options", options)
        pulumi.set(__self__, "resource", resource)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if keyspace_name is not None:
            pulumi.set(__self__, "keyspace_name", keyspace_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        Cosmos DB database account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def options(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        """
        A key-value pair of options to be applied for the request. This corresponds to the headers sent with the request.
        """
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Input['CassandraKeyspaceResourceArgs']:
        """
        The standard JSON format of a Cassandra keyspace
        """
        return pulumi.get(self, "resource")

    @resource.setter
    def resource(self, value: pulumi.Input['CassandraKeyspaceResourceArgs']):
        pulumi.set(self, "resource", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of an Azure resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="keyspaceName")
    def keyspace_name(self) -> Optional[pulumi.Input[str]]:
        """
        Cosmos DB keyspace name.
        """
        return pulumi.get(self, "keyspace_name")

    @keyspace_name.setter
    def keyspace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "keyspace_name", value)


warnings.warn("""Version 2015-11-06 will be removed in v2 of the provider.""", DeprecationWarning)


class DatabaseAccountCassandraKeyspace(pulumi.CustomResource):
    warnings.warn("""Version 2015-11-06 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 keyspace_name: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource: Optional[pulumi.Input[pulumi.InputType['CassandraKeyspaceResourceArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An Azure Cosmos DB Cassandra keyspace.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input[str] keyspace_name: Cosmos DB keyspace name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] options: A key-value pair of options to be applied for the request. This corresponds to the headers sent with the request.
        :param pulumi.Input[pulumi.InputType['CassandraKeyspaceResourceArgs']] resource: The standard JSON format of a Cassandra keyspace
        :param pulumi.Input[str] resource_group_name: Name of an Azure resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatabaseAccountCassandraKeyspaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure Cosmos DB Cassandra keyspace.

        :param str resource_name: The name of the resource.
        :param DatabaseAccountCassandraKeyspaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatabaseAccountCassandraKeyspaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 keyspace_name: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource: Optional[pulumi.Input[pulumi.InputType['CassandraKeyspaceResourceArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""DatabaseAccountCassandraKeyspace is deprecated: Version 2015-11-06 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatabaseAccountCassandraKeyspaceArgs.__new__(DatabaseAccountCassandraKeyspaceArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["keyspace_name"] = keyspace_name
            if options is None and not opts.urn:
                raise TypeError("Missing required property 'options'")
            __props__.__dict__["options"] = options
            if resource is None and not opts.urn:
                raise TypeError("Missing required property 'resource'")
            __props__.__dict__["resource"] = resource
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["tags"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:documentdb:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20150401:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20150408:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20160319:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20160331:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20190801:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20191212:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20200301:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20200401:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20200601preview:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20200901:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20210115:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20210301preview:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20210315:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20210401preview:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20210415:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20210515:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20210615:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20210701preview:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20211015:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20211015preview:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20211115preview:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20220215preview:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20220515:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20220515preview:DatabaseAccountCassandraKeyspace"), pulumi.Alias(type_="azure-native:documentdb/v20220815:DatabaseAccountCassandraKeyspace")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DatabaseAccountCassandraKeyspace, __self__).__init__(
            'azure-native:documentdb/v20151106:DatabaseAccountCassandraKeyspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DatabaseAccountCassandraKeyspace':
        """
        Get an existing DatabaseAccountCassandraKeyspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DatabaseAccountCassandraKeyspaceArgs.__new__(DatabaseAccountCassandraKeyspaceArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return DatabaseAccountCassandraKeyspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the database account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of Azure resource.
        """
        return pulumi.get(self, "type")

