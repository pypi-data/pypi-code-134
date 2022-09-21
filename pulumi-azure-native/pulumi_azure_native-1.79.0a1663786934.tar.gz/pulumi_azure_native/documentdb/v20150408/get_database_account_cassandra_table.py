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
    'GetDatabaseAccountCassandraTableResult',
    'AwaitableGetDatabaseAccountCassandraTableResult',
    'get_database_account_cassandra_table',
    'get_database_account_cassandra_table_output',
]

warnings.warn("""Version 2015-04-08 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetDatabaseAccountCassandraTableResult:
    """
    An Azure Cosmos DB Cassandra table.
    """
    def __init__(__self__, default_ttl=None, id=None, location=None, name=None, schema=None, tags=None, type=None):
        if default_ttl and not isinstance(default_ttl, int):
            raise TypeError("Expected argument 'default_ttl' to be a int")
        pulumi.set(__self__, "default_ttl", default_ttl)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if schema and not isinstance(schema, dict):
            raise TypeError("Expected argument 'schema' to be a dict")
        pulumi.set(__self__, "schema", schema)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[int]:
        """
        Time to live of the Cosmos DB Cassandra table
        """
        return pulumi.get(self, "default_ttl")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique resource identifier of the database account.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the database account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schema(self) -> Optional['outputs.CassandraSchemaResponse']:
        """
        Schema of the Cosmos DB Cassandra table
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of Azure resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetDatabaseAccountCassandraTableResult(GetDatabaseAccountCassandraTableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseAccountCassandraTableResult(
            default_ttl=self.default_ttl,
            id=self.id,
            location=self.location,
            name=self.name,
            schema=self.schema,
            tags=self.tags,
            type=self.type)


def get_database_account_cassandra_table(account_name: Optional[str] = None,
                                         keyspace_name: Optional[str] = None,
                                         resource_group_name: Optional[str] = None,
                                         table_name: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseAccountCassandraTableResult:
    """
    An Azure Cosmos DB Cassandra table.


    :param str account_name: Cosmos DB database account name.
    :param str keyspace_name: Cosmos DB keyspace name.
    :param str resource_group_name: Name of an Azure resource group.
    :param str table_name: Cosmos DB table name.
    """
    pulumi.log.warn("""get_database_account_cassandra_table is deprecated: Version 2015-04-08 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['keyspaceName'] = keyspace_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['tableName'] = table_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:documentdb/v20150408:getDatabaseAccountCassandraTable', __args__, opts=opts, typ=GetDatabaseAccountCassandraTableResult).value

    return AwaitableGetDatabaseAccountCassandraTableResult(
        default_ttl=__ret__.default_ttl,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        schema=__ret__.schema,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_database_account_cassandra_table)
def get_database_account_cassandra_table_output(account_name: Optional[pulumi.Input[str]] = None,
                                                keyspace_name: Optional[pulumi.Input[str]] = None,
                                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                                table_name: Optional[pulumi.Input[str]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseAccountCassandraTableResult]:
    """
    An Azure Cosmos DB Cassandra table.


    :param str account_name: Cosmos DB database account name.
    :param str keyspace_name: Cosmos DB keyspace name.
    :param str resource_group_name: Name of an Azure resource group.
    :param str table_name: Cosmos DB table name.
    """
    pulumi.log.warn("""get_database_account_cassandra_table is deprecated: Version 2015-04-08 will be removed in v2 of the provider.""")
    ...
