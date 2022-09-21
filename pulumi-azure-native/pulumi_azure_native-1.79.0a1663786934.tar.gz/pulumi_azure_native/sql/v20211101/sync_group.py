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

__all__ = ['SyncGroupArgs', 'SyncGroup']

@pulumi.input_type
class SyncGroupArgs:
    def __init__(__self__, *,
                 database_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 conflict_logging_retention_in_days: Optional[pulumi.Input[int]] = None,
                 conflict_resolution_policy: Optional[pulumi.Input[Union[str, 'SyncConflictResolutionPolicy']]] = None,
                 enable_conflict_logging: Optional[pulumi.Input[bool]] = None,
                 hub_database_password: Optional[pulumi.Input[str]] = None,
                 hub_database_user_name: Optional[pulumi.Input[str]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 schema: Optional[pulumi.Input['SyncGroupSchemaArgs']] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 sync_database_id: Optional[pulumi.Input[str]] = None,
                 sync_group_name: Optional[pulumi.Input[str]] = None,
                 use_private_link_connection: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a SyncGroup resource.
        :param pulumi.Input[str] database_name: The name of the database on which the sync group is hosted.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[int] conflict_logging_retention_in_days: Conflict logging retention period.
        :param pulumi.Input[Union[str, 'SyncConflictResolutionPolicy']] conflict_resolution_policy: Conflict resolution policy of the sync group.
        :param pulumi.Input[bool] enable_conflict_logging: If conflict logging is enabled.
        :param pulumi.Input[str] hub_database_password: Password for the sync group hub database credential.
        :param pulumi.Input[str] hub_database_user_name: User name for the sync group hub database credential.
        :param pulumi.Input[int] interval: Sync interval of the sync group.
        :param pulumi.Input['SyncGroupSchemaArgs'] schema: Sync schema of the sync group.
        :param pulumi.Input['SkuArgs'] sku: The name and capacity of the SKU.
        :param pulumi.Input[str] sync_database_id: ARM resource id of the sync database in the sync group.
        :param pulumi.Input[str] sync_group_name: The name of the sync group.
        :param pulumi.Input[bool] use_private_link_connection: If use private link connection is enabled.
        """
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        if conflict_logging_retention_in_days is not None:
            pulumi.set(__self__, "conflict_logging_retention_in_days", conflict_logging_retention_in_days)
        if conflict_resolution_policy is not None:
            pulumi.set(__self__, "conflict_resolution_policy", conflict_resolution_policy)
        if enable_conflict_logging is not None:
            pulumi.set(__self__, "enable_conflict_logging", enable_conflict_logging)
        if hub_database_password is not None:
            pulumi.set(__self__, "hub_database_password", hub_database_password)
        if hub_database_user_name is not None:
            pulumi.set(__self__, "hub_database_user_name", hub_database_user_name)
        if interval is not None:
            pulumi.set(__self__, "interval", interval)
        if schema is not None:
            pulumi.set(__self__, "schema", schema)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if sync_database_id is not None:
            pulumi.set(__self__, "sync_database_id", sync_database_id)
        if sync_group_name is not None:
            pulumi.set(__self__, "sync_group_name", sync_group_name)
        if use_private_link_connection is not None:
            pulumi.set(__self__, "use_private_link_connection", use_private_link_connection)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        The name of the database on which the sync group is hosted.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

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
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="conflictLoggingRetentionInDays")
    def conflict_logging_retention_in_days(self) -> Optional[pulumi.Input[int]]:
        """
        Conflict logging retention period.
        """
        return pulumi.get(self, "conflict_logging_retention_in_days")

    @conflict_logging_retention_in_days.setter
    def conflict_logging_retention_in_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "conflict_logging_retention_in_days", value)

    @property
    @pulumi.getter(name="conflictResolutionPolicy")
    def conflict_resolution_policy(self) -> Optional[pulumi.Input[Union[str, 'SyncConflictResolutionPolicy']]]:
        """
        Conflict resolution policy of the sync group.
        """
        return pulumi.get(self, "conflict_resolution_policy")

    @conflict_resolution_policy.setter
    def conflict_resolution_policy(self, value: Optional[pulumi.Input[Union[str, 'SyncConflictResolutionPolicy']]]):
        pulumi.set(self, "conflict_resolution_policy", value)

    @property
    @pulumi.getter(name="enableConflictLogging")
    def enable_conflict_logging(self) -> Optional[pulumi.Input[bool]]:
        """
        If conflict logging is enabled.
        """
        return pulumi.get(self, "enable_conflict_logging")

    @enable_conflict_logging.setter
    def enable_conflict_logging(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_conflict_logging", value)

    @property
    @pulumi.getter(name="hubDatabasePassword")
    def hub_database_password(self) -> Optional[pulumi.Input[str]]:
        """
        Password for the sync group hub database credential.
        """
        return pulumi.get(self, "hub_database_password")

    @hub_database_password.setter
    def hub_database_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hub_database_password", value)

    @property
    @pulumi.getter(name="hubDatabaseUserName")
    def hub_database_user_name(self) -> Optional[pulumi.Input[str]]:
        """
        User name for the sync group hub database credential.
        """
        return pulumi.get(self, "hub_database_user_name")

    @hub_database_user_name.setter
    def hub_database_user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hub_database_user_name", value)

    @property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[int]]:
        """
        Sync interval of the sync group.
        """
        return pulumi.get(self, "interval")

    @interval.setter
    def interval(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "interval", value)

    @property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input['SyncGroupSchemaArgs']]:
        """
        Sync schema of the sync group.
        """
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input['SyncGroupSchemaArgs']]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        The name and capacity of the SKU.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="syncDatabaseId")
    def sync_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM resource id of the sync database in the sync group.
        """
        return pulumi.get(self, "sync_database_id")

    @sync_database_id.setter
    def sync_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_database_id", value)

    @property
    @pulumi.getter(name="syncGroupName")
    def sync_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the sync group.
        """
        return pulumi.get(self, "sync_group_name")

    @sync_group_name.setter
    def sync_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_group_name", value)

    @property
    @pulumi.getter(name="usePrivateLinkConnection")
    def use_private_link_connection(self) -> Optional[pulumi.Input[bool]]:
        """
        If use private link connection is enabled.
        """
        return pulumi.get(self, "use_private_link_connection")

    @use_private_link_connection.setter
    def use_private_link_connection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_private_link_connection", value)


class SyncGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 conflict_logging_retention_in_days: Optional[pulumi.Input[int]] = None,
                 conflict_resolution_policy: Optional[pulumi.Input[Union[str, 'SyncConflictResolutionPolicy']]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 enable_conflict_logging: Optional[pulumi.Input[bool]] = None,
                 hub_database_password: Optional[pulumi.Input[str]] = None,
                 hub_database_user_name: Optional[pulumi.Input[str]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[pulumi.InputType['SyncGroupSchemaArgs']]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 sync_database_id: Optional[pulumi.Input[str]] = None,
                 sync_group_name: Optional[pulumi.Input[str]] = None,
                 use_private_link_connection: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        An Azure SQL Database sync group.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] conflict_logging_retention_in_days: Conflict logging retention period.
        :param pulumi.Input[Union[str, 'SyncConflictResolutionPolicy']] conflict_resolution_policy: Conflict resolution policy of the sync group.
        :param pulumi.Input[str] database_name: The name of the database on which the sync group is hosted.
        :param pulumi.Input[bool] enable_conflict_logging: If conflict logging is enabled.
        :param pulumi.Input[str] hub_database_password: Password for the sync group hub database credential.
        :param pulumi.Input[str] hub_database_user_name: User name for the sync group hub database credential.
        :param pulumi.Input[int] interval: Sync interval of the sync group.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[pulumi.InputType['SyncGroupSchemaArgs']] schema: Sync schema of the sync group.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The name and capacity of the SKU.
        :param pulumi.Input[str] sync_database_id: ARM resource id of the sync database in the sync group.
        :param pulumi.Input[str] sync_group_name: The name of the sync group.
        :param pulumi.Input[bool] use_private_link_connection: If use private link connection is enabled.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SyncGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure SQL Database sync group.

        :param str resource_name: The name of the resource.
        :param SyncGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SyncGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 conflict_logging_retention_in_days: Optional[pulumi.Input[int]] = None,
                 conflict_resolution_policy: Optional[pulumi.Input[Union[str, 'SyncConflictResolutionPolicy']]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 enable_conflict_logging: Optional[pulumi.Input[bool]] = None,
                 hub_database_password: Optional[pulumi.Input[str]] = None,
                 hub_database_user_name: Optional[pulumi.Input[str]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[pulumi.InputType['SyncGroupSchemaArgs']]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 sync_database_id: Optional[pulumi.Input[str]] = None,
                 sync_group_name: Optional[pulumi.Input[str]] = None,
                 use_private_link_connection: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SyncGroupArgs.__new__(SyncGroupArgs)

            __props__.__dict__["conflict_logging_retention_in_days"] = conflict_logging_retention_in_days
            __props__.__dict__["conflict_resolution_policy"] = conflict_resolution_policy
            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["enable_conflict_logging"] = enable_conflict_logging
            __props__.__dict__["hub_database_password"] = hub_database_password
            __props__.__dict__["hub_database_user_name"] = hub_database_user_name
            __props__.__dict__["interval"] = interval
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["schema"] = schema
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["sync_database_id"] = sync_database_id
            __props__.__dict__["sync_group_name"] = sync_group_name
            __props__.__dict__["use_private_link_connection"] = use_private_link_connection
            __props__.__dict__["last_sync_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint_name"] = None
            __props__.__dict__["sync_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:SyncGroup"), pulumi.Alias(type_="azure-native:sql/v20150501preview:SyncGroup"), pulumi.Alias(type_="azure-native:sql/v20190601preview:SyncGroup"), pulumi.Alias(type_="azure-native:sql/v20200202preview:SyncGroup"), pulumi.Alias(type_="azure-native:sql/v20200801preview:SyncGroup"), pulumi.Alias(type_="azure-native:sql/v20201101preview:SyncGroup"), pulumi.Alias(type_="azure-native:sql/v20210201preview:SyncGroup"), pulumi.Alias(type_="azure-native:sql/v20210501preview:SyncGroup"), pulumi.Alias(type_="azure-native:sql/v20210801preview:SyncGroup"), pulumi.Alias(type_="azure-native:sql/v20211101preview:SyncGroup"), pulumi.Alias(type_="azure-native:sql/v20220201preview:SyncGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SyncGroup, __self__).__init__(
            'azure-native:sql/v20211101:SyncGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SyncGroup':
        """
        Get an existing SyncGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SyncGroupArgs.__new__(SyncGroupArgs)

        __props__.__dict__["conflict_logging_retention_in_days"] = None
        __props__.__dict__["conflict_resolution_policy"] = None
        __props__.__dict__["enable_conflict_logging"] = None
        __props__.__dict__["hub_database_user_name"] = None
        __props__.__dict__["interval"] = None
        __props__.__dict__["last_sync_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint_name"] = None
        __props__.__dict__["schema"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["sync_database_id"] = None
        __props__.__dict__["sync_state"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["use_private_link_connection"] = None
        return SyncGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="conflictLoggingRetentionInDays")
    def conflict_logging_retention_in_days(self) -> pulumi.Output[Optional[int]]:
        """
        Conflict logging retention period.
        """
        return pulumi.get(self, "conflict_logging_retention_in_days")

    @property
    @pulumi.getter(name="conflictResolutionPolicy")
    def conflict_resolution_policy(self) -> pulumi.Output[Optional[str]]:
        """
        Conflict resolution policy of the sync group.
        """
        return pulumi.get(self, "conflict_resolution_policy")

    @property
    @pulumi.getter(name="enableConflictLogging")
    def enable_conflict_logging(self) -> pulumi.Output[Optional[bool]]:
        """
        If conflict logging is enabled.
        """
        return pulumi.get(self, "enable_conflict_logging")

    @property
    @pulumi.getter(name="hubDatabaseUserName")
    def hub_database_user_name(self) -> pulumi.Output[Optional[str]]:
        """
        User name for the sync group hub database credential.
        """
        return pulumi.get(self, "hub_database_user_name")

    @property
    @pulumi.getter
    def interval(self) -> pulumi.Output[Optional[int]]:
        """
        Sync interval of the sync group.
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter(name="lastSyncTime")
    def last_sync_time(self) -> pulumi.Output[str]:
        """
        Last sync time of the sync group.
        """
        return pulumi.get(self, "last_sync_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointName")
    def private_endpoint_name(self) -> pulumi.Output[str]:
        """
        Private endpoint name of the sync group if use private link connection is enabled.
        """
        return pulumi.get(self, "private_endpoint_name")

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Output[Optional['outputs.SyncGroupSchemaResponse']]:
        """
        Sync schema of the sync group.
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The name and capacity of the SKU.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="syncDatabaseId")
    def sync_database_id(self) -> pulumi.Output[Optional[str]]:
        """
        ARM resource id of the sync database in the sync group.
        """
        return pulumi.get(self, "sync_database_id")

    @property
    @pulumi.getter(name="syncState")
    def sync_state(self) -> pulumi.Output[str]:
        """
        Sync state of the sync group.
        """
        return pulumi.get(self, "sync_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="usePrivateLinkConnection")
    def use_private_link_connection(self) -> pulumi.Output[Optional[bool]]:
        """
        If use private link connection is enabled.
        """
        return pulumi.get(self, "use_private_link_connection")

