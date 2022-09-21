# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ApiSchemaArgs', 'ApiSchema']

@pulumi.input_type
class ApiSchemaArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 content_type: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 definitions: Optional[Any] = None,
                 schema_id: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ApiSchema resource.
        :param pulumi.Input[str] api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
        :param pulumi.Input[str] content_type: Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). </br> - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` </br> - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` </br> - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` </br> - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param Any definitions: Types definitions. Used for Swagger/OpenAPI schemas only, null otherwise.
        :param pulumi.Input[str] schema_id: Schema identifier within an API. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] value: Json escaped string defining the document representing the Schema. Used for schemas other than Swagger/OpenAPI.
        """
        pulumi.set(__self__, "api_id", api_id)
        pulumi.set(__self__, "content_type", content_type)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if definitions is not None:
            pulumi.set(__self__, "definitions", definitions)
        if schema_id is not None:
            pulumi.set(__self__, "schema_id", schema_id)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        """
        API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
        """
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Input[str]:
        """
        Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). </br> - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` </br> - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` </br> - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` </br> - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml`.
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "content_type", value)

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
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def definitions(self) -> Optional[Any]:
        """
        Types definitions. Used for Swagger/OpenAPI schemas only, null otherwise.
        """
        return pulumi.get(self, "definitions")

    @definitions.setter
    def definitions(self, value: Optional[Any]):
        pulumi.set(self, "definitions", value)

    @property
    @pulumi.getter(name="schemaId")
    def schema_id(self) -> Optional[pulumi.Input[str]]:
        """
        Schema identifier within an API. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "schema_id")

    @schema_id.setter
    def schema_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_id", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        Json escaped string defining the document representing the Schema. Used for schemas other than Swagger/OpenAPI.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class ApiSchema(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 definitions: Optional[Any] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schema_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Schema Contract details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
        :param pulumi.Input[str] content_type: Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). </br> - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` </br> - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` </br> - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` </br> - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml`.
        :param Any definitions: Types definitions. Used for Swagger/OpenAPI schemas only, null otherwise.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] schema_id: Schema identifier within an API. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] value: Json escaped string defining the document representing the Schema. Used for schemas other than Swagger/OpenAPI.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiSchemaArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Schema Contract details.

        :param str resource_name: The name of the resource.
        :param ApiSchemaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiSchemaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 definitions: Optional[Any] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schema_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiSchemaArgs.__new__(ApiSchemaArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            if content_type is None and not opts.urn:
                raise TypeError("Missing required property 'content_type'")
            __props__.__dict__["content_type"] = content_type
            __props__.__dict__["definitions"] = definitions
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["schema_id"] = schema_id
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["value"] = value
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement:ApiSchema"), pulumi.Alias(type_="azure-native:apimanagement/v20170301:ApiSchema"), pulumi.Alias(type_="azure-native:apimanagement/v20180101:ApiSchema"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:ApiSchema"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:ApiSchema"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:ApiSchema"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:ApiSchema"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:ApiSchema"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:ApiSchema"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:ApiSchema"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:ApiSchema"), pulumi.Alias(type_="azure-native:apimanagement/v20211201preview:ApiSchema")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ApiSchema, __self__).__init__(
            'azure-native:apimanagement/v20191201:ApiSchema',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApiSchema':
        """
        Get an existing ApiSchema resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApiSchemaArgs.__new__(ApiSchemaArgs)

        __props__.__dict__["content_type"] = None
        __props__.__dict__["definitions"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["value"] = None
        return ApiSchema(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[str]:
        """
        Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). </br> - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` </br> - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` </br> - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` </br> - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml`.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def definitions(self) -> pulumi.Output[Optional[Any]]:
        """
        Types definitions. Used for Swagger/OpenAPI schemas only, null otherwise.
        """
        return pulumi.get(self, "definitions")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[Optional[str]]:
        """
        Json escaped string defining the document representing the Schema. Used for schemas other than Swagger/OpenAPI.
        """
        return pulumi.get(self, "value")

