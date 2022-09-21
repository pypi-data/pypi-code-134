# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AccessBookmarkArgs', 'AccessBookmark']

@pulumi.input_type
class AccessBookmarkArgs:
    def __init__(__self__, *,
                 domain: pulumi.Input[str],
                 name: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 app_launcher_visible: Optional[pulumi.Input[bool]] = None,
                 logo_url: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccessBookmark resource.
        :param pulumi.Input[str] domain: The domain of the bookmark application. Can include subdomains, paths, or both.
        :param pulumi.Input[str] name: Name of the bookmark application.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. Conflicts with `zone_id`.
        :param pulumi.Input[bool] app_launcher_visible: Option to show/hide the bookmark in the app launcher. Defaults to `true`.
        :param pulumi.Input[str] logo_url: The image URL for the logo shown in the app launcher dashboard.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. Conflicts with `account_id`.
        """
        pulumi.set(__self__, "domain", domain)
        pulumi.set(__self__, "name", name)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if app_launcher_visible is not None:
            pulumi.set(__self__, "app_launcher_visible", app_launcher_visible)
        if logo_url is not None:
            pulumi.set(__self__, "logo_url", logo_url)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Input[str]:
        """
        The domain of the bookmark application. Can include subdomains, paths, or both.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the bookmark application.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account identifier to target for the resource. Conflicts with `zone_id`.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="appLauncherVisible")
    def app_launcher_visible(self) -> Optional[pulumi.Input[bool]]:
        """
        Option to show/hide the bookmark in the app launcher. Defaults to `true`.
        """
        return pulumi.get(self, "app_launcher_visible")

    @app_launcher_visible.setter
    def app_launcher_visible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "app_launcher_visible", value)

    @property
    @pulumi.getter(name="logoUrl")
    def logo_url(self) -> Optional[pulumi.Input[str]]:
        """
        The image URL for the logo shown in the app launcher dashboard.
        """
        return pulumi.get(self, "logo_url")

    @logo_url.setter
    def logo_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logo_url", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The zone identifier to target for the resource. Conflicts with `account_id`.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


@pulumi.input_type
class _AccessBookmarkState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 app_launcher_visible: Optional[pulumi.Input[bool]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 logo_url: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AccessBookmark resources.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. Conflicts with `zone_id`.
        :param pulumi.Input[bool] app_launcher_visible: Option to show/hide the bookmark in the app launcher. Defaults to `true`.
        :param pulumi.Input[str] domain: The domain of the bookmark application. Can include subdomains, paths, or both.
        :param pulumi.Input[str] logo_url: The image URL for the logo shown in the app launcher dashboard.
        :param pulumi.Input[str] name: Name of the bookmark application.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. Conflicts with `account_id`.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if app_launcher_visible is not None:
            pulumi.set(__self__, "app_launcher_visible", app_launcher_visible)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if logo_url is not None:
            pulumi.set(__self__, "logo_url", logo_url)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account identifier to target for the resource. Conflicts with `zone_id`.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="appLauncherVisible")
    def app_launcher_visible(self) -> Optional[pulumi.Input[bool]]:
        """
        Option to show/hide the bookmark in the app launcher. Defaults to `true`.
        """
        return pulumi.get(self, "app_launcher_visible")

    @app_launcher_visible.setter
    def app_launcher_visible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "app_launcher_visible", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The domain of the bookmark application. Can include subdomains, paths, or both.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="logoUrl")
    def logo_url(self) -> Optional[pulumi.Input[str]]:
        """
        The image URL for the logo shown in the app launcher dashboard.
        """
        return pulumi.get(self, "logo_url")

    @logo_url.setter
    def logo_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logo_url", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the bookmark application.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The zone identifier to target for the resource. Conflicts with `account_id`.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class AccessBookmark(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 app_launcher_visible: Optional[pulumi.Input[bool]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 logo_url: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        my_bookmark_app = cloudflare.AccessBookmark("myBookmarkApp",
            account_id="f037e56e89293a057740de681ac9abbe",
            app_launcher_visible=True,
            domain="example.com",
            logo_url="https://example.com/example.png",
            name="My Bookmark App")
        ```

        ## Import

        ```sh
         $ pulumi import cloudflare:index/accessBookmark:AccessBookmark example <account_id>/<bookmark_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. Conflicts with `zone_id`.
        :param pulumi.Input[bool] app_launcher_visible: Option to show/hide the bookmark in the app launcher. Defaults to `true`.
        :param pulumi.Input[str] domain: The domain of the bookmark application. Can include subdomains, paths, or both.
        :param pulumi.Input[str] logo_url: The image URL for the logo shown in the app launcher dashboard.
        :param pulumi.Input[str] name: Name of the bookmark application.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. Conflicts with `account_id`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessBookmarkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        my_bookmark_app = cloudflare.AccessBookmark("myBookmarkApp",
            account_id="f037e56e89293a057740de681ac9abbe",
            app_launcher_visible=True,
            domain="example.com",
            logo_url="https://example.com/example.png",
            name="My Bookmark App")
        ```

        ## Import

        ```sh
         $ pulumi import cloudflare:index/accessBookmark:AccessBookmark example <account_id>/<bookmark_id>
        ```

        :param str resource_name: The name of the resource.
        :param AccessBookmarkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessBookmarkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 app_launcher_visible: Optional[pulumi.Input[bool]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 logo_url: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccessBookmarkArgs.__new__(AccessBookmarkArgs)

            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["app_launcher_visible"] = app_launcher_visible
            if domain is None and not opts.urn:
                raise TypeError("Missing required property 'domain'")
            __props__.__dict__["domain"] = domain
            __props__.__dict__["logo_url"] = logo_url
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["zone_id"] = zone_id
        super(AccessBookmark, __self__).__init__(
            'cloudflare:index/accessBookmark:AccessBookmark',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            app_launcher_visible: Optional[pulumi.Input[bool]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            logo_url: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'AccessBookmark':
        """
        Get an existing AccessBookmark resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. Conflicts with `zone_id`.
        :param pulumi.Input[bool] app_launcher_visible: Option to show/hide the bookmark in the app launcher. Defaults to `true`.
        :param pulumi.Input[str] domain: The domain of the bookmark application. Can include subdomains, paths, or both.
        :param pulumi.Input[str] logo_url: The image URL for the logo shown in the app launcher dashboard.
        :param pulumi.Input[str] name: Name of the bookmark application.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. Conflicts with `account_id`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccessBookmarkState.__new__(_AccessBookmarkState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["app_launcher_visible"] = app_launcher_visible
        __props__.__dict__["domain"] = domain
        __props__.__dict__["logo_url"] = logo_url
        __props__.__dict__["name"] = name
        __props__.__dict__["zone_id"] = zone_id
        return AccessBookmark(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The account identifier to target for the resource. Conflicts with `zone_id`.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="appLauncherVisible")
    def app_launcher_visible(self) -> pulumi.Output[Optional[bool]]:
        """
        Option to show/hide the bookmark in the app launcher. Defaults to `true`.
        """
        return pulumi.get(self, "app_launcher_visible")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        The domain of the bookmark application. Can include subdomains, paths, or both.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="logoUrl")
    def logo_url(self) -> pulumi.Output[Optional[str]]:
        """
        The image URL for the logo shown in the app launcher dashboard.
        """
        return pulumi.get(self, "logo_url")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the bookmark application.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The zone identifier to target for the resource. Conflicts with `account_id`.
        """
        return pulumi.get(self, "zone_id")

