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

__all__ = ['DscNodeConfigurationArgs', 'DscNodeConfiguration']

@pulumi.input_type
class DscNodeConfigurationArgs:
    def __init__(__self__, *,
                 automation_account_name: pulumi.Input[str],
                 configuration: pulumi.Input['DscConfigurationAssociationPropertyArgs'],
                 resource_group_name: pulumi.Input[str],
                 source: pulumi.Input['ContentSourceArgs'],
                 increment_node_configuration_build: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_configuration_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DscNodeConfiguration resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input['DscConfigurationAssociationPropertyArgs'] configuration: Gets or sets the configuration of the node.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input['ContentSourceArgs'] source: Gets or sets the source.
        :param pulumi.Input[bool] increment_node_configuration_build: If a new build version of NodeConfiguration is required.
        :param pulumi.Input[str] name: Name of the node configuration.
        :param pulumi.Input[str] node_configuration_name: The Dsc node configuration name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the tags attached to the resource.
        """
        pulumi.set(__self__, "automation_account_name", automation_account_name)
        pulumi.set(__self__, "configuration", configuration)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "source", source)
        if increment_node_configuration_build is not None:
            pulumi.set(__self__, "increment_node_configuration_build", increment_node_configuration_build)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if node_configuration_name is not None:
            pulumi.set(__self__, "node_configuration_name", node_configuration_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[str]:
        """
        The name of the automation account.
        """
        return pulumi.get(self, "automation_account_name")

    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "automation_account_name", value)

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Input['DscConfigurationAssociationPropertyArgs']:
        """
        Gets or sets the configuration of the node.
        """
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: pulumi.Input['DscConfigurationAssociationPropertyArgs']):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of an Azure Resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input['ContentSourceArgs']:
        """
        Gets or sets the source.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input['ContentSourceArgs']):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="incrementNodeConfigurationBuild")
    def increment_node_configuration_build(self) -> Optional[pulumi.Input[bool]]:
        """
        If a new build version of NodeConfiguration is required.
        """
        return pulumi.get(self, "increment_node_configuration_build")

    @increment_node_configuration_build.setter
    def increment_node_configuration_build(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "increment_node_configuration_build", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the node configuration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nodeConfigurationName")
    def node_configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Dsc node configuration name.
        """
        return pulumi.get(self, "node_configuration_name")

    @node_configuration_name.setter
    def node_configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_configuration_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Gets or sets the tags attached to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class DscNodeConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['DscConfigurationAssociationPropertyArgs']]] = None,
                 increment_node_configuration_build: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_configuration_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['ContentSourceArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Definition of the dsc node configuration.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[pulumi.InputType['DscConfigurationAssociationPropertyArgs']] configuration: Gets or sets the configuration of the node.
        :param pulumi.Input[bool] increment_node_configuration_build: If a new build version of NodeConfiguration is required.
        :param pulumi.Input[str] name: Name of the node configuration.
        :param pulumi.Input[str] node_configuration_name: The Dsc node configuration name.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[pulumi.InputType['ContentSourceArgs']] source: Gets or sets the source.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the tags attached to the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DscNodeConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the dsc node configuration.

        :param str resource_name: The name of the resource.
        :param DscNodeConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DscNodeConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['DscConfigurationAssociationPropertyArgs']]] = None,
                 increment_node_configuration_build: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_configuration_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['ContentSourceArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DscNodeConfigurationArgs.__new__(DscNodeConfigurationArgs)

            if automation_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__.__dict__["automation_account_name"] = automation_account_name
            if configuration is None and not opts.urn:
                raise TypeError("Missing required property 'configuration'")
            __props__.__dict__["configuration"] = configuration
            __props__.__dict__["increment_node_configuration_build"] = increment_node_configuration_build
            __props__.__dict__["name"] = name
            __props__.__dict__["node_configuration_name"] = node_configuration_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            __props__.__dict__["tags"] = tags
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["node_count"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:automation:DscNodeConfiguration"), pulumi.Alias(type_="azure-native:automation/v20151031:DscNodeConfiguration"), pulumi.Alias(type_="azure-native:automation/v20190601:DscNodeConfiguration"), pulumi.Alias(type_="azure-native:automation/v20200113preview:DscNodeConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DscNodeConfiguration, __self__).__init__(
            'azure-native:automation/v20180115:DscNodeConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DscNodeConfiguration':
        """
        Get an existing DscNodeConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DscNodeConfigurationArgs.__new__(DscNodeConfigurationArgs)

        __props__.__dict__["configuration"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["increment_node_configuration_build"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["node_count"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["type"] = None
        return DscNodeConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[Optional['outputs.DscConfigurationAssociationPropertyResponse']]:
        """
        Gets or sets the configuration of the node.
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="incrementNodeConfigurationBuild")
    def increment_node_configuration_build(self) -> pulumi.Output[Optional[bool]]:
        """
        If a new build version of NodeConfiguration is required.
        """
        return pulumi.get(self, "increment_node_configuration_build")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Output[Optional[float]]:
        """
        Number of nodes with this node configuration assigned
        """
        return pulumi.get(self, "node_count")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[str]]:
        """
        Source of node configuration.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

