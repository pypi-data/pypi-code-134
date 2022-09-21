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
    'ListUpgradableVersionDetailsResult',
    'AwaitableListUpgradableVersionDetailsResult',
    'list_upgradable_version_details',
    'list_upgradable_version_details_output',
]

@pulumi.output_type
class ListUpgradableVersionDetailsResult:
    """
    Stack Versions that this version can upgrade to
    """
    def __init__(__self__, current_version=None, upgradable_versions=None):
        if current_version and not isinstance(current_version, str):
            raise TypeError("Expected argument 'current_version' to be a str")
        pulumi.set(__self__, "current_version", current_version)
        if upgradable_versions and not isinstance(upgradable_versions, list):
            raise TypeError("Expected argument 'upgradable_versions' to be a list")
        pulumi.set(__self__, "upgradable_versions", upgradable_versions)

    @property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> Optional[str]:
        """
        Current version of the elastic monitor
        """
        return pulumi.get(self, "current_version")

    @property
    @pulumi.getter(name="upgradableVersions")
    def upgradable_versions(self) -> Optional[Sequence[str]]:
        """
        Stack Versions that this version can upgrade to
        """
        return pulumi.get(self, "upgradable_versions")


class AwaitableListUpgradableVersionDetailsResult(ListUpgradableVersionDetailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListUpgradableVersionDetailsResult(
            current_version=self.current_version,
            upgradable_versions=self.upgradable_versions)


def list_upgradable_version_details(monitor_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListUpgradableVersionDetailsResult:
    """
    Stack Versions that this version can upgrade to


    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group to which the Elastic resource belongs.
    """
    __args__ = dict()
    __args__['monitorName'] = monitor_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:elastic/v20211001preview:listUpgradableVersionDetails', __args__, opts=opts, typ=ListUpgradableVersionDetailsResult).value

    return AwaitableListUpgradableVersionDetailsResult(
        current_version=__ret__.current_version,
        upgradable_versions=__ret__.upgradable_versions)


@_utilities.lift_output_func(list_upgradable_version_details)
def list_upgradable_version_details_output(monitor_name: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListUpgradableVersionDetailsResult]:
    """
    Stack Versions that this version can upgrade to


    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group to which the Elastic resource belongs.
    """
    ...
