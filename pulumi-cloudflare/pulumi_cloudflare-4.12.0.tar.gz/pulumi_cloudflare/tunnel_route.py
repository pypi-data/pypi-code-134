# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['TunnelRouteArgs', 'TunnelRoute']

@pulumi.input_type
class TunnelRouteArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 network: pulumi.Input[str],
                 tunnel_id: pulumi.Input[str],
                 comment: Optional[pulumi.Input[str]] = None,
                 virtual_network_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TunnelRoute resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input[str] network: The IPv4 or IPv6 network that should use this tunnel route, in CIDR notation.
        :param pulumi.Input[str] tunnel_id: The ID of the tunnel that will service the tunnel route.
        :param pulumi.Input[str] comment: Description of the tunnel route.
        :param pulumi.Input[str] virtual_network_id: The ID of the virtual network for which this route is being added; uses the default virtual network of the account if none is provided.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "network", network)
        pulumi.set(__self__, "tunnel_id", tunnel_id)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if virtual_network_id is not None:
            pulumi.set(__self__, "virtual_network_id", virtual_network_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        The account identifier to target for the resource.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def network(self) -> pulumi.Input[str]:
        """
        The IPv4 or IPv6 network that should use this tunnel route, in CIDR notation.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: pulumi.Input[str]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter(name="tunnelId")
    def tunnel_id(self) -> pulumi.Input[str]:
        """
        The ID of the tunnel that will service the tunnel route.
        """
        return pulumi.get(self, "tunnel_id")

    @tunnel_id.setter
    def tunnel_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "tunnel_id", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the tunnel route.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the virtual network for which this route is being added; uses the default virtual network of the account if none is provided.
        """
        return pulumi.get(self, "virtual_network_id")

    @virtual_network_id.setter
    def virtual_network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_network_id", value)


@pulumi.input_type
class _TunnelRouteState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 tunnel_id: Optional[pulumi.Input[str]] = None,
                 virtual_network_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TunnelRoute resources.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input[str] comment: Description of the tunnel route.
        :param pulumi.Input[str] network: The IPv4 or IPv6 network that should use this tunnel route, in CIDR notation.
        :param pulumi.Input[str] tunnel_id: The ID of the tunnel that will service the tunnel route.
        :param pulumi.Input[str] virtual_network_id: The ID of the virtual network for which this route is being added; uses the default virtual network of the account if none is provided.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if network is not None:
            pulumi.set(__self__, "network", network)
        if tunnel_id is not None:
            pulumi.set(__self__, "tunnel_id", tunnel_id)
        if virtual_network_id is not None:
            pulumi.set(__self__, "virtual_network_id", virtual_network_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account identifier to target for the resource.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the tunnel route.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 or IPv6 network that should use this tunnel route, in CIDR notation.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter(name="tunnelId")
    def tunnel_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the tunnel that will service the tunnel route.
        """
        return pulumi.get(self, "tunnel_id")

    @tunnel_id.setter
    def tunnel_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tunnel_id", value)

    @property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the virtual network for which this route is being added; uses the default virtual network of the account if none is provided.
        """
        return pulumi.get(self, "virtual_network_id")

    @virtual_network_id.setter
    def virtual_network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_network_id", value)


class TunnelRoute(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 tunnel_id: Optional[pulumi.Input[str]] = None,
                 virtual_network_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource, that manages Cloudflare tunnel routes for Zero
        Trust. Tunnel routes are used to direct IP traffic through
        Cloudflare Tunnels.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # Tunnel route
        example_tunnel_route = cloudflare.TunnelRoute("exampleTunnelRoute",
            account_id="f037e56e89293a057740de681ac9abbe",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            network="192.0.2.24/32",
            comment="New tunnel route for documentation",
            virtual_network_id="bdc39a3c-3104-4c23-8ac0-9f455dda691a")
        # Tunnel with tunnel route
        tunnel = cloudflare.ArgoTunnel("tunnel",
            account_id="f037e56e89293a057740de681ac9abbe",
            name="my_tunnel",
            secret="AQIDBAUGBwgBAgMEBQYHCAECAwQFBgcIAQIDBAUGBwg=")
        example_index_tunnel_route_tunnel_route = cloudflare.TunnelRoute("exampleIndex/tunnelRouteTunnelRoute",
            account_id="f037e56e89293a057740de681ac9abbe",
            tunnel_id=tunnel.id,
            network="192.0.2.24/32",
            comment="New tunnel route for documentation",
            virtual_network_id="bdc39a3c-3104-4c23-8ac0-9f455dda691a")
        ```

        ## Import

        # Use account ID, network CIDR and virtual network ID.

        ```sh
         $ pulumi import cloudflare:index/tunnelRoute:TunnelRoute example <account_id/<network_cidr>/<virtual_network_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input[str] comment: Description of the tunnel route.
        :param pulumi.Input[str] network: The IPv4 or IPv6 network that should use this tunnel route, in CIDR notation.
        :param pulumi.Input[str] tunnel_id: The ID of the tunnel that will service the tunnel route.
        :param pulumi.Input[str] virtual_network_id: The ID of the virtual network for which this route is being added; uses the default virtual network of the account if none is provided.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TunnelRouteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource, that manages Cloudflare tunnel routes for Zero
        Trust. Tunnel routes are used to direct IP traffic through
        Cloudflare Tunnels.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # Tunnel route
        example_tunnel_route = cloudflare.TunnelRoute("exampleTunnelRoute",
            account_id="f037e56e89293a057740de681ac9abbe",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            network="192.0.2.24/32",
            comment="New tunnel route for documentation",
            virtual_network_id="bdc39a3c-3104-4c23-8ac0-9f455dda691a")
        # Tunnel with tunnel route
        tunnel = cloudflare.ArgoTunnel("tunnel",
            account_id="f037e56e89293a057740de681ac9abbe",
            name="my_tunnel",
            secret="AQIDBAUGBwgBAgMEBQYHCAECAwQFBgcIAQIDBAUGBwg=")
        example_index_tunnel_route_tunnel_route = cloudflare.TunnelRoute("exampleIndex/tunnelRouteTunnelRoute",
            account_id="f037e56e89293a057740de681ac9abbe",
            tunnel_id=tunnel.id,
            network="192.0.2.24/32",
            comment="New tunnel route for documentation",
            virtual_network_id="bdc39a3c-3104-4c23-8ac0-9f455dda691a")
        ```

        ## Import

        # Use account ID, network CIDR and virtual network ID.

        ```sh
         $ pulumi import cloudflare:index/tunnelRoute:TunnelRoute example <account_id/<network_cidr>/<virtual_network_id>
        ```

        :param str resource_name: The name of the resource.
        :param TunnelRouteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TunnelRouteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 tunnel_id: Optional[pulumi.Input[str]] = None,
                 virtual_network_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TunnelRouteArgs.__new__(TunnelRouteArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["comment"] = comment
            if network is None and not opts.urn:
                raise TypeError("Missing required property 'network'")
            __props__.__dict__["network"] = network
            if tunnel_id is None and not opts.urn:
                raise TypeError("Missing required property 'tunnel_id'")
            __props__.__dict__["tunnel_id"] = tunnel_id
            __props__.__dict__["virtual_network_id"] = virtual_network_id
        super(TunnelRoute, __self__).__init__(
            'cloudflare:index/tunnelRoute:TunnelRoute',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            comment: Optional[pulumi.Input[str]] = None,
            network: Optional[pulumi.Input[str]] = None,
            tunnel_id: Optional[pulumi.Input[str]] = None,
            virtual_network_id: Optional[pulumi.Input[str]] = None) -> 'TunnelRoute':
        """
        Get an existing TunnelRoute resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input[str] comment: Description of the tunnel route.
        :param pulumi.Input[str] network: The IPv4 or IPv6 network that should use this tunnel route, in CIDR notation.
        :param pulumi.Input[str] tunnel_id: The ID of the tunnel that will service the tunnel route.
        :param pulumi.Input[str] virtual_network_id: The ID of the virtual network for which this route is being added; uses the default virtual network of the account if none is provided.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TunnelRouteState.__new__(_TunnelRouteState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["comment"] = comment
        __props__.__dict__["network"] = network
        __props__.__dict__["tunnel_id"] = tunnel_id
        __props__.__dict__["virtual_network_id"] = virtual_network_id
        return TunnelRoute(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The account identifier to target for the resource.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the tunnel route.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[str]:
        """
        The IPv4 or IPv6 network that should use this tunnel route, in CIDR notation.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="tunnelId")
    def tunnel_id(self) -> pulumi.Output[str]:
        """
        The ID of the tunnel that will service the tunnel route.
        """
        return pulumi.get(self, "tunnel_id")

    @property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the virtual network for which this route is being added; uses the default virtual network of the account if none is provided.
        """
        return pulumi.get(self, "virtual_network_id")

