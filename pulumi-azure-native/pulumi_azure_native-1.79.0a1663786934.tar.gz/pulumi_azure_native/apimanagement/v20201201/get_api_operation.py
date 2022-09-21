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
    'GetApiOperationResult',
    'AwaitableGetApiOperationResult',
    'get_api_operation',
    'get_api_operation_output',
]

@pulumi.output_type
class GetApiOperationResult:
    """
    Api Operation details.
    """
    def __init__(__self__, description=None, display_name=None, id=None, method=None, name=None, policies=None, request=None, responses=None, template_parameters=None, type=None, url_template=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if method and not isinstance(method, str):
            raise TypeError("Expected argument 'method' to be a str")
        pulumi.set(__self__, "method", method)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if policies and not isinstance(policies, str):
            raise TypeError("Expected argument 'policies' to be a str")
        pulumi.set(__self__, "policies", policies)
        if request and not isinstance(request, dict):
            raise TypeError("Expected argument 'request' to be a dict")
        pulumi.set(__self__, "request", request)
        if responses and not isinstance(responses, list):
            raise TypeError("Expected argument 'responses' to be a list")
        pulumi.set(__self__, "responses", responses)
        if template_parameters and not isinstance(template_parameters, list):
            raise TypeError("Expected argument 'template_parameters' to be a list")
        pulumi.set(__self__, "template_parameters", template_parameters)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if url_template and not isinstance(url_template, str):
            raise TypeError("Expected argument 'url_template' to be a str")
        pulumi.set(__self__, "url_template", url_template)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the operation. May include HTML formatting tags.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Operation Name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def method(self) -> str:
        """
        A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them.
        """
        return pulumi.get(self, "method")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def policies(self) -> Optional[str]:
        """
        Operation Policies
        """
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter
    def request(self) -> Optional['outputs.RequestContractResponse']:
        """
        An entity containing request details.
        """
        return pulumi.get(self, "request")

    @property
    @pulumi.getter
    def responses(self) -> Optional[Sequence['outputs.ResponseContractResponse']]:
        """
        Array of Operation responses.
        """
        return pulumi.get(self, "responses")

    @property
    @pulumi.getter(name="templateParameters")
    def template_parameters(self) -> Optional[Sequence['outputs.ParameterContractResponse']]:
        """
        Collection of URL template parameters.
        """
        return pulumi.get(self, "template_parameters")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="urlTemplate")
    def url_template(self) -> str:
        """
        Relative URL template identifying the target resource for this operation. May include parameters. Example: /customers/{cid}/orders/{oid}/?date={date}
        """
        return pulumi.get(self, "url_template")


class AwaitableGetApiOperationResult(GetApiOperationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiOperationResult(
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            method=self.method,
            name=self.name,
            policies=self.policies,
            request=self.request,
            responses=self.responses,
            template_parameters=self.template_parameters,
            type=self.type,
            url_template=self.url_template)


def get_api_operation(api_id: Optional[str] = None,
                      operation_id: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      service_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiOperationResult:
    """
    Api Operation details.


    :param str api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    :param str operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['operationId'] = operation_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20201201:getApiOperation', __args__, opts=opts, typ=GetApiOperationResult).value

    return AwaitableGetApiOperationResult(
        description=__ret__.description,
        display_name=__ret__.display_name,
        id=__ret__.id,
        method=__ret__.method,
        name=__ret__.name,
        policies=__ret__.policies,
        request=__ret__.request,
        responses=__ret__.responses,
        template_parameters=__ret__.template_parameters,
        type=__ret__.type,
        url_template=__ret__.url_template)


@_utilities.lift_output_func(get_api_operation)
def get_api_operation_output(api_id: Optional[pulumi.Input[str]] = None,
                             operation_id: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             service_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiOperationResult]:
    """
    Api Operation details.


    :param str api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    :param str operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    ...
