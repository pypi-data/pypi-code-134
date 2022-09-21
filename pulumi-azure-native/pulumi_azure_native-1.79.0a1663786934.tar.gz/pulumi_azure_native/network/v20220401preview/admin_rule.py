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

__all__ = ['AdminRuleArgs', 'AdminRule']

@pulumi.input_type
class AdminRuleArgs:
    def __init__(__self__, *,
                 configuration_name: pulumi.Input[str],
                 kind: pulumi.Input[Union[str, 'AdminRuleKind']],
                 network_manager_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 rule_collection_name: pulumi.Input[str],
                 rule_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AdminRule resource.
        :param pulumi.Input[str] configuration_name: The name of the network manager Security Configuration.
        :param pulumi.Input[Union[str, 'AdminRuleKind']] kind: Whether the rule is custom or default.
        :param pulumi.Input[str] network_manager_name: The name of the network manager.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] rule_collection_name: The name of the network manager security Configuration rule collection.
        :param pulumi.Input[str] rule_name: The name of the rule.
        """
        pulumi.set(__self__, "configuration_name", configuration_name)
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "network_manager_name", network_manager_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "rule_collection_name", rule_collection_name)
        if rule_name is not None:
            pulumi.set(__self__, "rule_name", rule_name)

    @property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> pulumi.Input[str]:
        """
        The name of the network manager Security Configuration.
        """
        return pulumi.get(self, "configuration_name")

    @configuration_name.setter
    def configuration_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "configuration_name", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[Union[str, 'AdminRuleKind']]:
        """
        Whether the rule is custom or default.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[Union[str, 'AdminRuleKind']]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="networkManagerName")
    def network_manager_name(self) -> pulumi.Input[str]:
        """
        The name of the network manager.
        """
        return pulumi.get(self, "network_manager_name")

    @network_manager_name.setter
    def network_manager_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_manager_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="ruleCollectionName")
    def rule_collection_name(self) -> pulumi.Input[str]:
        """
        The name of the network manager security Configuration rule collection.
        """
        return pulumi.get(self, "rule_collection_name")

    @rule_collection_name.setter
    def rule_collection_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "rule_collection_name", value)

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the rule.
        """
        return pulumi.get(self, "rule_name")

    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_name", value)


warnings.warn("""Please use one of the variants: AdminRule, DefaultAdminRule.""", DeprecationWarning)


class AdminRule(pulumi.CustomResource):
    warnings.warn("""Please use one of the variants: AdminRule, DefaultAdminRule.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'AdminRuleKind']]] = None,
                 network_manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_collection_name: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Network base admin rule.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] configuration_name: The name of the network manager Security Configuration.
        :param pulumi.Input[Union[str, 'AdminRuleKind']] kind: Whether the rule is custom or default.
        :param pulumi.Input[str] network_manager_name: The name of the network manager.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] rule_collection_name: The name of the network manager security Configuration rule collection.
        :param pulumi.Input[str] rule_name: The name of the rule.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AdminRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Network base admin rule.

        :param str resource_name: The name of the resource.
        :param AdminRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AdminRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'AdminRuleKind']]] = None,
                 network_manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_collection_name: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""AdminRule is deprecated: Please use one of the variants: AdminRule, DefaultAdminRule.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AdminRuleArgs.__new__(AdminRuleArgs)

            if configuration_name is None and not opts.urn:
                raise TypeError("Missing required property 'configuration_name'")
            __props__.__dict__["configuration_name"] = configuration_name
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = kind
            if network_manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_manager_name'")
            __props__.__dict__["network_manager_name"] = network_manager_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if rule_collection_name is None and not opts.urn:
                raise TypeError("Missing required property 'rule_collection_name'")
            __props__.__dict__["rule_collection_name"] = rule_collection_name
            __props__.__dict__["rule_name"] = rule_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:AdminRule"), pulumi.Alias(type_="azure-native:network/v20210201preview:AdminRule"), pulumi.Alias(type_="azure-native:network/v20210501preview:AdminRule"), pulumi.Alias(type_="azure-native:network/v20220101:AdminRule"), pulumi.Alias(type_="azure-native:network/v20220201preview:AdminRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AdminRule, __self__).__init__(
            'azure-native:network/v20220401preview:AdminRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AdminRule':
        """
        Get an existing AdminRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AdminRuleArgs.__new__(AdminRuleArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return AdminRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Whether the rule is custom or default.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata related to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

