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

__all__ = ['AnomaliesArgs', 'Anomalies']

@pulumi.input_type
class AnomaliesArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 operational_insights_resource_provider: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 settings_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Anomalies resource.
        :param pulumi.Input[str] kind: The kind of the setting
               Expected value is 'Anomalies'.
        :param pulumi.Input[str] operational_insights_resource_provider: The namespace of workspaces resource provider- Microsoft.OperationalInsights.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] settings_name: The setting name. Supports - Anomalies, EyesOn, EntityAnalytics, Ueba
        """
        pulumi.set(__self__, "kind", 'Anomalies')
        pulumi.set(__self__, "operational_insights_resource_provider", operational_insights_resource_provider)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if settings_name is not None:
            pulumi.set(__self__, "settings_name", settings_name)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The kind of the setting
        Expected value is 'Anomalies'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="operationalInsightsResourceProvider")
    def operational_insights_resource_provider(self) -> pulumi.Input[str]:
        """
        The namespace of workspaces resource provider- Microsoft.OperationalInsights.
        """
        return pulumi.get(self, "operational_insights_resource_provider")

    @operational_insights_resource_provider.setter
    def operational_insights_resource_provider(self, value: pulumi.Input[str]):
        pulumi.set(self, "operational_insights_resource_provider", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="settingsName")
    def settings_name(self) -> Optional[pulumi.Input[str]]:
        """
        The setting name. Supports - Anomalies, EyesOn, EntityAnalytics, Ueba
        """
        return pulumi.get(self, "settings_name")

    @settings_name.setter
    def settings_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "settings_name", value)


class Anomalies(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 operational_insights_resource_provider: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 settings_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Settings with single toggle.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kind: The kind of the setting
               Expected value is 'Anomalies'.
        :param pulumi.Input[str] operational_insights_resource_provider: The namespace of workspaces resource provider- Microsoft.OperationalInsights.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] settings_name: The setting name. Supports - Anomalies, EyesOn, EntityAnalytics, Ueba
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AnomaliesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Settings with single toggle.

        :param str resource_name: The name of the resource.
        :param AnomaliesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AnomaliesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 operational_insights_resource_provider: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 settings_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AnomaliesArgs.__new__(AnomaliesArgs)

            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'Anomalies'
            if operational_insights_resource_provider is None and not opts.urn:
                raise TypeError("Missing required property 'operational_insights_resource_provider'")
            __props__.__dict__["operational_insights_resource_provider"] = operational_insights_resource_provider
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["settings_name"] = settings_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["is_enabled"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:Anomalies"), pulumi.Alias(type_="azure-native:securityinsights/v20190101preview:Anomalies"), pulumi.Alias(type_="azure-native:securityinsights/v20210901preview:Anomalies"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:Anomalies"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:Anomalies"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:Anomalies"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:Anomalies"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:Anomalies"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:Anomalies"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:Anomalies"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:Anomalies")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Anomalies, __self__).__init__(
            'azure-native:securityinsights/v20210301preview:Anomalies',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Anomalies':
        """
        Get an existing Anomalies resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AnomaliesArgs.__new__(AnomaliesArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["is_enabled"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Anomalies(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[bool]:
        """
        Determines whether the setting is enable or disabled.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of the setting
        Expected value is 'Anomalies'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

