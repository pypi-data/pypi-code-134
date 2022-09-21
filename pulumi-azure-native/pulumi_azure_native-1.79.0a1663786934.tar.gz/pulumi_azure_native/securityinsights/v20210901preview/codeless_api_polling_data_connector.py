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

__all__ = ['CodelessApiPollingDataConnectorArgs', 'CodelessApiPollingDataConnector']

@pulumi.input_type
class CodelessApiPollingDataConnectorArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 connector_ui_config: Optional[pulumi.Input['CodelessUiConnectorConfigPropertiesArgs']] = None,
                 data_connector_id: Optional[pulumi.Input[str]] = None,
                 polling_config: Optional[pulumi.Input['CodelessConnectorPollingConfigPropertiesArgs']] = None):
        """
        The set of arguments for constructing a CodelessApiPollingDataConnector resource.
        :param pulumi.Input[str] kind: The kind of the data connector
               Expected value is 'APIPolling'.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input['CodelessUiConnectorConfigPropertiesArgs'] connector_ui_config: Config to describe the instructions blade
        :param pulumi.Input[str] data_connector_id: Connector ID
        :param pulumi.Input['CodelessConnectorPollingConfigPropertiesArgs'] polling_config: Config to describe the polling instructions
        """
        pulumi.set(__self__, "kind", 'APIPolling')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if connector_ui_config is not None:
            pulumi.set(__self__, "connector_ui_config", connector_ui_config)
        if data_connector_id is not None:
            pulumi.set(__self__, "data_connector_id", data_connector_id)
        if polling_config is not None:
            pulumi.set(__self__, "polling_config", polling_config)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The kind of the data connector
        Expected value is 'APIPolling'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

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
    @pulumi.getter(name="connectorUiConfig")
    def connector_ui_config(self) -> Optional[pulumi.Input['CodelessUiConnectorConfigPropertiesArgs']]:
        """
        Config to describe the instructions blade
        """
        return pulumi.get(self, "connector_ui_config")

    @connector_ui_config.setter
    def connector_ui_config(self, value: Optional[pulumi.Input['CodelessUiConnectorConfigPropertiesArgs']]):
        pulumi.set(self, "connector_ui_config", value)

    @property
    @pulumi.getter(name="dataConnectorId")
    def data_connector_id(self) -> Optional[pulumi.Input[str]]:
        """
        Connector ID
        """
        return pulumi.get(self, "data_connector_id")

    @data_connector_id.setter
    def data_connector_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_connector_id", value)

    @property
    @pulumi.getter(name="pollingConfig")
    def polling_config(self) -> Optional[pulumi.Input['CodelessConnectorPollingConfigPropertiesArgs']]:
        """
        Config to describe the polling instructions
        """
        return pulumi.get(self, "polling_config")

    @polling_config.setter
    def polling_config(self, value: Optional[pulumi.Input['CodelessConnectorPollingConfigPropertiesArgs']]):
        pulumi.set(self, "polling_config", value)


class CodelessApiPollingDataConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connector_ui_config: Optional[pulumi.Input[pulumi.InputType['CodelessUiConnectorConfigPropertiesArgs']]] = None,
                 data_connector_id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 polling_config: Optional[pulumi.Input[pulumi.InputType['CodelessConnectorPollingConfigPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents Codeless API Polling data connector.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CodelessUiConnectorConfigPropertiesArgs']] connector_ui_config: Config to describe the instructions blade
        :param pulumi.Input[str] data_connector_id: Connector ID
        :param pulumi.Input[str] kind: The kind of the data connector
               Expected value is 'APIPolling'.
        :param pulumi.Input[pulumi.InputType['CodelessConnectorPollingConfigPropertiesArgs']] polling_config: Config to describe the polling instructions
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CodelessApiPollingDataConnectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents Codeless API Polling data connector.

        :param str resource_name: The name of the resource.
        :param CodelessApiPollingDataConnectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CodelessApiPollingDataConnectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connector_ui_config: Optional[pulumi.Input[pulumi.InputType['CodelessUiConnectorConfigPropertiesArgs']]] = None,
                 data_connector_id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 polling_config: Optional[pulumi.Input[pulumi.InputType['CodelessConnectorPollingConfigPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CodelessApiPollingDataConnectorArgs.__new__(CodelessApiPollingDataConnectorArgs)

            __props__.__dict__["connector_ui_config"] = connector_ui_config
            __props__.__dict__["data_connector_id"] = data_connector_id
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'APIPolling'
            __props__.__dict__["polling_config"] = polling_config
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:CodelessApiPollingDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20190101preview:CodelessApiPollingDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20200101:CodelessApiPollingDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20210301preview:CodelessApiPollingDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20211001:CodelessApiPollingDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:CodelessApiPollingDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:CodelessApiPollingDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:CodelessApiPollingDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:CodelessApiPollingDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:CodelessApiPollingDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:CodelessApiPollingDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220801:CodelessApiPollingDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:CodelessApiPollingDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:CodelessApiPollingDataConnector")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CodelessApiPollingDataConnector, __self__).__init__(
            'azure-native:securityinsights/v20210901preview:CodelessApiPollingDataConnector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CodelessApiPollingDataConnector':
        """
        Get an existing CodelessApiPollingDataConnector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CodelessApiPollingDataConnectorArgs.__new__(CodelessApiPollingDataConnectorArgs)

        __props__.__dict__["connector_ui_config"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["polling_config"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return CodelessApiPollingDataConnector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectorUiConfig")
    def connector_ui_config(self) -> pulumi.Output[Optional['outputs.CodelessUiConnectorConfigPropertiesResponse']]:
        """
        Config to describe the instructions blade
        """
        return pulumi.get(self, "connector_ui_config")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of the data connector
        Expected value is 'APIPolling'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pollingConfig")
    def polling_config(self) -> pulumi.Output[Optional['outputs.CodelessConnectorPollingConfigPropertiesResponse']]:
        """
        Config to describe the polling instructions
        """
        return pulumi.get(self, "polling_config")

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

