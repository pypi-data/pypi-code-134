# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CloudToCloudSourceArgs', 'CloudToCloudSource']

@pulumi.input_type
class CloudToCloudSourceArgs:
    def __init__(__self__, *,
                 collector_id: pulumi.Input[int],
                 config: pulumi.Input[str],
                 schema_ref: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        """
        The set of arguments for constructing a CloudToCloudSource resource.
        :param pulumi.Input[str] config: This is a JSON object which contains the configuration parameters for the Source.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] schema_ref: Source schema details.
        """
        pulumi.set(__self__, "collector_id", collector_id)
        pulumi.set(__self__, "config", config)
        pulumi.set(__self__, "schema_ref", schema_ref)

    @property
    @pulumi.getter(name="collectorId")
    def collector_id(self) -> pulumi.Input[int]:
        return pulumi.get(self, "collector_id")

    @collector_id.setter
    def collector_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "collector_id", value)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Input[str]:
        """
        This is a JSON object which contains the configuration parameters for the Source.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: pulumi.Input[str]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter(name="schemaRef")
    def schema_ref(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        """
        Source schema details.
        """
        return pulumi.get(self, "schema_ref")

    @schema_ref.setter
    def schema_ref(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "schema_ref", value)


@pulumi.input_type
class _CloudToCloudSourceState:
    def __init__(__self__, *,
                 collector_id: Optional[pulumi.Input[int]] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 schema_ref: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering CloudToCloudSource resources.
        :param pulumi.Input[str] config: This is a JSON object which contains the configuration parameters for the Source.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] schema_ref: Source schema details.
        """
        if collector_id is not None:
            pulumi.set(__self__, "collector_id", collector_id)
        if config is not None:
            pulumi.set(__self__, "config", config)
        if schema_ref is not None:
            pulumi.set(__self__, "schema_ref", schema_ref)

    @property
    @pulumi.getter(name="collectorId")
    def collector_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "collector_id")

    @collector_id.setter
    def collector_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "collector_id", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[str]]:
        """
        This is a JSON object which contains the configuration parameters for the Source.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter(name="schemaRef")
    def schema_ref(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Source schema details.
        """
        return pulumi.get(self, "schema_ref")

    @schema_ref.setter
    def schema_ref(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "schema_ref", value)


class CloudToCloudSource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 collector_id: Optional[pulumi.Input[int]] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 schema_ref: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a [Sumologic Cloud-to-Cloud source][1].

        ## Supported Integrations

        List of available integrations along with their corresponding `JSON` templates is present [here](https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/Cloud-to-Cloud_Integration_Framework#Integrations)

        __IMPORTANT:__ The API credentials are stored in plain-text in the state. This is a potential security issue.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_sumologic as sumologic

        collector = sumologic.Collector("collector", description="Just testing this")
        okta_source = sumologic.CloudToCloudSource("oktaSource",
            collector_id=collector.id,
            schema_ref={
                "type": "Okta",
            },
            config=json.dumps({
                "name": "okta source",
                "domain": "dev-xxx-admin.okta.com",
                "collectAll": True,
                "apiKey": "xxx",
                "fields": {
                    "_siemForward": False,
                },
                "pollingInterval": 30,
            }))
        ```

        ## Import

        Cloud-to-Cloud sources can be imported using the collector and source IDs (`collector/source`), e.g.hcl

        ```sh
         $ pulumi import sumologic:index/cloudToCloudSource:CloudToCloudSource test 100000001/100000001
        ```

         Cloud-to-Cloud sources can be imported using the collector name and source name (`collectorName/sourceName`), e.g.hcl

        ```sh
         $ pulumi import sumologic:index/cloudToCloudSource:CloudToCloudSource test my-test-collector/my-test-source
        ```

         [1]https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/Cloud-to-Cloud_Integration_Framework [2]https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/Cloud-to-Cloud_Integration_Framework#Integrations

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] config: This is a JSON object which contains the configuration parameters for the Source.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] schema_ref: Source schema details.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CloudToCloudSourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a [Sumologic Cloud-to-Cloud source][1].

        ## Supported Integrations

        List of available integrations along with their corresponding `JSON` templates is present [here](https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/Cloud-to-Cloud_Integration_Framework#Integrations)

        __IMPORTANT:__ The API credentials are stored in plain-text in the state. This is a potential security issue.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_sumologic as sumologic

        collector = sumologic.Collector("collector", description="Just testing this")
        okta_source = sumologic.CloudToCloudSource("oktaSource",
            collector_id=collector.id,
            schema_ref={
                "type": "Okta",
            },
            config=json.dumps({
                "name": "okta source",
                "domain": "dev-xxx-admin.okta.com",
                "collectAll": True,
                "apiKey": "xxx",
                "fields": {
                    "_siemForward": False,
                },
                "pollingInterval": 30,
            }))
        ```

        ## Import

        Cloud-to-Cloud sources can be imported using the collector and source IDs (`collector/source`), e.g.hcl

        ```sh
         $ pulumi import sumologic:index/cloudToCloudSource:CloudToCloudSource test 100000001/100000001
        ```

         Cloud-to-Cloud sources can be imported using the collector name and source name (`collectorName/sourceName`), e.g.hcl

        ```sh
         $ pulumi import sumologic:index/cloudToCloudSource:CloudToCloudSource test my-test-collector/my-test-source
        ```

         [1]https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/Cloud-to-Cloud_Integration_Framework [2]https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/Cloud-to-Cloud_Integration_Framework#Integrations

        :param str resource_name: The name of the resource.
        :param CloudToCloudSourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudToCloudSourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 collector_id: Optional[pulumi.Input[int]] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 schema_ref: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CloudToCloudSourceArgs.__new__(CloudToCloudSourceArgs)

            if collector_id is None and not opts.urn:
                raise TypeError("Missing required property 'collector_id'")
            __props__.__dict__["collector_id"] = collector_id
            if config is None and not opts.urn:
                raise TypeError("Missing required property 'config'")
            __props__.__dict__["config"] = config
            if schema_ref is None and not opts.urn:
                raise TypeError("Missing required property 'schema_ref'")
            __props__.__dict__["schema_ref"] = schema_ref
        super(CloudToCloudSource, __self__).__init__(
            'sumologic:index/cloudToCloudSource:CloudToCloudSource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            collector_id: Optional[pulumi.Input[int]] = None,
            config: Optional[pulumi.Input[str]] = None,
            schema_ref: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'CloudToCloudSource':
        """
        Get an existing CloudToCloudSource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] config: This is a JSON object which contains the configuration parameters for the Source.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] schema_ref: Source schema details.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CloudToCloudSourceState.__new__(_CloudToCloudSourceState)

        __props__.__dict__["collector_id"] = collector_id
        __props__.__dict__["config"] = config
        __props__.__dict__["schema_ref"] = schema_ref
        return CloudToCloudSource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="collectorId")
    def collector_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "collector_id")

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[str]:
        """
        This is a JSON object which contains the configuration parameters for the Source.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="schemaRef")
    def schema_ref(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Source schema details.
        """
        return pulumi.get(self, "schema_ref")

