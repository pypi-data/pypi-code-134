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
    'GetWebAppSlotConfigurationNamesResult',
    'AwaitableGetWebAppSlotConfigurationNamesResult',
    'get_web_app_slot_configuration_names',
    'get_web_app_slot_configuration_names_output',
]

@pulumi.output_type
class GetWebAppSlotConfigurationNamesResult:
    """
    Slot Config names azure resource.
    """
    def __init__(__self__, app_setting_names=None, azure_storage_config_names=None, connection_string_names=None, id=None, kind=None, name=None, type=None):
        if app_setting_names and not isinstance(app_setting_names, list):
            raise TypeError("Expected argument 'app_setting_names' to be a list")
        pulumi.set(__self__, "app_setting_names", app_setting_names)
        if azure_storage_config_names and not isinstance(azure_storage_config_names, list):
            raise TypeError("Expected argument 'azure_storage_config_names' to be a list")
        pulumi.set(__self__, "azure_storage_config_names", azure_storage_config_names)
        if connection_string_names and not isinstance(connection_string_names, list):
            raise TypeError("Expected argument 'connection_string_names' to be a list")
        pulumi.set(__self__, "connection_string_names", connection_string_names)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="appSettingNames")
    def app_setting_names(self) -> Optional[Sequence[str]]:
        """
        List of application settings names.
        """
        return pulumi.get(self, "app_setting_names")

    @property
    @pulumi.getter(name="azureStorageConfigNames")
    def azure_storage_config_names(self) -> Optional[Sequence[str]]:
        """
        List of external Azure storage account identifiers.
        """
        return pulumi.get(self, "azure_storage_config_names")

    @property
    @pulumi.getter(name="connectionStringNames")
    def connection_string_names(self) -> Optional[Sequence[str]]:
        """
        List of connection string names.
        """
        return pulumi.get(self, "connection_string_names")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetWebAppSlotConfigurationNamesResult(GetWebAppSlotConfigurationNamesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebAppSlotConfigurationNamesResult(
            app_setting_names=self.app_setting_names,
            azure_storage_config_names=self.azure_storage_config_names,
            connection_string_names=self.connection_string_names,
            id=self.id,
            kind=self.kind,
            name=self.name,
            type=self.type)


def get_web_app_slot_configuration_names(name: Optional[str] = None,
                                         resource_group_name: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebAppSlotConfigurationNamesResult:
    """
    Slot Config names azure resource.


    :param str name: Name of the app.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20180201:getWebAppSlotConfigurationNames', __args__, opts=opts, typ=GetWebAppSlotConfigurationNamesResult).value

    return AwaitableGetWebAppSlotConfigurationNamesResult(
        app_setting_names=__ret__.app_setting_names,
        azure_storage_config_names=__ret__.azure_storage_config_names,
        connection_string_names=__ret__.connection_string_names,
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        type=__ret__.type)


@_utilities.lift_output_func(get_web_app_slot_configuration_names)
def get_web_app_slot_configuration_names_output(name: Optional[pulumi.Input[str]] = None,
                                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebAppSlotConfigurationNamesResult]:
    """
    Slot Config names azure resource.


    :param str name: Name of the app.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
