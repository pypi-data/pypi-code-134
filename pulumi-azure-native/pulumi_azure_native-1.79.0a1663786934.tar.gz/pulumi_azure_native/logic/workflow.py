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
from ._enums import *
from ._inputs import *

__all__ = ['WorkflowArgs', 'Workflow']

@pulumi.input_type
class WorkflowArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 access_control: Optional[pulumi.Input['FlowAccessControlConfigurationArgs']] = None,
                 definition: Optional[Any] = None,
                 endpoints_configuration: Optional[pulumi.Input['FlowEndpointsConfigurationArgs']] = None,
                 identity: Optional[pulumi.Input['ManagedServiceIdentityArgs']] = None,
                 integration_account: Optional[pulumi.Input['ResourceReferenceArgs']] = None,
                 integration_service_environment: Optional[pulumi.Input['ResourceReferenceArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input['WorkflowParameterArgs']]]] = None,
                 state: Optional[pulumi.Input[Union[str, 'WorkflowState']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workflow_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Workflow resource.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input['FlowAccessControlConfigurationArgs'] access_control: The access control configuration.
        :param Any definition: The definition.
        :param pulumi.Input['FlowEndpointsConfigurationArgs'] endpoints_configuration: The endpoints configuration.
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: Managed service identity properties.
        :param pulumi.Input['ResourceReferenceArgs'] integration_account: The integration account.
        :param pulumi.Input['ResourceReferenceArgs'] integration_service_environment: The integration service environment.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input['WorkflowParameterArgs']]] parameters: The parameters.
        :param pulumi.Input[Union[str, 'WorkflowState']] state: The state.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        :param pulumi.Input[str] workflow_name: The workflow name.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if access_control is not None:
            pulumi.set(__self__, "access_control", access_control)
        if definition is not None:
            pulumi.set(__self__, "definition", definition)
        if endpoints_configuration is not None:
            pulumi.set(__self__, "endpoints_configuration", endpoints_configuration)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if integration_account is not None:
            pulumi.set(__self__, "integration_account", integration_account)
        if integration_service_environment is not None:
            pulumi.set(__self__, "integration_service_environment", integration_service_environment)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if workflow_name is not None:
            pulumi.set(__self__, "workflow_name", workflow_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="accessControl")
    def access_control(self) -> Optional[pulumi.Input['FlowAccessControlConfigurationArgs']]:
        """
        The access control configuration.
        """
        return pulumi.get(self, "access_control")

    @access_control.setter
    def access_control(self, value: Optional[pulumi.Input['FlowAccessControlConfigurationArgs']]):
        pulumi.set(self, "access_control", value)

    @property
    @pulumi.getter
    def definition(self) -> Optional[Any]:
        """
        The definition.
        """
        return pulumi.get(self, "definition")

    @definition.setter
    def definition(self, value: Optional[Any]):
        pulumi.set(self, "definition", value)

    @property
    @pulumi.getter(name="endpointsConfiguration")
    def endpoints_configuration(self) -> Optional[pulumi.Input['FlowEndpointsConfigurationArgs']]:
        """
        The endpoints configuration.
        """
        return pulumi.get(self, "endpoints_configuration")

    @endpoints_configuration.setter
    def endpoints_configuration(self, value: Optional[pulumi.Input['FlowEndpointsConfigurationArgs']]):
        pulumi.set(self, "endpoints_configuration", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedServiceIdentityArgs']]:
        """
        Managed service identity properties.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="integrationAccount")
    def integration_account(self) -> Optional[pulumi.Input['ResourceReferenceArgs']]:
        """
        The integration account.
        """
        return pulumi.get(self, "integration_account")

    @integration_account.setter
    def integration_account(self, value: Optional[pulumi.Input['ResourceReferenceArgs']]):
        pulumi.set(self, "integration_account", value)

    @property
    @pulumi.getter(name="integrationServiceEnvironment")
    def integration_service_environment(self) -> Optional[pulumi.Input['ResourceReferenceArgs']]:
        """
        The integration service environment.
        """
        return pulumi.get(self, "integration_service_environment")

    @integration_service_environment.setter
    def integration_service_environment(self, value: Optional[pulumi.Input['ResourceReferenceArgs']]):
        pulumi.set(self, "integration_service_environment", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['WorkflowParameterArgs']]]]:
        """
        The parameters.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['WorkflowParameterArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[str, 'WorkflowState']]]:
        """
        The state.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[str, 'WorkflowState']]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="workflowName")
    def workflow_name(self) -> Optional[pulumi.Input[str]]:
        """
        The workflow name.
        """
        return pulumi.get(self, "workflow_name")

    @workflow_name.setter
    def workflow_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workflow_name", value)


class Workflow(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_control: Optional[pulumi.Input[pulumi.InputType['FlowAccessControlConfigurationArgs']]] = None,
                 definition: Optional[Any] = None,
                 endpoints_configuration: Optional[pulumi.Input[pulumi.InputType['FlowEndpointsConfigurationArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 integration_account: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 integration_service_environment: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['WorkflowParameterArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'WorkflowState']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workflow_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The workflow type.
        API Version: 2019-05-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['FlowAccessControlConfigurationArgs']] access_control: The access control configuration.
        :param Any definition: The definition.
        :param pulumi.Input[pulumi.InputType['FlowEndpointsConfigurationArgs']] endpoints_configuration: The endpoints configuration.
        :param pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']] identity: Managed service identity properties.
        :param pulumi.Input[pulumi.InputType['ResourceReferenceArgs']] integration_account: The integration account.
        :param pulumi.Input[pulumi.InputType['ResourceReferenceArgs']] integration_service_environment: The integration service environment.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['WorkflowParameterArgs']]]] parameters: The parameters.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Union[str, 'WorkflowState']] state: The state.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        :param pulumi.Input[str] workflow_name: The workflow name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkflowArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The workflow type.
        API Version: 2019-05-01.

        :param str resource_name: The name of the resource.
        :param WorkflowArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkflowArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_control: Optional[pulumi.Input[pulumi.InputType['FlowAccessControlConfigurationArgs']]] = None,
                 definition: Optional[Any] = None,
                 endpoints_configuration: Optional[pulumi.Input[pulumi.InputType['FlowEndpointsConfigurationArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 integration_account: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 integration_service_environment: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['WorkflowParameterArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'WorkflowState']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workflow_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkflowArgs.__new__(WorkflowArgs)

            __props__.__dict__["access_control"] = access_control
            __props__.__dict__["definition"] = definition
            __props__.__dict__["endpoints_configuration"] = endpoints_configuration
            __props__.__dict__["identity"] = identity
            __props__.__dict__["integration_account"] = integration_account
            __props__.__dict__["integration_service_environment"] = integration_service_environment
            __props__.__dict__["location"] = location
            __props__.__dict__["parameters"] = parameters
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["state"] = state
            __props__.__dict__["tags"] = tags
            __props__.__dict__["workflow_name"] = workflow_name
            __props__.__dict__["access_endpoint"] = None
            __props__.__dict__["changed_time"] = None
            __props__.__dict__["created_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["sku"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:logic/v20150201preview:Workflow"), pulumi.Alias(type_="azure-native:logic/v20160601:Workflow"), pulumi.Alias(type_="azure-native:logic/v20180701preview:Workflow"), pulumi.Alias(type_="azure-native:logic/v20190501:Workflow")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Workflow, __self__).__init__(
            'azure-native:logic:Workflow',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Workflow':
        """
        Get an existing Workflow resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkflowArgs.__new__(WorkflowArgs)

        __props__.__dict__["access_control"] = None
        __props__.__dict__["access_endpoint"] = None
        __props__.__dict__["changed_time"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["definition"] = None
        __props__.__dict__["endpoints_configuration"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["integration_account"] = None
        __props__.__dict__["integration_service_environment"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return Workflow(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessControl")
    def access_control(self) -> pulumi.Output[Optional['outputs.FlowAccessControlConfigurationResponse']]:
        """
        The access control configuration.
        """
        return pulumi.get(self, "access_control")

    @property
    @pulumi.getter(name="accessEndpoint")
    def access_endpoint(self) -> pulumi.Output[str]:
        """
        Gets the access endpoint.
        """
        return pulumi.get(self, "access_endpoint")

    @property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> pulumi.Output[str]:
        """
        Gets the changed time.
        """
        return pulumi.get(self, "changed_time")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        """
        Gets the created time.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Output[Optional[Any]]:
        """
        The definition.
        """
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter(name="endpointsConfiguration")
    def endpoints_configuration(self) -> pulumi.Output[Optional['outputs.FlowEndpointsConfigurationResponse']]:
        """
        The endpoints configuration.
        """
        return pulumi.get(self, "endpoints_configuration")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedServiceIdentityResponse']]:
        """
        Managed service identity properties.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="integrationAccount")
    def integration_account(self) -> pulumi.Output[Optional['outputs.ResourceReferenceResponse']]:
        """
        The integration account.
        """
        return pulumi.get(self, "integration_account")

    @property
    @pulumi.getter(name="integrationServiceEnvironment")
    def integration_service_environment(self) -> pulumi.Output[Optional['outputs.ResourceReferenceResponse']]:
        """
        The integration service environment.
        """
        return pulumi.get(self, "integration_service_environment")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Gets the resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.WorkflowParameterResponse']]]:
        """
        The parameters.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.SkuResponse']:
        """
        The sku.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        The state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Gets the version.
        """
        return pulumi.get(self, "version")

