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

__all__ = ['VolumeArgs', 'Volume']

@pulumi.input_type
class VolumeArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 creation_token: pulumi.Input[str],
                 pool_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 subnet_id: pulumi.Input[str],
                 usage_threshold: pulumi.Input[float],
                 backup_id: Optional[pulumi.Input[str]] = None,
                 data_protection: Optional[pulumi.Input['VolumePropertiesDataProtectionArgs']] = None,
                 export_policy: Optional[pulumi.Input['VolumePropertiesExportPolicyArgs']] = None,
                 is_restoring: Optional[pulumi.Input[bool]] = None,
                 kerberos_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 protocol_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 security_style: Optional[pulumi.Input[Union[str, 'SecurityStyle']]] = None,
                 service_level: Optional[pulumi.Input[Union[str, 'ServiceLevel']]] = None,
                 snapshot_directory_visible: Optional[pulumi.Input[bool]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 throughput_mibps: Optional[pulumi.Input[float]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 volume_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Volume resource.
        :param pulumi.Input[str] account_name: The name of the NetApp account
        :param pulumi.Input[str] creation_token: A unique file path for the volume. Used when creating mount targets
        :param pulumi.Input[str] pool_name: The name of the capacity pool
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] subnet_id: The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes
        :param pulumi.Input[float] usage_threshold: Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB. Specified in bytes.
        :param pulumi.Input[str] backup_id: UUID v4 or resource identifier used to identify the Backup.
        :param pulumi.Input['VolumePropertiesDataProtectionArgs'] data_protection: DataProtection type volumes include an object containing details of the replication
        :param pulumi.Input['VolumePropertiesExportPolicyArgs'] export_policy: Set of export policy rules
        :param pulumi.Input[bool] is_restoring: Restoring
        :param pulumi.Input[bool] kerberos_enabled: Describe if a volume is KerberosEnabled. To be use with swagger version 2020-05-01 or later
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Sequence[pulumi.Input[str]]] protocol_types: Set of protocol types, default NFSv3, CIFS for SMB protocol
        :param pulumi.Input[Union[str, 'SecurityStyle']] security_style: The security style of volume, default unix, ntfs for dual protocol or CIFS protocol
        :param pulumi.Input[Union[str, 'ServiceLevel']] service_level: The service level of the file system
        :param pulumi.Input[bool] snapshot_directory_visible: If enabled (true) the volume will contain a read-only .snapshot directory which provides access to each of the volume's snapshots (default to true).
        :param pulumi.Input[str] snapshot_id: UUID v4 or resource identifier used to identify the Snapshot.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] volume_name: The name of the volume
        :param pulumi.Input[str] volume_type: What type of volume is this
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "creation_token", creation_token)
        pulumi.set(__self__, "pool_name", pool_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "subnet_id", subnet_id)
        if usage_threshold is None:
            usage_threshold = 107374182400
        pulumi.set(__self__, "usage_threshold", usage_threshold)
        if backup_id is not None:
            pulumi.set(__self__, "backup_id", backup_id)
        if data_protection is not None:
            pulumi.set(__self__, "data_protection", data_protection)
        if export_policy is not None:
            pulumi.set(__self__, "export_policy", export_policy)
        if is_restoring is not None:
            pulumi.set(__self__, "is_restoring", is_restoring)
        if kerberos_enabled is None:
            kerberos_enabled = False
        if kerberos_enabled is not None:
            pulumi.set(__self__, "kerberos_enabled", kerberos_enabled)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if protocol_types is not None:
            pulumi.set(__self__, "protocol_types", protocol_types)
        if security_style is None:
            security_style = 'unix'
        if security_style is not None:
            pulumi.set(__self__, "security_style", security_style)
        if service_level is None:
            service_level = 'Premium'
        if service_level is not None:
            pulumi.set(__self__, "service_level", service_level)
        if snapshot_directory_visible is None:
            snapshot_directory_visible = True
        if snapshot_directory_visible is not None:
            pulumi.set(__self__, "snapshot_directory_visible", snapshot_directory_visible)
        if snapshot_id is not None:
            pulumi.set(__self__, "snapshot_id", snapshot_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if throughput_mibps is None:
            throughput_mibps = 0
        if throughput_mibps is not None:
            pulumi.set(__self__, "throughput_mibps", throughput_mibps)
        if volume_name is not None:
            pulumi.set(__self__, "volume_name", volume_name)
        if volume_type is not None:
            pulumi.set(__self__, "volume_type", volume_type)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the NetApp account
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="creationToken")
    def creation_token(self) -> pulumi.Input[str]:
        """
        A unique file path for the volume. Used when creating mount targets
        """
        return pulumi.get(self, "creation_token")

    @creation_token.setter
    def creation_token(self, value: pulumi.Input[str]):
        pulumi.set(self, "creation_token", value)

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> pulumi.Input[str]:
        """
        The name of the capacity pool
        """
        return pulumi.get(self, "pool_name")

    @pool_name.setter
    def pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "pool_name", value)

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
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="usageThreshold")
    def usage_threshold(self) -> pulumi.Input[float]:
        """
        Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB. Specified in bytes.
        """
        return pulumi.get(self, "usage_threshold")

    @usage_threshold.setter
    def usage_threshold(self, value: pulumi.Input[float]):
        pulumi.set(self, "usage_threshold", value)

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> Optional[pulumi.Input[str]]:
        """
        UUID v4 or resource identifier used to identify the Backup.
        """
        return pulumi.get(self, "backup_id")

    @backup_id.setter
    def backup_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backup_id", value)

    @property
    @pulumi.getter(name="dataProtection")
    def data_protection(self) -> Optional[pulumi.Input['VolumePropertiesDataProtectionArgs']]:
        """
        DataProtection type volumes include an object containing details of the replication
        """
        return pulumi.get(self, "data_protection")

    @data_protection.setter
    def data_protection(self, value: Optional[pulumi.Input['VolumePropertiesDataProtectionArgs']]):
        pulumi.set(self, "data_protection", value)

    @property
    @pulumi.getter(name="exportPolicy")
    def export_policy(self) -> Optional[pulumi.Input['VolumePropertiesExportPolicyArgs']]:
        """
        Set of export policy rules
        """
        return pulumi.get(self, "export_policy")

    @export_policy.setter
    def export_policy(self, value: Optional[pulumi.Input['VolumePropertiesExportPolicyArgs']]):
        pulumi.set(self, "export_policy", value)

    @property
    @pulumi.getter(name="isRestoring")
    def is_restoring(self) -> Optional[pulumi.Input[bool]]:
        """
        Restoring
        """
        return pulumi.get(self, "is_restoring")

    @is_restoring.setter
    def is_restoring(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_restoring", value)

    @property
    @pulumi.getter(name="kerberosEnabled")
    def kerberos_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Describe if a volume is KerberosEnabled. To be use with swagger version 2020-05-01 or later
        """
        return pulumi.get(self, "kerberos_enabled")

    @kerberos_enabled.setter
    def kerberos_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "kerberos_enabled", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="protocolTypes")
    def protocol_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Set of protocol types, default NFSv3, CIFS for SMB protocol
        """
        return pulumi.get(self, "protocol_types")

    @protocol_types.setter
    def protocol_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "protocol_types", value)

    @property
    @pulumi.getter(name="securityStyle")
    def security_style(self) -> Optional[pulumi.Input[Union[str, 'SecurityStyle']]]:
        """
        The security style of volume, default unix, ntfs for dual protocol or CIFS protocol
        """
        return pulumi.get(self, "security_style")

    @security_style.setter
    def security_style(self, value: Optional[pulumi.Input[Union[str, 'SecurityStyle']]]):
        pulumi.set(self, "security_style", value)

    @property
    @pulumi.getter(name="serviceLevel")
    def service_level(self) -> Optional[pulumi.Input[Union[str, 'ServiceLevel']]]:
        """
        The service level of the file system
        """
        return pulumi.get(self, "service_level")

    @service_level.setter
    def service_level(self, value: Optional[pulumi.Input[Union[str, 'ServiceLevel']]]):
        pulumi.set(self, "service_level", value)

    @property
    @pulumi.getter(name="snapshotDirectoryVisible")
    def snapshot_directory_visible(self) -> Optional[pulumi.Input[bool]]:
        """
        If enabled (true) the volume will contain a read-only .snapshot directory which provides access to each of the volume's snapshots (default to true).
        """
        return pulumi.get(self, "snapshot_directory_visible")

    @snapshot_directory_visible.setter
    def snapshot_directory_visible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "snapshot_directory_visible", value)

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[str]]:
        """
        UUID v4 or resource identifier used to identify the Snapshot.
        """
        return pulumi.get(self, "snapshot_id")

    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snapshot_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="throughputMibps")
    def throughput_mibps(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "throughput_mibps")

    @throughput_mibps.setter
    def throughput_mibps(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "throughput_mibps", value)

    @property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the volume
        """
        return pulumi.get(self, "volume_name")

    @volume_name.setter
    def volume_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_name", value)

    @property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[str]]:
        """
        What type of volume is this
        """
        return pulumi.get(self, "volume_type")

    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_type", value)


warnings.warn("""Version 2020-08-01 will be removed in v2 of the provider.""", DeprecationWarning)


class Volume(pulumi.CustomResource):
    warnings.warn("""Version 2020-08-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 backup_id: Optional[pulumi.Input[str]] = None,
                 creation_token: Optional[pulumi.Input[str]] = None,
                 data_protection: Optional[pulumi.Input[pulumi.InputType['VolumePropertiesDataProtectionArgs']]] = None,
                 export_policy: Optional[pulumi.Input[pulumi.InputType['VolumePropertiesExportPolicyArgs']]] = None,
                 is_restoring: Optional[pulumi.Input[bool]] = None,
                 kerberos_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 protocol_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_style: Optional[pulumi.Input[Union[str, 'SecurityStyle']]] = None,
                 service_level: Optional[pulumi.Input[Union[str, 'ServiceLevel']]] = None,
                 snapshot_directory_visible: Optional[pulumi.Input[bool]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 throughput_mibps: Optional[pulumi.Input[float]] = None,
                 usage_threshold: Optional[pulumi.Input[float]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 volume_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Volume resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the NetApp account
        :param pulumi.Input[str] backup_id: UUID v4 or resource identifier used to identify the Backup.
        :param pulumi.Input[str] creation_token: A unique file path for the volume. Used when creating mount targets
        :param pulumi.Input[pulumi.InputType['VolumePropertiesDataProtectionArgs']] data_protection: DataProtection type volumes include an object containing details of the replication
        :param pulumi.Input[pulumi.InputType['VolumePropertiesExportPolicyArgs']] export_policy: Set of export policy rules
        :param pulumi.Input[bool] is_restoring: Restoring
        :param pulumi.Input[bool] kerberos_enabled: Describe if a volume is KerberosEnabled. To be use with swagger version 2020-05-01 or later
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] pool_name: The name of the capacity pool
        :param pulumi.Input[Sequence[pulumi.Input[str]]] protocol_types: Set of protocol types, default NFSv3, CIFS for SMB protocol
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Union[str, 'SecurityStyle']] security_style: The security style of volume, default unix, ntfs for dual protocol or CIFS protocol
        :param pulumi.Input[Union[str, 'ServiceLevel']] service_level: The service level of the file system
        :param pulumi.Input[bool] snapshot_directory_visible: If enabled (true) the volume will contain a read-only .snapshot directory which provides access to each of the volume's snapshots (default to true).
        :param pulumi.Input[str] snapshot_id: UUID v4 or resource identifier used to identify the Snapshot.
        :param pulumi.Input[str] subnet_id: The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[float] usage_threshold: Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB. Specified in bytes.
        :param pulumi.Input[str] volume_name: The name of the volume
        :param pulumi.Input[str] volume_type: What type of volume is this
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Volume resource

        :param str resource_name: The name of the resource.
        :param VolumeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 backup_id: Optional[pulumi.Input[str]] = None,
                 creation_token: Optional[pulumi.Input[str]] = None,
                 data_protection: Optional[pulumi.Input[pulumi.InputType['VolumePropertiesDataProtectionArgs']]] = None,
                 export_policy: Optional[pulumi.Input[pulumi.InputType['VolumePropertiesExportPolicyArgs']]] = None,
                 is_restoring: Optional[pulumi.Input[bool]] = None,
                 kerberos_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 protocol_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_style: Optional[pulumi.Input[Union[str, 'SecurityStyle']]] = None,
                 service_level: Optional[pulumi.Input[Union[str, 'ServiceLevel']]] = None,
                 snapshot_directory_visible: Optional[pulumi.Input[bool]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 throughput_mibps: Optional[pulumi.Input[float]] = None,
                 usage_threshold: Optional[pulumi.Input[float]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 volume_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Volume is deprecated: Version 2020-08-01 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeArgs.__new__(VolumeArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["backup_id"] = backup_id
            if creation_token is None and not opts.urn:
                raise TypeError("Missing required property 'creation_token'")
            __props__.__dict__["creation_token"] = creation_token
            __props__.__dict__["data_protection"] = data_protection
            __props__.__dict__["export_policy"] = export_policy
            __props__.__dict__["is_restoring"] = is_restoring
            if kerberos_enabled is None:
                kerberos_enabled = False
            __props__.__dict__["kerberos_enabled"] = kerberos_enabled
            __props__.__dict__["location"] = location
            if pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'pool_name'")
            __props__.__dict__["pool_name"] = pool_name
            __props__.__dict__["protocol_types"] = protocol_types
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if security_style is None:
                security_style = 'unix'
            __props__.__dict__["security_style"] = security_style
            if service_level is None:
                service_level = 'Premium'
            __props__.__dict__["service_level"] = service_level
            if snapshot_directory_visible is None:
                snapshot_directory_visible = True
            __props__.__dict__["snapshot_directory_visible"] = snapshot_directory_visible
            __props__.__dict__["snapshot_id"] = snapshot_id
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__.__dict__["subnet_id"] = subnet_id
            __props__.__dict__["tags"] = tags
            if throughput_mibps is None:
                throughput_mibps = 0
            __props__.__dict__["throughput_mibps"] = throughput_mibps
            if usage_threshold is None:
                usage_threshold = 107374182400
            if usage_threshold is None and not opts.urn:
                raise TypeError("Missing required property 'usage_threshold'")
            __props__.__dict__["usage_threshold"] = usage_threshold
            __props__.__dict__["volume_name"] = volume_name
            __props__.__dict__["volume_type"] = volume_type
            __props__.__dict__["baremetal_tenant_id"] = None
            __props__.__dict__["file_system_id"] = None
            __props__.__dict__["mount_targets"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:netapp:Volume"), pulumi.Alias(type_="azure-native:netapp/v20170815:Volume"), pulumi.Alias(type_="azure-native:netapp/v20190501:Volume"), pulumi.Alias(type_="azure-native:netapp/v20190601:Volume"), pulumi.Alias(type_="azure-native:netapp/v20190701:Volume"), pulumi.Alias(type_="azure-native:netapp/v20190801:Volume"), pulumi.Alias(type_="azure-native:netapp/v20191001:Volume"), pulumi.Alias(type_="azure-native:netapp/v20191101:Volume"), pulumi.Alias(type_="azure-native:netapp/v20200201:Volume"), pulumi.Alias(type_="azure-native:netapp/v20200301:Volume"), pulumi.Alias(type_="azure-native:netapp/v20200501:Volume"), pulumi.Alias(type_="azure-native:netapp/v20200601:Volume"), pulumi.Alias(type_="azure-native:netapp/v20200701:Volume"), pulumi.Alias(type_="azure-native:netapp/v20200901:Volume"), pulumi.Alias(type_="azure-native:netapp/v20201101:Volume"), pulumi.Alias(type_="azure-native:netapp/v20201201:Volume"), pulumi.Alias(type_="azure-native:netapp/v20210201:Volume"), pulumi.Alias(type_="azure-native:netapp/v20210401:Volume"), pulumi.Alias(type_="azure-native:netapp/v20210401preview:Volume"), pulumi.Alias(type_="azure-native:netapp/v20210601:Volume"), pulumi.Alias(type_="azure-native:netapp/v20210801:Volume"), pulumi.Alias(type_="azure-native:netapp/v20211001:Volume"), pulumi.Alias(type_="azure-native:netapp/v20220101:Volume"), pulumi.Alias(type_="azure-native:netapp/v20220301:Volume"), pulumi.Alias(type_="azure-native:netapp/v20220501:Volume")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Volume, __self__).__init__(
            'azure-native:netapp/v20200801:Volume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Volume':
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VolumeArgs.__new__(VolumeArgs)

        __props__.__dict__["backup_id"] = None
        __props__.__dict__["baremetal_tenant_id"] = None
        __props__.__dict__["creation_token"] = None
        __props__.__dict__["data_protection"] = None
        __props__.__dict__["export_policy"] = None
        __props__.__dict__["file_system_id"] = None
        __props__.__dict__["is_restoring"] = None
        __props__.__dict__["kerberos_enabled"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mount_targets"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["protocol_types"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["security_style"] = None
        __props__.__dict__["service_level"] = None
        __props__.__dict__["snapshot_directory_visible"] = None
        __props__.__dict__["snapshot_id"] = None
        __props__.__dict__["subnet_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["throughput_mibps"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["usage_threshold"] = None
        __props__.__dict__["volume_type"] = None
        return Volume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> pulumi.Output[Optional[str]]:
        """
        UUID v4 or resource identifier used to identify the Backup.
        """
        return pulumi.get(self, "backup_id")

    @property
    @pulumi.getter(name="baremetalTenantId")
    def baremetal_tenant_id(self) -> pulumi.Output[str]:
        """
        Unique Baremetal Tenant Identifier.
        """
        return pulumi.get(self, "baremetal_tenant_id")

    @property
    @pulumi.getter(name="creationToken")
    def creation_token(self) -> pulumi.Output[str]:
        """
        A unique file path for the volume. Used when creating mount targets
        """
        return pulumi.get(self, "creation_token")

    @property
    @pulumi.getter(name="dataProtection")
    def data_protection(self) -> pulumi.Output[Optional['outputs.VolumePropertiesResponseDataProtection']]:
        """
        DataProtection type volumes include an object containing details of the replication
        """
        return pulumi.get(self, "data_protection")

    @property
    @pulumi.getter(name="exportPolicy")
    def export_policy(self) -> pulumi.Output[Optional['outputs.VolumePropertiesResponseExportPolicy']]:
        """
        Set of export policy rules
        """
        return pulumi.get(self, "export_policy")

    @property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Output[str]:
        """
        Unique FileSystem Identifier.
        """
        return pulumi.get(self, "file_system_id")

    @property
    @pulumi.getter(name="isRestoring")
    def is_restoring(self) -> pulumi.Output[Optional[bool]]:
        """
        Restoring
        """
        return pulumi.get(self, "is_restoring")

    @property
    @pulumi.getter(name="kerberosEnabled")
    def kerberos_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Describe if a volume is KerberosEnabled. To be use with swagger version 2020-05-01 or later
        """
        return pulumi.get(self, "kerberos_enabled")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mountTargets")
    def mount_targets(self) -> pulumi.Output[Sequence['outputs.MountTargetPropertiesResponse']]:
        """
        List of mount targets
        """
        return pulumi.get(self, "mount_targets")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="protocolTypes")
    def protocol_types(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Set of protocol types, default NFSv3, CIFS for SMB protocol
        """
        return pulumi.get(self, "protocol_types")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Azure lifecycle management
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="securityStyle")
    def security_style(self) -> pulumi.Output[Optional[str]]:
        """
        The security style of volume, default unix, ntfs for dual protocol or CIFS protocol
        """
        return pulumi.get(self, "security_style")

    @property
    @pulumi.getter(name="serviceLevel")
    def service_level(self) -> pulumi.Output[Optional[str]]:
        """
        The service level of the file system
        """
        return pulumi.get(self, "service_level")

    @property
    @pulumi.getter(name="snapshotDirectoryVisible")
    def snapshot_directory_visible(self) -> pulumi.Output[Optional[bool]]:
        """
        If enabled (true) the volume will contain a read-only .snapshot directory which provides access to each of the volume's snapshots (default to true).
        """
        return pulumi.get(self, "snapshot_directory_visible")

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> pulumi.Output[Optional[str]]:
        """
        UUID v4 or resource identifier used to identify the Snapshot.
        """
        return pulumi.get(self, "snapshot_id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="throughputMibps")
    def throughput_mibps(self) -> pulumi.Output[Optional[float]]:
        return pulumi.get(self, "throughput_mibps")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="usageThreshold")
    def usage_threshold(self) -> pulumi.Output[float]:
        """
        Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB. Specified in bytes.
        """
        return pulumi.get(self, "usage_threshold")

    @property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> pulumi.Output[Optional[str]]:
        """
        What type of volume is this
        """
        return pulumi.get(self, "volume_type")

