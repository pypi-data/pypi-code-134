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
from ._enums import *
from ._inputs import *

__all__ = ['PolicyAssignmentArgs', 'PolicyAssignment']

@pulumi.input_type
class PolicyAssignmentArgs:
    def __init__(__self__, *,
                 scope: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 not_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 parameters: Optional[Any] = None,
                 policy_assignment_name: Optional[pulumi.Input[str]] = None,
                 policy_definition_id: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['PolicySkuArgs']] = None):
        """
        The set of arguments for constructing a PolicyAssignment resource.
        :param pulumi.Input[str] scope: The scope for the policy assignment.
        :param pulumi.Input[str] description: This message will be part of response in case of policy violation.
        :param pulumi.Input[str] display_name: The display name of the policy assignment.
        :param pulumi.Input['IdentityArgs'] identity: The managed identity associated with the policy assignment.
        :param pulumi.Input[str] location: The location of the policy assignment. Only required when utilizing managed identity.
        :param Any metadata: The policy assignment metadata.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] not_scopes: The policy's excluded scopes.
        :param Any parameters: Required if a parameter is used in policy rule.
        :param pulumi.Input[str] policy_assignment_name: The name of the policy assignment.
        :param pulumi.Input[str] policy_definition_id: The ID of the policy definition or policy set definition being assigned.
        :param pulumi.Input['PolicySkuArgs'] sku: The policy sku. This property is optional, obsolete, and will be ignored.
        """
        pulumi.set(__self__, "scope", scope)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if not_scopes is not None:
            pulumi.set(__self__, "not_scopes", not_scopes)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if policy_assignment_name is not None:
            pulumi.set(__self__, "policy_assignment_name", policy_assignment_name)
        if policy_definition_id is not None:
            pulumi.set(__self__, "policy_definition_id", policy_definition_id)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The scope for the policy assignment.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        This message will be part of response in case of policy violation.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the policy assignment.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        The managed identity associated with the policy assignment.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the policy assignment. Only required when utilizing managed identity.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The policy assignment metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[Any]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="notScopes")
    def not_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The policy's excluded scopes.
        """
        return pulumi.get(self, "not_scopes")

    @not_scopes.setter
    def not_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "not_scopes", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Any]:
        """
        Required if a parameter is used in policy rule.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[Any]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="policyAssignmentName")
    def policy_assignment_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy assignment.
        """
        return pulumi.get(self, "policy_assignment_name")

    @policy_assignment_name.setter
    def policy_assignment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_assignment_name", value)

    @property
    @pulumi.getter(name="policyDefinitionId")
    def policy_definition_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the policy definition or policy set definition being assigned.
        """
        return pulumi.get(self, "policy_definition_id")

    @policy_definition_id.setter
    def policy_definition_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_definition_id", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['PolicySkuArgs']]:
        """
        The policy sku. This property is optional, obsolete, and will be ignored.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['PolicySkuArgs']]):
        pulumi.set(self, "sku", value)


class PolicyAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 not_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 parameters: Optional[Any] = None,
                 policy_assignment_name: Optional[pulumi.Input[str]] = None,
                 policy_definition_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['PolicySkuArgs']]] = None,
                 __props__=None):
        """
        The policy assignment.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: This message will be part of response in case of policy violation.
        :param pulumi.Input[str] display_name: The display name of the policy assignment.
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] identity: The managed identity associated with the policy assignment.
        :param pulumi.Input[str] location: The location of the policy assignment. Only required when utilizing managed identity.
        :param Any metadata: The policy assignment metadata.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] not_scopes: The policy's excluded scopes.
        :param Any parameters: Required if a parameter is used in policy rule.
        :param pulumi.Input[str] policy_assignment_name: The name of the policy assignment.
        :param pulumi.Input[str] policy_definition_id: The ID of the policy definition or policy set definition being assigned.
        :param pulumi.Input[str] scope: The scope for the policy assignment.
        :param pulumi.Input[pulumi.InputType['PolicySkuArgs']] sku: The policy sku. This property is optional, obsolete, and will be ignored.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The policy assignment.

        :param str resource_name: The name of the resource.
        :param PolicyAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 not_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 parameters: Optional[Any] = None,
                 policy_assignment_name: Optional[pulumi.Input[str]] = None,
                 policy_definition_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['PolicySkuArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PolicyAssignmentArgs.__new__(PolicyAssignmentArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["not_scopes"] = not_scopes
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["policy_assignment_name"] = policy_assignment_name
            __props__.__dict__["policy_definition_id"] = policy_definition_id
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["sku"] = sku
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:authorization:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20151001preview:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20160401:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20161201:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20170601preview:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20180301:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20190101:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20190601:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20190901:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20200301:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20200901:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20210601:PolicyAssignment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PolicyAssignment, __self__).__init__(
            'azure-native:authorization/v20180501:PolicyAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PolicyAssignment':
        """
        Get an existing PolicyAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PolicyAssignmentArgs.__new__(PolicyAssignmentArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["not_scopes"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["policy_definition_id"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["type"] = None
        return PolicyAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        This message will be part of response in case of policy violation.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of the policy assignment.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        The managed identity associated with the policy assignment.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the policy assignment. Only required when utilizing managed identity.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        """
        The policy assignment metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the policy assignment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notScopes")
    def not_scopes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The policy's excluded scopes.
        """
        return pulumi.get(self, "not_scopes")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Any]]:
        """
        Required if a parameter is used in policy rule.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="policyDefinitionId")
    def policy_definition_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the policy definition or policy set definition being assigned.
        """
        return pulumi.get(self, "policy_definition_id")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        The scope for the policy assignment.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.PolicySkuResponse']]:
        """
        The policy sku. This property is optional, obsolete, and will be ignored.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the policy assignment.
        """
        return pulumi.get(self, "type")

