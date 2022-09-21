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
    'GetApplianceDefinitionResult',
    'AwaitableGetApplianceDefinitionResult',
    'get_appliance_definition',
    'get_appliance_definition_output',
]

warnings.warn("""Version 2016-09-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetApplianceDefinitionResult:
    """
    Information about appliance definition.
    """
    def __init__(__self__, artifacts=None, authorizations=None, description=None, display_name=None, id=None, identity=None, location=None, lock_level=None, managed_by=None, name=None, package_file_uri=None, sku=None, tags=None, type=None):
        if artifacts and not isinstance(artifacts, list):
            raise TypeError("Expected argument 'artifacts' to be a list")
        pulumi.set(__self__, "artifacts", artifacts)
        if authorizations and not isinstance(authorizations, list):
            raise TypeError("Expected argument 'authorizations' to be a list")
        pulumi.set(__self__, "authorizations", authorizations)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if lock_level and not isinstance(lock_level, str):
            raise TypeError("Expected argument 'lock_level' to be a str")
        pulumi.set(__self__, "lock_level", lock_level)
        if managed_by and not isinstance(managed_by, str):
            raise TypeError("Expected argument 'managed_by' to be a str")
        pulumi.set(__self__, "managed_by", managed_by)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if package_file_uri and not isinstance(package_file_uri, str):
            raise TypeError("Expected argument 'package_file_uri' to be a str")
        pulumi.set(__self__, "package_file_uri", package_file_uri)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def artifacts(self) -> Optional[Sequence['outputs.ApplianceArtifactResponse']]:
        """
        The collection of appliance artifacts. The portal will use the files specified as artifacts to construct the user experience of creating an appliance from an appliance definition.
        """
        return pulumi.get(self, "artifacts")

    @property
    @pulumi.getter
    def authorizations(self) -> Sequence['outputs.ApplianceProviderAuthorizationResponse']:
        """
        The appliance provider authorizations.
        """
        return pulumi.get(self, "authorizations")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The appliance definition description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The appliance definition display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityResponse']:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="lockLevel")
    def lock_level(self) -> str:
        """
        The appliance lock level.
        """
        return pulumi.get(self, "lock_level")

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[str]:
        """
        ID of the resource that manages this resource.
        """
        return pulumi.get(self, "managed_by")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="packageFileUri")
    def package_file_uri(self) -> str:
        """
        The appliance definition package file Uri.
        """
        return pulumi.get(self, "package_file_uri")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The SKU of the resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetApplianceDefinitionResult(GetApplianceDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplianceDefinitionResult(
            artifacts=self.artifacts,
            authorizations=self.authorizations,
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            identity=self.identity,
            location=self.location,
            lock_level=self.lock_level,
            managed_by=self.managed_by,
            name=self.name,
            package_file_uri=self.package_file_uri,
            sku=self.sku,
            tags=self.tags,
            type=self.type)


def get_appliance_definition(appliance_definition_name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplianceDefinitionResult:
    """
    Information about appliance definition.


    :param str appliance_definition_name: The name of the appliance definition.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    pulumi.log.warn("""get_appliance_definition is deprecated: Version 2016-09-01-preview will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['applianceDefinitionName'] = appliance_definition_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:solutions/v20160901preview:getApplianceDefinition', __args__, opts=opts, typ=GetApplianceDefinitionResult).value

    return AwaitableGetApplianceDefinitionResult(
        artifacts=__ret__.artifacts,
        authorizations=__ret__.authorizations,
        description=__ret__.description,
        display_name=__ret__.display_name,
        id=__ret__.id,
        identity=__ret__.identity,
        location=__ret__.location,
        lock_level=__ret__.lock_level,
        managed_by=__ret__.managed_by,
        name=__ret__.name,
        package_file_uri=__ret__.package_file_uri,
        sku=__ret__.sku,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_appliance_definition)
def get_appliance_definition_output(appliance_definition_name: Optional[pulumi.Input[str]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplianceDefinitionResult]:
    """
    Information about appliance definition.


    :param str appliance_definition_name: The name of the appliance definition.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    pulumi.log.warn("""get_appliance_definition is deprecated: Version 2016-09-01-preview will be removed in v2 of the provider.""")
    ...
