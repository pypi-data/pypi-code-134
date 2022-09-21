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
from ._inputs import *

__all__ = ['ProfileArgs', 'Profile']

@pulumi.input_type
class ProfileArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 dns_config: Optional[pulumi.Input['DnsConfigArgs']] = None,
                 endpoints: Optional[pulumi.Input[Sequence[pulumi.Input['EndpointArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 monitor_config: Optional[pulumi.Input['MonitorConfigArgs']] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 profile_status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 traffic_routing_method: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Profile resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the Traffic Manager profile.
        :param pulumi.Input['DnsConfigArgs'] dns_config: Gets or sets the DNS settings of the Traffic Manager profile.
        :param pulumi.Input[Sequence[pulumi.Input['EndpointArgs']]] endpoints: Gets or sets the list of endpoints in the Traffic Manager profile.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input['MonitorConfigArgs'] monitor_config: Gets or sets the endpoint monitoring settings of the Traffic Manager profile.
        :param pulumi.Input[str] profile_name: The name of the Traffic Manager profile.
        :param pulumi.Input[str] profile_status: Gets or sets the status of the Traffic Manager profile.  Possible values are 'Enabled' and 'Disabled'.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] traffic_routing_method: Gets or sets the traffic routing method of the Traffic Manager profile.  Possible values are 'Performance', 'Weighted', or 'Priority'.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if dns_config is not None:
            pulumi.set(__self__, "dns_config", dns_config)
        if endpoints is not None:
            pulumi.set(__self__, "endpoints", endpoints)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if monitor_config is not None:
            pulumi.set(__self__, "monitor_config", monitor_config)
        if profile_name is not None:
            pulumi.set(__self__, "profile_name", profile_name)
        if profile_status is not None:
            pulumi.set(__self__, "profile_status", profile_status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if traffic_routing_method is not None:
            pulumi.set(__self__, "traffic_routing_method", traffic_routing_method)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group containing the Traffic Manager profile.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> Optional[pulumi.Input['DnsConfigArgs']]:
        """
        Gets or sets the DNS settings of the Traffic Manager profile.
        """
        return pulumi.get(self, "dns_config")

    @dns_config.setter
    def dns_config(self, value: Optional[pulumi.Input['DnsConfigArgs']]):
        pulumi.set(self, "dns_config", value)

    @property
    @pulumi.getter
    def endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EndpointArgs']]]]:
        """
        Gets or sets the list of endpoints in the Traffic Manager profile.
        """
        return pulumi.get(self, "endpoints")

    @endpoints.setter
    def endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EndpointArgs']]]]):
        pulumi.set(self, "endpoints", value)

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
    @pulumi.getter(name="monitorConfig")
    def monitor_config(self) -> Optional[pulumi.Input['MonitorConfigArgs']]:
        """
        Gets or sets the endpoint monitoring settings of the Traffic Manager profile.
        """
        return pulumi.get(self, "monitor_config")

    @monitor_config.setter
    def monitor_config(self, value: Optional[pulumi.Input['MonitorConfigArgs']]):
        pulumi.set(self, "monitor_config", value)

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Traffic Manager profile.
        """
        return pulumi.get(self, "profile_name")

    @profile_name.setter
    def profile_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "profile_name", value)

    @property
    @pulumi.getter(name="profileStatus")
    def profile_status(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the status of the Traffic Manager profile.  Possible values are 'Enabled' and 'Disabled'.
        """
        return pulumi.get(self, "profile_status")

    @profile_status.setter
    def profile_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "profile_status", value)

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

    @property
    @pulumi.getter(name="trafficRoutingMethod")
    def traffic_routing_method(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the traffic routing method of the Traffic Manager profile.  Possible values are 'Performance', 'Weighted', or 'Priority'.
        """
        return pulumi.get(self, "traffic_routing_method")

    @traffic_routing_method.setter
    def traffic_routing_method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "traffic_routing_method", value)


warnings.warn("""Version 2015-11-01 will be removed in v2 of the provider.""", DeprecationWarning)


class Profile(pulumi.CustomResource):
    warnings.warn("""Version 2015-11-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_config: Optional[pulumi.Input[pulumi.InputType['DnsConfigArgs']]] = None,
                 endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EndpointArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 monitor_config: Optional[pulumi.Input[pulumi.InputType['MonitorConfigArgs']]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 profile_status: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 traffic_routing_method: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Class representing a Traffic Manager profile.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DnsConfigArgs']] dns_config: Gets or sets the DNS settings of the Traffic Manager profile.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EndpointArgs']]]] endpoints: Gets or sets the list of endpoints in the Traffic Manager profile.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[pulumi.InputType['MonitorConfigArgs']] monitor_config: Gets or sets the endpoint monitoring settings of the Traffic Manager profile.
        :param pulumi.Input[str] profile_name: The name of the Traffic Manager profile.
        :param pulumi.Input[str] profile_status: Gets or sets the status of the Traffic Manager profile.  Possible values are 'Enabled' and 'Disabled'.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the Traffic Manager profile.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] traffic_routing_method: Gets or sets the traffic routing method of the Traffic Manager profile.  Possible values are 'Performance', 'Weighted', or 'Priority'.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Class representing a Traffic Manager profile.

        :param str resource_name: The name of the resource.
        :param ProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_config: Optional[pulumi.Input[pulumi.InputType['DnsConfigArgs']]] = None,
                 endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EndpointArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 monitor_config: Optional[pulumi.Input[pulumi.InputType['MonitorConfigArgs']]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 profile_status: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 traffic_routing_method: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Profile is deprecated: Version 2015-11-01 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProfileArgs.__new__(ProfileArgs)

            __props__.__dict__["dns_config"] = dns_config
            __props__.__dict__["endpoints"] = endpoints
            __props__.__dict__["location"] = location
            __props__.__dict__["monitor_config"] = monitor_config
            __props__.__dict__["profile_name"] = profile_name
            __props__.__dict__["profile_status"] = profile_status
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["traffic_routing_method"] = traffic_routing_method
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:Profile"), pulumi.Alias(type_="azure-native:network/v20170301:Profile"), pulumi.Alias(type_="azure-native:network/v20170501:Profile"), pulumi.Alias(type_="azure-native:network/v20180201:Profile"), pulumi.Alias(type_="azure-native:network/v20180301:Profile"), pulumi.Alias(type_="azure-native:network/v20180401:Profile"), pulumi.Alias(type_="azure-native:network/v20180801:Profile")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Profile, __self__).__init__(
            'azure-native:network/v20151101:Profile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Profile':
        """
        Get an existing Profile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProfileArgs.__new__(ProfileArgs)

        __props__.__dict__["dns_config"] = None
        __props__.__dict__["endpoints"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["monitor_config"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["profile_status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["traffic_routing_method"] = None
        __props__.__dict__["type"] = None
        return Profile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> pulumi.Output[Optional['outputs.DnsConfigResponse']]:
        """
        Gets or sets the DNS settings of the Traffic Manager profile.
        """
        return pulumi.get(self, "dns_config")

    @property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[Optional[Sequence['outputs.EndpointResponse']]]:
        """
        Gets or sets the list of endpoints in the Traffic Manager profile.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="monitorConfig")
    def monitor_config(self) -> pulumi.Output[Optional['outputs.MonitorConfigResponse']]:
        """
        Gets or sets the endpoint monitoring settings of the Traffic Manager profile.
        """
        return pulumi.get(self, "monitor_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="profileStatus")
    def profile_status(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the status of the Traffic Manager profile.  Possible values are 'Enabled' and 'Disabled'.
        """
        return pulumi.get(self, "profile_status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trafficRoutingMethod")
    def traffic_routing_method(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the traffic routing method of the Traffic Manager profile.  Possible values are 'Performance', 'Weighted', or 'Priority'.
        """
        return pulumi.get(self, "traffic_routing_method")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

