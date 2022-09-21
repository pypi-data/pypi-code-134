# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['WorkspaceArgs', 'Workspace']

@pulumi.input_type
class WorkspaceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 e_tag: Optional[pulumi.Input[str]] = None,
                 features: Optional[pulumi.Input['WorkspaceFeaturesArgs']] = None,
                 force_cmk_for_query: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'WorkspaceEntityStatus']]] = None,
                 public_network_access_for_ingestion: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]] = None,
                 public_network_access_for_query: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]] = None,
                 retention_in_days: Optional[pulumi.Input[int]] = None,
                 sku: Optional[pulumi.Input['WorkspaceSkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_capping: Optional[pulumi.Input['WorkspaceCappingArgs']] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Workspace resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] e_tag: The ETag of the workspace.
        :param pulumi.Input['WorkspaceFeaturesArgs'] features: Workspace features.
        :param pulumi.Input[bool] force_cmk_for_query: Indicates whether customer managed storage is mandatory for query management.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union[str, 'WorkspaceEntityStatus']] provisioning_state: The provisioning state of the workspace.
        :param pulumi.Input[Union[str, 'PublicNetworkAccessType']] public_network_access_for_ingestion: The network access type for accessing Log Analytics ingestion.
        :param pulumi.Input[Union[str, 'PublicNetworkAccessType']] public_network_access_for_query: The network access type for accessing Log Analytics query.
        :param pulumi.Input[int] retention_in_days: The workspace data retention in days. Allowed values are per pricing plan. See pricing tiers documentation for details.
        :param pulumi.Input['WorkspaceSkuArgs'] sku: The SKU of the workspace.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input['WorkspaceCappingArgs'] workspace_capping: The daily volume cap for ingestion.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if e_tag is not None:
            pulumi.set(__self__, "e_tag", e_tag)
        if features is not None:
            pulumi.set(__self__, "features", features)
        if force_cmk_for_query is not None:
            pulumi.set(__self__, "force_cmk_for_query", force_cmk_for_query)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access_for_ingestion is not None:
            pulumi.set(__self__, "public_network_access_for_ingestion", public_network_access_for_ingestion)
        if public_network_access_for_query is not None:
            pulumi.set(__self__, "public_network_access_for_query", public_network_access_for_query)
        if retention_in_days is not None:
            pulumi.set(__self__, "retention_in_days", retention_in_days)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if workspace_capping is not None:
            pulumi.set(__self__, "workspace_capping", workspace_capping)
        if workspace_name is not None:
            pulumi.set(__self__, "workspace_name", workspace_name)

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
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[str]]:
        """
        The ETag of the workspace.
        """
        return pulumi.get(self, "e_tag")

    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_tag", value)

    @property
    @pulumi.getter
    def features(self) -> Optional[pulumi.Input['WorkspaceFeaturesArgs']]:
        """
        Workspace features.
        """
        return pulumi.get(self, "features")

    @features.setter
    def features(self, value: Optional[pulumi.Input['WorkspaceFeaturesArgs']]):
        pulumi.set(self, "features", value)

    @property
    @pulumi.getter(name="forceCmkForQuery")
    def force_cmk_for_query(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether customer managed storage is mandatory for query management.
        """
        return pulumi.get(self, "force_cmk_for_query")

    @force_cmk_for_query.setter
    def force_cmk_for_query(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_cmk_for_query", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'WorkspaceEntityStatus']]]:
        """
        The provisioning state of the workspace.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'WorkspaceEntityStatus']]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="publicNetworkAccessForIngestion")
    def public_network_access_for_ingestion(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]]:
        """
        The network access type for accessing Log Analytics ingestion.
        """
        return pulumi.get(self, "public_network_access_for_ingestion")

    @public_network_access_for_ingestion.setter
    def public_network_access_for_ingestion(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]]):
        pulumi.set(self, "public_network_access_for_ingestion", value)

    @property
    @pulumi.getter(name="publicNetworkAccessForQuery")
    def public_network_access_for_query(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]]:
        """
        The network access type for accessing Log Analytics query.
        """
        return pulumi.get(self, "public_network_access_for_query")

    @public_network_access_for_query.setter
    def public_network_access_for_query(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]]):
        pulumi.set(self, "public_network_access_for_query", value)

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[pulumi.Input[int]]:
        """
        The workspace data retention in days. Allowed values are per pricing plan. See pricing tiers documentation for details.
        """
        return pulumi.get(self, "retention_in_days")

    @retention_in_days.setter
    def retention_in_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_in_days", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['WorkspaceSkuArgs']]:
        """
        The SKU of the workspace.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['WorkspaceSkuArgs']]):
        pulumi.set(self, "sku", value)

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

    @property
    @pulumi.getter(name="workspaceCapping")
    def workspace_capping(self) -> Optional[pulumi.Input['WorkspaceCappingArgs']]:
        """
        The daily volume cap for ingestion.
        """
        return pulumi.get(self, "workspace_capping")

    @workspace_capping.setter
    def workspace_capping(self, value: Optional[pulumi.Input['WorkspaceCappingArgs']]):
        pulumi.set(self, "workspace_capping", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_name", value)


class Workspace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 features: Optional[pulumi.Input[pulumi.InputType['WorkspaceFeaturesArgs']]] = None,
                 force_cmk_for_query: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'WorkspaceEntityStatus']]] = None,
                 public_network_access_for_ingestion: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]] = None,
                 public_network_access_for_query: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retention_in_days: Optional[pulumi.Input[int]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['WorkspaceSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_capping: Optional[pulumi.Input[pulumi.InputType['WorkspaceCappingArgs']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The top level Workspace resource container.
        API Version: 2020-10-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] e_tag: The ETag of the workspace.
        :param pulumi.Input[pulumi.InputType['WorkspaceFeaturesArgs']] features: Workspace features.
        :param pulumi.Input[bool] force_cmk_for_query: Indicates whether customer managed storage is mandatory for query management.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union[str, 'WorkspaceEntityStatus']] provisioning_state: The provisioning state of the workspace.
        :param pulumi.Input[Union[str, 'PublicNetworkAccessType']] public_network_access_for_ingestion: The network access type for accessing Log Analytics ingestion.
        :param pulumi.Input[Union[str, 'PublicNetworkAccessType']] public_network_access_for_query: The network access type for accessing Log Analytics query.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[int] retention_in_days: The workspace data retention in days. Allowed values are per pricing plan. See pricing tiers documentation for details.
        :param pulumi.Input[pulumi.InputType['WorkspaceSkuArgs']] sku: The SKU of the workspace.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[pulumi.InputType['WorkspaceCappingArgs']] workspace_capping: The daily volume cap for ingestion.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The top level Workspace resource container.
        API Version: 2020-10-01.

        :param str resource_name: The name of the resource.
        :param WorkspaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 features: Optional[pulumi.Input[pulumi.InputType['WorkspaceFeaturesArgs']]] = None,
                 force_cmk_for_query: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'WorkspaceEntityStatus']]] = None,
                 public_network_access_for_ingestion: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]] = None,
                 public_network_access_for_query: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retention_in_days: Optional[pulumi.Input[int]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['WorkspaceSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_capping: Optional[pulumi.Input[pulumi.InputType['WorkspaceCappingArgs']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

            __props__.__dict__["e_tag"] = e_tag
            __props__.__dict__["features"] = features
            __props__.__dict__["force_cmk_for_query"] = force_cmk_for_query
            __props__.__dict__["location"] = location
            __props__.__dict__["provisioning_state"] = provisioning_state
            __props__.__dict__["public_network_access_for_ingestion"] = public_network_access_for_ingestion
            __props__.__dict__["public_network_access_for_query"] = public_network_access_for_query
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["retention_in_days"] = retention_in_days
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["workspace_capping"] = workspace_capping
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["created_date"] = None
            __props__.__dict__["customer_id"] = None
            __props__.__dict__["modified_date"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_link_scoped_resources"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:operationalinsights/v20151101preview:Workspace"), pulumi.Alias(type_="azure-native:operationalinsights/v20200301preview:Workspace"), pulumi.Alias(type_="azure-native:operationalinsights/v20200801:Workspace"), pulumi.Alias(type_="azure-native:operationalinsights/v20201001:Workspace"), pulumi.Alias(type_="azure-native:operationalinsights/v20210601:Workspace"), pulumi.Alias(type_="azure-native:operationalinsights/v20211201preview:Workspace")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Workspace, __self__).__init__(
            'azure-native:operationalinsights:Workspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Workspace':
        """
        Get an existing Workspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

        __props__.__dict__["created_date"] = None
        __props__.__dict__["customer_id"] = None
        __props__.__dict__["e_tag"] = None
        __props__.__dict__["features"] = None
        __props__.__dict__["force_cmk_for_query"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["modified_date"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_link_scoped_resources"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access_for_ingestion"] = None
        __props__.__dict__["public_network_access_for_query"] = None
        __props__.__dict__["retention_in_days"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["workspace_capping"] = None
        return Workspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[str]:
        """
        Workspace creation date.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> pulumi.Output[str]:
        """
        This is a read-only property. Represents the ID associated with the workspace.
        """
        return pulumi.get(self, "customer_id")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        """
        The ETag of the workspace.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def features(self) -> pulumi.Output[Optional['outputs.WorkspaceFeaturesResponse']]:
        """
        Workspace features.
        """
        return pulumi.get(self, "features")

    @property
    @pulumi.getter(name="forceCmkForQuery")
    def force_cmk_for_query(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether customer managed storage is mandatory for query management.
        """
        return pulumi.get(self, "force_cmk_for_query")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="modifiedDate")
    def modified_date(self) -> pulumi.Output[str]:
        """
        Workspace modification date.
        """
        return pulumi.get(self, "modified_date")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateLinkScopedResources")
    def private_link_scoped_resources(self) -> pulumi.Output[Sequence['outputs.PrivateLinkScopedResourceResponse']]:
        """
        List of linked private link scope resources.
        """
        return pulumi.get(self, "private_link_scoped_resources")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The provisioning state of the workspace.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccessForIngestion")
    def public_network_access_for_ingestion(self) -> pulumi.Output[Optional[str]]:
        """
        The network access type for accessing Log Analytics ingestion.
        """
        return pulumi.get(self, "public_network_access_for_ingestion")

    @property
    @pulumi.getter(name="publicNetworkAccessForQuery")
    def public_network_access_for_query(self) -> pulumi.Output[Optional[str]]:
        """
        The network access type for accessing Log Analytics query.
        """
        return pulumi.get(self, "public_network_access_for_query")

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> pulumi.Output[Optional[int]]:
        """
        The workspace data retention in days. Allowed values are per pricing plan. See pricing tiers documentation for details.
        """
        return pulumi.get(self, "retention_in_days")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.WorkspaceSkuResponse']]:
        """
        The SKU of the workspace.
        """
        return pulumi.get(self, "sku")

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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workspaceCapping")
    def workspace_capping(self) -> pulumi.Output[Optional['outputs.WorkspaceCappingResponse']]:
        """
        The daily volume cap for ingestion.
        """
        return pulumi.get(self, "workspace_capping")

