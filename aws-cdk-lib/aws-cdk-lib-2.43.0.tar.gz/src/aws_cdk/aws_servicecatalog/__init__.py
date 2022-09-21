'''
# AWS Service Catalog Construct Library

[AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/dg/what-is-service-catalog.html)
enables organizations to create and manage catalogs of products for their end users that are approved for use on AWS.

## Table Of Contents

* [Portfolio](#portfolio)

  * [Granting access to a portfolio](#granting-access-to-a-portfolio)
  * [Sharing a portfolio with another AWS account](#sharing-a-portfolio-with-another-aws-account)
* [Product](#product)

  * [Creating a product from a local asset](#creating-a-product-from-local-asset)
  * [Creating a product from a stack](#creating-a-product-from-a-stack)
  * [Creating a Product from a stack with a history of previous versions](#creating-a-product-from-a-stack-with-a-history-of-all-previous-versions)
  * [Adding a product to a portfolio](#adding-a-product-to-a-portfolio)
* [TagOptions](#tag-options)
* [Constraints](#constraints)

  * [Tag update constraint](#tag-update-constraint)
  * [Notify on stack events](#notify-on-stack-events)
  * [CloudFormation template parameters constraint](#cloudformation-template-parameters-constraint)
  * [Set launch role](#set-launch-role)
  * [Deploy with StackSets](#deploy-with-stacksets)

The `@aws-cdk/aws-servicecatalog` package contains resources that enable users to automate governance and management of their AWS resources at scale.

```python
import aws_cdk.aws_servicecatalog as servicecatalog
```

## Portfolio

AWS Service Catalog portfolios allow administrators to organize, manage, and distribute cloud resources for their end users.
Using the CDK, a new portfolio can be created with the `Portfolio` construct:

```python
servicecatalog.Portfolio(self, "Portfolio",
    display_name="MyPortfolio",
    provider_name="MyTeam"
)
```

You can also specify optional metadata properties such as `description` and `messageLanguage`
to help better catalog and manage your portfolios.

```python
servicecatalog.Portfolio(self, "Portfolio",
    display_name="MyFirstPortfolio",
    provider_name="SCAdmin",
    description="Portfolio for a project",
    message_language=servicecatalog.MessageLanguage.EN
)
```

Read more at [Creating and Managing Portfolios](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios.html).

To reference an existing portfolio into your CDK application, use the `Portfolio.fromPortfolioArn()` factory method:

```python
portfolio = servicecatalog.Portfolio.from_portfolio_arn(self, "ReferencedPortfolio", "arn:aws:catalog:region:account-id:portfolio/port-abcdefghi")
```

### Granting access to a portfolio

You can grant access to and manage the `IAM` users, groups, or roles that have access to the products within a portfolio.
Entities with granted access will be able to utilize the portfolios resources and products via the console or AWS CLI.
Once resources are deployed end users will be able to access them via the console or service catalog CLI.

```python
import aws_cdk.aws_iam as iam

# portfolio: servicecatalog.Portfolio


user = iam.User(self, "User")
portfolio.give_access_to_user(user)

role = iam.Role(self, "Role",
    assumed_by=iam.AccountRootPrincipal()
)
portfolio.give_access_to_role(role)

group = iam.Group(self, "Group")
portfolio.give_access_to_group(group)
```

### Sharing a portfolio with another AWS account

You can use account-to-account sharing to distribute a reference to your portfolio to other AWS accounts by passing the recipient account number.
After the share is initiated, the recipient account can accept the share via CLI or console by importing the portfolio ID.
Changes made to the shared portfolio will automatically propagate to recipients.

```python
# portfolio: servicecatalog.Portfolio

portfolio.share_with_account("012345678901")
```

## Product

Products are version friendly infrastructure-as-code templates that admins create and add to portfolios for end users to provision and create AWS resources.
Service Catalog supports products from AWS Marketplace or ones defined by a CloudFormation template.
The CDK currently only supports adding products of type CloudFormation.
Using the CDK, a new Product can be created with the `CloudFormationProduct` construct.
You can use `CloudFormationTemplate.fromUrl` to create a Product from a CloudFormation template directly from a URL that points to the template in S3, GitHub, or CodeCommit:

```python
product = servicecatalog.CloudFormationProduct(self, "MyFirstProduct",
    product_name="My Product",
    owner="Product Owner",
    product_versions=[servicecatalog.CloudFormationProductVersion(
        product_version_name="v1",
        cloud_formation_template=servicecatalog.CloudFormationTemplate.from_url("https://raw.githubusercontent.com/awslabs/aws-cloudformation-templates/master/aws/services/ServiceCatalog/Product.yaml")
    )
    ]
)
```

### Creating a product from a local asset

A `CloudFormationProduct` can also be created by using a CloudFormation template held locally on disk using Assets.
Assets are files that are uploaded to an S3 Bucket before deployment.
`CloudFormationTemplate.fromAsset` can be utilized to create a Product by passing the path to a local template file on your disk:

```python
import path as path


product = servicecatalog.CloudFormationProduct(self, "Product",
    product_name="My Product",
    owner="Product Owner",
    product_versions=[servicecatalog.CloudFormationProductVersion(
        product_version_name="v1",
        cloud_formation_template=servicecatalog.CloudFormationTemplate.from_url("https://raw.githubusercontent.com/awslabs/aws-cloudformation-templates/master/aws/services/ServiceCatalog/Product.yaml")
    ), servicecatalog.CloudFormationProductVersion(
        product_version_name="v2",
        cloud_formation_template=servicecatalog.CloudFormationTemplate.from_asset(path.join(__dirname, "development-environment.template.json"))
    )
    ]
)
```

### Creating a product from a stack

You can create a Service Catalog `CloudFormationProduct` entirely defined with CDK code using a service catalog `ProductStack`.
A separate child stack for your product is created and you can add resources like you would for any other CDK stack,
such as an S3 Bucket, IAM roles, and EC2 instances. This stack is passed in as a product version to your
product.  This will not create a separate CloudFormation stack during deployment.

```python
import aws_cdk.aws_s3 as s3
import aws_cdk as cdk


class S3BucketProduct(servicecatalog.ProductStack):
    def __init__(self, scope, id):
        super().__init__(scope, id)

        s3.Bucket(self, "BucketProduct")

product = servicecatalog.CloudFormationProduct(self, "Product",
    product_name="My Product",
    owner="Product Owner",
    product_versions=[servicecatalog.CloudFormationProductVersion(
        product_version_name="v1",
        cloud_formation_template=servicecatalog.CloudFormationTemplate.from_product_stack(S3BucketProduct(self, "S3BucketProduct"))
    )
    ]
)
```

### Creating a Product from a stack with a history of previous versions

The default behavior of Service Catalog is to overwrite each product version upon deployment.
This applies to Product Stacks as well, where only the latest changes to your Product Stack will
be deployed.
To keep a history of the revisions of a ProductStack available in Service Catalog,
you would need to define a ProductStack for each historical copy.

You can instead create a `ProductStackHistory` to maintain snapshots of all previous versions.
The `ProductStackHistory` can be created by passing the base `productStack`,
a `currentVersionName` for your current version and a `locked` boolean.
The `locked` boolean which when set to true will prevent your `currentVersionName`
from being overwritten when there is an existing snapshot for that version.

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_s3 as s3
import aws_cdk as cdk


class S3BucketProduct(servicecatalog.ProductStack):
    def __init__(self, scope, id):
        super().__init__(scope, id)

        s3.Bucket(self, "BucketProduct")

product_stack_history = servicecatalog.ProductStackHistory(self, "ProductStackHistory",
    product_stack=S3BucketProduct(self, "S3BucketProduct"),
    current_version_name="v1",
    current_version_locked=True
)
```

We can deploy the current version `v1` by using `productStackHistory.currentVersion()`

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_s3 as s3
import aws_cdk as cdk


class S3BucketProduct(servicecatalog.ProductStack):
    def __init__(self, scope, id):
        super().__init__(scope, id)

        s3.Bucket(self, "BucketProductV2")

product_stack_history = servicecatalog.ProductStackHistory(self, "ProductStackHistory",
    product_stack=S3BucketProduct(self, "S3BucketProduct"),
    current_version_name="v2",
    current_version_locked=True
)

product = servicecatalog.CloudFormationProduct(self, "MyFirstProduct",
    product_name="My Product",
    owner="Product Owner",
    product_versions=[
        product_stack_history.current_version()
    ]
)
```

Using `ProductStackHistory` all deployed templates for the ProductStack will be written to disk,
so that they will still be available in the future as the definition of the `ProductStack` subclass changes over time.
**It is very important** that you commit these old versions to source control as these versions
determine whether a version has already been deployed and can also be deployed themselves.

After using `ProductStackHistory` to deploy version `v1` of your `ProductStack`, we
make changes to the `ProductStack` and update the `currentVersionName` to `v2`.
We still want our `v1` version to still be deployed, so we reference it by calling `productStackHistory.versionFromSnapshot('v1')`.

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_s3 as s3
import aws_cdk as cdk


class S3BucketProduct(servicecatalog.ProductStack):
    def __init__(self, scope, id):
        super().__init__(scope, id)

        s3.Bucket(self, "BucketProductV2")

product_stack_history = servicecatalog.ProductStackHistory(self, "ProductStackHistory",
    product_stack=S3BucketProduct(self, "S3BucketProduct"),
    current_version_name="v2",
    current_version_locked=True
)

product = servicecatalog.CloudFormationProduct(self, "MyFirstProduct",
    product_name="My Product",
    owner="Product Owner",
    product_versions=[
        product_stack_history.current_version(),
        product_stack_history.version_from_snapshot("v1")
    ]
)
```

### Adding a product to a portfolio

You add products to a portfolio to organize and distribute your catalog at scale.  Adding a product to a portfolio creates an association,
and the product will become visible within the portfolio side in both the Service Catalog console and AWS CLI.
You can add a product to multiple portfolios depending on your organizational structure and how you would like to group access to products.

```python
# portfolio: servicecatalog.Portfolio
# product: servicecatalog.CloudFormationProduct


portfolio.add_product(product)
```

## Tag Options

TagOptions allow administrators to easily manage tags on provisioned products by providing a template for a selection of tags that end users choose from.
TagOptions are created by specifying a tag key with a set of allowed values and can be associated with both portfolios and products.
When launching a product, both the TagOptions associated with the product and the containing portfolio are made available.

At the moment, TagOptions can only be deactivated in the console.

```python
# portfolio: servicecatalog.Portfolio
# product: servicecatalog.CloudFormationProduct


tag_options_for_portfolio = servicecatalog.TagOptions(self, "OrgTagOptions",
    allowed_values_for_tags={
        "Group": ["finance", "engineering", "marketing", "research"],
        "CostCenter": ["01", "02", "03"]
    }
)
portfolio.associate_tag_options(tag_options_for_portfolio)

tag_options_for_product = servicecatalog.TagOptions(self, "ProductTagOptions",
    allowed_values_for_tags={
        "Environment": ["dev", "alpha", "prod"]
    }
)
product.associate_tag_options(tag_options_for_product)
```

## Constraints

Constraints are governance gestures that you place on product-portfolio associations that allow you to manage minimal launch permissions, notifications, and other optional actions that end users can perform on products.
Using the CDK, if you do not explicitly associate a product to a portfolio and add a constraint, it will automatically add an association for you.

There are rules around how constraints are applied to portfolio-product associations.
For example, you can only have a single "launch role" constraint applied to a portfolio-product association.
If a misconfigured constraint is added, `synth` will fail with an error message.

Read more at [Service Catalog Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints.html).

### Tag update constraint

Tag update constraints allow or disallow end users to update tags on resources associated with an AWS Service Catalog product upon provisioning.
By default, if a Tag Update constraint is not configured, tag updating is not permitted.
If tag updating is allowed, then new tags associated with the product or portfolio will be applied to provisioned resources during a provisioned product update.

```python
# portfolio: servicecatalog.Portfolio
# product: servicecatalog.CloudFormationProduct


portfolio.add_product(product)
portfolio.constrain_tag_updates(product)
```

If you want to disable this feature later on, you can update it by setting the "allow" parameter to `false`:

```python
# portfolio: servicecatalog.Portfolio
# product: servicecatalog.CloudFormationProduct


# to disable tag updates:
portfolio.constrain_tag_updates(product,
    allow=False
)
```

### Notify on stack events

Allows users to subscribe an AWS `SNS` topic to a provisioned product's CloudFormation stack events.
When an end user provisions a product it creates a CloudFormation stack that notifies the subscribed topic on creation, edit, and delete events.
An individual `SNS` topic may only have a single subscription to any given portfolio-product association.

```python
import aws_cdk.aws_sns as sns

# portfolio: servicecatalog.Portfolio
# product: servicecatalog.CloudFormationProduct


topic1 = sns.Topic(self, "Topic1")
portfolio.notify_on_stack_events(product, topic1)

topic2 = sns.Topic(self, "Topic2")
portfolio.notify_on_stack_events(product, topic2,
    description="description for topic2"
)
```

### CloudFormation template parameters constraint

CloudFormation template parameter constraints allow you to configure the provisioning parameters that are available to end users when they launch a product.
Template constraint rules consist of one or more assertions that define the default and/or allowable values for a product’s provisioning parameters.
You can configure multiple parameter constraints to govern the different provisioning parameters within your products.
For example, a rule might define the `EC2` instance types that users can choose from when launching a product that includes one or more `EC2` instances.
Parameter rules have an optional `condition` field that allow for rule application to consider conditional evaluations.
If a `condition` is specified, all  assertions will be applied if the condition evaluates to true.
For information on rule-specific intrinsic functions to define rule conditions and assertions,
see [AWS Rule Functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-rules.html).

```python
import aws_cdk as cdk

# portfolio: servicecatalog.Portfolio
# product: servicecatalog.CloudFormationProduct


portfolio.constrain_cloud_formation_parameters(product,
    rule=servicecatalog.TemplateRule(
        rule_name="testInstanceType",
        condition=cdk.Fn.condition_equals(cdk.Fn.ref("Environment"), "test"),
        assertions=[servicecatalog.TemplateRuleAssertion(
            assert=cdk.Fn.condition_contains(["t2.micro", "t2.small"], cdk.Fn.ref("InstanceType")),
            description="For test environment, the instance type should be small"
        )]
    )
)
```

### Set launch role

Allows you to configure a specific `IAM` role that Service Catalog assumes on behalf of the end user when launching a product.
By setting a launch role constraint, you can maintain least permissions for an end user when launching a product.
For example, a launch role can grant permissions for specific resource creation like an `S3` bucket that the user.
The launch role must be assumed by the Service Catalog principal.
You can only have one launch role set for a portfolio-product association,
and you cannot set a launch role on a product that already has a StackSets deployment configured.

```python
import aws_cdk.aws_iam as iam

# portfolio: servicecatalog.Portfolio
# product: servicecatalog.CloudFormationProduct


launch_role = iam.Role(self, "LaunchRole",
    assumed_by=iam.ServicePrincipal("servicecatalog.amazonaws.com")
)

portfolio.set_launch_role(product, launch_role)
```

You can also set the launch role using just the name of a role which is locally deployed in end user accounts.
This is useful for when roles and users are separately managed outside of the CDK.
The given role must exist in both the account that creates the launch role constraint,
as well as in any end user accounts that wish to provision a product with the launch role.

You can do this by passing in the role with an explicitly set name:

```python
import aws_cdk.aws_iam as iam

# portfolio: servicecatalog.Portfolio
# product: servicecatalog.CloudFormationProduct


launch_role = iam.Role(self, "LaunchRole",
    role_name="MyRole",
    assumed_by=iam.ServicePrincipal("servicecatalog.amazonaws.com")
)

portfolio.set_local_launch_role(product, launch_role)
```

Or you can simply pass in a role name and CDK will create a role with that name that trusts service catalog in the account:

```python
import aws_cdk.aws_iam as iam

# portfolio: servicecatalog.Portfolio
# product: servicecatalog.CloudFormationProduct


role_name = "MyRole"
launch_role = portfolio.set_local_launch_role_name(product, role_name)
```

See [Launch Constraint](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-launch.html) documentation
to understand the permissions that launch roles need.

### Deploy with StackSets

A StackSets deployment constraint allows you to configure product deployment options using
[AWS CloudFormation StackSets](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-stacksets.html).
You can specify one or more accounts and regions into which stack instances will launch when the product is provisioned.
There is an additional field `allowStackSetInstanceOperations` that sets ability for end users to create, edit, or delete the stacks created by the StackSet.
By default, this field is set to `false`.
When launching a StackSets product, end users can select from the list of accounts and regions configured in the constraint to determine where the Stack Instances will deploy and the order of deployment.
You can only define one StackSets deployment configuration per portfolio-product association,
and you cannot both set a launch role and StackSets deployment configuration for an assocation.

```python
import aws_cdk.aws_iam as iam

# portfolio: servicecatalog.Portfolio
# product: servicecatalog.CloudFormationProduct


admin_role = iam.Role(self, "AdminRole",
    assumed_by=iam.AccountRootPrincipal()
)

portfolio.deploy_with_stack_sets(product,
    accounts=["012345678901", "012345678902", "012345678903"],
    regions=["us-west-1", "us-east-1", "us-west-2", "us-east-1"],
    admin_role=admin_role,
    execution_role_name="SCStackSetExecutionRole",  # Name of role deployed in end users accounts.
    allow_stack_set_instance_operations=True
)
```
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
    AssetHashType as _AssetHashType_05b67f2d,
    BundlingOptions as _BundlingOptions_588cc936,
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    ICfnRuleConditionExpression as _ICfnRuleConditionExpression_9aca991b,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    IgnoreMode as _IgnoreMode_655a98e8,
    Resource as _Resource_45bc6135,
    ResourceProps as _ResourceProps_15a65b4e,
    Stack as _Stack_2866e57f,
    SymlinkFollowMode as _SymlinkFollowMode_047ec1f6,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_iam import (
    IGrantable as _IGrantable_71c4f5de,
    IGroup as _IGroup_96daf542,
    IRole as _IRole_235f5d8e,
    IUser as _IUser_c32311f7,
)
from ..aws_s3_assets import AssetOptions as _AssetOptions_2aa69621
from ..aws_sns import ITopic as _ITopic_9eca4852


@jsii.implements(_IInspectable_c2943556)
class CfnAcceptedPortfolioShare(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnAcceptedPortfolioShare",
):
    '''A CloudFormation ``AWS::ServiceCatalog::AcceptedPortfolioShare``.

    Accepts an offer to share the specified portfolio.

    :cloudformationResource: AWS::ServiceCatalog::AcceptedPortfolioShare
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        cfn_accepted_portfolio_share = servicecatalog.CfnAcceptedPortfolioShare(self, "MyCfnAcceptedPortfolioShare",
            portfolio_id="portfolioId",
        
            # the properties below are optional
            accept_language="acceptLanguage"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        portfolio_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::AcceptedPortfolioShare``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param portfolio_id: The portfolio identifier.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAcceptedPortfolioShare.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAcceptedPortfolioShareProps(
            portfolio_id=portfolio_id, accept_language=accept_language
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAcceptedPortfolioShare.inspect)
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
            type_hints = typing.get_type_hints(CfnAcceptedPortfolioShare._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html#cfn-servicecatalog-acceptedportfolioshare-portfolioid
        '''
        return typing.cast(builtins.str, jsii.get(self, "portfolioId"))

    @portfolio_id.setter
    def portfolio_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAcceptedPortfolioShare, "portfolio_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portfolioId", value)

    @builtins.property
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html#cfn-servicecatalog-acceptedportfolioshare-acceptlanguage
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceptLanguage"))

    @accept_language.setter
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAcceptedPortfolioShare, "accept_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptLanguage", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnAcceptedPortfolioShareProps",
    jsii_struct_bases=[],
    name_mapping={"portfolio_id": "portfolioId", "accept_language": "acceptLanguage"},
)
class CfnAcceptedPortfolioShareProps:
    def __init__(
        self,
        *,
        portfolio_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAcceptedPortfolioShare``.

        :param portfolio_id: The portfolio identifier.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cfn_accepted_portfolio_share_props = servicecatalog.CfnAcceptedPortfolioShareProps(
                portfolio_id="portfolioId",
            
                # the properties below are optional
                accept_language="acceptLanguage"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAcceptedPortfolioShareProps.__init__)
            check_type(argname="argument portfolio_id", value=portfolio_id, expected_type=type_hints["portfolio_id"])
            check_type(argname="argument accept_language", value=accept_language, expected_type=type_hints["accept_language"])
        self._values: typing.Dict[str, typing.Any] = {
            "portfolio_id": portfolio_id,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html#cfn-servicecatalog-acceptedportfolioshare-portfolioid
        '''
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html#cfn-servicecatalog-acceptedportfolioshare-acceptlanguage
        '''
        result = self._values.get("accept_language")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAcceptedPortfolioShareProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnCloudFormationProduct(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnCloudFormationProduct",
):
    '''A CloudFormation ``AWS::ServiceCatalog::CloudFormationProduct``.

    Specifies a product.

    :cloudformationResource: AWS::ServiceCatalog::CloudFormationProduct
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        # info: Any
        
        cfn_cloud_formation_product = servicecatalog.CfnCloudFormationProduct(self, "MyCfnCloudFormationProduct",
            name="name",
            owner="owner",
            provisioning_artifact_parameters=[servicecatalog.CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty(
                info=info,
        
                # the properties below are optional
                description="description",
                disable_template_validation=False,
                name="name"
            )],
        
            # the properties below are optional
            accept_language="acceptLanguage",
            description="description",
            distributor="distributor",
            replace_provisioning_artifacts=False,
            support_description="supportDescription",
            support_email="supportEmail",
            support_url="supportUrl",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        owner: builtins.str,
        provisioning_artifact_parameters: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        distributor: typing.Optional[builtins.str] = None,
        replace_provisioning_artifacts: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        support_description: typing.Optional[builtins.str] = None,
        support_email: typing.Optional[builtins.str] = None,
        support_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::CloudFormationProduct``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the product.
        :param owner: The owner of the product.
        :param provisioning_artifact_parameters: The configuration of the provisioning artifact (also known as a version).
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param description: The description of the product.
        :param distributor: The distributor of the product.
        :param replace_provisioning_artifacts: This property is turned off by default. If turned off, you can update provisioning artifacts or product attributes (such as description, distributor, name, owner, and more) and the associated provisioning artifacts will retain the same unique identifier. Provisioning artifacts are matched within the CloudFormationProduct resource, and only those that have been updated will be changed. Provisioning artifacts are matched by a combinaton of provisioning artifact template URL and name. If turned on, provisioning artifacts will be given a new unique identifier when you update the product or provisioning artifacts.
        :param support_description: The support information about the product.
        :param support_email: The contact email for product support.
        :param support_url: The contact URL for product support. ``^https?:\\/\\//`` / is the pattern used to validate SupportUrl.
        :param tags: One or more tags.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCloudFormationProduct.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCloudFormationProductProps(
            name=name,
            owner=owner,
            provisioning_artifact_parameters=provisioning_artifact_parameters,
            accept_language=accept_language,
            description=description,
            distributor=distributor,
            replace_provisioning_artifacts=replace_provisioning_artifacts,
            support_description=support_description,
            support_email=support_email,
            support_url=support_url,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCloudFormationProduct.inspect)
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
            type_hints = typing.get_type_hints(CfnCloudFormationProduct._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrProductName")
    def attr_product_name(self) -> builtins.str:
        '''The name of the product.

        :cloudformationAttribute: ProductName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProductName"))

    @builtins.property
    @jsii.member(jsii_name="attrProvisioningArtifactIds")
    def attr_provisioning_artifact_ids(self) -> builtins.str:
        '''The IDs of the provisioning artifacts.

        :cloudformationAttribute: ProvisioningArtifactIds
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProvisioningArtifactIds"))

    @builtins.property
    @jsii.member(jsii_name="attrProvisioningArtifactNames")
    def attr_provisioning_artifact_names(self) -> builtins.str:
        '''The names of the provisioning artifacts.

        :cloudformationAttribute: ProvisioningArtifactNames
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProvisioningArtifactNames"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''One or more tags.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProduct, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        '''The owner of the product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-owner
        '''
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProduct, "owner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="provisioningArtifactParameters")
    def provisioning_artifact_parameters(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty", _IResolvable_da3f097b]]]:
        '''The configuration of the provisioning artifact (also known as a version).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactparameters
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty", _IResolvable_da3f097b]]], jsii.get(self, "provisioningArtifactParameters"))

    @provisioning_artifact_parameters.setter
    def provisioning_artifact_parameters(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProduct, "provisioning_artifact_parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioningArtifactParameters", value)

    @builtins.property
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-acceptlanguage
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceptLanguage"))

    @accept_language.setter
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProduct, "accept_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProduct, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="distributor")
    def distributor(self) -> typing.Optional[builtins.str]:
        '''The distributor of the product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-distributor
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distributor"))

    @distributor.setter
    def distributor(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProduct, "distributor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distributor", value)

    @builtins.property
    @jsii.member(jsii_name="replaceProvisioningArtifacts")
    def replace_provisioning_artifacts(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''This property is turned off by default.

        If turned off, you can update provisioning artifacts or product attributes (such as description, distributor, name, owner, and more) and the associated provisioning artifacts will retain the same unique identifier. Provisioning artifacts are matched within the CloudFormationProduct resource, and only those that have been updated will be changed. Provisioning artifacts are matched by a combinaton of provisioning artifact template URL and name.

        If turned on, provisioning artifacts will be given a new unique identifier when you update the product or provisioning artifacts.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-replaceprovisioningartifacts
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "replaceProvisioningArtifacts"))

    @replace_provisioning_artifacts.setter
    def replace_provisioning_artifacts(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProduct, "replace_provisioning_artifacts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replaceProvisioningArtifacts", value)

    @builtins.property
    @jsii.member(jsii_name="supportDescription")
    def support_description(self) -> typing.Optional[builtins.str]:
        '''The support information about the product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supportdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "supportDescription"))

    @support_description.setter
    def support_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProduct, "support_description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportDescription", value)

    @builtins.property
    @jsii.member(jsii_name="supportEmail")
    def support_email(self) -> typing.Optional[builtins.str]:
        '''The contact email for product support.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supportemail
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "supportEmail"))

    @support_email.setter
    def support_email(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProduct, "support_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportEmail", value)

    @builtins.property
    @jsii.member(jsii_name="supportUrl")
    def support_url(self) -> typing.Optional[builtins.str]:
        '''The contact URL for product support.

        ``^https?:\\/\\//`` / is the pattern used to validate SupportUrl.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supporturl
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "supportUrl"))

    @support_url.setter
    def support_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProduct, "support_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportUrl", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_servicecatalog.CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "info": "info",
            "description": "description",
            "disable_template_validation": "disableTemplateValidation",
            "name": "name",
        },
    )
    class ProvisioningArtifactPropertiesProperty:
        def __init__(
            self,
            *,
            info: typing.Any,
            description: typing.Optional[builtins.str] = None,
            disable_template_validation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about a provisioning artifact (also known as a version) for a product.

            :param info: Specify the template source with one of the following options, but not both. Keys accepted: [ ``LoadTemplateFromURL`` , ``ImportFromPhysicalId`` ] The URL of the AWS CloudFormation template in Amazon S3, AWS CodeCommit, or GitHub in JSON format. Specify the URL in JSON format as follows: ``"LoadTemplateFromURL": "https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/..."`` ``ImportFromPhysicalId`` : The physical id of the resource that contains the template. Currently only supports AWS CloudFormation stack arn. Specify the physical id in JSON format as follows: ``ImportFromPhysicalId: “arn:aws:cloudformation:[us-east-1]:[accountId]:stack/[StackName]/[resourceId]``
            :param description: The description of the provisioning artifact, including how it differs from the previous provisioning artifact.
            :param disable_template_validation: If set to true, AWS Service Catalog stops validating the specified provisioning artifact even if it is invalid.
            :param name: The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_servicecatalog as servicecatalog
                
                # info: Any
                
                provisioning_artifact_properties_property = servicecatalog.CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty(
                    info=info,
                
                    # the properties below are optional
                    description="description",
                    disable_template_validation=False,
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty.__init__)
                check_type(argname="argument info", value=info, expected_type=type_hints["info"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument disable_template_validation", value=disable_template_validation, expected_type=type_hints["disable_template_validation"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {
                "info": info,
            }
            if description is not None:
                self._values["description"] = description
            if disable_template_validation is not None:
                self._values["disable_template_validation"] = disable_template_validation
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def info(self) -> typing.Any:
            '''Specify the template source with one of the following options, but not both.

            Keys accepted: [ ``LoadTemplateFromURL`` , ``ImportFromPhysicalId`` ]

            The URL of the AWS CloudFormation template in Amazon S3, AWS CodeCommit, or GitHub in JSON format. Specify the URL in JSON format as follows:

            ``"LoadTemplateFromURL": "https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/..."``

            ``ImportFromPhysicalId`` : The physical id of the resource that contains the template. Currently only supports AWS CloudFormation stack arn. Specify the physical id in JSON format as follows: ``ImportFromPhysicalId: “arn:aws:cloudformation:[us-east-1]:[accountId]:stack/[StackName]/[resourceId]``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-info
            '''
            result = self._values.get("info")
            assert result is not None, "Required property 'info' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the provisioning artifact, including how it differs from the previous provisioning artifact.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def disable_template_validation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If set to true, AWS Service Catalog stops validating the specified provisioning artifact even if it is invalid.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-disabletemplatevalidation
            '''
            result = self._values.get("disable_template_validation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the provisioning artifact (for example, v1 v2beta).

            No spaces are allowed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisioningArtifactPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnCloudFormationProductProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "owner": "owner",
        "provisioning_artifact_parameters": "provisioningArtifactParameters",
        "accept_language": "acceptLanguage",
        "description": "description",
        "distributor": "distributor",
        "replace_provisioning_artifacts": "replaceProvisioningArtifacts",
        "support_description": "supportDescription",
        "support_email": "supportEmail",
        "support_url": "supportUrl",
        "tags": "tags",
    },
)
class CfnCloudFormationProductProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        owner: builtins.str,
        provisioning_artifact_parameters: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        distributor: typing.Optional[builtins.str] = None,
        replace_provisioning_artifacts: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        support_description: typing.Optional[builtins.str] = None,
        support_email: typing.Optional[builtins.str] = None,
        support_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCloudFormationProduct``.

        :param name: The name of the product.
        :param owner: The owner of the product.
        :param provisioning_artifact_parameters: The configuration of the provisioning artifact (also known as a version).
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param description: The description of the product.
        :param distributor: The distributor of the product.
        :param replace_provisioning_artifacts: This property is turned off by default. If turned off, you can update provisioning artifacts or product attributes (such as description, distributor, name, owner, and more) and the associated provisioning artifacts will retain the same unique identifier. Provisioning artifacts are matched within the CloudFormationProduct resource, and only those that have been updated will be changed. Provisioning artifacts are matched by a combinaton of provisioning artifact template URL and name. If turned on, provisioning artifacts will be given a new unique identifier when you update the product or provisioning artifacts.
        :param support_description: The support information about the product.
        :param support_email: The contact email for product support.
        :param support_url: The contact URL for product support. ``^https?:\\/\\//`` / is the pattern used to validate SupportUrl.
        :param tags: One or more tags.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            # info: Any
            
            cfn_cloud_formation_product_props = servicecatalog.CfnCloudFormationProductProps(
                name="name",
                owner="owner",
                provisioning_artifact_parameters=[servicecatalog.CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty(
                    info=info,
            
                    # the properties below are optional
                    description="description",
                    disable_template_validation=False,
                    name="name"
                )],
            
                # the properties below are optional
                accept_language="acceptLanguage",
                description="description",
                distributor="distributor",
                replace_provisioning_artifacts=False,
                support_description="supportDescription",
                support_email="supportEmail",
                support_url="supportUrl",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCloudFormationProductProps.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument provisioning_artifact_parameters", value=provisioning_artifact_parameters, expected_type=type_hints["provisioning_artifact_parameters"])
            check_type(argname="argument accept_language", value=accept_language, expected_type=type_hints["accept_language"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument distributor", value=distributor, expected_type=type_hints["distributor"])
            check_type(argname="argument replace_provisioning_artifacts", value=replace_provisioning_artifacts, expected_type=type_hints["replace_provisioning_artifacts"])
            check_type(argname="argument support_description", value=support_description, expected_type=type_hints["support_description"])
            check_type(argname="argument support_email", value=support_email, expected_type=type_hints["support_email"])
            check_type(argname="argument support_url", value=support_url, expected_type=type_hints["support_url"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "owner": owner,
            "provisioning_artifact_parameters": provisioning_artifact_parameters,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if description is not None:
            self._values["description"] = description
        if distributor is not None:
            self._values["distributor"] = distributor
        if replace_provisioning_artifacts is not None:
            self._values["replace_provisioning_artifacts"] = replace_provisioning_artifacts
        if support_description is not None:
            self._values["support_description"] = support_description
        if support_email is not None:
            self._values["support_email"] = support_email
        if support_url is not None:
            self._values["support_url"] = support_url
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def owner(self) -> builtins.str:
        '''The owner of the product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-owner
        '''
        result = self._values.get("owner")
        assert result is not None, "Required property 'owner' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def provisioning_artifact_parameters(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty, _IResolvable_da3f097b]]]:
        '''The configuration of the provisioning artifact (also known as a version).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactparameters
        '''
        result = self._values.get("provisioning_artifact_parameters")
        assert result is not None, "Required property 'provisioning_artifact_parameters' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnCloudFormationProduct.ProvisioningArtifactPropertiesProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-acceptlanguage
        '''
        result = self._values.get("accept_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distributor(self) -> typing.Optional[builtins.str]:
        '''The distributor of the product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-distributor
        '''
        result = self._values.get("distributor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replace_provisioning_artifacts(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''This property is turned off by default.

        If turned off, you can update provisioning artifacts or product attributes (such as description, distributor, name, owner, and more) and the associated provisioning artifacts will retain the same unique identifier. Provisioning artifacts are matched within the CloudFormationProduct resource, and only those that have been updated will be changed. Provisioning artifacts are matched by a combinaton of provisioning artifact template URL and name.

        If turned on, provisioning artifacts will be given a new unique identifier when you update the product or provisioning artifacts.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-replaceprovisioningartifacts
        '''
        result = self._values.get("replace_provisioning_artifacts")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def support_description(self) -> typing.Optional[builtins.str]:
        '''The support information about the product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supportdescription
        '''
        result = self._values.get("support_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def support_email(self) -> typing.Optional[builtins.str]:
        '''The contact email for product support.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supportemail
        '''
        result = self._values.get("support_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def support_url(self) -> typing.Optional[builtins.str]:
        '''The contact URL for product support.

        ``^https?:\\/\\//`` / is the pattern used to validate SupportUrl.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supporturl
        '''
        result = self._values.get("support_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more tags.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudFormationProductProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnCloudFormationProvisionedProduct(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnCloudFormationProvisionedProduct",
):
    '''A CloudFormation ``AWS::ServiceCatalog::CloudFormationProvisionedProduct``.

    Provisions the specified product.

    A provisioned product is a resourced instance of a product. For example, provisioning a product based on a AWS CloudFormation template launches a AWS CloudFormation stack and its underlying resources. You can check the status of this request using `DescribeRecord <https://docs.aws.amazon.com/servicecatalog/latest/dg/API_DescribeRecord.html>`_ .

    If the request contains a tag key with an empty list of values, there is a tag conflict for that key. Do not include conflicted keys as tags, or this causes the error "Parameter validation failed: Missing required parameter in Tags[ *N* ]: *Value* ".

    :cloudformationResource: AWS::ServiceCatalog::CloudFormationProvisionedProduct
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        cfn_cloud_formation_provisioned_product = servicecatalog.CfnCloudFormationProvisionedProduct(self, "MyCfnCloudFormationProvisionedProduct",
            accept_language="acceptLanguage",
            notification_arns=["notificationArns"],
            path_id="pathId",
            path_name="pathName",
            product_id="productId",
            product_name="productName",
            provisioned_product_name="provisionedProductName",
            provisioning_artifact_id="provisioningArtifactId",
            provisioning_artifact_name="provisioningArtifactName",
            provisioning_parameters=[servicecatalog.CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty(
                key="key",
                value="value"
            )],
            provisioning_preferences=servicecatalog.CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty(
                stack_set_accounts=["stackSetAccounts"],
                stack_set_failure_tolerance_count=123,
                stack_set_failure_tolerance_percentage=123,
                stack_set_max_concurrency_count=123,
                stack_set_max_concurrency_percentage=123,
                stack_set_operation_type="stackSetOperationType",
                stack_set_regions=["stackSetRegions"]
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        accept_language: typing.Optional[builtins.str] = None,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        path_id: typing.Optional[builtins.str] = None,
        path_name: typing.Optional[builtins.str] = None,
        product_id: typing.Optional[builtins.str] = None,
        product_name: typing.Optional[builtins.str] = None,
        provisioned_product_name: typing.Optional[builtins.str] = None,
        provisioning_artifact_id: typing.Optional[builtins.str] = None,
        provisioning_artifact_name: typing.Optional[builtins.str] = None,
        provisioning_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        provisioning_preferences: typing.Optional[typing.Union[typing.Union["CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::CloudFormationProvisionedProduct``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param notification_arns: Passed to AWS CloudFormation . The SNS topic ARNs to which to publish stack-related events.
        :param path_id: The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use `ListLaunchPaths <https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListLaunchPaths.html>`_ . .. epigraph:: You must provide the name or ID, but not both.
        :param path_name: The name of the path. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use `ListLaunchPaths <https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListLaunchPaths.html>`_ . .. epigraph:: You must provide the name or ID, but not both.
        :param product_id: The product identifier. .. epigraph:: You must specify either the ID or the name of the product, but not both.
        :param product_name: A user-friendly name for the provisioned product. This value must be unique for the AWS account and cannot be updated after the product is provisioned. Each time a stack is created or updated, if ``ProductName`` is provided it will successfully resolve to ``ProductId`` as long as only one product exists in the account or Region with that ``ProductName`` . .. epigraph:: You must specify either the name or the ID of the product, but not both.
        :param provisioned_product_name: A user-friendly name for the provisioned product. This value must be unique for the AWS account and cannot be updated after the product is provisioned.
        :param provisioning_artifact_id: The identifier of the provisioning artifact (also known as a version). .. epigraph:: You must specify either the ID or the name of the provisioning artifact, but not both.
        :param provisioning_artifact_name: The name of the provisioning artifact (also known as a version) for the product. This name must be unique for the product. .. epigraph:: You must specify either the name or the ID of the provisioning artifact, but not both. You must also specify either the name or the ID of the product, but not both.
        :param provisioning_parameters: Parameters specified by the administrator that are required for provisioning the product.
        :param provisioning_preferences: StackSet preferences that are required for provisioning the product or updating a provisioned product.
        :param tags: One or more tags. .. epigraph:: Requires the provisioned product to have an `ResourceUpdateConstraint <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html>`_ resource with ``TagUpdatesOnProvisionedProduct`` set to ``ALLOWED`` to allow tag updates. If ``RESOURCE_UPDATE`` constraint is not present, tags updates are ignored.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCloudFormationProvisionedProduct.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCloudFormationProvisionedProductProps(
            accept_language=accept_language,
            notification_arns=notification_arns,
            path_id=path_id,
            path_name=path_name,
            product_id=product_id,
            product_name=product_name,
            provisioned_product_name=provisioned_product_name,
            provisioning_artifact_id=provisioning_artifact_id,
            provisioning_artifact_name=provisioning_artifact_name,
            provisioning_parameters=provisioning_parameters,
            provisioning_preferences=provisioning_preferences,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCloudFormationProvisionedProduct.inspect)
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
            type_hints = typing.get_type_hints(CfnCloudFormationProvisionedProduct._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCloudformationStackArn")
    def attr_cloudformation_stack_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the CloudFormation stack, such as ``arn:aws:cloudformation:eu-west-1:123456789012:stack/SC-499278721343-pp-hfyszaotincww/8f3df460-346a-11e8-9444-503abe701c29`` .

        :cloudformationAttribute: CloudformationStackArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCloudformationStackArn"))

    @builtins.property
    @jsii.member(jsii_name="attrProvisionedProductId")
    def attr_provisioned_product_id(self) -> builtins.str:
        '''The ID of the provisioned product.

        :cloudformationAttribute: ProvisionedProductId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProvisionedProductId"))

    @builtins.property
    @jsii.member(jsii_name="attrRecordId")
    def attr_record_id(self) -> builtins.str:
        '''The ID of the record, such as ``rec-rjeatvy434trk`` .

        :cloudformationAttribute: RecordId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRecordId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''One or more tags.

        .. epigraph::

           Requires the provisioned product to have an `ResourceUpdateConstraint <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html>`_ resource with ``TagUpdatesOnProvisionedProduct`` set to ``ALLOWED`` to allow tag updates. If ``RESOURCE_UPDATE`` constraint is not present, tags updates are ignored.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-acceptlanguage
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceptLanguage"))

    @accept_language.setter
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProvisionedProduct, "accept_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="notificationArns")
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Passed to AWS CloudFormation .

        The SNS topic ARNs to which to publish stack-related events.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-notificationarns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationArns"))

    @notification_arns.setter
    def notification_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProvisionedProduct, "notification_arns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationArns", value)

    @builtins.property
    @jsii.member(jsii_name="pathId")
    def path_id(self) -> typing.Optional[builtins.str]:
        '''The path identifier of the product.

        This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use `ListLaunchPaths <https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListLaunchPaths.html>`_ .
        .. epigraph::

           You must provide the name or ID, but not both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-pathid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathId"))

    @path_id.setter
    def path_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProvisionedProduct, "path_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathId", value)

    @builtins.property
    @jsii.member(jsii_name="pathName")
    def path_name(self) -> typing.Optional[builtins.str]:
        '''The name of the path.

        This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use `ListLaunchPaths <https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListLaunchPaths.html>`_ .
        .. epigraph::

           You must provide the name or ID, but not both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-pathname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathName"))

    @path_name.setter
    def path_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProvisionedProduct, "path_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathName", value)

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> typing.Optional[builtins.str]:
        '''The product identifier.

        .. epigraph::

           You must specify either the ID or the name of the product, but not both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-productid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productId"))

    @product_id.setter
    def product_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProvisionedProduct, "product_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productId", value)

    @builtins.property
    @jsii.member(jsii_name="productName")
    def product_name(self) -> typing.Optional[builtins.str]:
        '''A user-friendly name for the provisioned product.

        This value must be unique for the AWS account and cannot be updated after the product is provisioned.

        Each time a stack is created or updated, if ``ProductName`` is provided it will successfully resolve to ``ProductId`` as long as only one product exists in the account or Region with that ``ProductName`` .
        .. epigraph::

           You must specify either the name or the ID of the product, but not both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-productname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productName"))

    @product_name.setter
    def product_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProvisionedProduct, "product_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productName", value)

    @builtins.property
    @jsii.member(jsii_name="provisionedProductName")
    def provisioned_product_name(self) -> typing.Optional[builtins.str]:
        '''A user-friendly name for the provisioned product.

        This value must be unique for the AWS account and cannot be updated after the product is provisioned.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisionedproductname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "provisionedProductName"))

    @provisioned_product_name.setter
    def provisioned_product_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProvisionedProduct, "provisioned_product_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionedProductName", value)

    @builtins.property
    @jsii.member(jsii_name="provisioningArtifactId")
    def provisioning_artifact_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the provisioning artifact (also known as a version).

        .. epigraph::

           You must specify either the ID or the name of the provisioning artifact, but not both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningartifactid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "provisioningArtifactId"))

    @provisioning_artifact_id.setter
    def provisioning_artifact_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProvisionedProduct, "provisioning_artifact_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioningArtifactId", value)

    @builtins.property
    @jsii.member(jsii_name="provisioningArtifactName")
    def provisioning_artifact_name(self) -> typing.Optional[builtins.str]:
        '''The name of the provisioning artifact (also known as a version) for the product.

        This name must be unique for the product.
        .. epigraph::

           You must specify either the name or the ID of the provisioning artifact, but not both. You must also specify either the name or the ID of the product, but not both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningartifactname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "provisioningArtifactName"))

    @provisioning_artifact_name.setter
    def provisioning_artifact_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProvisionedProduct, "provisioning_artifact_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioningArtifactName", value)

    @builtins.property
    @jsii.member(jsii_name="provisioningParameters")
    def provisioning_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty", _IResolvable_da3f097b]]]]:
        '''Parameters specified by the administrator that are required for provisioning the product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameters
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty", _IResolvable_da3f097b]]]], jsii.get(self, "provisioningParameters"))

    @provisioning_parameters.setter
    def provisioning_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProvisionedProduct, "provisioning_parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioningParameters", value)

    @builtins.property
    @jsii.member(jsii_name="provisioningPreferences")
    def provisioning_preferences(
        self,
    ) -> typing.Optional[typing.Union["CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty", _IResolvable_da3f097b]]:
        '''StackSet preferences that are required for provisioning the product or updating a provisioned product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences
        '''
        return typing.cast(typing.Optional[typing.Union["CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty", _IResolvable_da3f097b]], jsii.get(self, "provisioningPreferences"))

    @provisioning_preferences.setter
    def provisioning_preferences(
        self,
        value: typing.Optional[typing.Union["CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCloudFormationProvisionedProduct, "provisioning_preferences").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioningPreferences", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_servicecatalog.CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ProvisioningParameterProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''Information about a parameter used to provision a product.

            :param key: The parameter key.
            :param value: The parameter value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_servicecatalog as servicecatalog
                
                provisioning_parameter_property = servicecatalog.CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty.__init__)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The parameter key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningparameter.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameter-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The parameter value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningparameter.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisioningParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_servicecatalog.CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "stack_set_accounts": "stackSetAccounts",
            "stack_set_failure_tolerance_count": "stackSetFailureToleranceCount",
            "stack_set_failure_tolerance_percentage": "stackSetFailureTolerancePercentage",
            "stack_set_max_concurrency_count": "stackSetMaxConcurrencyCount",
            "stack_set_max_concurrency_percentage": "stackSetMaxConcurrencyPercentage",
            "stack_set_operation_type": "stackSetOperationType",
            "stack_set_regions": "stackSetRegions",
        },
    )
    class ProvisioningPreferencesProperty:
        def __init__(
            self,
            *,
            stack_set_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
            stack_set_failure_tolerance_count: typing.Optional[jsii.Number] = None,
            stack_set_failure_tolerance_percentage: typing.Optional[jsii.Number] = None,
            stack_set_max_concurrency_count: typing.Optional[jsii.Number] = None,
            stack_set_max_concurrency_percentage: typing.Optional[jsii.Number] = None,
            stack_set_operation_type: typing.Optional[builtins.str] = None,
            stack_set_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The user-defined preferences that will be applied when updating a provisioned product.

            Not all preferences are applicable to all provisioned product type

            One or more AWS accounts that will have access to the provisioned product.

            Applicable only to a ``CFN_STACKSET`` provisioned product type.

            The AWS accounts specified should be within the list of accounts in the ``STACKSET`` constraint. To get the list of accounts in the ``STACKSET`` constraint, use the ``DescribeProvisioningParameters`` operation.

            If no values are specified, the default value is all accounts from the ``STACKSET`` constraint.

            :param stack_set_accounts: One or more AWS accounts where the provisioned product will be available. Applicable only to a ``CFN_STACKSET`` provisioned product type. The specified accounts should be within the list of accounts from the ``STACKSET`` constraint. To get the list of accounts in the ``STACKSET`` constraint, use the ``DescribeProvisioningParameters`` operation. If no values are specified, the default value is all acounts from the ``STACKSET`` constraint.
            :param stack_set_failure_tolerance_count: The number of accounts, per Region, for which this operation can fail before AWS Service Catalog stops the operation in that Region. If the operation is stopped in a Region, AWS Service Catalog doesn't attempt the operation in any subsequent Regions. Applicable only to a ``CFN_STACKSET`` provisioned product type. Conditional: You must specify either ``StackSetFailureToleranceCount`` or ``StackSetFailureTolerancePercentage`` , but not both. The default value is ``0`` if no value is specified.
            :param stack_set_failure_tolerance_percentage: The percentage of accounts, per Region, for which this stack operation can fail before AWS Service Catalog stops the operation in that Region. If the operation is stopped in a Region, AWS Service Catalog doesn't attempt the operation in any subsequent Regions. When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. Applicable only to a ``CFN_STACKSET`` provisioned product type. Conditional: You must specify either ``StackSetFailureToleranceCount`` or ``StackSetFailureTolerancePercentage`` , but not both.
            :param stack_set_max_concurrency_count: The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of ``StackSetFailureToleranceCount`` . ``StackSetMaxConcurrentCount`` is at most one more than the ``StackSetFailureToleranceCount`` . Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling. Applicable only to a ``CFN_STACKSET`` provisioned product type. Conditional: You must specify either ``StackSetMaxConcurrentCount`` or ``StackSetMaxConcurrentPercentage`` , but not both.
            :param stack_set_max_concurrency_percentage: The maximum percentage of accounts in which to perform this operation at one time. When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, AWS Service Catalog sets the number as ``1`` instead. Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling. Applicable only to a ``CFN_STACKSET`` provisioned product type. Conditional: You must specify either ``StackSetMaxConcurrentCount`` or ``StackSetMaxConcurrentPercentage`` , but not both.
            :param stack_set_operation_type: Determines what action AWS Service Catalog performs to a stack set or a stack instance represented by the provisioned product. The default value is ``UPDATE`` if nothing is specified. Applicable only to a ``CFN_STACKSET`` provisioned product type. - **CREATE** - Creates a new stack instance in the stack set represented by the provisioned product. In this case, only new stack instances are created based on accounts and Regions; if new ProductId or ProvisioningArtifactID are passed, they will be ignored. - **UPDATE** - Updates the stack set represented by the provisioned product and also its stack instances. - **DELETE** - Deletes a stack instance in the stack set represented by the provisioned product.
            :param stack_set_regions: One or more AWS Regions where the provisioned product will be available. Applicable only to a ``CFN_STACKSET`` provisioned product type. The specified Regions should be within the list of Regions from the ``STACKSET`` constraint. To get the list of Regions in the ``STACKSET`` constraint, use the ``DescribeProvisioningParameters`` operation. If no values are specified, the default value is all Regions from the ``STACKSET`` constraint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_servicecatalog as servicecatalog
                
                provisioning_preferences_property = servicecatalog.CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty(
                    stack_set_accounts=["stackSetAccounts"],
                    stack_set_failure_tolerance_count=123,
                    stack_set_failure_tolerance_percentage=123,
                    stack_set_max_concurrency_count=123,
                    stack_set_max_concurrency_percentage=123,
                    stack_set_operation_type="stackSetOperationType",
                    stack_set_regions=["stackSetRegions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty.__init__)
                check_type(argname="argument stack_set_accounts", value=stack_set_accounts, expected_type=type_hints["stack_set_accounts"])
                check_type(argname="argument stack_set_failure_tolerance_count", value=stack_set_failure_tolerance_count, expected_type=type_hints["stack_set_failure_tolerance_count"])
                check_type(argname="argument stack_set_failure_tolerance_percentage", value=stack_set_failure_tolerance_percentage, expected_type=type_hints["stack_set_failure_tolerance_percentage"])
                check_type(argname="argument stack_set_max_concurrency_count", value=stack_set_max_concurrency_count, expected_type=type_hints["stack_set_max_concurrency_count"])
                check_type(argname="argument stack_set_max_concurrency_percentage", value=stack_set_max_concurrency_percentage, expected_type=type_hints["stack_set_max_concurrency_percentage"])
                check_type(argname="argument stack_set_operation_type", value=stack_set_operation_type, expected_type=type_hints["stack_set_operation_type"])
                check_type(argname="argument stack_set_regions", value=stack_set_regions, expected_type=type_hints["stack_set_regions"])
            self._values: typing.Dict[str, typing.Any] = {}
            if stack_set_accounts is not None:
                self._values["stack_set_accounts"] = stack_set_accounts
            if stack_set_failure_tolerance_count is not None:
                self._values["stack_set_failure_tolerance_count"] = stack_set_failure_tolerance_count
            if stack_set_failure_tolerance_percentage is not None:
                self._values["stack_set_failure_tolerance_percentage"] = stack_set_failure_tolerance_percentage
            if stack_set_max_concurrency_count is not None:
                self._values["stack_set_max_concurrency_count"] = stack_set_max_concurrency_count
            if stack_set_max_concurrency_percentage is not None:
                self._values["stack_set_max_concurrency_percentage"] = stack_set_max_concurrency_percentage
            if stack_set_operation_type is not None:
                self._values["stack_set_operation_type"] = stack_set_operation_type
            if stack_set_regions is not None:
                self._values["stack_set_regions"] = stack_set_regions

        @builtins.property
        def stack_set_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
            '''One or more AWS accounts where the provisioned product will be available.

            Applicable only to a ``CFN_STACKSET`` provisioned product type.

            The specified accounts should be within the list of accounts from the ``STACKSET`` constraint. To get the list of accounts in the ``STACKSET`` constraint, use the ``DescribeProvisioningParameters`` operation.

            If no values are specified, the default value is all acounts from the ``STACKSET`` constraint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetaccounts
            '''
            result = self._values.get("stack_set_accounts")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def stack_set_failure_tolerance_count(self) -> typing.Optional[jsii.Number]:
            '''The number of accounts, per Region, for which this operation can fail before AWS Service Catalog stops the operation in that Region.

            If the operation is stopped in a Region, AWS Service Catalog doesn't attempt the operation in any subsequent Regions.

            Applicable only to a ``CFN_STACKSET`` provisioned product type.

            Conditional: You must specify either ``StackSetFailureToleranceCount`` or ``StackSetFailureTolerancePercentage`` , but not both.

            The default value is ``0`` if no value is specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetfailuretolerancecount
            '''
            result = self._values.get("stack_set_failure_tolerance_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stack_set_failure_tolerance_percentage(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The percentage of accounts, per Region, for which this stack operation can fail before AWS Service Catalog stops the operation in that Region.

            If the operation is stopped in a Region, AWS Service Catalog doesn't attempt the operation in any subsequent Regions.

            When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number.

            Applicable only to a ``CFN_STACKSET`` provisioned product type.

            Conditional: You must specify either ``StackSetFailureToleranceCount`` or ``StackSetFailureTolerancePercentage`` , but not both.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetfailuretolerancepercentage
            '''
            result = self._values.get("stack_set_failure_tolerance_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stack_set_max_concurrency_count(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of accounts in which to perform this operation at one time.

            This is dependent on the value of ``StackSetFailureToleranceCount`` . ``StackSetMaxConcurrentCount`` is at most one more than the ``StackSetFailureToleranceCount`` .

            Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.

            Applicable only to a ``CFN_STACKSET`` provisioned product type.

            Conditional: You must specify either ``StackSetMaxConcurrentCount`` or ``StackSetMaxConcurrentPercentage`` , but not both.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetmaxconcurrencycount
            '''
            result = self._values.get("stack_set_max_concurrency_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stack_set_max_concurrency_percentage(self) -> typing.Optional[jsii.Number]:
            '''The maximum percentage of accounts in which to perform this operation at one time.

            When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, AWS Service Catalog sets the number as ``1`` instead.

            Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.

            Applicable only to a ``CFN_STACKSET`` provisioned product type.

            Conditional: You must specify either ``StackSetMaxConcurrentCount`` or ``StackSetMaxConcurrentPercentage`` , but not both.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetmaxconcurrencypercentage
            '''
            result = self._values.get("stack_set_max_concurrency_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stack_set_operation_type(self) -> typing.Optional[builtins.str]:
            '''Determines what action AWS Service Catalog performs to a stack set or a stack instance represented by the provisioned product.

            The default value is ``UPDATE`` if nothing is specified.

            Applicable only to a ``CFN_STACKSET`` provisioned product type.

            - **CREATE** - Creates a new stack instance in the stack set represented by the provisioned product. In this case, only new stack instances are created based on accounts and Regions; if new ProductId or ProvisioningArtifactID are passed, they will be ignored.
            - **UPDATE** - Updates the stack set represented by the provisioned product and also its stack instances.
            - **DELETE** - Deletes a stack instance in the stack set represented by the provisioned product.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetoperationtype
            '''
            result = self._values.get("stack_set_operation_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stack_set_regions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''One or more AWS Regions where the provisioned product will be available.

            Applicable only to a ``CFN_STACKSET`` provisioned product type.

            The specified Regions should be within the list of Regions from the ``STACKSET`` constraint. To get the list of Regions in the ``STACKSET`` constraint, use the ``DescribeProvisioningParameters`` operation.

            If no values are specified, the default value is all Regions from the ``STACKSET`` constraint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetregions
            '''
            result = self._values.get("stack_set_regions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisioningPreferencesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnCloudFormationProvisionedProductProps",
    jsii_struct_bases=[],
    name_mapping={
        "accept_language": "acceptLanguage",
        "notification_arns": "notificationArns",
        "path_id": "pathId",
        "path_name": "pathName",
        "product_id": "productId",
        "product_name": "productName",
        "provisioned_product_name": "provisionedProductName",
        "provisioning_artifact_id": "provisioningArtifactId",
        "provisioning_artifact_name": "provisioningArtifactName",
        "provisioning_parameters": "provisioningParameters",
        "provisioning_preferences": "provisioningPreferences",
        "tags": "tags",
    },
)
class CfnCloudFormationProvisionedProductProps:
    def __init__(
        self,
        *,
        accept_language: typing.Optional[builtins.str] = None,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        path_id: typing.Optional[builtins.str] = None,
        path_name: typing.Optional[builtins.str] = None,
        product_id: typing.Optional[builtins.str] = None,
        product_name: typing.Optional[builtins.str] = None,
        provisioned_product_name: typing.Optional[builtins.str] = None,
        provisioning_artifact_id: typing.Optional[builtins.str] = None,
        provisioning_artifact_name: typing.Optional[builtins.str] = None,
        provisioning_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        provisioning_preferences: typing.Optional[typing.Union[typing.Union[CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCloudFormationProvisionedProduct``.

        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param notification_arns: Passed to AWS CloudFormation . The SNS topic ARNs to which to publish stack-related events.
        :param path_id: The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use `ListLaunchPaths <https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListLaunchPaths.html>`_ . .. epigraph:: You must provide the name or ID, but not both.
        :param path_name: The name of the path. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use `ListLaunchPaths <https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListLaunchPaths.html>`_ . .. epigraph:: You must provide the name or ID, but not both.
        :param product_id: The product identifier. .. epigraph:: You must specify either the ID or the name of the product, but not both.
        :param product_name: A user-friendly name for the provisioned product. This value must be unique for the AWS account and cannot be updated after the product is provisioned. Each time a stack is created or updated, if ``ProductName`` is provided it will successfully resolve to ``ProductId`` as long as only one product exists in the account or Region with that ``ProductName`` . .. epigraph:: You must specify either the name or the ID of the product, but not both.
        :param provisioned_product_name: A user-friendly name for the provisioned product. This value must be unique for the AWS account and cannot be updated after the product is provisioned.
        :param provisioning_artifact_id: The identifier of the provisioning artifact (also known as a version). .. epigraph:: You must specify either the ID or the name of the provisioning artifact, but not both.
        :param provisioning_artifact_name: The name of the provisioning artifact (also known as a version) for the product. This name must be unique for the product. .. epigraph:: You must specify either the name or the ID of the provisioning artifact, but not both. You must also specify either the name or the ID of the product, but not both.
        :param provisioning_parameters: Parameters specified by the administrator that are required for provisioning the product.
        :param provisioning_preferences: StackSet preferences that are required for provisioning the product or updating a provisioned product.
        :param tags: One or more tags. .. epigraph:: Requires the provisioned product to have an `ResourceUpdateConstraint <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html>`_ resource with ``TagUpdatesOnProvisionedProduct`` set to ``ALLOWED`` to allow tag updates. If ``RESOURCE_UPDATE`` constraint is not present, tags updates are ignored.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cfn_cloud_formation_provisioned_product_props = servicecatalog.CfnCloudFormationProvisionedProductProps(
                accept_language="acceptLanguage",
                notification_arns=["notificationArns"],
                path_id="pathId",
                path_name="pathName",
                product_id="productId",
                product_name="productName",
                provisioned_product_name="provisionedProductName",
                provisioning_artifact_id="provisioningArtifactId",
                provisioning_artifact_name="provisioningArtifactName",
                provisioning_parameters=[servicecatalog.CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty(
                    key="key",
                    value="value"
                )],
                provisioning_preferences=servicecatalog.CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty(
                    stack_set_accounts=["stackSetAccounts"],
                    stack_set_failure_tolerance_count=123,
                    stack_set_failure_tolerance_percentage=123,
                    stack_set_max_concurrency_count=123,
                    stack_set_max_concurrency_percentage=123,
                    stack_set_operation_type="stackSetOperationType",
                    stack_set_regions=["stackSetRegions"]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCloudFormationProvisionedProductProps.__init__)
            check_type(argname="argument accept_language", value=accept_language, expected_type=type_hints["accept_language"])
            check_type(argname="argument notification_arns", value=notification_arns, expected_type=type_hints["notification_arns"])
            check_type(argname="argument path_id", value=path_id, expected_type=type_hints["path_id"])
            check_type(argname="argument path_name", value=path_name, expected_type=type_hints["path_name"])
            check_type(argname="argument product_id", value=product_id, expected_type=type_hints["product_id"])
            check_type(argname="argument product_name", value=product_name, expected_type=type_hints["product_name"])
            check_type(argname="argument provisioned_product_name", value=provisioned_product_name, expected_type=type_hints["provisioned_product_name"])
            check_type(argname="argument provisioning_artifact_id", value=provisioning_artifact_id, expected_type=type_hints["provisioning_artifact_id"])
            check_type(argname="argument provisioning_artifact_name", value=provisioning_artifact_name, expected_type=type_hints["provisioning_artifact_name"])
            check_type(argname="argument provisioning_parameters", value=provisioning_parameters, expected_type=type_hints["provisioning_parameters"])
            check_type(argname="argument provisioning_preferences", value=provisioning_preferences, expected_type=type_hints["provisioning_preferences"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {}
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if notification_arns is not None:
            self._values["notification_arns"] = notification_arns
        if path_id is not None:
            self._values["path_id"] = path_id
        if path_name is not None:
            self._values["path_name"] = path_name
        if product_id is not None:
            self._values["product_id"] = product_id
        if product_name is not None:
            self._values["product_name"] = product_name
        if provisioned_product_name is not None:
            self._values["provisioned_product_name"] = provisioned_product_name
        if provisioning_artifact_id is not None:
            self._values["provisioning_artifact_id"] = provisioning_artifact_id
        if provisioning_artifact_name is not None:
            self._values["provisioning_artifact_name"] = provisioning_artifact_name
        if provisioning_parameters is not None:
            self._values["provisioning_parameters"] = provisioning_parameters
        if provisioning_preferences is not None:
            self._values["provisioning_preferences"] = provisioning_preferences
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-acceptlanguage
        '''
        result = self._values.get("accept_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Passed to AWS CloudFormation .

        The SNS topic ARNs to which to publish stack-related events.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-notificationarns
        '''
        result = self._values.get("notification_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def path_id(self) -> typing.Optional[builtins.str]:
        '''The path identifier of the product.

        This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use `ListLaunchPaths <https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListLaunchPaths.html>`_ .
        .. epigraph::

           You must provide the name or ID, but not both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-pathid
        '''
        result = self._values.get("path_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_name(self) -> typing.Optional[builtins.str]:
        '''The name of the path.

        This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use `ListLaunchPaths <https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ListLaunchPaths.html>`_ .
        .. epigraph::

           You must provide the name or ID, but not both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-pathname
        '''
        result = self._values.get("path_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def product_id(self) -> typing.Optional[builtins.str]:
        '''The product identifier.

        .. epigraph::

           You must specify either the ID or the name of the product, but not both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-productid
        '''
        result = self._values.get("product_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def product_name(self) -> typing.Optional[builtins.str]:
        '''A user-friendly name for the provisioned product.

        This value must be unique for the AWS account and cannot be updated after the product is provisioned.

        Each time a stack is created or updated, if ``ProductName`` is provided it will successfully resolve to ``ProductId`` as long as only one product exists in the account or Region with that ``ProductName`` .
        .. epigraph::

           You must specify either the name or the ID of the product, but not both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-productname
        '''
        result = self._values.get("product_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provisioned_product_name(self) -> typing.Optional[builtins.str]:
        '''A user-friendly name for the provisioned product.

        This value must be unique for the AWS account and cannot be updated after the product is provisioned.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisionedproductname
        '''
        result = self._values.get("provisioned_product_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provisioning_artifact_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the provisioning artifact (also known as a version).

        .. epigraph::

           You must specify either the ID or the name of the provisioning artifact, but not both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningartifactid
        '''
        result = self._values.get("provisioning_artifact_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provisioning_artifact_name(self) -> typing.Optional[builtins.str]:
        '''The name of the provisioning artifact (also known as a version) for the product.

        This name must be unique for the product.
        .. epigraph::

           You must specify either the name or the ID of the provisioning artifact, but not both. You must also specify either the name or the ID of the product, but not both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningartifactname
        '''
        result = self._values.get("provisioning_artifact_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provisioning_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty, _IResolvable_da3f097b]]]]:
        '''Parameters specified by the administrator that are required for provisioning the product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameters
        '''
        result = self._values.get("provisioning_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnCloudFormationProvisionedProduct.ProvisioningParameterProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def provisioning_preferences(
        self,
    ) -> typing.Optional[typing.Union[CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty, _IResolvable_da3f097b]]:
        '''StackSet preferences that are required for provisioning the product or updating a provisioned product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences
        '''
        result = self._values.get("provisioning_preferences")
        return typing.cast(typing.Optional[typing.Union[CfnCloudFormationProvisionedProduct.ProvisioningPreferencesProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more tags.

        .. epigraph::

           Requires the provisioned product to have an `ResourceUpdateConstraint <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html>`_ resource with ``TagUpdatesOnProvisionedProduct`` set to ``ALLOWED`` to allow tag updates. If ``RESOURCE_UPDATE`` constraint is not present, tags updates are ignored.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudFormationProvisionedProductProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLaunchNotificationConstraint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnLaunchNotificationConstraint",
):
    '''A CloudFormation ``AWS::ServiceCatalog::LaunchNotificationConstraint``.

    Specifies a notification constraint.

    :cloudformationResource: AWS::ServiceCatalog::LaunchNotificationConstraint
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        cfn_launch_notification_constraint = servicecatalog.CfnLaunchNotificationConstraint(self, "MyCfnLaunchNotificationConstraint",
            notification_arns=["notificationArns"],
            portfolio_id="portfolioId",
            product_id="productId",
        
            # the properties below are optional
            accept_language="acceptLanguage",
            description="description"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        notification_arns: typing.Sequence[builtins.str],
        portfolio_id: builtins.str,
        product_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::LaunchNotificationConstraint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param notification_arns: The notification ARNs.
        :param portfolio_id: The portfolio identifier.
        :param product_id: The product identifier.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param description: The description of the constraint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLaunchNotificationConstraint.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLaunchNotificationConstraintProps(
            notification_arns=notification_arns,
            portfolio_id=portfolio_id,
            product_id=product_id,
            accept_language=accept_language,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLaunchNotificationConstraint.inspect)
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
            type_hints = typing.get_type_hints(CfnLaunchNotificationConstraint._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="notificationArns")
    def notification_arns(self) -> typing.List[builtins.str]:
        '''The notification ARNs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-notificationarns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notificationArns"))

    @notification_arns.setter
    def notification_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchNotificationConstraint, "notification_arns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationArns", value)

    @builtins.property
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-portfolioid
        '''
        return typing.cast(builtins.str, jsii.get(self, "portfolioId"))

    @portfolio_id.setter
    def portfolio_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchNotificationConstraint, "portfolio_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portfolioId", value)

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        '''The product identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-productid
        '''
        return typing.cast(builtins.str, jsii.get(self, "productId"))

    @product_id.setter
    def product_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchNotificationConstraint, "product_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productId", value)

    @builtins.property
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-acceptlanguage
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceptLanguage"))

    @accept_language.setter
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchNotificationConstraint, "accept_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchNotificationConstraint, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnLaunchNotificationConstraintProps",
    jsii_struct_bases=[],
    name_mapping={
        "notification_arns": "notificationArns",
        "portfolio_id": "portfolioId",
        "product_id": "productId",
        "accept_language": "acceptLanguage",
        "description": "description",
    },
)
class CfnLaunchNotificationConstraintProps:
    def __init__(
        self,
        *,
        notification_arns: typing.Sequence[builtins.str],
        portfolio_id: builtins.str,
        product_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnLaunchNotificationConstraint``.

        :param notification_arns: The notification ARNs.
        :param portfolio_id: The portfolio identifier.
        :param product_id: The product identifier.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param description: The description of the constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cfn_launch_notification_constraint_props = servicecatalog.CfnLaunchNotificationConstraintProps(
                notification_arns=["notificationArns"],
                portfolio_id="portfolioId",
                product_id="productId",
            
                # the properties below are optional
                accept_language="acceptLanguage",
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLaunchNotificationConstraintProps.__init__)
            check_type(argname="argument notification_arns", value=notification_arns, expected_type=type_hints["notification_arns"])
            check_type(argname="argument portfolio_id", value=portfolio_id, expected_type=type_hints["portfolio_id"])
            check_type(argname="argument product_id", value=product_id, expected_type=type_hints["product_id"])
            check_type(argname="argument accept_language", value=accept_language, expected_type=type_hints["accept_language"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "notification_arns": notification_arns,
            "portfolio_id": portfolio_id,
            "product_id": product_id,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def notification_arns(self) -> typing.List[builtins.str]:
        '''The notification ARNs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-notificationarns
        '''
        result = self._values.get("notification_arns")
        assert result is not None, "Required property 'notification_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-portfolioid
        '''
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_id(self) -> builtins.str:
        '''The product identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-productid
        '''
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-acceptlanguage
        '''
        result = self._values.get("accept_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLaunchNotificationConstraintProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLaunchRoleConstraint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnLaunchRoleConstraint",
):
    '''A CloudFormation ``AWS::ServiceCatalog::LaunchRoleConstraint``.

    Specifies a launch constraint.

    :cloudformationResource: AWS::ServiceCatalog::LaunchRoleConstraint
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        cfn_launch_role_constraint = servicecatalog.CfnLaunchRoleConstraint(self, "MyCfnLaunchRoleConstraint",
            portfolio_id="portfolioId",
            product_id="productId",
        
            # the properties below are optional
            accept_language="acceptLanguage",
            description="description",
            local_role_name="localRoleName",
            role_arn="roleArn"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        local_role_name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::LaunchRoleConstraint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param portfolio_id: The portfolio identifier.
        :param product_id: The product identifier.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param description: The description of the constraint.
        :param local_role_name: You are required to specify either the ``RoleArn`` or the ``LocalRoleName`` but can't use both. If you specify the ``LocalRoleName`` property, when an account uses the launch constraint, the IAM role with that name in the account will be used. This allows launch-role constraints to be account-agnostic so the administrator can create fewer resources per shared account. The given role name must exist in the account used to create the launch constraint and the account of the user who launches a product with this launch constraint.
        :param role_arn: The ARN of the launch role. You are required to specify ``RoleArn`` or ``LocalRoleName`` but can't use both.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLaunchRoleConstraint.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLaunchRoleConstraintProps(
            portfolio_id=portfolio_id,
            product_id=product_id,
            accept_language=accept_language,
            description=description,
            local_role_name=local_role_name,
            role_arn=role_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLaunchRoleConstraint.inspect)
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
            type_hints = typing.get_type_hints(CfnLaunchRoleConstraint._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-portfolioid
        '''
        return typing.cast(builtins.str, jsii.get(self, "portfolioId"))

    @portfolio_id.setter
    def portfolio_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchRoleConstraint, "portfolio_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portfolioId", value)

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        '''The product identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-productid
        '''
        return typing.cast(builtins.str, jsii.get(self, "productId"))

    @product_id.setter
    def product_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchRoleConstraint, "product_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productId", value)

    @builtins.property
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-acceptlanguage
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceptLanguage"))

    @accept_language.setter
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchRoleConstraint, "accept_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchRoleConstraint, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="localRoleName")
    def local_role_name(self) -> typing.Optional[builtins.str]:
        '''You are required to specify either the ``RoleArn`` or the ``LocalRoleName`` but can't use both.

        If you specify the ``LocalRoleName`` property, when an account uses the launch constraint, the IAM role with that name in the account will be used. This allows launch-role constraints to be account-agnostic so the administrator can create fewer resources per shared account.

        The given role name must exist in the account used to create the launch constraint and the account of the user who launches a product with this launch constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-localrolename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localRoleName"))

    @local_role_name.setter
    def local_role_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchRoleConstraint, "local_role_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localRoleName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the launch role.

        You are required to specify ``RoleArn`` or ``LocalRoleName`` but can't use both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-rolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchRoleConstraint, "role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnLaunchRoleConstraintProps",
    jsii_struct_bases=[],
    name_mapping={
        "portfolio_id": "portfolioId",
        "product_id": "productId",
        "accept_language": "acceptLanguage",
        "description": "description",
        "local_role_name": "localRoleName",
        "role_arn": "roleArn",
    },
)
class CfnLaunchRoleConstraintProps:
    def __init__(
        self,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        local_role_name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnLaunchRoleConstraint``.

        :param portfolio_id: The portfolio identifier.
        :param product_id: The product identifier.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param description: The description of the constraint.
        :param local_role_name: You are required to specify either the ``RoleArn`` or the ``LocalRoleName`` but can't use both. If you specify the ``LocalRoleName`` property, when an account uses the launch constraint, the IAM role with that name in the account will be used. This allows launch-role constraints to be account-agnostic so the administrator can create fewer resources per shared account. The given role name must exist in the account used to create the launch constraint and the account of the user who launches a product with this launch constraint.
        :param role_arn: The ARN of the launch role. You are required to specify ``RoleArn`` or ``LocalRoleName`` but can't use both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cfn_launch_role_constraint_props = servicecatalog.CfnLaunchRoleConstraintProps(
                portfolio_id="portfolioId",
                product_id="productId",
            
                # the properties below are optional
                accept_language="acceptLanguage",
                description="description",
                local_role_name="localRoleName",
                role_arn="roleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLaunchRoleConstraintProps.__init__)
            check_type(argname="argument portfolio_id", value=portfolio_id, expected_type=type_hints["portfolio_id"])
            check_type(argname="argument product_id", value=product_id, expected_type=type_hints["product_id"])
            check_type(argname="argument accept_language", value=accept_language, expected_type=type_hints["accept_language"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument local_role_name", value=local_role_name, expected_type=type_hints["local_role_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "portfolio_id": portfolio_id,
            "product_id": product_id,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if description is not None:
            self._values["description"] = description
        if local_role_name is not None:
            self._values["local_role_name"] = local_role_name
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-portfolioid
        '''
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_id(self) -> builtins.str:
        '''The product identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-productid
        '''
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-acceptlanguage
        '''
        result = self._values.get("accept_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_role_name(self) -> typing.Optional[builtins.str]:
        '''You are required to specify either the ``RoleArn`` or the ``LocalRoleName`` but can't use both.

        If you specify the ``LocalRoleName`` property, when an account uses the launch constraint, the IAM role with that name in the account will be used. This allows launch-role constraints to be account-agnostic so the administrator can create fewer resources per shared account.

        The given role name must exist in the account used to create the launch constraint and the account of the user who launches a product with this launch constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-localrolename
        '''
        result = self._values.get("local_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the launch role.

        You are required to specify ``RoleArn`` or ``LocalRoleName`` but can't use both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLaunchRoleConstraintProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLaunchTemplateConstraint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnLaunchTemplateConstraint",
):
    '''A CloudFormation ``AWS::ServiceCatalog::LaunchTemplateConstraint``.

    Specifies a template constraint.

    :cloudformationResource: AWS::ServiceCatalog::LaunchTemplateConstraint
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        cfn_launch_template_constraint = servicecatalog.CfnLaunchTemplateConstraint(self, "MyCfnLaunchTemplateConstraint",
            portfolio_id="portfolioId",
            product_id="productId",
            rules="rules",
        
            # the properties below are optional
            accept_language="acceptLanguage",
            description="description"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        rules: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::LaunchTemplateConstraint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param portfolio_id: The portfolio identifier.
        :param product_id: The product identifier.
        :param rules: The constraint rules.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param description: The description of the constraint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLaunchTemplateConstraint.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLaunchTemplateConstraintProps(
            portfolio_id=portfolio_id,
            product_id=product_id,
            rules=rules,
            accept_language=accept_language,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLaunchTemplateConstraint.inspect)
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
            type_hints = typing.get_type_hints(CfnLaunchTemplateConstraint._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-portfolioid
        '''
        return typing.cast(builtins.str, jsii.get(self, "portfolioId"))

    @portfolio_id.setter
    def portfolio_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchTemplateConstraint, "portfolio_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portfolioId", value)

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        '''The product identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-productid
        '''
        return typing.cast(builtins.str, jsii.get(self, "productId"))

    @product_id.setter
    def product_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchTemplateConstraint, "product_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productId", value)

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> builtins.str:
        '''The constraint rules.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-rules
        '''
        return typing.cast(builtins.str, jsii.get(self, "rules"))

    @rules.setter
    def rules(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchTemplateConstraint, "rules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rules", value)

    @builtins.property
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-acceptlanguage
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceptLanguage"))

    @accept_language.setter
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchTemplateConstraint, "accept_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLaunchTemplateConstraint, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnLaunchTemplateConstraintProps",
    jsii_struct_bases=[],
    name_mapping={
        "portfolio_id": "portfolioId",
        "product_id": "productId",
        "rules": "rules",
        "accept_language": "acceptLanguage",
        "description": "description",
    },
)
class CfnLaunchTemplateConstraintProps:
    def __init__(
        self,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        rules: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnLaunchTemplateConstraint``.

        :param portfolio_id: The portfolio identifier.
        :param product_id: The product identifier.
        :param rules: The constraint rules.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param description: The description of the constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cfn_launch_template_constraint_props = servicecatalog.CfnLaunchTemplateConstraintProps(
                portfolio_id="portfolioId",
                product_id="productId",
                rules="rules",
            
                # the properties below are optional
                accept_language="acceptLanguage",
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLaunchTemplateConstraintProps.__init__)
            check_type(argname="argument portfolio_id", value=portfolio_id, expected_type=type_hints["portfolio_id"])
            check_type(argname="argument product_id", value=product_id, expected_type=type_hints["product_id"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument accept_language", value=accept_language, expected_type=type_hints["accept_language"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "portfolio_id": portfolio_id,
            "product_id": product_id,
            "rules": rules,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-portfolioid
        '''
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_id(self) -> builtins.str:
        '''The product identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-productid
        '''
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rules(self) -> builtins.str:
        '''The constraint rules.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-rules
        '''
        result = self._values.get("rules")
        assert result is not None, "Required property 'rules' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-acceptlanguage
        '''
        result = self._values.get("accept_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLaunchTemplateConstraintProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPortfolio(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnPortfolio",
):
    '''A CloudFormation ``AWS::ServiceCatalog::Portfolio``.

    Specifies a portfolio.

    :cloudformationResource: AWS::ServiceCatalog::Portfolio
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        cfn_portfolio = servicecatalog.CfnPortfolio(self, "MyCfnPortfolio",
            display_name="displayName",
            provider_name="providerName",
        
            # the properties below are optional
            accept_language="acceptLanguage",
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        display_name: builtins.str,
        provider_name: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::Portfolio``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param display_name: The name to use for display purposes.
        :param provider_name: The name of the portfolio provider.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param description: The description of the portfolio.
        :param tags: One or more tags.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPortfolio.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPortfolioProps(
            display_name=display_name,
            provider_name=provider_name,
            accept_language=accept_language,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPortfolio.inspect)
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
            type_hints = typing.get_type_hints(CfnPortfolio._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPortfolioName")
    def attr_portfolio_name(self) -> builtins.str:
        '''The name of the portfolio.

        :cloudformationAttribute: PortfolioName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPortfolioName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''One or more tags.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''The name to use for display purposes.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-displayname
        '''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolio, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> builtins.str:
        '''The name of the portfolio provider.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-providername
        '''
        return typing.cast(builtins.str, jsii.get(self, "providerName"))

    @provider_name.setter
    def provider_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolio, "provider_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "providerName", value)

    @builtins.property
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-acceptlanguage
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceptLanguage"))

    @accept_language.setter
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolio, "accept_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the portfolio.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolio, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.implements(_IInspectable_c2943556)
class CfnPortfolioPrincipalAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnPortfolioPrincipalAssociation",
):
    '''A CloudFormation ``AWS::ServiceCatalog::PortfolioPrincipalAssociation``.

    Associates the specified principal ARN with the specified portfolio.

    :cloudformationResource: AWS::ServiceCatalog::PortfolioPrincipalAssociation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        cfn_portfolio_principal_association = servicecatalog.CfnPortfolioPrincipalAssociation(self, "MyCfnPortfolioPrincipalAssociation",
            portfolio_id="portfolioId",
            principal_arn="principalArn",
            principal_type="principalType",
        
            # the properties below are optional
            accept_language="acceptLanguage"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        portfolio_id: builtins.str,
        principal_arn: builtins.str,
        principal_type: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::PortfolioPrincipalAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param portfolio_id: The portfolio identifier.
        :param principal_arn: The ARN of the principal (IAM user, role, or group).
        :param principal_type: The principal type. The supported value is ``IAM`` .
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPortfolioPrincipalAssociation.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPortfolioPrincipalAssociationProps(
            portfolio_id=portfolio_id,
            principal_arn=principal_arn,
            principal_type=principal_type,
            accept_language=accept_language,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPortfolioPrincipalAssociation.inspect)
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
            type_hints = typing.get_type_hints(CfnPortfolioPrincipalAssociation._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-portfolioid
        '''
        return typing.cast(builtins.str, jsii.get(self, "portfolioId"))

    @portfolio_id.setter
    def portfolio_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolioPrincipalAssociation, "portfolio_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portfolioId", value)

    @builtins.property
    @jsii.member(jsii_name="principalArn")
    def principal_arn(self) -> builtins.str:
        '''The ARN of the principal (IAM user, role, or group).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-principalarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "principalArn"))

    @principal_arn.setter
    def principal_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolioPrincipalAssociation, "principal_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principalArn", value)

    @builtins.property
    @jsii.member(jsii_name="principalType")
    def principal_type(self) -> builtins.str:
        '''The principal type.

        The supported value is ``IAM`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-principaltype
        '''
        return typing.cast(builtins.str, jsii.get(self, "principalType"))

    @principal_type.setter
    def principal_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolioPrincipalAssociation, "principal_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principalType", value)

    @builtins.property
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-acceptlanguage
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceptLanguage"))

    @accept_language.setter
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolioPrincipalAssociation, "accept_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptLanguage", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnPortfolioPrincipalAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "portfolio_id": "portfolioId",
        "principal_arn": "principalArn",
        "principal_type": "principalType",
        "accept_language": "acceptLanguage",
    },
)
class CfnPortfolioPrincipalAssociationProps:
    def __init__(
        self,
        *,
        portfolio_id: builtins.str,
        principal_arn: builtins.str,
        principal_type: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPortfolioPrincipalAssociation``.

        :param portfolio_id: The portfolio identifier.
        :param principal_arn: The ARN of the principal (IAM user, role, or group).
        :param principal_type: The principal type. The supported value is ``IAM`` .
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cfn_portfolio_principal_association_props = servicecatalog.CfnPortfolioPrincipalAssociationProps(
                portfolio_id="portfolioId",
                principal_arn="principalArn",
                principal_type="principalType",
            
                # the properties below are optional
                accept_language="acceptLanguage"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPortfolioPrincipalAssociationProps.__init__)
            check_type(argname="argument portfolio_id", value=portfolio_id, expected_type=type_hints["portfolio_id"])
            check_type(argname="argument principal_arn", value=principal_arn, expected_type=type_hints["principal_arn"])
            check_type(argname="argument principal_type", value=principal_type, expected_type=type_hints["principal_type"])
            check_type(argname="argument accept_language", value=accept_language, expected_type=type_hints["accept_language"])
        self._values: typing.Dict[str, typing.Any] = {
            "portfolio_id": portfolio_id,
            "principal_arn": principal_arn,
            "principal_type": principal_type,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-portfolioid
        '''
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_arn(self) -> builtins.str:
        '''The ARN of the principal (IAM user, role, or group).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-principalarn
        '''
        result = self._values.get("principal_arn")
        assert result is not None, "Required property 'principal_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_type(self) -> builtins.str:
        '''The principal type.

        The supported value is ``IAM`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-principaltype
        '''
        result = self._values.get("principal_type")
        assert result is not None, "Required property 'principal_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-acceptlanguage
        '''
        result = self._values.get("accept_language")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPortfolioPrincipalAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPortfolioProductAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnPortfolioProductAssociation",
):
    '''A CloudFormation ``AWS::ServiceCatalog::PortfolioProductAssociation``.

    Associates the specified product with the specified portfolio.

    A delegated admin is authorized to invoke this command.

    :cloudformationResource: AWS::ServiceCatalog::PortfolioProductAssociation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        cfn_portfolio_product_association = servicecatalog.CfnPortfolioProductAssociation(self, "MyCfnPortfolioProductAssociation",
            portfolio_id="portfolioId",
            product_id="productId",
        
            # the properties below are optional
            accept_language="acceptLanguage",
            source_portfolio_id="sourcePortfolioId"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        source_portfolio_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::PortfolioProductAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param portfolio_id: The portfolio identifier.
        :param product_id: The product identifier.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param source_portfolio_id: The identifier of the source portfolio.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPortfolioProductAssociation.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPortfolioProductAssociationProps(
            portfolio_id=portfolio_id,
            product_id=product_id,
            accept_language=accept_language,
            source_portfolio_id=source_portfolio_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPortfolioProductAssociation.inspect)
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
            type_hints = typing.get_type_hints(CfnPortfolioProductAssociation._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-portfolioid
        '''
        return typing.cast(builtins.str, jsii.get(self, "portfolioId"))

    @portfolio_id.setter
    def portfolio_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolioProductAssociation, "portfolio_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portfolioId", value)

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        '''The product identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-productid
        '''
        return typing.cast(builtins.str, jsii.get(self, "productId"))

    @product_id.setter
    def product_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolioProductAssociation, "product_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productId", value)

    @builtins.property
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-acceptlanguage
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceptLanguage"))

    @accept_language.setter
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolioProductAssociation, "accept_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="sourcePortfolioId")
    def source_portfolio_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the source portfolio.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-sourceportfolioid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourcePortfolioId"))

    @source_portfolio_id.setter
    def source_portfolio_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolioProductAssociation, "source_portfolio_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourcePortfolioId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnPortfolioProductAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "portfolio_id": "portfolioId",
        "product_id": "productId",
        "accept_language": "acceptLanguage",
        "source_portfolio_id": "sourcePortfolioId",
    },
)
class CfnPortfolioProductAssociationProps:
    def __init__(
        self,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        source_portfolio_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPortfolioProductAssociation``.

        :param portfolio_id: The portfolio identifier.
        :param product_id: The product identifier.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param source_portfolio_id: The identifier of the source portfolio.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cfn_portfolio_product_association_props = servicecatalog.CfnPortfolioProductAssociationProps(
                portfolio_id="portfolioId",
                product_id="productId",
            
                # the properties below are optional
                accept_language="acceptLanguage",
                source_portfolio_id="sourcePortfolioId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPortfolioProductAssociationProps.__init__)
            check_type(argname="argument portfolio_id", value=portfolio_id, expected_type=type_hints["portfolio_id"])
            check_type(argname="argument product_id", value=product_id, expected_type=type_hints["product_id"])
            check_type(argname="argument accept_language", value=accept_language, expected_type=type_hints["accept_language"])
            check_type(argname="argument source_portfolio_id", value=source_portfolio_id, expected_type=type_hints["source_portfolio_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "portfolio_id": portfolio_id,
            "product_id": product_id,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if source_portfolio_id is not None:
            self._values["source_portfolio_id"] = source_portfolio_id

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-portfolioid
        '''
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_id(self) -> builtins.str:
        '''The product identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-productid
        '''
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-acceptlanguage
        '''
        result = self._values.get("accept_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_portfolio_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the source portfolio.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-sourceportfolioid
        '''
        result = self._values.get("source_portfolio_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPortfolioProductAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnPortfolioProps",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "provider_name": "providerName",
        "accept_language": "acceptLanguage",
        "description": "description",
        "tags": "tags",
    },
)
class CfnPortfolioProps:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        provider_name: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPortfolio``.

        :param display_name: The name to use for display purposes.
        :param provider_name: The name of the portfolio provider.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param description: The description of the portfolio.
        :param tags: One or more tags.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cfn_portfolio_props = servicecatalog.CfnPortfolioProps(
                display_name="displayName",
                provider_name="providerName",
            
                # the properties below are optional
                accept_language="acceptLanguage",
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPortfolioProps.__init__)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument accept_language", value=accept_language, expected_type=type_hints["accept_language"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
            "provider_name": provider_name,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name to use for display purposes.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def provider_name(self) -> builtins.str:
        '''The name of the portfolio provider.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-providername
        '''
        result = self._values.get("provider_name")
        assert result is not None, "Required property 'provider_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-acceptlanguage
        '''
        result = self._values.get("accept_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the portfolio.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more tags.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPortfolioProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPortfolioShare(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnPortfolioShare",
):
    '''A CloudFormation ``AWS::ServiceCatalog::PortfolioShare``.

    Shares the specified portfolio with the specified account.

    :cloudformationResource: AWS::ServiceCatalog::PortfolioShare
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        cfn_portfolio_share = servicecatalog.CfnPortfolioShare(self, "MyCfnPortfolioShare",
            account_id="accountId",
            portfolio_id="portfolioId",
        
            # the properties below are optional
            accept_language="acceptLanguage",
            share_tag_options=False
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account_id: builtins.str,
        portfolio_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        share_tag_options: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::PortfolioShare``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param account_id: The AWS account ID. For example, ``123456789012`` .
        :param portfolio_id: The portfolio identifier.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param share_tag_options: Indicates whether TagOptions sharing is enabled or disabled for the portfolio share.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPortfolioShare.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPortfolioShareProps(
            account_id=account_id,
            portfolio_id=portfolio_id,
            accept_language=accept_language,
            share_tag_options=share_tag_options,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPortfolioShare.inspect)
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
            type_hints = typing.get_type_hints(CfnPortfolioShare._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        '''The AWS account ID.

        For example, ``123456789012`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-accountid
        '''
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolioShare, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-portfolioid
        '''
        return typing.cast(builtins.str, jsii.get(self, "portfolioId"))

    @portfolio_id.setter
    def portfolio_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolioShare, "portfolio_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portfolioId", value)

    @builtins.property
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-acceptlanguage
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceptLanguage"))

    @accept_language.setter
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolioShare, "accept_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="shareTagOptions")
    def share_tag_options(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether TagOptions sharing is enabled or disabled for the portfolio share.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-sharetagoptions
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "shareTagOptions"))

    @share_tag_options.setter
    def share_tag_options(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPortfolioShare, "share_tag_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareTagOptions", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnPortfolioShareProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "portfolio_id": "portfolioId",
        "accept_language": "acceptLanguage",
        "share_tag_options": "shareTagOptions",
    },
)
class CfnPortfolioShareProps:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        portfolio_id: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        share_tag_options: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPortfolioShare``.

        :param account_id: The AWS account ID. For example, ``123456789012`` .
        :param portfolio_id: The portfolio identifier.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param share_tag_options: Indicates whether TagOptions sharing is enabled or disabled for the portfolio share.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cfn_portfolio_share_props = servicecatalog.CfnPortfolioShareProps(
                account_id="accountId",
                portfolio_id="portfolioId",
            
                # the properties below are optional
                accept_language="acceptLanguage",
                share_tag_options=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPortfolioShareProps.__init__)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument portfolio_id", value=portfolio_id, expected_type=type_hints["portfolio_id"])
            check_type(argname="argument accept_language", value=accept_language, expected_type=type_hints["accept_language"])
            check_type(argname="argument share_tag_options", value=share_tag_options, expected_type=type_hints["share_tag_options"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
            "portfolio_id": portfolio_id,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if share_tag_options is not None:
            self._values["share_tag_options"] = share_tag_options

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AWS account ID.

        For example, ``123456789012`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-accountid
        '''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-portfolioid
        '''
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-acceptlanguage
        '''
        result = self._values.get("accept_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def share_tag_options(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether TagOptions sharing is enabled or disabled for the portfolio share.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-sharetagoptions
        '''
        result = self._values.get("share_tag_options")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPortfolioShareProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourceUpdateConstraint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnResourceUpdateConstraint",
):
    '''A CloudFormation ``AWS::ServiceCatalog::ResourceUpdateConstraint``.

    Specifies a ``RESOURCE_UPDATE`` constraint.

    :cloudformationResource: AWS::ServiceCatalog::ResourceUpdateConstraint
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        cfn_resource_update_constraint = servicecatalog.CfnResourceUpdateConstraint(self, "MyCfnResourceUpdateConstraint",
            portfolio_id="portfolioId",
            product_id="productId",
            tag_update_on_provisioned_product="tagUpdateOnProvisionedProduct",
        
            # the properties below are optional
            accept_language="acceptLanguage",
            description="description"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        tag_update_on_provisioned_product: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::ResourceUpdateConstraint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param portfolio_id: The portfolio identifier.
        :param product_id: The product identifier.
        :param tag_update_on_provisioned_product: If set to ``ALLOWED`` , lets users change tags in a `CloudFormationProvisionedProduct <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html>`_ resource. If set to ``NOT_ALLOWED`` , prevents users from changing tags in a `CloudFormationProvisionedProduct <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html>`_ resource.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param description: The description of the constraint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnResourceUpdateConstraint.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceUpdateConstraintProps(
            portfolio_id=portfolio_id,
            product_id=product_id,
            tag_update_on_provisioned_product=tag_update_on_provisioned_product,
            accept_language=accept_language,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnResourceUpdateConstraint.inspect)
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
            type_hints = typing.get_type_hints(CfnResourceUpdateConstraint._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-portfolioid
        '''
        return typing.cast(builtins.str, jsii.get(self, "portfolioId"))

    @portfolio_id.setter
    def portfolio_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResourceUpdateConstraint, "portfolio_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portfolioId", value)

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        '''The product identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-productid
        '''
        return typing.cast(builtins.str, jsii.get(self, "productId"))

    @product_id.setter
    def product_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResourceUpdateConstraint, "product_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productId", value)

    @builtins.property
    @jsii.member(jsii_name="tagUpdateOnProvisionedProduct")
    def tag_update_on_provisioned_product(self) -> builtins.str:
        '''If set to ``ALLOWED`` , lets users change tags in a `CloudFormationProvisionedProduct <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html>`_ resource.

        If set to ``NOT_ALLOWED`` , prevents users from changing tags in a `CloudFormationProvisionedProduct <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html>`_ resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-tagupdateonprovisionedproduct
        '''
        return typing.cast(builtins.str, jsii.get(self, "tagUpdateOnProvisionedProduct"))

    @tag_update_on_provisioned_product.setter
    def tag_update_on_provisioned_product(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResourceUpdateConstraint, "tag_update_on_provisioned_product").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagUpdateOnProvisionedProduct", value)

    @builtins.property
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-acceptlanguage
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceptLanguage"))

    @accept_language.setter
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResourceUpdateConstraint, "accept_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResourceUpdateConstraint, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnResourceUpdateConstraintProps",
    jsii_struct_bases=[],
    name_mapping={
        "portfolio_id": "portfolioId",
        "product_id": "productId",
        "tag_update_on_provisioned_product": "tagUpdateOnProvisionedProduct",
        "accept_language": "acceptLanguage",
        "description": "description",
    },
)
class CfnResourceUpdateConstraintProps:
    def __init__(
        self,
        *,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        tag_update_on_provisioned_product: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnResourceUpdateConstraint``.

        :param portfolio_id: The portfolio identifier.
        :param product_id: The product identifier.
        :param tag_update_on_provisioned_product: If set to ``ALLOWED`` , lets users change tags in a `CloudFormationProvisionedProduct <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html>`_ resource. If set to ``NOT_ALLOWED`` , prevents users from changing tags in a `CloudFormationProvisionedProduct <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html>`_ resource.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param description: The description of the constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cfn_resource_update_constraint_props = servicecatalog.CfnResourceUpdateConstraintProps(
                portfolio_id="portfolioId",
                product_id="productId",
                tag_update_on_provisioned_product="tagUpdateOnProvisionedProduct",
            
                # the properties below are optional
                accept_language="acceptLanguage",
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnResourceUpdateConstraintProps.__init__)
            check_type(argname="argument portfolio_id", value=portfolio_id, expected_type=type_hints["portfolio_id"])
            check_type(argname="argument product_id", value=product_id, expected_type=type_hints["product_id"])
            check_type(argname="argument tag_update_on_provisioned_product", value=tag_update_on_provisioned_product, expected_type=type_hints["tag_update_on_provisioned_product"])
            check_type(argname="argument accept_language", value=accept_language, expected_type=type_hints["accept_language"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "portfolio_id": portfolio_id,
            "product_id": product_id,
            "tag_update_on_provisioned_product": tag_update_on_provisioned_product,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-portfolioid
        '''
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_id(self) -> builtins.str:
        '''The product identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-productid
        '''
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tag_update_on_provisioned_product(self) -> builtins.str:
        '''If set to ``ALLOWED`` , lets users change tags in a `CloudFormationProvisionedProduct <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html>`_ resource.

        If set to ``NOT_ALLOWED`` , prevents users from changing tags in a `CloudFormationProvisionedProduct <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html>`_ resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-tagupdateonprovisionedproduct
        '''
        result = self._values.get("tag_update_on_provisioned_product")
        assert result is not None, "Required property 'tag_update_on_provisioned_product' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-acceptlanguage
        '''
        result = self._values.get("accept_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceUpdateConstraintProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnServiceAction(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnServiceAction",
):
    '''A CloudFormation ``AWS::ServiceCatalog::ServiceAction``.

    Creates a self-service action.

    :cloudformationResource: AWS::ServiceCatalog::ServiceAction
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        cfn_service_action = servicecatalog.CfnServiceAction(self, "MyCfnServiceAction",
            definition=[servicecatalog.CfnServiceAction.DefinitionParameterProperty(
                key="key",
                value="value"
            )],
            definition_type="definitionType",
            name="name",
        
            # the properties below are optional
            accept_language="acceptLanguage",
            description="description"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        definition: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnServiceAction.DefinitionParameterProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        definition_type: builtins.str,
        name: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::ServiceAction``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param definition: A map that defines the self-service action.
        :param definition_type: The self-service action definition type. For example, ``SSM_AUTOMATION`` .
        :param name: The self-service action name.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param description: The self-service action description.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnServiceAction.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceActionProps(
            definition=definition,
            definition_type=definition_type,
            name=name,
            accept_language=accept_language,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnServiceAction.inspect)
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
            type_hints = typing.get_type_hints(CfnServiceAction._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The self-service action identifier.

        For example, ``act-fs7abcd89wxyz`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnServiceAction.DefinitionParameterProperty", _IResolvable_da3f097b]]]:
        '''A map that defines the self-service action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-definition
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnServiceAction.DefinitionParameterProperty", _IResolvable_da3f097b]]], jsii.get(self, "definition"))

    @definition.setter
    def definition(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnServiceAction.DefinitionParameterProperty", _IResolvable_da3f097b]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnServiceAction, "definition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definition", value)

    @builtins.property
    @jsii.member(jsii_name="definitionType")
    def definition_type(self) -> builtins.str:
        '''The self-service action definition type.

        For example, ``SSM_AUTOMATION`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-definitiontype
        '''
        return typing.cast(builtins.str, jsii.get(self, "definitionType"))

    @definition_type.setter
    def definition_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnServiceAction, "definition_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The self-service action name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnServiceAction, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-acceptlanguage
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceptLanguage"))

    @accept_language.setter
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnServiceAction, "accept_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The self-service action description.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnServiceAction, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_servicecatalog.CfnServiceAction.DefinitionParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class DefinitionParameterProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''The list of parameters in JSON format.

            For example: ``[{\\"Name\\":\\"InstanceId\\",\\"Type\\":\\"TARGET\\"}] or [{\\"Name\\":\\"InstanceId\\",\\"Type\\":\\"TEXT_VALUE\\"}]`` .

            :param key: The parameter key.
            :param value: The value of the parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-serviceaction-definitionparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_servicecatalog as servicecatalog
                
                definition_parameter_property = servicecatalog.CfnServiceAction.DefinitionParameterProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnServiceAction.DefinitionParameterProperty.__init__)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The parameter key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-serviceaction-definitionparameter.html#cfn-servicecatalog-serviceaction-definitionparameter-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value of the parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-serviceaction-definitionparameter.html#cfn-servicecatalog-serviceaction-definitionparameter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefinitionParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnServiceActionAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnServiceActionAssociation",
):
    '''A CloudFormation ``AWS::ServiceCatalog::ServiceActionAssociation``.

    A self-service action association consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.

    :cloudformationResource: AWS::ServiceCatalog::ServiceActionAssociation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        cfn_service_action_association = servicecatalog.CfnServiceActionAssociation(self, "MyCfnServiceActionAssociation",
            product_id="productId",
            provisioning_artifact_id="provisioningArtifactId",
            service_action_id="serviceActionId"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        product_id: builtins.str,
        provisioning_artifact_id: builtins.str,
        service_action_id: builtins.str,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::ServiceActionAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param product_id: The product identifier. For example, ``prod-abcdzk7xy33qa`` .
        :param provisioning_artifact_id: The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
        :param service_action_id: The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnServiceActionAssociation.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceActionAssociationProps(
            product_id=product_id,
            provisioning_artifact_id=provisioning_artifact_id,
            service_action_id=service_action_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnServiceActionAssociation.inspect)
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
            type_hints = typing.get_type_hints(CfnServiceActionAssociation._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        '''The product identifier.

        For example, ``prod-abcdzk7xy33qa`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-productid
        '''
        return typing.cast(builtins.str, jsii.get(self, "productId"))

    @product_id.setter
    def product_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnServiceActionAssociation, "product_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productId", value)

    @builtins.property
    @jsii.member(jsii_name="provisioningArtifactId")
    def provisioning_artifact_id(self) -> builtins.str:
        '''The identifier of the provisioning artifact.

        For example, ``pa-4abcdjnxjj6ne`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-provisioningartifactid
        '''
        return typing.cast(builtins.str, jsii.get(self, "provisioningArtifactId"))

    @provisioning_artifact_id.setter
    def provisioning_artifact_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnServiceActionAssociation, "provisioning_artifact_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioningArtifactId", value)

    @builtins.property
    @jsii.member(jsii_name="serviceActionId")
    def service_action_id(self) -> builtins.str:
        '''The self-service action identifier.

        For example, ``act-fs7abcd89wxyz`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-serviceactionid
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceActionId"))

    @service_action_id.setter
    def service_action_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnServiceActionAssociation, "service_action_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceActionId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnServiceActionAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "product_id": "productId",
        "provisioning_artifact_id": "provisioningArtifactId",
        "service_action_id": "serviceActionId",
    },
)
class CfnServiceActionAssociationProps:
    def __init__(
        self,
        *,
        product_id: builtins.str,
        provisioning_artifact_id: builtins.str,
        service_action_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnServiceActionAssociation``.

        :param product_id: The product identifier. For example, ``prod-abcdzk7xy33qa`` .
        :param provisioning_artifact_id: The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
        :param service_action_id: The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cfn_service_action_association_props = servicecatalog.CfnServiceActionAssociationProps(
                product_id="productId",
                provisioning_artifact_id="provisioningArtifactId",
                service_action_id="serviceActionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnServiceActionAssociationProps.__init__)
            check_type(argname="argument product_id", value=product_id, expected_type=type_hints["product_id"])
            check_type(argname="argument provisioning_artifact_id", value=provisioning_artifact_id, expected_type=type_hints["provisioning_artifact_id"])
            check_type(argname="argument service_action_id", value=service_action_id, expected_type=type_hints["service_action_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "product_id": product_id,
            "provisioning_artifact_id": provisioning_artifact_id,
            "service_action_id": service_action_id,
        }

    @builtins.property
    def product_id(self) -> builtins.str:
        '''The product identifier.

        For example, ``prod-abcdzk7xy33qa`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-productid
        '''
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def provisioning_artifact_id(self) -> builtins.str:
        '''The identifier of the provisioning artifact.

        For example, ``pa-4abcdjnxjj6ne`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-provisioningartifactid
        '''
        result = self._values.get("provisioning_artifact_id")
        assert result is not None, "Required property 'provisioning_artifact_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_action_id(self) -> builtins.str:
        '''The self-service action identifier.

        For example, ``act-fs7abcd89wxyz`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-serviceactionid
        '''
        result = self._values.get("service_action_id")
        assert result is not None, "Required property 'service_action_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceActionAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnServiceActionProps",
    jsii_struct_bases=[],
    name_mapping={
        "definition": "definition",
        "definition_type": "definitionType",
        "name": "name",
        "accept_language": "acceptLanguage",
        "description": "description",
    },
)
class CfnServiceActionProps:
    def __init__(
        self,
        *,
        definition: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnServiceAction.DefinitionParameterProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
        definition_type: builtins.str,
        name: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnServiceAction``.

        :param definition: A map that defines the self-service action.
        :param definition_type: The self-service action definition type. For example, ``SSM_AUTOMATION`` .
        :param name: The self-service action name.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        :param description: The self-service action description.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cfn_service_action_props = servicecatalog.CfnServiceActionProps(
                definition=[servicecatalog.CfnServiceAction.DefinitionParameterProperty(
                    key="key",
                    value="value"
                )],
                definition_type="definitionType",
                name="name",
            
                # the properties below are optional
                accept_language="acceptLanguage",
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnServiceActionProps.__init__)
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            check_type(argname="argument definition_type", value=definition_type, expected_type=type_hints["definition_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument accept_language", value=accept_language, expected_type=type_hints["accept_language"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "definition": definition,
            "definition_type": definition_type,
            "name": name,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def definition(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnServiceAction.DefinitionParameterProperty, _IResolvable_da3f097b]]]:
        '''A map that defines the self-service action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-definition
        '''
        result = self._values.get("definition")
        assert result is not None, "Required property 'definition' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnServiceAction.DefinitionParameterProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def definition_type(self) -> builtins.str:
        '''The self-service action definition type.

        For example, ``SSM_AUTOMATION`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-definitiontype
        '''
        result = self._values.get("definition_type")
        assert result is not None, "Required property 'definition_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The self-service action name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-acceptlanguage
        '''
        result = self._values.get("accept_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The self-service action description.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnStackSetConstraint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnStackSetConstraint",
):
    '''A CloudFormation ``AWS::ServiceCatalog::StackSetConstraint``.

    Specifies a StackSet constraint.

    :cloudformationResource: AWS::ServiceCatalog::StackSetConstraint
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        cfn_stack_set_constraint = servicecatalog.CfnStackSetConstraint(self, "MyCfnStackSetConstraint",
            account_list=["accountList"],
            admin_role="adminRole",
            description="description",
            execution_role="executionRole",
            portfolio_id="portfolioId",
            product_id="productId",
            region_list=["regionList"],
            stack_instance_control="stackInstanceControl",
        
            # the properties below are optional
            accept_language="acceptLanguage"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account_list: typing.Sequence[builtins.str],
        admin_role: builtins.str,
        description: builtins.str,
        execution_role: builtins.str,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        region_list: typing.Sequence[builtins.str],
        stack_instance_control: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::StackSetConstraint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param account_list: One or more AWS accounts that will have access to the provisioned product.
        :param admin_role: AdminRole ARN.
        :param description: The description of the constraint.
        :param execution_role: ExecutionRole name.
        :param portfolio_id: The portfolio identifier.
        :param product_id: The product identifier.
        :param region_list: One or more AWS Regions where the provisioned product will be available. Applicable only to a ``CFN_STACKSET`` provisioned product type. The specified Regions should be within the list of Regions from the ``STACKSET`` constraint. To get the list of Regions in the ``STACKSET`` constraint, use the ``DescribeProvisioningParameters`` operation. If no values are specified, the default value is all Regions from the ``STACKSET`` constraint.
        :param stack_instance_control: Permission to create, update, and delete stack instances. Choose from ALLOWED and NOT_ALLOWED.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnStackSetConstraint.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStackSetConstraintProps(
            account_list=account_list,
            admin_role=admin_role,
            description=description,
            execution_role=execution_role,
            portfolio_id=portfolio_id,
            product_id=product_id,
            region_list=region_list,
            stack_instance_control=stack_instance_control,
            accept_language=accept_language,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnStackSetConstraint.inspect)
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
            type_hints = typing.get_type_hints(CfnStackSetConstraint._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="accountList")
    def account_list(self) -> typing.List[builtins.str]:
        '''One or more AWS accounts that will have access to the provisioned product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-accountlist
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "accountList"))

    @account_list.setter
    def account_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnStackSetConstraint, "account_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountList", value)

    @builtins.property
    @jsii.member(jsii_name="adminRole")
    def admin_role(self) -> builtins.str:
        '''AdminRole ARN.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-adminrole
        '''
        return typing.cast(builtins.str, jsii.get(self, "adminRole"))

    @admin_role.setter
    def admin_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnStackSetConstraint, "admin_role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminRole", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnStackSetConstraint, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="executionRole")
    def execution_role(self) -> builtins.str:
        '''ExecutionRole name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-executionrole
        '''
        return typing.cast(builtins.str, jsii.get(self, "executionRole"))

    @execution_role.setter
    def execution_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnStackSetConstraint, "execution_role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRole", value)

    @builtins.property
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-portfolioid
        '''
        return typing.cast(builtins.str, jsii.get(self, "portfolioId"))

    @portfolio_id.setter
    def portfolio_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnStackSetConstraint, "portfolio_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portfolioId", value)

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        '''The product identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-productid
        '''
        return typing.cast(builtins.str, jsii.get(self, "productId"))

    @product_id.setter
    def product_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnStackSetConstraint, "product_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productId", value)

    @builtins.property
    @jsii.member(jsii_name="regionList")
    def region_list(self) -> typing.List[builtins.str]:
        '''One or more AWS Regions where the provisioned product will be available.

        Applicable only to a ``CFN_STACKSET`` provisioned product type.

        The specified Regions should be within the list of Regions from the ``STACKSET`` constraint. To get the list of Regions in the ``STACKSET`` constraint, use the ``DescribeProvisioningParameters`` operation.

        If no values are specified, the default value is all Regions from the ``STACKSET`` constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-regionlist
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regionList"))

    @region_list.setter
    def region_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnStackSetConstraint, "region_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionList", value)

    @builtins.property
    @jsii.member(jsii_name="stackInstanceControl")
    def stack_instance_control(self) -> builtins.str:
        '''Permission to create, update, and delete stack instances.

        Choose from ALLOWED and NOT_ALLOWED.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-stackinstancecontrol
        '''
        return typing.cast(builtins.str, jsii.get(self, "stackInstanceControl"))

    @stack_instance_control.setter
    def stack_instance_control(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnStackSetConstraint, "stack_instance_control").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackInstanceControl", value)

    @builtins.property
    @jsii.member(jsii_name="acceptLanguage")
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-acceptlanguage
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceptLanguage"))

    @accept_language.setter
    def accept_language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnStackSetConstraint, "accept_language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptLanguage", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnStackSetConstraintProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_list": "accountList",
        "admin_role": "adminRole",
        "description": "description",
        "execution_role": "executionRole",
        "portfolio_id": "portfolioId",
        "product_id": "productId",
        "region_list": "regionList",
        "stack_instance_control": "stackInstanceControl",
        "accept_language": "acceptLanguage",
    },
)
class CfnStackSetConstraintProps:
    def __init__(
        self,
        *,
        account_list: typing.Sequence[builtins.str],
        admin_role: builtins.str,
        description: builtins.str,
        execution_role: builtins.str,
        portfolio_id: builtins.str,
        product_id: builtins.str,
        region_list: typing.Sequence[builtins.str],
        stack_instance_control: builtins.str,
        accept_language: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnStackSetConstraint``.

        :param account_list: One or more AWS accounts that will have access to the provisioned product.
        :param admin_role: AdminRole ARN.
        :param description: The description of the constraint.
        :param execution_role: ExecutionRole name.
        :param portfolio_id: The portfolio identifier.
        :param product_id: The product identifier.
        :param region_list: One or more AWS Regions where the provisioned product will be available. Applicable only to a ``CFN_STACKSET`` provisioned product type. The specified Regions should be within the list of Regions from the ``STACKSET`` constraint. To get the list of Regions in the ``STACKSET`` constraint, use the ``DescribeProvisioningParameters`` operation. If no values are specified, the default value is all Regions from the ``STACKSET`` constraint.
        :param stack_instance_control: Permission to create, update, and delete stack instances. Choose from ALLOWED and NOT_ALLOWED.
        :param accept_language: The language code. - ``en`` - English (default) - ``jp`` - Japanese - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cfn_stack_set_constraint_props = servicecatalog.CfnStackSetConstraintProps(
                account_list=["accountList"],
                admin_role="adminRole",
                description="description",
                execution_role="executionRole",
                portfolio_id="portfolioId",
                product_id="productId",
                region_list=["regionList"],
                stack_instance_control="stackInstanceControl",
            
                # the properties below are optional
                accept_language="acceptLanguage"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnStackSetConstraintProps.__init__)
            check_type(argname="argument account_list", value=account_list, expected_type=type_hints["account_list"])
            check_type(argname="argument admin_role", value=admin_role, expected_type=type_hints["admin_role"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_role", value=execution_role, expected_type=type_hints["execution_role"])
            check_type(argname="argument portfolio_id", value=portfolio_id, expected_type=type_hints["portfolio_id"])
            check_type(argname="argument product_id", value=product_id, expected_type=type_hints["product_id"])
            check_type(argname="argument region_list", value=region_list, expected_type=type_hints["region_list"])
            check_type(argname="argument stack_instance_control", value=stack_instance_control, expected_type=type_hints["stack_instance_control"])
            check_type(argname="argument accept_language", value=accept_language, expected_type=type_hints["accept_language"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_list": account_list,
            "admin_role": admin_role,
            "description": description,
            "execution_role": execution_role,
            "portfolio_id": portfolio_id,
            "product_id": product_id,
            "region_list": region_list,
            "stack_instance_control": stack_instance_control,
        }
        if accept_language is not None:
            self._values["accept_language"] = accept_language

    @builtins.property
    def account_list(self) -> typing.List[builtins.str]:
        '''One or more AWS accounts that will have access to the provisioned product.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-accountlist
        '''
        result = self._values.get("account_list")
        assert result is not None, "Required property 'account_list' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def admin_role(self) -> builtins.str:
        '''AdminRole ARN.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-adminrole
        '''
        result = self._values.get("admin_role")
        assert result is not None, "Required property 'admin_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> builtins.str:
        '''The description of the constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def execution_role(self) -> builtins.str:
        '''ExecutionRole name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-executionrole
        '''
        result = self._values.get("execution_role")
        assert result is not None, "Required property 'execution_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        '''The portfolio identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-portfolioid
        '''
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_id(self) -> builtins.str:
        '''The product identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-productid
        '''
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region_list(self) -> typing.List[builtins.str]:
        '''One or more AWS Regions where the provisioned product will be available.

        Applicable only to a ``CFN_STACKSET`` provisioned product type.

        The specified Regions should be within the list of Regions from the ``STACKSET`` constraint. To get the list of Regions in the ``STACKSET`` constraint, use the ``DescribeProvisioningParameters`` operation.

        If no values are specified, the default value is all Regions from the ``STACKSET`` constraint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-regionlist
        '''
        result = self._values.get("region_list")
        assert result is not None, "Required property 'region_list' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def stack_instance_control(self) -> builtins.str:
        '''Permission to create, update, and delete stack instances.

        Choose from ALLOWED and NOT_ALLOWED.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-stackinstancecontrol
        '''
        result = self._values.get("stack_instance_control")
        assert result is not None, "Required property 'stack_instance_control' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accept_language(self) -> typing.Optional[builtins.str]:
        '''The language code.

        - ``en`` - English (default)
        - ``jp`` - Japanese
        - ``zh`` - Chinese

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-acceptlanguage
        '''
        result = self._values.get("accept_language")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStackSetConstraintProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTagOption(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnTagOption",
):
    '''A CloudFormation ``AWS::ServiceCatalog::TagOption``.

    Specifies a TagOption. A TagOption is a key-value pair managed by AWS Service Catalog that serves as a template for creating an AWS tag.

    :cloudformationResource: AWS::ServiceCatalog::TagOption
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        cfn_tag_option = servicecatalog.CfnTagOption(self, "MyCfnTagOption",
            key="key",
            value="value",
        
            # the properties below are optional
            active=False
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        key: builtins.str,
        value: builtins.str,
        active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::TagOption``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param key: The TagOption key.
        :param value: The TagOption value.
        :param active: The TagOption active state.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTagOption.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTagOptionProps(key=key, value=value, active=active)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTagOption.inspect)
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
            type_hints = typing.get_type_hints(CfnTagOption._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        '''The TagOption key.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-key
        '''
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTagOption, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        '''The TagOption value.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-value
        '''
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTagOption, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="active")
    def active(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The TagOption active state.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-active
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "active"))

    @active.setter
    def active(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTagOption, "active").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "active", value)


@jsii.implements(_IInspectable_c2943556)
class CfnTagOptionAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnTagOptionAssociation",
):
    '''A CloudFormation ``AWS::ServiceCatalog::TagOptionAssociation``.

    Associate the specified TagOption with the specified portfolio or product.

    :cloudformationResource: AWS::ServiceCatalog::TagOptionAssociation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        cfn_tag_option_association = servicecatalog.CfnTagOptionAssociation(self, "MyCfnTagOptionAssociation",
            resource_id="resourceId",
            tag_option_id="tagOptionId"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        resource_id: builtins.str,
        tag_option_id: builtins.str,
    ) -> None:
        '''Create a new ``AWS::ServiceCatalog::TagOptionAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resource_id: The resource identifier.
        :param tag_option_id: The TagOption identifier.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTagOptionAssociation.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTagOptionAssociationProps(
            resource_id=resource_id, tag_option_id=tag_option_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTagOptionAssociation.inspect)
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
            type_hints = typing.get_type_hints(CfnTagOptionAssociation._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        '''The resource identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html#cfn-servicecatalog-tagoptionassociation-resourceid
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTagOptionAssociation, "resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)

    @builtins.property
    @jsii.member(jsii_name="tagOptionId")
    def tag_option_id(self) -> builtins.str:
        '''The TagOption identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html#cfn-servicecatalog-tagoptionassociation-tagoptionid
        '''
        return typing.cast(builtins.str, jsii.get(self, "tagOptionId"))

    @tag_option_id.setter
    def tag_option_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTagOptionAssociation, "tag_option_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagOptionId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnTagOptionAssociationProps",
    jsii_struct_bases=[],
    name_mapping={"resource_id": "resourceId", "tag_option_id": "tagOptionId"},
)
class CfnTagOptionAssociationProps:
    def __init__(
        self,
        *,
        resource_id: builtins.str,
        tag_option_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnTagOptionAssociation``.

        :param resource_id: The resource identifier.
        :param tag_option_id: The TagOption identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cfn_tag_option_association_props = servicecatalog.CfnTagOptionAssociationProps(
                resource_id="resourceId",
                tag_option_id="tagOptionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTagOptionAssociationProps.__init__)
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument tag_option_id", value=tag_option_id, expected_type=type_hints["tag_option_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource_id": resource_id,
            "tag_option_id": tag_option_id,
        }

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''The resource identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html#cfn-servicecatalog-tagoptionassociation-resourceid
        '''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tag_option_id(self) -> builtins.str:
        '''The TagOption identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html#cfn-servicecatalog-tagoptionassociation-tagoptionid
        '''
        result = self._values.get("tag_option_id")
        assert result is not None, "Required property 'tag_option_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTagOptionAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CfnTagOptionProps",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value", "active": "active"},
)
class CfnTagOptionProps:
    def __init__(
        self,
        *,
        key: builtins.str,
        value: builtins.str,
        active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTagOption``.

        :param key: The TagOption key.
        :param value: The TagOption value.
        :param active: The TagOption active state.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cfn_tag_option_props = servicecatalog.CfnTagOptionProps(
                key="key",
                value="value",
            
                # the properties below are optional
                active=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTagOptionProps.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument active", value=active, expected_type=type_hints["active"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }
        if active is not None:
            self._values["active"] = active

    @builtins.property
    def key(self) -> builtins.str:
        '''The TagOption key.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The TagOption value.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-value
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The TagOption active state.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-active
        '''
        result = self._values.get("active")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTagOptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CloudFormationProductProps",
    jsii_struct_bases=[],
    name_mapping={
        "owner": "owner",
        "product_name": "productName",
        "product_versions": "productVersions",
        "description": "description",
        "distributor": "distributor",
        "message_language": "messageLanguage",
        "replace_product_version_ids": "replaceProductVersionIds",
        "support_description": "supportDescription",
        "support_email": "supportEmail",
        "support_url": "supportUrl",
        "tag_options": "tagOptions",
    },
)
class CloudFormationProductProps:
    def __init__(
        self,
        *,
        owner: builtins.str,
        product_name: builtins.str,
        product_versions: typing.Sequence[typing.Union["CloudFormationProductVersion", typing.Dict[str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        distributor: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
        replace_product_version_ids: typing.Optional[builtins.bool] = None,
        support_description: typing.Optional[builtins.str] = None,
        support_email: typing.Optional[builtins.str] = None,
        support_url: typing.Optional[builtins.str] = None,
        tag_options: typing.Optional["TagOptions"] = None,
    ) -> None:
        '''Properties for a Cloudformation Product.

        :param owner: The owner of the product.
        :param product_name: The name of the product.
        :param product_versions: The configuration of the product version.
        :param description: The description of the product. Default: - No description provided
        :param distributor: The distributor of the product. Default: - No distributor provided
        :param message_language: The language code. Controls language for logging and errors. Default: - English
        :param replace_product_version_ids: Whether to give provisioning artifacts a new unique identifier when the product attributes or provisioning artifacts is updated. Default: false
        :param support_description: The support information about the product. Default: - No support description provided
        :param support_email: The contact email for product support. Default: - No support email provided
        :param support_url: The contact URL for product support. Default: - No support URL provided
        :param tag_options: TagOptions associated directly to a product. Default: - No tagOptions provided

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_s3 as s3
            import aws_cdk as cdk
            
            
            class S3BucketProduct(servicecatalog.ProductStack):
                def __init__(self, scope, id):
                    super().__init__(scope, id)
            
                    s3.Bucket(self, "BucketProduct")
            
            product = servicecatalog.CloudFormationProduct(self, "Product",
                product_name="My Product",
                owner="Product Owner",
                product_versions=[servicecatalog.CloudFormationProductVersion(
                    product_version_name="v1",
                    cloud_formation_template=servicecatalog.CloudFormationTemplate.from_product_stack(S3BucketProduct(self, "S3BucketProduct"))
                )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudFormationProductProps.__init__)
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument product_name", value=product_name, expected_type=type_hints["product_name"])
            check_type(argname="argument product_versions", value=product_versions, expected_type=type_hints["product_versions"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument distributor", value=distributor, expected_type=type_hints["distributor"])
            check_type(argname="argument message_language", value=message_language, expected_type=type_hints["message_language"])
            check_type(argname="argument replace_product_version_ids", value=replace_product_version_ids, expected_type=type_hints["replace_product_version_ids"])
            check_type(argname="argument support_description", value=support_description, expected_type=type_hints["support_description"])
            check_type(argname="argument support_email", value=support_email, expected_type=type_hints["support_email"])
            check_type(argname="argument support_url", value=support_url, expected_type=type_hints["support_url"])
            check_type(argname="argument tag_options", value=tag_options, expected_type=type_hints["tag_options"])
        self._values: typing.Dict[str, typing.Any] = {
            "owner": owner,
            "product_name": product_name,
            "product_versions": product_versions,
        }
        if description is not None:
            self._values["description"] = description
        if distributor is not None:
            self._values["distributor"] = distributor
        if message_language is not None:
            self._values["message_language"] = message_language
        if replace_product_version_ids is not None:
            self._values["replace_product_version_ids"] = replace_product_version_ids
        if support_description is not None:
            self._values["support_description"] = support_description
        if support_email is not None:
            self._values["support_email"] = support_email
        if support_url is not None:
            self._values["support_url"] = support_url
        if tag_options is not None:
            self._values["tag_options"] = tag_options

    @builtins.property
    def owner(self) -> builtins.str:
        '''The owner of the product.'''
        result = self._values.get("owner")
        assert result is not None, "Required property 'owner' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_name(self) -> builtins.str:
        '''The name of the product.'''
        result = self._values.get("product_name")
        assert result is not None, "Required property 'product_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_versions(self) -> typing.List["CloudFormationProductVersion"]:
        '''The configuration of the product version.'''
        result = self._values.get("product_versions")
        assert result is not None, "Required property 'product_versions' is missing"
        return typing.cast(typing.List["CloudFormationProductVersion"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the product.

        :default: - No description provided
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distributor(self) -> typing.Optional[builtins.str]:
        '''The distributor of the product.

        :default: - No distributor provided
        '''
        result = self._values.get("distributor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message_language(self) -> typing.Optional["MessageLanguage"]:
        '''The language code.

        Controls language for logging and errors.

        :default: - English
        '''
        result = self._values.get("message_language")
        return typing.cast(typing.Optional["MessageLanguage"], result)

    @builtins.property
    def replace_product_version_ids(self) -> typing.Optional[builtins.bool]:
        '''Whether to give provisioning artifacts a new unique identifier when the product attributes or provisioning artifacts is updated.

        :default: false
        '''
        result = self._values.get("replace_product_version_ids")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def support_description(self) -> typing.Optional[builtins.str]:
        '''The support information about the product.

        :default: - No support description provided
        '''
        result = self._values.get("support_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def support_email(self) -> typing.Optional[builtins.str]:
        '''The contact email for product support.

        :default: - No support email provided
        '''
        result = self._values.get("support_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def support_url(self) -> typing.Optional[builtins.str]:
        '''The contact URL for product support.

        :default: - No support URL provided
        '''
        result = self._values.get("support_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_options(self) -> typing.Optional["TagOptions"]:
        '''TagOptions associated directly to a product.

        :default: - No tagOptions provided
        '''
        result = self._values.get("tag_options")
        return typing.cast(typing.Optional["TagOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFormationProductProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CloudFormationProductVersion",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_formation_template": "cloudFormationTemplate",
        "description": "description",
        "product_version_name": "productVersionName",
        "validate_template": "validateTemplate",
    },
)
class CloudFormationProductVersion:
    def __init__(
        self,
        *,
        cloud_formation_template: "CloudFormationTemplate",
        description: typing.Optional[builtins.str] = None,
        product_version_name: typing.Optional[builtins.str] = None,
        validate_template: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties of product version (also known as a provisioning artifact).

        :param cloud_formation_template: The S3 template that points to the provisioning version template.
        :param description: The description of the product version. Default: - No description provided
        :param product_version_name: The name of the product version. Default: - No product version name provided
        :param validate_template: Whether the specified product template will be validated by CloudFormation. If turned off, an invalid template configuration can be stored. Default: true

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            # cloud_formation_template: servicecatalog.CloudFormationTemplate
            
            cloud_formation_product_version = servicecatalog.CloudFormationProductVersion(
                cloud_formation_template=cloud_formation_template,
            
                # the properties below are optional
                description="description",
                product_version_name="productVersionName",
                validate_template=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudFormationProductVersion.__init__)
            check_type(argname="argument cloud_formation_template", value=cloud_formation_template, expected_type=type_hints["cloud_formation_template"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument product_version_name", value=product_version_name, expected_type=type_hints["product_version_name"])
            check_type(argname="argument validate_template", value=validate_template, expected_type=type_hints["validate_template"])
        self._values: typing.Dict[str, typing.Any] = {
            "cloud_formation_template": cloud_formation_template,
        }
        if description is not None:
            self._values["description"] = description
        if product_version_name is not None:
            self._values["product_version_name"] = product_version_name
        if validate_template is not None:
            self._values["validate_template"] = validate_template

    @builtins.property
    def cloud_formation_template(self) -> "CloudFormationTemplate":
        '''The S3 template that points to the provisioning version template.'''
        result = self._values.get("cloud_formation_template")
        assert result is not None, "Required property 'cloud_formation_template' is missing"
        return typing.cast("CloudFormationTemplate", result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the product version.

        :default: - No description provided
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def product_version_name(self) -> typing.Optional[builtins.str]:
        '''The name of the product version.

        :default: - No product version name provided
        '''
        result = self._values.get("product_version_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validate_template(self) -> typing.Optional[builtins.bool]:
        '''Whether the specified product template will be validated by CloudFormation.

        If turned off, an invalid template configuration can be stored.

        :default: true
        '''
        result = self._values.get("validate_template")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFormationProductVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudFormationTemplate(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CloudFormationTemplate",
):
    '''Represents the Product Provisioning Artifact Template.

    :exampleMetadata: infused

    Example::

        import path as path
        
        
        product = servicecatalog.CloudFormationProduct(self, "Product",
            product_name="My Product",
            owner="Product Owner",
            product_versions=[servicecatalog.CloudFormationProductVersion(
                product_version_name="v1",
                cloud_formation_template=servicecatalog.CloudFormationTemplate.from_url("https://raw.githubusercontent.com/awslabs/aws-cloudformation-templates/master/aws/services/ServiceCatalog/Product.yaml")
            ), servicecatalog.CloudFormationProductVersion(
                product_version_name="v2",
                cloud_formation_template=servicecatalog.CloudFormationTemplate.from_asset(path.join(__dirname, "development-environment.template.json"))
            )
            ]
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromAsset")
    @builtins.classmethod
    def from_asset(
        cls,
        path: builtins.str,
        *,
        readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
        bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
        ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
    ) -> "CloudFormationTemplate":
        '''Loads the provisioning artifacts template from a local disk path.

        :param path: A file containing the provisioning artifacts.
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudFormationTemplate.from_asset)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        options = _AssetOptions_2aa69621(
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        return typing.cast("CloudFormationTemplate", jsii.sinvoke(cls, "fromAsset", [path, options]))

    @jsii.member(jsii_name="fromProductStack")
    @builtins.classmethod
    def from_product_stack(
        cls,
        product_stack: "ProductStack",
    ) -> "CloudFormationTemplate":
        '''Creates a product with the resources defined in the given product stack.

        :param product_stack: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudFormationTemplate.from_product_stack)
            check_type(argname="argument product_stack", value=product_stack, expected_type=type_hints["product_stack"])
        return typing.cast("CloudFormationTemplate", jsii.sinvoke(cls, "fromProductStack", [product_stack]))

    @jsii.member(jsii_name="fromUrl")
    @builtins.classmethod
    def from_url(cls, url: builtins.str) -> "CloudFormationTemplate":
        '''Template from URL.

        :param url: The url that points to the provisioning artifacts template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudFormationTemplate.from_url)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        return typing.cast("CloudFormationTemplate", jsii.sinvoke(cls, "fromUrl", [url]))

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, scope: constructs.Construct) -> "CloudFormationTemplateConfig":
        '''Called when the product is initialized to allow this object to bind to the stack, add resources and have fun.

        :param scope: The binding scope. Don't be smart about trying to down-cast or assume it's initialized. You may just use it as a construct scope.
        '''
        ...


class _CloudFormationTemplateProxy(CloudFormationTemplate):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: constructs.Construct) -> "CloudFormationTemplateConfig":
        '''Called when the product is initialized to allow this object to bind to the stack, add resources and have fun.

        :param scope: The binding scope. Don't be smart about trying to down-cast or assume it's initialized. You may just use it as a construct scope.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudFormationTemplate.bind)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast("CloudFormationTemplateConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, CloudFormationTemplate).__jsii_proxy_class__ = lambda : _CloudFormationTemplateProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CloudFormationTemplateConfig",
    jsii_struct_bases=[],
    name_mapping={"http_url": "httpUrl"},
)
class CloudFormationTemplateConfig:
    def __init__(self, *, http_url: builtins.str) -> None:
        '''Result of binding ``Template`` into a ``Product``.

        :param http_url: The http url of the template in S3.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            cloud_formation_template_config = servicecatalog.CloudFormationTemplateConfig(
                http_url="httpUrl"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudFormationTemplateConfig.__init__)
            check_type(argname="argument http_url", value=http_url, expected_type=type_hints["http_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "http_url": http_url,
        }

    @builtins.property
    def http_url(self) -> builtins.str:
        '''The http url of the template in S3.'''
        result = self._values.get("http_url")
        assert result is not None, "Required property 'http_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFormationTemplateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CommonConstraintOptions",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "message_language": "messageLanguage"},
)
class CommonConstraintOptions:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
    ) -> None:
        '''Properties for governance mechanisms and constraints.

        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_sns as sns
            
            # portfolio: servicecatalog.Portfolio
            # product: servicecatalog.CloudFormationProduct
            
            
            topic1 = sns.Topic(self, "Topic1")
            portfolio.notify_on_stack_events(product, topic1)
            
            topic2 = sns.Topic(self, "Topic2")
            portfolio.notify_on_stack_events(product, topic2,
                description="description for topic2"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CommonConstraintOptions.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument message_language", value=message_language, expected_type=type_hints["message_language"])
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if message_language is not None:
            self._values["message_language"] = message_language

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the constraint.

        :default: - No description provided
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message_language(self) -> typing.Optional["MessageLanguage"]:
        '''The language code.

        Configures the language for error messages from service catalog.

        :default: - English
        '''
        result = self._values.get("message_language")
        return typing.cast(typing.Optional["MessageLanguage"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonConstraintOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_servicecatalog.IPortfolio")
class IPortfolio(_IResource_c80c4260, typing_extensions.Protocol):
    '''A Service Catalog portfolio.'''

    @builtins.property
    @jsii.member(jsii_name="portfolioArn")
    def portfolio_arn(self) -> builtins.str:
        '''The ARN of the portfolio.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        '''The ID of the portfolio.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addProduct")
    def add_product(self, product: "IProduct") -> None:
        '''Associate portfolio with the given product.

        :param product: A service catalog produt.
        '''
        ...

    @jsii.member(jsii_name="associateTagOptions")
    def associate_tag_options(self, tag_options: "TagOptions") -> None:
        '''Associate Tag Options.

        A TagOption is a key-value pair managed in AWS Service Catalog.
        It is not an AWS tag, but serves as a template for creating an AWS tag based on the TagOption.

        :param tag_options: -
        '''
        ...

    @jsii.member(jsii_name="constrainCloudFormationParameters")
    def constrain_cloud_formation_parameters(
        self,
        product: "IProduct",
        *,
        rule: typing.Union["TemplateRule", typing.Dict[str, typing.Any]],
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
    ) -> None:
        '''Set provisioning rules for the product.

        :param product: A service catalog product.
        :param rule: The rule with condition and assertions to apply to template.
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        ...

    @jsii.member(jsii_name="constrainTagUpdates")
    def constrain_tag_updates(
        self,
        product: "IProduct",
        *,
        allow: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
    ) -> None:
        '''Add a Resource Update Constraint.

        :param product: -
        :param allow: Toggle for if users should be allowed to change/update tags on provisioned products. Default: true
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        ...

    @jsii.member(jsii_name="deployWithStackSets")
    def deploy_with_stack_sets(
        self,
        product: "IProduct",
        *,
        accounts: typing.Sequence[builtins.str],
        admin_role: _IRole_235f5d8e,
        execution_role_name: builtins.str,
        regions: typing.Sequence[builtins.str],
        allow_stack_set_instance_operations: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
    ) -> None:
        '''Configure deployment options using AWS Cloudformation StackSets.

        :param product: A service catalog product.
        :param accounts: List of accounts to deploy stacks to.
        :param admin_role: IAM role used to administer the StackSets configuration.
        :param execution_role_name: IAM role used to provision the products in the Stacks.
        :param regions: List of regions to deploy stacks to.
        :param allow_stack_set_instance_operations: Wether to allow end users to create, update, and delete stacks. Default: false
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        ...

    @jsii.member(jsii_name="giveAccessToGroup")
    def give_access_to_group(self, group: _IGroup_96daf542) -> None:
        '''Associate portfolio with an IAM Group.

        :param group: an IAM Group.
        '''
        ...

    @jsii.member(jsii_name="giveAccessToRole")
    def give_access_to_role(self, role: _IRole_235f5d8e) -> None:
        '''Associate portfolio with an IAM Role.

        :param role: an IAM role.
        '''
        ...

    @jsii.member(jsii_name="giveAccessToUser")
    def give_access_to_user(self, user: _IUser_c32311f7) -> None:
        '''Associate portfolio with an IAM User.

        :param user: an IAM user.
        '''
        ...

    @jsii.member(jsii_name="notifyOnStackEvents")
    def notify_on_stack_events(
        self,
        product: "IProduct",
        topic: _ITopic_9eca4852,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
    ) -> None:
        '''Add notifications for supplied topics on the provisioned product.

        :param product: A service catalog product.
        :param topic: A SNS Topic to receive notifications on events related to the provisioned product.
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        ...

    @jsii.member(jsii_name="setLaunchRole")
    def set_launch_role(
        self,
        product: "IProduct",
        launch_role: _IRole_235f5d8e,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
    ) -> None:
        '''Force users to assume a certain role when launching a product.

        This sets the launch role using the role arn which is tied to the account this role exists in.
        This is useful if you will be provisioning products from the account where this role exists.
        If you intend to share the portfolio across accounts, use a local launch role.

        :param product: A service catalog product.
        :param launch_role: The IAM role a user must assume when provisioning the product.
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        ...

    @jsii.member(jsii_name="setLocalLaunchRole")
    def set_local_launch_role(
        self,
        product: "IProduct",
        launch_role: _IRole_235f5d8e,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
    ) -> None:
        '''Force users to assume a certain role when launching a product.

        The role name will be referenced by in the local account and must be set explicitly.
        This is useful when sharing the portfolio with multiple accounts.

        :param product: A service catalog product.
        :param launch_role: The IAM role a user must assume when provisioning the product. A role with this name must exist in the account where the portolio is created and the accounts it is shared with. The role name must be set explicitly.
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        ...

    @jsii.member(jsii_name="setLocalLaunchRoleName")
    def set_local_launch_role_name(
        self,
        product: "IProduct",
        launch_role_name: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
    ) -> _IRole_235f5d8e:
        '''Force users to assume a certain role when launching a product.

        The role will be referenced by name in the local account instead of a static role arn.
        A role with this name will automatically be created and assumable by Service Catalog in this account.
        This is useful when sharing the portfolio with multiple accounts.

        :param product: A service catalog product.
        :param launch_role_name: The name of the IAM role a user must assume when provisioning the product. A role with this name must exist in the account where the portolio is created and the accounts it is shared with.
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        ...

    @jsii.member(jsii_name="shareWithAccount")
    def share_with_account(
        self,
        account_id: builtins.str,
        *,
        message_language: typing.Optional["MessageLanguage"] = None,
        share_tag_options: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Initiate a portfolio share with another account.

        :param account_id: AWS account to share portfolio with.
        :param message_language: The message language of the share. Controls status and error message language for share. Default: - English
        :param share_tag_options: Whether to share tagOptions as a part of the portfolio share. Default: - share not specified
        '''
        ...


class _IPortfolioProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A Service Catalog portfolio.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_servicecatalog.IPortfolio"

    @builtins.property
    @jsii.member(jsii_name="portfolioArn")
    def portfolio_arn(self) -> builtins.str:
        '''The ARN of the portfolio.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "portfolioArn"))

    @builtins.property
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        '''The ID of the portfolio.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "portfolioId"))

    @jsii.member(jsii_name="addProduct")
    def add_product(self, product: "IProduct") -> None:
        '''Associate portfolio with the given product.

        :param product: A service catalog produt.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IPortfolio.add_product)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
        return typing.cast(None, jsii.invoke(self, "addProduct", [product]))

    @jsii.member(jsii_name="associateTagOptions")
    def associate_tag_options(self, tag_options: "TagOptions") -> None:
        '''Associate Tag Options.

        A TagOption is a key-value pair managed in AWS Service Catalog.
        It is not an AWS tag, but serves as a template for creating an AWS tag based on the TagOption.

        :param tag_options: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IPortfolio.associate_tag_options)
            check_type(argname="argument tag_options", value=tag_options, expected_type=type_hints["tag_options"])
        return typing.cast(None, jsii.invoke(self, "associateTagOptions", [tag_options]))

    @jsii.member(jsii_name="constrainCloudFormationParameters")
    def constrain_cloud_formation_parameters(
        self,
        product: "IProduct",
        *,
        rule: typing.Union["TemplateRule", typing.Dict[str, typing.Any]],
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
    ) -> None:
        '''Set provisioning rules for the product.

        :param product: A service catalog product.
        :param rule: The rule with condition and assertions to apply to template.
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IPortfolio.constrain_cloud_formation_parameters)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
        options = CloudFormationRuleConstraintOptions(
            rule=rule, description=description, message_language=message_language
        )

        return typing.cast(None, jsii.invoke(self, "constrainCloudFormationParameters", [product, options]))

    @jsii.member(jsii_name="constrainTagUpdates")
    def constrain_tag_updates(
        self,
        product: "IProduct",
        *,
        allow: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
    ) -> None:
        '''Add a Resource Update Constraint.

        :param product: -
        :param allow: Toggle for if users should be allowed to change/update tags on provisioned products. Default: true
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IPortfolio.constrain_tag_updates)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
        options = TagUpdateConstraintOptions(
            allow=allow, description=description, message_language=message_language
        )

        return typing.cast(None, jsii.invoke(self, "constrainTagUpdates", [product, options]))

    @jsii.member(jsii_name="deployWithStackSets")
    def deploy_with_stack_sets(
        self,
        product: "IProduct",
        *,
        accounts: typing.Sequence[builtins.str],
        admin_role: _IRole_235f5d8e,
        execution_role_name: builtins.str,
        regions: typing.Sequence[builtins.str],
        allow_stack_set_instance_operations: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
    ) -> None:
        '''Configure deployment options using AWS Cloudformation StackSets.

        :param product: A service catalog product.
        :param accounts: List of accounts to deploy stacks to.
        :param admin_role: IAM role used to administer the StackSets configuration.
        :param execution_role_name: IAM role used to provision the products in the Stacks.
        :param regions: List of regions to deploy stacks to.
        :param allow_stack_set_instance_operations: Wether to allow end users to create, update, and delete stacks. Default: false
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IPortfolio.deploy_with_stack_sets)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
        options = StackSetsConstraintOptions(
            accounts=accounts,
            admin_role=admin_role,
            execution_role_name=execution_role_name,
            regions=regions,
            allow_stack_set_instance_operations=allow_stack_set_instance_operations,
            description=description,
            message_language=message_language,
        )

        return typing.cast(None, jsii.invoke(self, "deployWithStackSets", [product, options]))

    @jsii.member(jsii_name="giveAccessToGroup")
    def give_access_to_group(self, group: _IGroup_96daf542) -> None:
        '''Associate portfolio with an IAM Group.

        :param group: an IAM Group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IPortfolio.give_access_to_group)
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
        return typing.cast(None, jsii.invoke(self, "giveAccessToGroup", [group]))

    @jsii.member(jsii_name="giveAccessToRole")
    def give_access_to_role(self, role: _IRole_235f5d8e) -> None:
        '''Associate portfolio with an IAM Role.

        :param role: an IAM role.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IPortfolio.give_access_to_role)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "giveAccessToRole", [role]))

    @jsii.member(jsii_name="giveAccessToUser")
    def give_access_to_user(self, user: _IUser_c32311f7) -> None:
        '''Associate portfolio with an IAM User.

        :param user: an IAM user.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IPortfolio.give_access_to_user)
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        return typing.cast(None, jsii.invoke(self, "giveAccessToUser", [user]))

    @jsii.member(jsii_name="notifyOnStackEvents")
    def notify_on_stack_events(
        self,
        product: "IProduct",
        topic: _ITopic_9eca4852,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
    ) -> None:
        '''Add notifications for supplied topics on the provisioned product.

        :param product: A service catalog product.
        :param topic: A SNS Topic to receive notifications on events related to the provisioned product.
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IPortfolio.notify_on_stack_events)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        options = CommonConstraintOptions(
            description=description, message_language=message_language
        )

        return typing.cast(None, jsii.invoke(self, "notifyOnStackEvents", [product, topic, options]))

    @jsii.member(jsii_name="setLaunchRole")
    def set_launch_role(
        self,
        product: "IProduct",
        launch_role: _IRole_235f5d8e,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
    ) -> None:
        '''Force users to assume a certain role when launching a product.

        This sets the launch role using the role arn which is tied to the account this role exists in.
        This is useful if you will be provisioning products from the account where this role exists.
        If you intend to share the portfolio across accounts, use a local launch role.

        :param product: A service catalog product.
        :param launch_role: The IAM role a user must assume when provisioning the product.
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IPortfolio.set_launch_role)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument launch_role", value=launch_role, expected_type=type_hints["launch_role"])
        options = CommonConstraintOptions(
            description=description, message_language=message_language
        )

        return typing.cast(None, jsii.invoke(self, "setLaunchRole", [product, launch_role, options]))

    @jsii.member(jsii_name="setLocalLaunchRole")
    def set_local_launch_role(
        self,
        product: "IProduct",
        launch_role: _IRole_235f5d8e,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
    ) -> None:
        '''Force users to assume a certain role when launching a product.

        The role name will be referenced by in the local account and must be set explicitly.
        This is useful when sharing the portfolio with multiple accounts.

        :param product: A service catalog product.
        :param launch_role: The IAM role a user must assume when provisioning the product. A role with this name must exist in the account where the portolio is created and the accounts it is shared with. The role name must be set explicitly.
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IPortfolio.set_local_launch_role)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument launch_role", value=launch_role, expected_type=type_hints["launch_role"])
        options = CommonConstraintOptions(
            description=description, message_language=message_language
        )

        return typing.cast(None, jsii.invoke(self, "setLocalLaunchRole", [product, launch_role, options]))

    @jsii.member(jsii_name="setLocalLaunchRoleName")
    def set_local_launch_role_name(
        self,
        product: "IProduct",
        launch_role_name: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional["MessageLanguage"] = None,
    ) -> _IRole_235f5d8e:
        '''Force users to assume a certain role when launching a product.

        The role will be referenced by name in the local account instead of a static role arn.
        A role with this name will automatically be created and assumable by Service Catalog in this account.
        This is useful when sharing the portfolio with multiple accounts.

        :param product: A service catalog product.
        :param launch_role_name: The name of the IAM role a user must assume when provisioning the product. A role with this name must exist in the account where the portolio is created and the accounts it is shared with.
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IPortfolio.set_local_launch_role_name)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument launch_role_name", value=launch_role_name, expected_type=type_hints["launch_role_name"])
        options = CommonConstraintOptions(
            description=description, message_language=message_language
        )

        return typing.cast(_IRole_235f5d8e, jsii.invoke(self, "setLocalLaunchRoleName", [product, launch_role_name, options]))

    @jsii.member(jsii_name="shareWithAccount")
    def share_with_account(
        self,
        account_id: builtins.str,
        *,
        message_language: typing.Optional["MessageLanguage"] = None,
        share_tag_options: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Initiate a portfolio share with another account.

        :param account_id: AWS account to share portfolio with.
        :param message_language: The message language of the share. Controls status and error message language for share. Default: - English
        :param share_tag_options: Whether to share tagOptions as a part of the portfolio share. Default: - share not specified
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IPortfolio.share_with_account)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        options = PortfolioShareOptions(
            message_language=message_language, share_tag_options=share_tag_options
        )

        return typing.cast(None, jsii.invoke(self, "shareWithAccount", [account_id, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPortfolio).__jsii_proxy_class__ = lambda : _IPortfolioProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_servicecatalog.IProduct")
class IProduct(_IResource_c80c4260, typing_extensions.Protocol):
    '''A Service Catalog product, currently only supports type CloudFormationProduct.'''

    @builtins.property
    @jsii.member(jsii_name="productArn")
    def product_arn(self) -> builtins.str:
        '''The ARN of the product.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        '''The id of the product.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="associateTagOptions")
    def associate_tag_options(self, tag_options: "TagOptions") -> None:
        '''Associate Tag Options.

        A TagOption is a key-value pair managed in AWS Service Catalog.
        It is not an AWS tag, but serves as a template for creating an AWS tag based on the TagOption.

        :param tag_options: -
        '''
        ...


class _IProductProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A Service Catalog product, currently only supports type CloudFormationProduct.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_servicecatalog.IProduct"

    @builtins.property
    @jsii.member(jsii_name="productArn")
    def product_arn(self) -> builtins.str:
        '''The ARN of the product.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "productArn"))

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        '''The id of the product.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "productId"))

    @jsii.member(jsii_name="associateTagOptions")
    def associate_tag_options(self, tag_options: "TagOptions") -> None:
        '''Associate Tag Options.

        A TagOption is a key-value pair managed in AWS Service Catalog.
        It is not an AWS tag, but serves as a template for creating an AWS tag based on the TagOption.

        :param tag_options: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IProduct.associate_tag_options)
            check_type(argname="argument tag_options", value=tag_options, expected_type=type_hints["tag_options"])
        return typing.cast(None, jsii.invoke(self, "associateTagOptions", [tag_options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProduct).__jsii_proxy_class__ = lambda : _IProductProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_servicecatalog.MessageLanguage")
class MessageLanguage(enum.Enum):
    '''The language code.

    Used for error and logging messages for end users.
    The default behavior if not specified is English.

    :exampleMetadata: infused

    Example::

        servicecatalog.Portfolio(self, "Portfolio",
            display_name="MyFirstPortfolio",
            provider_name="SCAdmin",
            description="Portfolio for a project",
            message_language=servicecatalog.MessageLanguage.EN
        )
    '''

    EN = "EN"
    '''English.'''
    JP = "JP"
    '''Japanese.'''
    ZH = "ZH"
    '''Chinese.'''


@jsii.implements(IPortfolio)
class Portfolio(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.Portfolio",
):
    '''A Service Catalog portfolio.

    :exampleMetadata: infused

    Example::

        servicecatalog.Portfolio(self, "Portfolio",
            display_name="MyPortfolio",
            provider_name="MyTeam"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        display_name: builtins.str,
        provider_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional[MessageLanguage] = None,
        tag_options: typing.Optional["TagOptions"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param display_name: The name of the portfolio.
        :param provider_name: The provider name.
        :param description: Description for portfolio. Default: - No description provided
        :param message_language: The message language. Controls language for status logging and errors. Default: - English
        :param tag_options: TagOptions associated directly to a portfolio. Default: - No tagOptions provided
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PortfolioProps(
            display_name=display_name,
            provider_name=provider_name,
            description=description,
            message_language=message_language,
            tag_options=tag_options,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromPortfolioArn")
    @builtins.classmethod
    def from_portfolio_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        portfolio_arn: builtins.str,
    ) -> IPortfolio:
        '''Creates a Portfolio construct that represents an external portfolio.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param portfolio_arn: the Amazon Resource Name of the existing portfolio.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio.from_portfolio_arn)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument portfolio_arn", value=portfolio_arn, expected_type=type_hints["portfolio_arn"])
        return typing.cast(IPortfolio, jsii.sinvoke(cls, "fromPortfolioArn", [scope, id, portfolio_arn]))

    @jsii.member(jsii_name="addProduct")
    def add_product(self, product: IProduct) -> None:
        '''Associate portfolio with the given product.

        :param product: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio.add_product)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
        return typing.cast(None, jsii.invoke(self, "addProduct", [product]))

    @jsii.member(jsii_name="associateTagOptions")
    def associate_tag_options(self, tag_options: "TagOptions") -> None:
        '''Associate Tag Options.

        A TagOption is a key-value pair managed in AWS Service Catalog.
        It is not an AWS tag, but serves as a template for creating an AWS tag based on the TagOption.

        :param tag_options: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio.associate_tag_options)
            check_type(argname="argument tag_options", value=tag_options, expected_type=type_hints["tag_options"])
        return typing.cast(None, jsii.invoke(self, "associateTagOptions", [tag_options]))

    @jsii.member(jsii_name="constrainCloudFormationParameters")
    def constrain_cloud_formation_parameters(
        self,
        product: IProduct,
        *,
        rule: typing.Union["TemplateRule", typing.Dict[str, typing.Any]],
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional[MessageLanguage] = None,
    ) -> None:
        '''Set provisioning rules for the product.

        :param product: -
        :param rule: The rule with condition and assertions to apply to template.
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio.constrain_cloud_formation_parameters)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
        options = CloudFormationRuleConstraintOptions(
            rule=rule, description=description, message_language=message_language
        )

        return typing.cast(None, jsii.invoke(self, "constrainCloudFormationParameters", [product, options]))

    @jsii.member(jsii_name="constrainTagUpdates")
    def constrain_tag_updates(
        self,
        product: IProduct,
        *,
        allow: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional[MessageLanguage] = None,
    ) -> None:
        '''Add a Resource Update Constraint.

        :param product: -
        :param allow: Toggle for if users should be allowed to change/update tags on provisioned products. Default: true
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio.constrain_tag_updates)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
        options = TagUpdateConstraintOptions(
            allow=allow, description=description, message_language=message_language
        )

        return typing.cast(None, jsii.invoke(self, "constrainTagUpdates", [product, options]))

    @jsii.member(jsii_name="deployWithStackSets")
    def deploy_with_stack_sets(
        self,
        product: IProduct,
        *,
        accounts: typing.Sequence[builtins.str],
        admin_role: _IRole_235f5d8e,
        execution_role_name: builtins.str,
        regions: typing.Sequence[builtins.str],
        allow_stack_set_instance_operations: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional[MessageLanguage] = None,
    ) -> None:
        '''Configure deployment options using AWS Cloudformation StackSets.

        :param product: -
        :param accounts: List of accounts to deploy stacks to.
        :param admin_role: IAM role used to administer the StackSets configuration.
        :param execution_role_name: IAM role used to provision the products in the Stacks.
        :param regions: List of regions to deploy stacks to.
        :param allow_stack_set_instance_operations: Wether to allow end users to create, update, and delete stacks. Default: false
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio.deploy_with_stack_sets)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
        options = StackSetsConstraintOptions(
            accounts=accounts,
            admin_role=admin_role,
            execution_role_name=execution_role_name,
            regions=regions,
            allow_stack_set_instance_operations=allow_stack_set_instance_operations,
            description=description,
            message_language=message_language,
        )

        return typing.cast(None, jsii.invoke(self, "deployWithStackSets", [product, options]))

    @jsii.member(jsii_name="generateUniqueHash")
    def _generate_unique_hash(self, value: builtins.str) -> builtins.str:
        '''Create a unique id based off the L1 CfnPortfolio or the arn of an imported portfolio.

        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio._generate_unique_hash)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(builtins.str, jsii.invoke(self, "generateUniqueHash", [value]))

    @jsii.member(jsii_name="giveAccessToGroup")
    def give_access_to_group(self, group: _IGroup_96daf542) -> None:
        '''Associate portfolio with an IAM Group.

        :param group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio.give_access_to_group)
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
        return typing.cast(None, jsii.invoke(self, "giveAccessToGroup", [group]))

    @jsii.member(jsii_name="giveAccessToRole")
    def give_access_to_role(self, role: _IRole_235f5d8e) -> None:
        '''Associate portfolio with an IAM Role.

        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio.give_access_to_role)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "giveAccessToRole", [role]))

    @jsii.member(jsii_name="giveAccessToUser")
    def give_access_to_user(self, user: _IUser_c32311f7) -> None:
        '''Associate portfolio with an IAM User.

        :param user: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio.give_access_to_user)
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        return typing.cast(None, jsii.invoke(self, "giveAccessToUser", [user]))

    @jsii.member(jsii_name="notifyOnStackEvents")
    def notify_on_stack_events(
        self,
        product: IProduct,
        topic: _ITopic_9eca4852,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional[MessageLanguage] = None,
    ) -> None:
        '''Add notifications for supplied topics on the provisioned product.

        :param product: -
        :param topic: -
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio.notify_on_stack_events)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        options = CommonConstraintOptions(
            description=description, message_language=message_language
        )

        return typing.cast(None, jsii.invoke(self, "notifyOnStackEvents", [product, topic, options]))

    @jsii.member(jsii_name="setLaunchRole")
    def set_launch_role(
        self,
        product: IProduct,
        launch_role: _IRole_235f5d8e,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional[MessageLanguage] = None,
    ) -> None:
        '''Force users to assume a certain role when launching a product.

        This sets the launch role using the role arn which is tied to the account this role exists in.
        This is useful if you will be provisioning products from the account where this role exists.
        If you intend to share the portfolio across accounts, use a local launch role.

        :param product: -
        :param launch_role: -
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio.set_launch_role)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument launch_role", value=launch_role, expected_type=type_hints["launch_role"])
        options = CommonConstraintOptions(
            description=description, message_language=message_language
        )

        return typing.cast(None, jsii.invoke(self, "setLaunchRole", [product, launch_role, options]))

    @jsii.member(jsii_name="setLocalLaunchRole")
    def set_local_launch_role(
        self,
        product: IProduct,
        launch_role: _IRole_235f5d8e,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional[MessageLanguage] = None,
    ) -> None:
        '''Force users to assume a certain role when launching a product.

        The role name will be referenced by in the local account and must be set explicitly.
        This is useful when sharing the portfolio with multiple accounts.

        :param product: -
        :param launch_role: -
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio.set_local_launch_role)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument launch_role", value=launch_role, expected_type=type_hints["launch_role"])
        options = CommonConstraintOptions(
            description=description, message_language=message_language
        )

        return typing.cast(None, jsii.invoke(self, "setLocalLaunchRole", [product, launch_role, options]))

    @jsii.member(jsii_name="setLocalLaunchRoleName")
    def set_local_launch_role_name(
        self,
        product: IProduct,
        launch_role_name: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional[MessageLanguage] = None,
    ) -> _IRole_235f5d8e:
        '''Force users to assume a certain role when launching a product.

        The role will be referenced by name in the local account instead of a static role arn.
        A role with this name will automatically be created and assumable by Service Catalog in this account.
        This is useful when sharing the portfolio with multiple accounts.

        :param product: -
        :param launch_role_name: -
        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio.set_local_launch_role_name)
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument launch_role_name", value=launch_role_name, expected_type=type_hints["launch_role_name"])
        options = CommonConstraintOptions(
            description=description, message_language=message_language
        )

        return typing.cast(_IRole_235f5d8e, jsii.invoke(self, "setLocalLaunchRoleName", [product, launch_role_name, options]))

    @jsii.member(jsii_name="shareWithAccount")
    def share_with_account(
        self,
        account_id: builtins.str,
        *,
        message_language: typing.Optional[MessageLanguage] = None,
        share_tag_options: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Initiate a portfolio share with another account.

        :param account_id: -
        :param message_language: The message language of the share. Controls status and error message language for share. Default: - English
        :param share_tag_options: Whether to share tagOptions as a part of the portfolio share. Default: - share not specified
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Portfolio.share_with_account)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        options = PortfolioShareOptions(
            message_language=message_language, share_tag_options=share_tag_options
        )

        return typing.cast(None, jsii.invoke(self, "shareWithAccount", [account_id, options]))

    @builtins.property
    @jsii.member(jsii_name="portfolioArn")
    def portfolio_arn(self) -> builtins.str:
        '''The ARN of the portfolio.'''
        return typing.cast(builtins.str, jsii.get(self, "portfolioArn"))

    @builtins.property
    @jsii.member(jsii_name="portfolioId")
    def portfolio_id(self) -> builtins.str:
        '''The ID of the portfolio.'''
        return typing.cast(builtins.str, jsii.get(self, "portfolioId"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.PortfolioProps",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "provider_name": "providerName",
        "description": "description",
        "message_language": "messageLanguage",
        "tag_options": "tagOptions",
    },
)
class PortfolioProps:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        provider_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional[MessageLanguage] = None,
        tag_options: typing.Optional["TagOptions"] = None,
    ) -> None:
        '''Properties for a Portfolio.

        :param display_name: The name of the portfolio.
        :param provider_name: The provider name.
        :param description: Description for portfolio. Default: - No description provided
        :param message_language: The message language. Controls language for status logging and errors. Default: - English
        :param tag_options: TagOptions associated directly to a portfolio. Default: - No tagOptions provided

        :exampleMetadata: infused

        Example::

            servicecatalog.Portfolio(self, "Portfolio",
                display_name="MyPortfolio",
                provider_name="MyTeam"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PortfolioProps.__init__)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument message_language", value=message_language, expected_type=type_hints["message_language"])
            check_type(argname="argument tag_options", value=tag_options, expected_type=type_hints["tag_options"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
            "provider_name": provider_name,
        }
        if description is not None:
            self._values["description"] = description
        if message_language is not None:
            self._values["message_language"] = message_language
        if tag_options is not None:
            self._values["tag_options"] = tag_options

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the portfolio.'''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def provider_name(self) -> builtins.str:
        '''The provider name.'''
        result = self._values.get("provider_name")
        assert result is not None, "Required property 'provider_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description for portfolio.

        :default: - No description provided
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message_language(self) -> typing.Optional[MessageLanguage]:
        '''The message language.

        Controls language for
        status logging and errors.

        :default: - English
        '''
        result = self._values.get("message_language")
        return typing.cast(typing.Optional[MessageLanguage], result)

    @builtins.property
    def tag_options(self) -> typing.Optional["TagOptions"]:
        '''TagOptions associated directly to a portfolio.

        :default: - No tagOptions provided
        '''
        result = self._values.get("tag_options")
        return typing.cast(typing.Optional["TagOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PortfolioProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.PortfolioShareOptions",
    jsii_struct_bases=[],
    name_mapping={
        "message_language": "messageLanguage",
        "share_tag_options": "shareTagOptions",
    },
)
class PortfolioShareOptions:
    def __init__(
        self,
        *,
        message_language: typing.Optional[MessageLanguage] = None,
        share_tag_options: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for portfolio share.

        :param message_language: The message language of the share. Controls status and error message language for share. Default: - English
        :param share_tag_options: Whether to share tagOptions as a part of the portfolio share. Default: - share not specified

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            portfolio_share_options = servicecatalog.PortfolioShareOptions(
                message_language=servicecatalog.MessageLanguage.EN,
                share_tag_options=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PortfolioShareOptions.__init__)
            check_type(argname="argument message_language", value=message_language, expected_type=type_hints["message_language"])
            check_type(argname="argument share_tag_options", value=share_tag_options, expected_type=type_hints["share_tag_options"])
        self._values: typing.Dict[str, typing.Any] = {}
        if message_language is not None:
            self._values["message_language"] = message_language
        if share_tag_options is not None:
            self._values["share_tag_options"] = share_tag_options

    @builtins.property
    def message_language(self) -> typing.Optional[MessageLanguage]:
        '''The message language of the share.

        Controls status and error message language for share.

        :default: - English
        '''
        result = self._values.get("message_language")
        return typing.cast(typing.Optional[MessageLanguage], result)

    @builtins.property
    def share_tag_options(self) -> typing.Optional[builtins.bool]:
        '''Whether to share tagOptions as a part of the portfolio share.

        :default: - share not specified
        '''
        result = self._values.get("share_tag_options")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PortfolioShareOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IProduct)
class Product(
    _Resource_45bc6135,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_servicecatalog.Product",
):
    '''Abstract class for Service Catalog Product.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_servicecatalog as servicecatalog
        
        product = servicecatalog.Product.from_product_arn(self, "MyProduct", "productArn")
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Product.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = _ResourceProps_15a65b4e(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromProductArn")
    @builtins.classmethod
    def from_product_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        product_arn: builtins.str,
    ) -> IProduct:
        '''Creates a Product construct that represents an external product.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param product_arn: Product Arn.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Product.from_product_arn)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument product_arn", value=product_arn, expected_type=type_hints["product_arn"])
        return typing.cast(IProduct, jsii.sinvoke(cls, "fromProductArn", [scope, id, product_arn]))

    @jsii.member(jsii_name="associateTagOptions")
    def associate_tag_options(self, tag_options: "TagOptions") -> None:
        '''Associate Tag Options.

        A TagOption is a key-value pair managed in AWS Service Catalog.
        It is not an AWS tag, but serves as a template for creating an AWS tag based on the TagOption.

        :param tag_options: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Product.associate_tag_options)
            check_type(argname="argument tag_options", value=tag_options, expected_type=type_hints["tag_options"])
        return typing.cast(None, jsii.invoke(self, "associateTagOptions", [tag_options]))

    @builtins.property
    @jsii.member(jsii_name="productArn")
    @abc.abstractmethod
    def product_arn(self) -> builtins.str:
        '''The ARN of the product.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="productId")
    @abc.abstractmethod
    def product_id(self) -> builtins.str:
        '''The id of the product.'''
        ...


class _ProductProxy(
    Product,
    jsii.proxy_for(_Resource_45bc6135), # type: ignore[misc]
):
    @builtins.property
    @jsii.member(jsii_name="productArn")
    def product_arn(self) -> builtins.str:
        '''The ARN of the product.'''
        return typing.cast(builtins.str, jsii.get(self, "productArn"))

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        '''The id of the product.'''
        return typing.cast(builtins.str, jsii.get(self, "productId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Product).__jsii_proxy_class__ = lambda : _ProductProxy


class ProductStack(
    _Stack_2866e57f,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.ProductStack",
):
    '''A Service Catalog product stack, which is similar in form to a Cloudformation nested stack.

    You can add the resources to this stack that you want to define for your service catalog product.

    This stack will not be treated as an independent deployment
    artifact (won't be listed in "cdk list" or deployable through "cdk deploy"),
    but rather only synthesized as a template and uploaded as an asset to S3.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_s3 as s3
        import aws_cdk as cdk
        
        
        class S3BucketProduct(servicecatalog.ProductStack):
            def __init__(self, scope, id):
                super().__init__(scope, id)
        
                s3.Bucket(self, "BucketProduct")
        
        product = servicecatalog.CloudFormationProduct(self, "Product",
            product_name="My Product",
            owner="Product Owner",
            product_versions=[servicecatalog.CloudFormationProductVersion(
                product_version_name="v1",
                cloud_formation_template=servicecatalog.CloudFormationTemplate.from_product_stack(S3BucketProduct(self, "S3BucketProduct"))
            )
            ]
        )
    '''

    def __init__(self, scope: constructs.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ProductStack.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])

    @builtins.property
    @jsii.member(jsii_name="templateFile")
    def template_file(self) -> builtins.str:
        '''The name of the CloudFormation template file emitted to the output directory during synthesis.

        Example value: ``MyStack.template.json``
        '''
        return typing.cast(builtins.str, jsii.get(self, "templateFile"))


class ProductStackHistory(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.ProductStackHistory",
):
    '''A Construct that contains a Service Catalog product stack with its previous deployments maintained.

    :exampleMetadata: infused

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        import aws_cdk.aws_s3 as s3
        import aws_cdk as cdk
        
        
        class S3BucketProduct(servicecatalog.ProductStack):
            def __init__(self, scope, id):
                super().__init__(scope, id)
        
                s3.Bucket(self, "BucketProductV2")
        
        product_stack_history = servicecatalog.ProductStackHistory(self, "ProductStackHistory",
            product_stack=S3BucketProduct(self, "S3BucketProduct"),
            current_version_name="v2",
            current_version_locked=True
        )
        
        product = servicecatalog.CloudFormationProduct(self, "MyFirstProduct",
            product_name="My Product",
            owner="Product Owner",
            product_versions=[
                product_stack_history.current_version()
            ]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        current_version_locked: builtins.bool,
        current_version_name: builtins.str,
        product_stack: ProductStack,
        description: typing.Optional[builtins.str] = None,
        directory: typing.Optional[builtins.str] = None,
        validate_template: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param current_version_locked: If this is set to true, the ProductStack will not be overwritten if a snapshot is found for the currentVersionName.
        :param current_version_name: The current version name of the ProductStack.
        :param product_stack: The ProductStack whose history will be retained as a snapshot.
        :param description: The description of the product version. Default: - No description provided
        :param directory: The directory where template snapshots will be stored. Default: 'product-stack-snapshots'
        :param validate_template: Whether the specified product template will be validated by CloudFormation. If turned off, an invalid template configuration can be stored. Default: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ProductStackHistory.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ProductStackHistoryProps(
            current_version_locked=current_version_locked,
            current_version_name=current_version_name,
            product_stack=product_stack,
            description=description,
            directory=directory,
            validate_template=validate_template,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="currentVersion")
    def current_version(self) -> CloudFormationProductVersion:
        '''Retains product stack template as a snapshot when deployed and retrieves a CloudFormationProductVersion for the current product version.'''
        return typing.cast(CloudFormationProductVersion, jsii.invoke(self, "currentVersion", []))

    @jsii.member(jsii_name="versionFromSnapshot")
    def version_from_snapshot(
        self,
        product_version_name: builtins.str,
    ) -> CloudFormationProductVersion:
        '''Retrieves a CloudFormationProductVersion from a previously deployed productVersionName.

        :param product_version_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ProductStackHistory.version_from_snapshot)
            check_type(argname="argument product_version_name", value=product_version_name, expected_type=type_hints["product_version_name"])
        return typing.cast(CloudFormationProductVersion, jsii.invoke(self, "versionFromSnapshot", [product_version_name]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.ProductStackHistoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "current_version_locked": "currentVersionLocked",
        "current_version_name": "currentVersionName",
        "product_stack": "productStack",
        "description": "description",
        "directory": "directory",
        "validate_template": "validateTemplate",
    },
)
class ProductStackHistoryProps:
    def __init__(
        self,
        *,
        current_version_locked: builtins.bool,
        current_version_name: builtins.str,
        product_stack: ProductStack,
        description: typing.Optional[builtins.str] = None,
        directory: typing.Optional[builtins.str] = None,
        validate_template: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for a ProductStackHistory.

        :param current_version_locked: If this is set to true, the ProductStack will not be overwritten if a snapshot is found for the currentVersionName.
        :param current_version_name: The current version name of the ProductStack.
        :param product_stack: The ProductStack whose history will be retained as a snapshot.
        :param description: The description of the product version. Default: - No description provided
        :param directory: The directory where template snapshots will be stored. Default: 'product-stack-snapshots'
        :param validate_template: Whether the specified product template will be validated by CloudFormation. If turned off, an invalid template configuration can be stored. Default: true

        :exampleMetadata: infused

        Example::

            # Example automatically generated from non-compiling source. May contain errors.
            import aws_cdk.aws_s3 as s3
            import aws_cdk as cdk
            
            
            class S3BucketProduct(servicecatalog.ProductStack):
                def __init__(self, scope, id):
                    super().__init__(scope, id)
            
                    s3.Bucket(self, "BucketProductV2")
            
            product_stack_history = servicecatalog.ProductStackHistory(self, "ProductStackHistory",
                product_stack=S3BucketProduct(self, "S3BucketProduct"),
                current_version_name="v2",
                current_version_locked=True
            )
            
            product = servicecatalog.CloudFormationProduct(self, "MyFirstProduct",
                product_name="My Product",
                owner="Product Owner",
                product_versions=[
                    product_stack_history.current_version()
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ProductStackHistoryProps.__init__)
            check_type(argname="argument current_version_locked", value=current_version_locked, expected_type=type_hints["current_version_locked"])
            check_type(argname="argument current_version_name", value=current_version_name, expected_type=type_hints["current_version_name"])
            check_type(argname="argument product_stack", value=product_stack, expected_type=type_hints["product_stack"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
            check_type(argname="argument validate_template", value=validate_template, expected_type=type_hints["validate_template"])
        self._values: typing.Dict[str, typing.Any] = {
            "current_version_locked": current_version_locked,
            "current_version_name": current_version_name,
            "product_stack": product_stack,
        }
        if description is not None:
            self._values["description"] = description
        if directory is not None:
            self._values["directory"] = directory
        if validate_template is not None:
            self._values["validate_template"] = validate_template

    @builtins.property
    def current_version_locked(self) -> builtins.bool:
        '''If this is set to true, the ProductStack will not be overwritten if a snapshot is found for the currentVersionName.'''
        result = self._values.get("current_version_locked")
        assert result is not None, "Required property 'current_version_locked' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def current_version_name(self) -> builtins.str:
        '''The current version name of the ProductStack.'''
        result = self._values.get("current_version_name")
        assert result is not None, "Required property 'current_version_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_stack(self) -> ProductStack:
        '''The ProductStack whose history will be retained as a snapshot.'''
        result = self._values.get("product_stack")
        assert result is not None, "Required property 'product_stack' is missing"
        return typing.cast(ProductStack, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the product version.

        :default: - No description provided
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory(self) -> typing.Optional[builtins.str]:
        '''The directory where template snapshots will be stored.

        :default: 'product-stack-snapshots'
        '''
        result = self._values.get("directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validate_template(self) -> typing.Optional[builtins.bool]:
        '''Whether the specified product template will be validated by CloudFormation.

        If turned off, an invalid template configuration can be stored.

        :default: true
        '''
        result = self._values.get("validate_template")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProductStackHistoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.StackSetsConstraintOptions",
    jsii_struct_bases=[CommonConstraintOptions],
    name_mapping={
        "description": "description",
        "message_language": "messageLanguage",
        "accounts": "accounts",
        "admin_role": "adminRole",
        "execution_role_name": "executionRoleName",
        "regions": "regions",
        "allow_stack_set_instance_operations": "allowStackSetInstanceOperations",
    },
)
class StackSetsConstraintOptions(CommonConstraintOptions):
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional[MessageLanguage] = None,
        accounts: typing.Sequence[builtins.str],
        admin_role: _IRole_235f5d8e,
        execution_role_name: builtins.str,
        regions: typing.Sequence[builtins.str],
        allow_stack_set_instance_operations: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for deploying with Stackset, which creates a StackSet constraint.

        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        :param accounts: List of accounts to deploy stacks to.
        :param admin_role: IAM role used to administer the StackSets configuration.
        :param execution_role_name: IAM role used to provision the products in the Stacks.
        :param regions: List of regions to deploy stacks to.
        :param allow_stack_set_instance_operations: Wether to allow end users to create, update, and delete stacks. Default: false

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_iam as iam
            
            # portfolio: servicecatalog.Portfolio
            # product: servicecatalog.CloudFormationProduct
            
            
            admin_role = iam.Role(self, "AdminRole",
                assumed_by=iam.AccountRootPrincipal()
            )
            
            portfolio.deploy_with_stack_sets(product,
                accounts=["012345678901", "012345678902", "012345678903"],
                regions=["us-west-1", "us-east-1", "us-west-2", "us-east-1"],
                admin_role=admin_role,
                execution_role_name="SCStackSetExecutionRole",  # Name of role deployed in end users accounts.
                allow_stack_set_instance_operations=True
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StackSetsConstraintOptions.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument message_language", value=message_language, expected_type=type_hints["message_language"])
            check_type(argname="argument accounts", value=accounts, expected_type=type_hints["accounts"])
            check_type(argname="argument admin_role", value=admin_role, expected_type=type_hints["admin_role"])
            check_type(argname="argument execution_role_name", value=execution_role_name, expected_type=type_hints["execution_role_name"])
            check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
            check_type(argname="argument allow_stack_set_instance_operations", value=allow_stack_set_instance_operations, expected_type=type_hints["allow_stack_set_instance_operations"])
        self._values: typing.Dict[str, typing.Any] = {
            "accounts": accounts,
            "admin_role": admin_role,
            "execution_role_name": execution_role_name,
            "regions": regions,
        }
        if description is not None:
            self._values["description"] = description
        if message_language is not None:
            self._values["message_language"] = message_language
        if allow_stack_set_instance_operations is not None:
            self._values["allow_stack_set_instance_operations"] = allow_stack_set_instance_operations

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the constraint.

        :default: - No description provided
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message_language(self) -> typing.Optional[MessageLanguage]:
        '''The language code.

        Configures the language for error messages from service catalog.

        :default: - English
        '''
        result = self._values.get("message_language")
        return typing.cast(typing.Optional[MessageLanguage], result)

    @builtins.property
    def accounts(self) -> typing.List[builtins.str]:
        '''List of accounts to deploy stacks to.'''
        result = self._values.get("accounts")
        assert result is not None, "Required property 'accounts' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def admin_role(self) -> _IRole_235f5d8e:
        '''IAM role used to administer the StackSets configuration.'''
        result = self._values.get("admin_role")
        assert result is not None, "Required property 'admin_role' is missing"
        return typing.cast(_IRole_235f5d8e, result)

    @builtins.property
    def execution_role_name(self) -> builtins.str:
        '''IAM role used to provision the products in the Stacks.'''
        result = self._values.get("execution_role_name")
        assert result is not None, "Required property 'execution_role_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regions(self) -> typing.List[builtins.str]:
        '''List of regions to deploy stacks to.'''
        result = self._values.get("regions")
        assert result is not None, "Required property 'regions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def allow_stack_set_instance_operations(self) -> typing.Optional[builtins.bool]:
        '''Wether to allow end users to create, update, and delete stacks.

        :default: false
        '''
        result = self._values.get("allow_stack_set_instance_operations")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StackSetsConstraintOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TagOptions(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.TagOptions",
):
    '''Defines a set of TagOptions, which are a list of key-value pairs managed in AWS Service Catalog.

    It is not an AWS tag, but serves as a template for creating an AWS tag based on the TagOption.
    See https://docs.aws.amazon.com/servicecatalog/latest/adminguide/tagoptions.html

    :resource: AWS::ServiceCatalog::TagOption
    :exampleMetadata: infused

    Example::

        # portfolio: servicecatalog.Portfolio
        # product: servicecatalog.CloudFormationProduct
        
        
        tag_options_for_portfolio = servicecatalog.TagOptions(self, "OrgTagOptions",
            allowed_values_for_tags={
                "Group": ["finance", "engineering", "marketing", "research"],
                "CostCenter": ["01", "02", "03"]
            }
        )
        portfolio.associate_tag_options(tag_options_for_portfolio)
        
        tag_options_for_product = servicecatalog.TagOptions(self, "ProductTagOptions",
            allowed_values_for_tags={
                "Environment": ["dev", "alpha", "prod"]
            }
        )
        product.associate_tag_options(tag_options_for_product)
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        allowed_values_for_tags: typing.Mapping[builtins.str, typing.Sequence[builtins.str]],
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param allowed_values_for_tags: The values that are allowed to be set for specific tags. The keys of the map represent the tag keys, and the values of the map are a list of allowed values for that particular tag key.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TagOptions.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TagOptionsProps(allowed_values_for_tags=allowed_values_for_tags)

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.TagOptionsProps",
    jsii_struct_bases=[],
    name_mapping={"allowed_values_for_tags": "allowedValuesForTags"},
)
class TagOptionsProps:
    def __init__(
        self,
        *,
        allowed_values_for_tags: typing.Mapping[builtins.str, typing.Sequence[builtins.str]],
    ) -> None:
        '''Properties for TagOptions.

        :param allowed_values_for_tags: The values that are allowed to be set for specific tags. The keys of the map represent the tag keys, and the values of the map are a list of allowed values for that particular tag key.

        :exampleMetadata: infused

        Example::

            # portfolio: servicecatalog.Portfolio
            # product: servicecatalog.CloudFormationProduct
            
            
            tag_options_for_portfolio = servicecatalog.TagOptions(self, "OrgTagOptions",
                allowed_values_for_tags={
                    "Group": ["finance", "engineering", "marketing", "research"],
                    "CostCenter": ["01", "02", "03"]
                }
            )
            portfolio.associate_tag_options(tag_options_for_portfolio)
            
            tag_options_for_product = servicecatalog.TagOptions(self, "ProductTagOptions",
                allowed_values_for_tags={
                    "Environment": ["dev", "alpha", "prod"]
                }
            )
            product.associate_tag_options(tag_options_for_product)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TagOptionsProps.__init__)
            check_type(argname="argument allowed_values_for_tags", value=allowed_values_for_tags, expected_type=type_hints["allowed_values_for_tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_values_for_tags": allowed_values_for_tags,
        }

    @builtins.property
    def allowed_values_for_tags(
        self,
    ) -> typing.Mapping[builtins.str, typing.List[builtins.str]]:
        '''The values that are allowed to be set for specific tags.

        The keys of the map represent the tag keys,
        and the values of the map are a list of allowed values for that particular tag key.
        '''
        result = self._values.get("allowed_values_for_tags")
        assert result is not None, "Required property 'allowed_values_for_tags' is missing"
        return typing.cast(typing.Mapping[builtins.str, typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagOptionsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.TagUpdateConstraintOptions",
    jsii_struct_bases=[CommonConstraintOptions],
    name_mapping={
        "description": "description",
        "message_language": "messageLanguage",
        "allow": "allow",
    },
)
class TagUpdateConstraintOptions(CommonConstraintOptions):
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional[MessageLanguage] = None,
        allow: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for ResourceUpdateConstraint.

        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        :param allow: Toggle for if users should be allowed to change/update tags on provisioned products. Default: true

        :exampleMetadata: infused

        Example::

            # portfolio: servicecatalog.Portfolio
            # product: servicecatalog.CloudFormationProduct
            
            
            # to disable tag updates:
            portfolio.constrain_tag_updates(product,
                allow=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TagUpdateConstraintOptions.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument message_language", value=message_language, expected_type=type_hints["message_language"])
            check_type(argname="argument allow", value=allow, expected_type=type_hints["allow"])
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if message_language is not None:
            self._values["message_language"] = message_language
        if allow is not None:
            self._values["allow"] = allow

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the constraint.

        :default: - No description provided
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message_language(self) -> typing.Optional[MessageLanguage]:
        '''The language code.

        Configures the language for error messages from service catalog.

        :default: - English
        '''
        result = self._values.get("message_language")
        return typing.cast(typing.Optional[MessageLanguage], result)

    @builtins.property
    def allow(self) -> typing.Optional[builtins.bool]:
        '''Toggle for if users should be allowed to change/update tags on provisioned products.

        :default: true
        '''
        result = self._values.get("allow")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagUpdateConstraintOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.TemplateRule",
    jsii_struct_bases=[],
    name_mapping={
        "assertions": "assertions",
        "rule_name": "ruleName",
        "condition": "condition",
    },
)
class TemplateRule:
    def __init__(
        self,
        *,
        assertions: typing.Sequence[typing.Union["TemplateRuleAssertion", typing.Dict[str, typing.Any]]],
        rule_name: builtins.str,
        condition: typing.Optional[_ICfnRuleConditionExpression_9aca991b] = None,
    ) -> None:
        '''Defines the provisioning template constraints.

        :param assertions: A list of assertions that make up the rule.
        :param rule_name: Name of the rule.
        :param condition: Specify when to apply rule with a rule-specific intrinsic function. Default: - no rule condition provided

        :exampleMetadata: infused

        Example::

            import aws_cdk as cdk
            
            # portfolio: servicecatalog.Portfolio
            # product: servicecatalog.CloudFormationProduct
            
            
            portfolio.constrain_cloud_formation_parameters(product,
                rule=servicecatalog.TemplateRule(
                    rule_name="testInstanceType",
                    condition=cdk.Fn.condition_equals(cdk.Fn.ref("Environment"), "test"),
                    assertions=[servicecatalog.TemplateRuleAssertion(
                        assert=cdk.Fn.condition_contains(["t2.micro", "t2.small"], cdk.Fn.ref("InstanceType")),
                        description="For test environment, the instance type should be small"
                    )]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TemplateRule.__init__)
            check_type(argname="argument assertions", value=assertions, expected_type=type_hints["assertions"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
        self._values: typing.Dict[str, typing.Any] = {
            "assertions": assertions,
            "rule_name": rule_name,
        }
        if condition is not None:
            self._values["condition"] = condition

    @builtins.property
    def assertions(self) -> typing.List["TemplateRuleAssertion"]:
        '''A list of assertions that make up the rule.'''
        result = self._values.get("assertions")
        assert result is not None, "Required property 'assertions' is missing"
        return typing.cast(typing.List["TemplateRuleAssertion"], result)

    @builtins.property
    def rule_name(self) -> builtins.str:
        '''Name of the rule.'''
        result = self._values.get("rule_name")
        assert result is not None, "Required property 'rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition(self) -> typing.Optional[_ICfnRuleConditionExpression_9aca991b]:
        '''Specify when to apply rule with a rule-specific intrinsic function.

        :default: - no rule condition provided
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[_ICfnRuleConditionExpression_9aca991b], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.TemplateRuleAssertion",
    jsii_struct_bases=[],
    name_mapping={"assert_": "assert", "description": "description"},
)
class TemplateRuleAssertion:
    def __init__(
        self,
        *,
        assert_: _ICfnRuleConditionExpression_9aca991b,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''An assertion within a template rule, defined by intrinsic functions.

        :param assert_: The assertion condition.
        :param description: The description for the asssertion. Default: - no description provided for the assertion.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_servicecatalog as servicecatalog
            
            # cfn_rule_condition_expression: cdk.ICfnRuleConditionExpression
            
            template_rule_assertion = servicecatalog.TemplateRuleAssertion(
                assert=cfn_rule_condition_expression,
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TemplateRuleAssertion.__init__)
            check_type(argname="argument assert_", value=assert_, expected_type=type_hints["assert_"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "assert_": assert_,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def assert_(self) -> _ICfnRuleConditionExpression_9aca991b:
        '''The assertion condition.'''
        result = self._values.get("assert_")
        assert result is not None, "Required property 'assert_' is missing"
        return typing.cast(_ICfnRuleConditionExpression_9aca991b, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the asssertion.

        :default: - no description provided for the assertion.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateRuleAssertion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudFormationProduct(
    Product,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_servicecatalog.CloudFormationProduct",
):
    '''A Service Catalog Cloudformation Product.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_s3 as s3
        import aws_cdk as cdk
        
        
        class S3BucketProduct(servicecatalog.ProductStack):
            def __init__(self, scope, id):
                super().__init__(scope, id)
        
                s3.Bucket(self, "BucketProduct")
        
        product = servicecatalog.CloudFormationProduct(self, "Product",
            product_name="My Product",
            owner="Product Owner",
            product_versions=[servicecatalog.CloudFormationProductVersion(
                product_version_name="v1",
                cloud_formation_template=servicecatalog.CloudFormationTemplate.from_product_stack(S3BucketProduct(self, "S3BucketProduct"))
            )
            ]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        owner: builtins.str,
        product_name: builtins.str,
        product_versions: typing.Sequence[typing.Union[CloudFormationProductVersion, typing.Dict[str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        distributor: typing.Optional[builtins.str] = None,
        message_language: typing.Optional[MessageLanguage] = None,
        replace_product_version_ids: typing.Optional[builtins.bool] = None,
        support_description: typing.Optional[builtins.str] = None,
        support_email: typing.Optional[builtins.str] = None,
        support_url: typing.Optional[builtins.str] = None,
        tag_options: typing.Optional[TagOptions] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param owner: The owner of the product.
        :param product_name: The name of the product.
        :param product_versions: The configuration of the product version.
        :param description: The description of the product. Default: - No description provided
        :param distributor: The distributor of the product. Default: - No distributor provided
        :param message_language: The language code. Controls language for logging and errors. Default: - English
        :param replace_product_version_ids: Whether to give provisioning artifacts a new unique identifier when the product attributes or provisioning artifacts is updated. Default: false
        :param support_description: The support information about the product. Default: - No support description provided
        :param support_email: The contact email for product support. Default: - No support email provided
        :param support_url: The contact URL for product support. Default: - No support URL provided
        :param tag_options: TagOptions associated directly to a product. Default: - No tagOptions provided
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudFormationProduct.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CloudFormationProductProps(
            owner=owner,
            product_name=product_name,
            product_versions=product_versions,
            description=description,
            distributor=distributor,
            message_language=message_language,
            replace_product_version_ids=replace_product_version_ids,
            support_description=support_description,
            support_email=support_email,
            support_url=support_url,
            tag_options=tag_options,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="productArn")
    def product_arn(self) -> builtins.str:
        '''The ARN of the product.'''
        return typing.cast(builtins.str, jsii.get(self, "productArn"))

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        '''The id of the product.'''
        return typing.cast(builtins.str, jsii.get(self, "productId"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_servicecatalog.CloudFormationRuleConstraintOptions",
    jsii_struct_bases=[CommonConstraintOptions],
    name_mapping={
        "description": "description",
        "message_language": "messageLanguage",
        "rule": "rule",
    },
)
class CloudFormationRuleConstraintOptions(CommonConstraintOptions):
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        message_language: typing.Optional[MessageLanguage] = None,
        rule: typing.Union[TemplateRule, typing.Dict[str, typing.Any]],
    ) -> None:
        '''Properties for provisoning rule constraint.

        :param description: The description of the constraint. Default: - No description provided
        :param message_language: The language code. Configures the language for error messages from service catalog. Default: - English
        :param rule: The rule with condition and assertions to apply to template.

        :exampleMetadata: infused

        Example::

            import aws_cdk as cdk
            
            # portfolio: servicecatalog.Portfolio
            # product: servicecatalog.CloudFormationProduct
            
            
            portfolio.constrain_cloud_formation_parameters(product,
                rule=servicecatalog.TemplateRule(
                    rule_name="testInstanceType",
                    condition=cdk.Fn.condition_equals(cdk.Fn.ref("Environment"), "test"),
                    assertions=[servicecatalog.TemplateRuleAssertion(
                        assert=cdk.Fn.condition_contains(["t2.micro", "t2.small"], cdk.Fn.ref("InstanceType")),
                        description="For test environment, the instance type should be small"
                    )]
                )
            )
        '''
        if isinstance(rule, dict):
            rule = TemplateRule(**rule)
        if __debug__:
            type_hints = typing.get_type_hints(CloudFormationRuleConstraintOptions.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument message_language", value=message_language, expected_type=type_hints["message_language"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        self._values: typing.Dict[str, typing.Any] = {
            "rule": rule,
        }
        if description is not None:
            self._values["description"] = description
        if message_language is not None:
            self._values["message_language"] = message_language

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the constraint.

        :default: - No description provided
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message_language(self) -> typing.Optional[MessageLanguage]:
        '''The language code.

        Configures the language for error messages from service catalog.

        :default: - English
        '''
        result = self._values.get("message_language")
        return typing.cast(typing.Optional[MessageLanguage], result)

    @builtins.property
    def rule(self) -> TemplateRule:
        '''The rule with condition and assertions to apply to template.'''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(TemplateRule, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFormationRuleConstraintOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAcceptedPortfolioShare",
    "CfnAcceptedPortfolioShareProps",
    "CfnCloudFormationProduct",
    "CfnCloudFormationProductProps",
    "CfnCloudFormationProvisionedProduct",
    "CfnCloudFormationProvisionedProductProps",
    "CfnLaunchNotificationConstraint",
    "CfnLaunchNotificationConstraintProps",
    "CfnLaunchRoleConstraint",
    "CfnLaunchRoleConstraintProps",
    "CfnLaunchTemplateConstraint",
    "CfnLaunchTemplateConstraintProps",
    "CfnPortfolio",
    "CfnPortfolioPrincipalAssociation",
    "CfnPortfolioPrincipalAssociationProps",
    "CfnPortfolioProductAssociation",
    "CfnPortfolioProductAssociationProps",
    "CfnPortfolioProps",
    "CfnPortfolioShare",
    "CfnPortfolioShareProps",
    "CfnResourceUpdateConstraint",
    "CfnResourceUpdateConstraintProps",
    "CfnServiceAction",
    "CfnServiceActionAssociation",
    "CfnServiceActionAssociationProps",
    "CfnServiceActionProps",
    "CfnStackSetConstraint",
    "CfnStackSetConstraintProps",
    "CfnTagOption",
    "CfnTagOptionAssociation",
    "CfnTagOptionAssociationProps",
    "CfnTagOptionProps",
    "CloudFormationProduct",
    "CloudFormationProductProps",
    "CloudFormationProductVersion",
    "CloudFormationRuleConstraintOptions",
    "CloudFormationTemplate",
    "CloudFormationTemplateConfig",
    "CommonConstraintOptions",
    "IPortfolio",
    "IProduct",
    "MessageLanguage",
    "Portfolio",
    "PortfolioProps",
    "PortfolioShareOptions",
    "Product",
    "ProductStack",
    "ProductStackHistory",
    "ProductStackHistoryProps",
    "StackSetsConstraintOptions",
    "TagOptions",
    "TagOptionsProps",
    "TagUpdateConstraintOptions",
    "TemplateRule",
    "TemplateRuleAssertion",
]

publication.publish()
