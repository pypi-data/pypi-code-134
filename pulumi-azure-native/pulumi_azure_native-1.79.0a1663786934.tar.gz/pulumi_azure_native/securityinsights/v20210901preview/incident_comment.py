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

__all__ = ['IncidentCommentArgs', 'IncidentComment']

@pulumi.input_type
class IncidentCommentArgs:
    def __init__(__self__, *,
                 incident_id: pulumi.Input[str],
                 message: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 incident_comment_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IncidentComment resource.
        :param pulumi.Input[str] incident_id: Incident ID
        :param pulumi.Input[str] message: The comment message
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] incident_comment_id: Incident comment ID
        """
        pulumi.set(__self__, "incident_id", incident_id)
        pulumi.set(__self__, "message", message)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if incident_comment_id is not None:
            pulumi.set(__self__, "incident_comment_id", incident_comment_id)

    @property
    @pulumi.getter(name="incidentId")
    def incident_id(self) -> pulumi.Input[str]:
        """
        Incident ID
        """
        return pulumi.get(self, "incident_id")

    @incident_id.setter
    def incident_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "incident_id", value)

    @property
    @pulumi.getter
    def message(self) -> pulumi.Input[str]:
        """
        The comment message
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: pulumi.Input[str]):
        pulumi.set(self, "message", value)

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
    @pulumi.getter(name="incidentCommentId")
    def incident_comment_id(self) -> Optional[pulumi.Input[str]]:
        """
        Incident comment ID
        """
        return pulumi.get(self, "incident_comment_id")

    @incident_comment_id.setter
    def incident_comment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "incident_comment_id", value)


class IncidentComment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 incident_comment_id: Optional[pulumi.Input[str]] = None,
                 incident_id: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents an incident comment

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] incident_comment_id: Incident comment ID
        :param pulumi.Input[str] incident_id: Incident ID
        :param pulumi.Input[str] message: The comment message
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IncidentCommentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents an incident comment

        :param str resource_name: The name of the resource.
        :param IncidentCommentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IncidentCommentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 incident_comment_id: Optional[pulumi.Input[str]] = None,
                 incident_id: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IncidentCommentArgs.__new__(IncidentCommentArgs)

            __props__.__dict__["incident_comment_id"] = incident_comment_id
            if incident_id is None and not opts.urn:
                raise TypeError("Missing required property 'incident_id'")
            __props__.__dict__["incident_id"] = incident_id
            if message is None and not opts.urn:
                raise TypeError("Missing required property 'message'")
            __props__.__dict__["message"] = message
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["author"] = None
            __props__.__dict__["created_time_utc"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["last_modified_time_utc"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:IncidentComment"), pulumi.Alias(type_="azure-native:securityinsights/v20190101preview:IncidentComment"), pulumi.Alias(type_="azure-native:securityinsights/v20210301preview:IncidentComment"), pulumi.Alias(type_="azure-native:securityinsights/v20210401:IncidentComment"), pulumi.Alias(type_="azure-native:securityinsights/v20211001:IncidentComment"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:IncidentComment"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:IncidentComment"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:IncidentComment"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:IncidentComment"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:IncidentComment"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:IncidentComment"), pulumi.Alias(type_="azure-native:securityinsights/v20220801:IncidentComment"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:IncidentComment"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:IncidentComment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IncidentComment, __self__).__init__(
            'azure-native:securityinsights/v20210901preview:IncidentComment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IncidentComment':
        """
        Get an existing IncidentComment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IncidentCommentArgs.__new__(IncidentCommentArgs)

        __props__.__dict__["author"] = None
        __props__.__dict__["created_time_utc"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["last_modified_time_utc"] = None
        __props__.__dict__["message"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return IncidentComment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def author(self) -> pulumi.Output['outputs.ClientInfoResponse']:
        """
        Describes the client that created the comment
        """
        return pulumi.get(self, "author")

    @property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> pulumi.Output[str]:
        """
        The time the comment was created
        """
        return pulumi.get(self, "created_time_utc")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="lastModifiedTimeUtc")
    def last_modified_time_utc(self) -> pulumi.Output[str]:
        """
        The time the comment was updated
        """
        return pulumi.get(self, "last_modified_time_utc")

    @property
    @pulumi.getter
    def message(self) -> pulumi.Output[str]:
        """
        The comment message
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

