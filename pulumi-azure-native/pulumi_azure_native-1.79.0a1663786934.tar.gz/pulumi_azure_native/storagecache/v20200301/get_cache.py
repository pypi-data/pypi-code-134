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
    'GetCacheResult',
    'AwaitableGetCacheResult',
    'get_cache',
    'get_cache_output',
]

warnings.warn("""Version 2020-03-01 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetCacheResult:
    """
    A Cache instance. Follows Azure Resource Manager standards: https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/resource-api-reference.md
    """
    def __init__(__self__, cache_size_gb=None, encryption_settings=None, health=None, id=None, identity=None, location=None, mount_addresses=None, name=None, network_settings=None, provisioning_state=None, security_settings=None, sku=None, subnet=None, system_data=None, tags=None, type=None, upgrade_status=None):
        if cache_size_gb and not isinstance(cache_size_gb, int):
            raise TypeError("Expected argument 'cache_size_gb' to be a int")
        pulumi.set(__self__, "cache_size_gb", cache_size_gb)
        if encryption_settings and not isinstance(encryption_settings, dict):
            raise TypeError("Expected argument 'encryption_settings' to be a dict")
        pulumi.set(__self__, "encryption_settings", encryption_settings)
        if health and not isinstance(health, dict):
            raise TypeError("Expected argument 'health' to be a dict")
        pulumi.set(__self__, "health", health)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mount_addresses and not isinstance(mount_addresses, list):
            raise TypeError("Expected argument 'mount_addresses' to be a list")
        pulumi.set(__self__, "mount_addresses", mount_addresses)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_settings and not isinstance(network_settings, dict):
            raise TypeError("Expected argument 'network_settings' to be a dict")
        pulumi.set(__self__, "network_settings", network_settings)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if security_settings and not isinstance(security_settings, dict):
            raise TypeError("Expected argument 'security_settings' to be a dict")
        pulumi.set(__self__, "security_settings", security_settings)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if subnet and not isinstance(subnet, str):
            raise TypeError("Expected argument 'subnet' to be a str")
        pulumi.set(__self__, "subnet", subnet)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if upgrade_status and not isinstance(upgrade_status, dict):
            raise TypeError("Expected argument 'upgrade_status' to be a dict")
        pulumi.set(__self__, "upgrade_status", upgrade_status)

    @property
    @pulumi.getter(name="cacheSizeGB")
    def cache_size_gb(self) -> Optional[int]:
        """
        The size of this Cache, in GB.
        """
        return pulumi.get(self, "cache_size_gb")

    @property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> Optional['outputs.CacheEncryptionSettingsResponse']:
        """
        Specifies encryption settings of the cache.
        """
        return pulumi.get(self, "encryption_settings")

    @property
    @pulumi.getter
    def health(self) -> 'outputs.CacheHealthResponse':
        """
        Health of the Cache.
        """
        return pulumi.get(self, "health")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID of the Cache.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.CacheIdentityResponse']:
        """
        The identity of the cache, if configured.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Region name string.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mountAddresses")
    def mount_addresses(self) -> Sequence[str]:
        """
        Array of IP addresses that can be used by clients mounting this Cache.
        """
        return pulumi.get(self, "mount_addresses")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of Cache.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkSettings")
    def network_settings(self) -> Optional['outputs.CacheNetworkSettingsResponse']:
        """
        Specifies network settings of the cache.
        """
        return pulumi.get(self, "network_settings")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> Optional['outputs.CacheSecuritySettingsResponse']:
        """
        Specifies security settings of the cache.
        """
        return pulumi.get(self, "security_settings")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.CacheResponseSku']:
        """
        SKU for the Cache.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def subnet(self) -> Optional[str]:
        """
        Subnet used for the Cache.
        """
        return pulumi.get(self, "subnet")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        ARM tags as name/value pairs.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the Cache; Microsoft.StorageCache/Cache
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="upgradeStatus")
    def upgrade_status(self) -> Optional['outputs.CacheUpgradeStatusResponse']:
        """
        Upgrade status of the Cache.
        """
        return pulumi.get(self, "upgrade_status")


class AwaitableGetCacheResult(GetCacheResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCacheResult(
            cache_size_gb=self.cache_size_gb,
            encryption_settings=self.encryption_settings,
            health=self.health,
            id=self.id,
            identity=self.identity,
            location=self.location,
            mount_addresses=self.mount_addresses,
            name=self.name,
            network_settings=self.network_settings,
            provisioning_state=self.provisioning_state,
            security_settings=self.security_settings,
            sku=self.sku,
            subnet=self.subnet,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            upgrade_status=self.upgrade_status)


def get_cache(cache_name: Optional[str] = None,
              resource_group_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCacheResult:
    """
    A Cache instance. Follows Azure Resource Manager standards: https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/resource-api-reference.md


    :param str cache_name: Name of Cache. Length of name must be not greater than 80 and chars must be in list of [-0-9a-zA-Z_] char class.
    :param str resource_group_name: Target resource group.
    """
    pulumi.log.warn("""get_cache is deprecated: Version 2020-03-01 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['cacheName'] = cache_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storagecache/v20200301:getCache', __args__, opts=opts, typ=GetCacheResult).value

    return AwaitableGetCacheResult(
        cache_size_gb=__ret__.cache_size_gb,
        encryption_settings=__ret__.encryption_settings,
        health=__ret__.health,
        id=__ret__.id,
        identity=__ret__.identity,
        location=__ret__.location,
        mount_addresses=__ret__.mount_addresses,
        name=__ret__.name,
        network_settings=__ret__.network_settings,
        provisioning_state=__ret__.provisioning_state,
        security_settings=__ret__.security_settings,
        sku=__ret__.sku,
        subnet=__ret__.subnet,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type,
        upgrade_status=__ret__.upgrade_status)


@_utilities.lift_output_func(get_cache)
def get_cache_output(cache_name: Optional[pulumi.Input[str]] = None,
                     resource_group_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCacheResult]:
    """
    A Cache instance. Follows Azure Resource Manager standards: https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/resource-api-reference.md


    :param str cache_name: Name of Cache. Length of name must be not greater than 80 and chars must be in list of [-0-9a-zA-Z_] char class.
    :param str resource_group_name: Target resource group.
    """
    pulumi.log.warn("""get_cache is deprecated: Version 2020-03-01 will be removed in v2 of the provider.""")
    ...
