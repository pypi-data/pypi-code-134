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
from ._inputs import *

__all__ = ['VirtualMachineResourceArgs', 'VirtualMachineResource']

@pulumi.input_type
class VirtualMachineResourceArgs:
    def __init__(__self__, *,
                 lab_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 artifact_deployment_status: Optional[pulumi.Input['ArtifactDeploymentStatusPropertiesArgs']] = None,
                 artifacts: Optional[pulumi.Input[Sequence[pulumi.Input['ArtifactInstallPropertiesArgs']]]] = None,
                 compute_id: Optional[pulumi.Input[str]] = None,
                 created_by_user: Optional[pulumi.Input[str]] = None,
                 created_by_user_id: Optional[pulumi.Input[str]] = None,
                 custom_image_id: Optional[pulumi.Input[str]] = None,
                 disallow_public_ip_address: Optional[pulumi.Input[bool]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 gallery_image_reference: Optional[pulumi.Input['GalleryImageReferenceArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_authentication_with_ssh_key: Optional[pulumi.Input[bool]] = None,
                 lab_subnet_name: Optional[pulumi.Input[str]] = None,
                 lab_virtual_network_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 os_type: Optional[pulumi.Input[str]] = None,
                 owner_object_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 ssh_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VirtualMachineResource resource.
        :param pulumi.Input[str] lab_name: The name of the lab.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['ArtifactDeploymentStatusPropertiesArgs'] artifact_deployment_status: The artifact deployment status for the virtual machine.
        :param pulumi.Input[Sequence[pulumi.Input['ArtifactInstallPropertiesArgs']]] artifacts: The artifacts to be installed on the virtual machine.
        :param pulumi.Input[str] compute_id: The resource identifier (Microsoft.Compute) of the virtual machine.
        :param pulumi.Input[str] created_by_user: The email address of creator of the virtual machine.
        :param pulumi.Input[str] created_by_user_id: The object identifier of the creator of the virtual machine.
        :param pulumi.Input[str] custom_image_id: The custom image identifier of the virtual machine.
        :param pulumi.Input[bool] disallow_public_ip_address: Indicates whether the virtual machine is to be created without a public IP address.
        :param pulumi.Input[str] fqdn: The fully-qualified domain name of the virtual machine.
        :param pulumi.Input['GalleryImageReferenceArgs'] gallery_image_reference: The Microsoft Azure Marketplace image reference of the virtual machine.
        :param pulumi.Input[str] id: The identifier of the resource.
        :param pulumi.Input[bool] is_authentication_with_ssh_key: A value indicating whether this virtual machine uses an SSH key for authentication.
        :param pulumi.Input[str] lab_subnet_name: The lab subnet name of the virtual machine.
        :param pulumi.Input[str] lab_virtual_network_id: The lab virtual network identifier of the virtual machine.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] notes: The notes of the virtual machine.
        :param pulumi.Input[str] os_type: The OS type of the virtual machine.
        :param pulumi.Input[str] owner_object_id: The object identifier of the owner of the virtual machine.
        :param pulumi.Input[str] password: The password of the virtual machine administrator.
        :param pulumi.Input[str] provisioning_state: The provisioning status of the resource.
        :param pulumi.Input[str] size: The size of the virtual machine.
        :param pulumi.Input[str] ssh_key: The SSH key of the virtual machine administrator.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[str] type: The type of the resource.
        :param pulumi.Input[str] user_name: The user name of the virtual machine.
        """
        pulumi.set(__self__, "lab_name", lab_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if artifact_deployment_status is not None:
            pulumi.set(__self__, "artifact_deployment_status", artifact_deployment_status)
        if artifacts is not None:
            pulumi.set(__self__, "artifacts", artifacts)
        if compute_id is not None:
            pulumi.set(__self__, "compute_id", compute_id)
        if created_by_user is not None:
            pulumi.set(__self__, "created_by_user", created_by_user)
        if created_by_user_id is not None:
            pulumi.set(__self__, "created_by_user_id", created_by_user_id)
        if custom_image_id is not None:
            pulumi.set(__self__, "custom_image_id", custom_image_id)
        if disallow_public_ip_address is not None:
            pulumi.set(__self__, "disallow_public_ip_address", disallow_public_ip_address)
        if fqdn is not None:
            pulumi.set(__self__, "fqdn", fqdn)
        if gallery_image_reference is not None:
            pulumi.set(__self__, "gallery_image_reference", gallery_image_reference)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if is_authentication_with_ssh_key is not None:
            pulumi.set(__self__, "is_authentication_with_ssh_key", is_authentication_with_ssh_key)
        if lab_subnet_name is not None:
            pulumi.set(__self__, "lab_subnet_name", lab_subnet_name)
        if lab_virtual_network_id is not None:
            pulumi.set(__self__, "lab_virtual_network_id", lab_virtual_network_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if os_type is not None:
            pulumi.set(__self__, "os_type", os_type)
        if owner_object_id is not None:
            pulumi.set(__self__, "owner_object_id", owner_object_id)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if ssh_key is not None:
            pulumi.set(__self__, "ssh_key", ssh_key)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if user_name is not None:
            pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="labName")
    def lab_name(self) -> pulumi.Input[str]:
        """
        The name of the lab.
        """
        return pulumi.get(self, "lab_name")

    @lab_name.setter
    def lab_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "lab_name", value)

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
    @pulumi.getter(name="artifactDeploymentStatus")
    def artifact_deployment_status(self) -> Optional[pulumi.Input['ArtifactDeploymentStatusPropertiesArgs']]:
        """
        The artifact deployment status for the virtual machine.
        """
        return pulumi.get(self, "artifact_deployment_status")

    @artifact_deployment_status.setter
    def artifact_deployment_status(self, value: Optional[pulumi.Input['ArtifactDeploymentStatusPropertiesArgs']]):
        pulumi.set(self, "artifact_deployment_status", value)

    @property
    @pulumi.getter
    def artifacts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ArtifactInstallPropertiesArgs']]]]:
        """
        The artifacts to be installed on the virtual machine.
        """
        return pulumi.get(self, "artifacts")

    @artifacts.setter
    def artifacts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ArtifactInstallPropertiesArgs']]]]):
        pulumi.set(self, "artifacts", value)

    @property
    @pulumi.getter(name="computeId")
    def compute_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource identifier (Microsoft.Compute) of the virtual machine.
        """
        return pulumi.get(self, "compute_id")

    @compute_id.setter
    def compute_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compute_id", value)

    @property
    @pulumi.getter(name="createdByUser")
    def created_by_user(self) -> Optional[pulumi.Input[str]]:
        """
        The email address of creator of the virtual machine.
        """
        return pulumi.get(self, "created_by_user")

    @created_by_user.setter
    def created_by_user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by_user", value)

    @property
    @pulumi.getter(name="createdByUserId")
    def created_by_user_id(self) -> Optional[pulumi.Input[str]]:
        """
        The object identifier of the creator of the virtual machine.
        """
        return pulumi.get(self, "created_by_user_id")

    @created_by_user_id.setter
    def created_by_user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by_user_id", value)

    @property
    @pulumi.getter(name="customImageId")
    def custom_image_id(self) -> Optional[pulumi.Input[str]]:
        """
        The custom image identifier of the virtual machine.
        """
        return pulumi.get(self, "custom_image_id")

    @custom_image_id.setter
    def custom_image_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_image_id", value)

    @property
    @pulumi.getter(name="disallowPublicIpAddress")
    def disallow_public_ip_address(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the virtual machine is to be created without a public IP address.
        """
        return pulumi.get(self, "disallow_public_ip_address")

    @disallow_public_ip_address.setter
    def disallow_public_ip_address(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disallow_public_ip_address", value)

    @property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[str]]:
        """
        The fully-qualified domain name of the virtual machine.
        """
        return pulumi.get(self, "fqdn")

    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fqdn", value)

    @property
    @pulumi.getter(name="galleryImageReference")
    def gallery_image_reference(self) -> Optional[pulumi.Input['GalleryImageReferenceArgs']]:
        """
        The Microsoft Azure Marketplace image reference of the virtual machine.
        """
        return pulumi.get(self, "gallery_image_reference")

    @gallery_image_reference.setter
    def gallery_image_reference(self, value: Optional[pulumi.Input['GalleryImageReferenceArgs']]):
        pulumi.set(self, "gallery_image_reference", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the resource.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="isAuthenticationWithSshKey")
    def is_authentication_with_ssh_key(self) -> Optional[pulumi.Input[bool]]:
        """
        A value indicating whether this virtual machine uses an SSH key for authentication.
        """
        return pulumi.get(self, "is_authentication_with_ssh_key")

    @is_authentication_with_ssh_key.setter
    def is_authentication_with_ssh_key(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_authentication_with_ssh_key", value)

    @property
    @pulumi.getter(name="labSubnetName")
    def lab_subnet_name(self) -> Optional[pulumi.Input[str]]:
        """
        The lab subnet name of the virtual machine.
        """
        return pulumi.get(self, "lab_subnet_name")

    @lab_subnet_name.setter
    def lab_subnet_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lab_subnet_name", value)

    @property
    @pulumi.getter(name="labVirtualNetworkId")
    def lab_virtual_network_id(self) -> Optional[pulumi.Input[str]]:
        """
        The lab virtual network identifier of the virtual machine.
        """
        return pulumi.get(self, "lab_virtual_network_id")

    @lab_virtual_network_id.setter
    def lab_virtual_network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lab_virtual_network_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        """
        The notes of the virtual machine.
        """
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[str]]:
        """
        The OS type of the virtual machine.
        """
        return pulumi.get(self, "os_type")

    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_type", value)

    @property
    @pulumi.getter(name="ownerObjectId")
    def owner_object_id(self) -> Optional[pulumi.Input[str]]:
        """
        The object identifier of the owner of the virtual machine.
        """
        return pulumi.get(self, "owner_object_id")

    @owner_object_id.setter
    def owner_object_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner_object_id", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the virtual machine administrator.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        """
        The size of the virtual machine.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="sshKey")
    def ssh_key(self) -> Optional[pulumi.Input[str]]:
        """
        The SSH key of the virtual machine administrator.
        """
        return pulumi.get(self, "ssh_key")

    @ssh_key.setter
    def ssh_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssh_key", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[str]]:
        """
        The user name of the virtual machine.
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_name", value)


warnings.warn("""Version 2015-05-21-preview will be removed in v2 of the provider.""", DeprecationWarning)


class VirtualMachineResource(pulumi.CustomResource):
    warnings.warn("""Version 2015-05-21-preview will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 artifact_deployment_status: Optional[pulumi.Input[pulumi.InputType['ArtifactDeploymentStatusPropertiesArgs']]] = None,
                 artifacts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ArtifactInstallPropertiesArgs']]]]] = None,
                 compute_id: Optional[pulumi.Input[str]] = None,
                 created_by_user: Optional[pulumi.Input[str]] = None,
                 created_by_user_id: Optional[pulumi.Input[str]] = None,
                 custom_image_id: Optional[pulumi.Input[str]] = None,
                 disallow_public_ip_address: Optional[pulumi.Input[bool]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 gallery_image_reference: Optional[pulumi.Input[pulumi.InputType['GalleryImageReferenceArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_authentication_with_ssh_key: Optional[pulumi.Input[bool]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 lab_subnet_name: Optional[pulumi.Input[str]] = None,
                 lab_virtual_network_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 os_type: Optional[pulumi.Input[str]] = None,
                 owner_object_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 ssh_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A virtual machine.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ArtifactDeploymentStatusPropertiesArgs']] artifact_deployment_status: The artifact deployment status for the virtual machine.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ArtifactInstallPropertiesArgs']]]] artifacts: The artifacts to be installed on the virtual machine.
        :param pulumi.Input[str] compute_id: The resource identifier (Microsoft.Compute) of the virtual machine.
        :param pulumi.Input[str] created_by_user: The email address of creator of the virtual machine.
        :param pulumi.Input[str] created_by_user_id: The object identifier of the creator of the virtual machine.
        :param pulumi.Input[str] custom_image_id: The custom image identifier of the virtual machine.
        :param pulumi.Input[bool] disallow_public_ip_address: Indicates whether the virtual machine is to be created without a public IP address.
        :param pulumi.Input[str] fqdn: The fully-qualified domain name of the virtual machine.
        :param pulumi.Input[pulumi.InputType['GalleryImageReferenceArgs']] gallery_image_reference: The Microsoft Azure Marketplace image reference of the virtual machine.
        :param pulumi.Input[str] id: The identifier of the resource.
        :param pulumi.Input[bool] is_authentication_with_ssh_key: A value indicating whether this virtual machine uses an SSH key for authentication.
        :param pulumi.Input[str] lab_name: The name of the lab.
        :param pulumi.Input[str] lab_subnet_name: The lab subnet name of the virtual machine.
        :param pulumi.Input[str] lab_virtual_network_id: The lab virtual network identifier of the virtual machine.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] notes: The notes of the virtual machine.
        :param pulumi.Input[str] os_type: The OS type of the virtual machine.
        :param pulumi.Input[str] owner_object_id: The object identifier of the owner of the virtual machine.
        :param pulumi.Input[str] password: The password of the virtual machine administrator.
        :param pulumi.Input[str] provisioning_state: The provisioning status of the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] size: The size of the virtual machine.
        :param pulumi.Input[str] ssh_key: The SSH key of the virtual machine administrator.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[str] type: The type of the resource.
        :param pulumi.Input[str] user_name: The user name of the virtual machine.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualMachineResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A virtual machine.

        :param str resource_name: The name of the resource.
        :param VirtualMachineResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualMachineResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 artifact_deployment_status: Optional[pulumi.Input[pulumi.InputType['ArtifactDeploymentStatusPropertiesArgs']]] = None,
                 artifacts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ArtifactInstallPropertiesArgs']]]]] = None,
                 compute_id: Optional[pulumi.Input[str]] = None,
                 created_by_user: Optional[pulumi.Input[str]] = None,
                 created_by_user_id: Optional[pulumi.Input[str]] = None,
                 custom_image_id: Optional[pulumi.Input[str]] = None,
                 disallow_public_ip_address: Optional[pulumi.Input[bool]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 gallery_image_reference: Optional[pulumi.Input[pulumi.InputType['GalleryImageReferenceArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_authentication_with_ssh_key: Optional[pulumi.Input[bool]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 lab_subnet_name: Optional[pulumi.Input[str]] = None,
                 lab_virtual_network_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 os_type: Optional[pulumi.Input[str]] = None,
                 owner_object_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 ssh_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""VirtualMachineResource is deprecated: Version 2015-05-21-preview will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualMachineResourceArgs.__new__(VirtualMachineResourceArgs)

            __props__.__dict__["artifact_deployment_status"] = artifact_deployment_status
            __props__.__dict__["artifacts"] = artifacts
            __props__.__dict__["compute_id"] = compute_id
            __props__.__dict__["created_by_user"] = created_by_user
            __props__.__dict__["created_by_user_id"] = created_by_user_id
            __props__.__dict__["custom_image_id"] = custom_image_id
            __props__.__dict__["disallow_public_ip_address"] = disallow_public_ip_address
            __props__.__dict__["fqdn"] = fqdn
            __props__.__dict__["gallery_image_reference"] = gallery_image_reference
            __props__.__dict__["id"] = id
            __props__.__dict__["is_authentication_with_ssh_key"] = is_authentication_with_ssh_key
            if lab_name is None and not opts.urn:
                raise TypeError("Missing required property 'lab_name'")
            __props__.__dict__["lab_name"] = lab_name
            __props__.__dict__["lab_subnet_name"] = lab_subnet_name
            __props__.__dict__["lab_virtual_network_id"] = lab_virtual_network_id
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["notes"] = notes
            __props__.__dict__["os_type"] = os_type
            __props__.__dict__["owner_object_id"] = owner_object_id
            __props__.__dict__["password"] = password
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["size"] = size
            __props__.__dict__["ssh_key"] = ssh_key
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = type
            __props__.__dict__["user_name"] = user_name
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devtestlab:VirtualMachineResource"), pulumi.Alias(type_="azure-native:devtestlab/v20160515:VirtualMachineResource"), pulumi.Alias(type_="azure-native:devtestlab/v20180915:VirtualMachineResource")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualMachineResource, __self__).__init__(
            'azure-native:devtestlab/v20150521preview:VirtualMachineResource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualMachineResource':
        """
        Get an existing VirtualMachineResource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualMachineResourceArgs.__new__(VirtualMachineResourceArgs)

        __props__.__dict__["artifact_deployment_status"] = None
        __props__.__dict__["artifacts"] = None
        __props__.__dict__["compute_id"] = None
        __props__.__dict__["created_by_user"] = None
        __props__.__dict__["created_by_user_id"] = None
        __props__.__dict__["custom_image_id"] = None
        __props__.__dict__["disallow_public_ip_address"] = None
        __props__.__dict__["fqdn"] = None
        __props__.__dict__["gallery_image_reference"] = None
        __props__.__dict__["is_authentication_with_ssh_key"] = None
        __props__.__dict__["lab_subnet_name"] = None
        __props__.__dict__["lab_virtual_network_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notes"] = None
        __props__.__dict__["os_type"] = None
        __props__.__dict__["owner_object_id"] = None
        __props__.__dict__["password"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["size"] = None
        __props__.__dict__["ssh_key"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_name"] = None
        return VirtualMachineResource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="artifactDeploymentStatus")
    def artifact_deployment_status(self) -> pulumi.Output[Optional['outputs.ArtifactDeploymentStatusPropertiesResponse']]:
        """
        The artifact deployment status for the virtual machine.
        """
        return pulumi.get(self, "artifact_deployment_status")

    @property
    @pulumi.getter
    def artifacts(self) -> pulumi.Output[Optional[Sequence['outputs.ArtifactInstallPropertiesResponse']]]:
        """
        The artifacts to be installed on the virtual machine.
        """
        return pulumi.get(self, "artifacts")

    @property
    @pulumi.getter(name="computeId")
    def compute_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource identifier (Microsoft.Compute) of the virtual machine.
        """
        return pulumi.get(self, "compute_id")

    @property
    @pulumi.getter(name="createdByUser")
    def created_by_user(self) -> pulumi.Output[Optional[str]]:
        """
        The email address of creator of the virtual machine.
        """
        return pulumi.get(self, "created_by_user")

    @property
    @pulumi.getter(name="createdByUserId")
    def created_by_user_id(self) -> pulumi.Output[Optional[str]]:
        """
        The object identifier of the creator of the virtual machine.
        """
        return pulumi.get(self, "created_by_user_id")

    @property
    @pulumi.getter(name="customImageId")
    def custom_image_id(self) -> pulumi.Output[Optional[str]]:
        """
        The custom image identifier of the virtual machine.
        """
        return pulumi.get(self, "custom_image_id")

    @property
    @pulumi.getter(name="disallowPublicIpAddress")
    def disallow_public_ip_address(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the virtual machine is to be created without a public IP address.
        """
        return pulumi.get(self, "disallow_public_ip_address")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[Optional[str]]:
        """
        The fully-qualified domain name of the virtual machine.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="galleryImageReference")
    def gallery_image_reference(self) -> pulumi.Output[Optional['outputs.GalleryImageReferenceResponse']]:
        """
        The Microsoft Azure Marketplace image reference of the virtual machine.
        """
        return pulumi.get(self, "gallery_image_reference")

    @property
    @pulumi.getter(name="isAuthenticationWithSshKey")
    def is_authentication_with_ssh_key(self) -> pulumi.Output[Optional[bool]]:
        """
        A value indicating whether this virtual machine uses an SSH key for authentication.
        """
        return pulumi.get(self, "is_authentication_with_ssh_key")

    @property
    @pulumi.getter(name="labSubnetName")
    def lab_subnet_name(self) -> pulumi.Output[Optional[str]]:
        """
        The lab subnet name of the virtual machine.
        """
        return pulumi.get(self, "lab_subnet_name")

    @property
    @pulumi.getter(name="labVirtualNetworkId")
    def lab_virtual_network_id(self) -> pulumi.Output[Optional[str]]:
        """
        The lab virtual network identifier of the virtual machine.
        """
        return pulumi.get(self, "lab_virtual_network_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[str]]:
        """
        The notes of the virtual machine.
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Output[Optional[str]]:
        """
        The OS type of the virtual machine.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="ownerObjectId")
    def owner_object_id(self) -> pulumi.Output[Optional[str]]:
        """
        The object identifier of the owner of the virtual machine.
        """
        return pulumi.get(self, "owner_object_id")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        The password of the virtual machine administrator.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[Optional[str]]:
        """
        The size of the virtual machine.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="sshKey")
    def ssh_key(self) -> pulumi.Output[Optional[str]]:
        """
        The SSH key of the virtual machine administrator.
        """
        return pulumi.get(self, "ssh_key")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[Optional[str]]:
        """
        The user name of the virtual machine.
        """
        return pulumi.get(self, "user_name")

