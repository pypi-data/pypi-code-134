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
    'ListConnectionKeysResult',
    'AwaitableListConnectionKeysResult',
    'list_connection_keys',
    'list_connection_keys_output',
]

@pulumi.output_type
class ListConnectionKeysResult:
    def __init__(__self__, connection_key=None, parameter_values=None):
        if connection_key and not isinstance(connection_key, str):
            raise TypeError("Expected argument 'connection_key' to be a str")
        pulumi.set(__self__, "connection_key", connection_key)
        if parameter_values and not isinstance(parameter_values, dict):
            raise TypeError("Expected argument 'parameter_values' to be a dict")
        pulumi.set(__self__, "parameter_values", parameter_values)

    @property
    @pulumi.getter(name="connectionKey")
    def connection_key(self) -> Optional[str]:
        """
        Connection Key
        """
        return pulumi.get(self, "connection_key")

    @property
    @pulumi.getter(name="parameterValues")
    def parameter_values(self) -> Optional[Mapping[str, Any]]:
        """
        Tokens/Claim
        """
        return pulumi.get(self, "parameter_values")


class AwaitableListConnectionKeysResult(ListConnectionKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListConnectionKeysResult(
            connection_key=self.connection_key,
            parameter_values=self.parameter_values)


def list_connection_keys(connection_name: Optional[str] = None,
                         id: Optional[str] = None,
                         kind: Optional[str] = None,
                         location: Optional[str] = None,
                         name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         tags: Optional[Mapping[str, str]] = None,
                         type: Optional[str] = None,
                         validity_time_span: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListConnectionKeysResult:
    """
    Use this data source to access information about an existing resource.

    :param str connection_name: The connection name.
    :param str id: Resource Id
    :param str kind: Kind of resource
    :param str location: Resource Location
    :param str name: Resource Name
    :param str resource_group_name: The resource group name.
    :param Mapping[str, str] tags: Resource tags
    :param str type: Resource type
    :param str validity_time_span: time span for how long the keys will be valid
    """
    __args__ = dict()
    __args__['connectionName'] = connection_name
    __args__['id'] = id
    __args__['kind'] = kind
    __args__['location'] = location
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['tags'] = tags
    __args__['type'] = type
    __args__['validityTimeSpan'] = validity_time_span
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20150801preview:listConnectionKeys', __args__, opts=opts, typ=ListConnectionKeysResult).value

    return AwaitableListConnectionKeysResult(
        connection_key=__ret__.connection_key,
        parameter_values=__ret__.parameter_values)


@_utilities.lift_output_func(list_connection_keys)
def list_connection_keys_output(connection_name: Optional[pulumi.Input[str]] = None,
                                id: Optional[pulumi.Input[Optional[str]]] = None,
                                kind: Optional[pulumi.Input[Optional[str]]] = None,
                                location: Optional[pulumi.Input[Optional[str]]] = None,
                                name: Optional[pulumi.Input[Optional[str]]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                type: Optional[pulumi.Input[Optional[str]]] = None,
                                validity_time_span: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListConnectionKeysResult]:
    """
    Use this data source to access information about an existing resource.

    :param str connection_name: The connection name.
    :param str id: Resource Id
    :param str kind: Kind of resource
    :param str location: Resource Location
    :param str name: Resource Name
    :param str resource_group_name: The resource group name.
    :param Mapping[str, str] tags: Resource tags
    :param str type: Resource type
    :param str validity_time_span: time span for how long the keys will be valid
    """
    ...
