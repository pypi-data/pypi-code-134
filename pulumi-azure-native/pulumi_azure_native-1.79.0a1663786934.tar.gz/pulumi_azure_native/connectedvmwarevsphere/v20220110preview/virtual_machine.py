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

__all__ = ['VirtualMachineArgs', 'VirtualMachine']

@pulumi.input_type
class VirtualMachineArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None,
                 firmware_type: Optional[pulumi.Input[Union[str, 'FirmwareType']]] = None,
                 hardware_profile: Optional[pulumi.Input['HardwareProfileArgs']] = None,
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 inventory_item_id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mo_ref_id: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input['NetworkProfileArgs']] = None,
                 os_profile: Optional[pulumi.Input['OsProfileArgs']] = None,
                 placement_profile: Optional[pulumi.Input['PlacementProfileArgs']] = None,
                 resource_pool_id: Optional[pulumi.Input[str]] = None,
                 security_profile: Optional[pulumi.Input['SecurityProfileArgs']] = None,
                 smbios_uuid: Optional[pulumi.Input[str]] = None,
                 storage_profile: Optional[pulumi.Input['StorageProfileArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 template_id: Optional[pulumi.Input[str]] = None,
                 v_center_id: Optional[pulumi.Input[str]] = None,
                 virtual_machine_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VirtualMachine resource.
        :param pulumi.Input[str] resource_group_name: The Resource Group Name.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: Gets or sets the extended location.
        :param pulumi.Input[Union[str, 'FirmwareType']] firmware_type: Firmware type
        :param pulumi.Input['HardwareProfileArgs'] hardware_profile: Hardware properties.
        :param pulumi.Input['IdentityArgs'] identity: The identity of the resource.
        :param pulumi.Input[str] inventory_item_id: Gets or sets the inventory Item ID for the virtual machine.
        :param pulumi.Input[str] kind: Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        :param pulumi.Input[str] location: Gets or sets the location.
        :param pulumi.Input[str] mo_ref_id: Gets or sets the vCenter MoRef (Managed Object Reference) ID for the virtual machine.
        :param pulumi.Input['NetworkProfileArgs'] network_profile: Network properties.
        :param pulumi.Input['OsProfileArgs'] os_profile: OS properties.
        :param pulumi.Input['PlacementProfileArgs'] placement_profile: Placement properties.
        :param pulumi.Input[str] resource_pool_id: Gets or sets the ARM Id of the resourcePool resource on which this virtual machine will
               deploy.
        :param pulumi.Input['SecurityProfileArgs'] security_profile: Gets the security profile.
        :param pulumi.Input[str] smbios_uuid: Gets or sets the SMBIOS UUID of the vm.
        :param pulumi.Input['StorageProfileArgs'] storage_profile: Storage properties.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the Resource tags.
        :param pulumi.Input[str] template_id: Gets or sets the ARM Id of the template resource to deploy the virtual machine.
        :param pulumi.Input[str] v_center_id: Gets or sets the ARM Id of the vCenter resource in which this resource pool resides.
        :param pulumi.Input[str] virtual_machine_name: Name of the virtual machine resource.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if firmware_type is not None:
            pulumi.set(__self__, "firmware_type", firmware_type)
        if hardware_profile is not None:
            pulumi.set(__self__, "hardware_profile", hardware_profile)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if inventory_item_id is not None:
            pulumi.set(__self__, "inventory_item_id", inventory_item_id)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mo_ref_id is not None:
            pulumi.set(__self__, "mo_ref_id", mo_ref_id)
        if network_profile is not None:
            pulumi.set(__self__, "network_profile", network_profile)
        if os_profile is not None:
            pulumi.set(__self__, "os_profile", os_profile)
        if placement_profile is not None:
            pulumi.set(__self__, "placement_profile", placement_profile)
        if resource_pool_id is not None:
            pulumi.set(__self__, "resource_pool_id", resource_pool_id)
        if security_profile is not None:
            pulumi.set(__self__, "security_profile", security_profile)
        if smbios_uuid is not None:
            pulumi.set(__self__, "smbios_uuid", smbios_uuid)
        if storage_profile is not None:
            pulumi.set(__self__, "storage_profile", storage_profile)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if template_id is not None:
            pulumi.set(__self__, "template_id", template_id)
        if v_center_id is not None:
            pulumi.set(__self__, "v_center_id", v_center_id)
        if virtual_machine_name is not None:
            pulumi.set(__self__, "virtual_machine_name", virtual_machine_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The Resource Group Name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        Gets or sets the extended location.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="firmwareType")
    def firmware_type(self) -> Optional[pulumi.Input[Union[str, 'FirmwareType']]]:
        """
        Firmware type
        """
        return pulumi.get(self, "firmware_type")

    @firmware_type.setter
    def firmware_type(self, value: Optional[pulumi.Input[Union[str, 'FirmwareType']]]):
        pulumi.set(self, "firmware_type", value)

    @property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[pulumi.Input['HardwareProfileArgs']]:
        """
        Hardware properties.
        """
        return pulumi.get(self, "hardware_profile")

    @hardware_profile.setter
    def hardware_profile(self, value: Optional[pulumi.Input['HardwareProfileArgs']]):
        pulumi.set(self, "hardware_profile", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="inventoryItemId")
    def inventory_item_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the inventory Item ID for the virtual machine.
        """
        return pulumi.get(self, "inventory_item_id")

    @inventory_item_id.setter
    def inventory_item_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "inventory_item_id", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="moRefId")
    def mo_ref_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the vCenter MoRef (Managed Object Reference) ID for the virtual machine.
        """
        return pulumi.get(self, "mo_ref_id")

    @mo_ref_id.setter
    def mo_ref_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mo_ref_id", value)

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input['NetworkProfileArgs']]:
        """
        Network properties.
        """
        return pulumi.get(self, "network_profile")

    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input['NetworkProfileArgs']]):
        pulumi.set(self, "network_profile", value)

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input['OsProfileArgs']]:
        """
        OS properties.
        """
        return pulumi.get(self, "os_profile")

    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input['OsProfileArgs']]):
        pulumi.set(self, "os_profile", value)

    @property
    @pulumi.getter(name="placementProfile")
    def placement_profile(self) -> Optional[pulumi.Input['PlacementProfileArgs']]:
        """
        Placement properties.
        """
        return pulumi.get(self, "placement_profile")

    @placement_profile.setter
    def placement_profile(self, value: Optional[pulumi.Input['PlacementProfileArgs']]):
        pulumi.set(self, "placement_profile", value)

    @property
    @pulumi.getter(name="resourcePoolId")
    def resource_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the ARM Id of the resourcePool resource on which this virtual machine will
        deploy.
        """
        return pulumi.get(self, "resource_pool_id")

    @resource_pool_id.setter
    def resource_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_pool_id", value)

    @property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input['SecurityProfileArgs']]:
        """
        Gets the security profile.
        """
        return pulumi.get(self, "security_profile")

    @security_profile.setter
    def security_profile(self, value: Optional[pulumi.Input['SecurityProfileArgs']]):
        pulumi.set(self, "security_profile", value)

    @property
    @pulumi.getter(name="smbiosUuid")
    def smbios_uuid(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the SMBIOS UUID of the vm.
        """
        return pulumi.get(self, "smbios_uuid")

    @smbios_uuid.setter
    def smbios_uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "smbios_uuid", value)

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input['StorageProfileArgs']]:
        """
        Storage properties.
        """
        return pulumi.get(self, "storage_profile")

    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input['StorageProfileArgs']]):
        pulumi.set(self, "storage_profile", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Gets or sets the Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="templateId")
    def template_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the ARM Id of the template resource to deploy the virtual machine.
        """
        return pulumi.get(self, "template_id")

    @template_id.setter
    def template_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_id", value)

    @property
    @pulumi.getter(name="vCenterId")
    def v_center_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the ARM Id of the vCenter resource in which this resource pool resides.
        """
        return pulumi.get(self, "v_center_id")

    @v_center_id.setter
    def v_center_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "v_center_id", value)

    @property
    @pulumi.getter(name="virtualMachineName")
    def virtual_machine_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the virtual machine resource.
        """
        return pulumi.get(self, "virtual_machine_name")

    @virtual_machine_name.setter
    def virtual_machine_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_machine_name", value)


class VirtualMachine(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 firmware_type: Optional[pulumi.Input[Union[str, 'FirmwareType']]] = None,
                 hardware_profile: Optional[pulumi.Input[pulumi.InputType['HardwareProfileArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 inventory_item_id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mo_ref_id: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['NetworkProfileArgs']]] = None,
                 os_profile: Optional[pulumi.Input[pulumi.InputType['OsProfileArgs']]] = None,
                 placement_profile: Optional[pulumi.Input[pulumi.InputType['PlacementProfileArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_pool_id: Optional[pulumi.Input[str]] = None,
                 security_profile: Optional[pulumi.Input[pulumi.InputType['SecurityProfileArgs']]] = None,
                 smbios_uuid: Optional[pulumi.Input[str]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['StorageProfileArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 template_id: Optional[pulumi.Input[str]] = None,
                 v_center_id: Optional[pulumi.Input[str]] = None,
                 virtual_machine_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Define the virtualMachine.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: Gets or sets the extended location.
        :param pulumi.Input[Union[str, 'FirmwareType']] firmware_type: Firmware type
        :param pulumi.Input[pulumi.InputType['HardwareProfileArgs']] hardware_profile: Hardware properties.
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] identity: The identity of the resource.
        :param pulumi.Input[str] inventory_item_id: Gets or sets the inventory Item ID for the virtual machine.
        :param pulumi.Input[str] kind: Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        :param pulumi.Input[str] location: Gets or sets the location.
        :param pulumi.Input[str] mo_ref_id: Gets or sets the vCenter MoRef (Managed Object Reference) ID for the virtual machine.
        :param pulumi.Input[pulumi.InputType['NetworkProfileArgs']] network_profile: Network properties.
        :param pulumi.Input[pulumi.InputType['OsProfileArgs']] os_profile: OS properties.
        :param pulumi.Input[pulumi.InputType['PlacementProfileArgs']] placement_profile: Placement properties.
        :param pulumi.Input[str] resource_group_name: The Resource Group Name.
        :param pulumi.Input[str] resource_pool_id: Gets or sets the ARM Id of the resourcePool resource on which this virtual machine will
               deploy.
        :param pulumi.Input[pulumi.InputType['SecurityProfileArgs']] security_profile: Gets the security profile.
        :param pulumi.Input[str] smbios_uuid: Gets or sets the SMBIOS UUID of the vm.
        :param pulumi.Input[pulumi.InputType['StorageProfileArgs']] storage_profile: Storage properties.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the Resource tags.
        :param pulumi.Input[str] template_id: Gets or sets the ARM Id of the template resource to deploy the virtual machine.
        :param pulumi.Input[str] v_center_id: Gets or sets the ARM Id of the vCenter resource in which this resource pool resides.
        :param pulumi.Input[str] virtual_machine_name: Name of the virtual machine resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualMachineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Define the virtualMachine.

        :param str resource_name: The name of the resource.
        :param VirtualMachineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualMachineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 firmware_type: Optional[pulumi.Input[Union[str, 'FirmwareType']]] = None,
                 hardware_profile: Optional[pulumi.Input[pulumi.InputType['HardwareProfileArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 inventory_item_id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mo_ref_id: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['NetworkProfileArgs']]] = None,
                 os_profile: Optional[pulumi.Input[pulumi.InputType['OsProfileArgs']]] = None,
                 placement_profile: Optional[pulumi.Input[pulumi.InputType['PlacementProfileArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_pool_id: Optional[pulumi.Input[str]] = None,
                 security_profile: Optional[pulumi.Input[pulumi.InputType['SecurityProfileArgs']]] = None,
                 smbios_uuid: Optional[pulumi.Input[str]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['StorageProfileArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 template_id: Optional[pulumi.Input[str]] = None,
                 v_center_id: Optional[pulumi.Input[str]] = None,
                 virtual_machine_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualMachineArgs.__new__(VirtualMachineArgs)

            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["firmware_type"] = firmware_type
            __props__.__dict__["hardware_profile"] = hardware_profile
            __props__.__dict__["identity"] = identity
            __props__.__dict__["inventory_item_id"] = inventory_item_id
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["mo_ref_id"] = mo_ref_id
            __props__.__dict__["network_profile"] = network_profile
            __props__.__dict__["os_profile"] = os_profile
            __props__.__dict__["placement_profile"] = placement_profile
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_pool_id"] = resource_pool_id
            __props__.__dict__["security_profile"] = security_profile
            __props__.__dict__["smbios_uuid"] = smbios_uuid
            __props__.__dict__["storage_profile"] = storage_profile
            __props__.__dict__["tags"] = tags
            __props__.__dict__["template_id"] = template_id
            __props__.__dict__["v_center_id"] = v_center_id
            __props__.__dict__["virtual_machine_name"] = virtual_machine_name
            __props__.__dict__["custom_resource_name"] = None
            __props__.__dict__["folder_path"] = None
            __props__.__dict__["guest_agent_profile"] = None
            __props__.__dict__["instance_uuid"] = None
            __props__.__dict__["mo_name"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["power_state"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["statuses"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["uuid"] = None
            __props__.__dict__["vm_id"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:connectedvmwarevsphere:VirtualMachine"), pulumi.Alias(type_="azure-native:connectedvmwarevsphere/v20201001preview:VirtualMachine")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualMachine, __self__).__init__(
            'azure-native:connectedvmwarevsphere/v20220110preview:VirtualMachine',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualMachine':
        """
        Get an existing VirtualMachine resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualMachineArgs.__new__(VirtualMachineArgs)

        __props__.__dict__["custom_resource_name"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["firmware_type"] = None
        __props__.__dict__["folder_path"] = None
        __props__.__dict__["guest_agent_profile"] = None
        __props__.__dict__["hardware_profile"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["instance_uuid"] = None
        __props__.__dict__["inventory_item_id"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mo_name"] = None
        __props__.__dict__["mo_ref_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_profile"] = None
        __props__.__dict__["os_profile"] = None
        __props__.__dict__["placement_profile"] = None
        __props__.__dict__["power_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_pool_id"] = None
        __props__.__dict__["security_profile"] = None
        __props__.__dict__["smbios_uuid"] = None
        __props__.__dict__["statuses"] = None
        __props__.__dict__["storage_profile"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["template_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["uuid"] = None
        __props__.__dict__["v_center_id"] = None
        __props__.__dict__["vm_id"] = None
        return VirtualMachine(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customResourceName")
    def custom_resource_name(self) -> pulumi.Output[str]:
        """
        Gets the name of the corresponding resource in Kubernetes.
        """
        return pulumi.get(self, "custom_resource_name")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        Gets or sets the extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="firmwareType")
    def firmware_type(self) -> pulumi.Output[Optional[str]]:
        """
        Firmware type
        """
        return pulumi.get(self, "firmware_type")

    @property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> pulumi.Output[str]:
        """
        Gets or sets the folder path of the vm.
        """
        return pulumi.get(self, "folder_path")

    @property
    @pulumi.getter(name="guestAgentProfile")
    def guest_agent_profile(self) -> pulumi.Output[Optional['outputs.GuestAgentProfileResponse']]:
        """
        Guest agent status properties.
        """
        return pulumi.get(self, "guest_agent_profile")

    @property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> pulumi.Output[Optional['outputs.HardwareProfileResponse']]:
        """
        Hardware properties.
        """
        return pulumi.get(self, "hardware_profile")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="instanceUuid")
    def instance_uuid(self) -> pulumi.Output[str]:
        """
        Gets or sets the instance uuid of the vm.
        """
        return pulumi.get(self, "instance_uuid")

    @property
    @pulumi.getter(name="inventoryItemId")
    def inventory_item_id(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the inventory Item ID for the virtual machine.
        """
        return pulumi.get(self, "inventory_item_id")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Gets or sets the location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="moName")
    def mo_name(self) -> pulumi.Output[str]:
        """
        Gets or sets the vCenter Managed Object name for the virtual machine.
        """
        return pulumi.get(self, "mo_name")

    @property
    @pulumi.getter(name="moRefId")
    def mo_ref_id(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the vCenter MoRef (Managed Object Reference) ID for the virtual machine.
        """
        return pulumi.get(self, "mo_ref_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Gets or sets the name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[Optional['outputs.NetworkProfileResponse']]:
        """
        Network properties.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> pulumi.Output[Optional['outputs.OsProfileResponse']]:
        """
        OS properties.
        """
        return pulumi.get(self, "os_profile")

    @property
    @pulumi.getter(name="placementProfile")
    def placement_profile(self) -> pulumi.Output[Optional['outputs.PlacementProfileResponse']]:
        """
        Placement properties.
        """
        return pulumi.get(self, "placement_profile")

    @property
    @pulumi.getter(name="powerState")
    def power_state(self) -> pulumi.Output[str]:
        """
        Gets the power state of the virtual machine.
        """
        return pulumi.get(self, "power_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets or sets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourcePoolId")
    def resource_pool_id(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the ARM Id of the resourcePool resource on which this virtual machine will
        deploy.
        """
        return pulumi.get(self, "resource_pool_id")

    @property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> pulumi.Output[Optional['outputs.SecurityProfileResponse']]:
        """
        Gets the security profile.
        """
        return pulumi.get(self, "security_profile")

    @property
    @pulumi.getter(name="smbiosUuid")
    def smbios_uuid(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the SMBIOS UUID of the vm.
        """
        return pulumi.get(self, "smbios_uuid")

    @property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence['outputs.ResourceStatusResponse']]:
        """
        The resource status information.
        """
        return pulumi.get(self, "statuses")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> pulumi.Output[Optional['outputs.StorageProfileResponse']]:
        """
        Storage properties.
        """
        return pulumi.get(self, "storage_profile")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system data.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Gets or sets the Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateId")
    def template_id(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the ARM Id of the template resource to deploy the virtual machine.
        """
        return pulumi.get(self, "template_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Gets or sets the type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        """
        Gets or sets a unique identifier for this resource.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter(name="vCenterId")
    def v_center_id(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the ARM Id of the vCenter resource in which this resource pool resides.
        """
        return pulumi.get(self, "v_center_id")

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> pulumi.Output[str]:
        """
        Gets or sets a unique identifier for the vm resource.
        """
        return pulumi.get(self, "vm_id")

