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
    'GetSupportPlanTypeResult',
    'AwaitableGetSupportPlanTypeResult',
    'get_support_plan_type',
    'get_support_plan_type_output',
]

@pulumi.output_type
class GetSupportPlanTypeResult:
    """
    The status of the Canonical support plan.
    """
    def __init__(__self__, id=None, name=None, provisioning_state=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the ARM resource, e.g. "/subscriptions/{id}/providers/Microsoft.Addons/supportProvider/{supportProviderName}/supportPlanTypes/{planTypeName}".
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Canonical support plan, i.e. "essential", "standard" or "advanced".
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Microsoft.Addons/supportProvider
        """
        return pulumi.get(self, "type")


class AwaitableGetSupportPlanTypeResult(GetSupportPlanTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSupportPlanTypeResult(
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            type=self.type)


def get_support_plan_type(plan_type_name: Optional[str] = None,
                          provider_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSupportPlanTypeResult:
    """
    The status of the Canonical support plan.


    :param str plan_type_name: The Canonical support plan type.
    :param str provider_name: The support plan type. For now the only valid type is "canonical".
    """
    __args__ = dict()
    __args__['planTypeName'] = plan_type_name
    __args__['providerName'] = provider_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:addons/v20180301:getSupportPlanType', __args__, opts=opts, typ=GetSupportPlanTypeResult).value

    return AwaitableGetSupportPlanTypeResult(
        id=__ret__.id,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        type=__ret__.type)


@_utilities.lift_output_func(get_support_plan_type)
def get_support_plan_type_output(plan_type_name: Optional[pulumi.Input[str]] = None,
                                 provider_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSupportPlanTypeResult]:
    """
    The status of the Canonical support plan.


    :param str plan_type_name: The Canonical support plan type.
    :param str provider_name: The support plan type. For now the only valid type is "canonical".
    """
    ...
