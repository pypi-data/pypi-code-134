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
    'ListManagedClusterUserCredentialsResult',
    'AwaitableListManagedClusterUserCredentialsResult',
    'list_managed_cluster_user_credentials',
    'list_managed_cluster_user_credentials_output',
]

@pulumi.output_type
class ListManagedClusterUserCredentialsResult:
    """
    The list of credential result response.
    """
    def __init__(__self__, kubeconfigs=None):
        if kubeconfigs and not isinstance(kubeconfigs, list):
            raise TypeError("Expected argument 'kubeconfigs' to be a list")
        pulumi.set(__self__, "kubeconfigs", kubeconfigs)

    @property
    @pulumi.getter
    def kubeconfigs(self) -> Sequence['outputs.CredentialResultResponse']:
        """
        Base64-encoded Kubernetes configuration file.
        """
        return pulumi.get(self, "kubeconfigs")


class AwaitableListManagedClusterUserCredentialsResult(ListManagedClusterUserCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListManagedClusterUserCredentialsResult(
            kubeconfigs=self.kubeconfigs)


def list_managed_cluster_user_credentials(resource_group_name: Optional[str] = None,
                                          resource_name: Optional[str] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListManagedClusterUserCredentialsResult:
    """
    The list of credential result response.


    :param str resource_group_name: The name of the resource group.
    :param str resource_name: The name of the managed cluster resource.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerservice/v20200101:listManagedClusterUserCredentials', __args__, opts=opts, typ=ListManagedClusterUserCredentialsResult).value

    return AwaitableListManagedClusterUserCredentialsResult(
        kubeconfigs=__ret__.kubeconfigs)


@_utilities.lift_output_func(list_managed_cluster_user_credentials)
def list_managed_cluster_user_credentials_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                 resource_name: Optional[pulumi.Input[str]] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListManagedClusterUserCredentialsResult]:
    """
    The list of credential result response.


    :param str resource_group_name: The name of the resource group.
    :param str resource_name: The name of the managed cluster resource.
    """
    ...
