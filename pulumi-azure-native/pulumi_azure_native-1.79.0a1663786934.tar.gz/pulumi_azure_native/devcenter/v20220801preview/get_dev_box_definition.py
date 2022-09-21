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
    'GetDevBoxDefinitionResult',
    'AwaitableGetDevBoxDefinitionResult',
    'get_dev_box_definition',
    'get_dev_box_definition_output',
]

@pulumi.output_type
class GetDevBoxDefinitionResult:
    """
    Represents a definition for a Developer Machine.
    """
    def __init__(__self__, active_image_reference=None, id=None, image_reference=None, image_validation_error_details=None, image_validation_status=None, location=None, name=None, os_storage_type=None, provisioning_state=None, sku=None, system_data=None, tags=None, type=None):
        if active_image_reference and not isinstance(active_image_reference, dict):
            raise TypeError("Expected argument 'active_image_reference' to be a dict")
        pulumi.set(__self__, "active_image_reference", active_image_reference)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_reference and not isinstance(image_reference, dict):
            raise TypeError("Expected argument 'image_reference' to be a dict")
        pulumi.set(__self__, "image_reference", image_reference)
        if image_validation_error_details and not isinstance(image_validation_error_details, dict):
            raise TypeError("Expected argument 'image_validation_error_details' to be a dict")
        pulumi.set(__self__, "image_validation_error_details", image_validation_error_details)
        if image_validation_status and not isinstance(image_validation_status, str):
            raise TypeError("Expected argument 'image_validation_status' to be a str")
        pulumi.set(__self__, "image_validation_status", image_validation_status)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if os_storage_type and not isinstance(os_storage_type, str):
            raise TypeError("Expected argument 'os_storage_type' to be a str")
        pulumi.set(__self__, "os_storage_type", os_storage_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="activeImageReference")
    def active_image_reference(self) -> 'outputs.ImageReferenceResponse':
        """
        Image reference information for the currently active image (only populated during updates).
        """
        return pulumi.get(self, "active_image_reference")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> 'outputs.ImageReferenceResponse':
        """
        Image reference information.
        """
        return pulumi.get(self, "image_reference")

    @property
    @pulumi.getter(name="imageValidationErrorDetails")
    def image_validation_error_details(self) -> 'outputs.ImageValidationErrorDetailsResponse':
        """
        Details for image validator error. Populated when the image validation is not successful.
        """
        return pulumi.get(self, "image_validation_error_details")

    @property
    @pulumi.getter(name="imageValidationStatus")
    def image_validation_status(self) -> str:
        """
        Validation status of the configured image.
        """
        return pulumi.get(self, "image_validation_status")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osStorageType")
    def os_storage_type(self) -> str:
        """
        The storage type used for the Operating System disk of Dev Boxes created using this definition.
        """
        return pulumi.get(self, "os_storage_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.SkuResponse':
        """
        The SKU for Dev Boxes created using this definition.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetDevBoxDefinitionResult(GetDevBoxDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDevBoxDefinitionResult(
            active_image_reference=self.active_image_reference,
            id=self.id,
            image_reference=self.image_reference,
            image_validation_error_details=self.image_validation_error_details,
            image_validation_status=self.image_validation_status,
            location=self.location,
            name=self.name,
            os_storage_type=self.os_storage_type,
            provisioning_state=self.provisioning_state,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_dev_box_definition(dev_box_definition_name: Optional[str] = None,
                           dev_center_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDevBoxDefinitionResult:
    """
    Represents a definition for a Developer Machine.


    :param str dev_box_definition_name: The name of the Dev Box definition.
    :param str dev_center_name: The name of the devcenter.
    :param str resource_group_name: Name of the resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['devBoxDefinitionName'] = dev_box_definition_name
    __args__['devCenterName'] = dev_center_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devcenter/v20220801preview:getDevBoxDefinition', __args__, opts=opts, typ=GetDevBoxDefinitionResult).value

    return AwaitableGetDevBoxDefinitionResult(
        active_image_reference=__ret__.active_image_reference,
        id=__ret__.id,
        image_reference=__ret__.image_reference,
        image_validation_error_details=__ret__.image_validation_error_details,
        image_validation_status=__ret__.image_validation_status,
        location=__ret__.location,
        name=__ret__.name,
        os_storage_type=__ret__.os_storage_type,
        provisioning_state=__ret__.provisioning_state,
        sku=__ret__.sku,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_dev_box_definition)
def get_dev_box_definition_output(dev_box_definition_name: Optional[pulumi.Input[str]] = None,
                                  dev_center_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDevBoxDefinitionResult]:
    """
    Represents a definition for a Developer Machine.


    :param str dev_box_definition_name: The name of the Dev Box definition.
    :param str dev_center_name: The name of the devcenter.
    :param str resource_group_name: Name of the resource group within the Azure subscription.
    """
    ...
