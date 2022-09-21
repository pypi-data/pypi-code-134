# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'ListConnectionConsentLinksResult',
    'AwaitableListConnectionConsentLinksResult',
    'list_connection_consent_links',
    'list_connection_consent_links_output',
]

@pulumi.output_type
class ListConnectionConsentLinksResult:
    """
    Collection of consent links
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.ConsentLinkDefinitionResponse']]:
        """
        Collection of resources
        """
        return pulumi.get(self, "value")


class AwaitableListConnectionConsentLinksResult(ListConnectionConsentLinksResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListConnectionConsentLinksResult(
            value=self.value)


def list_connection_consent_links(connection_name: Optional[str] = None,
                                  parameters: Optional[Sequence[pulumi.InputType['ConsentLinkParameterDefinition']]] = None,
                                  resource_group_name: Optional[str] = None,
                                  subscription_id: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListConnectionConsentLinksResult:
    """
    Collection of consent links
    API Version: 2016-06-01.


    :param str connection_name: Connection name
    :param Sequence[pulumi.InputType['ConsentLinkParameterDefinition']] parameters: Collection of resources
    :param str resource_group_name: The resource group
    :param str subscription_id: Subscription Id
    """
    __args__ = dict()
    __args__['connectionName'] = connection_name
    __args__['parameters'] = parameters
    __args__['resourceGroupName'] = resource_group_name
    __args__['subscriptionId'] = subscription_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web:listConnectionConsentLinks', __args__, opts=opts, typ=ListConnectionConsentLinksResult).value

    return AwaitableListConnectionConsentLinksResult(
        value=__ret__.value)


@_utilities.lift_output_func(list_connection_consent_links)
def list_connection_consent_links_output(connection_name: Optional[pulumi.Input[str]] = None,
                                         parameters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['ConsentLinkParameterDefinition']]]]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         subscription_id: Optional[pulumi.Input[Optional[str]]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListConnectionConsentLinksResult]:
    """
    Collection of consent links
    API Version: 2016-06-01.


    :param str connection_name: Connection name
    :param Sequence[pulumi.InputType['ConsentLinkParameterDefinition']] parameters: Collection of resources
    :param str resource_group_name: The resource group
    :param str subscription_id: Subscription Id
    """
    ...
