# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['CseMatchListArgs', 'CseMatchList']

@pulumi.input_type
class CseMatchListArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 target_column: pulumi.Input[str],
                 default_ttl: Optional[pulumi.Input[int]] = None,
                 items: Optional[pulumi.Input[Sequence[pulumi.Input['CseMatchListItemArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CseMatchList resource.
        :param pulumi.Input[str] description: Match list item description.
        :param pulumi.Input[str] target_column: Target column. (possible values: Hostname, FileHash, Url, SrcIp, DstIp, Domain, Username, Ip, Asn, Isp, Org, SrcAsn, SrcIsp, SrcOrg, DstAsn, DstIsp, DstOrg or any custom column.)
        :param pulumi.Input[int] default_ttl: The default time to live for match list items added through the UI. Specified in seconds.
        :param pulumi.Input[Sequence[pulumi.Input['CseMatchListItemArgs']]] items: List of match list items. See match_list_item schema for details.
        :param pulumi.Input[str] name: Match list name.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "target_column", target_column)
        if default_ttl is not None:
            pulumi.set(__self__, "default_ttl", default_ttl)
        if items is not None:
            pulumi.set(__self__, "items", items)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        Match list item description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="targetColumn")
    def target_column(self) -> pulumi.Input[str]:
        """
        Target column. (possible values: Hostname, FileHash, Url, SrcIp, DstIp, Domain, Username, Ip, Asn, Isp, Org, SrcAsn, SrcIsp, SrcOrg, DstAsn, DstIsp, DstOrg or any custom column.)
        """
        return pulumi.get(self, "target_column")

    @target_column.setter
    def target_column(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_column", value)

    @property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[pulumi.Input[int]]:
        """
        The default time to live for match list items added through the UI. Specified in seconds.
        """
        return pulumi.get(self, "default_ttl")

    @default_ttl.setter
    def default_ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "default_ttl", value)

    @property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CseMatchListItemArgs']]]]:
        """
        List of match list items. See match_list_item schema for details.
        """
        return pulumi.get(self, "items")

    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CseMatchListItemArgs']]]]):
        pulumi.set(self, "items", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Match list name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _CseMatchListState:
    def __init__(__self__, *,
                 created: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 default_ttl: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 items: Optional[pulumi.Input[Sequence[pulumi.Input['CseMatchListItemArgs']]]] = None,
                 last_updated: Optional[pulumi.Input[str]] = None,
                 last_updated_by: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 target_column: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CseMatchList resources.
        :param pulumi.Input[int] default_ttl: The default time to live for match list items added through the UI. Specified in seconds.
        :param pulumi.Input[str] description: Match list item description.
        :param pulumi.Input[Sequence[pulumi.Input['CseMatchListItemArgs']]] items: List of match list items. See match_list_item schema for details.
        :param pulumi.Input[str] name: Match list name.
        :param pulumi.Input[str] target_column: Target column. (possible values: Hostname, FileHash, Url, SrcIp, DstIp, Domain, Username, Ip, Asn, Isp, Org, SrcAsn, SrcIsp, SrcOrg, DstAsn, DstIsp, DstOrg or any custom column.)
        """
        if created is not None:
            pulumi.set(__self__, "created", created)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if default_ttl is not None:
            pulumi.set(__self__, "default_ttl", default_ttl)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if items is not None:
            pulumi.set(__self__, "items", items)
        if last_updated is not None:
            pulumi.set(__self__, "last_updated", last_updated)
        if last_updated_by is not None:
            pulumi.set(__self__, "last_updated_by", last_updated_by)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if target_column is not None:
            pulumi.set(__self__, "target_column", target_column)

    @property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "created")

    @created.setter
    def created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[pulumi.Input[int]]:
        """
        The default time to live for match list items added through the UI. Specified in seconds.
        """
        return pulumi.get(self, "default_ttl")

    @default_ttl.setter
    def default_ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "default_ttl", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Match list item description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CseMatchListItemArgs']]]]:
        """
        List of match list items. See match_list_item schema for details.
        """
        return pulumi.get(self, "items")

    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CseMatchListItemArgs']]]]):
        pulumi.set(self, "items", value)

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "last_updated")

    @last_updated.setter
    def last_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_updated", value)

    @property
    @pulumi.getter(name="lastUpdatedBy")
    def last_updated_by(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "last_updated_by")

    @last_updated_by.setter
    def last_updated_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_updated_by", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Match list name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="targetColumn")
    def target_column(self) -> Optional[pulumi.Input[str]]:
        """
        Target column. (possible values: Hostname, FileHash, Url, SrcIp, DstIp, Domain, Username, Ip, Asn, Isp, Org, SrcAsn, SrcIsp, SrcOrg, DstAsn, DstIsp, DstOrg or any custom column.)
        """
        return pulumi.get(self, "target_column")

    @target_column.setter
    def target_column(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_column", value)


class CseMatchList(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_ttl: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 items: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CseMatchListItemArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 target_column: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Sumologic CSE Match List.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        match_list = sumologic.CseMatchList("matchList",
            default_ttl=10800,
            description="Match list description",
            items=[sumologic.CseMatchListItemArgs(
                description="IP address",
                expiration="2022-02-27T04:00:00",
                value="192.168.0.1",
            )],
            target_column="SrcIp")
        ```

        ## Import

        Match List can be imported using the field id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/cseMatchList:CseMatchList match_list id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] default_ttl: The default time to live for match list items added through the UI. Specified in seconds.
        :param pulumi.Input[str] description: Match list item description.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CseMatchListItemArgs']]]] items: List of match list items. See match_list_item schema for details.
        :param pulumi.Input[str] name: Match list name.
        :param pulumi.Input[str] target_column: Target column. (possible values: Hostname, FileHash, Url, SrcIp, DstIp, Domain, Username, Ip, Asn, Isp, Org, SrcAsn, SrcIsp, SrcOrg, DstAsn, DstIsp, DstOrg or any custom column.)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CseMatchListArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Sumologic CSE Match List.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        match_list = sumologic.CseMatchList("matchList",
            default_ttl=10800,
            description="Match list description",
            items=[sumologic.CseMatchListItemArgs(
                description="IP address",
                expiration="2022-02-27T04:00:00",
                value="192.168.0.1",
            )],
            target_column="SrcIp")
        ```

        ## Import

        Match List can be imported using the field id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/cseMatchList:CseMatchList match_list id
        ```

        :param str resource_name: The name of the resource.
        :param CseMatchListArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CseMatchListArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_ttl: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 items: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CseMatchListItemArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 target_column: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CseMatchListArgs.__new__(CseMatchListArgs)

            __props__.__dict__["default_ttl"] = default_ttl
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            __props__.__dict__["items"] = items
            __props__.__dict__["name"] = name
            if target_column is None and not opts.urn:
                raise TypeError("Missing required property 'target_column'")
            __props__.__dict__["target_column"] = target_column
            __props__.__dict__["created"] = None
            __props__.__dict__["created_by"] = None
            __props__.__dict__["last_updated"] = None
            __props__.__dict__["last_updated_by"] = None
        super(CseMatchList, __self__).__init__(
            'sumologic:index/cseMatchList:CseMatchList',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created: Optional[pulumi.Input[str]] = None,
            created_by: Optional[pulumi.Input[str]] = None,
            default_ttl: Optional[pulumi.Input[int]] = None,
            description: Optional[pulumi.Input[str]] = None,
            items: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CseMatchListItemArgs']]]]] = None,
            last_updated: Optional[pulumi.Input[str]] = None,
            last_updated_by: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            target_column: Optional[pulumi.Input[str]] = None) -> 'CseMatchList':
        """
        Get an existing CseMatchList resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] default_ttl: The default time to live for match list items added through the UI. Specified in seconds.
        :param pulumi.Input[str] description: Match list item description.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CseMatchListItemArgs']]]] items: List of match list items. See match_list_item schema for details.
        :param pulumi.Input[str] name: Match list name.
        :param pulumi.Input[str] target_column: Target column. (possible values: Hostname, FileHash, Url, SrcIp, DstIp, Domain, Username, Ip, Asn, Isp, Org, SrcAsn, SrcIsp, SrcOrg, DstAsn, DstIsp, DstOrg or any custom column.)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CseMatchListState.__new__(_CseMatchListState)

        __props__.__dict__["created"] = created
        __props__.__dict__["created_by"] = created_by
        __props__.__dict__["default_ttl"] = default_ttl
        __props__.__dict__["description"] = description
        __props__.__dict__["items"] = items
        __props__.__dict__["last_updated"] = last_updated
        __props__.__dict__["last_updated_by"] = last_updated_by
        __props__.__dict__["name"] = name
        __props__.__dict__["target_column"] = target_column
        return CseMatchList(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> pulumi.Output[Optional[int]]:
        """
        The default time to live for match list items added through the UI. Specified in seconds.
        """
        return pulumi.get(self, "default_ttl")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Match list item description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def items(self) -> pulumi.Output[Optional[Sequence['outputs.CseMatchListItem']]]:
        """
        List of match list items. See match_list_item schema for details.
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> pulumi.Output[str]:
        return pulumi.get(self, "last_updated")

    @property
    @pulumi.getter(name="lastUpdatedBy")
    def last_updated_by(self) -> pulumi.Output[str]:
        return pulumi.get(self, "last_updated_by")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Match list name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="targetColumn")
    def target_column(self) -> pulumi.Output[str]:
        """
        Target column. (possible values: Hostname, FileHash, Url, SrcIp, DstIp, Domain, Username, Ip, Asn, Isp, Org, SrcAsn, SrcIsp, SrcOrg, DstAsn, DstIsp, DstOrg or any custom column.)
        """
        return pulumi.get(self, "target_column")

