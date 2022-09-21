# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['OutboundFirewallRuleArgs', 'OutboundFirewallRule']

@pulumi.input_type
class OutboundFirewallRuleArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 outbound_rule_fqdn: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OutboundFirewallRule resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        if outbound_rule_fqdn is not None:
            pulumi.set(__self__, "outbound_rule_fqdn", outbound_rule_fqdn)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="outboundRuleFqdn")
    def outbound_rule_fqdn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "outbound_rule_fqdn")

    @outbound_rule_fqdn.setter
    def outbound_rule_fqdn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "outbound_rule_fqdn", value)


class OutboundFirewallRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 outbound_rule_fqdn: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An Azure SQL DB Server Outbound Firewall Rule.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OutboundFirewallRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure SQL DB Server Outbound Firewall Rule.

        :param str resource_name: The name of the resource.
        :param OutboundFirewallRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OutboundFirewallRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 outbound_rule_fqdn: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OutboundFirewallRuleArgs.__new__(OutboundFirewallRuleArgs)

            __props__.__dict__["outbound_rule_fqdn"] = outbound_rule_fqdn
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:OutboundFirewallRule"), pulumi.Alias(type_="azure-native:sql/v20210201preview:OutboundFirewallRule"), pulumi.Alias(type_="azure-native:sql/v20210501preview:OutboundFirewallRule"), pulumi.Alias(type_="azure-native:sql/v20210801preview:OutboundFirewallRule"), pulumi.Alias(type_="azure-native:sql/v20211101preview:OutboundFirewallRule"), pulumi.Alias(type_="azure-native:sql/v20220201preview:OutboundFirewallRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(OutboundFirewallRule, __self__).__init__(
            'azure-native:sql/v20211101:OutboundFirewallRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OutboundFirewallRule':
        """
        Get an existing OutboundFirewallRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OutboundFirewallRuleArgs.__new__(OutboundFirewallRuleArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return OutboundFirewallRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The state of the outbound rule.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

