# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetBackupResult',
    'AwaitableGetBackupResult',
    'get_backup',
    'get_backup_output',
]

@pulumi.output_type
class GetBackupResult:
    """
    Backup of a Volume
    """
    def __init__(__self__, backup_id=None, backup_type=None, creation_date=None, failure_reason=None, id=None, label=None, location=None, name=None, provisioning_state=None, size=None, type=None, use_existing_snapshot=None, volume_name=None):
        if backup_id and not isinstance(backup_id, str):
            raise TypeError("Expected argument 'backup_id' to be a str")
        pulumi.set(__self__, "backup_id", backup_id)
        if backup_type and not isinstance(backup_type, str):
            raise TypeError("Expected argument 'backup_type' to be a str")
        pulumi.set(__self__, "backup_type", backup_type)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if failure_reason and not isinstance(failure_reason, str):
            raise TypeError("Expected argument 'failure_reason' to be a str")
        pulumi.set(__self__, "failure_reason", failure_reason)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if label and not isinstance(label, str):
            raise TypeError("Expected argument 'label' to be a str")
        pulumi.set(__self__, "label", label)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if size and not isinstance(size, float):
            raise TypeError("Expected argument 'size' to be a float")
        pulumi.set(__self__, "size", size)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if use_existing_snapshot and not isinstance(use_existing_snapshot, bool):
            raise TypeError("Expected argument 'use_existing_snapshot' to be a bool")
        pulumi.set(__self__, "use_existing_snapshot", use_existing_snapshot)
        if volume_name and not isinstance(volume_name, str):
            raise TypeError("Expected argument 'volume_name' to be a str")
        pulumi.set(__self__, "volume_name", volume_name)

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> str:
        """
        UUID v4 used to identify the Backup
        """
        return pulumi.get(self, "backup_id")

    @property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> str:
        """
        Type of backup Manual or Scheduled
        """
        return pulumi.get(self, "backup_type")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> str:
        """
        The creation date of the backup
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> str:
        """
        Failure reason
        """
        return pulumi.get(self, "failure_reason")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def label(self) -> Optional[str]:
        """
        Label for backup
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Azure lifecycle management
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def size(self) -> float:
        """
        Size of backup
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="useExistingSnapshot")
    def use_existing_snapshot(self) -> Optional[bool]:
        """
        Manual backup an already existing snapshot. This will always be false for scheduled backups and true/false for manual backups
        """
        return pulumi.get(self, "use_existing_snapshot")

    @property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> str:
        """
        Volume name
        """
        return pulumi.get(self, "volume_name")


class AwaitableGetBackupResult(GetBackupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBackupResult(
            backup_id=self.backup_id,
            backup_type=self.backup_type,
            creation_date=self.creation_date,
            failure_reason=self.failure_reason,
            id=self.id,
            label=self.label,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            size=self.size,
            type=self.type,
            use_existing_snapshot=self.use_existing_snapshot,
            volume_name=self.volume_name)


def get_backup(account_name: Optional[str] = None,
               backup_name: Optional[str] = None,
               pool_name: Optional[str] = None,
               resource_group_name: Optional[str] = None,
               volume_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBackupResult:
    """
    Backup of a Volume


    :param str account_name: The name of the NetApp account
    :param str backup_name: The name of the backup
    :param str pool_name: The name of the capacity pool
    :param str resource_group_name: The name of the resource group.
    :param str volume_name: The name of the volume
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['backupName'] = backup_name
    __args__['poolName'] = pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['volumeName'] = volume_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:netapp/v20210601:getBackup', __args__, opts=opts, typ=GetBackupResult).value

    return AwaitableGetBackupResult(
        backup_id=__ret__.backup_id,
        backup_type=__ret__.backup_type,
        creation_date=__ret__.creation_date,
        failure_reason=__ret__.failure_reason,
        id=__ret__.id,
        label=__ret__.label,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        size=__ret__.size,
        type=__ret__.type,
        use_existing_snapshot=__ret__.use_existing_snapshot,
        volume_name=__ret__.volume_name)


@_utilities.lift_output_func(get_backup)
def get_backup_output(account_name: Optional[pulumi.Input[str]] = None,
                      backup_name: Optional[pulumi.Input[str]] = None,
                      pool_name: Optional[pulumi.Input[str]] = None,
                      resource_group_name: Optional[pulumi.Input[str]] = None,
                      volume_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBackupResult]:
    """
    Backup of a Volume


    :param str account_name: The name of the NetApp account
    :param str backup_name: The name of the backup
    :param str pool_name: The name of the capacity pool
    :param str resource_group_name: The name of the resource group.
    :param str volume_name: The name of the volume
    """
    ...
