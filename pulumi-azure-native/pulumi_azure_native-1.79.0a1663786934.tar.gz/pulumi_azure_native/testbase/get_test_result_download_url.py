# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetTestResultDownloadURLResult',
    'AwaitableGetTestResultDownloadURLResult',
    'get_test_result_download_url',
    'get_test_result_download_url_output',
]

@pulumi.output_type
class GetTestResultDownloadURLResult:
    """
    The response of getting a download URL.
    """
    def __init__(__self__, download_url=None, expiration_time=None):
        if download_url and not isinstance(download_url, str):
            raise TypeError("Expected argument 'download_url' to be a str")
        pulumi.set(__self__, "download_url", download_url)
        if expiration_time and not isinstance(expiration_time, str):
            raise TypeError("Expected argument 'expiration_time' to be a str")
        pulumi.set(__self__, "expiration_time", expiration_time)

    @property
    @pulumi.getter(name="downloadUrl")
    def download_url(self) -> str:
        """
        The download URL.
        """
        return pulumi.get(self, "download_url")

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> str:
        """
        Expiry date of the download URL.
        """
        return pulumi.get(self, "expiration_time")


class AwaitableGetTestResultDownloadURLResult(GetTestResultDownloadURLResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTestResultDownloadURLResult(
            download_url=self.download_url,
            expiration_time=self.expiration_time)


def get_test_result_download_url(package_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 test_base_account_name: Optional[str] = None,
                                 test_result_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTestResultDownloadURLResult:
    """
    The response of getting a download URL.
    API Version: 2022-04-01-preview.


    :param str package_name: The resource name of the Test Base Package.
    :param str resource_group_name: The name of the resource group that contains the resource.
    :param str test_base_account_name: The resource name of the Test Base Account.
    :param str test_result_name: The Test Result Name. It equals to TestResult-{TestResultId} string.
    """
    __args__ = dict()
    __args__['packageName'] = package_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['testBaseAccountName'] = test_base_account_name
    __args__['testResultName'] = test_result_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:testbase:getTestResultDownloadURL', __args__, opts=opts, typ=GetTestResultDownloadURLResult).value

    return AwaitableGetTestResultDownloadURLResult(
        download_url=__ret__.download_url,
        expiration_time=__ret__.expiration_time)


@_utilities.lift_output_func(get_test_result_download_url)
def get_test_result_download_url_output(package_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        test_base_account_name: Optional[pulumi.Input[str]] = None,
                                        test_result_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTestResultDownloadURLResult]:
    """
    The response of getting a download URL.
    API Version: 2022-04-01-preview.


    :param str package_name: The resource name of the Test Base Package.
    :param str resource_group_name: The name of the resource group that contains the resource.
    :param str test_base_account_name: The resource name of the Test Base Account.
    :param str test_result_name: The Test Result Name. It equals to TestResult-{TestResultId} string.
    """
    ...
