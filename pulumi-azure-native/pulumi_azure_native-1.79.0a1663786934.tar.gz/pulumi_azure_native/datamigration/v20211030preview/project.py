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

__all__ = ['ProjectArgs', 'Project']

@pulumi.input_type
class ProjectArgs:
    def __init__(__self__, *,
                 group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 source_platform: pulumi.Input[Union[str, 'ProjectSourcePlatform']],
                 target_platform: pulumi.Input[Union[str, 'ProjectTargetPlatform']],
                 azure_authentication_info: Optional[pulumi.Input[str]] = None,
                 databases_info: Optional[pulumi.Input[Sequence[pulumi.Input['DatabaseInfoArgs']]]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 source_connection_info: Optional[pulumi.Input[Union['MiSqlConnectionInfoArgs', 'MongoDbConnectionInfoArgs', 'MySqlConnectionInfoArgs', 'OracleConnectionInfoArgs', 'PostgreSqlConnectionInfoArgs', 'SqlConnectionInfoArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_connection_info: Optional[pulumi.Input[Union['MiSqlConnectionInfoArgs', 'MongoDbConnectionInfoArgs', 'MySqlConnectionInfoArgs', 'OracleConnectionInfoArgs', 'PostgreSqlConnectionInfoArgs', 'SqlConnectionInfoArgs']]] = None):
        """
        The set of arguments for constructing a Project resource.
        :param pulumi.Input[str] group_name: Name of the resource group
        :param pulumi.Input[str] service_name: Name of the service
        :param pulumi.Input[Union[str, 'ProjectSourcePlatform']] source_platform: Source platform for the project
        :param pulumi.Input[Union[str, 'ProjectTargetPlatform']] target_platform: Target platform for the project
        :param pulumi.Input[str] azure_authentication_info: Field that defines the Azure active directory application info, used to connect to the target Azure resource
        :param pulumi.Input[Sequence[pulumi.Input['DatabaseInfoArgs']]] databases_info: List of DatabaseInfo
        :param pulumi.Input[str] e_tag: HTTP strong entity tag value. This is ignored if submitted.
        :param pulumi.Input[str] project_name: Name of the project
        :param pulumi.Input[Union['MiSqlConnectionInfoArgs', 'MongoDbConnectionInfoArgs', 'MySqlConnectionInfoArgs', 'OracleConnectionInfoArgs', 'PostgreSqlConnectionInfoArgs', 'SqlConnectionInfoArgs']] source_connection_info: Information for connecting to source
        :param pulumi.Input[Union['MiSqlConnectionInfoArgs', 'MongoDbConnectionInfoArgs', 'MySqlConnectionInfoArgs', 'OracleConnectionInfoArgs', 'PostgreSqlConnectionInfoArgs', 'SqlConnectionInfoArgs']] target_connection_info: Information for connecting to target
        """
        pulumi.set(__self__, "group_name", group_name)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "source_platform", source_platform)
        pulumi.set(__self__, "target_platform", target_platform)
        if azure_authentication_info is not None:
            pulumi.set(__self__, "azure_authentication_info", azure_authentication_info)
        if databases_info is not None:
            pulumi.set(__self__, "databases_info", databases_info)
        if e_tag is not None:
            pulumi.set(__self__, "e_tag", e_tag)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project_name is not None:
            pulumi.set(__self__, "project_name", project_name)
        if source_connection_info is not None:
            pulumi.set(__self__, "source_connection_info", source_connection_info)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if target_connection_info is not None:
            pulumi.set(__self__, "target_connection_info", target_connection_info)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group
        """
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        Name of the service
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="sourcePlatform")
    def source_platform(self) -> pulumi.Input[Union[str, 'ProjectSourcePlatform']]:
        """
        Source platform for the project
        """
        return pulumi.get(self, "source_platform")

    @source_platform.setter
    def source_platform(self, value: pulumi.Input[Union[str, 'ProjectSourcePlatform']]):
        pulumi.set(self, "source_platform", value)

    @property
    @pulumi.getter(name="targetPlatform")
    def target_platform(self) -> pulumi.Input[Union[str, 'ProjectTargetPlatform']]:
        """
        Target platform for the project
        """
        return pulumi.get(self, "target_platform")

    @target_platform.setter
    def target_platform(self, value: pulumi.Input[Union[str, 'ProjectTargetPlatform']]):
        pulumi.set(self, "target_platform", value)

    @property
    @pulumi.getter(name="azureAuthenticationInfo")
    def azure_authentication_info(self) -> Optional[pulumi.Input[str]]:
        """
        Field that defines the Azure active directory application info, used to connect to the target Azure resource
        """
        return pulumi.get(self, "azure_authentication_info")

    @azure_authentication_info.setter
    def azure_authentication_info(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "azure_authentication_info", value)

    @property
    @pulumi.getter(name="databasesInfo")
    def databases_info(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DatabaseInfoArgs']]]]:
        """
        List of DatabaseInfo
        """
        return pulumi.get(self, "databases_info")

    @databases_info.setter
    def databases_info(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DatabaseInfoArgs']]]]):
        pulumi.set(self, "databases_info", value)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[str]]:
        """
        HTTP strong entity tag value. This is ignored if submitted.
        """
        return pulumi.get(self, "e_tag")

    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_tag", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the project
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_name", value)

    @property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> Optional[pulumi.Input[Union['MiSqlConnectionInfoArgs', 'MongoDbConnectionInfoArgs', 'MySqlConnectionInfoArgs', 'OracleConnectionInfoArgs', 'PostgreSqlConnectionInfoArgs', 'SqlConnectionInfoArgs']]]:
        """
        Information for connecting to source
        """
        return pulumi.get(self, "source_connection_info")

    @source_connection_info.setter
    def source_connection_info(self, value: Optional[pulumi.Input[Union['MiSqlConnectionInfoArgs', 'MongoDbConnectionInfoArgs', 'MySqlConnectionInfoArgs', 'OracleConnectionInfoArgs', 'PostgreSqlConnectionInfoArgs', 'SqlConnectionInfoArgs']]]):
        pulumi.set(self, "source_connection_info", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> Optional[pulumi.Input[Union['MiSqlConnectionInfoArgs', 'MongoDbConnectionInfoArgs', 'MySqlConnectionInfoArgs', 'OracleConnectionInfoArgs', 'PostgreSqlConnectionInfoArgs', 'SqlConnectionInfoArgs']]]:
        """
        Information for connecting to target
        """
        return pulumi.get(self, "target_connection_info")

    @target_connection_info.setter
    def target_connection_info(self, value: Optional[pulumi.Input[Union['MiSqlConnectionInfoArgs', 'MongoDbConnectionInfoArgs', 'MySqlConnectionInfoArgs', 'OracleConnectionInfoArgs', 'PostgreSqlConnectionInfoArgs', 'SqlConnectionInfoArgs']]]):
        pulumi.set(self, "target_connection_info", value)


class Project(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_authentication_info: Optional[pulumi.Input[str]] = None,
                 databases_info: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatabaseInfoArgs']]]]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 source_connection_info: Optional[pulumi.Input[Union[pulumi.InputType['MiSqlConnectionInfoArgs'], pulumi.InputType['MongoDbConnectionInfoArgs'], pulumi.InputType['MySqlConnectionInfoArgs'], pulumi.InputType['OracleConnectionInfoArgs'], pulumi.InputType['PostgreSqlConnectionInfoArgs'], pulumi.InputType['SqlConnectionInfoArgs']]]] = None,
                 source_platform: Optional[pulumi.Input[Union[str, 'ProjectSourcePlatform']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_connection_info: Optional[pulumi.Input[Union[pulumi.InputType['MiSqlConnectionInfoArgs'], pulumi.InputType['MongoDbConnectionInfoArgs'], pulumi.InputType['MySqlConnectionInfoArgs'], pulumi.InputType['OracleConnectionInfoArgs'], pulumi.InputType['PostgreSqlConnectionInfoArgs'], pulumi.InputType['SqlConnectionInfoArgs']]]] = None,
                 target_platform: Optional[pulumi.Input[Union[str, 'ProjectTargetPlatform']]] = None,
                 __props__=None):
        """
        A project resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] azure_authentication_info: Field that defines the Azure active directory application info, used to connect to the target Azure resource
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatabaseInfoArgs']]]] databases_info: List of DatabaseInfo
        :param pulumi.Input[str] e_tag: HTTP strong entity tag value. This is ignored if submitted.
        :param pulumi.Input[str] group_name: Name of the resource group
        :param pulumi.Input[str] project_name: Name of the project
        :param pulumi.Input[str] service_name: Name of the service
        :param pulumi.Input[Union[pulumi.InputType['MiSqlConnectionInfoArgs'], pulumi.InputType['MongoDbConnectionInfoArgs'], pulumi.InputType['MySqlConnectionInfoArgs'], pulumi.InputType['OracleConnectionInfoArgs'], pulumi.InputType['PostgreSqlConnectionInfoArgs'], pulumi.InputType['SqlConnectionInfoArgs']]] source_connection_info: Information for connecting to source
        :param pulumi.Input[Union[str, 'ProjectSourcePlatform']] source_platform: Source platform for the project
        :param pulumi.Input[Union[pulumi.InputType['MiSqlConnectionInfoArgs'], pulumi.InputType['MongoDbConnectionInfoArgs'], pulumi.InputType['MySqlConnectionInfoArgs'], pulumi.InputType['OracleConnectionInfoArgs'], pulumi.InputType['PostgreSqlConnectionInfoArgs'], pulumi.InputType['SqlConnectionInfoArgs']]] target_connection_info: Information for connecting to target
        :param pulumi.Input[Union[str, 'ProjectTargetPlatform']] target_platform: Target platform for the project
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A project resource

        :param str resource_name: The name of the resource.
        :param ProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_authentication_info: Optional[pulumi.Input[str]] = None,
                 databases_info: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatabaseInfoArgs']]]]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 source_connection_info: Optional[pulumi.Input[Union[pulumi.InputType['MiSqlConnectionInfoArgs'], pulumi.InputType['MongoDbConnectionInfoArgs'], pulumi.InputType['MySqlConnectionInfoArgs'], pulumi.InputType['OracleConnectionInfoArgs'], pulumi.InputType['PostgreSqlConnectionInfoArgs'], pulumi.InputType['SqlConnectionInfoArgs']]]] = None,
                 source_platform: Optional[pulumi.Input[Union[str, 'ProjectSourcePlatform']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_connection_info: Optional[pulumi.Input[Union[pulumi.InputType['MiSqlConnectionInfoArgs'], pulumi.InputType['MongoDbConnectionInfoArgs'], pulumi.InputType['MySqlConnectionInfoArgs'], pulumi.InputType['OracleConnectionInfoArgs'], pulumi.InputType['PostgreSqlConnectionInfoArgs'], pulumi.InputType['SqlConnectionInfoArgs']]]] = None,
                 target_platform: Optional[pulumi.Input[Union[str, 'ProjectTargetPlatform']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectArgs.__new__(ProjectArgs)

            __props__.__dict__["azure_authentication_info"] = azure_authentication_info
            __props__.__dict__["databases_info"] = databases_info
            __props__.__dict__["e_tag"] = e_tag
            if group_name is None and not opts.urn:
                raise TypeError("Missing required property 'group_name'")
            __props__.__dict__["group_name"] = group_name
            __props__.__dict__["location"] = location
            __props__.__dict__["project_name"] = project_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["source_connection_info"] = source_connection_info
            if source_platform is None and not opts.urn:
                raise TypeError("Missing required property 'source_platform'")
            __props__.__dict__["source_platform"] = source_platform
            __props__.__dict__["tags"] = tags
            __props__.__dict__["target_connection_info"] = target_connection_info
            if target_platform is None and not opts.urn:
                raise TypeError("Missing required property 'target_platform'")
            __props__.__dict__["target_platform"] = target_platform
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datamigration:Project"), pulumi.Alias(type_="azure-native:datamigration/v20171115preview:Project"), pulumi.Alias(type_="azure-native:datamigration/v20180315preview:Project"), pulumi.Alias(type_="azure-native:datamigration/v20180331preview:Project"), pulumi.Alias(type_="azure-native:datamigration/v20180419:Project"), pulumi.Alias(type_="azure-native:datamigration/v20180715preview:Project"), pulumi.Alias(type_="azure-native:datamigration/v20210630:Project"), pulumi.Alias(type_="azure-native:datamigration/v20220130preview:Project"), pulumi.Alias(type_="azure-native:datamigration/v20220330preview:Project")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Project, __self__).__init__(
            'azure-native:datamigration/v20211030preview:Project',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Project':
        """
        Get an existing Project resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProjectArgs.__new__(ProjectArgs)

        __props__.__dict__["azure_authentication_info"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["databases_info"] = None
        __props__.__dict__["e_tag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["source_connection_info"] = None
        __props__.__dict__["source_platform"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_connection_info"] = None
        __props__.__dict__["target_platform"] = None
        __props__.__dict__["type"] = None
        return Project(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureAuthenticationInfo")
    def azure_authentication_info(self) -> pulumi.Output[Optional[str]]:
        """
        Field that defines the Azure active directory application info, used to connect to the target Azure resource
        """
        return pulumi.get(self, "azure_authentication_info")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        UTC Date and time when project was created
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="databasesInfo")
    def databases_info(self) -> pulumi.Output[Optional[Sequence['outputs.DatabaseInfoResponse']]]:
        """
        List of DatabaseInfo
        """
        return pulumi.get(self, "databases_info")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        """
        HTTP strong entity tag value. This is ignored if submitted.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The project's provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Output[Optional[Any]]:
        """
        Information for connecting to source
        """
        return pulumi.get(self, "source_connection_info")

    @property
    @pulumi.getter(name="sourcePlatform")
    def source_platform(self) -> pulumi.Output[str]:
        """
        Source platform for the project
        """
        return pulumi.get(self, "source_platform")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Output[Optional[Any]]:
        """
        Information for connecting to target
        """
        return pulumi.get(self, "target_connection_info")

    @property
    @pulumi.getter(name="targetPlatform")
    def target_platform(self) -> pulumi.Output[str]:
        """
        Target platform for the project
        """
        return pulumi.get(self, "target_platform")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "type")

