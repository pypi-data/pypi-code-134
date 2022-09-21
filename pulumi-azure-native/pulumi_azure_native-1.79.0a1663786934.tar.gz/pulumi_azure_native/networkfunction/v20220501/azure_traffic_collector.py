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

__all__ = ['AzureTrafficCollectorArgs', 'AzureTrafficCollector']

@pulumi.input_type
class AzureTrafficCollectorArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 azure_traffic_collector_name: Optional[pulumi.Input[str]] = None,
                 collector_policies: Optional[pulumi.Input[Sequence[pulumi.Input['CollectorPolicyArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AzureTrafficCollector resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] azure_traffic_collector_name: Azure Traffic Collector name
        :param pulumi.Input[Sequence[pulumi.Input['CollectorPolicyArgs']]] collector_policies: Collector Policies for Azure Traffic Collector.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if azure_traffic_collector_name is not None:
            pulumi.set(__self__, "azure_traffic_collector_name", azure_traffic_collector_name)
        if collector_policies is not None:
            pulumi.set(__self__, "collector_policies", collector_policies)
        if location is not None:
            pulumi.set(__self__, "location", location)
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
    @pulumi.getter(name="azureTrafficCollectorName")
    def azure_traffic_collector_name(self) -> Optional[pulumi.Input[str]]:
        """
        Azure Traffic Collector name
        """
        return pulumi.get(self, "azure_traffic_collector_name")

    @azure_traffic_collector_name.setter
    def azure_traffic_collector_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "azure_traffic_collector_name", value)

    @property
    @pulumi.getter(name="collectorPolicies")
    def collector_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CollectorPolicyArgs']]]]:
        """
        Collector Policies for Azure Traffic Collector.
        """
        return pulumi.get(self, "collector_policies")

    @collector_policies.setter
    def collector_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CollectorPolicyArgs']]]]):
        pulumi.set(self, "collector_policies", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class AzureTrafficCollector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_traffic_collector_name: Optional[pulumi.Input[str]] = None,
                 collector_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CollectorPolicyArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Azure Traffic Collector resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] azure_traffic_collector_name: Azure Traffic Collector name
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CollectorPolicyArgs']]]] collector_policies: Collector Policies for Azure Traffic Collector.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AzureTrafficCollectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Azure Traffic Collector resource.

        :param str resource_name: The name of the resource.
        :param AzureTrafficCollectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AzureTrafficCollectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_traffic_collector_name: Optional[pulumi.Input[str]] = None,
                 collector_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CollectorPolicyArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AzureTrafficCollectorArgs.__new__(AzureTrafficCollectorArgs)

            __props__.__dict__["azure_traffic_collector_name"] = azure_traffic_collector_name
            __props__.__dict__["collector_policies"] = collector_policies
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["virtual_hub"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:networkfunction:AzureTrafficCollector"), pulumi.Alias(type_="azure-native:networkfunction/v20210901preview:AzureTrafficCollector"), pulumi.Alias(type_="azure-native:networkfunction/v20220801:AzureTrafficCollector")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AzureTrafficCollector, __self__).__init__(
            'azure-native:networkfunction/v20220501:AzureTrafficCollector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AzureTrafficCollector':
        """
        Get an existing AzureTrafficCollector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AzureTrafficCollectorArgs.__new__(AzureTrafficCollectorArgs)

        __props__.__dict__["collector_policies"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_hub"] = None
        return AzureTrafficCollector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="collectorPolicies")
    def collector_policies(self) -> pulumi.Output[Optional[Sequence['outputs.CollectorPolicyResponse']]]:
        """
        Collector Policies for Azure Traffic Collector.
        """
        return pulumi.get(self, "collector_policies")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

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
        The provisioning state of the application rule collection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.TrackedResourceResponseSystemData']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> pulumi.Output[Optional['outputs.ResourceReferenceResponse']]:
        """
        The virtualHub to which the Azure Traffic Collector belongs.
        """
        return pulumi.get(self, "virtual_hub")

