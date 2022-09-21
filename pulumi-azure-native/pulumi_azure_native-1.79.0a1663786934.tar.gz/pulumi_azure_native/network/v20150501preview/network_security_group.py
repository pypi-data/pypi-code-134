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

__all__ = ['NetworkSecurityGroupArgs', 'NetworkSecurityGroup']

@pulumi.input_type
class NetworkSecurityGroupArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 default_security_rules: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityRuleArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]] = None,
                 network_security_group_name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 security_rules: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityRuleArgs']]]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NetworkSecurityGroup resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input['SecurityRuleArgs']]] default_security_rules: Gets or sets Default security rules of network security group
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]] network_interfaces: Gets collection of references to Network Interfaces
        :param pulumi.Input[str] network_security_group_name: The name of the network security group.
        :param pulumi.Input[str] provisioning_state: Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed
        :param pulumi.Input[str] resource_guid: Gets or sets resource guid property of the network security group resource
        :param pulumi.Input[Sequence[pulumi.Input['SecurityRuleArgs']]] security_rules: Gets or sets Security rules of network security group
        :param pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]] subnets: Gets collection of references to subnets
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if default_security_rules is not None:
            pulumi.set(__self__, "default_security_rules", default_security_rules)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network_interfaces is not None:
            pulumi.set(__self__, "network_interfaces", network_interfaces)
        if network_security_group_name is not None:
            pulumi.set(__self__, "network_security_group_name", network_security_group_name)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_guid is not None:
            pulumi.set(__self__, "resource_guid", resource_guid)
        if security_rules is not None:
            pulumi.set(__self__, "security_rules", security_rules)
        if subnets is not None:
            pulumi.set(__self__, "subnets", subnets)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="defaultSecurityRules")
    def default_security_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SecurityRuleArgs']]]]:
        """
        Gets or sets Default security rules of network security group
        """
        return pulumi.get(self, "default_security_rules")

    @default_security_rules.setter
    def default_security_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityRuleArgs']]]]):
        pulumi.set(self, "default_security_rules", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]]:
        """
        Gets collection of references to Network Interfaces
        """
        return pulumi.get(self, "network_interfaces")

    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]]):
        pulumi.set(self, "network_interfaces", value)

    @property
    @pulumi.getter(name="networkSecurityGroupName")
    def network_security_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the network security group.
        """
        return pulumi.get(self, "network_security_group_name")

    @network_security_group_name.setter
    def network_security_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_security_group_name", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets resource guid property of the network security group resource
        """
        return pulumi.get(self, "resource_guid")

    @resource_guid.setter
    def resource_guid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_guid", value)

    @property
    @pulumi.getter(name="securityRules")
    def security_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SecurityRuleArgs']]]]:
        """
        Gets or sets Security rules of network security group
        """
        return pulumi.get(self, "security_rules")

    @security_rules.setter
    def security_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityRuleArgs']]]]):
        pulumi.set(self, "security_rules", value)

    @property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]]:
        """
        Gets collection of references to subnets
        """
        return pulumi.get(self, "subnets")

    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]]):
        pulumi.set(self, "subnets", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""Version 2015-05-01-preview will be removed in v2 of the provider.""", DeprecationWarning)


class NetworkSecurityGroup(pulumi.CustomResource):
    warnings.warn("""Version 2015-05-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_security_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityRuleArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]]] = None,
                 network_security_group_name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 security_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityRuleArgs']]]]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        NetworkSecurityGroup resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityRuleArgs']]]] default_security_rules: Gets or sets Default security rules of network security group
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]] network_interfaces: Gets collection of references to Network Interfaces
        :param pulumi.Input[str] network_security_group_name: The name of the network security group.
        :param pulumi.Input[str] provisioning_state: Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_guid: Gets or sets resource guid property of the network security group resource
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityRuleArgs']]]] security_rules: Gets or sets Security rules of network security group
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]] subnets: Gets collection of references to subnets
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkSecurityGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        NetworkSecurityGroup resource

        :param str resource_name: The name of the resource.
        :param NetworkSecurityGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkSecurityGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_security_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityRuleArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]]] = None,
                 network_security_group_name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 security_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityRuleArgs']]]]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        pulumi.log.warn("""NetworkSecurityGroup is deprecated: Version 2015-05-01-preview will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkSecurityGroupArgs.__new__(NetworkSecurityGroupArgs)

            __props__.__dict__["default_security_rules"] = default_security_rules
            __props__.__dict__["location"] = location
            __props__.__dict__["network_interfaces"] = network_interfaces
            __props__.__dict__["network_security_group_name"] = network_security_group_name
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_guid"] = resource_guid
            __props__.__dict__["security_rules"] = security_rules
            __props__.__dict__["subnets"] = subnets
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20150615:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20160330:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20160601:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20160901:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20161201:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20170301:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20170601:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20170801:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20170901:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20171001:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20171101:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20180101:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20180201:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20180401:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20180601:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20180701:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20180801:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20181001:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20181101:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20181201:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20190201:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20190401:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20190601:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20190701:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20190801:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20190901:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20191101:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20191201:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20200301:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20200401:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20200501:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20200601:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20200701:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20200801:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20201101:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20210201:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20210301:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20210501:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20210801:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20220101:NetworkSecurityGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NetworkSecurityGroup, __self__).__init__(
            'azure-native:network/v20150501preview:NetworkSecurityGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkSecurityGroup':
        """
        Get an existing NetworkSecurityGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkSecurityGroupArgs.__new__(NetworkSecurityGroupArgs)

        __props__.__dict__["default_security_rules"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_interfaces"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["security_rules"] = None
        __props__.__dict__["subnets"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return NetworkSecurityGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultSecurityRules")
    def default_security_rules(self) -> pulumi.Output[Optional[Sequence['outputs.SecurityRuleResponse']]]:
        """
        Gets or sets Default security rules of network security group
        """
        return pulumi.get(self, "default_security_rules")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Gets a unique read-only string that changes whenever the resource is updated
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> pulumi.Output[Optional[Sequence['outputs.SubResourceResponse']]]:
        """
        Gets collection of references to Network Interfaces
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets resource guid property of the network security group resource
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter(name="securityRules")
    def security_rules(self) -> pulumi.Output[Optional[Sequence['outputs.SecurityRuleResponse']]]:
        """
        Gets or sets Security rules of network security group
        """
        return pulumi.get(self, "security_rules")

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Optional[Sequence['outputs.SubResourceResponse']]]:
        """
        Gets collection of references to subnets
        """
        return pulumi.get(self, "subnets")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

