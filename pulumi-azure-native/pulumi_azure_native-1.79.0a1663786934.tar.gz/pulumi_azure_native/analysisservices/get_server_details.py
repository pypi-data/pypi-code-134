# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetServerDetailsResult',
    'AwaitableGetServerDetailsResult',
    'get_server_details',
    'get_server_details_output',
]

@pulumi.output_type
class GetServerDetailsResult:
    """
    Represents an instance of an Analysis Services resource.
    """
    def __init__(__self__, as_administrators=None, backup_blob_container_uri=None, gateway_details=None, id=None, ip_v4_firewall_settings=None, location=None, managed_mode=None, name=None, provisioning_state=None, querypool_connection_mode=None, server_full_name=None, server_monitor_mode=None, sku=None, state=None, tags=None, type=None):
        if as_administrators and not isinstance(as_administrators, dict):
            raise TypeError("Expected argument 'as_administrators' to be a dict")
        pulumi.set(__self__, "as_administrators", as_administrators)
        if backup_blob_container_uri and not isinstance(backup_blob_container_uri, str):
            raise TypeError("Expected argument 'backup_blob_container_uri' to be a str")
        pulumi.set(__self__, "backup_blob_container_uri", backup_blob_container_uri)
        if gateway_details and not isinstance(gateway_details, dict):
            raise TypeError("Expected argument 'gateway_details' to be a dict")
        pulumi.set(__self__, "gateway_details", gateway_details)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_v4_firewall_settings and not isinstance(ip_v4_firewall_settings, dict):
            raise TypeError("Expected argument 'ip_v4_firewall_settings' to be a dict")
        pulumi.set(__self__, "ip_v4_firewall_settings", ip_v4_firewall_settings)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_mode and not isinstance(managed_mode, int):
            raise TypeError("Expected argument 'managed_mode' to be a int")
        pulumi.set(__self__, "managed_mode", managed_mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if querypool_connection_mode and not isinstance(querypool_connection_mode, str):
            raise TypeError("Expected argument 'querypool_connection_mode' to be a str")
        pulumi.set(__self__, "querypool_connection_mode", querypool_connection_mode)
        if server_full_name and not isinstance(server_full_name, str):
            raise TypeError("Expected argument 'server_full_name' to be a str")
        pulumi.set(__self__, "server_full_name", server_full_name)
        if server_monitor_mode and not isinstance(server_monitor_mode, int):
            raise TypeError("Expected argument 'server_monitor_mode' to be a int")
        pulumi.set(__self__, "server_monitor_mode", server_monitor_mode)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="asAdministrators")
    def as_administrators(self) -> Optional['outputs.ServerAdministratorsResponse']:
        """
        A collection of AS server administrators
        """
        return pulumi.get(self, "as_administrators")

    @property
    @pulumi.getter(name="backupBlobContainerUri")
    def backup_blob_container_uri(self) -> Optional[str]:
        """
        The SAS container URI to the backup container.
        """
        return pulumi.get(self, "backup_blob_container_uri")

    @property
    @pulumi.getter(name="gatewayDetails")
    def gateway_details(self) -> Optional['outputs.GatewayDetailsResponse']:
        """
        The gateway details configured for the AS server.
        """
        return pulumi.get(self, "gateway_details")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        An identifier that represents the Analysis Services resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipV4FirewallSettings")
    def ip_v4_firewall_settings(self) -> Optional['outputs.IPv4FirewallSettingsResponse']:
        """
        The firewall settings for the AS server.
        """
        return pulumi.get(self, "ip_v4_firewall_settings")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Location of the Analysis Services resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedMode")
    def managed_mode(self) -> Optional[int]:
        """
        The managed mode of the server (0 = not managed, 1 = managed).
        """
        return pulumi.get(self, "managed_mode")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Analysis Services resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current deployment state of Analysis Services resource. The provisioningState is to indicate states for resource provisioning.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="querypoolConnectionMode")
    def querypool_connection_mode(self) -> Optional[str]:
        """
        How the read-write server's participation in the query pool is controlled.<br/>It can have the following values: <ul><li>readOnly - indicates that the read-write server is intended not to participate in query operations</li><li>all - indicates that the read-write server can participate in query operations</li></ul>Specifying readOnly when capacity is 1 results in error.
        """
        return pulumi.get(self, "querypool_connection_mode")

    @property
    @pulumi.getter(name="serverFullName")
    def server_full_name(self) -> str:
        """
        The full name of the Analysis Services resource.
        """
        return pulumi.get(self, "server_full_name")

    @property
    @pulumi.getter(name="serverMonitorMode")
    def server_monitor_mode(self) -> Optional[int]:
        """
        The server monitor mode for AS server
        """
        return pulumi.get(self, "server_monitor_mode")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.ResourceSkuResponse':
        """
        The SKU of the Analysis Services resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of Analysis Services resource. The state is to indicate more states outside of resource provisioning.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Key-value pairs of additional resource provisioning properties.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the Analysis Services resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetServerDetailsResult(GetServerDetailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerDetailsResult(
            as_administrators=self.as_administrators,
            backup_blob_container_uri=self.backup_blob_container_uri,
            gateway_details=self.gateway_details,
            id=self.id,
            ip_v4_firewall_settings=self.ip_v4_firewall_settings,
            location=self.location,
            managed_mode=self.managed_mode,
            name=self.name,
            provisioning_state=self.provisioning_state,
            querypool_connection_mode=self.querypool_connection_mode,
            server_full_name=self.server_full_name,
            server_monitor_mode=self.server_monitor_mode,
            sku=self.sku,
            state=self.state,
            tags=self.tags,
            type=self.type)


def get_server_details(resource_group_name: Optional[str] = None,
                       server_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerDetailsResult:
    """
    Represents an instance of an Analysis Services resource.
    API Version: 2017-08-01.


    :param str resource_group_name: The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    :param str server_name: The name of the Analysis Services server. It must be a minimum of 3 characters, and a maximum of 63.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:analysisservices:getServerDetails', __args__, opts=opts, typ=GetServerDetailsResult).value

    return AwaitableGetServerDetailsResult(
        as_administrators=__ret__.as_administrators,
        backup_blob_container_uri=__ret__.backup_blob_container_uri,
        gateway_details=__ret__.gateway_details,
        id=__ret__.id,
        ip_v4_firewall_settings=__ret__.ip_v4_firewall_settings,
        location=__ret__.location,
        managed_mode=__ret__.managed_mode,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        querypool_connection_mode=__ret__.querypool_connection_mode,
        server_full_name=__ret__.server_full_name,
        server_monitor_mode=__ret__.server_monitor_mode,
        sku=__ret__.sku,
        state=__ret__.state,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_server_details)
def get_server_details_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                              server_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerDetailsResult]:
    """
    Represents an instance of an Analysis Services resource.
    API Version: 2017-08-01.


    :param str resource_group_name: The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    :param str server_name: The name of the Analysis Services server. It must be a minimum of 3 characters, and a maximum of 63.
    """
    ...
