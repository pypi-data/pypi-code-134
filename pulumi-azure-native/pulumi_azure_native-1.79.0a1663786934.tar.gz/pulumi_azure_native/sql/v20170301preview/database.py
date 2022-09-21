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

__all__ = ['DatabaseArgs', 'Database']

@pulumi.input_type
class DatabaseArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 catalog_collation: Optional[pulumi.Input[Union[str, 'CatalogCollationType']]] = None,
                 collation: Optional[pulumi.Input[str]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 elastic_pool_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 long_term_retention_backup_resource_id: Optional[pulumi.Input[str]] = None,
                 max_size_bytes: Optional[pulumi.Input[float]] = None,
                 recoverable_database_id: Optional[pulumi.Input[str]] = None,
                 recovery_services_recovery_point_id: Optional[pulumi.Input[str]] = None,
                 restorable_dropped_database_id: Optional[pulumi.Input[str]] = None,
                 restore_point_in_time: Optional[pulumi.Input[str]] = None,
                 sample_name: Optional[pulumi.Input[Union[str, 'SampleName']]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 source_database_deletion_date: Optional[pulumi.Input[str]] = None,
                 source_database_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Database resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[Union[str, 'CatalogCollationType']] catalog_collation: Collation of the metadata catalog.
        :param pulumi.Input[str] collation: The collation of the database.
        :param pulumi.Input[Union[str, 'CreateMode']] create_mode: Specifies the mode of database creation.
               
               Default: regular database creation.
               
               Copy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database.
               
               Secondary: creates a database as a secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database.
               
               PointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified.
               
               Recovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore.
               
               Restore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database's original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time.
               
               RestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID.
               
               Copy, Secondary, and RestoreLongTermRetentionBackup are not supported for DataWarehouse edition.
        :param pulumi.Input[str] database_name: The name of the database.
        :param pulumi.Input[str] elastic_pool_id: The resource identifier of the elastic pool containing this database.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] long_term_retention_backup_resource_id: The resource identifier of the long term retention backup associated with create operation of this database.
        :param pulumi.Input[float] max_size_bytes: The max size of the database expressed in bytes.
        :param pulumi.Input[str] recoverable_database_id: The resource identifier of the recoverable database associated with create operation of this database.
        :param pulumi.Input[str] recovery_services_recovery_point_id: The resource identifier of the recovery point associated with create operation of this database.
        :param pulumi.Input[str] restorable_dropped_database_id: The resource identifier of the restorable dropped database associated with create operation of this database.
        :param pulumi.Input[str] restore_point_in_time: Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.
        :param pulumi.Input[Union[str, 'SampleName']] sample_name: The name of the sample schema to apply when creating this database.
        :param pulumi.Input['SkuArgs'] sku: The name and tier of the SKU.
        :param pulumi.Input[str] source_database_deletion_date: Specifies the time that the database was deleted.
        :param pulumi.Input[str] source_database_id: The resource identifier of the source database associated with create operation of this database.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[bool] zone_redundant: Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        if catalog_collation is not None:
            pulumi.set(__self__, "catalog_collation", catalog_collation)
        if collation is not None:
            pulumi.set(__self__, "collation", collation)
        if create_mode is not None:
            pulumi.set(__self__, "create_mode", create_mode)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if elastic_pool_id is not None:
            pulumi.set(__self__, "elastic_pool_id", elastic_pool_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if long_term_retention_backup_resource_id is not None:
            pulumi.set(__self__, "long_term_retention_backup_resource_id", long_term_retention_backup_resource_id)
        if max_size_bytes is not None:
            pulumi.set(__self__, "max_size_bytes", max_size_bytes)
        if recoverable_database_id is not None:
            pulumi.set(__self__, "recoverable_database_id", recoverable_database_id)
        if recovery_services_recovery_point_id is not None:
            pulumi.set(__self__, "recovery_services_recovery_point_id", recovery_services_recovery_point_id)
        if restorable_dropped_database_id is not None:
            pulumi.set(__self__, "restorable_dropped_database_id", restorable_dropped_database_id)
        if restore_point_in_time is not None:
            pulumi.set(__self__, "restore_point_in_time", restore_point_in_time)
        if sample_name is not None:
            pulumi.set(__self__, "sample_name", sample_name)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if source_database_deletion_date is not None:
            pulumi.set(__self__, "source_database_deletion_date", source_database_deletion_date)
        if source_database_id is not None:
            pulumi.set(__self__, "source_database_id", source_database_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone_redundant is not None:
            pulumi.set(__self__, "zone_redundant", zone_redundant)

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
    @pulumi.getter(name="catalogCollation")
    def catalog_collation(self) -> Optional[pulumi.Input[Union[str, 'CatalogCollationType']]]:
        """
        Collation of the metadata catalog.
        """
        return pulumi.get(self, "catalog_collation")

    @catalog_collation.setter
    def catalog_collation(self, value: Optional[pulumi.Input[Union[str, 'CatalogCollationType']]]):
        pulumi.set(self, "catalog_collation", value)

    @property
    @pulumi.getter
    def collation(self) -> Optional[pulumi.Input[str]]:
        """
        The collation of the database.
        """
        return pulumi.get(self, "collation")

    @collation.setter
    def collation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "collation", value)

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[str, 'CreateMode']]]:
        """
        Specifies the mode of database creation.
        
        Default: regular database creation.
        
        Copy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database.
        
        Secondary: creates a database as a secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database.
        
        PointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified.
        
        Recovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore.
        
        Restore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database's original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time.
        
        RestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID.
        
        Copy, Secondary, and RestoreLongTermRetentionBackup are not supported for DataWarehouse edition.
        """
        return pulumi.get(self, "create_mode")

    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[str, 'CreateMode']]]):
        pulumi.set(self, "create_mode", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the database.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="elasticPoolId")
    def elastic_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource identifier of the elastic pool containing this database.
        """
        return pulumi.get(self, "elastic_pool_id")

    @elastic_pool_id.setter
    def elastic_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "elastic_pool_id", value)

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
    @pulumi.getter(name="longTermRetentionBackupResourceId")
    def long_term_retention_backup_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource identifier of the long term retention backup associated with create operation of this database.
        """
        return pulumi.get(self, "long_term_retention_backup_resource_id")

    @long_term_retention_backup_resource_id.setter
    def long_term_retention_backup_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "long_term_retention_backup_resource_id", value)

    @property
    @pulumi.getter(name="maxSizeBytes")
    def max_size_bytes(self) -> Optional[pulumi.Input[float]]:
        """
        The max size of the database expressed in bytes.
        """
        return pulumi.get(self, "max_size_bytes")

    @max_size_bytes.setter
    def max_size_bytes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "max_size_bytes", value)

    @property
    @pulumi.getter(name="recoverableDatabaseId")
    def recoverable_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource identifier of the recoverable database associated with create operation of this database.
        """
        return pulumi.get(self, "recoverable_database_id")

    @recoverable_database_id.setter
    def recoverable_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recoverable_database_id", value)

    @property
    @pulumi.getter(name="recoveryServicesRecoveryPointId")
    def recovery_services_recovery_point_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource identifier of the recovery point associated with create operation of this database.
        """
        return pulumi.get(self, "recovery_services_recovery_point_id")

    @recovery_services_recovery_point_id.setter
    def recovery_services_recovery_point_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recovery_services_recovery_point_id", value)

    @property
    @pulumi.getter(name="restorableDroppedDatabaseId")
    def restorable_dropped_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource identifier of the restorable dropped database associated with create operation of this database.
        """
        return pulumi.get(self, "restorable_dropped_database_id")

    @restorable_dropped_database_id.setter
    def restorable_dropped_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restorable_dropped_database_id", value)

    @property
    @pulumi.getter(name="restorePointInTime")
    def restore_point_in_time(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.
        """
        return pulumi.get(self, "restore_point_in_time")

    @restore_point_in_time.setter
    def restore_point_in_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restore_point_in_time", value)

    @property
    @pulumi.getter(name="sampleName")
    def sample_name(self) -> Optional[pulumi.Input[Union[str, 'SampleName']]]:
        """
        The name of the sample schema to apply when creating this database.
        """
        return pulumi.get(self, "sample_name")

    @sample_name.setter
    def sample_name(self, value: Optional[pulumi.Input[Union[str, 'SampleName']]]):
        pulumi.set(self, "sample_name", value)

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
    @pulumi.getter(name="sourceDatabaseDeletionDate")
    def source_database_deletion_date(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the time that the database was deleted.
        """
        return pulumi.get(self, "source_database_deletion_date")

    @source_database_deletion_date.setter
    def source_database_deletion_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_database_deletion_date", value)

    @property
    @pulumi.getter(name="sourceDatabaseId")
    def source_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource identifier of the source database associated with create operation of this database.
        """
        return pulumi.get(self, "source_database_id")

    @source_database_id.setter
    def source_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_database_id", value)

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

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones.
        """
        return pulumi.get(self, "zone_redundant")

    @zone_redundant.setter
    def zone_redundant(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "zone_redundant", value)


class Database(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_collation: Optional[pulumi.Input[Union[str, 'CatalogCollationType']]] = None,
                 collation: Optional[pulumi.Input[str]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 elastic_pool_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 long_term_retention_backup_resource_id: Optional[pulumi.Input[str]] = None,
                 max_size_bytes: Optional[pulumi.Input[float]] = None,
                 recoverable_database_id: Optional[pulumi.Input[str]] = None,
                 recovery_services_recovery_point_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restorable_dropped_database_id: Optional[pulumi.Input[str]] = None,
                 restore_point_in_time: Optional[pulumi.Input[str]] = None,
                 sample_name: Optional[pulumi.Input[Union[str, 'SampleName']]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 source_database_deletion_date: Optional[pulumi.Input[str]] = None,
                 source_database_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        A database resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'CatalogCollationType']] catalog_collation: Collation of the metadata catalog.
        :param pulumi.Input[str] collation: The collation of the database.
        :param pulumi.Input[Union[str, 'CreateMode']] create_mode: Specifies the mode of database creation.
               
               Default: regular database creation.
               
               Copy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database.
               
               Secondary: creates a database as a secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database.
               
               PointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified.
               
               Recovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore.
               
               Restore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database's original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time.
               
               RestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID.
               
               Copy, Secondary, and RestoreLongTermRetentionBackup are not supported for DataWarehouse edition.
        :param pulumi.Input[str] database_name: The name of the database.
        :param pulumi.Input[str] elastic_pool_id: The resource identifier of the elastic pool containing this database.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] long_term_retention_backup_resource_id: The resource identifier of the long term retention backup associated with create operation of this database.
        :param pulumi.Input[float] max_size_bytes: The max size of the database expressed in bytes.
        :param pulumi.Input[str] recoverable_database_id: The resource identifier of the recoverable database associated with create operation of this database.
        :param pulumi.Input[str] recovery_services_recovery_point_id: The resource identifier of the recovery point associated with create operation of this database.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] restorable_dropped_database_id: The resource identifier of the restorable dropped database associated with create operation of this database.
        :param pulumi.Input[str] restore_point_in_time: Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.
        :param pulumi.Input[Union[str, 'SampleName']] sample_name: The name of the sample schema to apply when creating this database.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The name and tier of the SKU.
        :param pulumi.Input[str] source_database_deletion_date: Specifies the time that the database was deleted.
        :param pulumi.Input[str] source_database_id: The resource identifier of the source database associated with create operation of this database.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[bool] zone_redundant: Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatabaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A database resource.

        :param str resource_name: The name of the resource.
        :param DatabaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatabaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_collation: Optional[pulumi.Input[Union[str, 'CatalogCollationType']]] = None,
                 collation: Optional[pulumi.Input[str]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 elastic_pool_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 long_term_retention_backup_resource_id: Optional[pulumi.Input[str]] = None,
                 max_size_bytes: Optional[pulumi.Input[float]] = None,
                 recoverable_database_id: Optional[pulumi.Input[str]] = None,
                 recovery_services_recovery_point_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restorable_dropped_database_id: Optional[pulumi.Input[str]] = None,
                 restore_point_in_time: Optional[pulumi.Input[str]] = None,
                 sample_name: Optional[pulumi.Input[Union[str, 'SampleName']]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 source_database_deletion_date: Optional[pulumi.Input[str]] = None,
                 source_database_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatabaseArgs.__new__(DatabaseArgs)

            __props__.__dict__["catalog_collation"] = catalog_collation
            __props__.__dict__["collation"] = collation
            __props__.__dict__["create_mode"] = create_mode
            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["elastic_pool_id"] = elastic_pool_id
            __props__.__dict__["location"] = location
            __props__.__dict__["long_term_retention_backup_resource_id"] = long_term_retention_backup_resource_id
            __props__.__dict__["max_size_bytes"] = max_size_bytes
            __props__.__dict__["recoverable_database_id"] = recoverable_database_id
            __props__.__dict__["recovery_services_recovery_point_id"] = recovery_services_recovery_point_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["restorable_dropped_database_id"] = restorable_dropped_database_id
            __props__.__dict__["restore_point_in_time"] = restore_point_in_time
            __props__.__dict__["sample_name"] = sample_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["source_database_deletion_date"] = source_database_deletion_date
            __props__.__dict__["source_database_id"] = source_database_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zone_redundant"] = zone_redundant
            __props__.__dict__["creation_date"] = None
            __props__.__dict__["current_service_objective_name"] = None
            __props__.__dict__["database_id"] = None
            __props__.__dict__["default_secondary_location"] = None
            __props__.__dict__["failover_group_id"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:Database"), pulumi.Alias(type_="azure-native:sql/v20140401:Database"), pulumi.Alias(type_="azure-native:sql/v20171001preview:Database"), pulumi.Alias(type_="azure-native:sql/v20190601preview:Database"), pulumi.Alias(type_="azure-native:sql/v20200202preview:Database"), pulumi.Alias(type_="azure-native:sql/v20200801preview:Database"), pulumi.Alias(type_="azure-native:sql/v20201101preview:Database"), pulumi.Alias(type_="azure-native:sql/v20210201preview:Database"), pulumi.Alias(type_="azure-native:sql/v20210501preview:Database"), pulumi.Alias(type_="azure-native:sql/v20210801preview:Database"), pulumi.Alias(type_="azure-native:sql/v20211101:Database"), pulumi.Alias(type_="azure-native:sql/v20211101preview:Database"), pulumi.Alias(type_="azure-native:sql/v20220201preview:Database")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Database, __self__).__init__(
            'azure-native:sql/v20170301preview:Database',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Database':
        """
        Get an existing Database resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DatabaseArgs.__new__(DatabaseArgs)

        __props__.__dict__["catalog_collation"] = None
        __props__.__dict__["collation"] = None
        __props__.__dict__["creation_date"] = None
        __props__.__dict__["current_service_objective_name"] = None
        __props__.__dict__["database_id"] = None
        __props__.__dict__["default_secondary_location"] = None
        __props__.__dict__["elastic_pool_id"] = None
        __props__.__dict__["failover_group_id"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["max_size_bytes"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["zone_redundant"] = None
        return Database(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="catalogCollation")
    def catalog_collation(self) -> pulumi.Output[Optional[str]]:
        """
        Collation of the metadata catalog.
        """
        return pulumi.get(self, "catalog_collation")

    @property
    @pulumi.getter
    def collation(self) -> pulumi.Output[Optional[str]]:
        """
        The collation of the database.
        """
        return pulumi.get(self, "collation")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        The creation date of the database (ISO8601 format).
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="currentServiceObjectiveName")
    def current_service_objective_name(self) -> pulumi.Output[str]:
        """
        The current service level objective name of the database.
        """
        return pulumi.get(self, "current_service_objective_name")

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> pulumi.Output[str]:
        """
        The ID of the database.
        """
        return pulumi.get(self, "database_id")

    @property
    @pulumi.getter(name="defaultSecondaryLocation")
    def default_secondary_location(self) -> pulumi.Output[str]:
        """
        The default secondary region for this database.
        """
        return pulumi.get(self, "default_secondary_location")

    @property
    @pulumi.getter(name="elasticPoolId")
    def elastic_pool_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource identifier of the elastic pool containing this database.
        """
        return pulumi.get(self, "elastic_pool_id")

    @property
    @pulumi.getter(name="failoverGroupId")
    def failover_group_id(self) -> pulumi.Output[str]:
        """
        Failover Group resource identifier that this database belongs to.
        """
        return pulumi.get(self, "failover_group_id")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind of database. This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxSizeBytes")
    def max_size_bytes(self) -> pulumi.Output[Optional[float]]:
        """
        The max size of the database expressed in bytes.
        """
        return pulumi.get(self, "max_size_bytes")

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
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the database.
        """
        return pulumi.get(self, "status")

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
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones.
        """
        return pulumi.get(self, "zone_redundant")

