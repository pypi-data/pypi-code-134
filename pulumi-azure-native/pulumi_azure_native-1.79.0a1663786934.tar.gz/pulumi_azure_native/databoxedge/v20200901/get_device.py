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
    'GetDeviceResult',
    'AwaitableGetDeviceResult',
    'get_device',
    'get_device_output',
]

warnings.warn("""Version 2020-09-01 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetDeviceResult:
    """
    The Data Box Edge/Gateway device.
    """
    def __init__(__self__, configured_role_types=None, culture=None, data_box_edge_device_status=None, description=None, device_hcs_version=None, device_local_capacity=None, device_model=None, device_software_version=None, device_type=None, edge_profile=None, etag=None, friendly_name=None, id=None, identity=None, kind=None, location=None, model_description=None, name=None, node_count=None, resource_move_details=None, serial_number=None, sku=None, system_data=None, tags=None, time_zone=None, type=None):
        if configured_role_types and not isinstance(configured_role_types, list):
            raise TypeError("Expected argument 'configured_role_types' to be a list")
        pulumi.set(__self__, "configured_role_types", configured_role_types)
        if culture and not isinstance(culture, str):
            raise TypeError("Expected argument 'culture' to be a str")
        pulumi.set(__self__, "culture", culture)
        if data_box_edge_device_status and not isinstance(data_box_edge_device_status, str):
            raise TypeError("Expected argument 'data_box_edge_device_status' to be a str")
        pulumi.set(__self__, "data_box_edge_device_status", data_box_edge_device_status)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if device_hcs_version and not isinstance(device_hcs_version, str):
            raise TypeError("Expected argument 'device_hcs_version' to be a str")
        pulumi.set(__self__, "device_hcs_version", device_hcs_version)
        if device_local_capacity and not isinstance(device_local_capacity, float):
            raise TypeError("Expected argument 'device_local_capacity' to be a float")
        pulumi.set(__self__, "device_local_capacity", device_local_capacity)
        if device_model and not isinstance(device_model, str):
            raise TypeError("Expected argument 'device_model' to be a str")
        pulumi.set(__self__, "device_model", device_model)
        if device_software_version and not isinstance(device_software_version, str):
            raise TypeError("Expected argument 'device_software_version' to be a str")
        pulumi.set(__self__, "device_software_version", device_software_version)
        if device_type and not isinstance(device_type, str):
            raise TypeError("Expected argument 'device_type' to be a str")
        pulumi.set(__self__, "device_type", device_type)
        if edge_profile and not isinstance(edge_profile, dict):
            raise TypeError("Expected argument 'edge_profile' to be a dict")
        pulumi.set(__self__, "edge_profile", edge_profile)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if model_description and not isinstance(model_description, str):
            raise TypeError("Expected argument 'model_description' to be a str")
        pulumi.set(__self__, "model_description", model_description)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if node_count and not isinstance(node_count, int):
            raise TypeError("Expected argument 'node_count' to be a int")
        pulumi.set(__self__, "node_count", node_count)
        if resource_move_details and not isinstance(resource_move_details, dict):
            raise TypeError("Expected argument 'resource_move_details' to be a dict")
        pulumi.set(__self__, "resource_move_details", resource_move_details)
        if serial_number and not isinstance(serial_number, str):
            raise TypeError("Expected argument 'serial_number' to be a str")
        pulumi.set(__self__, "serial_number", serial_number)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if time_zone and not isinstance(time_zone, str):
            raise TypeError("Expected argument 'time_zone' to be a str")
        pulumi.set(__self__, "time_zone", time_zone)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="configuredRoleTypes")
    def configured_role_types(self) -> Sequence[str]:
        """
        Type of compute roles configured.
        """
        return pulumi.get(self, "configured_role_types")

    @property
    @pulumi.getter
    def culture(self) -> str:
        """
        The Data Box Edge/Gateway device culture.
        """
        return pulumi.get(self, "culture")

    @property
    @pulumi.getter(name="dataBoxEdgeDeviceStatus")
    def data_box_edge_device_status(self) -> Optional[str]:
        """
        The status of the Data Box Edge/Gateway device.
        """
        return pulumi.get(self, "data_box_edge_device_status")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The Description of the Data Box Edge/Gateway device.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="deviceHcsVersion")
    def device_hcs_version(self) -> str:
        """
        The device software version number of the device (eg: 1.2.18105.6).
        """
        return pulumi.get(self, "device_hcs_version")

    @property
    @pulumi.getter(name="deviceLocalCapacity")
    def device_local_capacity(self) -> float:
        """
        The Data Box Edge/Gateway device local capacity in MB.
        """
        return pulumi.get(self, "device_local_capacity")

    @property
    @pulumi.getter(name="deviceModel")
    def device_model(self) -> str:
        """
        The Data Box Edge/Gateway device model.
        """
        return pulumi.get(self, "device_model")

    @property
    @pulumi.getter(name="deviceSoftwareVersion")
    def device_software_version(self) -> str:
        """
        The Data Box Edge/Gateway device software version.
        """
        return pulumi.get(self, "device_software_version")

    @property
    @pulumi.getter(name="deviceType")
    def device_type(self) -> str:
        """
        The type of the Data Box Edge/Gateway device.
        """
        return pulumi.get(self, "device_type")

    @property
    @pulumi.getter(name="edgeProfile")
    def edge_profile(self) -> 'outputs.EdgeProfileResponse':
        """
        The details of Edge Profile for this resource
        """
        return pulumi.get(self, "edge_profile")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        The etag for the devices.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> str:
        """
        The Data Box Edge/Gateway device name.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ResourceIdentityResponse']:
        """
        Msi identity of the resource
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The etag for the devices.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location of the device. This is a supported and registered Azure geographical region (for example, West US, East US, or Southeast Asia). The geographical region of a device cannot be changed once it is created, but if an identical geographical region is specified on update, the request will succeed.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="modelDescription")
    def model_description(self) -> str:
        """
        The description of the Data Box Edge/Gateway device model.
        """
        return pulumi.get(self, "model_description")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> int:
        """
        The number of nodes in the cluster.
        """
        return pulumi.get(self, "node_count")

    @property
    @pulumi.getter(name="resourceMoveDetails")
    def resource_move_details(self) -> 'outputs.ResourceMoveDetailsResponse':
        """
        The details of the move operation on this resource.
        """
        return pulumi.get(self, "resource_move_details")

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> str:
        """
        The Serial Number of Data Box Edge/Gateway device.
        """
        return pulumi.get(self, "serial_number")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The SKU type.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        DataBoxEdge Resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The list of tags that describe the device. These tags can be used to view and group this device (across resource groups).
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> str:
        """
        The Data Box Edge/Gateway device timezone.
        """
        return pulumi.get(self, "time_zone")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")


class AwaitableGetDeviceResult(GetDeviceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeviceResult(
            configured_role_types=self.configured_role_types,
            culture=self.culture,
            data_box_edge_device_status=self.data_box_edge_device_status,
            description=self.description,
            device_hcs_version=self.device_hcs_version,
            device_local_capacity=self.device_local_capacity,
            device_model=self.device_model,
            device_software_version=self.device_software_version,
            device_type=self.device_type,
            edge_profile=self.edge_profile,
            etag=self.etag,
            friendly_name=self.friendly_name,
            id=self.id,
            identity=self.identity,
            kind=self.kind,
            location=self.location,
            model_description=self.model_description,
            name=self.name,
            node_count=self.node_count,
            resource_move_details=self.resource_move_details,
            serial_number=self.serial_number,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            time_zone=self.time_zone,
            type=self.type)


def get_device(device_name: Optional[str] = None,
               resource_group_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeviceResult:
    """
    The Data Box Edge/Gateway device.


    :param str device_name: The device name.
    :param str resource_group_name: The resource group name.
    """
    pulumi.log.warn("""get_device is deprecated: Version 2020-09-01 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:databoxedge/v20200901:getDevice', __args__, opts=opts, typ=GetDeviceResult).value

    return AwaitableGetDeviceResult(
        configured_role_types=__ret__.configured_role_types,
        culture=__ret__.culture,
        data_box_edge_device_status=__ret__.data_box_edge_device_status,
        description=__ret__.description,
        device_hcs_version=__ret__.device_hcs_version,
        device_local_capacity=__ret__.device_local_capacity,
        device_model=__ret__.device_model,
        device_software_version=__ret__.device_software_version,
        device_type=__ret__.device_type,
        edge_profile=__ret__.edge_profile,
        etag=__ret__.etag,
        friendly_name=__ret__.friendly_name,
        id=__ret__.id,
        identity=__ret__.identity,
        kind=__ret__.kind,
        location=__ret__.location,
        model_description=__ret__.model_description,
        name=__ret__.name,
        node_count=__ret__.node_count,
        resource_move_details=__ret__.resource_move_details,
        serial_number=__ret__.serial_number,
        sku=__ret__.sku,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        time_zone=__ret__.time_zone,
        type=__ret__.type)


@_utilities.lift_output_func(get_device)
def get_device_output(device_name: Optional[pulumi.Input[str]] = None,
                      resource_group_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeviceResult]:
    """
    The Data Box Edge/Gateway device.


    :param str device_name: The device name.
    :param str resource_group_name: The resource group name.
    """
    pulumi.log.warn("""get_device is deprecated: Version 2020-09-01 will be removed in v2 of the provider.""")
    ...
