'''
# AWS IoT Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_iot as iot
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IoT construct libraries](https://constructs.dev/search?q=iot)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IoT resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoT.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-iot-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IoT](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoT.html).

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
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnAccountAuditConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnAccountAuditConfiguration",
):
    '''A CloudFormation ``AWS::IoT::AccountAuditConfiguration``.

    Use the ``AWS::IoT::AccountAuditConfiguration`` resource to configure or reconfigure the Device Defender audit settings for your account. Settings include how audit notifications are sent and which audit checks are enabled or disabled. For API reference, see `UpdateAccountAuditConfiguration <https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateAccountAuditConfiguration.html>`_ and for detailed information on all available audit checks, see `Audit checks <https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-audit-checks.html>`_ .

    :cloudformationResource: AWS::IoT::AccountAuditConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_account_audit_configuration = iot.CfnAccountAuditConfiguration(self, "MyCfnAccountAuditConfiguration",
            account_id="accountId",
            audit_check_configurations=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty(
                authenticated_cognito_role_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                ca_certificate_expiring_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                ca_certificate_key_quality_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                conflicting_client_ids_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                device_certificate_expiring_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                device_certificate_key_quality_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                device_certificate_shared_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                iot_policy_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                iot_role_alias_allows_access_to_unused_services_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                iot_role_alias_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                logging_disabled_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                revoked_ca_certificate_still_active_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                revoked_device_certificate_still_active_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                unauthenticated_cognito_role_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                )
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            audit_notification_target_configurations=iot.CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty(
                sns=iot.CfnAccountAuditConfiguration.AuditNotificationTargetProperty(
                    enabled=False,
                    role_arn="roleArn",
                    target_arn="targetArn"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account_id: builtins.str,
        audit_check_configurations: typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        role_arn: builtins.str,
        audit_notification_target_configurations: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::AccountAuditConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param account_id: The ID of the account. You can use the expression ``!Sub "${AWS::AccountId}"`` to use your account ID.
        :param audit_check_configurations: Specifies which audit checks are enabled and disabled for this account. Some data collection might start immediately when certain checks are enabled. When a check is disabled, any data collected so far in relation to the check is deleted. To disable a check, set the value of the ``Enabled:`` key to ``false`` . If an enabled check is removed from the template, it will also be disabled. You can't disable a check if it's used by any scheduled audit. You must delete the check from the scheduled audit or delete the scheduled audit itself to disable the check. For more information on avialbe auidt checks see `AWS::IoT::AccountAuditConfiguration AuditCheckConfigurations <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html>`_
        :param role_arn: The Amazon Resource Name (ARN) of the role that grants permission to AWS IoT to access information about your devices, policies, certificates, and other items as required when performing an audit.
        :param audit_notification_target_configurations: Information about the targets to which audit notifications are sent.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAccountAuditConfiguration.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccountAuditConfigurationProps(
            account_id=account_id,
            audit_check_configurations=audit_check_configurations,
            role_arn=role_arn,
            audit_notification_target_configurations=audit_notification_target_configurations,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAccountAuditConfiguration.inspect)
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
            type_hints = typing.get_type_hints(CfnAccountAuditConfiguration._render_properties)
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
        '''The ID of the account.

        You can use the expression ``!Sub "${AWS::AccountId}"`` to use your account ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-accountid
        '''
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAccountAuditConfiguration, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="auditCheckConfigurations")
    def audit_check_configurations(
        self,
    ) -> typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty", _IResolvable_da3f097b]:
        '''Specifies which audit checks are enabled and disabled for this account.

        Some data collection might start immediately when certain checks are enabled. When a check is disabled, any data collected so far in relation to the check is deleted. To disable a check, set the value of the ``Enabled:`` key to ``false`` .

        If an enabled check is removed from the template, it will also be disabled.

        You can't disable a check if it's used by any scheduled audit. You must delete the check from the scheduled audit or delete the scheduled audit itself to disable the check.

        For more information on avialbe auidt checks see `AWS::IoT::AccountAuditConfiguration AuditCheckConfigurations <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html>`_

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations
        '''
        return typing.cast(typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty", _IResolvable_da3f097b], jsii.get(self, "auditCheckConfigurations"))

    @audit_check_configurations.setter
    def audit_check_configurations(
        self,
        value: typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAccountAuditConfiguration, "audit_check_configurations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditCheckConfigurations", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the role that grants permission to AWS IoT to access information about your devices, policies, certificates, and other items as required when performing an audit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAccountAuditConfiguration, "role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="auditNotificationTargetConfigurations")
    def audit_notification_target_configurations(
        self,
    ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty", _IResolvable_da3f097b]]:
        '''Information about the targets to which audit notifications are sent.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditnotificationtargetconfigurations
        '''
        return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty", _IResolvable_da3f097b]], jsii.get(self, "auditNotificationTargetConfigurations"))

    @audit_notification_target_configurations.setter
    def audit_notification_target_configurations(
        self,
        value: typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAccountAuditConfiguration, "audit_notification_target_configurations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditNotificationTargetConfigurations", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class AuditCheckConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Which audit checks are enabled and disabled for this account.

            :param enabled: True if this audit check is enabled for this account.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                audit_check_configuration_property = iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnAccountAuditConfiguration.AuditCheckConfigurationProperty.__init__)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''True if this audit check is enabled for this account.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfiguration.html#cfn-iot-accountauditconfiguration-auditcheckconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuditCheckConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authenticated_cognito_role_overly_permissive_check": "authenticatedCognitoRoleOverlyPermissiveCheck",
            "ca_certificate_expiring_check": "caCertificateExpiringCheck",
            "ca_certificate_key_quality_check": "caCertificateKeyQualityCheck",
            "conflicting_client_ids_check": "conflictingClientIdsCheck",
            "device_certificate_expiring_check": "deviceCertificateExpiringCheck",
            "device_certificate_key_quality_check": "deviceCertificateKeyQualityCheck",
            "device_certificate_shared_check": "deviceCertificateSharedCheck",
            "iot_policy_overly_permissive_check": "iotPolicyOverlyPermissiveCheck",
            "iot_role_alias_allows_access_to_unused_services_check": "iotRoleAliasAllowsAccessToUnusedServicesCheck",
            "iot_role_alias_overly_permissive_check": "iotRoleAliasOverlyPermissiveCheck",
            "logging_disabled_check": "loggingDisabledCheck",
            "revoked_ca_certificate_still_active_check": "revokedCaCertificateStillActiveCheck",
            "revoked_device_certificate_still_active_check": "revokedDeviceCertificateStillActiveCheck",
            "unauthenticated_cognito_role_overly_permissive_check": "unauthenticatedCognitoRoleOverlyPermissiveCheck",
        },
    )
    class AuditCheckConfigurationsProperty:
        def __init__(
            self,
            *,
            authenticated_cognito_role_overly_permissive_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            ca_certificate_expiring_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            ca_certificate_key_quality_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            conflicting_client_ids_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            device_certificate_expiring_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            device_certificate_key_quality_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            device_certificate_shared_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            iot_policy_overly_permissive_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            iot_role_alias_allows_access_to_unused_services_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            iot_role_alias_overly_permissive_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            logging_disabled_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            revoked_ca_certificate_still_active_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            revoked_device_certificate_still_active_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            unauthenticated_cognito_role_overly_permissive_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The types of audit checks that can be performed.

            :param authenticated_cognito_role_overly_permissive_check: Checks the permissiveness of an authenticated Amazon Cognito identity pool role. For this check, AWS IoT Device Defender audits all Amazon Cognito identity pools that have been used to connect to the AWS IoT message broker during the 31 days before the audit is performed.
            :param ca_certificate_expiring_check: Checks if a CA certificate is expiring. This check applies to CA certificates expiring within 30 days or that have expired.
            :param ca_certificate_key_quality_check: Checks the quality of the CA certificate key. The quality checks if the key is in a valid format, not expired, and if the key meets a minimum required size. This check applies to CA certificates that are ``ACTIVE`` or ``PENDING_TRANSFER`` .
            :param conflicting_client_ids_check: Checks if multiple devices connect using the same client ID.
            :param device_certificate_expiring_check: Checks if a device certificate is expiring. This check applies to device certificates expiring within 30 days or that have expired.
            :param device_certificate_key_quality_check: Checks the quality of the device certificate key. The quality checks if the key is in a valid format, not expired, signed by a registered certificate authority, and if the key meets a minimum required size.
            :param device_certificate_shared_check: Checks if multiple concurrent connections use the same X.509 certificate to authenticate with AWS IoT .
            :param iot_policy_overly_permissive_check: Checks the permissiveness of a policy attached to an authenticated Amazon Cognito identity pool role.
            :param iot_role_alias_allows_access_to_unused_services_check: Checks if a role alias has access to services that haven't been used for the AWS IoT device in the last year.
            :param iot_role_alias_overly_permissive_check: Checks if the temporary credentials provided by AWS IoT role aliases are overly permissive.
            :param logging_disabled_check: Checks if AWS IoT logs are disabled.
            :param revoked_ca_certificate_still_active_check: Checks if a revoked CA certificate is still active.
            :param revoked_device_certificate_still_active_check: Checks if a revoked device certificate is still active.
            :param unauthenticated_cognito_role_overly_permissive_check: Checks if policy attached to an unauthenticated Amazon Cognito identity pool role is too permissive.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                audit_check_configurations_property = iot.CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty(
                    authenticated_cognito_role_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    ca_certificate_expiring_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    ca_certificate_key_quality_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    conflicting_client_ids_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    device_certificate_expiring_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    device_certificate_key_quality_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    device_certificate_shared_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    iot_policy_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    iot_role_alias_allows_access_to_unused_services_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    iot_role_alias_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    logging_disabled_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    revoked_ca_certificate_still_active_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    revoked_device_certificate_still_active_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    unauthenticated_cognito_role_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty.__init__)
                check_type(argname="argument authenticated_cognito_role_overly_permissive_check", value=authenticated_cognito_role_overly_permissive_check, expected_type=type_hints["authenticated_cognito_role_overly_permissive_check"])
                check_type(argname="argument ca_certificate_expiring_check", value=ca_certificate_expiring_check, expected_type=type_hints["ca_certificate_expiring_check"])
                check_type(argname="argument ca_certificate_key_quality_check", value=ca_certificate_key_quality_check, expected_type=type_hints["ca_certificate_key_quality_check"])
                check_type(argname="argument conflicting_client_ids_check", value=conflicting_client_ids_check, expected_type=type_hints["conflicting_client_ids_check"])
                check_type(argname="argument device_certificate_expiring_check", value=device_certificate_expiring_check, expected_type=type_hints["device_certificate_expiring_check"])
                check_type(argname="argument device_certificate_key_quality_check", value=device_certificate_key_quality_check, expected_type=type_hints["device_certificate_key_quality_check"])
                check_type(argname="argument device_certificate_shared_check", value=device_certificate_shared_check, expected_type=type_hints["device_certificate_shared_check"])
                check_type(argname="argument iot_policy_overly_permissive_check", value=iot_policy_overly_permissive_check, expected_type=type_hints["iot_policy_overly_permissive_check"])
                check_type(argname="argument iot_role_alias_allows_access_to_unused_services_check", value=iot_role_alias_allows_access_to_unused_services_check, expected_type=type_hints["iot_role_alias_allows_access_to_unused_services_check"])
                check_type(argname="argument iot_role_alias_overly_permissive_check", value=iot_role_alias_overly_permissive_check, expected_type=type_hints["iot_role_alias_overly_permissive_check"])
                check_type(argname="argument logging_disabled_check", value=logging_disabled_check, expected_type=type_hints["logging_disabled_check"])
                check_type(argname="argument revoked_ca_certificate_still_active_check", value=revoked_ca_certificate_still_active_check, expected_type=type_hints["revoked_ca_certificate_still_active_check"])
                check_type(argname="argument revoked_device_certificate_still_active_check", value=revoked_device_certificate_still_active_check, expected_type=type_hints["revoked_device_certificate_still_active_check"])
                check_type(argname="argument unauthenticated_cognito_role_overly_permissive_check", value=unauthenticated_cognito_role_overly_permissive_check, expected_type=type_hints["unauthenticated_cognito_role_overly_permissive_check"])
            self._values: typing.Dict[str, typing.Any] = {}
            if authenticated_cognito_role_overly_permissive_check is not None:
                self._values["authenticated_cognito_role_overly_permissive_check"] = authenticated_cognito_role_overly_permissive_check
            if ca_certificate_expiring_check is not None:
                self._values["ca_certificate_expiring_check"] = ca_certificate_expiring_check
            if ca_certificate_key_quality_check is not None:
                self._values["ca_certificate_key_quality_check"] = ca_certificate_key_quality_check
            if conflicting_client_ids_check is not None:
                self._values["conflicting_client_ids_check"] = conflicting_client_ids_check
            if device_certificate_expiring_check is not None:
                self._values["device_certificate_expiring_check"] = device_certificate_expiring_check
            if device_certificate_key_quality_check is not None:
                self._values["device_certificate_key_quality_check"] = device_certificate_key_quality_check
            if device_certificate_shared_check is not None:
                self._values["device_certificate_shared_check"] = device_certificate_shared_check
            if iot_policy_overly_permissive_check is not None:
                self._values["iot_policy_overly_permissive_check"] = iot_policy_overly_permissive_check
            if iot_role_alias_allows_access_to_unused_services_check is not None:
                self._values["iot_role_alias_allows_access_to_unused_services_check"] = iot_role_alias_allows_access_to_unused_services_check
            if iot_role_alias_overly_permissive_check is not None:
                self._values["iot_role_alias_overly_permissive_check"] = iot_role_alias_overly_permissive_check
            if logging_disabled_check is not None:
                self._values["logging_disabled_check"] = logging_disabled_check
            if revoked_ca_certificate_still_active_check is not None:
                self._values["revoked_ca_certificate_still_active_check"] = revoked_ca_certificate_still_active_check
            if revoked_device_certificate_still_active_check is not None:
                self._values["revoked_device_certificate_still_active_check"] = revoked_device_certificate_still_active_check
            if unauthenticated_cognito_role_overly_permissive_check is not None:
                self._values["unauthenticated_cognito_role_overly_permissive_check"] = unauthenticated_cognito_role_overly_permissive_check

        @builtins.property
        def authenticated_cognito_role_overly_permissive_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]]:
            '''Checks the permissiveness of an authenticated Amazon Cognito identity pool role.

            For this check, AWS IoT Device Defender audits all Amazon Cognito identity pools that have been used to connect to the AWS IoT message broker during the 31 days before the audit is performed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-authenticatedcognitoroleoverlypermissivecheck
            '''
            result = self._values.get("authenticated_cognito_role_overly_permissive_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def ca_certificate_expiring_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]]:
            '''Checks if a CA certificate is expiring.

            This check applies to CA certificates expiring within 30 days or that have expired.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-cacertificateexpiringcheck
            '''
            result = self._values.get("ca_certificate_expiring_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def ca_certificate_key_quality_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]]:
            '''Checks the quality of the CA certificate key.

            The quality checks if the key is in a valid format, not expired, and if the key meets a minimum required size. This check applies to CA certificates that are ``ACTIVE`` or ``PENDING_TRANSFER`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-cacertificatekeyqualitycheck
            '''
            result = self._values.get("ca_certificate_key_quality_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def conflicting_client_ids_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]]:
            '''Checks if multiple devices connect using the same client ID.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-conflictingclientidscheck
            '''
            result = self._values.get("conflicting_client_ids_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def device_certificate_expiring_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]]:
            '''Checks if a device certificate is expiring.

            This check applies to device certificates expiring within 30 days or that have expired.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-devicecertificateexpiringcheck
            '''
            result = self._values.get("device_certificate_expiring_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def device_certificate_key_quality_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]]:
            '''Checks the quality of the device certificate key.

            The quality checks if the key is in a valid format, not expired, signed by a registered certificate authority, and if the key meets a minimum required size.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-devicecertificatekeyqualitycheck
            '''
            result = self._values.get("device_certificate_key_quality_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def device_certificate_shared_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]]:
            '''Checks if multiple concurrent connections use the same X.509 certificate to authenticate with AWS IoT .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-devicecertificatesharedcheck
            '''
            result = self._values.get("device_certificate_shared_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def iot_policy_overly_permissive_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]]:
            '''Checks the permissiveness of a policy attached to an authenticated Amazon Cognito identity pool role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-iotpolicyoverlypermissivecheck
            '''
            result = self._values.get("iot_policy_overly_permissive_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def iot_role_alias_allows_access_to_unused_services_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]]:
            '''Checks if a role alias has access to services that haven't been used for the AWS IoT device in the last year.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-iotrolealiasallowsaccesstounusedservicescheck
            '''
            result = self._values.get("iot_role_alias_allows_access_to_unused_services_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def iot_role_alias_overly_permissive_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]]:
            '''Checks if the temporary credentials provided by AWS IoT role aliases are overly permissive.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-iotrolealiasoverlypermissivecheck
            '''
            result = self._values.get("iot_role_alias_overly_permissive_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def logging_disabled_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]]:
            '''Checks if AWS IoT logs are disabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-loggingdisabledcheck
            '''
            result = self._values.get("logging_disabled_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def revoked_ca_certificate_still_active_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]]:
            '''Checks if a revoked CA certificate is still active.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-revokedcacertificatestillactivecheck
            '''
            result = self._values.get("revoked_ca_certificate_still_active_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def revoked_device_certificate_still_active_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]]:
            '''Checks if a revoked device certificate is still active.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-revokeddevicecertificatestillactivecheck
            '''
            result = self._values.get("revoked_device_certificate_still_active_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def unauthenticated_cognito_role_overly_permissive_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]]:
            '''Checks if policy attached to an unauthenticated Amazon Cognito identity pool role is too permissive.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-unauthenticatedcognitoroleoverlypermissivecheck
            '''
            result = self._values.get("unauthenticated_cognito_role_overly_permissive_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuditCheckConfigurationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty",
        jsii_struct_bases=[],
        name_mapping={"sns": "sns"},
    )
    class AuditNotificationTargetConfigurationsProperty:
        def __init__(
            self,
            *,
            sns: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditNotificationTargetProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The configuration of the audit notification target.

            :param sns: The ``Sns`` notification target.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtargetconfigurations.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                audit_notification_target_configurations_property = iot.CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty(
                    sns=iot.CfnAccountAuditConfiguration.AuditNotificationTargetProperty(
                        enabled=False,
                        role_arn="roleArn",
                        target_arn="targetArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty.__init__)
                check_type(argname="argument sns", value=sns, expected_type=type_hints["sns"])
            self._values: typing.Dict[str, typing.Any] = {}
            if sns is not None:
                self._values["sns"] = sns

        @builtins.property
        def sns(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditNotificationTargetProperty", _IResolvable_da3f097b]]:
            '''The ``Sns`` notification target.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtargetconfigurations.html#cfn-iot-accountauditconfiguration-auditnotificationtargetconfigurations-sns
            '''
            result = self._values.get("sns")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditNotificationTargetProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuditNotificationTargetConfigurationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnAccountAuditConfiguration.AuditNotificationTargetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "role_arn": "roleArn",
            "target_arn": "targetArn",
        },
    )
    class AuditNotificationTargetProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            role_arn: typing.Optional[builtins.str] = None,
            target_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the targets to which audit notifications are sent.

            :param enabled: True if notifications to the target are enabled.
            :param role_arn: The ARN of the role that grants permission to send notifications to the target.
            :param target_arn: The ARN of the target (SNS topic) to which audit notifications are sent.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                audit_notification_target_property = iot.CfnAccountAuditConfiguration.AuditNotificationTargetProperty(
                    enabled=False,
                    role_arn="roleArn",
                    target_arn="targetArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnAccountAuditConfiguration.AuditNotificationTargetProperty.__init__)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            self._values: typing.Dict[str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if target_arn is not None:
                self._values["target_arn"] = target_arn

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''True if notifications to the target are enabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtarget.html#cfn-iot-accountauditconfiguration-auditnotificationtarget-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the role that grants permission to send notifications to the target.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtarget.html#cfn-iot-accountauditconfiguration-auditnotificationtarget-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the target (SNS topic) to which audit notifications are sent.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtarget.html#cfn-iot-accountauditconfiguration-auditnotificationtarget-targetarn
            '''
            result = self._values.get("target_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuditNotificationTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnAccountAuditConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "audit_check_configurations": "auditCheckConfigurations",
        "role_arn": "roleArn",
        "audit_notification_target_configurations": "auditNotificationTargetConfigurations",
    },
)
class CfnAccountAuditConfigurationProps:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        audit_check_configurations: typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        role_arn: builtins.str,
        audit_notification_target_configurations: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccountAuditConfiguration``.

        :param account_id: The ID of the account. You can use the expression ``!Sub "${AWS::AccountId}"`` to use your account ID.
        :param audit_check_configurations: Specifies which audit checks are enabled and disabled for this account. Some data collection might start immediately when certain checks are enabled. When a check is disabled, any data collected so far in relation to the check is deleted. To disable a check, set the value of the ``Enabled:`` key to ``false`` . If an enabled check is removed from the template, it will also be disabled. You can't disable a check if it's used by any scheduled audit. You must delete the check from the scheduled audit or delete the scheduled audit itself to disable the check. For more information on avialbe auidt checks see `AWS::IoT::AccountAuditConfiguration AuditCheckConfigurations <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html>`_
        :param role_arn: The Amazon Resource Name (ARN) of the role that grants permission to AWS IoT to access information about your devices, policies, certificates, and other items as required when performing an audit.
        :param audit_notification_target_configurations: Information about the targets to which audit notifications are sent.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_account_audit_configuration_props = iot.CfnAccountAuditConfigurationProps(
                account_id="accountId",
                audit_check_configurations=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty(
                    authenticated_cognito_role_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    ca_certificate_expiring_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    ca_certificate_key_quality_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    conflicting_client_ids_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    device_certificate_expiring_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    device_certificate_key_quality_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    device_certificate_shared_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    iot_policy_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    iot_role_alias_allows_access_to_unused_services_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    iot_role_alias_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    logging_disabled_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    revoked_ca_certificate_still_active_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    revoked_device_certificate_still_active_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    unauthenticated_cognito_role_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    )
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                audit_notification_target_configurations=iot.CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty(
                    sns=iot.CfnAccountAuditConfiguration.AuditNotificationTargetProperty(
                        enabled=False,
                        role_arn="roleArn",
                        target_arn="targetArn"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAccountAuditConfigurationProps.__init__)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument audit_check_configurations", value=audit_check_configurations, expected_type=type_hints["audit_check_configurations"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument audit_notification_target_configurations", value=audit_notification_target_configurations, expected_type=type_hints["audit_notification_target_configurations"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
            "audit_check_configurations": audit_check_configurations,
            "role_arn": role_arn,
        }
        if audit_notification_target_configurations is not None:
            self._values["audit_notification_target_configurations"] = audit_notification_target_configurations

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The ID of the account.

        You can use the expression ``!Sub "${AWS::AccountId}"`` to use your account ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-accountid
        '''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audit_check_configurations(
        self,
    ) -> typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty, _IResolvable_da3f097b]:
        '''Specifies which audit checks are enabled and disabled for this account.

        Some data collection might start immediately when certain checks are enabled. When a check is disabled, any data collected so far in relation to the check is deleted. To disable a check, set the value of the ``Enabled:`` key to ``false`` .

        If an enabled check is removed from the template, it will also be disabled.

        You can't disable a check if it's used by any scheduled audit. You must delete the check from the scheduled audit or delete the scheduled audit itself to disable the check.

        For more information on avialbe auidt checks see `AWS::IoT::AccountAuditConfiguration AuditCheckConfigurations <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html>`_

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations
        '''
        result = self._values.get("audit_check_configurations")
        assert result is not None, "Required property 'audit_check_configurations' is missing"
        return typing.cast(typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the role that grants permission to AWS IoT to access information about your devices, policies, certificates, and other items as required when performing an audit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audit_notification_target_configurations(
        self,
    ) -> typing.Optional[typing.Union[CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty, _IResolvable_da3f097b]]:
        '''Information about the targets to which audit notifications are sent.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditnotificationtargetconfigurations
        '''
        result = self._values.get("audit_notification_target_configurations")
        return typing.cast(typing.Optional[typing.Union[CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccountAuditConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAuthorizer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnAuthorizer",
):
    '''A CloudFormation ``AWS::IoT::Authorizer``.

    Specifies an authorizer.

    :cloudformationResource: AWS::IoT::Authorizer
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_authorizer = iot.CfnAuthorizer(self, "MyCfnAuthorizer",
            authorizer_function_arn="authorizerFunctionArn",
        
            # the properties below are optional
            authorizer_name="authorizerName",
            enable_caching_for_http=False,
            signing_disabled=False,
            status="status",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            token_key_name="tokenKeyName",
            token_signing_public_keys={
                "token_signing_public_keys_key": "tokenSigningPublicKeys"
            }
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        authorizer_function_arn: builtins.str,
        authorizer_name: typing.Optional[builtins.str] = None,
        enable_caching_for_http: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        signing_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        token_key_name: typing.Optional[builtins.str] = None,
        token_signing_public_keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::Authorizer``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param authorizer_function_arn: The authorizer's Lambda function ARN.
        :param authorizer_name: The authorizer name.
        :param enable_caching_for_http: ``AWS::IoT::Authorizer.EnableCachingForHttp``.
        :param signing_disabled: Specifies whether AWS IoT validates the token signature in an authorization request.
        :param status: The status of the authorizer. Valid values: ``ACTIVE`` | ``INACTIVE``
        :param tags: Metadata which can be used to manage the custom authorizer. .. epigraph:: For URI Request parameters use format: ...key1=value1&key2=value2... For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..." For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
        :param token_key_name: The key used to extract the token from the HTTP headers.
        :param token_signing_public_keys: The public keys used to validate the token signature returned by your custom authentication service.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAuthorizer.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAuthorizerProps(
            authorizer_function_arn=authorizer_function_arn,
            authorizer_name=authorizer_name,
            enable_caching_for_http=enable_caching_for_http,
            signing_disabled=signing_disabled,
            status=status,
            tags=tags,
            token_key_name=token_key_name,
            token_signing_public_keys=token_signing_public_keys,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAuthorizer.inspect)
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
            type_hints = typing.get_type_hints(CfnAuthorizer._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the authorizer.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata which can be used to manage the custom authorizer.

        .. epigraph::

           For URI Request parameters use format: ...key1=value1&key2=value2...

           For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."

           For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="authorizerFunctionArn")
    def authorizer_function_arn(self) -> builtins.str:
        '''The authorizer's Lambda function ARN.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-authorizerfunctionarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "authorizerFunctionArn"))

    @authorizer_function_arn.setter
    def authorizer_function_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAuthorizer, "authorizer_function_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerFunctionArn", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerName")
    def authorizer_name(self) -> typing.Optional[builtins.str]:
        '''The authorizer name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-authorizername
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerName"))

    @authorizer_name.setter
    def authorizer_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAuthorizer, "authorizer_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerName", value)

    @builtins.property
    @jsii.member(jsii_name="enableCachingForHttp")
    def enable_caching_for_http(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::IoT::Authorizer.EnableCachingForHttp``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-enablecachingforhttp
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableCachingForHttp"))

    @enable_caching_for_http.setter
    def enable_caching_for_http(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAuthorizer, "enable_caching_for_http").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableCachingForHttp", value)

    @builtins.property
    @jsii.member(jsii_name="signingDisabled")
    def signing_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether AWS IoT validates the token signature in an authorization request.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-signingdisabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "signingDisabled"))

    @signing_disabled.setter
    def signing_disabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAuthorizer, "signing_disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signingDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the authorizer.

        Valid values: ``ACTIVE`` | ``INACTIVE``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAuthorizer, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="tokenKeyName")
    def token_key_name(self) -> typing.Optional[builtins.str]:
        '''The key used to extract the token from the HTTP headers.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-tokenkeyname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKeyName"))

    @token_key_name.setter
    def token_key_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAuthorizer, "token_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="tokenSigningPublicKeys")
    def token_signing_public_keys(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''The public keys used to validate the token signature returned by your custom authentication service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-tokensigningpublickeys
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "tokenSigningPublicKeys"))

    @token_signing_public_keys.setter
    def token_signing_public_keys(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnAuthorizer, "token_signing_public_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenSigningPublicKeys", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnAuthorizerProps",
    jsii_struct_bases=[],
    name_mapping={
        "authorizer_function_arn": "authorizerFunctionArn",
        "authorizer_name": "authorizerName",
        "enable_caching_for_http": "enableCachingForHttp",
        "signing_disabled": "signingDisabled",
        "status": "status",
        "tags": "tags",
        "token_key_name": "tokenKeyName",
        "token_signing_public_keys": "tokenSigningPublicKeys",
    },
)
class CfnAuthorizerProps:
    def __init__(
        self,
        *,
        authorizer_function_arn: builtins.str,
        authorizer_name: typing.Optional[builtins.str] = None,
        enable_caching_for_http: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        signing_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        token_key_name: typing.Optional[builtins.str] = None,
        token_signing_public_keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAuthorizer``.

        :param authorizer_function_arn: The authorizer's Lambda function ARN.
        :param authorizer_name: The authorizer name.
        :param enable_caching_for_http: ``AWS::IoT::Authorizer.EnableCachingForHttp``.
        :param signing_disabled: Specifies whether AWS IoT validates the token signature in an authorization request.
        :param status: The status of the authorizer. Valid values: ``ACTIVE`` | ``INACTIVE``
        :param tags: Metadata which can be used to manage the custom authorizer. .. epigraph:: For URI Request parameters use format: ...key1=value1&key2=value2... For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..." For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
        :param token_key_name: The key used to extract the token from the HTTP headers.
        :param token_signing_public_keys: The public keys used to validate the token signature returned by your custom authentication service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_authorizer_props = iot.CfnAuthorizerProps(
                authorizer_function_arn="authorizerFunctionArn",
            
                # the properties below are optional
                authorizer_name="authorizerName",
                enable_caching_for_http=False,
                signing_disabled=False,
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                token_key_name="tokenKeyName",
                token_signing_public_keys={
                    "token_signing_public_keys_key": "tokenSigningPublicKeys"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnAuthorizerProps.__init__)
            check_type(argname="argument authorizer_function_arn", value=authorizer_function_arn, expected_type=type_hints["authorizer_function_arn"])
            check_type(argname="argument authorizer_name", value=authorizer_name, expected_type=type_hints["authorizer_name"])
            check_type(argname="argument enable_caching_for_http", value=enable_caching_for_http, expected_type=type_hints["enable_caching_for_http"])
            check_type(argname="argument signing_disabled", value=signing_disabled, expected_type=type_hints["signing_disabled"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument token_key_name", value=token_key_name, expected_type=type_hints["token_key_name"])
            check_type(argname="argument token_signing_public_keys", value=token_signing_public_keys, expected_type=type_hints["token_signing_public_keys"])
        self._values: typing.Dict[str, typing.Any] = {
            "authorizer_function_arn": authorizer_function_arn,
        }
        if authorizer_name is not None:
            self._values["authorizer_name"] = authorizer_name
        if enable_caching_for_http is not None:
            self._values["enable_caching_for_http"] = enable_caching_for_http
        if signing_disabled is not None:
            self._values["signing_disabled"] = signing_disabled
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags
        if token_key_name is not None:
            self._values["token_key_name"] = token_key_name
        if token_signing_public_keys is not None:
            self._values["token_signing_public_keys"] = token_signing_public_keys

    @builtins.property
    def authorizer_function_arn(self) -> builtins.str:
        '''The authorizer's Lambda function ARN.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-authorizerfunctionarn
        '''
        result = self._values.get("authorizer_function_arn")
        assert result is not None, "Required property 'authorizer_function_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_name(self) -> typing.Optional[builtins.str]:
        '''The authorizer name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-authorizername
        '''
        result = self._values.get("authorizer_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_caching_for_http(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::IoT::Authorizer.EnableCachingForHttp``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-enablecachingforhttp
        '''
        result = self._values.get("enable_caching_for_http")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def signing_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether AWS IoT validates the token signature in an authorization request.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-signingdisabled
        '''
        result = self._values.get("signing_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the authorizer.

        Valid values: ``ACTIVE`` | ``INACTIVE``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata which can be used to manage the custom authorizer.

        .. epigraph::

           For URI Request parameters use format: ...key1=value1&key2=value2...

           For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."

           For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def token_key_name(self) -> typing.Optional[builtins.str]:
        '''The key used to extract the token from the HTTP headers.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-tokenkeyname
        '''
        result = self._values.get("token_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_signing_public_keys(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''The public keys used to validate the token signature returned by your custom authentication service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-tokensigningpublickeys
        '''
        result = self._values.get("token_signing_public_keys")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAuthorizerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnCACertificate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnCACertificate",
):
    '''A CloudFormation ``AWS::IoT::CACertificate``.

    :cloudformationResource: AWS::IoT::CACertificate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_cACertificate = iot.CfnCACertificate(self, "MyCfnCACertificate",
            ca_certificate_pem="caCertificatePem",
            status="status",
        
            # the properties below are optional
            auto_registration_status="autoRegistrationStatus",
            certificate_mode="certificateMode",
            registration_config=iot.CfnCACertificate.RegistrationConfigProperty(
                role_arn="roleArn",
                template_body="templateBody",
                template_name="templateName"
            ),
            remove_auto_registration=False,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            verification_certificate_pem="verificationCertificatePem"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        ca_certificate_pem: builtins.str,
        status: builtins.str,
        auto_registration_status: typing.Optional[builtins.str] = None,
        certificate_mode: typing.Optional[builtins.str] = None,
        registration_config: typing.Optional[typing.Union[typing.Union["CfnCACertificate.RegistrationConfigProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        remove_auto_registration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        verification_certificate_pem: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::CACertificate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param ca_certificate_pem: ``AWS::IoT::CACertificate.CACertificatePem``.
        :param status: ``AWS::IoT::CACertificate.Status``.
        :param auto_registration_status: ``AWS::IoT::CACertificate.AutoRegistrationStatus``.
        :param certificate_mode: ``AWS::IoT::CACertificate.CertificateMode``.
        :param registration_config: ``AWS::IoT::CACertificate.RegistrationConfig``.
        :param remove_auto_registration: ``AWS::IoT::CACertificate.RemoveAutoRegistration``.
        :param tags: ``AWS::IoT::CACertificate.Tags``.
        :param verification_certificate_pem: ``AWS::IoT::CACertificate.VerificationCertificatePem``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCACertificate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCACertificateProps(
            ca_certificate_pem=ca_certificate_pem,
            status=status,
            auto_registration_status=auto_registration_status,
            certificate_mode=certificate_mode,
            registration_config=registration_config,
            remove_auto_registration=remove_auto_registration,
            tags=tags,
            verification_certificate_pem=verification_certificate_pem,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCACertificate.inspect)
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
            type_hints = typing.get_type_hints(CfnCACertificate._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::IoT::CACertificate.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="caCertificatePem")
    def ca_certificate_pem(self) -> builtins.str:
        '''``AWS::IoT::CACertificate.CACertificatePem``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-cacertificatepem
        '''
        return typing.cast(builtins.str, jsii.get(self, "caCertificatePem"))

    @ca_certificate_pem.setter
    def ca_certificate_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCACertificate, "ca_certificate_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCertificatePem", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        '''``AWS::IoT::CACertificate.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-status
        '''
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCACertificate, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="autoRegistrationStatus")
    def auto_registration_status(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoT::CACertificate.AutoRegistrationStatus``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-autoregistrationstatus
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoRegistrationStatus"))

    @auto_registration_status.setter
    def auto_registration_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCACertificate, "auto_registration_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoRegistrationStatus", value)

    @builtins.property
    @jsii.member(jsii_name="certificateMode")
    def certificate_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoT::CACertificate.CertificateMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-certificatemode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateMode"))

    @certificate_mode.setter
    def certificate_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCACertificate, "certificate_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateMode", value)

    @builtins.property
    @jsii.member(jsii_name="registrationConfig")
    def registration_config(
        self,
    ) -> typing.Optional[typing.Union["CfnCACertificate.RegistrationConfigProperty", _IResolvable_da3f097b]]:
        '''``AWS::IoT::CACertificate.RegistrationConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-registrationconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnCACertificate.RegistrationConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "registrationConfig"))

    @registration_config.setter
    def registration_config(
        self,
        value: typing.Optional[typing.Union["CfnCACertificate.RegistrationConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCACertificate, "registration_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registrationConfig", value)

    @builtins.property
    @jsii.member(jsii_name="removeAutoRegistration")
    def remove_auto_registration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::IoT::CACertificate.RemoveAutoRegistration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-removeautoregistration
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "removeAutoRegistration"))

    @remove_auto_registration.setter
    def remove_auto_registration(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCACertificate, "remove_auto_registration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "removeAutoRegistration", value)

    @builtins.property
    @jsii.member(jsii_name="verificationCertificatePem")
    def verification_certificate_pem(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoT::CACertificate.VerificationCertificatePem``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-verificationcertificatepem
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "verificationCertificatePem"))

    @verification_certificate_pem.setter
    def verification_certificate_pem(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCACertificate, "verification_certificate_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verificationCertificatePem", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnCACertificate.RegistrationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "template_body": "templateBody",
            "template_name": "templateName",
        },
    )
    class RegistrationConfigProperty:
        def __init__(
            self,
            *,
            role_arn: typing.Optional[builtins.str] = None,
            template_body: typing.Optional[builtins.str] = None,
            template_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param role_arn: ``CfnCACertificate.RegistrationConfigProperty.RoleArn``.
            :param template_body: ``CfnCACertificate.RegistrationConfigProperty.TemplateBody``.
            :param template_name: ``CfnCACertificate.RegistrationConfigProperty.TemplateName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-cacertificate-registrationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                registration_config_property = iot.CfnCACertificate.RegistrationConfigProperty(
                    role_arn="roleArn",
                    template_body="templateBody",
                    template_name="templateName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCACertificate.RegistrationConfigProperty.__init__)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument template_body", value=template_body, expected_type=type_hints["template_body"])
                check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
            self._values: typing.Dict[str, typing.Any] = {}
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if template_body is not None:
                self._values["template_body"] = template_body
            if template_name is not None:
                self._values["template_name"] = template_name

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnCACertificate.RegistrationConfigProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-cacertificate-registrationconfig.html#cfn-iot-cacertificate-registrationconfig-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def template_body(self) -> typing.Optional[builtins.str]:
            '''``CfnCACertificate.RegistrationConfigProperty.TemplateBody``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-cacertificate-registrationconfig.html#cfn-iot-cacertificate-registrationconfig-templatebody
            '''
            result = self._values.get("template_body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def template_name(self) -> typing.Optional[builtins.str]:
            '''``CfnCACertificate.RegistrationConfigProperty.TemplateName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-cacertificate-registrationconfig.html#cfn-iot-cacertificate-registrationconfig-templatename
            '''
            result = self._values.get("template_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegistrationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnCACertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "ca_certificate_pem": "caCertificatePem",
        "status": "status",
        "auto_registration_status": "autoRegistrationStatus",
        "certificate_mode": "certificateMode",
        "registration_config": "registrationConfig",
        "remove_auto_registration": "removeAutoRegistration",
        "tags": "tags",
        "verification_certificate_pem": "verificationCertificatePem",
    },
)
class CfnCACertificateProps:
    def __init__(
        self,
        *,
        ca_certificate_pem: builtins.str,
        status: builtins.str,
        auto_registration_status: typing.Optional[builtins.str] = None,
        certificate_mode: typing.Optional[builtins.str] = None,
        registration_config: typing.Optional[typing.Union[typing.Union[CfnCACertificate.RegistrationConfigProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        remove_auto_registration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        verification_certificate_pem: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCACertificate``.

        :param ca_certificate_pem: ``AWS::IoT::CACertificate.CACertificatePem``.
        :param status: ``AWS::IoT::CACertificate.Status``.
        :param auto_registration_status: ``AWS::IoT::CACertificate.AutoRegistrationStatus``.
        :param certificate_mode: ``AWS::IoT::CACertificate.CertificateMode``.
        :param registration_config: ``AWS::IoT::CACertificate.RegistrationConfig``.
        :param remove_auto_registration: ``AWS::IoT::CACertificate.RemoveAutoRegistration``.
        :param tags: ``AWS::IoT::CACertificate.Tags``.
        :param verification_certificate_pem: ``AWS::IoT::CACertificate.VerificationCertificatePem``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_cACertificate_props = iot.CfnCACertificateProps(
                ca_certificate_pem="caCertificatePem",
                status="status",
            
                # the properties below are optional
                auto_registration_status="autoRegistrationStatus",
                certificate_mode="certificateMode",
                registration_config=iot.CfnCACertificate.RegistrationConfigProperty(
                    role_arn="roleArn",
                    template_body="templateBody",
                    template_name="templateName"
                ),
                remove_auto_registration=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                verification_certificate_pem="verificationCertificatePem"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCACertificateProps.__init__)
            check_type(argname="argument ca_certificate_pem", value=ca_certificate_pem, expected_type=type_hints["ca_certificate_pem"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument auto_registration_status", value=auto_registration_status, expected_type=type_hints["auto_registration_status"])
            check_type(argname="argument certificate_mode", value=certificate_mode, expected_type=type_hints["certificate_mode"])
            check_type(argname="argument registration_config", value=registration_config, expected_type=type_hints["registration_config"])
            check_type(argname="argument remove_auto_registration", value=remove_auto_registration, expected_type=type_hints["remove_auto_registration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument verification_certificate_pem", value=verification_certificate_pem, expected_type=type_hints["verification_certificate_pem"])
        self._values: typing.Dict[str, typing.Any] = {
            "ca_certificate_pem": ca_certificate_pem,
            "status": status,
        }
        if auto_registration_status is not None:
            self._values["auto_registration_status"] = auto_registration_status
        if certificate_mode is not None:
            self._values["certificate_mode"] = certificate_mode
        if registration_config is not None:
            self._values["registration_config"] = registration_config
        if remove_auto_registration is not None:
            self._values["remove_auto_registration"] = remove_auto_registration
        if tags is not None:
            self._values["tags"] = tags
        if verification_certificate_pem is not None:
            self._values["verification_certificate_pem"] = verification_certificate_pem

    @builtins.property
    def ca_certificate_pem(self) -> builtins.str:
        '''``AWS::IoT::CACertificate.CACertificatePem``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-cacertificatepem
        '''
        result = self._values.get("ca_certificate_pem")
        assert result is not None, "Required property 'ca_certificate_pem' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> builtins.str:
        '''``AWS::IoT::CACertificate.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-status
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_registration_status(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoT::CACertificate.AutoRegistrationStatus``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-autoregistrationstatus
        '''
        result = self._values.get("auto_registration_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoT::CACertificate.CertificateMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-certificatemode
        '''
        result = self._values.get("certificate_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registration_config(
        self,
    ) -> typing.Optional[typing.Union[CfnCACertificate.RegistrationConfigProperty, _IResolvable_da3f097b]]:
        '''``AWS::IoT::CACertificate.RegistrationConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-registrationconfig
        '''
        result = self._values.get("registration_config")
        return typing.cast(typing.Optional[typing.Union[CfnCACertificate.RegistrationConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def remove_auto_registration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::IoT::CACertificate.RemoveAutoRegistration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-removeautoregistration
        '''
        result = self._values.get("remove_auto_registration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::IoT::CACertificate.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def verification_certificate_pem(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoT::CACertificate.VerificationCertificatePem``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-verificationcertificatepem
        '''
        result = self._values.get("verification_certificate_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCACertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnCertificate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnCertificate",
):
    '''A CloudFormation ``AWS::IoT::Certificate``.

    Use the ``AWS::IoT::Certificate`` resource to declare an AWS IoT X.509 certificate. For information about working with X.509 certificates, see `X.509 Client Certificates <https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html>`_ in the *AWS IoT Developer Guide* .

    :cloudformationResource: AWS::IoT::Certificate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_certificate = iot.CfnCertificate(self, "MyCfnCertificate",
            status="status",
        
            # the properties below are optional
            ca_certificate_pem="caCertificatePem",
            certificate_mode="certificateMode",
            certificate_pem="certificatePem",
            certificate_signing_request="certificateSigningRequest"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        status: builtins.str,
        ca_certificate_pem: typing.Optional[builtins.str] = None,
        certificate_mode: typing.Optional[builtins.str] = None,
        certificate_pem: typing.Optional[builtins.str] = None,
        certificate_signing_request: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::Certificate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param status: The status of the certificate. Valid values are ACTIVE, INACTIVE, REVOKED, PENDING_TRANSFER, and PENDING_ACTIVATION. The status value REGISTER_INACTIVE is deprecated and should not be used.
        :param ca_certificate_pem: The CA certificate used to sign the device certificate being registered, not available when CertificateMode is SNI_ONLY.
        :param certificate_mode: Specifies which mode of certificate registration to use with this resource. Valid options are DEFAULT with CaCertificatePem and CertificatePem, SNI_ONLY with CertificatePem, and Default with CertificateSigningRequest.
        :param certificate_pem: The certificate data in PEM format. Requires SNI_ONLY for the certificate mode or the accompanying CACertificatePem for registration.
        :param certificate_signing_request: The certificate signing request (CSR).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCertificate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCertificateProps(
            status=status,
            ca_certificate_pem=ca_certificate_pem,
            certificate_mode=certificate_mode,
            certificate_pem=certificate_pem,
            certificate_signing_request=certificate_signing_request,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCertificate.inspect)
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
            type_hints = typing.get_type_hints(CfnCertificate._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) for the instance profile. For example:.

        ``{ "Fn::GetAtt": ["MyCertificate", "Arn"] }``

        A value similar to the following is returned:

        ``arn:aws:iot:ap-southeast-2:123456789012:cert/a1234567b89c012d3e4fg567hij8k9l01mno1p23q45678901rs234567890t1u2``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The certificate ID.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        '''The status of the certificate.

        Valid values are ACTIVE, INACTIVE, REVOKED, PENDING_TRANSFER, and PENDING_ACTIVATION.

        The status value REGISTER_INACTIVE is deprecated and should not be used.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-status
        '''
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCertificate, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="caCertificatePem")
    def ca_certificate_pem(self) -> typing.Optional[builtins.str]:
        '''The CA certificate used to sign the device certificate being registered, not available when CertificateMode is SNI_ONLY.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-cacertificatepem
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertificatePem"))

    @ca_certificate_pem.setter
    def ca_certificate_pem(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCertificate, "ca_certificate_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCertificatePem", value)

    @builtins.property
    @jsii.member(jsii_name="certificateMode")
    def certificate_mode(self) -> typing.Optional[builtins.str]:
        '''Specifies which mode of certificate registration to use with this resource.

        Valid options are DEFAULT with CaCertificatePem and CertificatePem, SNI_ONLY with CertificatePem, and Default with CertificateSigningRequest.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-certificatemode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateMode"))

    @certificate_mode.setter
    def certificate_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCertificate, "certificate_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateMode", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePem")
    def certificate_pem(self) -> typing.Optional[builtins.str]:
        '''The certificate data in PEM format.

        Requires SNI_ONLY for the certificate mode or the accompanying CACertificatePem for registration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-certificatepem
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePem"))

    @certificate_pem.setter
    def certificate_pem(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCertificate, "certificate_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePem", value)

    @builtins.property
    @jsii.member(jsii_name="certificateSigningRequest")
    def certificate_signing_request(self) -> typing.Optional[builtins.str]:
        '''The certificate signing request (CSR).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-certificatesigningrequest
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateSigningRequest"))

    @certificate_signing_request.setter
    def certificate_signing_request(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCertificate, "certificate_signing_request").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateSigningRequest", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnCertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "status": "status",
        "ca_certificate_pem": "caCertificatePem",
        "certificate_mode": "certificateMode",
        "certificate_pem": "certificatePem",
        "certificate_signing_request": "certificateSigningRequest",
    },
)
class CfnCertificateProps:
    def __init__(
        self,
        *,
        status: builtins.str,
        ca_certificate_pem: typing.Optional[builtins.str] = None,
        certificate_mode: typing.Optional[builtins.str] = None,
        certificate_pem: typing.Optional[builtins.str] = None,
        certificate_signing_request: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCertificate``.

        :param status: The status of the certificate. Valid values are ACTIVE, INACTIVE, REVOKED, PENDING_TRANSFER, and PENDING_ACTIVATION. The status value REGISTER_INACTIVE is deprecated and should not be used.
        :param ca_certificate_pem: The CA certificate used to sign the device certificate being registered, not available when CertificateMode is SNI_ONLY.
        :param certificate_mode: Specifies which mode of certificate registration to use with this resource. Valid options are DEFAULT with CaCertificatePem and CertificatePem, SNI_ONLY with CertificatePem, and Default with CertificateSigningRequest.
        :param certificate_pem: The certificate data in PEM format. Requires SNI_ONLY for the certificate mode or the accompanying CACertificatePem for registration.
        :param certificate_signing_request: The certificate signing request (CSR).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_certificate_props = iot.CfnCertificateProps(
                status="status",
            
                # the properties below are optional
                ca_certificate_pem="caCertificatePem",
                certificate_mode="certificateMode",
                certificate_pem="certificatePem",
                certificate_signing_request="certificateSigningRequest"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCertificateProps.__init__)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument ca_certificate_pem", value=ca_certificate_pem, expected_type=type_hints["ca_certificate_pem"])
            check_type(argname="argument certificate_mode", value=certificate_mode, expected_type=type_hints["certificate_mode"])
            check_type(argname="argument certificate_pem", value=certificate_pem, expected_type=type_hints["certificate_pem"])
            check_type(argname="argument certificate_signing_request", value=certificate_signing_request, expected_type=type_hints["certificate_signing_request"])
        self._values: typing.Dict[str, typing.Any] = {
            "status": status,
        }
        if ca_certificate_pem is not None:
            self._values["ca_certificate_pem"] = ca_certificate_pem
        if certificate_mode is not None:
            self._values["certificate_mode"] = certificate_mode
        if certificate_pem is not None:
            self._values["certificate_pem"] = certificate_pem
        if certificate_signing_request is not None:
            self._values["certificate_signing_request"] = certificate_signing_request

    @builtins.property
    def status(self) -> builtins.str:
        '''The status of the certificate.

        Valid values are ACTIVE, INACTIVE, REVOKED, PENDING_TRANSFER, and PENDING_ACTIVATION.

        The status value REGISTER_INACTIVE is deprecated and should not be used.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-status
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ca_certificate_pem(self) -> typing.Optional[builtins.str]:
        '''The CA certificate used to sign the device certificate being registered, not available when CertificateMode is SNI_ONLY.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-cacertificatepem
        '''
        result = self._values.get("ca_certificate_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_mode(self) -> typing.Optional[builtins.str]:
        '''Specifies which mode of certificate registration to use with this resource.

        Valid options are DEFAULT with CaCertificatePem and CertificatePem, SNI_ONLY with CertificatePem, and Default with CertificateSigningRequest.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-certificatemode
        '''
        result = self._values.get("certificate_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_pem(self) -> typing.Optional[builtins.str]:
        '''The certificate data in PEM format.

        Requires SNI_ONLY for the certificate mode or the accompanying CACertificatePem for registration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-certificatepem
        '''
        result = self._values.get("certificate_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_signing_request(self) -> typing.Optional[builtins.str]:
        '''The certificate signing request (CSR).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-certificatesigningrequest
        '''
        result = self._values.get("certificate_signing_request")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnCustomMetric(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnCustomMetric",
):
    '''A CloudFormation ``AWS::IoT::CustomMetric``.

    Use the ``AWS::IoT::CustomMetric`` resource to define a custom metric published by your devices to Device Defender. For API reference, see `CreateCustomMetric <https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCustomMetric.html>`_ and for general information, see `Custom metrics <https://docs.aws.amazon.com/iot/latest/developerguide/dd-detect-custom-metrics.html>`_ .

    :cloudformationResource: AWS::IoT::CustomMetric
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_custom_metric = iot.CfnCustomMetric(self, "MyCfnCustomMetric",
            metric_type="metricType",
        
            # the properties below are optional
            display_name="displayName",
            metric_name="metricName",
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
        metric_type: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        metric_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::CustomMetric``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param metric_type: The type of the custom metric. Types include ``string-list`` , ``ip-address-list`` , ``number-list`` , and ``number`` . .. epigraph:: The type ``number`` only takes a single metric value as an input, but when you submit the metrics value in the DeviceMetrics report, you must pass it as an array with a single value.
        :param display_name: The friendly name in the console for the custom metric. This name doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. You can update the friendly name after you define it.
        :param metric_name: The name of the custom metric. This will be used in the metric report submitted from the device/thing. The name can't begin with ``aws:`` . You can’t change the name after you define it.
        :param tags: Metadata that can be used to manage the custom metric.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCustomMetric.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCustomMetricProps(
            metric_type=metric_type,
            display_name=display_name,
            metric_name=metric_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCustomMetric.inspect)
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
            type_hints = typing.get_type_hints(CfnCustomMetric._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrMetricArn")
    def attr_metric_arn(self) -> builtins.str:
        '''The Amazon Resource Number (ARN) of the custom metric;

        for example, ``arn: *aws-partition* :iot: *region* : *accountId* :custommetric/ *metricName*`` .

        :cloudformationAttribute: MetricArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMetricArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata that can be used to manage the custom metric.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="metricType")
    def metric_type(self) -> builtins.str:
        '''The type of the custom metric. Types include ``string-list`` , ``ip-address-list`` , ``number-list`` , and ``number`` .

        .. epigraph::

           The type ``number`` only takes a single metric value as an input, but when you submit the metrics value in the DeviceMetrics report, you must pass it as an array with a single value.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-metrictype
        '''
        return typing.cast(builtins.str, jsii.get(self, "metricType"))

    @metric_type.setter
    def metric_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCustomMetric, "metric_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricType", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The friendly name in the console for the custom metric.

        This name doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. You can update the friendly name after you define it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-displayname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCustomMetric, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> typing.Optional[builtins.str]:
        '''The name of the custom metric.

        This will be used in the metric report submitted from the device/thing. The name can't begin with ``aws:`` . You can’t change the name after you define it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-metricname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCustomMetric, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnCustomMetricProps",
    jsii_struct_bases=[],
    name_mapping={
        "metric_type": "metricType",
        "display_name": "displayName",
        "metric_name": "metricName",
        "tags": "tags",
    },
)
class CfnCustomMetricProps:
    def __init__(
        self,
        *,
        metric_type: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        metric_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCustomMetric``.

        :param metric_type: The type of the custom metric. Types include ``string-list`` , ``ip-address-list`` , ``number-list`` , and ``number`` . .. epigraph:: The type ``number`` only takes a single metric value as an input, but when you submit the metrics value in the DeviceMetrics report, you must pass it as an array with a single value.
        :param display_name: The friendly name in the console for the custom metric. This name doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. You can update the friendly name after you define it.
        :param metric_name: The name of the custom metric. This will be used in the metric report submitted from the device/thing. The name can't begin with ``aws:`` . You can’t change the name after you define it.
        :param tags: Metadata that can be used to manage the custom metric.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_custom_metric_props = iot.CfnCustomMetricProps(
                metric_type="metricType",
            
                # the properties below are optional
                display_name="displayName",
                metric_name="metricName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCustomMetricProps.__init__)
            check_type(argname="argument metric_type", value=metric_type, expected_type=type_hints["metric_type"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_type": metric_type,
        }
        if display_name is not None:
            self._values["display_name"] = display_name
        if metric_name is not None:
            self._values["metric_name"] = metric_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def metric_type(self) -> builtins.str:
        '''The type of the custom metric. Types include ``string-list`` , ``ip-address-list`` , ``number-list`` , and ``number`` .

        .. epigraph::

           The type ``number`` only takes a single metric value as an input, but when you submit the metrics value in the DeviceMetrics report, you must pass it as an array with a single value.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-metrictype
        '''
        result = self._values.get("metric_type")
        assert result is not None, "Required property 'metric_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The friendly name in the console for the custom metric.

        This name doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. You can update the friendly name after you define it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_name(self) -> typing.Optional[builtins.str]:
        '''The name of the custom metric.

        This will be used in the metric report submitted from the device/thing. The name can't begin with ``aws:`` . You can’t change the name after you define it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-metricname
        '''
        result = self._values.get("metric_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata that can be used to manage the custom metric.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomMetricProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDimension(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnDimension",
):
    '''A CloudFormation ``AWS::IoT::Dimension``.

    Use the ``AWS::IoT::Dimension`` to limit the scope of a metric used in a security profile for AWS IoT Device Defender . For example, using a ``TOPIC_FILTER`` dimension, you can narrow down the scope of the metric to only MQTT topics where the name matches the pattern specified in the dimension. For API reference, see `CreateDimension <https://docs.aws.amazon.com/iot/latest/apireference/API_CreateDimension.html>`_ and for general information, see `Scoping metrics in security profiles using dimensions <https://docs.aws.amazon.com/iot/latest/developerguide/scoping-security-behavior.html>`_ .

    :cloudformationResource: AWS::IoT::Dimension
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_dimension = iot.CfnDimension(self, "MyCfnDimension",
            string_values=["stringValues"],
            type="type",
        
            # the properties below are optional
            name="name",
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
        string_values: typing.Sequence[builtins.str],
        type: builtins.str,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::Dimension``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param string_values: Specifies the value or list of values for the dimension. For ``TOPIC_FILTER`` dimensions, this is a pattern used to match the MQTT topic (for example, "admin/#").
        :param type: Specifies the type of dimension. Supported types: ``TOPIC_FILTER.``
        :param name: A unique identifier for the dimension.
        :param tags: Metadata that can be used to manage the dimension.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDimension.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDimensionProps(
            string_values=string_values, type=type, name=name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDimension.inspect)
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
            type_hints = typing.get_type_hints(CfnDimension._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the dimension.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata that can be used to manage the dimension.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="stringValues")
    def string_values(self) -> typing.List[builtins.str]:
        '''Specifies the value or list of values for the dimension.

        For ``TOPIC_FILTER`` dimensions, this is a pattern used to match the MQTT topic (for example, "admin/#").

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-stringvalues
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringValues"))

    @string_values.setter
    def string_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDimension, "string_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringValues", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''Specifies the type of dimension.

        Supported types: ``TOPIC_FILTER.``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDimension, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the dimension.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDimension, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnDimensionProps",
    jsii_struct_bases=[],
    name_mapping={
        "string_values": "stringValues",
        "type": "type",
        "name": "name",
        "tags": "tags",
    },
)
class CfnDimensionProps:
    def __init__(
        self,
        *,
        string_values: typing.Sequence[builtins.str],
        type: builtins.str,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDimension``.

        :param string_values: Specifies the value or list of values for the dimension. For ``TOPIC_FILTER`` dimensions, this is a pattern used to match the MQTT topic (for example, "admin/#").
        :param type: Specifies the type of dimension. Supported types: ``TOPIC_FILTER.``
        :param name: A unique identifier for the dimension.
        :param tags: Metadata that can be used to manage the dimension.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_dimension_props = iot.CfnDimensionProps(
                string_values=["stringValues"],
                type="type",
            
                # the properties below are optional
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDimensionProps.__init__)
            check_type(argname="argument string_values", value=string_values, expected_type=type_hints["string_values"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "string_values": string_values,
            "type": type,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def string_values(self) -> typing.List[builtins.str]:
        '''Specifies the value or list of values for the dimension.

        For ``TOPIC_FILTER`` dimensions, this is a pattern used to match the MQTT topic (for example, "admin/#").

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-stringvalues
        '''
        result = self._values.get("string_values")
        assert result is not None, "Required property 'string_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Specifies the type of dimension.

        Supported types: ``TOPIC_FILTER.``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the dimension.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata that can be used to manage the dimension.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDimensionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDomainConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnDomainConfiguration",
):
    '''A CloudFormation ``AWS::IoT::DomainConfiguration``.

    Specifies a domain configuration.

    :cloudformationResource: AWS::IoT::DomainConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_domain_configuration = iot.CfnDomainConfiguration(self, "MyCfnDomainConfiguration",
            authorizer_config=iot.CfnDomainConfiguration.AuthorizerConfigProperty(
                allow_authorizer_override=False,
                default_authorizer_name="defaultAuthorizerName"
            ),
            domain_configuration_name="domainConfigurationName",
            domain_configuration_status="domainConfigurationStatus",
            domain_name="domainName",
            server_certificate_arns=["serverCertificateArns"],
            service_type="serviceType",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            validation_certificate_arn="validationCertificateArn"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        authorizer_config: typing.Optional[typing.Union[typing.Union["CfnDomainConfiguration.AuthorizerConfigProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        domain_configuration_name: typing.Optional[builtins.str] = None,
        domain_configuration_status: typing.Optional[builtins.str] = None,
        domain_name: typing.Optional[builtins.str] = None,
        server_certificate_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        validation_certificate_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::DomainConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param authorizer_config: An object that specifies the authorization service for a domain.
        :param domain_configuration_name: The name of the domain configuration. This value must be unique to a region.
        :param domain_configuration_status: The status to which the domain configuration should be updated. Valid values: ``ENABLED`` | ``DISABLED``
        :param domain_name: The name of the domain.
        :param server_certificate_arns: The ARNs of the certificates that AWS IoT passes to the device during the TLS handshake. Currently you can specify only one certificate ARN. This value is not required for AWS -managed domains.
        :param service_type: The type of service delivered by the endpoint. .. epigraph:: AWS IoT Core currently supports only the ``DATA`` service type.
        :param tags: Metadata which can be used to manage the domain configuration. .. epigraph:: For URI Request parameters use format: ...key1=value1&key2=value2... For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..." For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
        :param validation_certificate_arn: The certificate used to validate the server certificate and prove domain name ownership. This certificate must be signed by a public certificate authority. This value is not required for AWS -managed domains.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDomainConfiguration.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainConfigurationProps(
            authorizer_config=authorizer_config,
            domain_configuration_name=domain_configuration_name,
            domain_configuration_status=domain_configuration_status,
            domain_name=domain_name,
            server_certificate_arns=server_certificate_arns,
            service_type=service_type,
            tags=tags,
            validation_certificate_arn=validation_certificate_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDomainConfiguration.inspect)
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
            type_hints = typing.get_type_hints(CfnDomainConfiguration._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the domain configuration.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainType")
    def attr_domain_type(self) -> builtins.str:
        '''The type of service delivered by the domain.

        :cloudformationAttribute: DomainType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainType"))

    @builtins.property
    @jsii.member(jsii_name="attrServerCertificates")
    def attr_server_certificates(self) -> _IResolvable_da3f097b:
        '''The ARNs of the certificates that AWS IoT passes to the device during the TLS handshake.

        Currently you can specify only one certificate ARN. This value is not required for AWS -managed domains.

        :cloudformationAttribute: ServerCertificates
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrServerCertificates"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata which can be used to manage the domain configuration.

        .. epigraph::

           For URI Request parameters use format: ...key1=value1&key2=value2...

           For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."

           For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="authorizerConfig")
    def authorizer_config(
        self,
    ) -> typing.Optional[typing.Union["CfnDomainConfiguration.AuthorizerConfigProperty", _IResolvable_da3f097b]]:
        '''An object that specifies the authorization service for a domain.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-authorizerconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDomainConfiguration.AuthorizerConfigProperty", _IResolvable_da3f097b]], jsii.get(self, "authorizerConfig"))

    @authorizer_config.setter
    def authorizer_config(
        self,
        value: typing.Optional[typing.Union["CfnDomainConfiguration.AuthorizerConfigProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDomainConfiguration, "authorizer_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerConfig", value)

    @builtins.property
    @jsii.member(jsii_name="domainConfigurationName")
    def domain_configuration_name(self) -> typing.Optional[builtins.str]:
        '''The name of the domain configuration.

        This value must be unique to a region.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-domainconfigurationname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainConfigurationName"))

    @domain_configuration_name.setter
    def domain_configuration_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDomainConfiguration, "domain_configuration_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="domainConfigurationStatus")
    def domain_configuration_status(self) -> typing.Optional[builtins.str]:
        '''The status to which the domain configuration should be updated.

        Valid values: ``ENABLED`` | ``DISABLED``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-domainconfigurationstatus
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainConfigurationStatus"))

    @domain_configuration_status.setter
    def domain_configuration_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDomainConfiguration, "domain_configuration_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainConfigurationStatus", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''The name of the domain.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-domainname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDomainConfiguration, "domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="serverCertificateArns")
    def server_certificate_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the certificates that AWS IoT passes to the device during the TLS handshake.

        Currently you can specify only one certificate ARN. This value is not required for AWS -managed domains.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-servercertificatearns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serverCertificateArns"))

    @server_certificate_arns.setter
    def server_certificate_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDomainConfiguration, "server_certificate_arns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverCertificateArns", value)

    @builtins.property
    @jsii.member(jsii_name="serviceType")
    def service_type(self) -> typing.Optional[builtins.str]:
        '''The type of service delivered by the endpoint.

        .. epigraph::

           AWS IoT Core currently supports only the ``DATA`` service type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-servicetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceType"))

    @service_type.setter
    def service_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDomainConfiguration, "service_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceType", value)

    @builtins.property
    @jsii.member(jsii_name="validationCertificateArn")
    def validation_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''The certificate used to validate the server certificate and prove domain name ownership.

        This certificate must be signed by a public certificate authority. This value is not required for AWS -managed domains.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-validationcertificatearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "validationCertificateArn"))

    @validation_certificate_arn.setter
    def validation_certificate_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnDomainConfiguration, "validation_certificate_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validationCertificateArn", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnDomainConfiguration.AuthorizerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allow_authorizer_override": "allowAuthorizerOverride",
            "default_authorizer_name": "defaultAuthorizerName",
        },
    )
    class AuthorizerConfigProperty:
        def __init__(
            self,
            *,
            allow_authorizer_override: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            default_authorizer_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that specifies the authorization service for a domain.

            :param allow_authorizer_override: A Boolean that specifies whether the domain configuration's authorization service can be overridden.
            :param default_authorizer_name: The name of the authorization service for a domain configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-authorizerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                authorizer_config_property = iot.CfnDomainConfiguration.AuthorizerConfigProperty(
                    allow_authorizer_override=False,
                    default_authorizer_name="defaultAuthorizerName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDomainConfiguration.AuthorizerConfigProperty.__init__)
                check_type(argname="argument allow_authorizer_override", value=allow_authorizer_override, expected_type=type_hints["allow_authorizer_override"])
                check_type(argname="argument default_authorizer_name", value=default_authorizer_name, expected_type=type_hints["default_authorizer_name"])
            self._values: typing.Dict[str, typing.Any] = {}
            if allow_authorizer_override is not None:
                self._values["allow_authorizer_override"] = allow_authorizer_override
            if default_authorizer_name is not None:
                self._values["default_authorizer_name"] = default_authorizer_name

        @builtins.property
        def allow_authorizer_override(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean that specifies whether the domain configuration's authorization service can be overridden.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-authorizerconfig.html#cfn-iot-domainconfiguration-authorizerconfig-allowauthorizeroverride
            '''
            result = self._values.get("allow_authorizer_override")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def default_authorizer_name(self) -> typing.Optional[builtins.str]:
            '''The name of the authorization service for a domain configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-authorizerconfig.html#cfn-iot-domainconfiguration-authorizerconfig-defaultauthorizername
            '''
            result = self._values.get("default_authorizer_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnDomainConfiguration.ServerCertificateSummaryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "server_certificate_arn": "serverCertificateArn",
            "server_certificate_status": "serverCertificateStatus",
            "server_certificate_status_detail": "serverCertificateStatusDetail",
        },
    )
    class ServerCertificateSummaryProperty:
        def __init__(
            self,
            *,
            server_certificate_arn: typing.Optional[builtins.str] = None,
            server_certificate_status: typing.Optional[builtins.str] = None,
            server_certificate_status_detail: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that contains information about a server certificate.

            :param server_certificate_arn: The ARN of the server certificate.
            :param server_certificate_status: The status of the server certificate.
            :param server_certificate_status_detail: Details that explain the status of the server certificate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-servercertificatesummary.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                server_certificate_summary_property = iot.CfnDomainConfiguration.ServerCertificateSummaryProperty(
                    server_certificate_arn="serverCertificateArn",
                    server_certificate_status="serverCertificateStatus",
                    server_certificate_status_detail="serverCertificateStatusDetail"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnDomainConfiguration.ServerCertificateSummaryProperty.__init__)
                check_type(argname="argument server_certificate_arn", value=server_certificate_arn, expected_type=type_hints["server_certificate_arn"])
                check_type(argname="argument server_certificate_status", value=server_certificate_status, expected_type=type_hints["server_certificate_status"])
                check_type(argname="argument server_certificate_status_detail", value=server_certificate_status_detail, expected_type=type_hints["server_certificate_status_detail"])
            self._values: typing.Dict[str, typing.Any] = {}
            if server_certificate_arn is not None:
                self._values["server_certificate_arn"] = server_certificate_arn
            if server_certificate_status is not None:
                self._values["server_certificate_status"] = server_certificate_status
            if server_certificate_status_detail is not None:
                self._values["server_certificate_status_detail"] = server_certificate_status_detail

        @builtins.property
        def server_certificate_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the server certificate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-servercertificatesummary.html#cfn-iot-domainconfiguration-servercertificatesummary-servercertificatearn
            '''
            result = self._values.get("server_certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def server_certificate_status(self) -> typing.Optional[builtins.str]:
            '''The status of the server certificate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-servercertificatesummary.html#cfn-iot-domainconfiguration-servercertificatesummary-servercertificatestatus
            '''
            result = self._values.get("server_certificate_status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def server_certificate_status_detail(self) -> typing.Optional[builtins.str]:
            '''Details that explain the status of the server certificate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-servercertificatesummary.html#cfn-iot-domainconfiguration-servercertificatesummary-servercertificatestatusdetail
            '''
            result = self._values.get("server_certificate_status_detail")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerCertificateSummaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnDomainConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "authorizer_config": "authorizerConfig",
        "domain_configuration_name": "domainConfigurationName",
        "domain_configuration_status": "domainConfigurationStatus",
        "domain_name": "domainName",
        "server_certificate_arns": "serverCertificateArns",
        "service_type": "serviceType",
        "tags": "tags",
        "validation_certificate_arn": "validationCertificateArn",
    },
)
class CfnDomainConfigurationProps:
    def __init__(
        self,
        *,
        authorizer_config: typing.Optional[typing.Union[typing.Union[CfnDomainConfiguration.AuthorizerConfigProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        domain_configuration_name: typing.Optional[builtins.str] = None,
        domain_configuration_status: typing.Optional[builtins.str] = None,
        domain_name: typing.Optional[builtins.str] = None,
        server_certificate_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        validation_certificate_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDomainConfiguration``.

        :param authorizer_config: An object that specifies the authorization service for a domain.
        :param domain_configuration_name: The name of the domain configuration. This value must be unique to a region.
        :param domain_configuration_status: The status to which the domain configuration should be updated. Valid values: ``ENABLED`` | ``DISABLED``
        :param domain_name: The name of the domain.
        :param server_certificate_arns: The ARNs of the certificates that AWS IoT passes to the device during the TLS handshake. Currently you can specify only one certificate ARN. This value is not required for AWS -managed domains.
        :param service_type: The type of service delivered by the endpoint. .. epigraph:: AWS IoT Core currently supports only the ``DATA`` service type.
        :param tags: Metadata which can be used to manage the domain configuration. .. epigraph:: For URI Request parameters use format: ...key1=value1&key2=value2... For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..." For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
        :param validation_certificate_arn: The certificate used to validate the server certificate and prove domain name ownership. This certificate must be signed by a public certificate authority. This value is not required for AWS -managed domains.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_domain_configuration_props = iot.CfnDomainConfigurationProps(
                authorizer_config=iot.CfnDomainConfiguration.AuthorizerConfigProperty(
                    allow_authorizer_override=False,
                    default_authorizer_name="defaultAuthorizerName"
                ),
                domain_configuration_name="domainConfigurationName",
                domain_configuration_status="domainConfigurationStatus",
                domain_name="domainName",
                server_certificate_arns=["serverCertificateArns"],
                service_type="serviceType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                validation_certificate_arn="validationCertificateArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnDomainConfigurationProps.__init__)
            check_type(argname="argument authorizer_config", value=authorizer_config, expected_type=type_hints["authorizer_config"])
            check_type(argname="argument domain_configuration_name", value=domain_configuration_name, expected_type=type_hints["domain_configuration_name"])
            check_type(argname="argument domain_configuration_status", value=domain_configuration_status, expected_type=type_hints["domain_configuration_status"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument server_certificate_arns", value=server_certificate_arns, expected_type=type_hints["server_certificate_arns"])
            check_type(argname="argument service_type", value=service_type, expected_type=type_hints["service_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument validation_certificate_arn", value=validation_certificate_arn, expected_type=type_hints["validation_certificate_arn"])
        self._values: typing.Dict[str, typing.Any] = {}
        if authorizer_config is not None:
            self._values["authorizer_config"] = authorizer_config
        if domain_configuration_name is not None:
            self._values["domain_configuration_name"] = domain_configuration_name
        if domain_configuration_status is not None:
            self._values["domain_configuration_status"] = domain_configuration_status
        if domain_name is not None:
            self._values["domain_name"] = domain_name
        if server_certificate_arns is not None:
            self._values["server_certificate_arns"] = server_certificate_arns
        if service_type is not None:
            self._values["service_type"] = service_type
        if tags is not None:
            self._values["tags"] = tags
        if validation_certificate_arn is not None:
            self._values["validation_certificate_arn"] = validation_certificate_arn

    @builtins.property
    def authorizer_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDomainConfiguration.AuthorizerConfigProperty, _IResolvable_da3f097b]]:
        '''An object that specifies the authorization service for a domain.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-authorizerconfig
        '''
        result = self._values.get("authorizer_config")
        return typing.cast(typing.Optional[typing.Union[CfnDomainConfiguration.AuthorizerConfigProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def domain_configuration_name(self) -> typing.Optional[builtins.str]:
        '''The name of the domain configuration.

        This value must be unique to a region.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-domainconfigurationname
        '''
        result = self._values.get("domain_configuration_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_configuration_status(self) -> typing.Optional[builtins.str]:
        '''The status to which the domain configuration should be updated.

        Valid values: ``ENABLED`` | ``DISABLED``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-domainconfigurationstatus
        '''
        result = self._values.get("domain_configuration_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''The name of the domain.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-domainname
        '''
        result = self._values.get("domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_certificate_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the certificates that AWS IoT passes to the device during the TLS handshake.

        Currently you can specify only one certificate ARN. This value is not required for AWS -managed domains.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-servercertificatearns
        '''
        result = self._values.get("server_certificate_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def service_type(self) -> typing.Optional[builtins.str]:
        '''The type of service delivered by the endpoint.

        .. epigraph::

           AWS IoT Core currently supports only the ``DATA`` service type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-servicetype
        '''
        result = self._values.get("service_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata which can be used to manage the domain configuration.

        .. epigraph::

           For URI Request parameters use format: ...key1=value1&key2=value2...

           For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."

           For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def validation_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''The certificate used to validate the server certificate and prove domain name ownership.

        This certificate must be signed by a public certificate authority. This value is not required for AWS -managed domains.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-validationcertificatearn
        '''
        result = self._values.get("validation_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFleetMetric(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnFleetMetric",
):
    '''A CloudFormation ``AWS::IoT::FleetMetric``.

    Use the ``AWS::IoT::FleetMetric`` resource to declare a fleet metric.

    :cloudformationResource: AWS::IoT::FleetMetric
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_fleet_metric = iot.CfnFleetMetric(self, "MyCfnFleetMetric",
            metric_name="metricName",
        
            # the properties below are optional
            aggregation_field="aggregationField",
            aggregation_type=iot.CfnFleetMetric.AggregationTypeProperty(
                name="name",
                values=["values"]
            ),
            description="description",
            index_name="indexName",
            period=123,
            query_string="queryString",
            query_version="queryVersion",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            unit="unit"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metric_name: builtins.str,
        aggregation_field: typing.Optional[builtins.str] = None,
        aggregation_type: typing.Optional[typing.Union[typing.Union["CfnFleetMetric.AggregationTypeProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        index_name: typing.Optional[builtins.str] = None,
        period: typing.Optional[jsii.Number] = None,
        query_string: typing.Optional[builtins.str] = None,
        query_version: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::FleetMetric``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param metric_name: The name of the fleet metric to create.
        :param aggregation_field: The field to aggregate.
        :param aggregation_type: The type of the aggregation query.
        :param description: The fleet metric description.
        :param index_name: The name of the index to search.
        :param period: The time in seconds between fleet metric emissions. Range [60(1 min), 86400(1 day)] and must be multiple of 60.
        :param query_string: The search query string.
        :param query_version: The query version.
        :param tags: Metadata which can be used to manage the fleet metric.
        :param unit: Used to support unit transformation such as milliseconds to seconds. Must be a unit supported by CW metric. Default to null.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFleetMetric.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFleetMetricProps(
            metric_name=metric_name,
            aggregation_field=aggregation_field,
            aggregation_type=aggregation_type,
            description=description,
            index_name=index_name,
            period=period,
            query_string=query_string,
            query_version=query_version,
            tags=tags,
            unit=unit,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFleetMetric.inspect)
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
            type_hints = typing.get_type_hints(CfnFleetMetric._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationDate")
    def attr_creation_date(self) -> _IResolvable_da3f097b:
        '''The time the fleet metric was created.

        :cloudformationAttribute: CreationDate
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrCreationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedDate")
    def attr_last_modified_date(self) -> _IResolvable_da3f097b:
        '''The time the fleet metric was last modified.

        :cloudformationAttribute: LastModifiedDate
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLastModifiedDate"))

    @builtins.property
    @jsii.member(jsii_name="attrMetricArn")
    def attr_metric_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the fleet metric.

        :cloudformationAttribute: MetricArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMetricArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVersion")
    def attr_version(self) -> _IResolvable_da3f097b:
        '''The fleet metric version.

        :cloudformationAttribute: Version
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrVersion"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata which can be used to manage the fleet metric.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        '''The name of the fleet metric to create.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-metricname
        '''
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFleetMetric, "metric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="aggregationField")
    def aggregation_field(self) -> typing.Optional[builtins.str]:
        '''The field to aggregate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-aggregationfield
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationField"))

    @aggregation_field.setter
    def aggregation_field(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFleetMetric, "aggregation_field").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationField", value)

    @builtins.property
    @jsii.member(jsii_name="aggregationType")
    def aggregation_type(
        self,
    ) -> typing.Optional[typing.Union["CfnFleetMetric.AggregationTypeProperty", _IResolvable_da3f097b]]:
        '''The type of the aggregation query.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-aggregationtype
        '''
        return typing.cast(typing.Optional[typing.Union["CfnFleetMetric.AggregationTypeProperty", _IResolvable_da3f097b]], jsii.get(self, "aggregationType"))

    @aggregation_type.setter
    def aggregation_type(
        self,
        value: typing.Optional[typing.Union["CfnFleetMetric.AggregationTypeProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFleetMetric, "aggregation_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The fleet metric description.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFleetMetric, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="indexName")
    def index_name(self) -> typing.Optional[builtins.str]:
        '''The name of the index to search.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-indexname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexName"))

    @index_name.setter
    def index_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFleetMetric, "index_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexName", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> typing.Optional[jsii.Number]:
        '''The time in seconds between fleet metric emissions.

        Range [60(1 min), 86400(1 day)] and must be multiple of 60.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-period
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "period"))

    @period.setter
    def period(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFleetMetric, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> typing.Optional[builtins.str]:
        '''The search query string.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-querystring
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryString"))

    @query_string.setter
    def query_string(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFleetMetric, "query_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryString", value)

    @builtins.property
    @jsii.member(jsii_name="queryVersion")
    def query_version(self) -> typing.Optional[builtins.str]:
        '''The query version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-queryversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryVersion"))

    @query_version.setter
    def query_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFleetMetric, "query_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryVersion", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> typing.Optional[builtins.str]:
        '''Used to support unit transformation such as milliseconds to seconds.

        Must be a unit supported by CW metric. Default to null.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-unit
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnFleetMetric, "unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnFleetMetric.AggregationTypeProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class AggregationTypeProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''The type of aggregation queries.

            :param name: The name of the aggregation type.
            :param values: A list of the values of aggregation types.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-fleetmetric-aggregationtype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                aggregation_type_property = iot.CfnFleetMetric.AggregationTypeProperty(
                    name="name",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnFleetMetric.AggregationTypeProperty.__init__)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the aggregation type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-fleetmetric-aggregationtype.html#cfn-iot-fleetmetric-aggregationtype-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''A list of the values of aggregation types.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-fleetmetric-aggregationtype.html#cfn-iot-fleetmetric-aggregationtype-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AggregationTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnFleetMetricProps",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "aggregation_field": "aggregationField",
        "aggregation_type": "aggregationType",
        "description": "description",
        "index_name": "indexName",
        "period": "period",
        "query_string": "queryString",
        "query_version": "queryVersion",
        "tags": "tags",
        "unit": "unit",
    },
)
class CfnFleetMetricProps:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        aggregation_field: typing.Optional[builtins.str] = None,
        aggregation_type: typing.Optional[typing.Union[typing.Union[CfnFleetMetric.AggregationTypeProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        index_name: typing.Optional[builtins.str] = None,
        period: typing.Optional[jsii.Number] = None,
        query_string: typing.Optional[builtins.str] = None,
        query_version: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnFleetMetric``.

        :param metric_name: The name of the fleet metric to create.
        :param aggregation_field: The field to aggregate.
        :param aggregation_type: The type of the aggregation query.
        :param description: The fleet metric description.
        :param index_name: The name of the index to search.
        :param period: The time in seconds between fleet metric emissions. Range [60(1 min), 86400(1 day)] and must be multiple of 60.
        :param query_string: The search query string.
        :param query_version: The query version.
        :param tags: Metadata which can be used to manage the fleet metric.
        :param unit: Used to support unit transformation such as milliseconds to seconds. Must be a unit supported by CW metric. Default to null.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_fleet_metric_props = iot.CfnFleetMetricProps(
                metric_name="metricName",
            
                # the properties below are optional
                aggregation_field="aggregationField",
                aggregation_type=iot.CfnFleetMetric.AggregationTypeProperty(
                    name="name",
                    values=["values"]
                ),
                description="description",
                index_name="indexName",
                period=123,
                query_string="queryString",
                query_version="queryVersion",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                unit="unit"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnFleetMetricProps.__init__)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument aggregation_field", value=aggregation_field, expected_type=type_hints["aggregation_field"])
            check_type(argname="argument aggregation_type", value=aggregation_type, expected_type=type_hints["aggregation_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument query_version", value=query_version, expected_type=type_hints["query_version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
        }
        if aggregation_field is not None:
            self._values["aggregation_field"] = aggregation_field
        if aggregation_type is not None:
            self._values["aggregation_type"] = aggregation_type
        if description is not None:
            self._values["description"] = description
        if index_name is not None:
            self._values["index_name"] = index_name
        if period is not None:
            self._values["period"] = period
        if query_string is not None:
            self._values["query_string"] = query_string
        if query_version is not None:
            self._values["query_version"] = query_version
        if tags is not None:
            self._values["tags"] = tags
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''The name of the fleet metric to create.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-metricname
        '''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aggregation_field(self) -> typing.Optional[builtins.str]:
        '''The field to aggregate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-aggregationfield
        '''
        result = self._values.get("aggregation_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aggregation_type(
        self,
    ) -> typing.Optional[typing.Union[CfnFleetMetric.AggregationTypeProperty, _IResolvable_da3f097b]]:
        '''The type of the aggregation query.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-aggregationtype
        '''
        result = self._values.get("aggregation_type")
        return typing.cast(typing.Optional[typing.Union[CfnFleetMetric.AggregationTypeProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The fleet metric description.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def index_name(self) -> typing.Optional[builtins.str]:
        '''The name of the index to search.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-indexname
        '''
        result = self._values.get("index_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''The time in seconds between fleet metric emissions.

        Range [60(1 min), 86400(1 day)] and must be multiple of 60.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-period
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def query_string(self) -> typing.Optional[builtins.str]:
        '''The search query string.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-querystring
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_version(self) -> typing.Optional[builtins.str]:
        '''The query version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-queryversion
        '''
        result = self._values.get("query_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata which can be used to manage the fleet metric.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Used to support unit transformation such as milliseconds to seconds.

        Must be a unit supported by CW metric. Default to null.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-unit
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFleetMetricProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnJobTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnJobTemplate",
):
    '''A CloudFormation ``AWS::IoT::JobTemplate``.

    Represents a job template.

    :cloudformationResource: AWS::IoT::JobTemplate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        # abort_config: Any
        # job_executions_retry_config: Any
        # job_executions_rollout_config: Any
        # presigned_url_config: Any
        # timeout_config: Any
        
        cfn_job_template = iot.CfnJobTemplate(self, "MyCfnJobTemplate",
            description="description",
            job_template_id="jobTemplateId",
        
            # the properties below are optional
            abort_config=abort_config,
            document="document",
            document_source="documentSource",
            job_arn="jobArn",
            job_executions_retry_config=job_executions_retry_config,
            job_executions_rollout_config=job_executions_rollout_config,
            presigned_url_config=presigned_url_config,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            timeout_config=timeout_config
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        job_template_id: builtins.str,
        abort_config: typing.Any = None,
        document: typing.Optional[builtins.str] = None,
        document_source: typing.Optional[builtins.str] = None,
        job_arn: typing.Optional[builtins.str] = None,
        job_executions_retry_config: typing.Any = None,
        job_executions_rollout_config: typing.Any = None,
        presigned_url_config: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        timeout_config: typing.Any = None,
    ) -> None:
        '''Create a new ``AWS::IoT::JobTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: A description of the job template.
        :param job_template_id: A unique identifier for the job template. We recommend using a UUID. Alpha-numeric characters, "-", and "_" are valid for use here.
        :param abort_config: The criteria that determine when and how a job abort takes place.
        :param document: The job document. Required if you don't specify a value for ``documentSource`` .
        :param document_source: An S3 link to the job document to use in the template. Required if you don't specify a value for ``document`` . .. epigraph:: If the job document resides in an S3 bucket, you must use a placeholder link when specifying the document. The placeholder link is of the following form: ``${aws:iot:s3-presigned-url:https://s3.amazonaws.com/ *bucket* / *key* }`` where *bucket* is your bucket name and *key* is the object in the bucket to which you are linking.
        :param job_arn: The ARN of the job to use as the basis for the job template.
        :param job_executions_retry_config: Allows you to create the criteria to retry a job.
        :param job_executions_rollout_config: Allows you to create a staged rollout of a job.
        :param presigned_url_config: Configuration for pre-signed S3 URLs.
        :param tags: Metadata that can be used to manage the job template.
        :param timeout_config: Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to ``TIMED_OUT`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnJobTemplate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnJobTemplateProps(
            description=description,
            job_template_id=job_template_id,
            abort_config=abort_config,
            document=document,
            document_source=document_source,
            job_arn=job_arn,
            job_executions_retry_config=job_executions_retry_config,
            job_executions_rollout_config=job_executions_rollout_config,
            presigned_url_config=presigned_url_config,
            tags=tags,
            timeout_config=timeout_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnJobTemplate.inspect)
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
            type_hints = typing.get_type_hints(CfnJobTemplate._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the job to use as the basis for the job template.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata that can be used to manage the job template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="abortConfig")
    def abort_config(self) -> typing.Any:
        '''The criteria that determine when and how a job abort takes place.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-abortconfig
        '''
        return typing.cast(typing.Any, jsii.get(self, "abortConfig"))

    @abort_config.setter
    def abort_config(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobTemplate, "abort_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "abortConfig", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A description of the job template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobTemplate, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="jobExecutionsRetryConfig")
    def job_executions_retry_config(self) -> typing.Any:
        '''Allows you to create the criteria to retry a job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobexecutionsretryconfig
        '''
        return typing.cast(typing.Any, jsii.get(self, "jobExecutionsRetryConfig"))

    @job_executions_retry_config.setter
    def job_executions_retry_config(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobTemplate, "job_executions_retry_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobExecutionsRetryConfig", value)

    @builtins.property
    @jsii.member(jsii_name="jobExecutionsRolloutConfig")
    def job_executions_rollout_config(self) -> typing.Any:
        '''Allows you to create a staged rollout of a job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobexecutionsrolloutconfig
        '''
        return typing.cast(typing.Any, jsii.get(self, "jobExecutionsRolloutConfig"))

    @job_executions_rollout_config.setter
    def job_executions_rollout_config(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobTemplate, "job_executions_rollout_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobExecutionsRolloutConfig", value)

    @builtins.property
    @jsii.member(jsii_name="jobTemplateId")
    def job_template_id(self) -> builtins.str:
        '''A unique identifier for the job template.

        We recommend using a UUID. Alpha-numeric characters, "-", and "_" are valid for use here.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobtemplateid
        '''
        return typing.cast(builtins.str, jsii.get(self, "jobTemplateId"))

    @job_template_id.setter
    def job_template_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobTemplate, "job_template_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobTemplateId", value)

    @builtins.property
    @jsii.member(jsii_name="presignedUrlConfig")
    def presigned_url_config(self) -> typing.Any:
        '''Configuration for pre-signed S3 URLs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-presignedurlconfig
        '''
        return typing.cast(typing.Any, jsii.get(self, "presignedUrlConfig"))

    @presigned_url_config.setter
    def presigned_url_config(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobTemplate, "presigned_url_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "presignedUrlConfig", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutConfig")
    def timeout_config(self) -> typing.Any:
        '''Specifies the amount of time each device has to finish its execution of the job.

        A timer is started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to ``TIMED_OUT`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-timeoutconfig
        '''
        return typing.cast(typing.Any, jsii.get(self, "timeoutConfig"))

    @timeout_config.setter
    def timeout_config(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobTemplate, "timeout_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutConfig", value)

    @builtins.property
    @jsii.member(jsii_name="document")
    def document(self) -> typing.Optional[builtins.str]:
        '''The job document.

        Required if you don't specify a value for ``documentSource`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-document
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "document"))

    @document.setter
    def document(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobTemplate, "document").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "document", value)

    @builtins.property
    @jsii.member(jsii_name="documentSource")
    def document_source(self) -> typing.Optional[builtins.str]:
        '''An S3 link to the job document to use in the template.

        Required if you don't specify a value for ``document`` .
        .. epigraph::

           If the job document resides in an S3 bucket, you must use a placeholder link when specifying the document.

           The placeholder link is of the following form:

           ``${aws:iot:s3-presigned-url:https://s3.amazonaws.com/ *bucket* / *key* }``

           where *bucket* is your bucket name and *key* is the object in the bucket to which you are linking.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-documentsource
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentSource"))

    @document_source.setter
    def document_source(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobTemplate, "document_source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentSource", value)

    @builtins.property
    @jsii.member(jsii_name="jobArn")
    def job_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the job to use as the basis for the job template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobArn"))

    @job_arn.setter
    def job_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnJobTemplate, "job_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnJobTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "job_template_id": "jobTemplateId",
        "abort_config": "abortConfig",
        "document": "document",
        "document_source": "documentSource",
        "job_arn": "jobArn",
        "job_executions_retry_config": "jobExecutionsRetryConfig",
        "job_executions_rollout_config": "jobExecutionsRolloutConfig",
        "presigned_url_config": "presignedUrlConfig",
        "tags": "tags",
        "timeout_config": "timeoutConfig",
    },
)
class CfnJobTemplateProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        job_template_id: builtins.str,
        abort_config: typing.Any = None,
        document: typing.Optional[builtins.str] = None,
        document_source: typing.Optional[builtins.str] = None,
        job_arn: typing.Optional[builtins.str] = None,
        job_executions_retry_config: typing.Any = None,
        job_executions_rollout_config: typing.Any = None,
        presigned_url_config: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        timeout_config: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnJobTemplate``.

        :param description: A description of the job template.
        :param job_template_id: A unique identifier for the job template. We recommend using a UUID. Alpha-numeric characters, "-", and "_" are valid for use here.
        :param abort_config: The criteria that determine when and how a job abort takes place.
        :param document: The job document. Required if you don't specify a value for ``documentSource`` .
        :param document_source: An S3 link to the job document to use in the template. Required if you don't specify a value for ``document`` . .. epigraph:: If the job document resides in an S3 bucket, you must use a placeholder link when specifying the document. The placeholder link is of the following form: ``${aws:iot:s3-presigned-url:https://s3.amazonaws.com/ *bucket* / *key* }`` where *bucket* is your bucket name and *key* is the object in the bucket to which you are linking.
        :param job_arn: The ARN of the job to use as the basis for the job template.
        :param job_executions_retry_config: Allows you to create the criteria to retry a job.
        :param job_executions_rollout_config: Allows you to create a staged rollout of a job.
        :param presigned_url_config: Configuration for pre-signed S3 URLs.
        :param tags: Metadata that can be used to manage the job template.
        :param timeout_config: Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to ``TIMED_OUT`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            # abort_config: Any
            # job_executions_retry_config: Any
            # job_executions_rollout_config: Any
            # presigned_url_config: Any
            # timeout_config: Any
            
            cfn_job_template_props = iot.CfnJobTemplateProps(
                description="description",
                job_template_id="jobTemplateId",
            
                # the properties below are optional
                abort_config=abort_config,
                document="document",
                document_source="documentSource",
                job_arn="jobArn",
                job_executions_retry_config=job_executions_retry_config,
                job_executions_rollout_config=job_executions_rollout_config,
                presigned_url_config=presigned_url_config,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                timeout_config=timeout_config
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnJobTemplateProps.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument job_template_id", value=job_template_id, expected_type=type_hints["job_template_id"])
            check_type(argname="argument abort_config", value=abort_config, expected_type=type_hints["abort_config"])
            check_type(argname="argument document", value=document, expected_type=type_hints["document"])
            check_type(argname="argument document_source", value=document_source, expected_type=type_hints["document_source"])
            check_type(argname="argument job_arn", value=job_arn, expected_type=type_hints["job_arn"])
            check_type(argname="argument job_executions_retry_config", value=job_executions_retry_config, expected_type=type_hints["job_executions_retry_config"])
            check_type(argname="argument job_executions_rollout_config", value=job_executions_rollout_config, expected_type=type_hints["job_executions_rollout_config"])
            check_type(argname="argument presigned_url_config", value=presigned_url_config, expected_type=type_hints["presigned_url_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeout_config", value=timeout_config, expected_type=type_hints["timeout_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "job_template_id": job_template_id,
        }
        if abort_config is not None:
            self._values["abort_config"] = abort_config
        if document is not None:
            self._values["document"] = document
        if document_source is not None:
            self._values["document_source"] = document_source
        if job_arn is not None:
            self._values["job_arn"] = job_arn
        if job_executions_retry_config is not None:
            self._values["job_executions_retry_config"] = job_executions_retry_config
        if job_executions_rollout_config is not None:
            self._values["job_executions_rollout_config"] = job_executions_rollout_config
        if presigned_url_config is not None:
            self._values["presigned_url_config"] = presigned_url_config
        if tags is not None:
            self._values["tags"] = tags
        if timeout_config is not None:
            self._values["timeout_config"] = timeout_config

    @builtins.property
    def description(self) -> builtins.str:
        '''A description of the job template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_template_id(self) -> builtins.str:
        '''A unique identifier for the job template.

        We recommend using a UUID. Alpha-numeric characters, "-", and "_" are valid for use here.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobtemplateid
        '''
        result = self._values.get("job_template_id")
        assert result is not None, "Required property 'job_template_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def abort_config(self) -> typing.Any:
        '''The criteria that determine when and how a job abort takes place.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-abortconfig
        '''
        result = self._values.get("abort_config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def document(self) -> typing.Optional[builtins.str]:
        '''The job document.

        Required if you don't specify a value for ``documentSource`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-document
        '''
        result = self._values.get("document")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_source(self) -> typing.Optional[builtins.str]:
        '''An S3 link to the job document to use in the template.

        Required if you don't specify a value for ``document`` .
        .. epigraph::

           If the job document resides in an S3 bucket, you must use a placeholder link when specifying the document.

           The placeholder link is of the following form:

           ``${aws:iot:s3-presigned-url:https://s3.amazonaws.com/ *bucket* / *key* }``

           where *bucket* is your bucket name and *key* is the object in the bucket to which you are linking.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-documentsource
        '''
        result = self._values.get("document_source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the job to use as the basis for the job template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobarn
        '''
        result = self._values.get("job_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_executions_retry_config(self) -> typing.Any:
        '''Allows you to create the criteria to retry a job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobexecutionsretryconfig
        '''
        result = self._values.get("job_executions_retry_config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def job_executions_rollout_config(self) -> typing.Any:
        '''Allows you to create a staged rollout of a job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobexecutionsrolloutconfig
        '''
        result = self._values.get("job_executions_rollout_config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def presigned_url_config(self) -> typing.Any:
        '''Configuration for pre-signed S3 URLs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-presignedurlconfig
        '''
        result = self._values.get("presigned_url_config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata that can be used to manage the job template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def timeout_config(self) -> typing.Any:
        '''Specifies the amount of time each device has to finish its execution of the job.

        A timer is started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to ``TIMED_OUT`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-timeoutconfig
        '''
        result = self._values.get("timeout_config")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnJobTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLogging(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnLogging",
):
    '''A CloudFormation ``AWS::IoT::Logging``.

    Configure logging.

    :cloudformationResource: AWS::IoT::Logging
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_logging = iot.CfnLogging(self, "MyCfnLogging",
            account_id="accountId",
            default_log_level="defaultLogLevel",
            role_arn="roleArn"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account_id: builtins.str,
        default_log_level: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''Create a new ``AWS::IoT::Logging``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param account_id: The account ID.
        :param default_log_level: The default log level. Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``
        :param role_arn: The role ARN used for the log.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLogging.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLoggingProps(
            account_id=account_id,
            default_log_level=default_log_level,
            role_arn=role_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLogging.inspect)
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
            type_hints = typing.get_type_hints(CfnLogging._render_properties)
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
        '''The account ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html#cfn-iot-logging-accountid
        '''
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLogging, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="defaultLogLevel")
    def default_log_level(self) -> builtins.str:
        '''The default log level.

        Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html#cfn-iot-logging-defaultloglevel
        '''
        return typing.cast(builtins.str, jsii.get(self, "defaultLogLevel"))

    @default_log_level.setter
    def default_log_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLogging, "default_log_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultLogLevel", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The role ARN used for the log.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html#cfn-iot-logging-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnLogging, "role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnLoggingProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "default_log_level": "defaultLogLevel",
        "role_arn": "roleArn",
    },
)
class CfnLoggingProps:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        default_log_level: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnLogging``.

        :param account_id: The account ID.
        :param default_log_level: The default log level. Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``
        :param role_arn: The role ARN used for the log.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_logging_props = iot.CfnLoggingProps(
                account_id="accountId",
                default_log_level="defaultLogLevel",
                role_arn="roleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnLoggingProps.__init__)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument default_log_level", value=default_log_level, expected_type=type_hints["default_log_level"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
            "default_log_level": default_log_level,
            "role_arn": role_arn,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The account ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html#cfn-iot-logging-accountid
        '''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_log_level(self) -> builtins.str:
        '''The default log level.

        Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html#cfn-iot-logging-defaultloglevel
        '''
        result = self._values.get("default_log_level")
        assert result is not None, "Required property 'default_log_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The role ARN used for the log.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html#cfn-iot-logging-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoggingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMitigationAction(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnMitigationAction",
):
    '''A CloudFormation ``AWS::IoT::MitigationAction``.

    Defines an action that can be applied to audit findings by using StartAuditMitigationActionsTask. For API reference, see `CreateMitigationAction <https://docs.aws.amazon.com/iot/latest/apireference/API_CreateMitigationAction.html>`_ and for general information, see `Mitigation actions <https://docs.aws.amazon.com/iot/latest/developerguide/dd-mitigation-actions.html>`_ .

    :cloudformationResource: AWS::IoT::MitigationAction
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_mitigation_action = iot.CfnMitigationAction(self, "MyCfnMitigationAction",
            action_params=iot.CfnMitigationAction.ActionParamsProperty(
                add_things_to_thing_group_params=iot.CfnMitigationAction.AddThingsToThingGroupParamsProperty(
                    thing_group_names=["thingGroupNames"],
        
                    # the properties below are optional
                    override_dynamic_groups=False
                ),
                enable_io_tLogging_params=iot.CfnMitigationAction.EnableIoTLoggingParamsProperty(
                    log_level="logLevel",
                    role_arn_for_logging="roleArnForLogging"
                ),
                publish_finding_to_sns_params=iot.CfnMitigationAction.PublishFindingToSnsParamsProperty(
                    topic_arn="topicArn"
                ),
                replace_default_policy_version_params=iot.CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty(
                    template_name="templateName"
                ),
                update_ca_certificate_params=iot.CfnMitigationAction.UpdateCACertificateParamsProperty(
                    action="action"
                ),
                update_device_certificate_params=iot.CfnMitigationAction.UpdateDeviceCertificateParamsProperty(
                    action="action"
                )
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            action_name="actionName",
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
        action_params: typing.Union[typing.Union["CfnMitigationAction.ActionParamsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        role_arn: builtins.str,
        action_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::MitigationAction``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param action_params: The set of parameters for this mitigation action. The parameters vary, depending on the kind of action you apply.
        :param role_arn: The IAM role ARN used to apply this mitigation action.
        :param action_name: The friendly name of the mitigation action.
        :param tags: Metadata that can be used to manage the mitigation action.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnMitigationAction.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMitigationActionProps(
            action_params=action_params,
            role_arn=role_arn,
            action_name=action_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnMitigationAction.inspect)
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
            type_hints = typing.get_type_hints(CfnMitigationAction._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrMitigationActionArn")
    def attr_mitigation_action_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the mitigation action.

        :cloudformationAttribute: MitigationActionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMitigationActionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrMitigationActionId")
    def attr_mitigation_action_id(self) -> builtins.str:
        '''The ID of the mitigation action.

        :cloudformationAttribute: MitigationActionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMitigationActionId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata that can be used to manage the mitigation action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="actionParams")
    def action_params(
        self,
    ) -> typing.Union["CfnMitigationAction.ActionParamsProperty", _IResolvable_da3f097b]:
        '''The set of parameters for this mitigation action.

        The parameters vary, depending on the kind of action you apply.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionparams
        '''
        return typing.cast(typing.Union["CfnMitigationAction.ActionParamsProperty", _IResolvable_da3f097b], jsii.get(self, "actionParams"))

    @action_params.setter
    def action_params(
        self,
        value: typing.Union["CfnMitigationAction.ActionParamsProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnMitigationAction, "action_params").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionParams", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The IAM role ARN used to apply this mitigation action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnMitigationAction, "role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="actionName")
    def action_name(self) -> typing.Optional[builtins.str]:
        '''The friendly name of the mitigation action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionName"))

    @action_name.setter
    def action_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnMitigationAction, "action_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnMitigationAction.ActionParamsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_things_to_thing_group_params": "addThingsToThingGroupParams",
            "enable_io_t_logging_params": "enableIoTLoggingParams",
            "publish_finding_to_sns_params": "publishFindingToSnsParams",
            "replace_default_policy_version_params": "replaceDefaultPolicyVersionParams",
            "update_ca_certificate_params": "updateCaCertificateParams",
            "update_device_certificate_params": "updateDeviceCertificateParams",
        },
    )
    class ActionParamsProperty:
        def __init__(
            self,
            *,
            add_things_to_thing_group_params: typing.Optional[typing.Union[typing.Union["CfnMitigationAction.AddThingsToThingGroupParamsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            enable_io_t_logging_params: typing.Optional[typing.Union[typing.Union["CfnMitigationAction.EnableIoTLoggingParamsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            publish_finding_to_sns_params: typing.Optional[typing.Union[typing.Union["CfnMitigationAction.PublishFindingToSnsParamsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            replace_default_policy_version_params: typing.Optional[typing.Union[typing.Union["CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            update_ca_certificate_params: typing.Optional[typing.Union[typing.Union["CfnMitigationAction.UpdateCACertificateParamsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            update_device_certificate_params: typing.Optional[typing.Union[typing.Union["CfnMitigationAction.UpdateDeviceCertificateParamsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Defines the type of action and the parameters for that action.

            :param add_things_to_thing_group_params: Specifies the group to which you want to add the devices.
            :param enable_io_t_logging_params: Specifies the logging level and the role with permissions for logging. You cannot specify a logging level of ``DISABLED`` .
            :param publish_finding_to_sns_params: Specifies the topic to which the finding should be published.
            :param replace_default_policy_version_params: Replaces the policy version with a default or blank policy. You specify the template name. Only a value of ``BLANK_POLICY`` is currently supported.
            :param update_ca_certificate_params: Specifies the new state for the CA certificate. Only a value of ``DEACTIVATE`` is currently supported.
            :param update_device_certificate_params: Specifies the new state for a device certificate. Only a value of ``DEACTIVATE`` is currently supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                action_params_property = iot.CfnMitigationAction.ActionParamsProperty(
                    add_things_to_thing_group_params=iot.CfnMitigationAction.AddThingsToThingGroupParamsProperty(
                        thing_group_names=["thingGroupNames"],
                
                        # the properties below are optional
                        override_dynamic_groups=False
                    ),
                    enable_io_tLogging_params=iot.CfnMitigationAction.EnableIoTLoggingParamsProperty(
                        log_level="logLevel",
                        role_arn_for_logging="roleArnForLogging"
                    ),
                    publish_finding_to_sns_params=iot.CfnMitigationAction.PublishFindingToSnsParamsProperty(
                        topic_arn="topicArn"
                    ),
                    replace_default_policy_version_params=iot.CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty(
                        template_name="templateName"
                    ),
                    update_ca_certificate_params=iot.CfnMitigationAction.UpdateCACertificateParamsProperty(
                        action="action"
                    ),
                    update_device_certificate_params=iot.CfnMitigationAction.UpdateDeviceCertificateParamsProperty(
                        action="action"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnMitigationAction.ActionParamsProperty.__init__)
                check_type(argname="argument add_things_to_thing_group_params", value=add_things_to_thing_group_params, expected_type=type_hints["add_things_to_thing_group_params"])
                check_type(argname="argument enable_io_t_logging_params", value=enable_io_t_logging_params, expected_type=type_hints["enable_io_t_logging_params"])
                check_type(argname="argument publish_finding_to_sns_params", value=publish_finding_to_sns_params, expected_type=type_hints["publish_finding_to_sns_params"])
                check_type(argname="argument replace_default_policy_version_params", value=replace_default_policy_version_params, expected_type=type_hints["replace_default_policy_version_params"])
                check_type(argname="argument update_ca_certificate_params", value=update_ca_certificate_params, expected_type=type_hints["update_ca_certificate_params"])
                check_type(argname="argument update_device_certificate_params", value=update_device_certificate_params, expected_type=type_hints["update_device_certificate_params"])
            self._values: typing.Dict[str, typing.Any] = {}
            if add_things_to_thing_group_params is not None:
                self._values["add_things_to_thing_group_params"] = add_things_to_thing_group_params
            if enable_io_t_logging_params is not None:
                self._values["enable_io_t_logging_params"] = enable_io_t_logging_params
            if publish_finding_to_sns_params is not None:
                self._values["publish_finding_to_sns_params"] = publish_finding_to_sns_params
            if replace_default_policy_version_params is not None:
                self._values["replace_default_policy_version_params"] = replace_default_policy_version_params
            if update_ca_certificate_params is not None:
                self._values["update_ca_certificate_params"] = update_ca_certificate_params
            if update_device_certificate_params is not None:
                self._values["update_device_certificate_params"] = update_device_certificate_params

        @builtins.property
        def add_things_to_thing_group_params(
            self,
        ) -> typing.Optional[typing.Union["CfnMitigationAction.AddThingsToThingGroupParamsProperty", _IResolvable_da3f097b]]:
            '''Specifies the group to which you want to add the devices.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-addthingstothinggroupparams
            '''
            result = self._values.get("add_things_to_thing_group_params")
            return typing.cast(typing.Optional[typing.Union["CfnMitigationAction.AddThingsToThingGroupParamsProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def enable_io_t_logging_params(
            self,
        ) -> typing.Optional[typing.Union["CfnMitigationAction.EnableIoTLoggingParamsProperty", _IResolvable_da3f097b]]:
            '''Specifies the logging level and the role with permissions for logging.

            You cannot specify a logging level of ``DISABLED`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-enableiotloggingparams
            '''
            result = self._values.get("enable_io_t_logging_params")
            return typing.cast(typing.Optional[typing.Union["CfnMitigationAction.EnableIoTLoggingParamsProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def publish_finding_to_sns_params(
            self,
        ) -> typing.Optional[typing.Union["CfnMitigationAction.PublishFindingToSnsParamsProperty", _IResolvable_da3f097b]]:
            '''Specifies the topic to which the finding should be published.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-publishfindingtosnsparams
            '''
            result = self._values.get("publish_finding_to_sns_params")
            return typing.cast(typing.Optional[typing.Union["CfnMitigationAction.PublishFindingToSnsParamsProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def replace_default_policy_version_params(
            self,
        ) -> typing.Optional[typing.Union["CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty", _IResolvable_da3f097b]]:
            '''Replaces the policy version with a default or blank policy.

            You specify the template name. Only a value of ``BLANK_POLICY`` is currently supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-replacedefaultpolicyversionparams
            '''
            result = self._values.get("replace_default_policy_version_params")
            return typing.cast(typing.Optional[typing.Union["CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def update_ca_certificate_params(
            self,
        ) -> typing.Optional[typing.Union["CfnMitigationAction.UpdateCACertificateParamsProperty", _IResolvable_da3f097b]]:
            '''Specifies the new state for the CA certificate.

            Only a value of ``DEACTIVATE`` is currently supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-updatecacertificateparams
            '''
            result = self._values.get("update_ca_certificate_params")
            return typing.cast(typing.Optional[typing.Union["CfnMitigationAction.UpdateCACertificateParamsProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def update_device_certificate_params(
            self,
        ) -> typing.Optional[typing.Union["CfnMitigationAction.UpdateDeviceCertificateParamsProperty", _IResolvable_da3f097b]]:
            '''Specifies the new state for a device certificate.

            Only a value of ``DEACTIVATE`` is currently supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-updatedevicecertificateparams
            '''
            result = self._values.get("update_device_certificate_params")
            return typing.cast(typing.Optional[typing.Union["CfnMitigationAction.UpdateDeviceCertificateParamsProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnMitigationAction.AddThingsToThingGroupParamsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "thing_group_names": "thingGroupNames",
            "override_dynamic_groups": "overrideDynamicGroups",
        },
    )
    class AddThingsToThingGroupParamsProperty:
        def __init__(
            self,
            *,
            thing_group_names: typing.Sequence[builtins.str],
            override_dynamic_groups: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Parameters used when defining a mitigation action that move a set of things to a thing group.

            :param thing_group_names: The list of groups to which you want to add the things that triggered the mitigation action. You can add a thing to a maximum of 10 groups, but you can't add a thing to more than one group in the same hierarchy.
            :param override_dynamic_groups: Specifies if this mitigation action can move the things that triggered the mitigation action even if they are part of one or more dynamic thing groups.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-addthingstothinggroupparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                add_things_to_thing_group_params_property = iot.CfnMitigationAction.AddThingsToThingGroupParamsProperty(
                    thing_group_names=["thingGroupNames"],
                
                    # the properties below are optional
                    override_dynamic_groups=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnMitigationAction.AddThingsToThingGroupParamsProperty.__init__)
                check_type(argname="argument thing_group_names", value=thing_group_names, expected_type=type_hints["thing_group_names"])
                check_type(argname="argument override_dynamic_groups", value=override_dynamic_groups, expected_type=type_hints["override_dynamic_groups"])
            self._values: typing.Dict[str, typing.Any] = {
                "thing_group_names": thing_group_names,
            }
            if override_dynamic_groups is not None:
                self._values["override_dynamic_groups"] = override_dynamic_groups

        @builtins.property
        def thing_group_names(self) -> typing.List[builtins.str]:
            '''The list of groups to which you want to add the things that triggered the mitigation action.

            You can add a thing to a maximum of 10 groups, but you can't add a thing to more than one group in the same hierarchy.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-addthingstothinggroupparams.html#cfn-iot-mitigationaction-addthingstothinggroupparams-thinggroupnames
            '''
            result = self._values.get("thing_group_names")
            assert result is not None, "Required property 'thing_group_names' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def override_dynamic_groups(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies if this mitigation action can move the things that triggered the mitigation action even if they are part of one or more dynamic thing groups.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-addthingstothinggroupparams.html#cfn-iot-mitigationaction-addthingstothinggroupparams-overridedynamicgroups
            '''
            result = self._values.get("override_dynamic_groups")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddThingsToThingGroupParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnMitigationAction.EnableIoTLoggingParamsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_level": "logLevel",
            "role_arn_for_logging": "roleArnForLogging",
        },
    )
    class EnableIoTLoggingParamsProperty:
        def __init__(
            self,
            *,
            log_level: builtins.str,
            role_arn_for_logging: builtins.str,
        ) -> None:
            '''Parameters used when defining a mitigation action that enable AWS IoT Core logging.

            :param log_level: Specifies the type of information to be logged.
            :param role_arn_for_logging: The Amazon Resource Name (ARN) of the IAM role used for logging.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-enableiotloggingparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                enable_io_tLogging_params_property = iot.CfnMitigationAction.EnableIoTLoggingParamsProperty(
                    log_level="logLevel",
                    role_arn_for_logging="roleArnForLogging"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnMitigationAction.EnableIoTLoggingParamsProperty.__init__)
                check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
                check_type(argname="argument role_arn_for_logging", value=role_arn_for_logging, expected_type=type_hints["role_arn_for_logging"])
            self._values: typing.Dict[str, typing.Any] = {
                "log_level": log_level,
                "role_arn_for_logging": role_arn_for_logging,
            }

        @builtins.property
        def log_level(self) -> builtins.str:
            '''Specifies the type of information to be logged.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-enableiotloggingparams.html#cfn-iot-mitigationaction-enableiotloggingparams-loglevel
            '''
            result = self._values.get("log_level")
            assert result is not None, "Required property 'log_level' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn_for_logging(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the IAM role used for logging.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-enableiotloggingparams.html#cfn-iot-mitigationaction-enableiotloggingparams-rolearnforlogging
            '''
            result = self._values.get("role_arn_for_logging")
            assert result is not None, "Required property 'role_arn_for_logging' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnableIoTLoggingParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnMitigationAction.PublishFindingToSnsParamsProperty",
        jsii_struct_bases=[],
        name_mapping={"topic_arn": "topicArn"},
    )
    class PublishFindingToSnsParamsProperty:
        def __init__(self, *, topic_arn: builtins.str) -> None:
            '''Parameters to define a mitigation action that publishes findings to Amazon SNS.

            You can implement your own custom actions in response to the Amazon SNS messages.

            :param topic_arn: The ARN of the topic to which you want to publish the findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-publishfindingtosnsparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                publish_finding_to_sns_params_property = iot.CfnMitigationAction.PublishFindingToSnsParamsProperty(
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnMitigationAction.PublishFindingToSnsParamsProperty.__init__)
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "topic_arn": topic_arn,
            }

        @builtins.property
        def topic_arn(self) -> builtins.str:
            '''The ARN of the topic to which you want to publish the findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-publishfindingtosnsparams.html#cfn-iot-mitigationaction-publishfindingtosnsparams-topicarn
            '''
            result = self._values.get("topic_arn")
            assert result is not None, "Required property 'topic_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PublishFindingToSnsParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty",
        jsii_struct_bases=[],
        name_mapping={"template_name": "templateName"},
    )
    class ReplaceDefaultPolicyVersionParamsProperty:
        def __init__(self, *, template_name: builtins.str) -> None:
            '''Parameters to define a mitigation action that adds a blank policy to restrict permissions.

            :param template_name: The name of the template to be applied. The only supported value is ``BLANK_POLICY`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-replacedefaultpolicyversionparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                replace_default_policy_version_params_property = iot.CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty(
                    template_name="templateName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty.__init__)
                check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
            self._values: typing.Dict[str, typing.Any] = {
                "template_name": template_name,
            }

        @builtins.property
        def template_name(self) -> builtins.str:
            '''The name of the template to be applied.

            The only supported value is ``BLANK_POLICY`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-replacedefaultpolicyversionparams.html#cfn-iot-mitigationaction-replacedefaultpolicyversionparams-templatename
            '''
            result = self._values.get("template_name")
            assert result is not None, "Required property 'template_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReplaceDefaultPolicyVersionParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnMitigationAction.UpdateCACertificateParamsProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action"},
    )
    class UpdateCACertificateParamsProperty:
        def __init__(self, *, action: builtins.str) -> None:
            '''Parameters to define a mitigation action that changes the state of the CA certificate to inactive.

            :param action: The action that you want to apply to the CA certificate. The only supported value is ``DEACTIVATE`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-updatecacertificateparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                update_cACertificate_params_property = iot.CfnMitigationAction.UpdateCACertificateParamsProperty(
                    action="action"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnMitigationAction.UpdateCACertificateParamsProperty.__init__)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            self._values: typing.Dict[str, typing.Any] = {
                "action": action,
            }

        @builtins.property
        def action(self) -> builtins.str:
            '''The action that you want to apply to the CA certificate.

            The only supported value is ``DEACTIVATE`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-updatecacertificateparams.html#cfn-iot-mitigationaction-updatecacertificateparams-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpdateCACertificateParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnMitigationAction.UpdateDeviceCertificateParamsProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action"},
    )
    class UpdateDeviceCertificateParamsProperty:
        def __init__(self, *, action: builtins.str) -> None:
            '''Parameters to define a mitigation action that changes the state of the device certificate to inactive.

            :param action: The action that you want to apply to the device certificate. The only supported value is ``DEACTIVATE`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-updatedevicecertificateparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                update_device_certificate_params_property = iot.CfnMitigationAction.UpdateDeviceCertificateParamsProperty(
                    action="action"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnMitigationAction.UpdateDeviceCertificateParamsProperty.__init__)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            self._values: typing.Dict[str, typing.Any] = {
                "action": action,
            }

        @builtins.property
        def action(self) -> builtins.str:
            '''The action that you want to apply to the device certificate.

            The only supported value is ``DEACTIVATE`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-updatedevicecertificateparams.html#cfn-iot-mitigationaction-updatedevicecertificateparams-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpdateDeviceCertificateParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnMitigationActionProps",
    jsii_struct_bases=[],
    name_mapping={
        "action_params": "actionParams",
        "role_arn": "roleArn",
        "action_name": "actionName",
        "tags": "tags",
    },
)
class CfnMitigationActionProps:
    def __init__(
        self,
        *,
        action_params: typing.Union[typing.Union[CfnMitigationAction.ActionParamsProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        role_arn: builtins.str,
        action_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMitigationAction``.

        :param action_params: The set of parameters for this mitigation action. The parameters vary, depending on the kind of action you apply.
        :param role_arn: The IAM role ARN used to apply this mitigation action.
        :param action_name: The friendly name of the mitigation action.
        :param tags: Metadata that can be used to manage the mitigation action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_mitigation_action_props = iot.CfnMitigationActionProps(
                action_params=iot.CfnMitigationAction.ActionParamsProperty(
                    add_things_to_thing_group_params=iot.CfnMitigationAction.AddThingsToThingGroupParamsProperty(
                        thing_group_names=["thingGroupNames"],
            
                        # the properties below are optional
                        override_dynamic_groups=False
                    ),
                    enable_io_tLogging_params=iot.CfnMitigationAction.EnableIoTLoggingParamsProperty(
                        log_level="logLevel",
                        role_arn_for_logging="roleArnForLogging"
                    ),
                    publish_finding_to_sns_params=iot.CfnMitigationAction.PublishFindingToSnsParamsProperty(
                        topic_arn="topicArn"
                    ),
                    replace_default_policy_version_params=iot.CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty(
                        template_name="templateName"
                    ),
                    update_ca_certificate_params=iot.CfnMitigationAction.UpdateCACertificateParamsProperty(
                        action="action"
                    ),
                    update_device_certificate_params=iot.CfnMitigationAction.UpdateDeviceCertificateParamsProperty(
                        action="action"
                    )
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                action_name="actionName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnMitigationActionProps.__init__)
            check_type(argname="argument action_params", value=action_params, expected_type=type_hints["action_params"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "action_params": action_params,
            "role_arn": role_arn,
        }
        if action_name is not None:
            self._values["action_name"] = action_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def action_params(
        self,
    ) -> typing.Union[CfnMitigationAction.ActionParamsProperty, _IResolvable_da3f097b]:
        '''The set of parameters for this mitigation action.

        The parameters vary, depending on the kind of action you apply.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionparams
        '''
        result = self._values.get("action_params")
        assert result is not None, "Required property 'action_params' is missing"
        return typing.cast(typing.Union[CfnMitigationAction.ActionParamsProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The IAM role ARN used to apply this mitigation action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action_name(self) -> typing.Optional[builtins.str]:
        '''The friendly name of the mitigation action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionname
        '''
        result = self._values.get("action_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata that can be used to manage the mitigation action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMitigationActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnPolicy",
):
    '''A CloudFormation ``AWS::IoT::Policy``.

    Use the ``AWS::IoT::Policy`` resource to declare an AWS IoT policy. For more information about working with AWS IoT policies, see `Authorization <https://docs.aws.amazon.com/iot/latest/developerguide/authorization.html>`_ in the *AWS IoT Developer Guide* .

    :cloudformationResource: AWS::IoT::Policy
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        # policy_document: Any
        
        cfn_policy = iot.CfnPolicy(self, "MyCfnPolicy",
            policy_document=policy_document,
        
            # the properties below are optional
            policy_name="policyName"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        policy_document: typing.Any,
        policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::Policy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param policy_document: The JSON document that describes the policy.
        :param policy_name: The policy name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPolicyProps(
            policy_document=policy_document, policy_name=policy_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPolicy.inspect)
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
            type_hints = typing.get_type_hints(CfnPolicy._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AWS IoT policy, such as ``arn:aws:iot:us-east-2:123456789012:policy/MyPolicy`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''The JSON document that describes the policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html#cfn-iot-policy-policydocument
        '''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPolicy, "policy_document").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''The policy name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html#cfn-iot-policy-policyname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPolicy, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)


@jsii.implements(_IInspectable_c2943556)
class CfnPolicyPrincipalAttachment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnPolicyPrincipalAttachment",
):
    '''A CloudFormation ``AWS::IoT::PolicyPrincipalAttachment``.

    Use the ``AWS::IoT::PolicyPrincipalAttachment`` resource to attach an AWS IoT policy to a principal (an X.509 certificate or other credential).

    For information about working with AWS IoT policies and principals, see `Authorization <https://docs.aws.amazon.com/iot/latest/developerguide/authorization.html>`_ in the *AWS IoT Developer Guide* .

    :cloudformationResource: AWS::IoT::PolicyPrincipalAttachment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_policy_principal_attachment = iot.CfnPolicyPrincipalAttachment(self, "MyCfnPolicyPrincipalAttachment",
            policy_name="policyName",
            principal="principal"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        policy_name: builtins.str,
        principal: builtins.str,
    ) -> None:
        '''Create a new ``AWS::IoT::PolicyPrincipalAttachment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param policy_name: The name of the AWS IoT policy.
        :param principal: The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPolicyPrincipalAttachment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPolicyPrincipalAttachmentProps(
            policy_name=policy_name, principal=principal
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPolicyPrincipalAttachment.inspect)
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
            type_hints = typing.get_type_hints(CfnPolicyPrincipalAttachment._render_properties)
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
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of the AWS IoT policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html#cfn-iot-policyprincipalattachment-policyname
        '''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPolicyPrincipalAttachment, "policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        '''The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html#cfn-iot-policyprincipalattachment-principal
        '''
        return typing.cast(builtins.str, jsii.get(self, "principal"))

    @principal.setter
    def principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnPolicyPrincipalAttachment, "principal").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnPolicyPrincipalAttachmentProps",
    jsii_struct_bases=[],
    name_mapping={"policy_name": "policyName", "principal": "principal"},
)
class CfnPolicyPrincipalAttachmentProps:
    def __init__(self, *, policy_name: builtins.str, principal: builtins.str) -> None:
        '''Properties for defining a ``CfnPolicyPrincipalAttachment``.

        :param policy_name: The name of the AWS IoT policy.
        :param principal: The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_policy_principal_attachment_props = iot.CfnPolicyPrincipalAttachmentProps(
                policy_name="policyName",
                principal="principal"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPolicyPrincipalAttachmentProps.__init__)
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
        self._values: typing.Dict[str, typing.Any] = {
            "policy_name": policy_name,
            "principal": principal,
        }

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The name of the AWS IoT policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html#cfn-iot-policyprincipalattachment-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal(self) -> builtins.str:
        '''The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html#cfn-iot-policyprincipalattachment-principal
        '''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPolicyPrincipalAttachmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"policy_document": "policyDocument", "policy_name": "policyName"},
)
class CfnPolicyProps:
    def __init__(
        self,
        *,
        policy_document: typing.Any,
        policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPolicy``.

        :param policy_document: The JSON document that describes the policy.
        :param policy_name: The policy name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            # policy_document: Any
            
            cfn_policy_props = iot.CfnPolicyProps(
                policy_document=policy_document,
            
                # the properties below are optional
                policy_name="policyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnPolicyProps.__init__)
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "policy_document": policy_document,
        }
        if policy_name is not None:
            self._values["policy_name"] = policy_name

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''The JSON document that describes the policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html#cfn-iot-policy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''The policy name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html#cfn-iot-policy-policyname
        '''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnProvisioningTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnProvisioningTemplate",
):
    '''A CloudFormation ``AWS::IoT::ProvisioningTemplate``.

    Creates a fleet provisioning template.

    :cloudformationResource: AWS::IoT::ProvisioningTemplate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_provisioning_template = iot.CfnProvisioningTemplate(self, "MyCfnProvisioningTemplate",
            provisioning_role_arn="provisioningRoleArn",
            template_body="templateBody",
        
            # the properties below are optional
            description="description",
            enabled=False,
            pre_provisioning_hook=iot.CfnProvisioningTemplate.ProvisioningHookProperty(
                payload_version="payloadVersion",
                target_arn="targetArn"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            template_name="templateName",
            template_type="templateType"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        provisioning_role_arn: builtins.str,
        template_body: builtins.str,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        pre_provisioning_hook: typing.Optional[typing.Union[typing.Union["CfnProvisioningTemplate.ProvisioningHookProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        template_name: typing.Optional[builtins.str] = None,
        template_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::ProvisioningTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param provisioning_role_arn: The role ARN for the role associated with the fleet provisioning template. This IoT role grants permission to provision a device.
        :param template_body: The JSON formatted contents of the fleet provisioning template version.
        :param description: The description of the fleet provisioning template.
        :param enabled: True to enable the fleet provisioning template, otherwise false.
        :param pre_provisioning_hook: Creates a pre-provisioning hook template.
        :param tags: Metadata that can be used to manage the fleet provisioning template.
        :param template_name: The name of the fleet provisioning template.
        :param template_type: ``AWS::IoT::ProvisioningTemplate.TemplateType``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnProvisioningTemplate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProvisioningTemplateProps(
            provisioning_role_arn=provisioning_role_arn,
            template_body=template_body,
            description=description,
            enabled=enabled,
            pre_provisioning_hook=pre_provisioning_hook,
            tags=tags,
            template_name=template_name,
            template_type=template_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnProvisioningTemplate.inspect)
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
            type_hints = typing.get_type_hints(CfnProvisioningTemplate._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrTemplateArn")
    def attr_template_arn(self) -> builtins.str:
        '''The ARN that identifies the provisioning template.

        :cloudformationAttribute: TemplateArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTemplateArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata that can be used to manage the fleet provisioning template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="provisioningRoleArn")
    def provisioning_role_arn(self) -> builtins.str:
        '''The role ARN for the role associated with the fleet provisioning template.

        This IoT role grants permission to provision a device.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-provisioningrolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "provisioningRoleArn"))

    @provisioning_role_arn.setter
    def provisioning_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnProvisioningTemplate, "provisioning_role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioningRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="templateBody")
    def template_body(self) -> builtins.str:
        '''The JSON formatted contents of the fleet provisioning template version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatebody
        '''
        return typing.cast(builtins.str, jsii.get(self, "templateBody"))

    @template_body.setter
    def template_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnProvisioningTemplate, "template_body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateBody", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the fleet provisioning template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnProvisioningTemplate, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''True to enable the fleet provisioning template, otherwise false.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnProvisioningTemplate, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="preProvisioningHook")
    def pre_provisioning_hook(
        self,
    ) -> typing.Optional[typing.Union["CfnProvisioningTemplate.ProvisioningHookProperty", _IResolvable_da3f097b]]:
        '''Creates a pre-provisioning hook template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-preprovisioninghook
        '''
        return typing.cast(typing.Optional[typing.Union["CfnProvisioningTemplate.ProvisioningHookProperty", _IResolvable_da3f097b]], jsii.get(self, "preProvisioningHook"))

    @pre_provisioning_hook.setter
    def pre_provisioning_hook(
        self,
        value: typing.Optional[typing.Union["CfnProvisioningTemplate.ProvisioningHookProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnProvisioningTemplate, "pre_provisioning_hook").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preProvisioningHook", value)

    @builtins.property
    @jsii.member(jsii_name="templateName")
    def template_name(self) -> typing.Optional[builtins.str]:
        '''The name of the fleet provisioning template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateName"))

    @template_name.setter
    def template_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnProvisioningTemplate, "template_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateName", value)

    @builtins.property
    @jsii.member(jsii_name="templateType")
    def template_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoT::ProvisioningTemplate.TemplateType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateType"))

    @template_type.setter
    def template_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnProvisioningTemplate, "template_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateType", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnProvisioningTemplate.ProvisioningHookProperty",
        jsii_struct_bases=[],
        name_mapping={"payload_version": "payloadVersion", "target_arn": "targetArn"},
    )
    class ProvisioningHookProperty:
        def __init__(
            self,
            *,
            payload_version: typing.Optional[builtins.str] = None,
            target_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Structure that contains payloadVersion and targetArn.

            Provisioning hooks can be used when fleet provisioning to validate device parameters before allowing the device to be provisioned.

            :param payload_version: The payload that was sent to the target function. The valid payload is ``"2020-04-01"`` .
            :param target_arn: The ARN of the target function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-provisioningtemplate-provisioninghook.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                provisioning_hook_property = iot.CfnProvisioningTemplate.ProvisioningHookProperty(
                    payload_version="payloadVersion",
                    target_arn="targetArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnProvisioningTemplate.ProvisioningHookProperty.__init__)
                check_type(argname="argument payload_version", value=payload_version, expected_type=type_hints["payload_version"])
                check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            self._values: typing.Dict[str, typing.Any] = {}
            if payload_version is not None:
                self._values["payload_version"] = payload_version
            if target_arn is not None:
                self._values["target_arn"] = target_arn

        @builtins.property
        def payload_version(self) -> typing.Optional[builtins.str]:
            '''The payload that was sent to the target function.

            The valid payload is ``"2020-04-01"`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-provisioningtemplate-provisioninghook.html#cfn-iot-provisioningtemplate-provisioninghook-payloadversion
            '''
            result = self._values.get("payload_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the target function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-provisioningtemplate-provisioninghook.html#cfn-iot-provisioningtemplate-provisioninghook-targetarn
            '''
            result = self._values.get("target_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisioningHookProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnProvisioningTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "provisioning_role_arn": "provisioningRoleArn",
        "template_body": "templateBody",
        "description": "description",
        "enabled": "enabled",
        "pre_provisioning_hook": "preProvisioningHook",
        "tags": "tags",
        "template_name": "templateName",
        "template_type": "templateType",
    },
)
class CfnProvisioningTemplateProps:
    def __init__(
        self,
        *,
        provisioning_role_arn: builtins.str,
        template_body: builtins.str,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        pre_provisioning_hook: typing.Optional[typing.Union[typing.Union[CfnProvisioningTemplate.ProvisioningHookProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        template_name: typing.Optional[builtins.str] = None,
        template_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnProvisioningTemplate``.

        :param provisioning_role_arn: The role ARN for the role associated with the fleet provisioning template. This IoT role grants permission to provision a device.
        :param template_body: The JSON formatted contents of the fleet provisioning template version.
        :param description: The description of the fleet provisioning template.
        :param enabled: True to enable the fleet provisioning template, otherwise false.
        :param pre_provisioning_hook: Creates a pre-provisioning hook template.
        :param tags: Metadata that can be used to manage the fleet provisioning template.
        :param template_name: The name of the fleet provisioning template.
        :param template_type: ``AWS::IoT::ProvisioningTemplate.TemplateType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_provisioning_template_props = iot.CfnProvisioningTemplateProps(
                provisioning_role_arn="provisioningRoleArn",
                template_body="templateBody",
            
                # the properties below are optional
                description="description",
                enabled=False,
                pre_provisioning_hook=iot.CfnProvisioningTemplate.ProvisioningHookProperty(
                    payload_version="payloadVersion",
                    target_arn="targetArn"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                template_name="templateName",
                template_type="templateType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnProvisioningTemplateProps.__init__)
            check_type(argname="argument provisioning_role_arn", value=provisioning_role_arn, expected_type=type_hints["provisioning_role_arn"])
            check_type(argname="argument template_body", value=template_body, expected_type=type_hints["template_body"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument pre_provisioning_hook", value=pre_provisioning_hook, expected_type=type_hints["pre_provisioning_hook"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
            check_type(argname="argument template_type", value=template_type, expected_type=type_hints["template_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "provisioning_role_arn": provisioning_role_arn,
            "template_body": template_body,
        }
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if pre_provisioning_hook is not None:
            self._values["pre_provisioning_hook"] = pre_provisioning_hook
        if tags is not None:
            self._values["tags"] = tags
        if template_name is not None:
            self._values["template_name"] = template_name
        if template_type is not None:
            self._values["template_type"] = template_type

    @builtins.property
    def provisioning_role_arn(self) -> builtins.str:
        '''The role ARN for the role associated with the fleet provisioning template.

        This IoT role grants permission to provision a device.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-provisioningrolearn
        '''
        result = self._values.get("provisioning_role_arn")
        assert result is not None, "Required property 'provisioning_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_body(self) -> builtins.str:
        '''The JSON formatted contents of the fleet provisioning template version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatebody
        '''
        result = self._values.get("template_body")
        assert result is not None, "Required property 'template_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the fleet provisioning template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''True to enable the fleet provisioning template, otherwise false.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def pre_provisioning_hook(
        self,
    ) -> typing.Optional[typing.Union[CfnProvisioningTemplate.ProvisioningHookProperty, _IResolvable_da3f097b]]:
        '''Creates a pre-provisioning hook template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-preprovisioninghook
        '''
        result = self._values.get("pre_provisioning_hook")
        return typing.cast(typing.Optional[typing.Union[CfnProvisioningTemplate.ProvisioningHookProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata that can be used to manage the fleet provisioning template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def template_name(self) -> typing.Optional[builtins.str]:
        '''The name of the fleet provisioning template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatename
        '''
        result = self._values.get("template_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoT::ProvisioningTemplate.TemplateType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatetype
        '''
        result = self._values.get("template_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProvisioningTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourceSpecificLogging(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnResourceSpecificLogging",
):
    '''A CloudFormation ``AWS::IoT::ResourceSpecificLogging``.

    Configure resource-specific logging.

    :cloudformationResource: AWS::IoT::ResourceSpecificLogging
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_resource_specific_logging = iot.CfnResourceSpecificLogging(self, "MyCfnResourceSpecificLogging",
            log_level="logLevel",
            target_name="targetName",
            target_type="targetType"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        log_level: builtins.str,
        target_name: builtins.str,
        target_type: builtins.str,
    ) -> None:
        '''Create a new ``AWS::IoT::ResourceSpecificLogging``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param log_level: The default log level.Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``.
        :param target_name: The target name.
        :param target_type: The target type. Valid Values: ``DEFAULT | THING_GROUP``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnResourceSpecificLogging.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceSpecificLoggingProps(
            log_level=log_level, target_name=target_name, target_type=target_type
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnResourceSpecificLogging.inspect)
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
            type_hints = typing.get_type_hints(CfnResourceSpecificLogging._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrTargetId")
    def attr_target_id(self) -> builtins.str:
        '''The target Id.

        :cloudformationAttribute: TargetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTargetId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> builtins.str:
        '''The default log level.Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html#cfn-iot-resourcespecificlogging-loglevel
        '''
        return typing.cast(builtins.str, jsii.get(self, "logLevel"))

    @log_level.setter
    def log_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResourceSpecificLogging, "log_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logLevel", value)

    @builtins.property
    @jsii.member(jsii_name="targetName")
    def target_name(self) -> builtins.str:
        '''The target name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html#cfn-iot-resourcespecificlogging-targetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetName"))

    @target_name.setter
    def target_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResourceSpecificLogging, "target_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetName", value)

    @builtins.property
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> builtins.str:
        '''The target type.

        Valid Values: ``DEFAULT | THING_GROUP``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html#cfn-iot-resourcespecificlogging-targettype
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnResourceSpecificLogging, "target_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetType", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnResourceSpecificLoggingProps",
    jsii_struct_bases=[],
    name_mapping={
        "log_level": "logLevel",
        "target_name": "targetName",
        "target_type": "targetType",
    },
)
class CfnResourceSpecificLoggingProps:
    def __init__(
        self,
        *,
        log_level: builtins.str,
        target_name: builtins.str,
        target_type: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnResourceSpecificLogging``.

        :param log_level: The default log level.Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``.
        :param target_name: The target name.
        :param target_type: The target type. Valid Values: ``DEFAULT | THING_GROUP``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_resource_specific_logging_props = iot.CfnResourceSpecificLoggingProps(
                log_level="logLevel",
                target_name="targetName",
                target_type="targetType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnResourceSpecificLoggingProps.__init__)
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            check_type(argname="argument target_name", value=target_name, expected_type=type_hints["target_name"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "log_level": log_level,
            "target_name": target_name,
            "target_type": target_type,
        }

    @builtins.property
    def log_level(self) -> builtins.str:
        '''The default log level.Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html#cfn-iot-resourcespecificlogging-loglevel
        '''
        result = self._values.get("log_level")
        assert result is not None, "Required property 'log_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_name(self) -> builtins.str:
        '''The target name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html#cfn-iot-resourcespecificlogging-targetname
        '''
        result = self._values.get("target_name")
        assert result is not None, "Required property 'target_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_type(self) -> builtins.str:
        '''The target type.

        Valid Values: ``DEFAULT | THING_GROUP``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html#cfn-iot-resourcespecificlogging-targettype
        '''
        result = self._values.get("target_type")
        assert result is not None, "Required property 'target_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceSpecificLoggingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnRoleAlias(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnRoleAlias",
):
    '''A CloudFormation ``AWS::IoT::RoleAlias``.

    Specifies a role alias.

    Requires permission to access the `CreateRoleAlias <https://docs.aws.amazon.com//service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions>`_ action.

    :cloudformationResource: AWS::IoT::RoleAlias
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_role_alias = iot.CfnRoleAlias(self, "MyCfnRoleAlias",
            role_arn="roleArn",
        
            # the properties below are optional
            credential_duration_seconds=123,
            role_alias="roleAlias",
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
        role_arn: builtins.str,
        credential_duration_seconds: typing.Optional[jsii.Number] = None,
        role_alias: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::RoleAlias``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param role_arn: The role ARN.
        :param credential_duration_seconds: The number of seconds for which the credential is valid.
        :param role_alias: The role alias.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnRoleAlias.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRoleAliasProps(
            role_arn=role_arn,
            credential_duration_seconds=credential_duration_seconds,
            role_alias=role_alias,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnRoleAlias.inspect)
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
            type_hints = typing.get_type_hints(CfnRoleAlias._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRoleAliasArn")
    def attr_role_alias_arn(self) -> builtins.str:
        '''The role alias ARN.

        :cloudformationAttribute: RoleAliasArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRoleAliasArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The role ARN.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnRoleAlias, "role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="credentialDurationSeconds")
    def credential_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds for which the credential is valid.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-credentialdurationseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "credentialDurationSeconds"))

    @credential_duration_seconds.setter
    def credential_duration_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnRoleAlias, "credential_duration_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialDurationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="roleAlias")
    def role_alias(self) -> typing.Optional[builtins.str]:
        '''The role alias.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-rolealias
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleAlias"))

    @role_alias.setter
    def role_alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnRoleAlias, "role_alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleAlias", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnRoleAliasProps",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "credential_duration_seconds": "credentialDurationSeconds",
        "role_alias": "roleAlias",
        "tags": "tags",
    },
)
class CfnRoleAliasProps:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        credential_duration_seconds: typing.Optional[jsii.Number] = None,
        role_alias: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRoleAlias``.

        :param role_arn: The role ARN.
        :param credential_duration_seconds: The number of seconds for which the credential is valid.
        :param role_alias: The role alias.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_role_alias_props = iot.CfnRoleAliasProps(
                role_arn="roleArn",
            
                # the properties below are optional
                credential_duration_seconds=123,
                role_alias="roleAlias",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnRoleAliasProps.__init__)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument credential_duration_seconds", value=credential_duration_seconds, expected_type=type_hints["credential_duration_seconds"])
            check_type(argname="argument role_alias", value=role_alias, expected_type=type_hints["role_alias"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "role_arn": role_arn,
        }
        if credential_duration_seconds is not None:
            self._values["credential_duration_seconds"] = credential_duration_seconds
        if role_alias is not None:
            self._values["role_alias"] = role_alias
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The role ARN.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def credential_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds for which the credential is valid.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-credentialdurationseconds
        '''
        result = self._values.get("credential_duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role_alias(self) -> typing.Optional[builtins.str]:
        '''The role alias.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-rolealias
        '''
        result = self._values.get("role_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRoleAliasProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnScheduledAudit(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnScheduledAudit",
):
    '''A CloudFormation ``AWS::IoT::ScheduledAudit``.

    Use the ``AWS::IoT::ScheduledAudit`` resource to create a scheduled audit that is run at a specified time interval. For API reference, see `CreateScheduleAudit <https://docs.aws.amazon.com/iot/latest/apireference/API_CreateScheduledAudit.html>`_ and for general information, see `Audit <https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-audit.html>`_ .

    :cloudformationResource: AWS::IoT::ScheduledAudit
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_scheduled_audit = iot.CfnScheduledAudit(self, "MyCfnScheduledAudit",
            frequency="frequency",
            target_check_names=["targetCheckNames"],
        
            # the properties below are optional
            day_of_month="dayOfMonth",
            day_of_week="dayOfWeek",
            scheduled_audit_name="scheduledAuditName",
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
        frequency: builtins.str,
        target_check_names: typing.Sequence[builtins.str],
        day_of_month: typing.Optional[builtins.str] = None,
        day_of_week: typing.Optional[builtins.str] = None,
        scheduled_audit_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::ScheduledAudit``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param frequency: How often the scheduled audit occurs.
        :param target_check_names: Which checks are performed during the scheduled audit. Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are enabled.) The following checks are currently aviable: - ``AUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK`` - ``CA_CERTIFICATE_EXPIRING_CHECK`` - ``CA_CERTIFICATE_KEY_QUALITY_CHECK`` - ``CONFLICTING_CLIENT_IDS_CHECK`` - ``DEVICE_CERTIFICATE_EXPIRING_CHECK`` - ``DEVICE_CERTIFICATE_KEY_QUALITY_CHECK`` - ``DEVICE_CERTIFICATE_SHARED_CHECK`` - ``IOT_POLICY_OVERLY_PERMISSIVE_CHECK`` - ``IOT_ROLE_ALIAS_ALLOWS_ACCESS_TO_UNUSED_SERVICES_CHECK`` - ``IOT_ROLE_ALIAS_OVERLY_PERMISSIVE_CHECK`` - ``LOGGING_DISABLED_CHECK`` - ``REVOKED_CA_CERTIFICATE_STILL_ACTIVE_CHECK`` - ``REVOKED_DEVICE_CERTIFICATE_STILL_ACTIVE_CHECK`` - ``UNAUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK``
        :param day_of_month: The day of the month on which the scheduled audit is run (if the ``frequency`` is "MONTHLY"). If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.
        :param day_of_week: The day of the week on which the scheduled audit is run (if the ``frequency`` is "WEEKLY" or "BIWEEKLY").
        :param scheduled_audit_name: The name of the scheduled audit.
        :param tags: Metadata that can be used to manage the scheduled audit.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnScheduledAudit.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScheduledAuditProps(
            frequency=frequency,
            target_check_names=target_check_names,
            day_of_month=day_of_month,
            day_of_week=day_of_week,
            scheduled_audit_name=scheduled_audit_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnScheduledAudit.inspect)
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
            type_hints = typing.get_type_hints(CfnScheduledAudit._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrScheduledAuditArn")
    def attr_scheduled_audit_arn(self) -> builtins.str:
        '''The ARN of the scheduled audit.

        :cloudformationAttribute: ScheduledAuditArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrScheduledAuditArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata that can be used to manage the scheduled audit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        '''How often the scheduled audit occurs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-frequency
        '''
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnScheduledAudit, "frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="targetCheckNames")
    def target_check_names(self) -> typing.List[builtins.str]:
        '''Which checks are performed during the scheduled audit.

        Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)

        The following checks are currently aviable:

        - ``AUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK``
        - ``CA_CERTIFICATE_EXPIRING_CHECK``
        - ``CA_CERTIFICATE_KEY_QUALITY_CHECK``
        - ``CONFLICTING_CLIENT_IDS_CHECK``
        - ``DEVICE_CERTIFICATE_EXPIRING_CHECK``
        - ``DEVICE_CERTIFICATE_KEY_QUALITY_CHECK``
        - ``DEVICE_CERTIFICATE_SHARED_CHECK``
        - ``IOT_POLICY_OVERLY_PERMISSIVE_CHECK``
        - ``IOT_ROLE_ALIAS_ALLOWS_ACCESS_TO_UNUSED_SERVICES_CHECK``
        - ``IOT_ROLE_ALIAS_OVERLY_PERMISSIVE_CHECK``
        - ``LOGGING_DISABLED_CHECK``
        - ``REVOKED_CA_CERTIFICATE_STILL_ACTIVE_CHECK``
        - ``REVOKED_DEVICE_CERTIFICATE_STILL_ACTIVE_CHECK``
        - ``UNAUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-targetchecknames
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetCheckNames"))

    @target_check_names.setter
    def target_check_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnScheduledAudit, "target_check_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetCheckNames", value)

    @builtins.property
    @jsii.member(jsii_name="dayOfMonth")
    def day_of_month(self) -> typing.Optional[builtins.str]:
        '''The day of the month on which the scheduled audit is run (if the ``frequency`` is "MONTHLY").

        If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofmonth
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfMonth"))

    @day_of_month.setter
    def day_of_month(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnScheduledAudit, "day_of_month").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfMonth", value)

    @builtins.property
    @jsii.member(jsii_name="dayOfWeek")
    def day_of_week(self) -> typing.Optional[builtins.str]:
        '''The day of the week on which the scheduled audit is run (if the ``frequency`` is "WEEKLY" or "BIWEEKLY").

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofweek
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfWeek"))

    @day_of_week.setter
    def day_of_week(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnScheduledAudit, "day_of_week").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="scheduledAuditName")
    def scheduled_audit_name(self) -> typing.Optional[builtins.str]:
        '''The name of the scheduled audit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-scheduledauditname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduledAuditName"))

    @scheduled_audit_name.setter
    def scheduled_audit_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnScheduledAudit, "scheduled_audit_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduledAuditName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnScheduledAuditProps",
    jsii_struct_bases=[],
    name_mapping={
        "frequency": "frequency",
        "target_check_names": "targetCheckNames",
        "day_of_month": "dayOfMonth",
        "day_of_week": "dayOfWeek",
        "scheduled_audit_name": "scheduledAuditName",
        "tags": "tags",
    },
)
class CfnScheduledAuditProps:
    def __init__(
        self,
        *,
        frequency: builtins.str,
        target_check_names: typing.Sequence[builtins.str],
        day_of_month: typing.Optional[builtins.str] = None,
        day_of_week: typing.Optional[builtins.str] = None,
        scheduled_audit_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnScheduledAudit``.

        :param frequency: How often the scheduled audit occurs.
        :param target_check_names: Which checks are performed during the scheduled audit. Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are enabled.) The following checks are currently aviable: - ``AUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK`` - ``CA_CERTIFICATE_EXPIRING_CHECK`` - ``CA_CERTIFICATE_KEY_QUALITY_CHECK`` - ``CONFLICTING_CLIENT_IDS_CHECK`` - ``DEVICE_CERTIFICATE_EXPIRING_CHECK`` - ``DEVICE_CERTIFICATE_KEY_QUALITY_CHECK`` - ``DEVICE_CERTIFICATE_SHARED_CHECK`` - ``IOT_POLICY_OVERLY_PERMISSIVE_CHECK`` - ``IOT_ROLE_ALIAS_ALLOWS_ACCESS_TO_UNUSED_SERVICES_CHECK`` - ``IOT_ROLE_ALIAS_OVERLY_PERMISSIVE_CHECK`` - ``LOGGING_DISABLED_CHECK`` - ``REVOKED_CA_CERTIFICATE_STILL_ACTIVE_CHECK`` - ``REVOKED_DEVICE_CERTIFICATE_STILL_ACTIVE_CHECK`` - ``UNAUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK``
        :param day_of_month: The day of the month on which the scheduled audit is run (if the ``frequency`` is "MONTHLY"). If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.
        :param day_of_week: The day of the week on which the scheduled audit is run (if the ``frequency`` is "WEEKLY" or "BIWEEKLY").
        :param scheduled_audit_name: The name of the scheduled audit.
        :param tags: Metadata that can be used to manage the scheduled audit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_scheduled_audit_props = iot.CfnScheduledAuditProps(
                frequency="frequency",
                target_check_names=["targetCheckNames"],
            
                # the properties below are optional
                day_of_month="dayOfMonth",
                day_of_week="dayOfWeek",
                scheduled_audit_name="scheduledAuditName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnScheduledAuditProps.__init__)
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument target_check_names", value=target_check_names, expected_type=type_hints["target_check_names"])
            check_type(argname="argument day_of_month", value=day_of_month, expected_type=type_hints["day_of_month"])
            check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
            check_type(argname="argument scheduled_audit_name", value=scheduled_audit_name, expected_type=type_hints["scheduled_audit_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "frequency": frequency,
            "target_check_names": target_check_names,
        }
        if day_of_month is not None:
            self._values["day_of_month"] = day_of_month
        if day_of_week is not None:
            self._values["day_of_week"] = day_of_week
        if scheduled_audit_name is not None:
            self._values["scheduled_audit_name"] = scheduled_audit_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def frequency(self) -> builtins.str:
        '''How often the scheduled audit occurs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-frequency
        '''
        result = self._values.get("frequency")
        assert result is not None, "Required property 'frequency' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_check_names(self) -> typing.List[builtins.str]:
        '''Which checks are performed during the scheduled audit.

        Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)

        The following checks are currently aviable:

        - ``AUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK``
        - ``CA_CERTIFICATE_EXPIRING_CHECK``
        - ``CA_CERTIFICATE_KEY_QUALITY_CHECK``
        - ``CONFLICTING_CLIENT_IDS_CHECK``
        - ``DEVICE_CERTIFICATE_EXPIRING_CHECK``
        - ``DEVICE_CERTIFICATE_KEY_QUALITY_CHECK``
        - ``DEVICE_CERTIFICATE_SHARED_CHECK``
        - ``IOT_POLICY_OVERLY_PERMISSIVE_CHECK``
        - ``IOT_ROLE_ALIAS_ALLOWS_ACCESS_TO_UNUSED_SERVICES_CHECK``
        - ``IOT_ROLE_ALIAS_OVERLY_PERMISSIVE_CHECK``
        - ``LOGGING_DISABLED_CHECK``
        - ``REVOKED_CA_CERTIFICATE_STILL_ACTIVE_CHECK``
        - ``REVOKED_DEVICE_CERTIFICATE_STILL_ACTIVE_CHECK``
        - ``UNAUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-targetchecknames
        '''
        result = self._values.get("target_check_names")
        assert result is not None, "Required property 'target_check_names' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def day_of_month(self) -> typing.Optional[builtins.str]:
        '''The day of the month on which the scheduled audit is run (if the ``frequency`` is "MONTHLY").

        If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofmonth
        '''
        result = self._values.get("day_of_month")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def day_of_week(self) -> typing.Optional[builtins.str]:
        '''The day of the week on which the scheduled audit is run (if the ``frequency`` is "WEEKLY" or "BIWEEKLY").

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofweek
        '''
        result = self._values.get("day_of_week")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduled_audit_name(self) -> typing.Optional[builtins.str]:
        '''The name of the scheduled audit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-scheduledauditname
        '''
        result = self._values.get("scheduled_audit_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata that can be used to manage the scheduled audit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScheduledAuditProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSecurityProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnSecurityProfile",
):
    '''A CloudFormation ``AWS::IoT::SecurityProfile``.

    Use the ``AWS::IoT::SecurityProfile`` resource to create a Device Defender security profile. For API reference, see `CreateSecurityProfile <https://docs.aws.amazon.com/iot/latest/apireference/API_CreateSecurityProfile.html>`_ and for general information, see `Detect <https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-detect.html>`_ .

    :cloudformationResource: AWS::IoT::SecurityProfile
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_security_profile = iot.CfnSecurityProfile(self, "MyCfnSecurityProfile",
            additional_metrics_to_retain_v2=[iot.CfnSecurityProfile.MetricToRetainProperty(
                metric="metric",
        
                # the properties below are optional
                metric_dimension=iot.CfnSecurityProfile.MetricDimensionProperty(
                    dimension_name="dimensionName",
        
                    # the properties below are optional
                    operator="operator"
                )
            )],
            alert_targets={
                "alert_targets_key": iot.CfnSecurityProfile.AlertTargetProperty(
                    alert_target_arn="alertTargetArn",
                    role_arn="roleArn"
                )
            },
            behaviors=[iot.CfnSecurityProfile.BehaviorProperty(
                name="name",
        
                # the properties below are optional
                criteria=iot.CfnSecurityProfile.BehaviorCriteriaProperty(
                    comparison_operator="comparisonOperator",
                    consecutive_datapoints_to_alarm=123,
                    consecutive_datapoints_to_clear=123,
                    duration_seconds=123,
                    ml_detection_config=iot.CfnSecurityProfile.MachineLearningDetectionConfigProperty(
                        confidence_level="confidenceLevel"
                    ),
                    statistical_threshold=iot.CfnSecurityProfile.StatisticalThresholdProperty(
                        statistic="statistic"
                    ),
                    value=iot.CfnSecurityProfile.MetricValueProperty(
                        cidrs=["cidrs"],
                        count="count",
                        number=123,
                        numbers=[123],
                        ports=[123],
                        strings=["strings"]
                    )
                ),
                metric="metric",
                metric_dimension=iot.CfnSecurityProfile.MetricDimensionProperty(
                    dimension_name="dimensionName",
        
                    # the properties below are optional
                    operator="operator"
                ),
                suppress_alerts=False
            )],
            security_profile_description="securityProfileDescription",
            security_profile_name="securityProfileName",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            target_arns=["targetArns"]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        additional_metrics_to_retain_v2: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnSecurityProfile.MetricToRetainProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        alert_targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union["CfnSecurityProfile.AlertTargetProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        behaviors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnSecurityProfile.BehaviorProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        security_profile_description: typing.Optional[builtins.str] = None,
        security_profile_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        target_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::SecurityProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param additional_metrics_to_retain_v2: A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's ``behaviors`` , but it's also retained for any metric specified here. Can be used with custom metrics; can't be used with dimensions.
        :param alert_targets: Specifies the destinations to which alerts are sent. (Alerts are always sent to the console.) Alerts are generated when a device (thing) violates a behavior.
        :param behaviors: Specifies the behaviors that, when violated by a device (thing), cause an alert.
        :param security_profile_description: A description of the security profile.
        :param security_profile_name: The name you gave to the security profile.
        :param tags: Metadata that can be used to manage the security profile.
        :param target_arns: The ARN of the target (thing group) to which the security profile is attached.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSecurityProfile.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSecurityProfileProps(
            additional_metrics_to_retain_v2=additional_metrics_to_retain_v2,
            alert_targets=alert_targets,
            behaviors=behaviors,
            security_profile_description=security_profile_description,
            security_profile_name=security_profile_name,
            tags=tags,
            target_arns=target_arns,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSecurityProfile.inspect)
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
            type_hints = typing.get_type_hints(CfnSecurityProfile._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrSecurityProfileArn")
    def attr_security_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the security profile.

        :cloudformationAttribute: SecurityProfileArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSecurityProfileArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata that can be used to manage the security profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="additionalMetricsToRetainV2")
    def additional_metrics_to_retain_v2(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSecurityProfile.MetricToRetainProperty", _IResolvable_da3f097b]]]]:
        '''A list of metrics whose data is retained (stored).

        By default, data is retained for any metric used in the profile's ``behaviors`` , but it's also retained for any metric specified here. Can be used with custom metrics; can't be used with dimensions.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-additionalmetricstoretainv2
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSecurityProfile.MetricToRetainProperty", _IResolvable_da3f097b]]]], jsii.get(self, "additionalMetricsToRetainV2"))

    @additional_metrics_to_retain_v2.setter
    def additional_metrics_to_retain_v2(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSecurityProfile.MetricToRetainProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSecurityProfile, "additional_metrics_to_retain_v2").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalMetricsToRetainV2", value)

    @builtins.property
    @jsii.member(jsii_name="alertTargets")
    def alert_targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnSecurityProfile.AlertTargetProperty", _IResolvable_da3f097b]]]]:
        '''Specifies the destinations to which alerts are sent.

        (Alerts are always sent to the console.) Alerts are generated when a device (thing) violates a behavior.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-alerttargets
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnSecurityProfile.AlertTargetProperty", _IResolvable_da3f097b]]]], jsii.get(self, "alertTargets"))

    @alert_targets.setter
    def alert_targets(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union["CfnSecurityProfile.AlertTargetProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSecurityProfile, "alert_targets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alertTargets", value)

    @builtins.property
    @jsii.member(jsii_name="behaviors")
    def behaviors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSecurityProfile.BehaviorProperty", _IResolvable_da3f097b]]]]:
        '''Specifies the behaviors that, when violated by a device (thing), cause an alert.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-behaviors
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSecurityProfile.BehaviorProperty", _IResolvable_da3f097b]]]], jsii.get(self, "behaviors"))

    @behaviors.setter
    def behaviors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSecurityProfile.BehaviorProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSecurityProfile, "behaviors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "behaviors", value)

    @builtins.property
    @jsii.member(jsii_name="securityProfileDescription")
    def security_profile_description(self) -> typing.Optional[builtins.str]:
        '''A description of the security profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-securityprofiledescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityProfileDescription"))

    @security_profile_description.setter
    def security_profile_description(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSecurityProfile, "security_profile_description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityProfileDescription", value)

    @builtins.property
    @jsii.member(jsii_name="securityProfileName")
    def security_profile_name(self) -> typing.Optional[builtins.str]:
        '''The name you gave to the security profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-securityprofilename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityProfileName"))

    @security_profile_name.setter
    def security_profile_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSecurityProfile, "security_profile_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityProfileName", value)

    @builtins.property
    @jsii.member(jsii_name="targetArns")
    def target_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARN of the target (thing group) to which the security profile is attached.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-targetarns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetArns"))

    @target_arns.setter
    def target_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnSecurityProfile, "target_arns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetArns", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnSecurityProfile.AlertTargetProperty",
        jsii_struct_bases=[],
        name_mapping={"alert_target_arn": "alertTargetArn", "role_arn": "roleArn"},
    )
    class AlertTargetProperty:
        def __init__(
            self,
            *,
            alert_target_arn: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''A structure containing the alert target ARN and the role ARN.

            :param alert_target_arn: The Amazon Resource Name (ARN) of the notification target to which alerts are sent.
            :param role_arn: The ARN of the role that grants permission to send alerts to the notification target.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-alerttarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                alert_target_property = iot.CfnSecurityProfile.AlertTargetProperty(
                    alert_target_arn="alertTargetArn",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSecurityProfile.AlertTargetProperty.__init__)
                check_type(argname="argument alert_target_arn", value=alert_target_arn, expected_type=type_hints["alert_target_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "alert_target_arn": alert_target_arn,
                "role_arn": role_arn,
            }

        @builtins.property
        def alert_target_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the notification target to which alerts are sent.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-alerttarget.html#cfn-iot-securityprofile-alerttarget-alerttargetarn
            '''
            result = self._values.get("alert_target_arn")
            assert result is not None, "Required property 'alert_target_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that grants permission to send alerts to the notification target.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-alerttarget.html#cfn-iot-securityprofile-alerttarget-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlertTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnSecurityProfile.BehaviorCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "consecutive_datapoints_to_alarm": "consecutiveDatapointsToAlarm",
            "consecutive_datapoints_to_clear": "consecutiveDatapointsToClear",
            "duration_seconds": "durationSeconds",
            "ml_detection_config": "mlDetectionConfig",
            "statistical_threshold": "statisticalThreshold",
            "value": "value",
        },
    )
    class BehaviorCriteriaProperty:
        def __init__(
            self,
            *,
            comparison_operator: typing.Optional[builtins.str] = None,
            consecutive_datapoints_to_alarm: typing.Optional[jsii.Number] = None,
            consecutive_datapoints_to_clear: typing.Optional[jsii.Number] = None,
            duration_seconds: typing.Optional[jsii.Number] = None,
            ml_detection_config: typing.Optional[typing.Union[typing.Union["CfnSecurityProfile.MachineLearningDetectionConfigProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            statistical_threshold: typing.Optional[typing.Union[typing.Union["CfnSecurityProfile.StatisticalThresholdProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            value: typing.Optional[typing.Union[typing.Union["CfnSecurityProfile.MetricValueProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The criteria by which the behavior is determined to be normal.

            :param comparison_operator: The operator that relates the thing measured ( ``metric`` ) to the criteria (containing a ``value`` or ``statisticalThreshold`` ). Valid operators include: - ``string-list`` : ``in-set`` and ``not-in-set`` - ``number-list`` : ``in-set`` and ``not-in-set`` - ``ip-address-list`` : ``in-cidr-set`` and ``not-in-cidr-set`` - ``number`` : ``less-than`` , ``less-than-equals`` , ``greater-than`` , and ``greater-than-equals``
            :param consecutive_datapoints_to_alarm: If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.
            :param consecutive_datapoints_to_clear: If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.
            :param duration_seconds: Use this to specify the time duration over which the behavior is evaluated, for those criteria that have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank. Cannot be used with list-based metric datatypes.
            :param ml_detection_config: The confidence level of the detection model.
            :param statistical_threshold: A statistical ranking (percentile)that indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.
            :param value: The value to be compared with the ``metric`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                behavior_criteria_property = iot.CfnSecurityProfile.BehaviorCriteriaProperty(
                    comparison_operator="comparisonOperator",
                    consecutive_datapoints_to_alarm=123,
                    consecutive_datapoints_to_clear=123,
                    duration_seconds=123,
                    ml_detection_config=iot.CfnSecurityProfile.MachineLearningDetectionConfigProperty(
                        confidence_level="confidenceLevel"
                    ),
                    statistical_threshold=iot.CfnSecurityProfile.StatisticalThresholdProperty(
                        statistic="statistic"
                    ),
                    value=iot.CfnSecurityProfile.MetricValueProperty(
                        cidrs=["cidrs"],
                        count="count",
                        number=123,
                        numbers=[123],
                        ports=[123],
                        strings=["strings"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSecurityProfile.BehaviorCriteriaProperty.__init__)
                check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
                check_type(argname="argument consecutive_datapoints_to_alarm", value=consecutive_datapoints_to_alarm, expected_type=type_hints["consecutive_datapoints_to_alarm"])
                check_type(argname="argument consecutive_datapoints_to_clear", value=consecutive_datapoints_to_clear, expected_type=type_hints["consecutive_datapoints_to_clear"])
                check_type(argname="argument duration_seconds", value=duration_seconds, expected_type=type_hints["duration_seconds"])
                check_type(argname="argument ml_detection_config", value=ml_detection_config, expected_type=type_hints["ml_detection_config"])
                check_type(argname="argument statistical_threshold", value=statistical_threshold, expected_type=type_hints["statistical_threshold"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[str, typing.Any] = {}
            if comparison_operator is not None:
                self._values["comparison_operator"] = comparison_operator
            if consecutive_datapoints_to_alarm is not None:
                self._values["consecutive_datapoints_to_alarm"] = consecutive_datapoints_to_alarm
            if consecutive_datapoints_to_clear is not None:
                self._values["consecutive_datapoints_to_clear"] = consecutive_datapoints_to_clear
            if duration_seconds is not None:
                self._values["duration_seconds"] = duration_seconds
            if ml_detection_config is not None:
                self._values["ml_detection_config"] = ml_detection_config
            if statistical_threshold is not None:
                self._values["statistical_threshold"] = statistical_threshold
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def comparison_operator(self) -> typing.Optional[builtins.str]:
            '''The operator that relates the thing measured ( ``metric`` ) to the criteria (containing a ``value`` or ``statisticalThreshold`` ).

            Valid operators include:

            - ``string-list`` : ``in-set`` and ``not-in-set``
            - ``number-list`` : ``in-set`` and ``not-in-set``
            - ``ip-address-list`` : ``in-cidr-set`` and ``not-in-cidr-set``
            - ``number`` : ``less-than`` , ``less-than-equals`` , ``greater-than`` , and ``greater-than-equals``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def consecutive_datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
            '''If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs.

            If not specified, the default is 1.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-consecutivedatapointstoalarm
            '''
            result = self._values.get("consecutive_datapoints_to_alarm")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def consecutive_datapoints_to_clear(self) -> typing.Optional[jsii.Number]:
            '''If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared.

            If not specified, the default is 1.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-consecutivedatapointstoclear
            '''
            result = self._values.get("consecutive_datapoints_to_clear")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''Use this to specify the time duration over which the behavior is evaluated, for those criteria that have a time dimension (for example, ``NUM_MESSAGES_SENT`` ).

            For a ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank. Cannot be used with list-based metric datatypes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-durationseconds
            '''
            result = self._values.get("duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ml_detection_config(
            self,
        ) -> typing.Optional[typing.Union["CfnSecurityProfile.MachineLearningDetectionConfigProperty", _IResolvable_da3f097b]]:
            '''The confidence level of the detection model.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-mldetectionconfig
            '''
            result = self._values.get("ml_detection_config")
            return typing.cast(typing.Optional[typing.Union["CfnSecurityProfile.MachineLearningDetectionConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def statistical_threshold(
            self,
        ) -> typing.Optional[typing.Union["CfnSecurityProfile.StatisticalThresholdProperty", _IResolvable_da3f097b]]:
            '''A statistical ranking (percentile)that indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-statisticalthreshold
            '''
            result = self._values.get("statistical_threshold")
            return typing.cast(typing.Optional[typing.Union["CfnSecurityProfile.StatisticalThresholdProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def value(
            self,
        ) -> typing.Optional[typing.Union["CfnSecurityProfile.MetricValueProperty", _IResolvable_da3f097b]]:
            '''The value to be compared with the ``metric`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[typing.Union["CfnSecurityProfile.MetricValueProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BehaviorCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnSecurityProfile.BehaviorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "criteria": "criteria",
            "metric": "metric",
            "metric_dimension": "metricDimension",
            "suppress_alerts": "suppressAlerts",
        },
    )
    class BehaviorProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            criteria: typing.Optional[typing.Union[typing.Union["CfnSecurityProfile.BehaviorCriteriaProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            metric: typing.Optional[builtins.str] = None,
            metric_dimension: typing.Optional[typing.Union[typing.Union["CfnSecurityProfile.MetricDimensionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            suppress_alerts: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''A Device Defender security profile behavior.

            :param name: The name you've given to the behavior.
            :param criteria: The criteria that determine if a device is behaving normally in regard to the ``metric`` .
            :param metric: What is measured by the behavior.
            :param metric_dimension: The dimension of the metric.
            :param suppress_alerts: The alert status. If you set the value to ``true`` , alerts will be suppressed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                behavior_property = iot.CfnSecurityProfile.BehaviorProperty(
                    name="name",
                
                    # the properties below are optional
                    criteria=iot.CfnSecurityProfile.BehaviorCriteriaProperty(
                        comparison_operator="comparisonOperator",
                        consecutive_datapoints_to_alarm=123,
                        consecutive_datapoints_to_clear=123,
                        duration_seconds=123,
                        ml_detection_config=iot.CfnSecurityProfile.MachineLearningDetectionConfigProperty(
                            confidence_level="confidenceLevel"
                        ),
                        statistical_threshold=iot.CfnSecurityProfile.StatisticalThresholdProperty(
                            statistic="statistic"
                        ),
                        value=iot.CfnSecurityProfile.MetricValueProperty(
                            cidrs=["cidrs"],
                            count="count",
                            number=123,
                            numbers=[123],
                            ports=[123],
                            strings=["strings"]
                        )
                    ),
                    metric="metric",
                    metric_dimension=iot.CfnSecurityProfile.MetricDimensionProperty(
                        dimension_name="dimensionName",
                
                        # the properties below are optional
                        operator="operator"
                    ),
                    suppress_alerts=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSecurityProfile.BehaviorProperty.__init__)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument criteria", value=criteria, expected_type=type_hints["criteria"])
                check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
                check_type(argname="argument metric_dimension", value=metric_dimension, expected_type=type_hints["metric_dimension"])
                check_type(argname="argument suppress_alerts", value=suppress_alerts, expected_type=type_hints["suppress_alerts"])
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }
            if criteria is not None:
                self._values["criteria"] = criteria
            if metric is not None:
                self._values["metric"] = metric
            if metric_dimension is not None:
                self._values["metric_dimension"] = metric_dimension
            if suppress_alerts is not None:
                self._values["suppress_alerts"] = suppress_alerts

        @builtins.property
        def name(self) -> builtins.str:
            '''The name you've given to the behavior.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html#cfn-iot-securityprofile-behavior-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def criteria(
            self,
        ) -> typing.Optional[typing.Union["CfnSecurityProfile.BehaviorCriteriaProperty", _IResolvable_da3f097b]]:
            '''The criteria that determine if a device is behaving normally in regard to the ``metric`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html#cfn-iot-securityprofile-behavior-criteria
            '''
            result = self._values.get("criteria")
            return typing.cast(typing.Optional[typing.Union["CfnSecurityProfile.BehaviorCriteriaProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def metric(self) -> typing.Optional[builtins.str]:
            '''What is measured by the behavior.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html#cfn-iot-securityprofile-behavior-metric
            '''
            result = self._values.get("metric")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metric_dimension(
            self,
        ) -> typing.Optional[typing.Union["CfnSecurityProfile.MetricDimensionProperty", _IResolvable_da3f097b]]:
            '''The dimension of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html#cfn-iot-securityprofile-behavior-metricdimension
            '''
            result = self._values.get("metric_dimension")
            return typing.cast(typing.Optional[typing.Union["CfnSecurityProfile.MetricDimensionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def suppress_alerts(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The alert status.

            If you set the value to ``true`` , alerts will be suppressed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html#cfn-iot-securityprofile-behavior-suppressalerts
            '''
            result = self._values.get("suppress_alerts")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BehaviorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnSecurityProfile.MachineLearningDetectionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"confidence_level": "confidenceLevel"},
    )
    class MachineLearningDetectionConfigProperty:
        def __init__(
            self,
            *,
            confidence_level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``MachineLearningDetectionConfig`` property type controls confidence of the machine learning model.

            :param confidence_level: The model confidence level. There are three levels of confidence, ``"high"`` , ``"medium"`` , and ``"low"`` . The higher the confidence level, the lower the sensitivity, and the lower the alarm frequency will be.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-machinelearningdetectionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                machine_learning_detection_config_property = iot.CfnSecurityProfile.MachineLearningDetectionConfigProperty(
                    confidence_level="confidenceLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSecurityProfile.MachineLearningDetectionConfigProperty.__init__)
                check_type(argname="argument confidence_level", value=confidence_level, expected_type=type_hints["confidence_level"])
            self._values: typing.Dict[str, typing.Any] = {}
            if confidence_level is not None:
                self._values["confidence_level"] = confidence_level

        @builtins.property
        def confidence_level(self) -> typing.Optional[builtins.str]:
            '''The model confidence level.

            There are three levels of confidence, ``"high"`` , ``"medium"`` , and ``"low"`` .

            The higher the confidence level, the lower the sensitivity, and the lower the alarm frequency will be.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-machinelearningdetectionconfig.html#cfn-iot-securityprofile-machinelearningdetectionconfig-confidencelevel
            '''
            result = self._values.get("confidence_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MachineLearningDetectionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnSecurityProfile.MetricDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_name": "dimensionName", "operator": "operator"},
    )
    class MetricDimensionProperty:
        def __init__(
            self,
            *,
            dimension_name: builtins.str,
            operator: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The dimension of the metric.

            :param dimension_name: The name of the dimension.
            :param operator: Operators are constructs that perform logical operations. Valid values are ``IN`` and ``NOT_IN`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricdimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                metric_dimension_property = iot.CfnSecurityProfile.MetricDimensionProperty(
                    dimension_name="dimensionName",
                
                    # the properties below are optional
                    operator="operator"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSecurityProfile.MetricDimensionProperty.__init__)
                check_type(argname="argument dimension_name", value=dimension_name, expected_type=type_hints["dimension_name"])
                check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            self._values: typing.Dict[str, typing.Any] = {
                "dimension_name": dimension_name,
            }
            if operator is not None:
                self._values["operator"] = operator

        @builtins.property
        def dimension_name(self) -> builtins.str:
            '''The name of the dimension.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricdimension.html#cfn-iot-securityprofile-metricdimension-dimensionname
            '''
            result = self._values.get("dimension_name")
            assert result is not None, "Required property 'dimension_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def operator(self) -> typing.Optional[builtins.str]:
            '''Operators are constructs that perform logical operations.

            Valid values are ``IN`` and ``NOT_IN`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricdimension.html#cfn-iot-securityprofile-metricdimension-operator
            '''
            result = self._values.get("operator")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnSecurityProfile.MetricToRetainProperty",
        jsii_struct_bases=[],
        name_mapping={"metric": "metric", "metric_dimension": "metricDimension"},
    )
    class MetricToRetainProperty:
        def __init__(
            self,
            *,
            metric: builtins.str,
            metric_dimension: typing.Optional[typing.Union[typing.Union["CfnSecurityProfile.MetricDimensionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The metric you want to retain.

            Dimensions are optional.

            :param metric: A standard of measurement.
            :param metric_dimension: The dimension of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metrictoretain.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                metric_to_retain_property = iot.CfnSecurityProfile.MetricToRetainProperty(
                    metric="metric",
                
                    # the properties below are optional
                    metric_dimension=iot.CfnSecurityProfile.MetricDimensionProperty(
                        dimension_name="dimensionName",
                
                        # the properties below are optional
                        operator="operator"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSecurityProfile.MetricToRetainProperty.__init__)
                check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
                check_type(argname="argument metric_dimension", value=metric_dimension, expected_type=type_hints["metric_dimension"])
            self._values: typing.Dict[str, typing.Any] = {
                "metric": metric,
            }
            if metric_dimension is not None:
                self._values["metric_dimension"] = metric_dimension

        @builtins.property
        def metric(self) -> builtins.str:
            '''A standard of measurement.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metrictoretain.html#cfn-iot-securityprofile-metrictoretain-metric
            '''
            result = self._values.get("metric")
            assert result is not None, "Required property 'metric' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_dimension(
            self,
        ) -> typing.Optional[typing.Union["CfnSecurityProfile.MetricDimensionProperty", _IResolvable_da3f097b]]:
            '''The dimension of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metrictoretain.html#cfn-iot-securityprofile-metrictoretain-metricdimension
            '''
            result = self._values.get("metric_dimension")
            return typing.cast(typing.Optional[typing.Union["CfnSecurityProfile.MetricDimensionProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricToRetainProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnSecurityProfile.MetricValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cidrs": "cidrs",
            "count": "count",
            "number": "number",
            "numbers": "numbers",
            "ports": "ports",
            "strings": "strings",
        },
    )
    class MetricValueProperty:
        def __init__(
            self,
            *,
            cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
            count: typing.Optional[builtins.str] = None,
            number: typing.Optional[jsii.Number] = None,
            numbers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
            ports: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
            strings: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The value to be compared with the ``metric`` .

            :param cidrs: If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .
            :param count: If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .
            :param number: The numeric values of a metric.
            :param numbers: The numeric value of a metric.
            :param ports: If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .
            :param strings: The string values of a metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                metric_value_property = iot.CfnSecurityProfile.MetricValueProperty(
                    cidrs=["cidrs"],
                    count="count",
                    number=123,
                    numbers=[123],
                    ports=[123],
                    strings=["strings"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSecurityProfile.MetricValueProperty.__init__)
                check_type(argname="argument cidrs", value=cidrs, expected_type=type_hints["cidrs"])
                check_type(argname="argument count", value=count, expected_type=type_hints["count"])
                check_type(argname="argument number", value=number, expected_type=type_hints["number"])
                check_type(argname="argument numbers", value=numbers, expected_type=type_hints["numbers"])
                check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
                check_type(argname="argument strings", value=strings, expected_type=type_hints["strings"])
            self._values: typing.Dict[str, typing.Any] = {}
            if cidrs is not None:
                self._values["cidrs"] = cidrs
            if count is not None:
                self._values["count"] = count
            if number is not None:
                self._values["number"] = number
            if numbers is not None:
                self._values["numbers"] = numbers
            if ports is not None:
                self._values["ports"] = ports
            if strings is not None:
                self._values["strings"] = strings

        @builtins.property
        def cidrs(self) -> typing.Optional[typing.List[builtins.str]]:
            '''If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-cidrs
            '''
            result = self._values.get("cidrs")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def count(self) -> typing.Optional[builtins.str]:
            '''If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def number(self) -> typing.Optional[jsii.Number]:
            '''The numeric values of a metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-number
            '''
            result = self._values.get("number")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def numbers(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]]:
            '''The numeric value of a metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-numbers
            '''
            result = self._values.get("numbers")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]], result)

        @builtins.property
        def ports(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]]:
            '''If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-ports
            '''
            result = self._values.get("ports")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]], result)

        @builtins.property
        def strings(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The string values of a metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-strings
            '''
            result = self._values.get("strings")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnSecurityProfile.StatisticalThresholdProperty",
        jsii_struct_bases=[],
        name_mapping={"statistic": "statistic"},
    )
    class StatisticalThresholdProperty:
        def __init__(self, *, statistic: typing.Optional[builtins.str] = None) -> None:
            '''A statistical ranking (percentile) that indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.

            :param statistic: The percentile that resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period ( ``durationSeconds`` ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below ( ``comparisonOperator`` ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-statisticalthreshold.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                statistical_threshold_property = iot.CfnSecurityProfile.StatisticalThresholdProperty(
                    statistic="statistic"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnSecurityProfile.StatisticalThresholdProperty.__init__)
                check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            self._values: typing.Dict[str, typing.Any] = {}
            if statistic is not None:
                self._values["statistic"] = statistic

        @builtins.property
        def statistic(self) -> typing.Optional[builtins.str]:
            '''The percentile that resolves to a threshold value by which compliance with a behavior is determined.

            Metrics are collected over the specified period ( ``durationSeconds`` ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below ( ``comparisonOperator`` ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-statisticalthreshold.html#cfn-iot-securityprofile-statisticalthreshold-statistic
            '''
            result = self._values.get("statistic")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatisticalThresholdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnSecurityProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "additional_metrics_to_retain_v2": "additionalMetricsToRetainV2",
        "alert_targets": "alertTargets",
        "behaviors": "behaviors",
        "security_profile_description": "securityProfileDescription",
        "security_profile_name": "securityProfileName",
        "tags": "tags",
        "target_arns": "targetArns",
    },
)
class CfnSecurityProfileProps:
    def __init__(
        self,
        *,
        additional_metrics_to_retain_v2: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnSecurityProfile.MetricToRetainProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        alert_targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnSecurityProfile.AlertTargetProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        behaviors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnSecurityProfile.BehaviorProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        security_profile_description: typing.Optional[builtins.str] = None,
        security_profile_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        target_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSecurityProfile``.

        :param additional_metrics_to_retain_v2: A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's ``behaviors`` , but it's also retained for any metric specified here. Can be used with custom metrics; can't be used with dimensions.
        :param alert_targets: Specifies the destinations to which alerts are sent. (Alerts are always sent to the console.) Alerts are generated when a device (thing) violates a behavior.
        :param behaviors: Specifies the behaviors that, when violated by a device (thing), cause an alert.
        :param security_profile_description: A description of the security profile.
        :param security_profile_name: The name you gave to the security profile.
        :param tags: Metadata that can be used to manage the security profile.
        :param target_arns: The ARN of the target (thing group) to which the security profile is attached.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_security_profile_props = iot.CfnSecurityProfileProps(
                additional_metrics_to_retain_v2=[iot.CfnSecurityProfile.MetricToRetainProperty(
                    metric="metric",
            
                    # the properties below are optional
                    metric_dimension=iot.CfnSecurityProfile.MetricDimensionProperty(
                        dimension_name="dimensionName",
            
                        # the properties below are optional
                        operator="operator"
                    )
                )],
                alert_targets={
                    "alert_targets_key": iot.CfnSecurityProfile.AlertTargetProperty(
                        alert_target_arn="alertTargetArn",
                        role_arn="roleArn"
                    )
                },
                behaviors=[iot.CfnSecurityProfile.BehaviorProperty(
                    name="name",
            
                    # the properties below are optional
                    criteria=iot.CfnSecurityProfile.BehaviorCriteriaProperty(
                        comparison_operator="comparisonOperator",
                        consecutive_datapoints_to_alarm=123,
                        consecutive_datapoints_to_clear=123,
                        duration_seconds=123,
                        ml_detection_config=iot.CfnSecurityProfile.MachineLearningDetectionConfigProperty(
                            confidence_level="confidenceLevel"
                        ),
                        statistical_threshold=iot.CfnSecurityProfile.StatisticalThresholdProperty(
                            statistic="statistic"
                        ),
                        value=iot.CfnSecurityProfile.MetricValueProperty(
                            cidrs=["cidrs"],
                            count="count",
                            number=123,
                            numbers=[123],
                            ports=[123],
                            strings=["strings"]
                        )
                    ),
                    metric="metric",
                    metric_dimension=iot.CfnSecurityProfile.MetricDimensionProperty(
                        dimension_name="dimensionName",
            
                        # the properties below are optional
                        operator="operator"
                    ),
                    suppress_alerts=False
                )],
                security_profile_description="securityProfileDescription",
                security_profile_name="securityProfileName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                target_arns=["targetArns"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnSecurityProfileProps.__init__)
            check_type(argname="argument additional_metrics_to_retain_v2", value=additional_metrics_to_retain_v2, expected_type=type_hints["additional_metrics_to_retain_v2"])
            check_type(argname="argument alert_targets", value=alert_targets, expected_type=type_hints["alert_targets"])
            check_type(argname="argument behaviors", value=behaviors, expected_type=type_hints["behaviors"])
            check_type(argname="argument security_profile_description", value=security_profile_description, expected_type=type_hints["security_profile_description"])
            check_type(argname="argument security_profile_name", value=security_profile_name, expected_type=type_hints["security_profile_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_arns", value=target_arns, expected_type=type_hints["target_arns"])
        self._values: typing.Dict[str, typing.Any] = {}
        if additional_metrics_to_retain_v2 is not None:
            self._values["additional_metrics_to_retain_v2"] = additional_metrics_to_retain_v2
        if alert_targets is not None:
            self._values["alert_targets"] = alert_targets
        if behaviors is not None:
            self._values["behaviors"] = behaviors
        if security_profile_description is not None:
            self._values["security_profile_description"] = security_profile_description
        if security_profile_name is not None:
            self._values["security_profile_name"] = security_profile_name
        if tags is not None:
            self._values["tags"] = tags
        if target_arns is not None:
            self._values["target_arns"] = target_arns

    @builtins.property
    def additional_metrics_to_retain_v2(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnSecurityProfile.MetricToRetainProperty, _IResolvable_da3f097b]]]]:
        '''A list of metrics whose data is retained (stored).

        By default, data is retained for any metric used in the profile's ``behaviors`` , but it's also retained for any metric specified here. Can be used with custom metrics; can't be used with dimensions.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-additionalmetricstoretainv2
        '''
        result = self._values.get("additional_metrics_to_retain_v2")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnSecurityProfile.MetricToRetainProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def alert_targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnSecurityProfile.AlertTargetProperty, _IResolvable_da3f097b]]]]:
        '''Specifies the destinations to which alerts are sent.

        (Alerts are always sent to the console.) Alerts are generated when a device (thing) violates a behavior.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-alerttargets
        '''
        result = self._values.get("alert_targets")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[CfnSecurityProfile.AlertTargetProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def behaviors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnSecurityProfile.BehaviorProperty, _IResolvable_da3f097b]]]]:
        '''Specifies the behaviors that, when violated by a device (thing), cause an alert.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-behaviors
        '''
        result = self._values.get("behaviors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnSecurityProfile.BehaviorProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def security_profile_description(self) -> typing.Optional[builtins.str]:
        '''A description of the security profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-securityprofiledescription
        '''
        result = self._values.get("security_profile_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_profile_name(self) -> typing.Optional[builtins.str]:
        '''The name you gave to the security profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-securityprofilename
        '''
        result = self._values.get("security_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata that can be used to manage the security profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def target_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARN of the target (thing group) to which the security profile is attached.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-targetarns
        '''
        result = self._values.get("target_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnThing(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnThing",
):
    '''A CloudFormation ``AWS::IoT::Thing``.

    Use the ``AWS::IoT::Thing`` resource to declare an AWS IoT thing.

    For information about working with things, see `How AWS IoT Works <https://docs.aws.amazon.com/iot/latest/developerguide/aws-iot-how-it-works.html>`_ and `Device Registry for AWS IoT <https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html>`_ in the *AWS IoT Developer Guide* .

    :cloudformationResource: AWS::IoT::Thing
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_thing = iot.CfnThing(self, "MyCfnThing",
            attribute_payload=iot.CfnThing.AttributePayloadProperty(
                attributes={
                    "attributes_key": "attributes"
                }
            ),
            thing_name="thingName"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        attribute_payload: typing.Optional[typing.Union[typing.Union["CfnThing.AttributePayloadProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        thing_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::Thing``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param attribute_payload: A string that contains up to three key value pairs. Maximum length of 800. Duplicates not allowed.
        :param thing_name: The name of the thing to update. You can't change a thing's name. To change a thing's name, you must create a new thing, give it the new name, and then delete the old thing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnThing.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnThingProps(
            attribute_payload=attribute_payload, thing_name=thing_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnThing.inspect)
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
            type_hints = typing.get_type_hints(CfnThing._render_properties)
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
    @jsii.member(jsii_name="attributePayload")
    def attribute_payload(
        self,
    ) -> typing.Optional[typing.Union["CfnThing.AttributePayloadProperty", _IResolvable_da3f097b]]:
        '''A string that contains up to three key value pairs.

        Maximum length of 800. Duplicates not allowed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html#cfn-iot-thing-attributepayload
        '''
        return typing.cast(typing.Optional[typing.Union["CfnThing.AttributePayloadProperty", _IResolvable_da3f097b]], jsii.get(self, "attributePayload"))

    @attribute_payload.setter
    def attribute_payload(
        self,
        value: typing.Optional[typing.Union["CfnThing.AttributePayloadProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnThing, "attribute_payload").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributePayload", value)

    @builtins.property
    @jsii.member(jsii_name="thingName")
    def thing_name(self) -> typing.Optional[builtins.str]:
        '''The name of the thing to update.

        You can't change a thing's name. To change a thing's name, you must create a new thing, give it the new name, and then delete the old thing.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html#cfn-iot-thing-thingname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingName"))

    @thing_name.setter
    def thing_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnThing, "thing_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnThing.AttributePayloadProperty",
        jsii_struct_bases=[],
        name_mapping={"attributes": "attributes"},
    )
    class AttributePayloadProperty:
        def __init__(
            self,
            *,
            attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''The AttributePayload property specifies up to three attributes for an AWS IoT as key-value pairs.

            AttributePayload is a property of the `AWS::IoT::Thing <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html>`_ resource.

            :param attributes: A JSON string containing up to three key-value pair in JSON format. For example:. ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-thing-attributepayload.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                attribute_payload_property = iot.CfnThing.AttributePayloadProperty(
                    attributes={
                        "attributes_key": "attributes"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnThing.AttributePayloadProperty.__init__)
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            self._values: typing.Dict[str, typing.Any] = {}
            if attributes is not None:
                self._values["attributes"] = attributes

        @builtins.property
        def attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''A JSON string containing up to three key-value pair in JSON format. For example:.

            ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-thing-attributepayload.html#cfn-iot-thing-attributepayload-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributePayloadProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnThingPrincipalAttachment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnThingPrincipalAttachment",
):
    '''A CloudFormation ``AWS::IoT::ThingPrincipalAttachment``.

    Use the ``AWS::IoT::ThingPrincipalAttachment`` resource to attach a principal (an X.509 certificate or another credential) to a thing.

    For more information about working with AWS IoT things and principals, see `Authorization <https://docs.aws.amazon.com/iot/latest/developerguide/authorization.html>`_ in the *AWS IoT Developer Guide* .

    :cloudformationResource: AWS::IoT::ThingPrincipalAttachment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_thing_principal_attachment = iot.CfnThingPrincipalAttachment(self, "MyCfnThingPrincipalAttachment",
            principal="principal",
            thing_name="thingName"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        principal: builtins.str,
        thing_name: builtins.str,
    ) -> None:
        '''Create a new ``AWS::IoT::ThingPrincipalAttachment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param principal: The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.
        :param thing_name: The name of the AWS IoT thing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnThingPrincipalAttachment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnThingPrincipalAttachmentProps(
            principal=principal, thing_name=thing_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnThingPrincipalAttachment.inspect)
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
            type_hints = typing.get_type_hints(CfnThingPrincipalAttachment._render_properties)
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
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        '''The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html#cfn-iot-thingprincipalattachment-principal
        '''
        return typing.cast(builtins.str, jsii.get(self, "principal"))

    @principal.setter
    def principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnThingPrincipalAttachment, "principal").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)

    @builtins.property
    @jsii.member(jsii_name="thingName")
    def thing_name(self) -> builtins.str:
        '''The name of the AWS IoT thing.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html#cfn-iot-thingprincipalattachment-thingname
        '''
        return typing.cast(builtins.str, jsii.get(self, "thingName"))

    @thing_name.setter
    def thing_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnThingPrincipalAttachment, "thing_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnThingPrincipalAttachmentProps",
    jsii_struct_bases=[],
    name_mapping={"principal": "principal", "thing_name": "thingName"},
)
class CfnThingPrincipalAttachmentProps:
    def __init__(self, *, principal: builtins.str, thing_name: builtins.str) -> None:
        '''Properties for defining a ``CfnThingPrincipalAttachment``.

        :param principal: The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.
        :param thing_name: The name of the AWS IoT thing.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_thing_principal_attachment_props = iot.CfnThingPrincipalAttachmentProps(
                principal="principal",
                thing_name="thingName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnThingPrincipalAttachmentProps.__init__)
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument thing_name", value=thing_name, expected_type=type_hints["thing_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "principal": principal,
            "thing_name": thing_name,
        }

    @builtins.property
    def principal(self) -> builtins.str:
        '''The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html#cfn-iot-thingprincipalattachment-principal
        '''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def thing_name(self) -> builtins.str:
        '''The name of the AWS IoT thing.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html#cfn-iot-thingprincipalattachment-thingname
        '''
        result = self._values.get("thing_name")
        assert result is not None, "Required property 'thing_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnThingPrincipalAttachmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnThingProps",
    jsii_struct_bases=[],
    name_mapping={"attribute_payload": "attributePayload", "thing_name": "thingName"},
)
class CfnThingProps:
    def __init__(
        self,
        *,
        attribute_payload: typing.Optional[typing.Union[typing.Union[CfnThing.AttributePayloadProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        thing_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnThing``.

        :param attribute_payload: A string that contains up to three key value pairs. Maximum length of 800. Duplicates not allowed.
        :param thing_name: The name of the thing to update. You can't change a thing's name. To change a thing's name, you must create a new thing, give it the new name, and then delete the old thing.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_thing_props = iot.CfnThingProps(
                attribute_payload=iot.CfnThing.AttributePayloadProperty(
                    attributes={
                        "attributes_key": "attributes"
                    }
                ),
                thing_name="thingName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnThingProps.__init__)
            check_type(argname="argument attribute_payload", value=attribute_payload, expected_type=type_hints["attribute_payload"])
            check_type(argname="argument thing_name", value=thing_name, expected_type=type_hints["thing_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if attribute_payload is not None:
            self._values["attribute_payload"] = attribute_payload
        if thing_name is not None:
            self._values["thing_name"] = thing_name

    @builtins.property
    def attribute_payload(
        self,
    ) -> typing.Optional[typing.Union[CfnThing.AttributePayloadProperty, _IResolvable_da3f097b]]:
        '''A string that contains up to three key value pairs.

        Maximum length of 800. Duplicates not allowed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html#cfn-iot-thing-attributepayload
        '''
        result = self._values.get("attribute_payload")
        return typing.cast(typing.Optional[typing.Union[CfnThing.AttributePayloadProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def thing_name(self) -> typing.Optional[builtins.str]:
        '''The name of the thing to update.

        You can't change a thing's name. To change a thing's name, you must create a new thing, give it the new name, and then delete the old thing.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html#cfn-iot-thing-thingname
        '''
        result = self._values.get("thing_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnThingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTopicRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule",
):
    '''A CloudFormation ``AWS::IoT::TopicRule``.

    Use the ``AWS::IoT::TopicRule`` resource to declare an AWS IoT rule. For information about working with AWS IoT rules, see `Rules for AWS IoT <https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html>`_ in the *AWS IoT Developer Guide* .

    :cloudformationResource: AWS::IoT::TopicRule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_topic_rule = iot.CfnTopicRule(self, "MyCfnTopicRule",
            topic_rule_payload=iot.CfnTopicRule.TopicRulePayloadProperty(
                actions=[iot.CfnTopicRule.ActionProperty(
                    cloudwatch_alarm=iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                        alarm_name="alarmName",
                        role_arn="roleArn",
                        state_reason="stateReason",
                        state_value="stateValue"
                    ),
                    cloudwatch_logs=iot.CfnTopicRule.CloudwatchLogsActionProperty(
                        log_group_name="logGroupName",
                        role_arn="roleArn"
                    ),
                    cloudwatch_metric=iot.CfnTopicRule.CloudwatchMetricActionProperty(
                        metric_name="metricName",
                        metric_namespace="metricNamespace",
                        metric_unit="metricUnit",
                        metric_value="metricValue",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        metric_timestamp="metricTimestamp"
                    ),
                    dynamo_db=iot.CfnTopicRule.DynamoDBActionProperty(
                        hash_key_field="hashKeyField",
                        hash_key_value="hashKeyValue",
                        role_arn="roleArn",
                        table_name="tableName",
        
                        # the properties below are optional
                        hash_key_type="hashKeyType",
                        payload_field="payloadField",
                        range_key_field="rangeKeyField",
                        range_key_type="rangeKeyType",
                        range_key_value="rangeKeyValue"
                    ),
                    dynamo_dBv2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                        put_item=iot.CfnTopicRule.PutItemInputProperty(
                            table_name="tableName"
                        ),
                        role_arn="roleArn"
                    ),
                    elasticsearch=iot.CfnTopicRule.ElasticsearchActionProperty(
                        endpoint="endpoint",
                        id="id",
                        index="index",
                        role_arn="roleArn",
                        type="type"
                    ),
                    firehose=iot.CfnTopicRule.FirehoseActionProperty(
                        delivery_stream_name="deliveryStreamName",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        batch_mode=False,
                        separator="separator"
                    ),
                    http=iot.CfnTopicRule.HttpActionProperty(
                        url="url",
        
                        # the properties below are optional
                        auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                            sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                                role_arn="roleArn",
                                service_name="serviceName",
                                signing_region="signingRegion"
                            )
                        ),
                        confirmation_url="confirmationUrl",
                        headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                            key="key",
                            value="value"
                        )]
                    ),
                    iot_analytics=iot.CfnTopicRule.IotAnalyticsActionProperty(
                        channel_name="channelName",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        batch_mode=False
                    ),
                    iot_events=iot.CfnTopicRule.IotEventsActionProperty(
                        input_name="inputName",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        batch_mode=False,
                        message_id="messageId"
                    ),
                    iot_site_wise=iot.CfnTopicRule.IotSiteWiseActionProperty(
                        put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                            property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                                timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                    time_in_seconds="timeInSeconds",
        
                                    # the properties below are optional
                                    offset_in_nanos="offsetInNanos"
                                ),
                                value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                    boolean_value="booleanValue",
                                    double_value="doubleValue",
                                    integer_value="integerValue",
                                    string_value="stringValue"
                                ),
        
                                # the properties below are optional
                                quality="quality"
                            )],
        
                            # the properties below are optional
                            asset_id="assetId",
                            entry_id="entryId",
                            property_alias="propertyAlias",
                            property_id="propertyId"
                        )],
                        role_arn="roleArn"
                    ),
                    kafka=iot.CfnTopicRule.KafkaActionProperty(
                        client_properties={
                            "client_properties_key": "clientProperties"
                        },
                        destination_arn="destinationArn",
                        topic="topic",
        
                        # the properties below are optional
                        key="key",
                        partition="partition"
                    ),
                    kinesis=iot.CfnTopicRule.KinesisActionProperty(
                        role_arn="roleArn",
                        stream_name="streamName",
        
                        # the properties below are optional
                        partition_key="partitionKey"
                    ),
                    lambda_=iot.CfnTopicRule.LambdaActionProperty(
                        function_arn="functionArn"
                    ),
                    open_search=iot.CfnTopicRule.OpenSearchActionProperty(
                        endpoint="endpoint",
                        id="id",
                        index="index",
                        role_arn="roleArn",
                        type="type"
                    ),
                    republish=iot.CfnTopicRule.RepublishActionProperty(
                        role_arn="roleArn",
                        topic="topic",
        
                        # the properties below are optional
                        qos=123
                    ),
                    s3=iot.CfnTopicRule.S3ActionProperty(
                        bucket_name="bucketName",
                        key="key",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        canned_acl="cannedAcl"
                    ),
                    sns=iot.CfnTopicRule.SnsActionProperty(
                        role_arn="roleArn",
                        target_arn="targetArn",
        
                        # the properties below are optional
                        message_format="messageFormat"
                    ),
                    sqs=iot.CfnTopicRule.SqsActionProperty(
                        queue_url="queueUrl",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        use_base64=False
                    ),
                    step_functions=iot.CfnTopicRule.StepFunctionsActionProperty(
                        role_arn="roleArn",
                        state_machine_name="stateMachineName",
        
                        # the properties below are optional
                        execution_name_prefix="executionNamePrefix"
                    ),
                    timestream=iot.CfnTopicRule.TimestreamActionProperty(
                        database_name="databaseName",
                        dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        role_arn="roleArn",
                        table_name="tableName",
        
                        # the properties below are optional
                        batch_mode=False,
                        timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                            unit="unit",
                            value="value"
                        )
                    )
                )],
                sql="sql",
        
                # the properties below are optional
                aws_iot_sql_version="awsIotSqlVersion",
                description="description",
                error_action=iot.CfnTopicRule.ActionProperty(
                    cloudwatch_alarm=iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                        alarm_name="alarmName",
                        role_arn="roleArn",
                        state_reason="stateReason",
                        state_value="stateValue"
                    ),
                    cloudwatch_logs=iot.CfnTopicRule.CloudwatchLogsActionProperty(
                        log_group_name="logGroupName",
                        role_arn="roleArn"
                    ),
                    cloudwatch_metric=iot.CfnTopicRule.CloudwatchMetricActionProperty(
                        metric_name="metricName",
                        metric_namespace="metricNamespace",
                        metric_unit="metricUnit",
                        metric_value="metricValue",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        metric_timestamp="metricTimestamp"
                    ),
                    dynamo_db=iot.CfnTopicRule.DynamoDBActionProperty(
                        hash_key_field="hashKeyField",
                        hash_key_value="hashKeyValue",
                        role_arn="roleArn",
                        table_name="tableName",
        
                        # the properties below are optional
                        hash_key_type="hashKeyType",
                        payload_field="payloadField",
                        range_key_field="rangeKeyField",
                        range_key_type="rangeKeyType",
                        range_key_value="rangeKeyValue"
                    ),
                    dynamo_dBv2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                        put_item=iot.CfnTopicRule.PutItemInputProperty(
                            table_name="tableName"
                        ),
                        role_arn="roleArn"
                    ),
                    elasticsearch=iot.CfnTopicRule.ElasticsearchActionProperty(
                        endpoint="endpoint",
                        id="id",
                        index="index",
                        role_arn="roleArn",
                        type="type"
                    ),
                    firehose=iot.CfnTopicRule.FirehoseActionProperty(
                        delivery_stream_name="deliveryStreamName",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        batch_mode=False,
                        separator="separator"
                    ),
                    http=iot.CfnTopicRule.HttpActionProperty(
                        url="url",
        
                        # the properties below are optional
                        auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                            sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                                role_arn="roleArn",
                                service_name="serviceName",
                                signing_region="signingRegion"
                            )
                        ),
                        confirmation_url="confirmationUrl",
                        headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                            key="key",
                            value="value"
                        )]
                    ),
                    iot_analytics=iot.CfnTopicRule.IotAnalyticsActionProperty(
                        channel_name="channelName",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        batch_mode=False
                    ),
                    iot_events=iot.CfnTopicRule.IotEventsActionProperty(
                        input_name="inputName",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        batch_mode=False,
                        message_id="messageId"
                    ),
                    iot_site_wise=iot.CfnTopicRule.IotSiteWiseActionProperty(
                        put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                            property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                                timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                    time_in_seconds="timeInSeconds",
        
                                    # the properties below are optional
                                    offset_in_nanos="offsetInNanos"
                                ),
                                value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                    boolean_value="booleanValue",
                                    double_value="doubleValue",
                                    integer_value="integerValue",
                                    string_value="stringValue"
                                ),
        
                                # the properties below are optional
                                quality="quality"
                            )],
        
                            # the properties below are optional
                            asset_id="assetId",
                            entry_id="entryId",
                            property_alias="propertyAlias",
                            property_id="propertyId"
                        )],
                        role_arn="roleArn"
                    ),
                    kafka=iot.CfnTopicRule.KafkaActionProperty(
                        client_properties={
                            "client_properties_key": "clientProperties"
                        },
                        destination_arn="destinationArn",
                        topic="topic",
        
                        # the properties below are optional
                        key="key",
                        partition="partition"
                    ),
                    kinesis=iot.CfnTopicRule.KinesisActionProperty(
                        role_arn="roleArn",
                        stream_name="streamName",
        
                        # the properties below are optional
                        partition_key="partitionKey"
                    ),
                    lambda_=iot.CfnTopicRule.LambdaActionProperty(
                        function_arn="functionArn"
                    ),
                    open_search=iot.CfnTopicRule.OpenSearchActionProperty(
                        endpoint="endpoint",
                        id="id",
                        index="index",
                        role_arn="roleArn",
                        type="type"
                    ),
                    republish=iot.CfnTopicRule.RepublishActionProperty(
                        role_arn="roleArn",
                        topic="topic",
        
                        # the properties below are optional
                        qos=123
                    ),
                    s3=iot.CfnTopicRule.S3ActionProperty(
                        bucket_name="bucketName",
                        key="key",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        canned_acl="cannedAcl"
                    ),
                    sns=iot.CfnTopicRule.SnsActionProperty(
                        role_arn="roleArn",
                        target_arn="targetArn",
        
                        # the properties below are optional
                        message_format="messageFormat"
                    ),
                    sqs=iot.CfnTopicRule.SqsActionProperty(
                        queue_url="queueUrl",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        use_base64=False
                    ),
                    step_functions=iot.CfnTopicRule.StepFunctionsActionProperty(
                        role_arn="roleArn",
                        state_machine_name="stateMachineName",
        
                        # the properties below are optional
                        execution_name_prefix="executionNamePrefix"
                    ),
                    timestream=iot.CfnTopicRule.TimestreamActionProperty(
                        database_name="databaseName",
                        dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        role_arn="roleArn",
                        table_name="tableName",
        
                        # the properties below are optional
                        batch_mode=False,
                        timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                            unit="unit",
                            value="value"
                        )
                    )
                ),
                rule_disabled=False
            ),
        
            # the properties below are optional
            rule_name="ruleName",
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
        topic_rule_payload: typing.Union[typing.Union["CfnTopicRule.TopicRulePayloadProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        rule_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::TopicRule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param topic_rule_payload: The rule payload.
        :param rule_name: The name of the rule.
        :param tags: Metadata which can be used to manage the topic rule. .. epigraph:: For URI Request parameters use format: ...key1=value1&key2=value2... For the CLI command-line parameter use format: --tags "key1=value1&key2=value2..." For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTopicRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTopicRuleProps(
            topic_rule_payload=topic_rule_payload, rule_name=rule_name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTopicRule.inspect)
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
            type_hints = typing.get_type_hints(CfnTopicRule._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AWS IoT rule, such as ``arn:aws:iot:us-east-2:123456789012:rule/MyIoTRule`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata which can be used to manage the topic rule.

        .. epigraph::

           For URI Request parameters use format: ...key1=value1&key2=value2...

           For the CLI command-line parameter use format: --tags "key1=value1&key2=value2..."

           For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html#cfn-iot-topicrule-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="topicRulePayload")
    def topic_rule_payload(
        self,
    ) -> typing.Union["CfnTopicRule.TopicRulePayloadProperty", _IResolvable_da3f097b]:
        '''The rule payload.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html#cfn-iot-topicrule-topicrulepayload
        '''
        return typing.cast(typing.Union["CfnTopicRule.TopicRulePayloadProperty", _IResolvable_da3f097b], jsii.get(self, "topicRulePayload"))

    @topic_rule_payload.setter
    def topic_rule_payload(
        self,
        value: typing.Union["CfnTopicRule.TopicRulePayloadProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTopicRule, "topic_rule_payload").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topicRulePayload", value)

    @builtins.property
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''The name of the rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html#cfn-iot-topicrule-rulename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTopicRule, "rule_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloudwatch_alarm": "cloudwatchAlarm",
            "cloudwatch_logs": "cloudwatchLogs",
            "cloudwatch_metric": "cloudwatchMetric",
            "dynamo_db": "dynamoDb",
            "dynamo_d_bv2": "dynamoDBv2",
            "elasticsearch": "elasticsearch",
            "firehose": "firehose",
            "http": "http",
            "iot_analytics": "iotAnalytics",
            "iot_events": "iotEvents",
            "iot_site_wise": "iotSiteWise",
            "kafka": "kafka",
            "kinesis": "kinesis",
            "lambda_": "lambda",
            "open_search": "openSearch",
            "republish": "republish",
            "s3": "s3",
            "sns": "sns",
            "sqs": "sqs",
            "step_functions": "stepFunctions",
            "timestream": "timestream",
        },
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            cloudwatch_alarm: typing.Optional[typing.Union[typing.Union["CfnTopicRule.CloudwatchAlarmActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            cloudwatch_logs: typing.Optional[typing.Union[typing.Union["CfnTopicRule.CloudwatchLogsActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            cloudwatch_metric: typing.Optional[typing.Union[typing.Union["CfnTopicRule.CloudwatchMetricActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            dynamo_db: typing.Optional[typing.Union[typing.Union["CfnTopicRule.DynamoDBActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            dynamo_d_bv2: typing.Optional[typing.Union[typing.Union["CfnTopicRule.DynamoDBv2ActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            elasticsearch: typing.Optional[typing.Union[typing.Union["CfnTopicRule.ElasticsearchActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            firehose: typing.Optional[typing.Union[typing.Union["CfnTopicRule.FirehoseActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            http: typing.Optional[typing.Union[typing.Union["CfnTopicRule.HttpActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            iot_analytics: typing.Optional[typing.Union[typing.Union["CfnTopicRule.IotAnalyticsActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            iot_events: typing.Optional[typing.Union[typing.Union["CfnTopicRule.IotEventsActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            iot_site_wise: typing.Optional[typing.Union[typing.Union["CfnTopicRule.IotSiteWiseActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            kafka: typing.Optional[typing.Union[typing.Union["CfnTopicRule.KafkaActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            kinesis: typing.Optional[typing.Union[typing.Union["CfnTopicRule.KinesisActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            lambda_: typing.Optional[typing.Union[typing.Union["CfnTopicRule.LambdaActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            open_search: typing.Optional[typing.Union[typing.Union["CfnTopicRule.OpenSearchActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            republish: typing.Optional[typing.Union[typing.Union["CfnTopicRule.RepublishActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            s3: typing.Optional[typing.Union[typing.Union["CfnTopicRule.S3ActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            sns: typing.Optional[typing.Union[typing.Union["CfnTopicRule.SnsActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            sqs: typing.Optional[typing.Union[typing.Union["CfnTopicRule.SqsActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            step_functions: typing.Optional[typing.Union[typing.Union["CfnTopicRule.StepFunctionsActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            timestream: typing.Optional[typing.Union[typing.Union["CfnTopicRule.TimestreamActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes the actions associated with a rule.

            :param cloudwatch_alarm: Change the state of a CloudWatch alarm.
            :param cloudwatch_logs: Sends data to CloudWatch.
            :param cloudwatch_metric: Capture a CloudWatch metric.
            :param dynamo_db: Write to a DynamoDB table.
            :param dynamo_d_bv2: Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
            :param elasticsearch: Write data to an Amazon OpenSearch Service domain. .. epigraph:: The ``Elasticsearch`` action can only be used by existing rule actions. To create a new rule action or to update an existing rule action, use the ``OpenSearch`` rule action instead. For more information, see `OpenSearchAction <https://docs.aws.amazon.com//iot/latest/apireference/API_OpenSearchAction.html>`_ .
            :param firehose: Write to an Amazon Kinesis Firehose stream.
            :param http: Send data to an HTTPS endpoint.
            :param iot_analytics: Sends message data to an AWS IoT Analytics channel.
            :param iot_events: Sends an input to an AWS IoT Events detector.
            :param iot_site_wise: Sends data from the MQTT message that triggered the rule to AWS IoT SiteWise asset properties.
            :param kafka: Send messages to an Amazon Managed Streaming for Apache Kafka (Amazon MSK) or self-managed Apache Kafka cluster.
            :param kinesis: Write data to an Amazon Kinesis stream.
            :param lambda_: Invoke a Lambda function.
            :param open_search: Write data to an Amazon OpenSearch Service domain.
            :param republish: Publish to another MQTT topic.
            :param s3: Write to an Amazon S3 bucket.
            :param sns: Publish to an Amazon SNS topic.
            :param sqs: Publish to an Amazon SQS queue.
            :param step_functions: Starts execution of a Step Functions state machine.
            :param timestream: Writes attributes from an MQTT message.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                action_property = iot.CfnTopicRule.ActionProperty(
                    cloudwatch_alarm=iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                        alarm_name="alarmName",
                        role_arn="roleArn",
                        state_reason="stateReason",
                        state_value="stateValue"
                    ),
                    cloudwatch_logs=iot.CfnTopicRule.CloudwatchLogsActionProperty(
                        log_group_name="logGroupName",
                        role_arn="roleArn"
                    ),
                    cloudwatch_metric=iot.CfnTopicRule.CloudwatchMetricActionProperty(
                        metric_name="metricName",
                        metric_namespace="metricNamespace",
                        metric_unit="metricUnit",
                        metric_value="metricValue",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        metric_timestamp="metricTimestamp"
                    ),
                    dynamo_db=iot.CfnTopicRule.DynamoDBActionProperty(
                        hash_key_field="hashKeyField",
                        hash_key_value="hashKeyValue",
                        role_arn="roleArn",
                        table_name="tableName",
                
                        # the properties below are optional
                        hash_key_type="hashKeyType",
                        payload_field="payloadField",
                        range_key_field="rangeKeyField",
                        range_key_type="rangeKeyType",
                        range_key_value="rangeKeyValue"
                    ),
                    dynamo_dBv2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                        put_item=iot.CfnTopicRule.PutItemInputProperty(
                            table_name="tableName"
                        ),
                        role_arn="roleArn"
                    ),
                    elasticsearch=iot.CfnTopicRule.ElasticsearchActionProperty(
                        endpoint="endpoint",
                        id="id",
                        index="index",
                        role_arn="roleArn",
                        type="type"
                    ),
                    firehose=iot.CfnTopicRule.FirehoseActionProperty(
                        delivery_stream_name="deliveryStreamName",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        batch_mode=False,
                        separator="separator"
                    ),
                    http=iot.CfnTopicRule.HttpActionProperty(
                        url="url",
                
                        # the properties below are optional
                        auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                            sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                                role_arn="roleArn",
                                service_name="serviceName",
                                signing_region="signingRegion"
                            )
                        ),
                        confirmation_url="confirmationUrl",
                        headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                            key="key",
                            value="value"
                        )]
                    ),
                    iot_analytics=iot.CfnTopicRule.IotAnalyticsActionProperty(
                        channel_name="channelName",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        batch_mode=False
                    ),
                    iot_events=iot.CfnTopicRule.IotEventsActionProperty(
                        input_name="inputName",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        batch_mode=False,
                        message_id="messageId"
                    ),
                    iot_site_wise=iot.CfnTopicRule.IotSiteWiseActionProperty(
                        put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                            property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                                timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                    time_in_seconds="timeInSeconds",
                
                                    # the properties below are optional
                                    offset_in_nanos="offsetInNanos"
                                ),
                                value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                    boolean_value="booleanValue",
                                    double_value="doubleValue",
                                    integer_value="integerValue",
                                    string_value="stringValue"
                                ),
                
                                # the properties below are optional
                                quality="quality"
                            )],
                
                            # the properties below are optional
                            asset_id="assetId",
                            entry_id="entryId",
                            property_alias="propertyAlias",
                            property_id="propertyId"
                        )],
                        role_arn="roleArn"
                    ),
                    kafka=iot.CfnTopicRule.KafkaActionProperty(
                        client_properties={
                            "client_properties_key": "clientProperties"
                        },
                        destination_arn="destinationArn",
                        topic="topic",
                
                        # the properties below are optional
                        key="key",
                        partition="partition"
                    ),
                    kinesis=iot.CfnTopicRule.KinesisActionProperty(
                        role_arn="roleArn",
                        stream_name="streamName",
                
                        # the properties below are optional
                        partition_key="partitionKey"
                    ),
                    lambda_=iot.CfnTopicRule.LambdaActionProperty(
                        function_arn="functionArn"
                    ),
                    open_search=iot.CfnTopicRule.OpenSearchActionProperty(
                        endpoint="endpoint",
                        id="id",
                        index="index",
                        role_arn="roleArn",
                        type="type"
                    ),
                    republish=iot.CfnTopicRule.RepublishActionProperty(
                        role_arn="roleArn",
                        topic="topic",
                
                        # the properties below are optional
                        qos=123
                    ),
                    s3=iot.CfnTopicRule.S3ActionProperty(
                        bucket_name="bucketName",
                        key="key",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        canned_acl="cannedAcl"
                    ),
                    sns=iot.CfnTopicRule.SnsActionProperty(
                        role_arn="roleArn",
                        target_arn="targetArn",
                
                        # the properties below are optional
                        message_format="messageFormat"
                    ),
                    sqs=iot.CfnTopicRule.SqsActionProperty(
                        queue_url="queueUrl",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        use_base64=False
                    ),
                    step_functions=iot.CfnTopicRule.StepFunctionsActionProperty(
                        role_arn="roleArn",
                        state_machine_name="stateMachineName",
                
                        # the properties below are optional
                        execution_name_prefix="executionNamePrefix"
                    ),
                    timestream=iot.CfnTopicRule.TimestreamActionProperty(
                        database_name="databaseName",
                        dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        role_arn="roleArn",
                        table_name="tableName",
                
                        # the properties below are optional
                        batch_mode=False,
                        timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                            unit="unit",
                            value="value"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.ActionProperty.__init__)
                check_type(argname="argument cloudwatch_alarm", value=cloudwatch_alarm, expected_type=type_hints["cloudwatch_alarm"])
                check_type(argname="argument cloudwatch_logs", value=cloudwatch_logs, expected_type=type_hints["cloudwatch_logs"])
                check_type(argname="argument cloudwatch_metric", value=cloudwatch_metric, expected_type=type_hints["cloudwatch_metric"])
                check_type(argname="argument dynamo_db", value=dynamo_db, expected_type=type_hints["dynamo_db"])
                check_type(argname="argument dynamo_d_bv2", value=dynamo_d_bv2, expected_type=type_hints["dynamo_d_bv2"])
                check_type(argname="argument elasticsearch", value=elasticsearch, expected_type=type_hints["elasticsearch"])
                check_type(argname="argument firehose", value=firehose, expected_type=type_hints["firehose"])
                check_type(argname="argument http", value=http, expected_type=type_hints["http"])
                check_type(argname="argument iot_analytics", value=iot_analytics, expected_type=type_hints["iot_analytics"])
                check_type(argname="argument iot_events", value=iot_events, expected_type=type_hints["iot_events"])
                check_type(argname="argument iot_site_wise", value=iot_site_wise, expected_type=type_hints["iot_site_wise"])
                check_type(argname="argument kafka", value=kafka, expected_type=type_hints["kafka"])
                check_type(argname="argument kinesis", value=kinesis, expected_type=type_hints["kinesis"])
                check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
                check_type(argname="argument open_search", value=open_search, expected_type=type_hints["open_search"])
                check_type(argname="argument republish", value=republish, expected_type=type_hints["republish"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
                check_type(argname="argument sns", value=sns, expected_type=type_hints["sns"])
                check_type(argname="argument sqs", value=sqs, expected_type=type_hints["sqs"])
                check_type(argname="argument step_functions", value=step_functions, expected_type=type_hints["step_functions"])
                check_type(argname="argument timestream", value=timestream, expected_type=type_hints["timestream"])
            self._values: typing.Dict[str, typing.Any] = {}
            if cloudwatch_alarm is not None:
                self._values["cloudwatch_alarm"] = cloudwatch_alarm
            if cloudwatch_logs is not None:
                self._values["cloudwatch_logs"] = cloudwatch_logs
            if cloudwatch_metric is not None:
                self._values["cloudwatch_metric"] = cloudwatch_metric
            if dynamo_db is not None:
                self._values["dynamo_db"] = dynamo_db
            if dynamo_d_bv2 is not None:
                self._values["dynamo_d_bv2"] = dynamo_d_bv2
            if elasticsearch is not None:
                self._values["elasticsearch"] = elasticsearch
            if firehose is not None:
                self._values["firehose"] = firehose
            if http is not None:
                self._values["http"] = http
            if iot_analytics is not None:
                self._values["iot_analytics"] = iot_analytics
            if iot_events is not None:
                self._values["iot_events"] = iot_events
            if iot_site_wise is not None:
                self._values["iot_site_wise"] = iot_site_wise
            if kafka is not None:
                self._values["kafka"] = kafka
            if kinesis is not None:
                self._values["kinesis"] = kinesis
            if lambda_ is not None:
                self._values["lambda_"] = lambda_
            if open_search is not None:
                self._values["open_search"] = open_search
            if republish is not None:
                self._values["republish"] = republish
            if s3 is not None:
                self._values["s3"] = s3
            if sns is not None:
                self._values["sns"] = sns
            if sqs is not None:
                self._values["sqs"] = sqs
            if step_functions is not None:
                self._values["step_functions"] = step_functions
            if timestream is not None:
                self._values["timestream"] = timestream

        @builtins.property
        def cloudwatch_alarm(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.CloudwatchAlarmActionProperty", _IResolvable_da3f097b]]:
            '''Change the state of a CloudWatch alarm.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-cloudwatchalarm
            '''
            result = self._values.get("cloudwatch_alarm")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.CloudwatchAlarmActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def cloudwatch_logs(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.CloudwatchLogsActionProperty", _IResolvable_da3f097b]]:
            '''Sends data to CloudWatch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-cloudwatchlogs
            '''
            result = self._values.get("cloudwatch_logs")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.CloudwatchLogsActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def cloudwatch_metric(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.CloudwatchMetricActionProperty", _IResolvable_da3f097b]]:
            '''Capture a CloudWatch metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-cloudwatchmetric
            '''
            result = self._values.get("cloudwatch_metric")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.CloudwatchMetricActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def dynamo_db(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.DynamoDBActionProperty", _IResolvable_da3f097b]]:
            '''Write to a DynamoDB table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-dynamodb
            '''
            result = self._values.get("dynamo_db")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.DynamoDBActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def dynamo_d_bv2(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.DynamoDBv2ActionProperty", _IResolvable_da3f097b]]:
            '''Write to a DynamoDB table.

            This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-dynamodbv2
            '''
            result = self._values.get("dynamo_d_bv2")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.DynamoDBv2ActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def elasticsearch(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.ElasticsearchActionProperty", _IResolvable_da3f097b]]:
            '''Write data to an Amazon OpenSearch Service domain.

            .. epigraph::

               The ``Elasticsearch`` action can only be used by existing rule actions. To create a new rule action or to update an existing rule action, use the ``OpenSearch`` rule action instead. For more information, see `OpenSearchAction <https://docs.aws.amazon.com//iot/latest/apireference/API_OpenSearchAction.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-elasticsearch
            '''
            result = self._values.get("elasticsearch")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.ElasticsearchActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def firehose(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.FirehoseActionProperty", _IResolvable_da3f097b]]:
            '''Write to an Amazon Kinesis Firehose stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-firehose
            '''
            result = self._values.get("firehose")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.FirehoseActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def http(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.HttpActionProperty", _IResolvable_da3f097b]]:
            '''Send data to an HTTPS endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-http
            '''
            result = self._values.get("http")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.HttpActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def iot_analytics(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.IotAnalyticsActionProperty", _IResolvable_da3f097b]]:
            '''Sends message data to an AWS IoT Analytics channel.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-iotanalytics
            '''
            result = self._values.get("iot_analytics")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.IotAnalyticsActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def iot_events(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.IotEventsActionProperty", _IResolvable_da3f097b]]:
            '''Sends an input to an AWS IoT Events detector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-iotevents
            '''
            result = self._values.get("iot_events")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.IotEventsActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def iot_site_wise(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.IotSiteWiseActionProperty", _IResolvable_da3f097b]]:
            '''Sends data from the MQTT message that triggered the rule to AWS IoT SiteWise asset properties.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-iotsitewise
            '''
            result = self._values.get("iot_site_wise")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.IotSiteWiseActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def kafka(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.KafkaActionProperty", _IResolvable_da3f097b]]:
            '''Send messages to an Amazon Managed Streaming for Apache Kafka (Amazon MSK) or self-managed Apache Kafka cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-kafka
            '''
            result = self._values.get("kafka")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.KafkaActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def kinesis(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.KinesisActionProperty", _IResolvable_da3f097b]]:
            '''Write data to an Amazon Kinesis stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-kinesis
            '''
            result = self._values.get("kinesis")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.KinesisActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def lambda_(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.LambdaActionProperty", _IResolvable_da3f097b]]:
            '''Invoke a Lambda function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-lambda
            '''
            result = self._values.get("lambda_")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.LambdaActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def open_search(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.OpenSearchActionProperty", _IResolvable_da3f097b]]:
            '''Write data to an Amazon OpenSearch Service domain.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-opensearch
            '''
            result = self._values.get("open_search")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.OpenSearchActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def republish(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.RepublishActionProperty", _IResolvable_da3f097b]]:
            '''Publish to another MQTT topic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-republish
            '''
            result = self._values.get("republish")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.RepublishActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.S3ActionProperty", _IResolvable_da3f097b]]:
            '''Write to an Amazon S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.S3ActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def sns(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.SnsActionProperty", _IResolvable_da3f097b]]:
            '''Publish to an Amazon SNS topic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-sns
            '''
            result = self._values.get("sns")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.SnsActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def sqs(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.SqsActionProperty", _IResolvable_da3f097b]]:
            '''Publish to an Amazon SQS queue.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-sqs
            '''
            result = self._values.get("sqs")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.SqsActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def step_functions(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.StepFunctionsActionProperty", _IResolvable_da3f097b]]:
            '''Starts execution of a Step Functions state machine.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-stepfunctions
            '''
            result = self._values.get("step_functions")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.StepFunctionsActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def timestream(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.TimestreamActionProperty", _IResolvable_da3f097b]]:
            '''Writes attributes from an MQTT message.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-timestream
            '''
            result = self._values.get("timestream")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.TimestreamActionProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.AssetPropertyTimestampProperty",
        jsii_struct_bases=[],
        name_mapping={
            "time_in_seconds": "timeInSeconds",
            "offset_in_nanos": "offsetInNanos",
        },
    )
    class AssetPropertyTimestampProperty:
        def __init__(
            self,
            *,
            time_in_seconds: builtins.str,
            offset_in_nanos: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An asset property timestamp entry containing the following information.

            :param time_in_seconds: A string that contains the time in seconds since epoch. Accepts substitution templates.
            :param offset_in_nanos: Optional. A string that contains the nanosecond time offset. Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertytimestamp.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                asset_property_timestamp_property = iot.CfnTopicRule.AssetPropertyTimestampProperty(
                    time_in_seconds="timeInSeconds",
                
                    # the properties below are optional
                    offset_in_nanos="offsetInNanos"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.AssetPropertyTimestampProperty.__init__)
                check_type(argname="argument time_in_seconds", value=time_in_seconds, expected_type=type_hints["time_in_seconds"])
                check_type(argname="argument offset_in_nanos", value=offset_in_nanos, expected_type=type_hints["offset_in_nanos"])
            self._values: typing.Dict[str, typing.Any] = {
                "time_in_seconds": time_in_seconds,
            }
            if offset_in_nanos is not None:
                self._values["offset_in_nanos"] = offset_in_nanos

        @builtins.property
        def time_in_seconds(self) -> builtins.str:
            '''A string that contains the time in seconds since epoch.

            Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertytimestamp.html#cfn-iot-topicrule-assetpropertytimestamp-timeinseconds
            '''
            result = self._values.get("time_in_seconds")
            assert result is not None, "Required property 'time_in_seconds' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def offset_in_nanos(self) -> typing.Optional[builtins.str]:
            '''Optional.

            A string that contains the nanosecond time offset. Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertytimestamp.html#cfn-iot-topicrule-assetpropertytimestamp-offsetinnanos
            '''
            result = self._values.get("offset_in_nanos")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyTimestampProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.AssetPropertyValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "timestamp": "timestamp",
            "value": "value",
            "quality": "quality",
        },
    )
    class AssetPropertyValueProperty:
        def __init__(
            self,
            *,
            timestamp: typing.Union[typing.Union["CfnTopicRule.AssetPropertyTimestampProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
            value: typing.Union[typing.Union["CfnTopicRule.AssetPropertyVariantProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
            quality: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An asset property value entry containing the following information.

            :param timestamp: The asset property value timestamp.
            :param value: The value of the asset property.
            :param quality: Optional. A string that describes the quality of the value. Accepts substitution templates. Must be ``GOOD`` , ``BAD`` , or ``UNCERTAIN`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                asset_property_value_property = iot.CfnTopicRule.AssetPropertyValueProperty(
                    timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                        time_in_seconds="timeInSeconds",
                
                        # the properties below are optional
                        offset_in_nanos="offsetInNanos"
                    ),
                    value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                        boolean_value="booleanValue",
                        double_value="doubleValue",
                        integer_value="integerValue",
                        string_value="stringValue"
                    ),
                
                    # the properties below are optional
                    quality="quality"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.AssetPropertyValueProperty.__init__)
                check_type(argname="argument timestamp", value=timestamp, expected_type=type_hints["timestamp"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument quality", value=quality, expected_type=type_hints["quality"])
            self._values: typing.Dict[str, typing.Any] = {
                "timestamp": timestamp,
                "value": value,
            }
            if quality is not None:
                self._values["quality"] = quality

        @builtins.property
        def timestamp(
            self,
        ) -> typing.Union["CfnTopicRule.AssetPropertyTimestampProperty", _IResolvable_da3f097b]:
            '''The asset property value timestamp.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvalue.html#cfn-iot-topicrule-assetpropertyvalue-timestamp
            '''
            result = self._values.get("timestamp")
            assert result is not None, "Required property 'timestamp' is missing"
            return typing.cast(typing.Union["CfnTopicRule.AssetPropertyTimestampProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def value(
            self,
        ) -> typing.Union["CfnTopicRule.AssetPropertyVariantProperty", _IResolvable_da3f097b]:
            '''The value of the asset property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvalue.html#cfn-iot-topicrule-assetpropertyvalue-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union["CfnTopicRule.AssetPropertyVariantProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def quality(self) -> typing.Optional[builtins.str]:
            '''Optional.

            A string that describes the quality of the value. Accepts substitution templates. Must be ``GOOD`` , ``BAD`` , or ``UNCERTAIN`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvalue.html#cfn-iot-topicrule-assetpropertyvalue-quality
            '''
            result = self._values.get("quality")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.AssetPropertyVariantProperty",
        jsii_struct_bases=[],
        name_mapping={
            "boolean_value": "booleanValue",
            "double_value": "doubleValue",
            "integer_value": "integerValue",
            "string_value": "stringValue",
        },
    )
    class AssetPropertyVariantProperty:
        def __init__(
            self,
            *,
            boolean_value: typing.Optional[builtins.str] = None,
            double_value: typing.Optional[builtins.str] = None,
            integer_value: typing.Optional[builtins.str] = None,
            string_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains an asset property value (of a single type).

            :param boolean_value: Optional. A string that contains the boolean value ( ``true`` or ``false`` ) of the value entry. Accepts substitution templates.
            :param double_value: Optional. A string that contains the double value of the value entry. Accepts substitution templates.
            :param integer_value: Optional. A string that contains the integer value of the value entry. Accepts substitution templates.
            :param string_value: Optional. The string value of the value entry. Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                asset_property_variant_property = iot.CfnTopicRule.AssetPropertyVariantProperty(
                    boolean_value="booleanValue",
                    double_value="doubleValue",
                    integer_value="integerValue",
                    string_value="stringValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.AssetPropertyVariantProperty.__init__)
                check_type(argname="argument boolean_value", value=boolean_value, expected_type=type_hints["boolean_value"])
                check_type(argname="argument double_value", value=double_value, expected_type=type_hints["double_value"])
                check_type(argname="argument integer_value", value=integer_value, expected_type=type_hints["integer_value"])
                check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
            self._values: typing.Dict[str, typing.Any] = {}
            if boolean_value is not None:
                self._values["boolean_value"] = boolean_value
            if double_value is not None:
                self._values["double_value"] = double_value
            if integer_value is not None:
                self._values["integer_value"] = integer_value
            if string_value is not None:
                self._values["string_value"] = string_value

        @builtins.property
        def boolean_value(self) -> typing.Optional[builtins.str]:
            '''Optional.

            A string that contains the boolean value ( ``true`` or ``false`` ) of the value entry. Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html#cfn-iot-topicrule-assetpropertyvariant-booleanvalue
            '''
            result = self._values.get("boolean_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def double_value(self) -> typing.Optional[builtins.str]:
            '''Optional.

            A string that contains the double value of the value entry. Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html#cfn-iot-topicrule-assetpropertyvariant-doublevalue
            '''
            result = self._values.get("double_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def integer_value(self) -> typing.Optional[builtins.str]:
            '''Optional.

            A string that contains the integer value of the value entry. Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html#cfn-iot-topicrule-assetpropertyvariant-integervalue
            '''
            result = self._values.get("integer_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            '''Optional.

            The string value of the value entry. Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html#cfn-iot-topicrule-assetpropertyvariant-stringvalue
            '''
            result = self._values.get("string_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyVariantProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.CloudwatchAlarmActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alarm_name": "alarmName",
            "role_arn": "roleArn",
            "state_reason": "stateReason",
            "state_value": "stateValue",
        },
    )
    class CloudwatchAlarmActionProperty:
        def __init__(
            self,
            *,
            alarm_name: builtins.str,
            role_arn: builtins.str,
            state_reason: builtins.str,
            state_value: builtins.str,
        ) -> None:
            '''Describes an action that updates a CloudWatch alarm.

            :param alarm_name: The CloudWatch alarm name.
            :param role_arn: The IAM role that allows access to the CloudWatch alarm.
            :param state_reason: The reason for the alarm change.
            :param state_value: The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                cloudwatch_alarm_action_property = iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                    alarm_name="alarmName",
                    role_arn="roleArn",
                    state_reason="stateReason",
                    state_value="stateValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.CloudwatchAlarmActionProperty.__init__)
                check_type(argname="argument alarm_name", value=alarm_name, expected_type=type_hints["alarm_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument state_reason", value=state_reason, expected_type=type_hints["state_reason"])
                check_type(argname="argument state_value", value=state_value, expected_type=type_hints["state_value"])
            self._values: typing.Dict[str, typing.Any] = {
                "alarm_name": alarm_name,
                "role_arn": role_arn,
                "state_reason": state_reason,
                "state_value": state_value,
            }

        @builtins.property
        def alarm_name(self) -> builtins.str:
            '''The CloudWatch alarm name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html#cfn-iot-topicrule-cloudwatchalarmaction-alarmname
            '''
            result = self._values.get("alarm_name")
            assert result is not None, "Required property 'alarm_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The IAM role that allows access to the CloudWatch alarm.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html#cfn-iot-topicrule-cloudwatchalarmaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def state_reason(self) -> builtins.str:
            '''The reason for the alarm change.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html#cfn-iot-topicrule-cloudwatchalarmaction-statereason
            '''
            result = self._values.get("state_reason")
            assert result is not None, "Required property 'state_reason' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def state_value(self) -> builtins.str:
            '''The value of the alarm state.

            Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html#cfn-iot-topicrule-cloudwatchalarmaction-statevalue
            '''
            result = self._values.get("state_value")
            assert result is not None, "Required property 'state_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudwatchAlarmActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.CloudwatchLogsActionProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName", "role_arn": "roleArn"},
    )
    class CloudwatchLogsActionProperty:
        def __init__(
            self,
            *,
            log_group_name: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''Describes an action that updates a CloudWatch log.

            :param log_group_name: The CloudWatch log name.
            :param role_arn: The IAM role that allows access to the CloudWatch log.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchlogsaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                cloudwatch_logs_action_property = iot.CfnTopicRule.CloudwatchLogsActionProperty(
                    log_group_name="logGroupName",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.CloudwatchLogsActionProperty.__init__)
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "log_group_name": log_group_name,
                "role_arn": role_arn,
            }

        @builtins.property
        def log_group_name(self) -> builtins.str:
            '''The CloudWatch log name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchlogsaction.html#cfn-iot-topicrule-cloudwatchlogsaction-loggroupname
            '''
            result = self._values.get("log_group_name")
            assert result is not None, "Required property 'log_group_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The IAM role that allows access to the CloudWatch log.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchlogsaction.html#cfn-iot-topicrule-cloudwatchlogsaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudwatchLogsActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.CloudwatchMetricActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "metric_namespace": "metricNamespace",
            "metric_unit": "metricUnit",
            "metric_value": "metricValue",
            "role_arn": "roleArn",
            "metric_timestamp": "metricTimestamp",
        },
    )
    class CloudwatchMetricActionProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            metric_namespace: builtins.str,
            metric_unit: builtins.str,
            metric_value: builtins.str,
            role_arn: builtins.str,
            metric_timestamp: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action that captures a CloudWatch metric.

            :param metric_name: The CloudWatch metric name.
            :param metric_namespace: The CloudWatch metric namespace name.
            :param metric_unit: The `metric unit <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`_ supported by CloudWatch.
            :param metric_value: The CloudWatch metric value.
            :param role_arn: The IAM role that allows access to the CloudWatch metric.
            :param metric_timestamp: An optional `Unix timestamp <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                cloudwatch_metric_action_property = iot.CfnTopicRule.CloudwatchMetricActionProperty(
                    metric_name="metricName",
                    metric_namespace="metricNamespace",
                    metric_unit="metricUnit",
                    metric_value="metricValue",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    metric_timestamp="metricTimestamp"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.CloudwatchMetricActionProperty.__init__)
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument metric_namespace", value=metric_namespace, expected_type=type_hints["metric_namespace"])
                check_type(argname="argument metric_unit", value=metric_unit, expected_type=type_hints["metric_unit"])
                check_type(argname="argument metric_value", value=metric_value, expected_type=type_hints["metric_value"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument metric_timestamp", value=metric_timestamp, expected_type=type_hints["metric_timestamp"])
            self._values: typing.Dict[str, typing.Any] = {
                "metric_name": metric_name,
                "metric_namespace": metric_namespace,
                "metric_unit": metric_unit,
                "metric_value": metric_value,
                "role_arn": role_arn,
            }
            if metric_timestamp is not None:
                self._values["metric_timestamp"] = metric_timestamp

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''The CloudWatch metric name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_namespace(self) -> builtins.str:
            '''The CloudWatch metric namespace name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-metricnamespace
            '''
            result = self._values.get("metric_namespace")
            assert result is not None, "Required property 'metric_namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_unit(self) -> builtins.str:
            '''The `metric unit <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`_ supported by CloudWatch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-metricunit
            '''
            result = self._values.get("metric_unit")
            assert result is not None, "Required property 'metric_unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_value(self) -> builtins.str:
            '''The CloudWatch metric value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-metricvalue
            '''
            result = self._values.get("metric_value")
            assert result is not None, "Required property 'metric_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The IAM role that allows access to the CloudWatch metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_timestamp(self) -> typing.Optional[builtins.str]:
            '''An optional `Unix timestamp <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-metrictimestamp
            '''
            result = self._values.get("metric_timestamp")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudwatchMetricActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.DynamoDBActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hash_key_field": "hashKeyField",
            "hash_key_value": "hashKeyValue",
            "role_arn": "roleArn",
            "table_name": "tableName",
            "hash_key_type": "hashKeyType",
            "payload_field": "payloadField",
            "range_key_field": "rangeKeyField",
            "range_key_type": "rangeKeyType",
            "range_key_value": "rangeKeyValue",
        },
    )
    class DynamoDBActionProperty:
        def __init__(
            self,
            *,
            hash_key_field: builtins.str,
            hash_key_value: builtins.str,
            role_arn: builtins.str,
            table_name: builtins.str,
            hash_key_type: typing.Optional[builtins.str] = None,
            payload_field: typing.Optional[builtins.str] = None,
            range_key_field: typing.Optional[builtins.str] = None,
            range_key_type: typing.Optional[builtins.str] = None,
            range_key_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action to write to a DynamoDB table.

            The ``tableName`` , ``hashKeyField`` , and ``rangeKeyField`` values must match the values used when you created the table.

            The ``hashKeyValue`` and ``rangeKeyvalue`` fields use a substitution template syntax. These templates provide data at runtime. The syntax is as follows: ${ *sql-expression* }.

            You can specify any valid expression in a WHERE or SELECT clause, including JSON properties, comparisons, calculations, and functions. For example, the following field uses the third level of the topic:

            ``"hashKeyValue": "${topic(3)}"``

            The following field uses the timestamp:

            ``"rangeKeyValue": "${timestamp()}"``

            For more information, see `DynamoDBv2 Action <https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html>`_ in the *AWS IoT Developer Guide* .

            :param hash_key_field: The hash key name.
            :param hash_key_value: The hash key value.
            :param role_arn: The ARN of the IAM role that grants access to the DynamoDB table.
            :param table_name: The name of the DynamoDB table.
            :param hash_key_type: The hash key type. Valid values are "STRING" or "NUMBER"
            :param payload_field: The action payload. This name can be customized.
            :param range_key_field: The range key name.
            :param range_key_type: The range key type. Valid values are "STRING" or "NUMBER"
            :param range_key_value: The range key value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                dynamo_dBAction_property = iot.CfnTopicRule.DynamoDBActionProperty(
                    hash_key_field="hashKeyField",
                    hash_key_value="hashKeyValue",
                    role_arn="roleArn",
                    table_name="tableName",
                
                    # the properties below are optional
                    hash_key_type="hashKeyType",
                    payload_field="payloadField",
                    range_key_field="rangeKeyField",
                    range_key_type="rangeKeyType",
                    range_key_value="rangeKeyValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.DynamoDBActionProperty.__init__)
                check_type(argname="argument hash_key_field", value=hash_key_field, expected_type=type_hints["hash_key_field"])
                check_type(argname="argument hash_key_value", value=hash_key_value, expected_type=type_hints["hash_key_value"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument hash_key_type", value=hash_key_type, expected_type=type_hints["hash_key_type"])
                check_type(argname="argument payload_field", value=payload_field, expected_type=type_hints["payload_field"])
                check_type(argname="argument range_key_field", value=range_key_field, expected_type=type_hints["range_key_field"])
                check_type(argname="argument range_key_type", value=range_key_type, expected_type=type_hints["range_key_type"])
                check_type(argname="argument range_key_value", value=range_key_value, expected_type=type_hints["range_key_value"])
            self._values: typing.Dict[str, typing.Any] = {
                "hash_key_field": hash_key_field,
                "hash_key_value": hash_key_value,
                "role_arn": role_arn,
                "table_name": table_name,
            }
            if hash_key_type is not None:
                self._values["hash_key_type"] = hash_key_type
            if payload_field is not None:
                self._values["payload_field"] = payload_field
            if range_key_field is not None:
                self._values["range_key_field"] = range_key_field
            if range_key_type is not None:
                self._values["range_key_type"] = range_key_type
            if range_key_value is not None:
                self._values["range_key_value"] = range_key_value

        @builtins.property
        def hash_key_field(self) -> builtins.str:
            '''The hash key name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-hashkeyfield
            '''
            result = self._values.get("hash_key_field")
            assert result is not None, "Required property 'hash_key_field' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hash_key_value(self) -> builtins.str:
            '''The hash key value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-hashkeyvalue
            '''
            result = self._values.get("hash_key_value")
            assert result is not None, "Required property 'hash_key_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that grants access to the DynamoDB table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The name of the DynamoDB table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hash_key_type(self) -> typing.Optional[builtins.str]:
            '''The hash key type.

            Valid values are "STRING" or "NUMBER"

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-hashkeytype
            '''
            result = self._values.get("hash_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def payload_field(self) -> typing.Optional[builtins.str]:
            '''The action payload.

            This name can be customized.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-payloadfield
            '''
            result = self._values.get("payload_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range_key_field(self) -> typing.Optional[builtins.str]:
            '''The range key name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-rangekeyfield
            '''
            result = self._values.get("range_key_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range_key_type(self) -> typing.Optional[builtins.str]:
            '''The range key type.

            Valid values are "STRING" or "NUMBER"

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-rangekeytype
            '''
            result = self._values.get("range_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range_key_value(self) -> typing.Optional[builtins.str]:
            '''The range key value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-rangekeyvalue
            '''
            result = self._values.get("range_key_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.DynamoDBv2ActionProperty",
        jsii_struct_bases=[],
        name_mapping={"put_item": "putItem", "role_arn": "roleArn"},
    )
    class DynamoDBv2ActionProperty:
        def __init__(
            self,
            *,
            put_item: typing.Optional[typing.Union[typing.Union["CfnTopicRule.PutItemInputProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action to write to a DynamoDB table.

            This DynamoDB action writes each attribute in the message payload into it's own column in the DynamoDB table.

            :param put_item: Specifies the DynamoDB table to which the message data will be written. For example:. ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }`` Each attribute in the message payload will be written to a separate column in the DynamoDB database.
            :param role_arn: The ARN of the IAM role that grants access to the DynamoDB table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbv2action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                dynamo_dBv2_action_property = iot.CfnTopicRule.DynamoDBv2ActionProperty(
                    put_item=iot.CfnTopicRule.PutItemInputProperty(
                        table_name="tableName"
                    ),
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.DynamoDBv2ActionProperty.__init__)
                check_type(argname="argument put_item", value=put_item, expected_type=type_hints["put_item"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[str, typing.Any] = {}
            if put_item is not None:
                self._values["put_item"] = put_item
            if role_arn is not None:
                self._values["role_arn"] = role_arn

        @builtins.property
        def put_item(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.PutItemInputProperty", _IResolvable_da3f097b]]:
            '''Specifies the DynamoDB table to which the message data will be written. For example:.

            ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }``

            Each attribute in the message payload will be written to a separate column in the DynamoDB database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbv2action.html#cfn-iot-topicrule-dynamodbv2action-putitem
            '''
            result = self._values.get("put_item")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.PutItemInputProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the IAM role that grants access to the DynamoDB table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbv2action.html#cfn-iot-topicrule-dynamodbv2action-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBv2ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.ElasticsearchActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint": "endpoint",
            "id": "id",
            "index": "index",
            "role_arn": "roleArn",
            "type": "type",
        },
    )
    class ElasticsearchActionProperty:
        def __init__(
            self,
            *,
            endpoint: builtins.str,
            id: builtins.str,
            index: builtins.str,
            role_arn: builtins.str,
            type: builtins.str,
        ) -> None:
            '''Describes an action that writes data to an Amazon OpenSearch Service domain.

            .. epigraph::

               The ``Elasticsearch`` action can only be used by existing rule actions. To create a new rule action or to update an existing rule action, use the ``OpenSearch`` rule action instead. For more information, see `OpenSearchAction <https://docs.aws.amazon.com//iot/latest/apireference/API_OpenSearchAction.html>`_ .

            :param endpoint: The endpoint of your OpenSearch domain.
            :param id: The unique identifier for the document you are storing.
            :param index: The index where you want to store your data.
            :param role_arn: The IAM role ARN that has access to OpenSearch.
            :param type: The type of document you are storing.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                elasticsearch_action_property = iot.CfnTopicRule.ElasticsearchActionProperty(
                    endpoint="endpoint",
                    id="id",
                    index="index",
                    role_arn="roleArn",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.ElasticsearchActionProperty.__init__)
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument index", value=index, expected_type=type_hints["index"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint": endpoint,
                "id": id,
                "index": index,
                "role_arn": role_arn,
                "type": type,
            }

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''The endpoint of your OpenSearch domain.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html#cfn-iot-topicrule-elasticsearchaction-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def id(self) -> builtins.str:
            '''The unique identifier for the document you are storing.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html#cfn-iot-topicrule-elasticsearchaction-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def index(self) -> builtins.str:
            '''The index where you want to store your data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html#cfn-iot-topicrule-elasticsearchaction-index
            '''
            result = self._values.get("index")
            assert result is not None, "Required property 'index' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The IAM role ARN that has access to OpenSearch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html#cfn-iot-topicrule-elasticsearchaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of document you are storing.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html#cfn-iot-topicrule-elasticsearchaction-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.FirehoseActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delivery_stream_name": "deliveryStreamName",
            "role_arn": "roleArn",
            "batch_mode": "batchMode",
            "separator": "separator",
        },
    )
    class FirehoseActionProperty:
        def __init__(
            self,
            *,
            delivery_stream_name: builtins.str,
            role_arn: builtins.str,
            batch_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            separator: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action that writes data to an Amazon Kinesis Firehose stream.

            :param delivery_stream_name: The delivery stream name.
            :param role_arn: The IAM role that grants access to the Amazon Kinesis Firehose stream.
            :param batch_mode: Whether to deliver the Kinesis Data Firehose stream as a batch by using ```PutRecordBatch`` <https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html>`_ . The default value is ``false`` . When ``batchMode`` is ``true`` and the rule's SQL statement evaluates to an Array, each Array element forms one record in the ```PutRecordBatch`` <https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html>`_ request. The resulting array can't have more than 500 records.
            :param separator: A character separator that will be used to separate records written to the Firehose stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                firehose_action_property = iot.CfnTopicRule.FirehoseActionProperty(
                    delivery_stream_name="deliveryStreamName",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    batch_mode=False,
                    separator="separator"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.FirehoseActionProperty.__init__)
                check_type(argname="argument delivery_stream_name", value=delivery_stream_name, expected_type=type_hints["delivery_stream_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument batch_mode", value=batch_mode, expected_type=type_hints["batch_mode"])
                check_type(argname="argument separator", value=separator, expected_type=type_hints["separator"])
            self._values: typing.Dict[str, typing.Any] = {
                "delivery_stream_name": delivery_stream_name,
                "role_arn": role_arn,
            }
            if batch_mode is not None:
                self._values["batch_mode"] = batch_mode
            if separator is not None:
                self._values["separator"] = separator

        @builtins.property
        def delivery_stream_name(self) -> builtins.str:
            '''The delivery stream name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html#cfn-iot-topicrule-firehoseaction-deliverystreamname
            '''
            result = self._values.get("delivery_stream_name")
            assert result is not None, "Required property 'delivery_stream_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The IAM role that grants access to the Amazon Kinesis Firehose stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html#cfn-iot-topicrule-firehoseaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_mode(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether to deliver the Kinesis Data Firehose stream as a batch by using ```PutRecordBatch`` <https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html>`_ . The default value is ``false`` .

            When ``batchMode`` is ``true`` and the rule's SQL statement evaluates to an Array, each Array element forms one record in the ```PutRecordBatch`` <https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html>`_ request. The resulting array can't have more than 500 records.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html#cfn-iot-topicrule-firehoseaction-batchmode
            '''
            result = self._values.get("batch_mode")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def separator(self) -> typing.Optional[builtins.str]:
            '''A character separator that will be used to separate records written to the Firehose stream.

            Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html#cfn-iot-topicrule-firehoseaction-separator
            '''
            result = self._values.get("separator")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirehoseActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.HttpActionHeaderProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class HttpActionHeaderProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''The HTTP action header.

            :param key: The HTTP header key.
            :param value: The HTTP header value. Substitution templates are supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpactionheader.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                http_action_header_property = iot.CfnTopicRule.HttpActionHeaderProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.HttpActionHeaderProperty.__init__)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The HTTP header key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpactionheader.html#cfn-iot-topicrule-httpactionheader-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The HTTP header value.

            Substitution templates are supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpactionheader.html#cfn-iot-topicrule-httpactionheader-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpActionHeaderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.HttpActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "url": "url",
            "auth": "auth",
            "confirmation_url": "confirmationUrl",
            "headers": "headers",
        },
    )
    class HttpActionProperty:
        def __init__(
            self,
            *,
            url: builtins.str,
            auth: typing.Optional[typing.Union[typing.Union["CfnTopicRule.HttpAuthorizationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            confirmation_url: typing.Optional[builtins.str] = None,
            headers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnTopicRule.HttpActionHeaderProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''Send data to an HTTPS endpoint.

            :param url: The endpoint URL. If substitution templates are used in the URL, you must also specify a ``confirmationUrl`` . If this is a new destination, a new ``TopicRuleDestination`` is created if possible.
            :param auth: The authentication method to use when sending data to an HTTPS endpoint.
            :param confirmation_url: The URL to which AWS IoT sends a confirmation message. The value of the confirmation URL must be a prefix of the endpoint URL. If you do not specify a confirmation URL AWS IoT uses the endpoint URL as the confirmation URL. If you use substitution templates in the confirmationUrl, you must create and enable topic rule destinations that match each possible value of the substitution template before traffic is allowed to your endpoint URL.
            :param headers: The HTTP headers to send with the message data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                http_action_property = iot.CfnTopicRule.HttpActionProperty(
                    url="url",
                
                    # the properties below are optional
                    auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                        sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                            role_arn="roleArn",
                            service_name="serviceName",
                            signing_region="signingRegion"
                        )
                    ),
                    confirmation_url="confirmationUrl",
                    headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.HttpActionProperty.__init__)
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
                check_type(argname="argument confirmation_url", value=confirmation_url, expected_type=type_hints["confirmation_url"])
                check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            self._values: typing.Dict[str, typing.Any] = {
                "url": url,
            }
            if auth is not None:
                self._values["auth"] = auth
            if confirmation_url is not None:
                self._values["confirmation_url"] = confirmation_url
            if headers is not None:
                self._values["headers"] = headers

        @builtins.property
        def url(self) -> builtins.str:
            '''The endpoint URL.

            If substitution templates are used in the URL, you must also specify a ``confirmationUrl`` . If this is a new destination, a new ``TopicRuleDestination`` is created if possible.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html#cfn-iot-topicrule-httpaction-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def auth(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.HttpAuthorizationProperty", _IResolvable_da3f097b]]:
            '''The authentication method to use when sending data to an HTTPS endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html#cfn-iot-topicrule-httpaction-auth
            '''
            result = self._values.get("auth")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.HttpAuthorizationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def confirmation_url(self) -> typing.Optional[builtins.str]:
            '''The URL to which AWS IoT sends a confirmation message.

            The value of the confirmation URL must be a prefix of the endpoint URL. If you do not specify a confirmation URL AWS IoT uses the endpoint URL as the confirmation URL. If you use substitution templates in the confirmationUrl, you must create and enable topic rule destinations that match each possible value of the substitution template before traffic is allowed to your endpoint URL.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html#cfn-iot-topicrule-httpaction-confirmationurl
            '''
            result = self._values.get("confirmation_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def headers(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTopicRule.HttpActionHeaderProperty", _IResolvable_da3f097b]]]]:
            '''The HTTP headers to send with the message data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html#cfn-iot-topicrule-httpaction-headers
            '''
            result = self._values.get("headers")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTopicRule.HttpActionHeaderProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.HttpAuthorizationProperty",
        jsii_struct_bases=[],
        name_mapping={"sigv4": "sigv4"},
    )
    class HttpAuthorizationProperty:
        def __init__(
            self,
            *,
            sigv4: typing.Optional[typing.Union[typing.Union["CfnTopicRule.SigV4AuthorizationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The authorization method used to send messages.

            :param sigv4: Use Sig V4 authorization. For more information, see `Signature Version 4 Signing Process <https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpauthorization.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                http_authorization_property = iot.CfnTopicRule.HttpAuthorizationProperty(
                    sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                        role_arn="roleArn",
                        service_name="serviceName",
                        signing_region="signingRegion"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.HttpAuthorizationProperty.__init__)
                check_type(argname="argument sigv4", value=sigv4, expected_type=type_hints["sigv4"])
            self._values: typing.Dict[str, typing.Any] = {}
            if sigv4 is not None:
                self._values["sigv4"] = sigv4

        @builtins.property
        def sigv4(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.SigV4AuthorizationProperty", _IResolvable_da3f097b]]:
            '''Use Sig V4 authorization.

            For more information, see `Signature Version 4 Signing Process <https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpauthorization.html#cfn-iot-topicrule-httpauthorization-sigv4
            '''
            result = self._values.get("sigv4")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.SigV4AuthorizationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpAuthorizationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.IotAnalyticsActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "channel_name": "channelName",
            "role_arn": "roleArn",
            "batch_mode": "batchMode",
        },
    )
    class IotAnalyticsActionProperty:
        def __init__(
            self,
            *,
            channel_name: builtins.str,
            role_arn: builtins.str,
            batch_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Sends message data to an AWS IoT Analytics channel.

            :param channel_name: The name of the IoT Analytics channel to which message data will be sent.
            :param role_arn: The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).
            :param batch_mode: Whether to process the action as a batch. The default value is ``false`` . When ``batchMode`` is ``true`` and the rule SQL statement evaluates to an Array, each Array element is delivered as a separate message when passed by ```BatchPutMessage`` <https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_BatchPutMessage.html>`_ The resulting array can't have more than 100 messages.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotanalyticsaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                iot_analytics_action_property = iot.CfnTopicRule.IotAnalyticsActionProperty(
                    channel_name="channelName",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    batch_mode=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.IotAnalyticsActionProperty.__init__)
                check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument batch_mode", value=batch_mode, expected_type=type_hints["batch_mode"])
            self._values: typing.Dict[str, typing.Any] = {
                "channel_name": channel_name,
                "role_arn": role_arn,
            }
            if batch_mode is not None:
                self._values["batch_mode"] = batch_mode

        @builtins.property
        def channel_name(self) -> builtins.str:
            '''The name of the IoT Analytics channel to which message data will be sent.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotanalyticsaction.html#cfn-iot-topicrule-iotanalyticsaction-channelname
            '''
            result = self._values.get("channel_name")
            assert result is not None, "Required property 'channel_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotanalyticsaction.html#cfn-iot-topicrule-iotanalyticsaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_mode(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether to process the action as a batch. The default value is ``false`` .

            When ``batchMode`` is ``true`` and the rule SQL statement evaluates to an Array, each Array element is delivered as a separate message when passed by ```BatchPutMessage`` <https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_BatchPutMessage.html>`_ The resulting array can't have more than 100 messages.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotanalyticsaction.html#cfn-iot-topicrule-iotanalyticsaction-batchmode
            '''
            result = self._values.get("batch_mode")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotAnalyticsActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.IotEventsActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_name": "inputName",
            "role_arn": "roleArn",
            "batch_mode": "batchMode",
            "message_id": "messageId",
        },
    )
    class IotEventsActionProperty:
        def __init__(
            self,
            *,
            input_name: builtins.str,
            role_arn: builtins.str,
            batch_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            message_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Sends an input to an AWS IoT Events detector.

            :param input_name: The name of the AWS IoT Events input.
            :param role_arn: The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. ("Action":"iotevents:BatchPutMessage").
            :param batch_mode: Whether to process the event actions as a batch. The default value is ``false`` . When ``batchMode`` is ``true`` , you can't specify a ``messageId`` . When ``batchMode`` is ``true`` and the rule SQL statement evaluates to an Array, each Array element is treated as a separate message when Events by calling ```BatchPutMessage`` <https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchPutMessage.html>`_ . The resulting array can't have more than 10 messages.
            :param message_id: The ID of the message. The default ``messageId`` is a new UUID value. When ``batchMode`` is ``true`` , you can't specify a ``messageId`` --a new UUID value will be assigned. Assign a value to this property to ensure that only one input (message) with a given ``messageId`` will be processed by an AWS IoT Events detector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                iot_events_action_property = iot.CfnTopicRule.IotEventsActionProperty(
                    input_name="inputName",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    batch_mode=False,
                    message_id="messageId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.IotEventsActionProperty.__init__)
                check_type(argname="argument input_name", value=input_name, expected_type=type_hints["input_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument batch_mode", value=batch_mode, expected_type=type_hints["batch_mode"])
                check_type(argname="argument message_id", value=message_id, expected_type=type_hints["message_id"])
            self._values: typing.Dict[str, typing.Any] = {
                "input_name": input_name,
                "role_arn": role_arn,
            }
            if batch_mode is not None:
                self._values["batch_mode"] = batch_mode
            if message_id is not None:
                self._values["message_id"] = message_id

        @builtins.property
        def input_name(self) -> builtins.str:
            '''The name of the AWS IoT Events input.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html#cfn-iot-topicrule-ioteventsaction-inputname
            '''
            result = self._values.get("input_name")
            assert result is not None, "Required property 'input_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector.

            ("Action":"iotevents:BatchPutMessage").

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html#cfn-iot-topicrule-ioteventsaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_mode(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether to process the event actions as a batch. The default value is ``false`` .

            When ``batchMode`` is ``true`` , you can't specify a ``messageId`` .

            When ``batchMode`` is ``true`` and the rule SQL statement evaluates to an Array, each Array element is treated as a separate message when Events by calling ```BatchPutMessage`` <https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchPutMessage.html>`_ . The resulting array can't have more than 10 messages.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html#cfn-iot-topicrule-ioteventsaction-batchmode
            '''
            result = self._values.get("batch_mode")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def message_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the message. The default ``messageId`` is a new UUID value.

            When ``batchMode`` is ``true`` , you can't specify a ``messageId`` --a new UUID value will be assigned.

            Assign a value to this property to ensure that only one input (message) with a given ``messageId`` will be processed by an AWS IoT Events detector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html#cfn-iot-topicrule-ioteventsaction-messageid
            '''
            result = self._values.get("message_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotEventsActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.IotSiteWiseActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "put_asset_property_value_entries": "putAssetPropertyValueEntries",
            "role_arn": "roleArn",
        },
    )
    class IotSiteWiseActionProperty:
        def __init__(
            self,
            *,
            put_asset_property_value_entries: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnTopicRule.PutAssetPropertyValueEntryProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
            role_arn: builtins.str,
        ) -> None:
            '''Describes an action to send data from an MQTT message that triggered the rule to AWS IoT SiteWise asset properties.

            :param put_asset_property_value_entries: A list of asset property value entries.
            :param role_arn: The ARN of the role that grants AWS IoT permission to send an asset property value to AWS IoT SiteWise. ( ``"Action": "iotsitewise:BatchPutAssetPropertyValue"`` ). The trust policy can restrict access to specific asset hierarchy paths.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotsitewiseaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                iot_site_wise_action_property = iot.CfnTopicRule.IotSiteWiseActionProperty(
                    put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                        property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                            timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                time_in_seconds="timeInSeconds",
                
                                # the properties below are optional
                                offset_in_nanos="offsetInNanos"
                            ),
                            value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                boolean_value="booleanValue",
                                double_value="doubleValue",
                                integer_value="integerValue",
                                string_value="stringValue"
                            ),
                
                            # the properties below are optional
                            quality="quality"
                        )],
                
                        # the properties below are optional
                        asset_id="assetId",
                        entry_id="entryId",
                        property_alias="propertyAlias",
                        property_id="propertyId"
                    )],
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.IotSiteWiseActionProperty.__init__)
                check_type(argname="argument put_asset_property_value_entries", value=put_asset_property_value_entries, expected_type=type_hints["put_asset_property_value_entries"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "put_asset_property_value_entries": put_asset_property_value_entries,
                "role_arn": role_arn,
            }

        @builtins.property
        def put_asset_property_value_entries(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTopicRule.PutAssetPropertyValueEntryProperty", _IResolvable_da3f097b]]]:
            '''A list of asset property value entries.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotsitewiseaction.html#cfn-iot-topicrule-iotsitewiseaction-putassetpropertyvalueentries
            '''
            result = self._values.get("put_asset_property_value_entries")
            assert result is not None, "Required property 'put_asset_property_value_entries' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTopicRule.PutAssetPropertyValueEntryProperty", _IResolvable_da3f097b]]], result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that grants AWS IoT permission to send an asset property value to AWS IoT SiteWise.

            ( ``"Action": "iotsitewise:BatchPutAssetPropertyValue"`` ). The trust policy can restrict access to specific asset hierarchy paths.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotsitewiseaction.html#cfn-iot-topicrule-iotsitewiseaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotSiteWiseActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.KafkaActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_properties": "clientProperties",
            "destination_arn": "destinationArn",
            "topic": "topic",
            "key": "key",
            "partition": "partition",
        },
    )
    class KafkaActionProperty:
        def __init__(
            self,
            *,
            client_properties: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
            destination_arn: builtins.str,
            topic: builtins.str,
            key: typing.Optional[builtins.str] = None,
            partition: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Send messages to an Amazon Managed Streaming for Apache Kafka (Amazon MSK) or self-managed Apache Kafka cluster.

            :param client_properties: Properties of the Apache Kafka producer client.
            :param destination_arn: The ARN of Kafka action's VPC ``TopicRuleDestination`` .
            :param topic: The Kafka topic for messages to be sent to the Kafka broker.
            :param key: The Kafka message key.
            :param partition: The Kafka message partition.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                kafka_action_property = iot.CfnTopicRule.KafkaActionProperty(
                    client_properties={
                        "client_properties_key": "clientProperties"
                    },
                    destination_arn="destinationArn",
                    topic="topic",
                
                    # the properties below are optional
                    key="key",
                    partition="partition"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.KafkaActionProperty.__init__)
                check_type(argname="argument client_properties", value=client_properties, expected_type=type_hints["client_properties"])
                check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
                check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            self._values: typing.Dict[str, typing.Any] = {
                "client_properties": client_properties,
                "destination_arn": destination_arn,
                "topic": topic,
            }
            if key is not None:
                self._values["key"] = key
            if partition is not None:
                self._values["partition"] = partition

        @builtins.property
        def client_properties(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]:
            '''Properties of the Apache Kafka producer client.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-clientproperties
            '''
            result = self._values.get("client_properties")
            assert result is not None, "Required property 'client_properties' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]], result)

        @builtins.property
        def destination_arn(self) -> builtins.str:
            '''The ARN of Kafka action's VPC ``TopicRuleDestination`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-destinationarn
            '''
            result = self._values.get("destination_arn")
            assert result is not None, "Required property 'destination_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def topic(self) -> builtins.str:
            '''The Kafka topic for messages to be sent to the Kafka broker.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-topic
            '''
            result = self._values.get("topic")
            assert result is not None, "Required property 'topic' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The Kafka message key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def partition(self) -> typing.Optional[builtins.str]:
            '''The Kafka message partition.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-partition
            '''
            result = self._values.get("partition")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KafkaActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.KinesisActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "stream_name": "streamName",
            "partition_key": "partitionKey",
        },
    )
    class KinesisActionProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            stream_name: builtins.str,
            partition_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action to write data to an Amazon Kinesis stream.

            :param role_arn: The ARN of the IAM role that grants access to the Amazon Kinesis stream.
            :param stream_name: The name of the Amazon Kinesis stream.
            :param partition_key: The partition key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kinesisaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                kinesis_action_property = iot.CfnTopicRule.KinesisActionProperty(
                    role_arn="roleArn",
                    stream_name="streamName",
                
                    # the properties below are optional
                    partition_key="partitionKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.KinesisActionProperty.__init__)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument stream_name", value=stream_name, expected_type=type_hints["stream_name"])
                check_type(argname="argument partition_key", value=partition_key, expected_type=type_hints["partition_key"])
            self._values: typing.Dict[str, typing.Any] = {
                "role_arn": role_arn,
                "stream_name": stream_name,
            }
            if partition_key is not None:
                self._values["partition_key"] = partition_key

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that grants access to the Amazon Kinesis stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kinesisaction.html#cfn-iot-topicrule-kinesisaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def stream_name(self) -> builtins.str:
            '''The name of the Amazon Kinesis stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kinesisaction.html#cfn-iot-topicrule-kinesisaction-streamname
            '''
            result = self._values.get("stream_name")
            assert result is not None, "Required property 'stream_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def partition_key(self) -> typing.Optional[builtins.str]:
            '''The partition key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kinesisaction.html#cfn-iot-topicrule-kinesisaction-partitionkey
            '''
            result = self._values.get("partition_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.LambdaActionProperty",
        jsii_struct_bases=[],
        name_mapping={"function_arn": "functionArn"},
    )
    class LambdaActionProperty:
        def __init__(
            self,
            *,
            function_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action to invoke a Lambda function.

            :param function_arn: The ARN of the Lambda function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-lambdaaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                lambda_action_property = iot.CfnTopicRule.LambdaActionProperty(
                    function_arn="functionArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.LambdaActionProperty.__init__)
                check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
            self._values: typing.Dict[str, typing.Any] = {}
            if function_arn is not None:
                self._values["function_arn"] = function_arn

        @builtins.property
        def function_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Lambda function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-lambdaaction.html#cfn-iot-topicrule-lambdaaction-functionarn
            '''
            result = self._values.get("function_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.OpenSearchActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint": "endpoint",
            "id": "id",
            "index": "index",
            "role_arn": "roleArn",
            "type": "type",
        },
    )
    class OpenSearchActionProperty:
        def __init__(
            self,
            *,
            endpoint: builtins.str,
            id: builtins.str,
            index: builtins.str,
            role_arn: builtins.str,
            type: builtins.str,
        ) -> None:
            '''Describes an action that writes data to an Amazon OpenSearch Service domain.

            :param endpoint: The endpoint of your OpenSearch domain.
            :param id: The unique identifier for the document you are storing.
            :param index: The OpenSearch index where you want to store your data.
            :param role_arn: The IAM role ARN that has access to OpenSearch.
            :param type: The type of document you are storing.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                open_search_action_property = iot.CfnTopicRule.OpenSearchActionProperty(
                    endpoint="endpoint",
                    id="id",
                    index="index",
                    role_arn="roleArn",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.OpenSearchActionProperty.__init__)
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument index", value=index, expected_type=type_hints["index"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint": endpoint,
                "id": id,
                "index": index,
                "role_arn": role_arn,
                "type": type,
            }

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''The endpoint of your OpenSearch domain.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html#cfn-iot-topicrule-opensearchaction-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def id(self) -> builtins.str:
            '''The unique identifier for the document you are storing.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html#cfn-iot-topicrule-opensearchaction-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def index(self) -> builtins.str:
            '''The OpenSearch index where you want to store your data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html#cfn-iot-topicrule-opensearchaction-index
            '''
            result = self._values.get("index")
            assert result is not None, "Required property 'index' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The IAM role ARN that has access to OpenSearch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html#cfn-iot-topicrule-opensearchaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of document you are storing.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html#cfn-iot-topicrule-opensearchaction-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenSearchActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.PutAssetPropertyValueEntryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "property_values": "propertyValues",
            "asset_id": "assetId",
            "entry_id": "entryId",
            "property_alias": "propertyAlias",
            "property_id": "propertyId",
        },
    )
    class PutAssetPropertyValueEntryProperty:
        def __init__(
            self,
            *,
            property_values: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnTopicRule.AssetPropertyValueProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
            asset_id: typing.Optional[builtins.str] = None,
            entry_id: typing.Optional[builtins.str] = None,
            property_alias: typing.Optional[builtins.str] = None,
            property_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An asset property value entry containing the following information.

            :param property_values: A list of property values to insert that each contain timestamp, quality, and value (TQV) information.
            :param asset_id: The ID of the AWS IoT SiteWise asset. You must specify either a ``propertyAlias`` or both an ``aliasId`` and a ``propertyId`` . Accepts substitution templates.
            :param entry_id: Optional. A unique identifier for this entry that you can define to better track which message caused an error in case of failure. Accepts substitution templates. Defaults to a new UUID.
            :param property_alias: The name of the property alias associated with your asset property. You must specify either a ``propertyAlias`` or both an ``aliasId`` and a ``propertyId`` . Accepts substitution templates.
            :param property_id: The ID of the asset's property. You must specify either a ``propertyAlias`` or both an ``aliasId`` and a ``propertyId`` . Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                put_asset_property_value_entry_property = iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                    property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                        timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                            time_in_seconds="timeInSeconds",
                
                            # the properties below are optional
                            offset_in_nanos="offsetInNanos"
                        ),
                        value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                            boolean_value="booleanValue",
                            double_value="doubleValue",
                            integer_value="integerValue",
                            string_value="stringValue"
                        ),
                
                        # the properties below are optional
                        quality="quality"
                    )],
                
                    # the properties below are optional
                    asset_id="assetId",
                    entry_id="entryId",
                    property_alias="propertyAlias",
                    property_id="propertyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.PutAssetPropertyValueEntryProperty.__init__)
                check_type(argname="argument property_values", value=property_values, expected_type=type_hints["property_values"])
                check_type(argname="argument asset_id", value=asset_id, expected_type=type_hints["asset_id"])
                check_type(argname="argument entry_id", value=entry_id, expected_type=type_hints["entry_id"])
                check_type(argname="argument property_alias", value=property_alias, expected_type=type_hints["property_alias"])
                check_type(argname="argument property_id", value=property_id, expected_type=type_hints["property_id"])
            self._values: typing.Dict[str, typing.Any] = {
                "property_values": property_values,
            }
            if asset_id is not None:
                self._values["asset_id"] = asset_id
            if entry_id is not None:
                self._values["entry_id"] = entry_id
            if property_alias is not None:
                self._values["property_alias"] = property_alias
            if property_id is not None:
                self._values["property_id"] = property_id

        @builtins.property
        def property_values(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTopicRule.AssetPropertyValueProperty", _IResolvable_da3f097b]]]:
            '''A list of property values to insert that each contain timestamp, quality, and value (TQV) information.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html#cfn-iot-topicrule-putassetpropertyvalueentry-propertyvalues
            '''
            result = self._values.get("property_values")
            assert result is not None, "Required property 'property_values' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTopicRule.AssetPropertyValueProperty", _IResolvable_da3f097b]]], result)

        @builtins.property
        def asset_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the AWS IoT SiteWise asset.

            You must specify either a ``propertyAlias`` or both an ``aliasId`` and a ``propertyId`` . Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html#cfn-iot-topicrule-putassetpropertyvalueentry-assetid
            '''
            result = self._values.get("asset_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def entry_id(self) -> typing.Optional[builtins.str]:
            '''Optional.

            A unique identifier for this entry that you can define to better track which message caused an error in case of failure. Accepts substitution templates. Defaults to a new UUID.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html#cfn-iot-topicrule-putassetpropertyvalueentry-entryid
            '''
            result = self._values.get("entry_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_alias(self) -> typing.Optional[builtins.str]:
            '''The name of the property alias associated with your asset property.

            You must specify either a ``propertyAlias`` or both an ``aliasId`` and a ``propertyId`` . Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html#cfn-iot-topicrule-putassetpropertyvalueentry-propertyalias
            '''
            result = self._values.get("property_alias")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the asset's property.

            You must specify either a ``propertyAlias`` or both an ``aliasId`` and a ``propertyId`` . Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html#cfn-iot-topicrule-putassetpropertyvalueentry-propertyid
            '''
            result = self._values.get("property_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PutAssetPropertyValueEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.PutItemInputProperty",
        jsii_struct_bases=[],
        name_mapping={"table_name": "tableName"},
    )
    class PutItemInputProperty:
        def __init__(self, *, table_name: builtins.str) -> None:
            '''The input for the DynamoActionVS action that specifies the DynamoDB table to which the message data will be written.

            :param table_name: The table where the message data will be written.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putiteminput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                put_item_input_property = iot.CfnTopicRule.PutItemInputProperty(
                    table_name="tableName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.PutItemInputProperty.__init__)
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            self._values: typing.Dict[str, typing.Any] = {
                "table_name": table_name,
            }

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The table where the message data will be written.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putiteminput.html#cfn-iot-topicrule-putiteminput-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PutItemInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.RepublishActionProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn", "topic": "topic", "qos": "qos"},
    )
    class RepublishActionProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            topic: builtins.str,
            qos: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes an action to republish to another topic.

            :param role_arn: The ARN of the IAM role that grants access.
            :param topic: The name of the MQTT topic.
            :param qos: The Quality of Service (QoS) level to use when republishing messages. The default value is 0.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                republish_action_property = iot.CfnTopicRule.RepublishActionProperty(
                    role_arn="roleArn",
                    topic="topic",
                
                    # the properties below are optional
                    qos=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.RepublishActionProperty.__init__)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
                check_type(argname="argument qos", value=qos, expected_type=type_hints["qos"])
            self._values: typing.Dict[str, typing.Any] = {
                "role_arn": role_arn,
                "topic": topic,
            }
            if qos is not None:
                self._values["qos"] = qos

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that grants access.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishaction.html#cfn-iot-topicrule-republishaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def topic(self) -> builtins.str:
            '''The name of the MQTT topic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishaction.html#cfn-iot-topicrule-republishaction-topic
            '''
            result = self._values.get("topic")
            assert result is not None, "Required property 'topic' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def qos(self) -> typing.Optional[jsii.Number]:
            '''The Quality of Service (QoS) level to use when republishing messages.

            The default value is 0.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishaction.html#cfn-iot-topicrule-republishaction-qos
            '''
            result = self._values.get("qos")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RepublishActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.S3ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "key": "key",
            "role_arn": "roleArn",
            "canned_acl": "cannedAcl",
        },
    )
    class S3ActionProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            key: builtins.str,
            role_arn: builtins.str,
            canned_acl: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action to write data to an Amazon S3 bucket.

            :param bucket_name: The Amazon S3 bucket.
            :param key: The object key. For more information, see `Actions, resources, and condition keys for Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/dev/list_amazons3.html>`_ .
            :param role_arn: The ARN of the IAM role that grants access.
            :param canned_acl: The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see `S3 canned ACLs <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                s3_action_property = iot.CfnTopicRule.S3ActionProperty(
                    bucket_name="bucketName",
                    key="key",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    canned_acl="cannedAcl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.S3ActionProperty.__init__)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument canned_acl", value=canned_acl, expected_type=type_hints["canned_acl"])
            self._values: typing.Dict[str, typing.Any] = {
                "bucket_name": bucket_name,
                "key": key,
                "role_arn": role_arn,
            }
            if canned_acl is not None:
                self._values["canned_acl"] = canned_acl

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The Amazon S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html#cfn-iot-topicrule-s3action-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The object key.

            For more information, see `Actions, resources, and condition keys for Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/dev/list_amazons3.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html#cfn-iot-topicrule-s3action-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that grants access.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html#cfn-iot-topicrule-s3action-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def canned_acl(self) -> typing.Optional[builtins.str]:
            '''The Amazon S3 canned ACL that controls access to the object identified by the object key.

            For more information, see `S3 canned ACLs <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html#cfn-iot-topicrule-s3action-cannedacl
            '''
            result = self._values.get("canned_acl")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.SigV4AuthorizationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "service_name": "serviceName",
            "signing_region": "signingRegion",
        },
    )
    class SigV4AuthorizationProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            service_name: builtins.str,
            signing_region: builtins.str,
        ) -> None:
            '''For more information, see `Signature Version 4 signing process <https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>`_ .

            :param role_arn: The ARN of the signing role.
            :param service_name: The service name to use while signing with Sig V4.
            :param signing_region: The signing region.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sigv4authorization.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                sig_v4_authorization_property = iot.CfnTopicRule.SigV4AuthorizationProperty(
                    role_arn="roleArn",
                    service_name="serviceName",
                    signing_region="signingRegion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.SigV4AuthorizationProperty.__init__)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
                check_type(argname="argument signing_region", value=signing_region, expected_type=type_hints["signing_region"])
            self._values: typing.Dict[str, typing.Any] = {
                "role_arn": role_arn,
                "service_name": service_name,
                "signing_region": signing_region,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the signing role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sigv4authorization.html#cfn-iot-topicrule-sigv4authorization-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def service_name(self) -> builtins.str:
            '''The service name to use while signing with Sig V4.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sigv4authorization.html#cfn-iot-topicrule-sigv4authorization-servicename
            '''
            result = self._values.get("service_name")
            assert result is not None, "Required property 'service_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def signing_region(self) -> builtins.str:
            '''The signing region.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sigv4authorization.html#cfn-iot-topicrule-sigv4authorization-signingregion
            '''
            result = self._values.get("signing_region")
            assert result is not None, "Required property 'signing_region' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SigV4AuthorizationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.SnsActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "target_arn": "targetArn",
            "message_format": "messageFormat",
        },
    )
    class SnsActionProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            target_arn: builtins.str,
            message_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action to publish to an Amazon SNS topic.

            :param role_arn: The ARN of the IAM role that grants access.
            :param target_arn: The ARN of the SNS topic.
            :param message_format: (Optional) The message format of the message to publish. Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. For more information, see `Amazon SNS Message and JSON Formats <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`_ in the *Amazon Simple Notification Service Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-snsaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                sns_action_property = iot.CfnTopicRule.SnsActionProperty(
                    role_arn="roleArn",
                    target_arn="targetArn",
                
                    # the properties below are optional
                    message_format="messageFormat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.SnsActionProperty.__init__)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
                check_type(argname="argument message_format", value=message_format, expected_type=type_hints["message_format"])
            self._values: typing.Dict[str, typing.Any] = {
                "role_arn": role_arn,
                "target_arn": target_arn,
            }
            if message_format is not None:
                self._values["message_format"] = message_format

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that grants access.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-snsaction.html#cfn-iot-topicrule-snsaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_arn(self) -> builtins.str:
            '''The ARN of the SNS topic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-snsaction.html#cfn-iot-topicrule-snsaction-targetarn
            '''
            result = self._values.get("target_arn")
            assert result is not None, "Required property 'target_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def message_format(self) -> typing.Optional[builtins.str]:
            '''(Optional) The message format of the message to publish.

            Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. For more information, see `Amazon SNS Message and JSON Formats <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`_ in the *Amazon Simple Notification Service Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-snsaction.html#cfn-iot-topicrule-snsaction-messageformat
            '''
            result = self._values.get("message_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnsActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.SqsActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "queue_url": "queueUrl",
            "role_arn": "roleArn",
            "use_base64": "useBase64",
        },
    )
    class SqsActionProperty:
        def __init__(
            self,
            *,
            queue_url: builtins.str,
            role_arn: builtins.str,
            use_base64: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes an action to publish data to an Amazon SQS queue.

            :param queue_url: The URL of the Amazon SQS queue.
            :param role_arn: The ARN of the IAM role that grants access.
            :param use_base64: Specifies whether to use Base64 encoding.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sqsaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                sqs_action_property = iot.CfnTopicRule.SqsActionProperty(
                    queue_url="queueUrl",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    use_base64=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.SqsActionProperty.__init__)
                check_type(argname="argument queue_url", value=queue_url, expected_type=type_hints["queue_url"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument use_base64", value=use_base64, expected_type=type_hints["use_base64"])
            self._values: typing.Dict[str, typing.Any] = {
                "queue_url": queue_url,
                "role_arn": role_arn,
            }
            if use_base64 is not None:
                self._values["use_base64"] = use_base64

        @builtins.property
        def queue_url(self) -> builtins.str:
            '''The URL of the Amazon SQS queue.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sqsaction.html#cfn-iot-topicrule-sqsaction-queueurl
            '''
            result = self._values.get("queue_url")
            assert result is not None, "Required property 'queue_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that grants access.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sqsaction.html#cfn-iot-topicrule-sqsaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def use_base64(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether to use Base64 encoding.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sqsaction.html#cfn-iot-topicrule-sqsaction-usebase64
            '''
            result = self._values.get("use_base64")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqsActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.StepFunctionsActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "state_machine_name": "stateMachineName",
            "execution_name_prefix": "executionNamePrefix",
        },
    )
    class StepFunctionsActionProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            state_machine_name: builtins.str,
            execution_name_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Starts execution of a Step Functions state machine.

            :param role_arn: The ARN of the role that grants IoT permission to start execution of a state machine ("Action":"states:StartExecution").
            :param state_machine_name: The name of the Step Functions state machine whose execution will be started.
            :param execution_name_prefix: (Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-stepfunctionsaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                step_functions_action_property = iot.CfnTopicRule.StepFunctionsActionProperty(
                    role_arn="roleArn",
                    state_machine_name="stateMachineName",
                
                    # the properties below are optional
                    execution_name_prefix="executionNamePrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.StepFunctionsActionProperty.__init__)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument state_machine_name", value=state_machine_name, expected_type=type_hints["state_machine_name"])
                check_type(argname="argument execution_name_prefix", value=execution_name_prefix, expected_type=type_hints["execution_name_prefix"])
            self._values: typing.Dict[str, typing.Any] = {
                "role_arn": role_arn,
                "state_machine_name": state_machine_name,
            }
            if execution_name_prefix is not None:
                self._values["execution_name_prefix"] = execution_name_prefix

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that grants IoT permission to start execution of a state machine ("Action":"states:StartExecution").

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-stepfunctionsaction.html#cfn-iot-topicrule-stepfunctionsaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def state_machine_name(self) -> builtins.str:
            '''The name of the Step Functions state machine whose execution will be started.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-stepfunctionsaction.html#cfn-iot-topicrule-stepfunctionsaction-statemachinename
            '''
            result = self._values.get("state_machine_name")
            assert result is not None, "Required property 'state_machine_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def execution_name_prefix(self) -> typing.Optional[builtins.str]:
            '''(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID.

            Step Functions automatically creates a unique name for each state machine execution if one is not provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-stepfunctionsaction.html#cfn-iot-topicrule-stepfunctionsaction-executionnameprefix
            '''
            result = self._values.get("execution_name_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StepFunctionsActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.TimestreamActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_name": "databaseName",
            "dimensions": "dimensions",
            "role_arn": "roleArn",
            "table_name": "tableName",
            "batch_mode": "batchMode",
            "timestamp": "timestamp",
        },
    )
    class TimestreamActionProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            dimensions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnTopicRule.TimestreamDimensionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
            role_arn: builtins.str,
            table_name: builtins.str,
            batch_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            timestamp: typing.Optional[typing.Union[typing.Union["CfnTopicRule.TimestreamTimestampProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes an action that writes records into an Amazon Timestream table.

            :param database_name: The name of an Amazon Timestream database that has the table to write records into.
            :param dimensions: Metadata attributes of the time series that are written in each measure record.
            :param role_arn: The Amazon Resource Name (ARN) of the role that grants AWS IoT permission to write to the Timestream database table.
            :param table_name: The table where the message data will be written.
            :param batch_mode: Whether to process the action as a batch.
            :param timestamp: The value to use for the entry's timestamp. If blank, the time that the entry was processed is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                timestream_action_property = iot.CfnTopicRule.TimestreamActionProperty(
                    database_name="databaseName",
                    dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                        name="name",
                        value="value"
                    )],
                    role_arn="roleArn",
                    table_name="tableName",
                
                    # the properties below are optional
                    batch_mode=False,
                    timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                        unit="unit",
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.TimestreamActionProperty.__init__)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument batch_mode", value=batch_mode, expected_type=type_hints["batch_mode"])
                check_type(argname="argument timestamp", value=timestamp, expected_type=type_hints["timestamp"])
            self._values: typing.Dict[str, typing.Any] = {
                "database_name": database_name,
                "dimensions": dimensions,
                "role_arn": role_arn,
                "table_name": table_name,
            }
            if batch_mode is not None:
                self._values["batch_mode"] = batch_mode
            if timestamp is not None:
                self._values["timestamp"] = timestamp

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of an Amazon Timestream database that has the table to write records into.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTopicRule.TimestreamDimensionProperty", _IResolvable_da3f097b]]]:
            '''Metadata attributes of the time series that are written in each measure record.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-dimensions
            '''
            result = self._values.get("dimensions")
            assert result is not None, "Required property 'dimensions' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTopicRule.TimestreamDimensionProperty", _IResolvable_da3f097b]]], result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the role that grants AWS IoT permission to write to the Timestream database table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The table where the message data will be written.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_mode(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether to process the action as a batch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-batchmode
            '''
            result = self._values.get("batch_mode")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def timestamp(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.TimestreamTimestampProperty", _IResolvable_da3f097b]]:
            '''The value to use for the entry's timestamp.

            If blank, the time that the entry was processed is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-timestamp
            '''
            result = self._values.get("timestamp")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.TimestreamTimestampProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimestreamActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.TimestreamDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class TimestreamDimensionProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''Metadata attributes of the time series that are written in each measure record.

            :param name: The metadata dimension name. This is the name of the column in the Amazon Timestream database table record.
            :param value: The value to write in this column of the database record.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamdimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                timestream_dimension_property = iot.CfnTopicRule.TimestreamDimensionProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.TimestreamDimensionProperty.__init__)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The metadata dimension name.

            This is the name of the column in the Amazon Timestream database table record.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamdimension.html#cfn-iot-topicrule-timestreamdimension-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value to write in this column of the database record.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamdimension.html#cfn-iot-topicrule-timestreamdimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimestreamDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.TimestreamTimestampProperty",
        jsii_struct_bases=[],
        name_mapping={"unit": "unit", "value": "value"},
    )
    class TimestreamTimestampProperty:
        def __init__(self, *, unit: builtins.str, value: builtins.str) -> None:
            '''The value to use for the entry's timestamp.

            If blank, the time that the entry was processed is used.

            :param unit: The precision of the timestamp value that results from the expression described in ``value`` .
            :param value: An expression that returns a long epoch time value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamtimestamp.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                timestream_timestamp_property = iot.CfnTopicRule.TimestreamTimestampProperty(
                    unit="unit",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.TimestreamTimestampProperty.__init__)
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[str, typing.Any] = {
                "unit": unit,
                "value": value,
            }

        @builtins.property
        def unit(self) -> builtins.str:
            '''The precision of the timestamp value that results from the expression described in ``value`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamtimestamp.html#cfn-iot-topicrule-timestreamtimestamp-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''An expression that returns a long epoch time value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamtimestamp.html#cfn-iot-topicrule-timestreamtimestamp-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimestreamTimestampProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRule.TopicRulePayloadProperty",
        jsii_struct_bases=[],
        name_mapping={
            "actions": "actions",
            "sql": "sql",
            "aws_iot_sql_version": "awsIotSqlVersion",
            "description": "description",
            "error_action": "errorAction",
            "rule_disabled": "ruleDisabled",
        },
    )
    class TopicRulePayloadProperty:
        def __init__(
            self,
            *,
            actions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnTopicRule.ActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
            sql: builtins.str,
            aws_iot_sql_version: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            error_action: typing.Optional[typing.Union[typing.Union["CfnTopicRule.ActionProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            rule_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes a rule.

            :param actions: The actions associated with the rule.
            :param sql: The SQL statement used to query the topic. For more information, see `AWS IoT SQL Reference <https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html>`_ in the *AWS IoT Developer Guide* .
            :param aws_iot_sql_version: The version of the SQL rules engine to use when evaluating the rule. The default value is 2015-10-08.
            :param description: The description of the rule.
            :param error_action: The action to take when an error occurs.
            :param rule_disabled: Specifies whether the rule is disabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                topic_rule_payload_property = iot.CfnTopicRule.TopicRulePayloadProperty(
                    actions=[iot.CfnTopicRule.ActionProperty(
                        cloudwatch_alarm=iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                            alarm_name="alarmName",
                            role_arn="roleArn",
                            state_reason="stateReason",
                            state_value="stateValue"
                        ),
                        cloudwatch_logs=iot.CfnTopicRule.CloudwatchLogsActionProperty(
                            log_group_name="logGroupName",
                            role_arn="roleArn"
                        ),
                        cloudwatch_metric=iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name="metricName",
                            metric_namespace="metricNamespace",
                            metric_unit="metricUnit",
                            metric_value="metricValue",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            metric_timestamp="metricTimestamp"
                        ),
                        dynamo_db=iot.CfnTopicRule.DynamoDBActionProperty(
                            hash_key_field="hashKeyField",
                            hash_key_value="hashKeyValue",
                            role_arn="roleArn",
                            table_name="tableName",
                
                            # the properties below are optional
                            hash_key_type="hashKeyType",
                            payload_field="payloadField",
                            range_key_field="rangeKeyField",
                            range_key_type="rangeKeyType",
                            range_key_value="rangeKeyValue"
                        ),
                        dynamo_dBv2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                            put_item=iot.CfnTopicRule.PutItemInputProperty(
                                table_name="tableName"
                            ),
                            role_arn="roleArn"
                        ),
                        elasticsearch=iot.CfnTopicRule.ElasticsearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        firehose=iot.CfnTopicRule.FirehoseActionProperty(
                            delivery_stream_name="deliveryStreamName",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            batch_mode=False,
                            separator="separator"
                        ),
                        http=iot.CfnTopicRule.HttpActionProperty(
                            url="url",
                
                            # the properties below are optional
                            auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                                sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                                    role_arn="roleArn",
                                    service_name="serviceName",
                                    signing_region="signingRegion"
                                )
                            ),
                            confirmation_url="confirmationUrl",
                            headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                                key="key",
                                value="value"
                            )]
                        ),
                        iot_analytics=iot.CfnTopicRule.IotAnalyticsActionProperty(
                            channel_name="channelName",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            batch_mode=False
                        ),
                        iot_events=iot.CfnTopicRule.IotEventsActionProperty(
                            input_name="inputName",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            batch_mode=False,
                            message_id="messageId"
                        ),
                        iot_site_wise=iot.CfnTopicRule.IotSiteWiseActionProperty(
                            put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                                property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                                    timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                        time_in_seconds="timeInSeconds",
                
                                        # the properties below are optional
                                        offset_in_nanos="offsetInNanos"
                                    ),
                                    value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                        boolean_value="booleanValue",
                                        double_value="doubleValue",
                                        integer_value="integerValue",
                                        string_value="stringValue"
                                    ),
                
                                    # the properties below are optional
                                    quality="quality"
                                )],
                
                                # the properties below are optional
                                asset_id="assetId",
                                entry_id="entryId",
                                property_alias="propertyAlias",
                                property_id="propertyId"
                            )],
                            role_arn="roleArn"
                        ),
                        kafka=iot.CfnTopicRule.KafkaActionProperty(
                            client_properties={
                                "client_properties_key": "clientProperties"
                            },
                            destination_arn="destinationArn",
                            topic="topic",
                
                            # the properties below are optional
                            key="key",
                            partition="partition"
                        ),
                        kinesis=iot.CfnTopicRule.KinesisActionProperty(
                            role_arn="roleArn",
                            stream_name="streamName",
                
                            # the properties below are optional
                            partition_key="partitionKey"
                        ),
                        lambda_=iot.CfnTopicRule.LambdaActionProperty(
                            function_arn="functionArn"
                        ),
                        open_search=iot.CfnTopicRule.OpenSearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        republish=iot.CfnTopicRule.RepublishActionProperty(
                            role_arn="roleArn",
                            topic="topic",
                
                            # the properties below are optional
                            qos=123
                        ),
                        s3=iot.CfnTopicRule.S3ActionProperty(
                            bucket_name="bucketName",
                            key="key",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            canned_acl="cannedAcl"
                        ),
                        sns=iot.CfnTopicRule.SnsActionProperty(
                            role_arn="roleArn",
                            target_arn="targetArn",
                
                            # the properties below are optional
                            message_format="messageFormat"
                        ),
                        sqs=iot.CfnTopicRule.SqsActionProperty(
                            queue_url="queueUrl",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            use_base64=False
                        ),
                        step_functions=iot.CfnTopicRule.StepFunctionsActionProperty(
                            role_arn="roleArn",
                            state_machine_name="stateMachineName",
                
                            # the properties below are optional
                            execution_name_prefix="executionNamePrefix"
                        ),
                        timestream=iot.CfnTopicRule.TimestreamActionProperty(
                            database_name="databaseName",
                            dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                                name="name",
                                value="value"
                            )],
                            role_arn="roleArn",
                            table_name="tableName",
                
                            # the properties below are optional
                            batch_mode=False,
                            timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                                unit="unit",
                                value="value"
                            )
                        )
                    )],
                    sql="sql",
                
                    # the properties below are optional
                    aws_iot_sql_version="awsIotSqlVersion",
                    description="description",
                    error_action=iot.CfnTopicRule.ActionProperty(
                        cloudwatch_alarm=iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                            alarm_name="alarmName",
                            role_arn="roleArn",
                            state_reason="stateReason",
                            state_value="stateValue"
                        ),
                        cloudwatch_logs=iot.CfnTopicRule.CloudwatchLogsActionProperty(
                            log_group_name="logGroupName",
                            role_arn="roleArn"
                        ),
                        cloudwatch_metric=iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name="metricName",
                            metric_namespace="metricNamespace",
                            metric_unit="metricUnit",
                            metric_value="metricValue",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            metric_timestamp="metricTimestamp"
                        ),
                        dynamo_db=iot.CfnTopicRule.DynamoDBActionProperty(
                            hash_key_field="hashKeyField",
                            hash_key_value="hashKeyValue",
                            role_arn="roleArn",
                            table_name="tableName",
                
                            # the properties below are optional
                            hash_key_type="hashKeyType",
                            payload_field="payloadField",
                            range_key_field="rangeKeyField",
                            range_key_type="rangeKeyType",
                            range_key_value="rangeKeyValue"
                        ),
                        dynamo_dBv2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                            put_item=iot.CfnTopicRule.PutItemInputProperty(
                                table_name="tableName"
                            ),
                            role_arn="roleArn"
                        ),
                        elasticsearch=iot.CfnTopicRule.ElasticsearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        firehose=iot.CfnTopicRule.FirehoseActionProperty(
                            delivery_stream_name="deliveryStreamName",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            batch_mode=False,
                            separator="separator"
                        ),
                        http=iot.CfnTopicRule.HttpActionProperty(
                            url="url",
                
                            # the properties below are optional
                            auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                                sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                                    role_arn="roleArn",
                                    service_name="serviceName",
                                    signing_region="signingRegion"
                                )
                            ),
                            confirmation_url="confirmationUrl",
                            headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                                key="key",
                                value="value"
                            )]
                        ),
                        iot_analytics=iot.CfnTopicRule.IotAnalyticsActionProperty(
                            channel_name="channelName",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            batch_mode=False
                        ),
                        iot_events=iot.CfnTopicRule.IotEventsActionProperty(
                            input_name="inputName",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            batch_mode=False,
                            message_id="messageId"
                        ),
                        iot_site_wise=iot.CfnTopicRule.IotSiteWiseActionProperty(
                            put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                                property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                                    timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                        time_in_seconds="timeInSeconds",
                
                                        # the properties below are optional
                                        offset_in_nanos="offsetInNanos"
                                    ),
                                    value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                        boolean_value="booleanValue",
                                        double_value="doubleValue",
                                        integer_value="integerValue",
                                        string_value="stringValue"
                                    ),
                
                                    # the properties below are optional
                                    quality="quality"
                                )],
                
                                # the properties below are optional
                                asset_id="assetId",
                                entry_id="entryId",
                                property_alias="propertyAlias",
                                property_id="propertyId"
                            )],
                            role_arn="roleArn"
                        ),
                        kafka=iot.CfnTopicRule.KafkaActionProperty(
                            client_properties={
                                "client_properties_key": "clientProperties"
                            },
                            destination_arn="destinationArn",
                            topic="topic",
                
                            # the properties below are optional
                            key="key",
                            partition="partition"
                        ),
                        kinesis=iot.CfnTopicRule.KinesisActionProperty(
                            role_arn="roleArn",
                            stream_name="streamName",
                
                            # the properties below are optional
                            partition_key="partitionKey"
                        ),
                        lambda_=iot.CfnTopicRule.LambdaActionProperty(
                            function_arn="functionArn"
                        ),
                        open_search=iot.CfnTopicRule.OpenSearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        republish=iot.CfnTopicRule.RepublishActionProperty(
                            role_arn="roleArn",
                            topic="topic",
                
                            # the properties below are optional
                            qos=123
                        ),
                        s3=iot.CfnTopicRule.S3ActionProperty(
                            bucket_name="bucketName",
                            key="key",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            canned_acl="cannedAcl"
                        ),
                        sns=iot.CfnTopicRule.SnsActionProperty(
                            role_arn="roleArn",
                            target_arn="targetArn",
                
                            # the properties below are optional
                            message_format="messageFormat"
                        ),
                        sqs=iot.CfnTopicRule.SqsActionProperty(
                            queue_url="queueUrl",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            use_base64=False
                        ),
                        step_functions=iot.CfnTopicRule.StepFunctionsActionProperty(
                            role_arn="roleArn",
                            state_machine_name="stateMachineName",
                
                            # the properties below are optional
                            execution_name_prefix="executionNamePrefix"
                        ),
                        timestream=iot.CfnTopicRule.TimestreamActionProperty(
                            database_name="databaseName",
                            dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                                name="name",
                                value="value"
                            )],
                            role_arn="roleArn",
                            table_name="tableName",
                
                            # the properties below are optional
                            batch_mode=False,
                            timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                                unit="unit",
                                value="value"
                            )
                        )
                    ),
                    rule_disabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRule.TopicRulePayloadProperty.__init__)
                check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
                check_type(argname="argument sql", value=sql, expected_type=type_hints["sql"])
                check_type(argname="argument aws_iot_sql_version", value=aws_iot_sql_version, expected_type=type_hints["aws_iot_sql_version"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument error_action", value=error_action, expected_type=type_hints["error_action"])
                check_type(argname="argument rule_disabled", value=rule_disabled, expected_type=type_hints["rule_disabled"])
            self._values: typing.Dict[str, typing.Any] = {
                "actions": actions,
                "sql": sql,
            }
            if aws_iot_sql_version is not None:
                self._values["aws_iot_sql_version"] = aws_iot_sql_version
            if description is not None:
                self._values["description"] = description
            if error_action is not None:
                self._values["error_action"] = error_action
            if rule_disabled is not None:
                self._values["rule_disabled"] = rule_disabled

        @builtins.property
        def actions(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTopicRule.ActionProperty", _IResolvable_da3f097b]]]:
            '''The actions associated with the rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-actions
            '''
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnTopicRule.ActionProperty", _IResolvable_da3f097b]]], result)

        @builtins.property
        def sql(self) -> builtins.str:
            '''The SQL statement used to query the topic.

            For more information, see `AWS IoT SQL Reference <https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html>`_ in the *AWS IoT Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-sql
            '''
            result = self._values.get("sql")
            assert result is not None, "Required property 'sql' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def aws_iot_sql_version(self) -> typing.Optional[builtins.str]:
            '''The version of the SQL rules engine to use when evaluating the rule.

            The default value is 2015-10-08.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-awsiotsqlversion
            '''
            result = self._values.get("aws_iot_sql_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def error_action(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.ActionProperty", _IResolvable_da3f097b]]:
            '''The action to take when an error occurs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-erroraction
            '''
            result = self._values.get("error_action")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.ActionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def rule_disabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the rule is disabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-ruledisabled
            '''
            result = self._values.get("rule_disabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TopicRulePayloadProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnTopicRuleDestination(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iot.CfnTopicRuleDestination",
):
    '''A CloudFormation ``AWS::IoT::TopicRuleDestination``.

    A topic rule destination.

    :cloudformationResource: AWS::IoT::TopicRuleDestination
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iot as iot
        
        cfn_topic_rule_destination = iot.CfnTopicRuleDestination(self, "MyCfnTopicRuleDestination",
            http_url_properties=iot.CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty(
                confirmation_url="confirmationUrl"
            ),
            status="status",
            vpc_properties=iot.CfnTopicRuleDestination.VpcDestinationPropertiesProperty(
                role_arn="roleArn",
                security_groups=["securityGroups"],
                subnet_ids=["subnetIds"],
                vpc_id="vpcId"
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        http_url_properties: typing.Optional[typing.Union[typing.Union["CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        status: typing.Optional[builtins.str] = None,
        vpc_properties: typing.Optional[typing.Union[typing.Union["CfnTopicRuleDestination.VpcDestinationPropertiesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::TopicRuleDestination``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param http_url_properties: Properties of the HTTP URL.
        :param status: - **IN_PROGRESS** - A topic rule destination was created but has not been confirmed. You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint. - **ENABLED** - Confirmation was completed, and traffic to this destination is allowed. You can set status to ``DISABLED`` by calling ``UpdateTopicRuleDestination`` . - **DISABLED** - Confirmation was completed, and traffic to this destination is not allowed. You can set status to ``ENABLED`` by calling ``UpdateTopicRuleDestination`` . - **ERROR** - Confirmation could not be completed; for example, if the confirmation timed out. You can call ``GetTopicRuleDestination`` for details about the error. You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint.
        :param vpc_properties: Properties of the virtual private cloud (VPC) connection.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTopicRuleDestination.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTopicRuleDestinationProps(
            http_url_properties=http_url_properties,
            status=status,
            vpc_properties=vpc_properties,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTopicRuleDestination.inspect)
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
            type_hints = typing.get_type_hints(CfnTopicRuleDestination._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The topic rule destination URL.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReason")
    def attr_status_reason(self) -> builtins.str:
        '''Additional details or reason why the topic rule destination is in the current status.

        :cloudformationAttribute: StatusReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusReason"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="httpUrlProperties")
    def http_url_properties(
        self,
    ) -> typing.Optional[typing.Union["CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty", _IResolvable_da3f097b]]:
        '''Properties of the HTTP URL.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-httpurlproperties
        '''
        return typing.cast(typing.Optional[typing.Union["CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty", _IResolvable_da3f097b]], jsii.get(self, "httpUrlProperties"))

    @http_url_properties.setter
    def http_url_properties(
        self,
        value: typing.Optional[typing.Union["CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTopicRuleDestination, "http_url_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpUrlProperties", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''- **IN_PROGRESS** - A topic rule destination was created but has not been confirmed.

        You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint.

        - **ENABLED** - Confirmation was completed, and traffic to this destination is allowed. You can set status to ``DISABLED`` by calling ``UpdateTopicRuleDestination`` .
        - **DISABLED** - Confirmation was completed, and traffic to this destination is not allowed. You can set status to ``ENABLED`` by calling ``UpdateTopicRuleDestination`` .
        - **ERROR** - Confirmation could not be completed; for example, if the confirmation timed out. You can call ``GetTopicRuleDestination`` for details about the error. You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTopicRuleDestination, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="vpcProperties")
    def vpc_properties(
        self,
    ) -> typing.Optional[typing.Union["CfnTopicRuleDestination.VpcDestinationPropertiesProperty", _IResolvable_da3f097b]]:
        '''Properties of the virtual private cloud (VPC) connection.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-vpcproperties
        '''
        return typing.cast(typing.Optional[typing.Union["CfnTopicRuleDestination.VpcDestinationPropertiesProperty", _IResolvable_da3f097b]], jsii.get(self, "vpcProperties"))

    @vpc_properties.setter
    def vpc_properties(
        self,
        value: typing.Optional[typing.Union["CfnTopicRuleDestination.VpcDestinationPropertiesProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnTopicRuleDestination, "vpc_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcProperties", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty",
        jsii_struct_bases=[],
        name_mapping={"confirmation_url": "confirmationUrl"},
    )
    class HttpUrlDestinationSummaryProperty:
        def __init__(
            self,
            *,
            confirmation_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''HTTP URL destination properties.

            :param confirmation_url: The URL used to confirm the HTTP topic rule destination URL.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-httpurldestinationsummary.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                http_url_destination_summary_property = iot.CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty(
                    confirmation_url="confirmationUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty.__init__)
                check_type(argname="argument confirmation_url", value=confirmation_url, expected_type=type_hints["confirmation_url"])
            self._values: typing.Dict[str, typing.Any] = {}
            if confirmation_url is not None:
                self._values["confirmation_url"] = confirmation_url

        @builtins.property
        def confirmation_url(self) -> typing.Optional[builtins.str]:
            '''The URL used to confirm the HTTP topic rule destination URL.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-httpurldestinationsummary.html#cfn-iot-topicruledestination-httpurldestinationsummary-confirmationurl
            '''
            result = self._values.get("confirmation_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpUrlDestinationSummaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iot.CfnTopicRuleDestination.VpcDestinationPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "security_groups": "securityGroups",
            "subnet_ids": "subnetIds",
            "vpc_id": "vpcId",
        },
    )
    class VpcDestinationPropertiesProperty:
        def __init__(
            self,
            *,
            role_arn: typing.Optional[builtins.str] = None,
            security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            vpc_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The properties of a virtual private cloud (VPC) destination.

            :param role_arn: The ARN of a role that has permission to create and attach to elastic network interfaces (ENIs).
            :param security_groups: The security groups of the VPC destination.
            :param subnet_ids: The subnet IDs of the VPC destination.
            :param vpc_id: The ID of the VPC.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iot as iot
                
                vpc_destination_properties_property = iot.CfnTopicRuleDestination.VpcDestinationPropertiesProperty(
                    role_arn="roleArn",
                    security_groups=["securityGroups"],
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnTopicRuleDestination.VpcDestinationPropertiesProperty.__init__)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[str, typing.Any] = {}
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if security_groups is not None:
                self._values["security_groups"] = security_groups
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids
            if vpc_id is not None:
                self._values["vpc_id"] = vpc_id

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of a role that has permission to create and attach to elastic network interfaces (ENIs).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html#cfn-iot-topicruledestination-vpcdestinationproperties-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The security groups of the VPC destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html#cfn-iot-topicruledestination-vpcdestinationproperties-securitygroups
            '''
            result = self._values.get("security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The subnet IDs of the VPC destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html#cfn-iot-topicruledestination-vpcdestinationproperties-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def vpc_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the VPC.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html#cfn-iot-topicruledestination-vpcdestinationproperties-vpcid
            '''
            result = self._values.get("vpc_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcDestinationPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnTopicRuleDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "http_url_properties": "httpUrlProperties",
        "status": "status",
        "vpc_properties": "vpcProperties",
    },
)
class CfnTopicRuleDestinationProps:
    def __init__(
        self,
        *,
        http_url_properties: typing.Optional[typing.Union[typing.Union[CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        status: typing.Optional[builtins.str] = None,
        vpc_properties: typing.Optional[typing.Union[typing.Union[CfnTopicRuleDestination.VpcDestinationPropertiesProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTopicRuleDestination``.

        :param http_url_properties: Properties of the HTTP URL.
        :param status: - **IN_PROGRESS** - A topic rule destination was created but has not been confirmed. You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint. - **ENABLED** - Confirmation was completed, and traffic to this destination is allowed. You can set status to ``DISABLED`` by calling ``UpdateTopicRuleDestination`` . - **DISABLED** - Confirmation was completed, and traffic to this destination is not allowed. You can set status to ``ENABLED`` by calling ``UpdateTopicRuleDestination`` . - **ERROR** - Confirmation could not be completed; for example, if the confirmation timed out. You can call ``GetTopicRuleDestination`` for details about the error. You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint.
        :param vpc_properties: Properties of the virtual private cloud (VPC) connection.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_topic_rule_destination_props = iot.CfnTopicRuleDestinationProps(
                http_url_properties=iot.CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty(
                    confirmation_url="confirmationUrl"
                ),
                status="status",
                vpc_properties=iot.CfnTopicRuleDestination.VpcDestinationPropertiesProperty(
                    role_arn="roleArn",
                    security_groups=["securityGroups"],
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTopicRuleDestinationProps.__init__)
            check_type(argname="argument http_url_properties", value=http_url_properties, expected_type=type_hints["http_url_properties"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument vpc_properties", value=vpc_properties, expected_type=type_hints["vpc_properties"])
        self._values: typing.Dict[str, typing.Any] = {}
        if http_url_properties is not None:
            self._values["http_url_properties"] = http_url_properties
        if status is not None:
            self._values["status"] = status
        if vpc_properties is not None:
            self._values["vpc_properties"] = vpc_properties

    @builtins.property
    def http_url_properties(
        self,
    ) -> typing.Optional[typing.Union[CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty, _IResolvable_da3f097b]]:
        '''Properties of the HTTP URL.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-httpurlproperties
        '''
        result = self._values.get("http_url_properties")
        return typing.cast(typing.Optional[typing.Union[CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''- **IN_PROGRESS** - A topic rule destination was created but has not been confirmed.

        You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint.

        - **ENABLED** - Confirmation was completed, and traffic to this destination is allowed. You can set status to ``DISABLED`` by calling ``UpdateTopicRuleDestination`` .
        - **DISABLED** - Confirmation was completed, and traffic to this destination is not allowed. You can set status to ``ENABLED`` by calling ``UpdateTopicRuleDestination`` .
        - **ERROR** - Confirmation could not be completed; for example, if the confirmation timed out. You can call ``GetTopicRuleDestination`` for details about the error. You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_properties(
        self,
    ) -> typing.Optional[typing.Union[CfnTopicRuleDestination.VpcDestinationPropertiesProperty, _IResolvable_da3f097b]]:
        '''Properties of the virtual private cloud (VPC) connection.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-vpcproperties
        '''
        result = self._values.get("vpc_properties")
        return typing.cast(typing.Optional[typing.Union[CfnTopicRuleDestination.VpcDestinationPropertiesProperty, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTopicRuleDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iot.CfnTopicRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "topic_rule_payload": "topicRulePayload",
        "rule_name": "ruleName",
        "tags": "tags",
    },
)
class CfnTopicRuleProps:
    def __init__(
        self,
        *,
        topic_rule_payload: typing.Union[typing.Union[CfnTopicRule.TopicRulePayloadProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
        rule_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTopicRule``.

        :param topic_rule_payload: The rule payload.
        :param rule_name: The name of the rule.
        :param tags: Metadata which can be used to manage the topic rule. .. epigraph:: For URI Request parameters use format: ...key1=value1&key2=value2... For the CLI command-line parameter use format: --tags "key1=value1&key2=value2..." For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iot as iot
            
            cfn_topic_rule_props = iot.CfnTopicRuleProps(
                topic_rule_payload=iot.CfnTopicRule.TopicRulePayloadProperty(
                    actions=[iot.CfnTopicRule.ActionProperty(
                        cloudwatch_alarm=iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                            alarm_name="alarmName",
                            role_arn="roleArn",
                            state_reason="stateReason",
                            state_value="stateValue"
                        ),
                        cloudwatch_logs=iot.CfnTopicRule.CloudwatchLogsActionProperty(
                            log_group_name="logGroupName",
                            role_arn="roleArn"
                        ),
                        cloudwatch_metric=iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name="metricName",
                            metric_namespace="metricNamespace",
                            metric_unit="metricUnit",
                            metric_value="metricValue",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            metric_timestamp="metricTimestamp"
                        ),
                        dynamo_db=iot.CfnTopicRule.DynamoDBActionProperty(
                            hash_key_field="hashKeyField",
                            hash_key_value="hashKeyValue",
                            role_arn="roleArn",
                            table_name="tableName",
            
                            # the properties below are optional
                            hash_key_type="hashKeyType",
                            payload_field="payloadField",
                            range_key_field="rangeKeyField",
                            range_key_type="rangeKeyType",
                            range_key_value="rangeKeyValue"
                        ),
                        dynamo_dBv2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                            put_item=iot.CfnTopicRule.PutItemInputProperty(
                                table_name="tableName"
                            ),
                            role_arn="roleArn"
                        ),
                        elasticsearch=iot.CfnTopicRule.ElasticsearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        firehose=iot.CfnTopicRule.FirehoseActionProperty(
                            delivery_stream_name="deliveryStreamName",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            batch_mode=False,
                            separator="separator"
                        ),
                        http=iot.CfnTopicRule.HttpActionProperty(
                            url="url",
            
                            # the properties below are optional
                            auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                                sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                                    role_arn="roleArn",
                                    service_name="serviceName",
                                    signing_region="signingRegion"
                                )
                            ),
                            confirmation_url="confirmationUrl",
                            headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                                key="key",
                                value="value"
                            )]
                        ),
                        iot_analytics=iot.CfnTopicRule.IotAnalyticsActionProperty(
                            channel_name="channelName",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            batch_mode=False
                        ),
                        iot_events=iot.CfnTopicRule.IotEventsActionProperty(
                            input_name="inputName",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            batch_mode=False,
                            message_id="messageId"
                        ),
                        iot_site_wise=iot.CfnTopicRule.IotSiteWiseActionProperty(
                            put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                                property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                                    timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                        time_in_seconds="timeInSeconds",
            
                                        # the properties below are optional
                                        offset_in_nanos="offsetInNanos"
                                    ),
                                    value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                        boolean_value="booleanValue",
                                        double_value="doubleValue",
                                        integer_value="integerValue",
                                        string_value="stringValue"
                                    ),
            
                                    # the properties below are optional
                                    quality="quality"
                                )],
            
                                # the properties below are optional
                                asset_id="assetId",
                                entry_id="entryId",
                                property_alias="propertyAlias",
                                property_id="propertyId"
                            )],
                            role_arn="roleArn"
                        ),
                        kafka=iot.CfnTopicRule.KafkaActionProperty(
                            client_properties={
                                "client_properties_key": "clientProperties"
                            },
                            destination_arn="destinationArn",
                            topic="topic",
            
                            # the properties below are optional
                            key="key",
                            partition="partition"
                        ),
                        kinesis=iot.CfnTopicRule.KinesisActionProperty(
                            role_arn="roleArn",
                            stream_name="streamName",
            
                            # the properties below are optional
                            partition_key="partitionKey"
                        ),
                        lambda_=iot.CfnTopicRule.LambdaActionProperty(
                            function_arn="functionArn"
                        ),
                        open_search=iot.CfnTopicRule.OpenSearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        republish=iot.CfnTopicRule.RepublishActionProperty(
                            role_arn="roleArn",
                            topic="topic",
            
                            # the properties below are optional
                            qos=123
                        ),
                        s3=iot.CfnTopicRule.S3ActionProperty(
                            bucket_name="bucketName",
                            key="key",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            canned_acl="cannedAcl"
                        ),
                        sns=iot.CfnTopicRule.SnsActionProperty(
                            role_arn="roleArn",
                            target_arn="targetArn",
            
                            # the properties below are optional
                            message_format="messageFormat"
                        ),
                        sqs=iot.CfnTopicRule.SqsActionProperty(
                            queue_url="queueUrl",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            use_base64=False
                        ),
                        step_functions=iot.CfnTopicRule.StepFunctionsActionProperty(
                            role_arn="roleArn",
                            state_machine_name="stateMachineName",
            
                            # the properties below are optional
                            execution_name_prefix="executionNamePrefix"
                        ),
                        timestream=iot.CfnTopicRule.TimestreamActionProperty(
                            database_name="databaseName",
                            dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                                name="name",
                                value="value"
                            )],
                            role_arn="roleArn",
                            table_name="tableName",
            
                            # the properties below are optional
                            batch_mode=False,
                            timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                                unit="unit",
                                value="value"
                            )
                        )
                    )],
                    sql="sql",
            
                    # the properties below are optional
                    aws_iot_sql_version="awsIotSqlVersion",
                    description="description",
                    error_action=iot.CfnTopicRule.ActionProperty(
                        cloudwatch_alarm=iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                            alarm_name="alarmName",
                            role_arn="roleArn",
                            state_reason="stateReason",
                            state_value="stateValue"
                        ),
                        cloudwatch_logs=iot.CfnTopicRule.CloudwatchLogsActionProperty(
                            log_group_name="logGroupName",
                            role_arn="roleArn"
                        ),
                        cloudwatch_metric=iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name="metricName",
                            metric_namespace="metricNamespace",
                            metric_unit="metricUnit",
                            metric_value="metricValue",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            metric_timestamp="metricTimestamp"
                        ),
                        dynamo_db=iot.CfnTopicRule.DynamoDBActionProperty(
                            hash_key_field="hashKeyField",
                            hash_key_value="hashKeyValue",
                            role_arn="roleArn",
                            table_name="tableName",
            
                            # the properties below are optional
                            hash_key_type="hashKeyType",
                            payload_field="payloadField",
                            range_key_field="rangeKeyField",
                            range_key_type="rangeKeyType",
                            range_key_value="rangeKeyValue"
                        ),
                        dynamo_dBv2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                            put_item=iot.CfnTopicRule.PutItemInputProperty(
                                table_name="tableName"
                            ),
                            role_arn="roleArn"
                        ),
                        elasticsearch=iot.CfnTopicRule.ElasticsearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        firehose=iot.CfnTopicRule.FirehoseActionProperty(
                            delivery_stream_name="deliveryStreamName",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            batch_mode=False,
                            separator="separator"
                        ),
                        http=iot.CfnTopicRule.HttpActionProperty(
                            url="url",
            
                            # the properties below are optional
                            auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                                sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                                    role_arn="roleArn",
                                    service_name="serviceName",
                                    signing_region="signingRegion"
                                )
                            ),
                            confirmation_url="confirmationUrl",
                            headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                                key="key",
                                value="value"
                            )]
                        ),
                        iot_analytics=iot.CfnTopicRule.IotAnalyticsActionProperty(
                            channel_name="channelName",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            batch_mode=False
                        ),
                        iot_events=iot.CfnTopicRule.IotEventsActionProperty(
                            input_name="inputName",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            batch_mode=False,
                            message_id="messageId"
                        ),
                        iot_site_wise=iot.CfnTopicRule.IotSiteWiseActionProperty(
                            put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                                property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                                    timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                        time_in_seconds="timeInSeconds",
            
                                        # the properties below are optional
                                        offset_in_nanos="offsetInNanos"
                                    ),
                                    value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                        boolean_value="booleanValue",
                                        double_value="doubleValue",
                                        integer_value="integerValue",
                                        string_value="stringValue"
                                    ),
            
                                    # the properties below are optional
                                    quality="quality"
                                )],
            
                                # the properties below are optional
                                asset_id="assetId",
                                entry_id="entryId",
                                property_alias="propertyAlias",
                                property_id="propertyId"
                            )],
                            role_arn="roleArn"
                        ),
                        kafka=iot.CfnTopicRule.KafkaActionProperty(
                            client_properties={
                                "client_properties_key": "clientProperties"
                            },
                            destination_arn="destinationArn",
                            topic="topic",
            
                            # the properties below are optional
                            key="key",
                            partition="partition"
                        ),
                        kinesis=iot.CfnTopicRule.KinesisActionProperty(
                            role_arn="roleArn",
                            stream_name="streamName",
            
                            # the properties below are optional
                            partition_key="partitionKey"
                        ),
                        lambda_=iot.CfnTopicRule.LambdaActionProperty(
                            function_arn="functionArn"
                        ),
                        open_search=iot.CfnTopicRule.OpenSearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        republish=iot.CfnTopicRule.RepublishActionProperty(
                            role_arn="roleArn",
                            topic="topic",
            
                            # the properties below are optional
                            qos=123
                        ),
                        s3=iot.CfnTopicRule.S3ActionProperty(
                            bucket_name="bucketName",
                            key="key",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            canned_acl="cannedAcl"
                        ),
                        sns=iot.CfnTopicRule.SnsActionProperty(
                            role_arn="roleArn",
                            target_arn="targetArn",
            
                            # the properties below are optional
                            message_format="messageFormat"
                        ),
                        sqs=iot.CfnTopicRule.SqsActionProperty(
                            queue_url="queueUrl",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            use_base64=False
                        ),
                        step_functions=iot.CfnTopicRule.StepFunctionsActionProperty(
                            role_arn="roleArn",
                            state_machine_name="stateMachineName",
            
                            # the properties below are optional
                            execution_name_prefix="executionNamePrefix"
                        ),
                        timestream=iot.CfnTopicRule.TimestreamActionProperty(
                            database_name="databaseName",
                            dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                                name="name",
                                value="value"
                            )],
                            role_arn="roleArn",
                            table_name="tableName",
            
                            # the properties below are optional
                            batch_mode=False,
                            timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                                unit="unit",
                                value="value"
                            )
                        )
                    ),
                    rule_disabled=False
                ),
            
                # the properties below are optional
                rule_name="ruleName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnTopicRuleProps.__init__)
            check_type(argname="argument topic_rule_payload", value=topic_rule_payload, expected_type=type_hints["topic_rule_payload"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "topic_rule_payload": topic_rule_payload,
        }
        if rule_name is not None:
            self._values["rule_name"] = rule_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def topic_rule_payload(
        self,
    ) -> typing.Union[CfnTopicRule.TopicRulePayloadProperty, _IResolvable_da3f097b]:
        '''The rule payload.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html#cfn-iot-topicrule-topicrulepayload
        '''
        result = self._values.get("topic_rule_payload")
        assert result is not None, "Required property 'topic_rule_payload' is missing"
        return typing.cast(typing.Union[CfnTopicRule.TopicRulePayloadProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''The name of the rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html#cfn-iot-topicrule-rulename
        '''
        result = self._values.get("rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata which can be used to manage the topic rule.

        .. epigraph::

           For URI Request parameters use format: ...key1=value1&key2=value2...

           For the CLI command-line parameter use format: --tags "key1=value1&key2=value2..."

           For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html#cfn-iot-topicrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTopicRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAccountAuditConfiguration",
    "CfnAccountAuditConfigurationProps",
    "CfnAuthorizer",
    "CfnAuthorizerProps",
    "CfnCACertificate",
    "CfnCACertificateProps",
    "CfnCertificate",
    "CfnCertificateProps",
    "CfnCustomMetric",
    "CfnCustomMetricProps",
    "CfnDimension",
    "CfnDimensionProps",
    "CfnDomainConfiguration",
    "CfnDomainConfigurationProps",
    "CfnFleetMetric",
    "CfnFleetMetricProps",
    "CfnJobTemplate",
    "CfnJobTemplateProps",
    "CfnLogging",
    "CfnLoggingProps",
    "CfnMitigationAction",
    "CfnMitigationActionProps",
    "CfnPolicy",
    "CfnPolicyPrincipalAttachment",
    "CfnPolicyPrincipalAttachmentProps",
    "CfnPolicyProps",
    "CfnProvisioningTemplate",
    "CfnProvisioningTemplateProps",
    "CfnResourceSpecificLogging",
    "CfnResourceSpecificLoggingProps",
    "CfnRoleAlias",
    "CfnRoleAliasProps",
    "CfnScheduledAudit",
    "CfnScheduledAuditProps",
    "CfnSecurityProfile",
    "CfnSecurityProfileProps",
    "CfnThing",
    "CfnThingPrincipalAttachment",
    "CfnThingPrincipalAttachmentProps",
    "CfnThingProps",
    "CfnTopicRule",
    "CfnTopicRuleDestination",
    "CfnTopicRuleDestinationProps",
    "CfnTopicRuleProps",
]

publication.publish()
