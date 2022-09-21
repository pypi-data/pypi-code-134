'''
# AWS::ResilienceHub Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_resiliencehub as resiliencehub
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ResilienceHub construct libraries](https://constructs.dev/search?q=resiliencehub)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ResilienceHub resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ResilienceHub.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ResilienceHub](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ResilienceHub.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import constructs
from .. import (
    CfnResource as _CfnResource_9df397a6,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnApp(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_resiliencehub.CfnApp",
):
    '''A CloudFormation ``AWS::ResilienceHub::App``.

    Creates a Resilience Hub application. A Resilience Hub application is a collection of AWS resources structured to prevent and recover AWS application disruptions. To describe a Resilience Hub application, you provide an application name, resources from one or more–up to five– AWS CloudFormation stacks, and an appropriate resiliency policy.

    After you create a Resilience Hub application, you publish it so that you can run a resiliency assessment on it. You can then use recommendations from the assessment to improve resiliency by running another assessment, comparing results, and then iterating the process until you achieve your goals for recovery time objective (RTO) and recovery point objective (RPO).

    :cloudformationResource: AWS::ResilienceHub::App
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_resiliencehub as resiliencehub
        
        cfn_app = resiliencehub.CfnApp(self, "MyCfnApp",
            app_template_body="appTemplateBody",
            name="name",
            resource_mappings=[resiliencehub.CfnApp.ResourceMappingProperty(
                mapping_type="mappingType",
                physical_resource_id=resiliencehub.CfnApp.PhysicalResourceIdProperty(
                    identifier="identifier",
                    type="type",
        
                    # the properties below are optional
                    aws_account_id="awsAccountId",
                    aws_region="awsRegion"
                ),
        
                # the properties below are optional
                logical_stack_name="logicalStackName",
                resource_name="resourceName",
                terraform_source_name="terraformSourceName"
            )],
        
            # the properties below are optional
            app_assessment_schedule="appAssessmentSchedule",
            description="description",
            resiliency_policy_arn="resiliencyPolicyArn",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        app_template_body: builtins.str,
        name: builtins.str,
        resource_mappings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnApp.ResourceMappingProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        app_assessment_schedule: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        resiliency_policy_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::ResilienceHub::App``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param app_template_body: A string containing a full Resilience Hub app template body.
        :param name: The name for the application.
        :param resource_mappings: An array of ResourceMapping objects.
        :param app_assessment_schedule: ``AWS::ResilienceHub::App.AppAssessmentSchedule``.
        :param description: The optional description for an app.
        :param resiliency_policy_arn: The Amazon Resource Name (ARN) of the resiliency policy.
        :param tags: The tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnApp.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAppProps(
            app_template_body=app_template_body,
            name=name,
            resource_mappings=resource_mappings,
            app_assessment_schedule=app_assessment_schedule,
            description=description,
            resiliency_policy_arn=resiliency_policy_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnApp.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnApp._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAppArn")
    def attr_app_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the app.

        :cloudformationAttribute: AppArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags assigned to the resource.

        A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="appTemplateBody")
    def app_template_body(self) -> builtins.str:
        '''A string containing a full Resilience Hub app template body.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-apptemplatebody
        '''
        return typing.cast(builtins.str, jsii.get(self, "appTemplateBody"))

    @app_template_body.setter
    def app_template_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApp, "app_template_body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appTemplateBody", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApp, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceMappings")
    def resource_mappings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApp.ResourceMappingProperty", _IResolvable_da3f097b]]]:
        '''An array of ResourceMapping objects.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-resourcemappings
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApp.ResourceMappingProperty", _IResolvable_da3f097b]]], jsii.get(self, "resourceMappings"))

    @resource_mappings.setter
    def resource_mappings(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApp.ResourceMappingProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApp, "resource_mappings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceMappings", value)

    @builtins.property
    @jsii.member(jsii_name="appAssessmentSchedule")
    def app_assessment_schedule(self) -> typing.Optional[builtins.str]:
        '''``AWS::ResilienceHub::App.AppAssessmentSchedule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-appassessmentschedule
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appAssessmentSchedule"))

    @app_assessment_schedule.setter
    def app_assessment_schedule(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApp, "app_assessment_schedule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appAssessmentSchedule", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The optional description for an app.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApp, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="resiliencyPolicyArn")
    def resiliency_policy_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resiliency policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-resiliencypolicyarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resiliencyPolicyArn"))

    @resiliency_policy_arn.setter
    def resiliency_policy_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApp, "resiliency_policy_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resiliencyPolicyArn", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_resiliencehub.CfnApp.PhysicalResourceIdProperty",
        jsii_struct_bases=[],
        name_mapping={
            "identifier": "identifier",
            "type": "type",
            "aws_account_id": "awsAccountId",
            "aws_region": "awsRegion",
        },
    )
    class PhysicalResourceIdProperty:
        def __init__(
            self,
            *,
            identifier: builtins.str,
            type: builtins.str,
            aws_account_id: typing.Optional[builtins.str] = None,
            aws_region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines a physical resource identifier.

            :param identifier: The identifier of the physical resource.
            :param type: Specifies the type of physical resource identifier. - **Arn** - The resource identifier is an Amazon Resource Name (ARN) . - **Native** - The resource identifier is a Resilience Hub-native identifier.
            :param aws_account_id: The AWS account that owns the physical resource.
            :param aws_region: The AWS Region that the physical resource is located in.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_resiliencehub as resiliencehub
                
                physical_resource_id_property = resiliencehub.CfnApp.PhysicalResourceIdProperty(
                    identifier="identifier",
                    type="type",
                
                    # the properties below are optional
                    aws_account_id="awsAccountId",
                    aws_region="awsRegion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApp.PhysicalResourceIdProperty.__init__)
                check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
            self._values: typing.Dict[str, typing.Any] = {
                "identifier": identifier,
                "type": type,
            }
            if aws_account_id is not None:
                self._values["aws_account_id"] = aws_account_id
            if aws_region is not None:
                self._values["aws_region"] = aws_region

        @builtins.property
        def identifier(self) -> builtins.str:
            '''The identifier of the physical resource.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html#cfn-resiliencehub-app-physicalresourceid-identifier
            '''
            result = self._values.get("identifier")
            assert result is not None, "Required property 'identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''Specifies the type of physical resource identifier.

            - **Arn** - The resource identifier is an Amazon Resource Name (ARN) .
            - **Native** - The resource identifier is a Resilience Hub-native identifier.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html#cfn-resiliencehub-app-physicalresourceid-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def aws_account_id(self) -> typing.Optional[builtins.str]:
            '''The AWS account that owns the physical resource.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html#cfn-resiliencehub-app-physicalresourceid-awsaccountid
            '''
            result = self._values.get("aws_account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def aws_region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region that the physical resource is located in.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html#cfn-resiliencehub-app-physicalresourceid-awsregion
            '''
            result = self._values.get("aws_region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PhysicalResourceIdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_resiliencehub.CfnApp.ResourceMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "mapping_type": "mappingType",
            "physical_resource_id": "physicalResourceId",
            "logical_stack_name": "logicalStackName",
            "resource_name": "resourceName",
            "terraform_source_name": "terraformSourceName",
        },
    )
    class ResourceMappingProperty:
        def __init__(
            self,
            *,
            mapping_type: builtins.str,
            physical_resource_id: typing.Union[typing.Union["CfnApp.PhysicalResourceIdProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
            logical_stack_name: typing.Optional[builtins.str] = None,
            resource_name: typing.Optional[builtins.str] = None,
            terraform_source_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines a resource mapping.

            :param mapping_type: Specifies the type of resource mapping. - **AppRegistryApp** - The resource is mapped to another application. The name of the application is contained in the ``appRegistryAppName`` property. - **CfnStack** - The resource is mapped to a CloudFormation stack. The name of the CloudFormation stack is contained in the ``logicalStackName`` property. - **Resource** - The resource is mapped to another resource. The name of the resource is contained in the ``resourceName`` property. - **ResourceGroup** - The resource is mapped to a resource group. The name of the resource group is contained in the ``resourceGroupName`` property.
            :param physical_resource_id: The identifier of this resource.
            :param logical_stack_name: The name of the CloudFormation stack this resource is mapped to.
            :param resource_name: The name of the resource this resource is mapped to.
            :param terraform_source_name: ``CfnApp.ResourceMappingProperty.TerraformSourceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_resiliencehub as resiliencehub
                
                resource_mapping_property = resiliencehub.CfnApp.ResourceMappingProperty(
                    mapping_type="mappingType",
                    physical_resource_id=resiliencehub.CfnApp.PhysicalResourceIdProperty(
                        identifier="identifier",
                        type="type",
                
                        # the properties below are optional
                        aws_account_id="awsAccountId",
                        aws_region="awsRegion"
                    ),
                
                    # the properties below are optional
                    logical_stack_name="logicalStackName",
                    resource_name="resourceName",
                    terraform_source_name="terraformSourceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApp.ResourceMappingProperty.__init__)
                check_type(argname="argument mapping_type", value=mapping_type, expected_type=type_hints["mapping_type"])
                check_type(argname="argument physical_resource_id", value=physical_resource_id, expected_type=type_hints["physical_resource_id"])
                check_type(argname="argument logical_stack_name", value=logical_stack_name, expected_type=type_hints["logical_stack_name"])
                check_type(argname="argument resource_name", value=resource_name, expected_type=type_hints["resource_name"])
                check_type(argname="argument terraform_source_name", value=terraform_source_name, expected_type=type_hints["terraform_source_name"])
            self._values: typing.Dict[str, typing.Any] = {
                "mapping_type": mapping_type,
                "physical_resource_id": physical_resource_id,
            }
            if logical_stack_name is not None:
                self._values["logical_stack_name"] = logical_stack_name
            if resource_name is not None:
                self._values["resource_name"] = resource_name
            if terraform_source_name is not None:
                self._values["terraform_source_name"] = terraform_source_name

        @builtins.property
        def mapping_type(self) -> builtins.str:
            '''Specifies the type of resource mapping.

            - **AppRegistryApp** - The resource is mapped to another application. The name of the application is contained in the ``appRegistryAppName`` property.
            - **CfnStack** - The resource is mapped to a CloudFormation stack. The name of the CloudFormation stack is contained in the ``logicalStackName`` property.
            - **Resource** - The resource is mapped to another resource. The name of the resource is contained in the ``resourceName`` property.
            - **ResourceGroup** - The resource is mapped to a resource group. The name of the resource group is contained in the ``resourceGroupName`` property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-mappingtype
            '''
            result = self._values.get("mapping_type")
            assert result is not None, "Required property 'mapping_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def physical_resource_id(
            self,
        ) -> typing.Union["CfnApp.PhysicalResourceIdProperty", _IResolvable_da3f097b]:
            '''The identifier of this resource.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-physicalresourceid
            '''
            result = self._values.get("physical_resource_id")
            assert result is not None, "Required property 'physical_resource_id' is missing"
            return typing.cast(typing.Union["CfnApp.PhysicalResourceIdProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def logical_stack_name(self) -> typing.Optional[builtins.str]:
            '''The name of the CloudFormation stack this resource is mapped to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-logicalstackname
            '''
            result = self._values.get("logical_stack_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_name(self) -> typing.Optional[builtins.str]:
            '''The name of the resource this resource is mapped to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-resourcename
            '''
            result = self._values.get("resource_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def terraform_source_name(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.ResourceMappingProperty.TerraformSourceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-terraformsourcename
            '''
            result = self._values.get("terraform_source_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_resiliencehub.CfnAppProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_template_body": "appTemplateBody",
        "name": "name",
        "resource_mappings": "resourceMappings",
        "app_assessment_schedule": "appAssessmentSchedule",
        "description": "description",
        "resiliency_policy_arn": "resiliencyPolicyArn",
        "tags": "tags",
    },
)
class CfnAppProps:
    def __init__(
        self,
        *,
        app_template_body: builtins.str,
        name: builtins.str,
        resource_mappings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnApp.ResourceMappingProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        app_assessment_schedule: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        resiliency_policy_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApp``.

        :param app_template_body: A string containing a full Resilience Hub app template body.
        :param name: The name for the application.
        :param resource_mappings: An array of ResourceMapping objects.
        :param app_assessment_schedule: ``AWS::ResilienceHub::App.AppAssessmentSchedule``.
        :param description: The optional description for an app.
        :param resiliency_policy_arn: The Amazon Resource Name (ARN) of the resiliency policy.
        :param tags: The tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_resiliencehub as resiliencehub
            
            cfn_app_props = resiliencehub.CfnAppProps(
                app_template_body="appTemplateBody",
                name="name",
                resource_mappings=[resiliencehub.CfnApp.ResourceMappingProperty(
                    mapping_type="mappingType",
                    physical_resource_id=resiliencehub.CfnApp.PhysicalResourceIdProperty(
                        identifier="identifier",
                        type="type",
            
                        # the properties below are optional
                        aws_account_id="awsAccountId",
                        aws_region="awsRegion"
                    ),
            
                    # the properties below are optional
                    logical_stack_name="logicalStackName",
                    resource_name="resourceName",
                    terraform_source_name="terraformSourceName"
                )],
            
                # the properties below are optional
                app_assessment_schedule="appAssessmentSchedule",
                description="description",
                resiliency_policy_arn="resiliencyPolicyArn",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAppProps.__init__)
            check_type(argname="argument app_template_body", value=app_template_body, expected_type=type_hints["app_template_body"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_mappings", value=resource_mappings, expected_type=type_hints["resource_mappings"])
            check_type(argname="argument app_assessment_schedule", value=app_assessment_schedule, expected_type=type_hints["app_assessment_schedule"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument resiliency_policy_arn", value=resiliency_policy_arn, expected_type=type_hints["resiliency_policy_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "app_template_body": app_template_body,
            "name": name,
            "resource_mappings": resource_mappings,
        }
        if app_assessment_schedule is not None:
            self._values["app_assessment_schedule"] = app_assessment_schedule
        if description is not None:
            self._values["description"] = description
        if resiliency_policy_arn is not None:
            self._values["resiliency_policy_arn"] = resiliency_policy_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def app_template_body(self) -> builtins.str:
        '''A string containing a full Resilience Hub app template body.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-apptemplatebody
        '''
        result = self._values.get("app_template_body")
        assert result is not None, "Required property 'app_template_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_mappings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnApp.ResourceMappingProperty, _IResolvable_da3f097b]]]:
        '''An array of ResourceMapping objects.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-resourcemappings
        '''
        result = self._values.get("resource_mappings")
        assert result is not None, "Required property 'resource_mappings' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnApp.ResourceMappingProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def app_assessment_schedule(self) -> typing.Optional[builtins.str]:
        '''``AWS::ResilienceHub::App.AppAssessmentSchedule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-appassessmentschedule
        '''
        result = self._values.get("app_assessment_schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The optional description for an app.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resiliency_policy_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resiliency policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-resiliencypolicyarn
        '''
        result = self._values.get("resiliency_policy_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags assigned to the resource.

        A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResiliencyPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_resiliencehub.CfnResiliencyPolicy",
):
    '''A CloudFormation ``AWS::ResilienceHub::ResiliencyPolicy``.

    Defines a resiliency policy.

    :cloudformationResource: AWS::ResilienceHub::ResiliencyPolicy
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_resiliencehub as resiliencehub
        
        cfn_resiliency_policy = resiliencehub.CfnResiliencyPolicy(self, "MyCfnResiliencyPolicy",
            policy={
                "policy_key": resiliencehub.CfnResiliencyPolicy.FailurePolicyProperty(
                    rpo_in_secs=123,
                    rto_in_secs=123
                )
            },
            policy_name="policyName",
            tier="tier",
        
            # the properties below are optional
            data_location_constraint="dataLocationConstraint",
            policy_description="policyDescription",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        policy: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union["CfnResiliencyPolicy.FailurePolicyProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        policy_name: builtins.str,
        tier: builtins.str,
        data_location_constraint: typing.Optional[builtins.str] = None,
        policy_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::ResilienceHub::ResiliencyPolicy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param policy: The resiliency policy.
        :param policy_name: The name of the policy.
        :param tier: The tier for this resiliency policy, ranging from the highest severity ( ``MissionCritical`` ) to lowest ( ``NonCritical`` ).
        :param data_location_constraint: Specifies a high-level geographical location constraint for where your resilience policy data can be stored.
        :param policy_description: The description for the policy.
        :param tags: The tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnResiliencyPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResiliencyPolicyProps(
            policy=policy,
            policy_name=policy_name,
            tier=tier,
            data_location_constraint=data_location_constraint,
            policy_description=policy_description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnResiliencyPolicy.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnResiliencyPolicy._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyArn")
    def attr_policy_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resiliency policy.

        :cloudformationAttribute: PolicyArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPolicyArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags assigned to the resource.

        A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnResiliencyPolicy.FailurePolicyProperty", _IResolvable_da3f097b]]]:
        '''The resiliency policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-policy
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnResiliencyPolicy.FailurePolicyProperty", _IResolvable_da3f097b]]], jsii.get(self, "policy"))

    @policy.setter
    def policy(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnResiliencyPolicy.FailurePolicyProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResiliencyPolicy, "policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of the policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-policyname
        '''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResiliencyPolicy, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        '''The tier for this resiliency policy, ranging from the highest severity ( ``MissionCritical`` ) to lowest ( ``NonCritical`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-tier
        '''
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResiliencyPolicy, "tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)

    @builtins.property
    @jsii.member(jsii_name="dataLocationConstraint")
    def data_location_constraint(self) -> typing.Optional[builtins.str]:
        '''Specifies a high-level geographical location constraint for where your resilience policy data can be stored.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-datalocationconstraint
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataLocationConstraint"))

    @data_location_constraint.setter
    def data_location_constraint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResiliencyPolicy, "data_location_constraint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataLocationConstraint", value)

    @builtins.property
    @jsii.member(jsii_name="policyDescription")
    def policy_description(self) -> typing.Optional[builtins.str]:
        '''The description for the policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-policydescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyDescription"))

    @policy_description.setter
    def policy_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResiliencyPolicy, "policy_description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDescription", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_resiliencehub.CfnResiliencyPolicy.FailurePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"rpo_in_secs": "rpoInSecs", "rto_in_secs": "rtoInSecs"},
    )
    class FailurePolicyProperty:
        def __init__(
            self,
            *,
            rpo_in_secs: jsii.Number,
            rto_in_secs: jsii.Number,
        ) -> None:
            '''Defines a failure policy.

            :param rpo_in_secs: The Recovery Point Objective (RPO), in seconds.
            :param rto_in_secs: The Recovery Time Objective (RTO), in seconds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-resiliencypolicy-failurepolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_resiliencehub as resiliencehub
                
                failure_policy_property = resiliencehub.CfnResiliencyPolicy.FailurePolicyProperty(
                    rpo_in_secs=123,
                    rto_in_secs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnResiliencyPolicy.FailurePolicyProperty.__init__)
                check_type(argname="argument rpo_in_secs", value=rpo_in_secs, expected_type=type_hints["rpo_in_secs"])
                check_type(argname="argument rto_in_secs", value=rto_in_secs, expected_type=type_hints["rto_in_secs"])
            self._values: typing.Dict[str, typing.Any] = {
                "rpo_in_secs": rpo_in_secs,
                "rto_in_secs": rto_in_secs,
            }

        @builtins.property
        def rpo_in_secs(self) -> jsii.Number:
            '''The Recovery Point Objective (RPO), in seconds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-resiliencypolicy-failurepolicy.html#cfn-resiliencehub-resiliencypolicy-failurepolicy-rpoinsecs
            '''
            result = self._values.get("rpo_in_secs")
            assert result is not None, "Required property 'rpo_in_secs' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def rto_in_secs(self) -> jsii.Number:
            '''The Recovery Time Objective (RTO), in seconds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-resiliencypolicy-failurepolicy.html#cfn-resiliencehub-resiliencypolicy-failurepolicy-rtoinsecs
            '''
            result = self._values.get("rto_in_secs")
            assert result is not None, "Required property 'rto_in_secs' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FailurePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_resiliencehub.CfnResiliencyPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy": "policy",
        "policy_name": "policyName",
        "tier": "tier",
        "data_location_constraint": "dataLocationConstraint",
        "policy_description": "policyDescription",
        "tags": "tags",
    },
)
class CfnResiliencyPolicyProps:
    def __init__(
        self,
        *,
        policy: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnResiliencyPolicy.FailurePolicyProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        policy_name: builtins.str,
        tier: builtins.str,
        data_location_constraint: typing.Optional[builtins.str] = None,
        policy_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnResiliencyPolicy``.

        :param policy: The resiliency policy.
        :param policy_name: The name of the policy.
        :param tier: The tier for this resiliency policy, ranging from the highest severity ( ``MissionCritical`` ) to lowest ( ``NonCritical`` ).
        :param data_location_constraint: Specifies a high-level geographical location constraint for where your resilience policy data can be stored.
        :param policy_description: The description for the policy.
        :param tags: The tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_resiliencehub as resiliencehub
            
            cfn_resiliency_policy_props = resiliencehub.CfnResiliencyPolicyProps(
                policy={
                    "policy_key": resiliencehub.CfnResiliencyPolicy.FailurePolicyProperty(
                        rpo_in_secs=123,
                        rto_in_secs=123
                    )
                },
                policy_name="policyName",
                tier="tier",
            
                # the properties below are optional
                data_location_constraint="dataLocationConstraint",
                policy_description="policyDescription",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnResiliencyPolicyProps.__init__)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument data_location_constraint", value=data_location_constraint, expected_type=type_hints["data_location_constraint"])
            check_type(argname="argument policy_description", value=policy_description, expected_type=type_hints["policy_description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "policy": policy,
            "policy_name": policy_name,
            "tier": tier,
        }
        if data_location_constraint is not None:
            self._values["data_location_constraint"] = data_location_constraint
        if policy_description is not None:
            self._values["policy_description"] = policy_description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def policy(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnResiliencyPolicy.FailurePolicyProperty, _IResolvable_da3f097b]]]:
        '''The resiliency policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnResiliencyPolicy.FailurePolicyProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The name of the policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tier(self) -> builtins.str:
        '''The tier for this resiliency policy, ranging from the highest severity ( ``MissionCritical`` ) to lowest ( ``NonCritical`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-tier
        '''
        result = self._values.get("tier")
        assert result is not None, "Required property 'tier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_location_constraint(self) -> typing.Optional[builtins.str]:
        '''Specifies a high-level geographical location constraint for where your resilience policy data can be stored.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-datalocationconstraint
        '''
        result = self._values.get("data_location_constraint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_description(self) -> typing.Optional[builtins.str]:
        '''The description for the policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-policydescription
        '''
        result = self._values.get("policy_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags assigned to the resource.

        A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResiliencyPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApp",
    "CfnAppProps",
    "CfnResiliencyPolicy",
    "CfnResiliencyPolicyProps",
]

publication.publish()
