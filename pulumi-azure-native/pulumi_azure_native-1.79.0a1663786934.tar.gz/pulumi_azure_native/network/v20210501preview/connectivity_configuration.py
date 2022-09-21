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

__all__ = ['ConnectivityConfigurationArgs', 'ConnectivityConfiguration']

@pulumi.input_type
class ConnectivityConfigurationArgs:
    def __init__(__self__, *,
                 applies_to_groups: pulumi.Input[Sequence[pulumi.Input['ConnectivityGroupItemArgs']]],
                 connectivity_topology: pulumi.Input[Union[str, 'ConnectivityTopology']],
                 network_manager_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 delete_existing_peering: Optional[pulumi.Input[Union[str, 'DeleteExistingPeering']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 hubs: Optional[pulumi.Input[Sequence[pulumi.Input['HubArgs']]]] = None,
                 is_global: Optional[pulumi.Input[Union[str, 'IsGlobal']]] = None):
        """
        The set of arguments for constructing a ConnectivityConfiguration resource.
        :param pulumi.Input[Sequence[pulumi.Input['ConnectivityGroupItemArgs']]] applies_to_groups: Groups for configuration
        :param pulumi.Input[Union[str, 'ConnectivityTopology']] connectivity_topology: Connectivity topology type.
        :param pulumi.Input[str] network_manager_name: The name of the network manager.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] configuration_name: The name of the network manager connectivity configuration.
        :param pulumi.Input[Union[str, 'DeleteExistingPeering']] delete_existing_peering: Flag if need to remove current existing peerings.
        :param pulumi.Input[str] description: A description of the connectivity configuration.
        :param pulumi.Input[str] display_name: A friendly name for the resource.
        :param pulumi.Input[Sequence[pulumi.Input['HubArgs']]] hubs: List of hubItems
        :param pulumi.Input[Union[str, 'IsGlobal']] is_global: Flag if global mesh is supported.
        """
        pulumi.set(__self__, "applies_to_groups", applies_to_groups)
        pulumi.set(__self__, "connectivity_topology", connectivity_topology)
        pulumi.set(__self__, "network_manager_name", network_manager_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if configuration_name is not None:
            pulumi.set(__self__, "configuration_name", configuration_name)
        if delete_existing_peering is not None:
            pulumi.set(__self__, "delete_existing_peering", delete_existing_peering)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if hubs is not None:
            pulumi.set(__self__, "hubs", hubs)
        if is_global is not None:
            pulumi.set(__self__, "is_global", is_global)

    @property
    @pulumi.getter(name="appliesToGroups")
    def applies_to_groups(self) -> pulumi.Input[Sequence[pulumi.Input['ConnectivityGroupItemArgs']]]:
        """
        Groups for configuration
        """
        return pulumi.get(self, "applies_to_groups")

    @applies_to_groups.setter
    def applies_to_groups(self, value: pulumi.Input[Sequence[pulumi.Input['ConnectivityGroupItemArgs']]]):
        pulumi.set(self, "applies_to_groups", value)

    @property
    @pulumi.getter(name="connectivityTopology")
    def connectivity_topology(self) -> pulumi.Input[Union[str, 'ConnectivityTopology']]:
        """
        Connectivity topology type.
        """
        return pulumi.get(self, "connectivity_topology")

    @connectivity_topology.setter
    def connectivity_topology(self, value: pulumi.Input[Union[str, 'ConnectivityTopology']]):
        pulumi.set(self, "connectivity_topology", value)

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
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the network manager connectivity configuration.
        """
        return pulumi.get(self, "configuration_name")

    @configuration_name.setter
    def configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "configuration_name", value)

    @property
    @pulumi.getter(name="deleteExistingPeering")
    def delete_existing_peering(self) -> Optional[pulumi.Input[Union[str, 'DeleteExistingPeering']]]:
        """
        Flag if need to remove current existing peerings.
        """
        return pulumi.get(self, "delete_existing_peering")

    @delete_existing_peering.setter
    def delete_existing_peering(self, value: Optional[pulumi.Input[Union[str, 'DeleteExistingPeering']]]):
        pulumi.set(self, "delete_existing_peering", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the connectivity configuration.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        A friendly name for the resource.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def hubs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['HubArgs']]]]:
        """
        List of hubItems
        """
        return pulumi.get(self, "hubs")

    @hubs.setter
    def hubs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['HubArgs']]]]):
        pulumi.set(self, "hubs", value)

    @property
    @pulumi.getter(name="isGlobal")
    def is_global(self) -> Optional[pulumi.Input[Union[str, 'IsGlobal']]]:
        """
        Flag if global mesh is supported.
        """
        return pulumi.get(self, "is_global")

    @is_global.setter
    def is_global(self, value: Optional[pulumi.Input[Union[str, 'IsGlobal']]]):
        pulumi.set(self, "is_global", value)


class ConnectivityConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 applies_to_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectivityGroupItemArgs']]]]] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 connectivity_topology: Optional[pulumi.Input[Union[str, 'ConnectivityTopology']]] = None,
                 delete_existing_peering: Optional[pulumi.Input[Union[str, 'DeleteExistingPeering']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 hubs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HubArgs']]]]] = None,
                 is_global: Optional[pulumi.Input[Union[str, 'IsGlobal']]] = None,
                 network_manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The network manager connectivity configuration resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectivityGroupItemArgs']]]] applies_to_groups: Groups for configuration
        :param pulumi.Input[str] configuration_name: The name of the network manager connectivity configuration.
        :param pulumi.Input[Union[str, 'ConnectivityTopology']] connectivity_topology: Connectivity topology type.
        :param pulumi.Input[Union[str, 'DeleteExistingPeering']] delete_existing_peering: Flag if need to remove current existing peerings.
        :param pulumi.Input[str] description: A description of the connectivity configuration.
        :param pulumi.Input[str] display_name: A friendly name for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HubArgs']]]] hubs: List of hubItems
        :param pulumi.Input[Union[str, 'IsGlobal']] is_global: Flag if global mesh is supported.
        :param pulumi.Input[str] network_manager_name: The name of the network manager.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectivityConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The network manager connectivity configuration resource

        :param str resource_name: The name of the resource.
        :param ConnectivityConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectivityConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 applies_to_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectivityGroupItemArgs']]]]] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 connectivity_topology: Optional[pulumi.Input[Union[str, 'ConnectivityTopology']]] = None,
                 delete_existing_peering: Optional[pulumi.Input[Union[str, 'DeleteExistingPeering']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 hubs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HubArgs']]]]] = None,
                 is_global: Optional[pulumi.Input[Union[str, 'IsGlobal']]] = None,
                 network_manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectivityConfigurationArgs.__new__(ConnectivityConfigurationArgs)

            if applies_to_groups is None and not opts.urn:
                raise TypeError("Missing required property 'applies_to_groups'")
            __props__.__dict__["applies_to_groups"] = applies_to_groups
            __props__.__dict__["configuration_name"] = configuration_name
            if connectivity_topology is None and not opts.urn:
                raise TypeError("Missing required property 'connectivity_topology'")
            __props__.__dict__["connectivity_topology"] = connectivity_topology
            __props__.__dict__["delete_existing_peering"] = delete_existing_peering
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["hubs"] = hubs
            __props__.__dict__["is_global"] = is_global
            if network_manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_manager_name'")
            __props__.__dict__["network_manager_name"] = network_manager_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:ConnectivityConfiguration"), pulumi.Alias(type_="azure-native:network/v20210201preview:ConnectivityConfiguration"), pulumi.Alias(type_="azure-native:network/v20220101:ConnectivityConfiguration"), pulumi.Alias(type_="azure-native:network/v20220201preview:ConnectivityConfiguration"), pulumi.Alias(type_="azure-native:network/v20220401preview:ConnectivityConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ConnectivityConfiguration, __self__).__init__(
            'azure-native:network/v20210501preview:ConnectivityConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConnectivityConfiguration':
        """
        Get an existing ConnectivityConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectivityConfigurationArgs.__new__(ConnectivityConfigurationArgs)

        __props__.__dict__["applies_to_groups"] = None
        __props__.__dict__["connectivity_topology"] = None
        __props__.__dict__["delete_existing_peering"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["hubs"] = None
        __props__.__dict__["is_global"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ConnectivityConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appliesToGroups")
    def applies_to_groups(self) -> pulumi.Output[Sequence['outputs.ConnectivityGroupItemResponse']]:
        """
        Groups for configuration
        """
        return pulumi.get(self, "applies_to_groups")

    @property
    @pulumi.getter(name="connectivityTopology")
    def connectivity_topology(self) -> pulumi.Output[str]:
        """
        Connectivity topology type.
        """
        return pulumi.get(self, "connectivity_topology")

    @property
    @pulumi.getter(name="deleteExistingPeering")
    def delete_existing_peering(self) -> pulumi.Output[Optional[str]]:
        """
        Flag if need to remove current existing peerings.
        """
        return pulumi.get(self, "delete_existing_peering")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the connectivity configuration.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        A friendly name for the resource.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def hubs(self) -> pulumi.Output[Optional[Sequence['outputs.HubResponse']]]:
        """
        List of hubItems
        """
        return pulumi.get(self, "hubs")

    @property
    @pulumi.getter(name="isGlobal")
    def is_global(self) -> pulumi.Output[Optional[str]]:
        """
        Flag if global mesh is supported.
        """
        return pulumi.get(self, "is_global")

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
        The provisioning state of the connectivity configuration resource.
        """
        return pulumi.get(self, "provisioning_state")

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

