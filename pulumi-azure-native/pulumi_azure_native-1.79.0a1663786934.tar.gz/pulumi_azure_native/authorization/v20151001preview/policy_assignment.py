# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['PolicyAssignmentArgs', 'PolicyAssignment']

@pulumi.input_type
class PolicyAssignmentArgs:
    def __init__(__self__, *,
                 scope: pulumi.Input[str],
                 display_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_assignment_name: Optional[pulumi.Input[str]] = None,
                 policy_definition_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PolicyAssignment resource.
        :param pulumi.Input[str] scope: The scope for the policy assignment.
        :param pulumi.Input[str] display_name: The display name of the policy assignment.
        :param pulumi.Input[str] id: The ID of the policy assignment.
        :param pulumi.Input[str] name: The name of the policy assignment.
        :param pulumi.Input[str] policy_assignment_name: The name of the policy assignment.
        :param pulumi.Input[str] policy_definition_id: The ID of the policy definition.
        :param pulumi.Input[str] type: The type of the policy assignment.
        """
        pulumi.set(__self__, "scope", scope)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy_assignment_name is not None:
            pulumi.set(__self__, "policy_assignment_name", policy_assignment_name)
        if policy_definition_id is not None:
            pulumi.set(__self__, "policy_definition_id", policy_definition_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

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
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the policy assignment.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy assignment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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
        The ID of the policy definition.
        """
        return pulumi.get(self, "policy_definition_id")

    @policy_definition_id.setter
    def policy_definition_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_definition_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the policy assignment.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


warnings.warn("""Version 2015-10-01-preview will be removed in v2 of the provider.""", DeprecationWarning)


class PolicyAssignment(pulumi.CustomResource):
    warnings.warn("""Version 2015-10-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_assignment_name: Optional[pulumi.Input[str]] = None,
                 policy_definition_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The policy assignment.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: The display name of the policy assignment.
        :param pulumi.Input[str] id: The ID of the policy assignment.
        :param pulumi.Input[str] name: The name of the policy assignment.
        :param pulumi.Input[str] policy_assignment_name: The name of the policy assignment.
        :param pulumi.Input[str] policy_definition_id: The ID of the policy definition.
        :param pulumi.Input[str] scope: The scope for the policy assignment.
        :param pulumi.Input[str] type: The type of the policy assignment.
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
                 display_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_assignment_name: Optional[pulumi.Input[str]] = None,
                 policy_definition_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""PolicyAssignment is deprecated: Version 2015-10-01-preview will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PolicyAssignmentArgs.__new__(PolicyAssignmentArgs)

            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["id"] = id
            __props__.__dict__["name"] = name
            __props__.__dict__["policy_assignment_name"] = policy_assignment_name
            __props__.__dict__["policy_definition_id"] = policy_definition_id
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["type"] = type
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:authorization:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20160401:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20161201:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20170601preview:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20180301:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20180501:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20190101:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20190601:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20190901:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20200301:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20200901:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20210601:PolicyAssignment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PolicyAssignment, __self__).__init__(
            'azure-native:authorization/v20151001preview:PolicyAssignment',
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

        __props__.__dict__["display_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["policy_definition_id"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["type"] = None
        return PolicyAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of the policy assignment.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the policy assignment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyDefinitionId")
    def policy_definition_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the policy definition.
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
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the policy assignment.
        """
        return pulumi.get(self, "type")

