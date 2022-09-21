'''
# AWS::ApplicationInsights Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_applicationinsights as applicationinsights
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ApplicationInsights construct libraries](https://constructs.dev/search?q=applicationinsights)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ApplicationInsights resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApplicationInsights.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ApplicationInsights](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApplicationInsights.html).

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
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication",
):
    '''A CloudFormation ``AWS::ApplicationInsights::Application``.

    The ``AWS::ApplicationInsights::Application`` resource adds an application that is created from a resource group.

    :cloudformationResource: AWS::ApplicationInsights::Application
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_applicationinsights as applicationinsights
        
        cfn_application = applicationinsights.CfnApplication(self, "MyCfnApplication",
            resource_group_name="resourceGroupName",
        
            # the properties below are optional
            auto_configuration_enabled=False,
            component_monitoring_settings=[applicationinsights.CfnApplication.ComponentMonitoringSettingProperty(
                component_configuration_mode="componentConfigurationMode",
                tier="tier",
        
                # the properties below are optional
                component_arn="componentArn",
                component_name="componentName",
                custom_component_configuration=applicationinsights.CfnApplication.ComponentConfigurationProperty(
                    configuration_details=applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                        alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                            alarm_metric_name="alarmMetricName"
                        )],
                        alarms=[applicationinsights.CfnApplication.AlarmProperty(
                            alarm_name="alarmName",
        
                            # the properties below are optional
                            severity="severity"
                        )],
                        ha_cluster_prometheus_exporter=applicationinsights.CfnApplication.HAClusterPrometheusExporterProperty(
                            prometheus_port="prometheusPort"
                        ),
                        hana_prometheus_exporter=applicationinsights.CfnApplication.HANAPrometheusExporterProperty(
                            agree_to_install_hanadb_client=False,
                            hana_port="hanaPort",
                            hana_secret_name="hanaSecretName",
                            hanasid="hanasid",
        
                            # the properties below are optional
                            prometheus_port="prometheusPort"
                        ),
                        jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                            host_port="hostPort",
                            jmxurl="jmxurl",
                            prometheus_port="prometheusPort"
                        ),
                        logs=[applicationinsights.CfnApplication.LogProperty(
                            log_type="logType",
        
                            # the properties below are optional
                            encoding="encoding",
                            log_group_name="logGroupName",
                            log_path="logPath",
                            pattern_set="patternSet"
                        )],
                        windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                            event_levels=["eventLevels"],
                            event_name="eventName",
                            log_group_name="logGroupName",
        
                            # the properties below are optional
                            pattern_set="patternSet"
                        )]
                    ),
                    sub_component_type_configurations=[applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                        sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                            alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                alarm_metric_name="alarmMetricName"
                            )],
                            logs=[applicationinsights.CfnApplication.LogProperty(
                                log_type="logType",
        
                                # the properties below are optional
                                encoding="encoding",
                                log_group_name="logGroupName",
                                log_path="logPath",
                                pattern_set="patternSet"
                            )],
                            windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                event_levels=["eventLevels"],
                                event_name="eventName",
                                log_group_name="logGroupName",
        
                                # the properties below are optional
                                pattern_set="patternSet"
                            )]
                        ),
                        sub_component_type="subComponentType"
                    )]
                ),
                default_overwrite_component_configuration=applicationinsights.CfnApplication.ComponentConfigurationProperty(
                    configuration_details=applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                        alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                            alarm_metric_name="alarmMetricName"
                        )],
                        alarms=[applicationinsights.CfnApplication.AlarmProperty(
                            alarm_name="alarmName",
        
                            # the properties below are optional
                            severity="severity"
                        )],
                        ha_cluster_prometheus_exporter=applicationinsights.CfnApplication.HAClusterPrometheusExporterProperty(
                            prometheus_port="prometheusPort"
                        ),
                        hana_prometheus_exporter=applicationinsights.CfnApplication.HANAPrometheusExporterProperty(
                            agree_to_install_hanadb_client=False,
                            hana_port="hanaPort",
                            hana_secret_name="hanaSecretName",
                            hanasid="hanasid",
        
                            # the properties below are optional
                            prometheus_port="prometheusPort"
                        ),
                        jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                            host_port="hostPort",
                            jmxurl="jmxurl",
                            prometheus_port="prometheusPort"
                        ),
                        logs=[applicationinsights.CfnApplication.LogProperty(
                            log_type="logType",
        
                            # the properties below are optional
                            encoding="encoding",
                            log_group_name="logGroupName",
                            log_path="logPath",
                            pattern_set="patternSet"
                        )],
                        windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                            event_levels=["eventLevels"],
                            event_name="eventName",
                            log_group_name="logGroupName",
        
                            # the properties below are optional
                            pattern_set="patternSet"
                        )]
                    ),
                    sub_component_type_configurations=[applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                        sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                            alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                alarm_metric_name="alarmMetricName"
                            )],
                            logs=[applicationinsights.CfnApplication.LogProperty(
                                log_type="logType",
        
                                # the properties below are optional
                                encoding="encoding",
                                log_group_name="logGroupName",
                                log_path="logPath",
                                pattern_set="patternSet"
                            )],
                            windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                event_levels=["eventLevels"],
                                event_name="eventName",
                                log_group_name="logGroupName",
        
                                # the properties below are optional
                                pattern_set="patternSet"
                            )]
                        ),
                        sub_component_type="subComponentType"
                    )]
                )
            )],
            custom_components=[applicationinsights.CfnApplication.CustomComponentProperty(
                component_name="componentName",
                resource_list=["resourceList"]
            )],
            cwe_monitor_enabled=False,
            grouping_type="groupingType",
            log_pattern_sets=[applicationinsights.CfnApplication.LogPatternSetProperty(
                log_patterns=[applicationinsights.CfnApplication.LogPatternProperty(
                    pattern="pattern",
                    pattern_name="patternName",
                    rank=123
                )],
                pattern_set_name="patternSetName"
            )],
            ops_center_enabled=False,
            ops_item_sns_topic_arn="opsItemSnsTopicArn",
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
        resource_group_name: builtins.str,
        auto_configuration_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        component_monitoring_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnApplication.ComponentMonitoringSettingProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        custom_components: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnApplication.CustomComponentProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        cwe_monitor_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        grouping_type: typing.Optional[builtins.str] = None,
        log_pattern_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnApplication.LogPatternSetProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ops_center_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ops_item_sns_topic_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::ApplicationInsights::Application``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resource_group_name: The name of the resource group used for the application.
        :param auto_configuration_enabled: If set to ``true`` , the application components will be configured with the monitoring configuration recommended by Application Insights.
        :param component_monitoring_settings: The monitoring settings of the components.
        :param custom_components: Describes a custom component by grouping similar standalone instances to monitor.
        :param cwe_monitor_enabled: Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as ``instance terminated`` , ``failed deployment`` , and others.
        :param grouping_type: ``AWS::ApplicationInsights::Application.GroupingType``.
        :param log_pattern_sets: The log pattern sets.
        :param ops_center_enabled: Indicates whether Application Insights will create OpsItems for any problem that is detected by Application Insights for an application.
        :param ops_item_sns_topic_arn: The SNS topic provided to Application Insights that is associated with the created OpsItems to receive SNS notifications for opsItem updates.
        :param tags: An array of ``Tags`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnApplication.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            resource_group_name=resource_group_name,
            auto_configuration_enabled=auto_configuration_enabled,
            component_monitoring_settings=component_monitoring_settings,
            custom_components=custom_components,
            cwe_monitor_enabled=cwe_monitor_enabled,
            grouping_type=grouping_type,
            log_pattern_sets=log_pattern_sets,
            ops_center_enabled=ops_center_enabled,
            ops_item_sns_topic_arn=ops_item_sns_topic_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnApplication.inspect)
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
            type_hints = typing.get_type_hints(CfnApplication._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationArn")
    def attr_application_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of the application, such as ``arn:aws:applicationinsights:us-east-1:123456789012:application/resource-group/my_resource_group`` .

        :cloudformationAttribute: ApplicationARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''An array of ``Tags`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        '''The name of the resource group used for the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-resourcegroupname
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApplication, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="autoConfigurationEnabled")
    def auto_configuration_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If set to ``true`` , the application components will be configured with the monitoring configuration recommended by Application Insights.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-autoconfigurationenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "autoConfigurationEnabled"))

    @auto_configuration_enabled.setter
    def auto_configuration_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApplication, "auto_configuration_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoConfigurationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="componentMonitoringSettings")
    def component_monitoring_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.ComponentMonitoringSettingProperty", _IResolvable_da3f097b]]]]:
        '''The monitoring settings of the components.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-componentmonitoringsettings
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.ComponentMonitoringSettingProperty", _IResolvable_da3f097b]]]], jsii.get(self, "componentMonitoringSettings"))

    @component_monitoring_settings.setter
    def component_monitoring_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.ComponentMonitoringSettingProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApplication, "component_monitoring_settings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "componentMonitoringSettings", value)

    @builtins.property
    @jsii.member(jsii_name="customComponents")
    def custom_components(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.CustomComponentProperty", _IResolvable_da3f097b]]]]:
        '''Describes a custom component by grouping similar standalone instances to monitor.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-customcomponents
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.CustomComponentProperty", _IResolvable_da3f097b]]]], jsii.get(self, "customComponents"))

    @custom_components.setter
    def custom_components(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.CustomComponentProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApplication, "custom_components").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customComponents", value)

    @builtins.property
    @jsii.member(jsii_name="cweMonitorEnabled")
    def cwe_monitor_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as ``instance terminated`` , ``failed deployment`` , and others.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-cwemonitorenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "cweMonitorEnabled"))

    @cwe_monitor_enabled.setter
    def cwe_monitor_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApplication, "cwe_monitor_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cweMonitorEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="groupingType")
    def grouping_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::ApplicationInsights::Application.GroupingType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-groupingtype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupingType"))

    @grouping_type.setter
    def grouping_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApplication, "grouping_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupingType", value)

    @builtins.property
    @jsii.member(jsii_name="logPatternSets")
    def log_pattern_sets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogPatternSetProperty", _IResolvable_da3f097b]]]]:
        '''The log pattern sets.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-logpatternsets
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogPatternSetProperty", _IResolvable_da3f097b]]]], jsii.get(self, "logPatternSets"))

    @log_pattern_sets.setter
    def log_pattern_sets(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogPatternSetProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApplication, "log_pattern_sets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logPatternSets", value)

    @builtins.property
    @jsii.member(jsii_name="opsCenterEnabled")
    def ops_center_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether Application Insights will create OpsItems for any problem that is detected by Application Insights for an application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-opscenterenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "opsCenterEnabled"))

    @ops_center_enabled.setter
    def ops_center_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApplication, "ops_center_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "opsCenterEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="opsItemSnsTopicArn")
    def ops_item_sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The SNS topic provided to Application Insights that is associated with the created OpsItems to receive SNS notifications for opsItem updates.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-opsitemsnstopicarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "opsItemSnsTopicArn"))

    @ops_item_sns_topic_arn.setter
    def ops_item_sns_topic_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnApplication, "ops_item_sns_topic_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "opsItemSnsTopicArn", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.AlarmMetricProperty",
        jsii_struct_bases=[],
        name_mapping={"alarm_metric_name": "alarmMetricName"},
    )
    class AlarmMetricProperty:
        def __init__(self, *, alarm_metric_name: builtins.str) -> None:
            '''The ``AWS::ApplicationInsights::Application AlarmMetric`` property type defines a metric to monitor for the component.

            :param alarm_metric_name: The name of the metric to be monitored for the component. For metrics supported by Application Insights, see `Logs and metrics supported by Amazon CloudWatch Application Insights <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-logs-and-metrics.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarmmetric.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                alarm_metric_property = applicationinsights.CfnApplication.AlarmMetricProperty(
                    alarm_metric_name="alarmMetricName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.AlarmMetricProperty.__init__)
                check_type(argname="argument alarm_metric_name", value=alarm_metric_name, expected_type=type_hints["alarm_metric_name"])
            self._values: typing.Dict[str, typing.Any] = {
                "alarm_metric_name": alarm_metric_name,
            }

        @builtins.property
        def alarm_metric_name(self) -> builtins.str:
            '''The name of the metric to be monitored for the component.

            For metrics supported by Application Insights, see `Logs and metrics supported by Amazon CloudWatch Application Insights <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-logs-and-metrics.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarmmetric.html#cfn-applicationinsights-application-alarmmetric-alarmmetricname
            '''
            result = self._values.get("alarm_metric_name")
            assert result is not None, "Required property 'alarm_metric_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmMetricProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.AlarmProperty",
        jsii_struct_bases=[],
        name_mapping={"alarm_name": "alarmName", "severity": "severity"},
    )
    class AlarmProperty:
        def __init__(
            self,
            *,
            alarm_name: builtins.str,
            severity: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``AWS::ApplicationInsights::Application Alarm`` property type defines a CloudWatch alarm to be monitored for the component.

            :param alarm_name: The name of the CloudWatch alarm to be monitored for the component.
            :param severity: Indicates the degree of outage when the alarm goes off.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                alarm_property = applicationinsights.CfnApplication.AlarmProperty(
                    alarm_name="alarmName",
                
                    # the properties below are optional
                    severity="severity"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.AlarmProperty.__init__)
                check_type(argname="argument alarm_name", value=alarm_name, expected_type=type_hints["alarm_name"])
                check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            self._values: typing.Dict[str, typing.Any] = {
                "alarm_name": alarm_name,
            }
            if severity is not None:
                self._values["severity"] = severity

        @builtins.property
        def alarm_name(self) -> builtins.str:
            '''The name of the CloudWatch alarm to be monitored for the component.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html#cfn-applicationinsights-application-alarm-alarmname
            '''
            result = self._values.get("alarm_name")
            assert result is not None, "Required property 'alarm_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def severity(self) -> typing.Optional[builtins.str]:
            '''Indicates the degree of outage when the alarm goes off.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html#cfn-applicationinsights-application-alarm-severity
            '''
            result = self._values.get("severity")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.ComponentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration_details": "configurationDetails",
            "sub_component_type_configurations": "subComponentTypeConfigurations",
        },
    )
    class ComponentConfigurationProperty:
        def __init__(
            self,
            *,
            configuration_details: typing.Optional[typing.Union[typing.Union["CfnApplication.ConfigurationDetailsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            sub_component_type_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnApplication.SubComponentTypeConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''The ``AWS::ApplicationInsights::Application ComponentConfiguration`` property type defines the configuration settings of the component.

            :param configuration_details: The configuration settings.
            :param sub_component_type_configurations: Sub-component configurations of the component.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                component_configuration_property = applicationinsights.CfnApplication.ComponentConfigurationProperty(
                    configuration_details=applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                        alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                            alarm_metric_name="alarmMetricName"
                        )],
                        alarms=[applicationinsights.CfnApplication.AlarmProperty(
                            alarm_name="alarmName",
                
                            # the properties below are optional
                            severity="severity"
                        )],
                        ha_cluster_prometheus_exporter=applicationinsights.CfnApplication.HAClusterPrometheusExporterProperty(
                            prometheus_port="prometheusPort"
                        ),
                        hana_prometheus_exporter=applicationinsights.CfnApplication.HANAPrometheusExporterProperty(
                            agree_to_install_hanadb_client=False,
                            hana_port="hanaPort",
                            hana_secret_name="hanaSecretName",
                            hanasid="hanasid",
                
                            # the properties below are optional
                            prometheus_port="prometheusPort"
                        ),
                        jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                            host_port="hostPort",
                            jmxurl="jmxurl",
                            prometheus_port="prometheusPort"
                        ),
                        logs=[applicationinsights.CfnApplication.LogProperty(
                            log_type="logType",
                
                            # the properties below are optional
                            encoding="encoding",
                            log_group_name="logGroupName",
                            log_path="logPath",
                            pattern_set="patternSet"
                        )],
                        windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                            event_levels=["eventLevels"],
                            event_name="eventName",
                            log_group_name="logGroupName",
                
                            # the properties below are optional
                            pattern_set="patternSet"
                        )]
                    ),
                    sub_component_type_configurations=[applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                        sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                            alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                alarm_metric_name="alarmMetricName"
                            )],
                            logs=[applicationinsights.CfnApplication.LogProperty(
                                log_type="logType",
                
                                # the properties below are optional
                                encoding="encoding",
                                log_group_name="logGroupName",
                                log_path="logPath",
                                pattern_set="patternSet"
                            )],
                            windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                event_levels=["eventLevels"],
                                event_name="eventName",
                                log_group_name="logGroupName",
                
                                # the properties below are optional
                                pattern_set="patternSet"
                            )]
                        ),
                        sub_component_type="subComponentType"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.ComponentConfigurationProperty.__init__)
                check_type(argname="argument configuration_details", value=configuration_details, expected_type=type_hints["configuration_details"])
                check_type(argname="argument sub_component_type_configurations", value=sub_component_type_configurations, expected_type=type_hints["sub_component_type_configurations"])
            self._values: typing.Dict[str, typing.Any] = {}
            if configuration_details is not None:
                self._values["configuration_details"] = configuration_details
            if sub_component_type_configurations is not None:
                self._values["sub_component_type_configurations"] = sub_component_type_configurations

        @builtins.property
        def configuration_details(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.ConfigurationDetailsProperty", _IResolvable_da3f097b]]:
            '''The configuration settings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html#cfn-applicationinsights-application-componentconfiguration-configurationdetails
            '''
            result = self._values.get("configuration_details")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.ConfigurationDetailsProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def sub_component_type_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.SubComponentTypeConfigurationProperty", _IResolvable_da3f097b]]]]:
            '''Sub-component configurations of the component.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html#cfn-applicationinsights-application-componentconfiguration-subcomponenttypeconfigurations
            '''
            result = self._values.get("sub_component_type_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.SubComponentTypeConfigurationProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.ComponentMonitoringSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "component_configuration_mode": "componentConfigurationMode",
            "tier": "tier",
            "component_arn": "componentArn",
            "component_name": "componentName",
            "custom_component_configuration": "customComponentConfiguration",
            "default_overwrite_component_configuration": "defaultOverwriteComponentConfiguration",
        },
    )
    class ComponentMonitoringSettingProperty:
        def __init__(
            self,
            *,
            component_configuration_mode: builtins.str,
            tier: builtins.str,
            component_arn: typing.Optional[builtins.str] = None,
            component_name: typing.Optional[builtins.str] = None,
            custom_component_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.ComponentConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            default_overwrite_component_configuration: typing.Optional[typing.Union[typing.Union["CfnApplication.ComponentConfigurationProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The ``AWS::ApplicationInsights::Application ComponentMonitoringSetting`` property type defines the monitoring setting of the component.

            :param component_configuration_mode: Component monitoring can be configured in one of the following three modes:. - ``DEFAULT`` : The component will be configured with the recommended default monitoring settings of the selected ``Tier`` . - ``CUSTOM`` : The component will be configured with the customized monitoring settings that are specified in ``CustomComponentConfiguration`` . If used, ``CustomComponentConfiguration`` must be provided. - ``DEFAULT_WITH_OVERWRITE`` : The component will be configured with the recommended default monitoring settings of the selected ``Tier`` , and merged with customized overwrite settings that are specified in ``DefaultOverwriteComponentConfiguration`` . If used, ``DefaultOverwriteComponentConfiguration`` must be provided.
            :param tier: The tier of the application component. Supported tiers include ``DOT_NET_CORE`` , ``DOT_NET_WORKER`` , ``DOT_NET_WEB`` , ``SQL_SERVER`` , ``SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP`` , ``SQL_SERVER_FAILOVER_CLUSTER_INSTANCE`` , ``MYSQL`` , ``POSTGRESQL`` , ``JAVA_JMX`` , ``ORACLE`` , ``SAP_HANA_MULTI_NODE`` , ``SAP_HANA_SINGLE_NODE`` , ``SAP_HANA_HIGH_AVAILABILITY`` , ``SHAREPOINT`` . ``ACTIVE_DIRECTORY`` , and ``DEFAULT`` .
            :param component_arn: The ARN of the component.
            :param component_name: The name of the component.
            :param custom_component_configuration: Customized monitoring settings. Required if CUSTOM mode is configured in ``ComponentConfigurationMode`` .
            :param default_overwrite_component_configuration: Customized overwrite monitoring settings. Required if CUSTOM mode is configured in ``ComponentConfigurationMode`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                component_monitoring_setting_property = applicationinsights.CfnApplication.ComponentMonitoringSettingProperty(
                    component_configuration_mode="componentConfigurationMode",
                    tier="tier",
                
                    # the properties below are optional
                    component_arn="componentArn",
                    component_name="componentName",
                    custom_component_configuration=applicationinsights.CfnApplication.ComponentConfigurationProperty(
                        configuration_details=applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                            alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                alarm_metric_name="alarmMetricName"
                            )],
                            alarms=[applicationinsights.CfnApplication.AlarmProperty(
                                alarm_name="alarmName",
                
                                # the properties below are optional
                                severity="severity"
                            )],
                            ha_cluster_prometheus_exporter=applicationinsights.CfnApplication.HAClusterPrometheusExporterProperty(
                                prometheus_port="prometheusPort"
                            ),
                            hana_prometheus_exporter=applicationinsights.CfnApplication.HANAPrometheusExporterProperty(
                                agree_to_install_hanadb_client=False,
                                hana_port="hanaPort",
                                hana_secret_name="hanaSecretName",
                                hanasid="hanasid",
                
                                # the properties below are optional
                                prometheus_port="prometheusPort"
                            ),
                            jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                                host_port="hostPort",
                                jmxurl="jmxurl",
                                prometheus_port="prometheusPort"
                            ),
                            logs=[applicationinsights.CfnApplication.LogProperty(
                                log_type="logType",
                
                                # the properties below are optional
                                encoding="encoding",
                                log_group_name="logGroupName",
                                log_path="logPath",
                                pattern_set="patternSet"
                            )],
                            windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                event_levels=["eventLevels"],
                                event_name="eventName",
                                log_group_name="logGroupName",
                
                                # the properties below are optional
                                pattern_set="patternSet"
                            )]
                        ),
                        sub_component_type_configurations=[applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                            sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                                alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                    alarm_metric_name="alarmMetricName"
                                )],
                                logs=[applicationinsights.CfnApplication.LogProperty(
                                    log_type="logType",
                
                                    # the properties below are optional
                                    encoding="encoding",
                                    log_group_name="logGroupName",
                                    log_path="logPath",
                                    pattern_set="patternSet"
                                )],
                                windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                    event_levels=["eventLevels"],
                                    event_name="eventName",
                                    log_group_name="logGroupName",
                
                                    # the properties below are optional
                                    pattern_set="patternSet"
                                )]
                            ),
                            sub_component_type="subComponentType"
                        )]
                    ),
                    default_overwrite_component_configuration=applicationinsights.CfnApplication.ComponentConfigurationProperty(
                        configuration_details=applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                            alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                alarm_metric_name="alarmMetricName"
                            )],
                            alarms=[applicationinsights.CfnApplication.AlarmProperty(
                                alarm_name="alarmName",
                
                                # the properties below are optional
                                severity="severity"
                            )],
                            ha_cluster_prometheus_exporter=applicationinsights.CfnApplication.HAClusterPrometheusExporterProperty(
                                prometheus_port="prometheusPort"
                            ),
                            hana_prometheus_exporter=applicationinsights.CfnApplication.HANAPrometheusExporterProperty(
                                agree_to_install_hanadb_client=False,
                                hana_port="hanaPort",
                                hana_secret_name="hanaSecretName",
                                hanasid="hanasid",
                
                                # the properties below are optional
                                prometheus_port="prometheusPort"
                            ),
                            jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                                host_port="hostPort",
                                jmxurl="jmxurl",
                                prometheus_port="prometheusPort"
                            ),
                            logs=[applicationinsights.CfnApplication.LogProperty(
                                log_type="logType",
                
                                # the properties below are optional
                                encoding="encoding",
                                log_group_name="logGroupName",
                                log_path="logPath",
                                pattern_set="patternSet"
                            )],
                            windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                event_levels=["eventLevels"],
                                event_name="eventName",
                                log_group_name="logGroupName",
                
                                # the properties below are optional
                                pattern_set="patternSet"
                            )]
                        ),
                        sub_component_type_configurations=[applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                            sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                                alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                    alarm_metric_name="alarmMetricName"
                                )],
                                logs=[applicationinsights.CfnApplication.LogProperty(
                                    log_type="logType",
                
                                    # the properties below are optional
                                    encoding="encoding",
                                    log_group_name="logGroupName",
                                    log_path="logPath",
                                    pattern_set="patternSet"
                                )],
                                windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                    event_levels=["eventLevels"],
                                    event_name="eventName",
                                    log_group_name="logGroupName",
                
                                    # the properties below are optional
                                    pattern_set="patternSet"
                                )]
                            ),
                            sub_component_type="subComponentType"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.ComponentMonitoringSettingProperty.__init__)
                check_type(argname="argument component_configuration_mode", value=component_configuration_mode, expected_type=type_hints["component_configuration_mode"])
                check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
                check_type(argname="argument component_arn", value=component_arn, expected_type=type_hints["component_arn"])
                check_type(argname="argument component_name", value=component_name, expected_type=type_hints["component_name"])
                check_type(argname="argument custom_component_configuration", value=custom_component_configuration, expected_type=type_hints["custom_component_configuration"])
                check_type(argname="argument default_overwrite_component_configuration", value=default_overwrite_component_configuration, expected_type=type_hints["default_overwrite_component_configuration"])
            self._values: typing.Dict[str, typing.Any] = {
                "component_configuration_mode": component_configuration_mode,
                "tier": tier,
            }
            if component_arn is not None:
                self._values["component_arn"] = component_arn
            if component_name is not None:
                self._values["component_name"] = component_name
            if custom_component_configuration is not None:
                self._values["custom_component_configuration"] = custom_component_configuration
            if default_overwrite_component_configuration is not None:
                self._values["default_overwrite_component_configuration"] = default_overwrite_component_configuration

        @builtins.property
        def component_configuration_mode(self) -> builtins.str:
            '''Component monitoring can be configured in one of the following three modes:.

            - ``DEFAULT`` : The component will be configured with the recommended default monitoring settings of the selected ``Tier`` .
            - ``CUSTOM`` : The component will be configured with the customized monitoring settings that are specified in ``CustomComponentConfiguration`` . If used, ``CustomComponentConfiguration`` must be provided.
            - ``DEFAULT_WITH_OVERWRITE`` : The component will be configured with the recommended default monitoring settings of the selected ``Tier`` , and merged with customized overwrite settings that are specified in ``DefaultOverwriteComponentConfiguration`` . If used, ``DefaultOverwriteComponentConfiguration`` must be provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-componentconfigurationmode
            '''
            result = self._values.get("component_configuration_mode")
            assert result is not None, "Required property 'component_configuration_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tier(self) -> builtins.str:
            '''The tier of the application component.

            Supported tiers include ``DOT_NET_CORE`` , ``DOT_NET_WORKER`` , ``DOT_NET_WEB`` , ``SQL_SERVER`` , ``SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP`` , ``SQL_SERVER_FAILOVER_CLUSTER_INSTANCE`` , ``MYSQL`` , ``POSTGRESQL`` , ``JAVA_JMX`` , ``ORACLE`` , ``SAP_HANA_MULTI_NODE`` , ``SAP_HANA_SINGLE_NODE`` , ``SAP_HANA_HIGH_AVAILABILITY`` , ``SHAREPOINT`` . ``ACTIVE_DIRECTORY`` , and ``DEFAULT`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-tier
            '''
            result = self._values.get("tier")
            assert result is not None, "Required property 'tier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def component_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the component.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-componentarn
            '''
            result = self._values.get("component_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def component_name(self) -> typing.Optional[builtins.str]:
            '''The name of the component.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-componentname
            '''
            result = self._values.get("component_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_component_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.ComponentConfigurationProperty", _IResolvable_da3f097b]]:
            '''Customized monitoring settings.

            Required if CUSTOM mode is configured in ``ComponentConfigurationMode`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-customcomponentconfiguration
            '''
            result = self._values.get("custom_component_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.ComponentConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def default_overwrite_component_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.ComponentConfigurationProperty", _IResolvable_da3f097b]]:
            '''Customized overwrite monitoring settings.

            Required if CUSTOM mode is configured in ``ComponentConfigurationMode`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-defaultoverwritecomponentconfiguration
            '''
            result = self._values.get("default_overwrite_component_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.ComponentConfigurationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentMonitoringSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.ConfigurationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alarm_metrics": "alarmMetrics",
            "alarms": "alarms",
            "ha_cluster_prometheus_exporter": "haClusterPrometheusExporter",
            "hana_prometheus_exporter": "hanaPrometheusExporter",
            "jmx_prometheus_exporter": "jmxPrometheusExporter",
            "logs": "logs",
            "windows_events": "windowsEvents",
        },
    )
    class ConfigurationDetailsProperty:
        def __init__(
            self,
            *,
            alarm_metrics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnApplication.AlarmMetricProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            alarms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnApplication.AlarmProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            ha_cluster_prometheus_exporter: typing.Optional[typing.Union[typing.Union["CfnApplication.HAClusterPrometheusExporterProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            hana_prometheus_exporter: typing.Optional[typing.Union[typing.Union["CfnApplication.HANAPrometheusExporterProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            jmx_prometheus_exporter: typing.Optional[typing.Union[typing.Union["CfnApplication.JMXPrometheusExporterProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
            logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnApplication.LogProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            windows_events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnApplication.WindowsEventProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''The ``AWS::ApplicationInsights::Application ConfigurationDetails`` property type specifies the configuration settings.

            :param alarm_metrics: A list of metrics to monitor for the component. All component types can use ``AlarmMetrics`` .
            :param alarms: A list of alarms to monitor for the component. All component types can use ``Alarm`` .
            :param ha_cluster_prometheus_exporter: The HA cluster Prometheus Exporter settings.
            :param hana_prometheus_exporter: The HANA DB Prometheus Exporter settings.
            :param jmx_prometheus_exporter: A list of Java metrics to monitor for the component.
            :param logs: A list of logs to monitor for the component. Only Amazon EC2 instances can use ``Logs`` .
            :param windows_events: A list of Windows Events to monitor for the component. Only Amazon EC2 instances running on Windows can use ``WindowsEvents`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                configuration_details_property = applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                    alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                        alarm_metric_name="alarmMetricName"
                    )],
                    alarms=[applicationinsights.CfnApplication.AlarmProperty(
                        alarm_name="alarmName",
                
                        # the properties below are optional
                        severity="severity"
                    )],
                    ha_cluster_prometheus_exporter=applicationinsights.CfnApplication.HAClusterPrometheusExporterProperty(
                        prometheus_port="prometheusPort"
                    ),
                    hana_prometheus_exporter=applicationinsights.CfnApplication.HANAPrometheusExporterProperty(
                        agree_to_install_hanadb_client=False,
                        hana_port="hanaPort",
                        hana_secret_name="hanaSecretName",
                        hanasid="hanasid",
                
                        # the properties below are optional
                        prometheus_port="prometheusPort"
                    ),
                    jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                        host_port="hostPort",
                        jmxurl="jmxurl",
                        prometheus_port="prometheusPort"
                    ),
                    logs=[applicationinsights.CfnApplication.LogProperty(
                        log_type="logType",
                
                        # the properties below are optional
                        encoding="encoding",
                        log_group_name="logGroupName",
                        log_path="logPath",
                        pattern_set="patternSet"
                    )],
                    windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                        event_levels=["eventLevels"],
                        event_name="eventName",
                        log_group_name="logGroupName",
                
                        # the properties below are optional
                        pattern_set="patternSet"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.ConfigurationDetailsProperty.__init__)
                check_type(argname="argument alarm_metrics", value=alarm_metrics, expected_type=type_hints["alarm_metrics"])
                check_type(argname="argument alarms", value=alarms, expected_type=type_hints["alarms"])
                check_type(argname="argument ha_cluster_prometheus_exporter", value=ha_cluster_prometheus_exporter, expected_type=type_hints["ha_cluster_prometheus_exporter"])
                check_type(argname="argument hana_prometheus_exporter", value=hana_prometheus_exporter, expected_type=type_hints["hana_prometheus_exporter"])
                check_type(argname="argument jmx_prometheus_exporter", value=jmx_prometheus_exporter, expected_type=type_hints["jmx_prometheus_exporter"])
                check_type(argname="argument logs", value=logs, expected_type=type_hints["logs"])
                check_type(argname="argument windows_events", value=windows_events, expected_type=type_hints["windows_events"])
            self._values: typing.Dict[str, typing.Any] = {}
            if alarm_metrics is not None:
                self._values["alarm_metrics"] = alarm_metrics
            if alarms is not None:
                self._values["alarms"] = alarms
            if ha_cluster_prometheus_exporter is not None:
                self._values["ha_cluster_prometheus_exporter"] = ha_cluster_prometheus_exporter
            if hana_prometheus_exporter is not None:
                self._values["hana_prometheus_exporter"] = hana_prometheus_exporter
            if jmx_prometheus_exporter is not None:
                self._values["jmx_prometheus_exporter"] = jmx_prometheus_exporter
            if logs is not None:
                self._values["logs"] = logs
            if windows_events is not None:
                self._values["windows_events"] = windows_events

        @builtins.property
        def alarm_metrics(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.AlarmMetricProperty", _IResolvable_da3f097b]]]]:
            '''A list of metrics to monitor for the component.

            All component types can use ``AlarmMetrics`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-alarmmetrics
            '''
            result = self._values.get("alarm_metrics")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.AlarmMetricProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def alarms(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.AlarmProperty", _IResolvable_da3f097b]]]]:
            '''A list of alarms to monitor for the component.

            All component types can use ``Alarm`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-alarms
            '''
            result = self._values.get("alarms")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.AlarmProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def ha_cluster_prometheus_exporter(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.HAClusterPrometheusExporterProperty", _IResolvable_da3f097b]]:
            '''The HA cluster Prometheus Exporter settings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-haclusterprometheusexporter
            '''
            result = self._values.get("ha_cluster_prometheus_exporter")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.HAClusterPrometheusExporterProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def hana_prometheus_exporter(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.HANAPrometheusExporterProperty", _IResolvable_da3f097b]]:
            '''The HANA DB Prometheus Exporter settings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-hanaprometheusexporter
            '''
            result = self._values.get("hana_prometheus_exporter")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.HANAPrometheusExporterProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def jmx_prometheus_exporter(
            self,
        ) -> typing.Optional[typing.Union["CfnApplication.JMXPrometheusExporterProperty", _IResolvable_da3f097b]]:
            '''A list of Java metrics to monitor for the component.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-jmxprometheusexporter
            '''
            result = self._values.get("jmx_prometheus_exporter")
            return typing.cast(typing.Optional[typing.Union["CfnApplication.JMXPrometheusExporterProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def logs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogProperty", _IResolvable_da3f097b]]]]:
            '''A list of logs to monitor for the component.

            Only Amazon EC2 instances can use ``Logs`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-logs
            '''
            result = self._values.get("logs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def windows_events(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.WindowsEventProperty", _IResolvable_da3f097b]]]]:
            '''A list of Windows Events to monitor for the component.

            Only Amazon EC2 instances running on Windows can use ``WindowsEvents`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-windowsevents
            '''
            result = self._values.get("windows_events")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.WindowsEventProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.CustomComponentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "component_name": "componentName",
            "resource_list": "resourceList",
        },
    )
    class CustomComponentProperty:
        def __init__(
            self,
            *,
            component_name: builtins.str,
            resource_list: typing.Sequence[builtins.str],
        ) -> None:
            '''The ``AWS::ApplicationInsights::Application CustomComponent`` property type describes a custom component by grouping similar standalone instances to monitor.

            :param component_name: The name of the component.
            :param resource_list: The list of resource ARNs that belong to the component.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                custom_component_property = applicationinsights.CfnApplication.CustomComponentProperty(
                    component_name="componentName",
                    resource_list=["resourceList"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.CustomComponentProperty.__init__)
                check_type(argname="argument component_name", value=component_name, expected_type=type_hints["component_name"])
                check_type(argname="argument resource_list", value=resource_list, expected_type=type_hints["resource_list"])
            self._values: typing.Dict[str, typing.Any] = {
                "component_name": component_name,
                "resource_list": resource_list,
            }

        @builtins.property
        def component_name(self) -> builtins.str:
            '''The name of the component.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html#cfn-applicationinsights-application-customcomponent-componentname
            '''
            result = self._values.get("component_name")
            assert result is not None, "Required property 'component_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_list(self) -> typing.List[builtins.str]:
            '''The list of resource ARNs that belong to the component.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html#cfn-applicationinsights-application-customcomponent-resourcelist
            '''
            result = self._values.get("resource_list")
            assert result is not None, "Required property 'resource_list' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomComponentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.HAClusterPrometheusExporterProperty",
        jsii_struct_bases=[],
        name_mapping={"prometheus_port": "prometheusPort"},
    )
    class HAClusterPrometheusExporterProperty:
        def __init__(
            self,
            *,
            prometheus_port: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``AWS::ApplicationInsights::Application HAClusterPrometheusExporter`` property type defines the HA cluster Prometheus Exporter settings.

            For more information, see the `component configuration <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-config-sections.html#component-configuration-prometheus>`_ in the CloudWatch Application Insights documentation.

            :param prometheus_port: The target port to which Prometheus sends metrics. If not specified, the default port 9668 is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-haclusterprometheusexporter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                h_aCluster_prometheus_exporter_property = applicationinsights.CfnApplication.HAClusterPrometheusExporterProperty(
                    prometheus_port="prometheusPort"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.HAClusterPrometheusExporterProperty.__init__)
                check_type(argname="argument prometheus_port", value=prometheus_port, expected_type=type_hints["prometheus_port"])
            self._values: typing.Dict[str, typing.Any] = {}
            if prometheus_port is not None:
                self._values["prometheus_port"] = prometheus_port

        @builtins.property
        def prometheus_port(self) -> typing.Optional[builtins.str]:
            '''The target port to which Prometheus sends metrics.

            If not specified, the default port 9668 is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-haclusterprometheusexporter.html#cfn-applicationinsights-application-haclusterprometheusexporter-prometheusport
            '''
            result = self._values.get("prometheus_port")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HAClusterPrometheusExporterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.HANAPrometheusExporterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "agree_to_install_hanadb_client": "agreeToInstallHanadbClient",
            "hana_port": "hanaPort",
            "hana_secret_name": "hanaSecretName",
            "hanasid": "hanasid",
            "prometheus_port": "prometheusPort",
        },
    )
    class HANAPrometheusExporterProperty:
        def __init__(
            self,
            *,
            agree_to_install_hanadb_client: typing.Union[builtins.bool, _IResolvable_da3f097b],
            hana_port: builtins.str,
            hana_secret_name: builtins.str,
            hanasid: builtins.str,
            prometheus_port: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``AWS::ApplicationInsights::Application HANAPrometheusExporter`` property type defines the HANA DB Prometheus Exporter settings.

            For more information, see the `component configuration <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-config-sections.html#component-configuration-prometheus>`_ in the CloudWatch Application Insights documentation.

            :param agree_to_install_hanadb_client: Designates whether you agree to install the HANA DB client.
            :param hana_port: The HANA database port by which the exporter will query HANA metrics.
            :param hana_secret_name: The AWS Secrets Manager secret that stores HANA monitoring user credentials. The HANA Prometheus exporter uses these credentials to connect to the database and query HANA metrics.
            :param hanasid: The three-character SAP system ID (SID) of the SAP HANA system.
            :param prometheus_port: The target port to which Prometheus sends metrics. If not specified, the default port 9668 is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-hanaprometheusexporter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                h_aNAPrometheus_exporter_property = applicationinsights.CfnApplication.HANAPrometheusExporterProperty(
                    agree_to_install_hanadb_client=False,
                    hana_port="hanaPort",
                    hana_secret_name="hanaSecretName",
                    hanasid="hanasid",
                
                    # the properties below are optional
                    prometheus_port="prometheusPort"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.HANAPrometheusExporterProperty.__init__)
                check_type(argname="argument agree_to_install_hanadb_client", value=agree_to_install_hanadb_client, expected_type=type_hints["agree_to_install_hanadb_client"])
                check_type(argname="argument hana_port", value=hana_port, expected_type=type_hints["hana_port"])
                check_type(argname="argument hana_secret_name", value=hana_secret_name, expected_type=type_hints["hana_secret_name"])
                check_type(argname="argument hanasid", value=hanasid, expected_type=type_hints["hanasid"])
                check_type(argname="argument prometheus_port", value=prometheus_port, expected_type=type_hints["prometheus_port"])
            self._values: typing.Dict[str, typing.Any] = {
                "agree_to_install_hanadb_client": agree_to_install_hanadb_client,
                "hana_port": hana_port,
                "hana_secret_name": hana_secret_name,
                "hanasid": hanasid,
            }
            if prometheus_port is not None:
                self._values["prometheus_port"] = prometheus_port

        @builtins.property
        def agree_to_install_hanadb_client(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Designates whether you agree to install the HANA DB client.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-hanaprometheusexporter.html#cfn-applicationinsights-application-hanaprometheusexporter-agreetoinstallhanadbclient
            '''
            result = self._values.get("agree_to_install_hanadb_client")
            assert result is not None, "Required property 'agree_to_install_hanadb_client' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def hana_port(self) -> builtins.str:
            '''The HANA database port by which the exporter will query HANA metrics.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-hanaprometheusexporter.html#cfn-applicationinsights-application-hanaprometheusexporter-hanaport
            '''
            result = self._values.get("hana_port")
            assert result is not None, "Required property 'hana_port' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hana_secret_name(self) -> builtins.str:
            '''The AWS Secrets Manager secret that stores HANA monitoring user credentials.

            The HANA Prometheus exporter uses these credentials to connect to the database and query HANA metrics.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-hanaprometheusexporter.html#cfn-applicationinsights-application-hanaprometheusexporter-hanasecretname
            '''
            result = self._values.get("hana_secret_name")
            assert result is not None, "Required property 'hana_secret_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hanasid(self) -> builtins.str:
            '''The three-character SAP system ID (SID) of the SAP HANA system.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-hanaprometheusexporter.html#cfn-applicationinsights-application-hanaprometheusexporter-hanasid
            '''
            result = self._values.get("hanasid")
            assert result is not None, "Required property 'hanasid' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def prometheus_port(self) -> typing.Optional[builtins.str]:
            '''The target port to which Prometheus sends metrics.

            If not specified, the default port 9668 is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-hanaprometheusexporter.html#cfn-applicationinsights-application-hanaprometheusexporter-prometheusport
            '''
            result = self._values.get("prometheus_port")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HANAPrometheusExporterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.JMXPrometheusExporterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "host_port": "hostPort",
            "jmxurl": "jmxurl",
            "prometheus_port": "prometheusPort",
        },
    )
    class JMXPrometheusExporterProperty:
        def __init__(
            self,
            *,
            host_port: typing.Optional[builtins.str] = None,
            jmxurl: typing.Optional[builtins.str] = None,
            prometheus_port: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``AWS::ApplicationInsights::Application JMXPrometheusExporter`` property type defines the JMXPrometheus Exporter configuration.

            For more information, see the `component configuration <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-config-sections.html#component-configuration-prometheus>`_ in the CloudWatch Application Insights documentation.

            :param host_port: The host and port to connect to through remote JMX. Only one of ``jmxURL`` and ``hostPort`` can be specified.
            :param jmxurl: The complete JMX URL to connect to.
            :param prometheus_port: The target port to send Prometheus metrics to. If not specified, the default port ``9404`` is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                j_mXPrometheus_exporter_property = applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                    host_port="hostPort",
                    jmxurl="jmxurl",
                    prometheus_port="prometheusPort"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.JMXPrometheusExporterProperty.__init__)
                check_type(argname="argument host_port", value=host_port, expected_type=type_hints["host_port"])
                check_type(argname="argument jmxurl", value=jmxurl, expected_type=type_hints["jmxurl"])
                check_type(argname="argument prometheus_port", value=prometheus_port, expected_type=type_hints["prometheus_port"])
            self._values: typing.Dict[str, typing.Any] = {}
            if host_port is not None:
                self._values["host_port"] = host_port
            if jmxurl is not None:
                self._values["jmxurl"] = jmxurl
            if prometheus_port is not None:
                self._values["prometheus_port"] = prometheus_port

        @builtins.property
        def host_port(self) -> typing.Optional[builtins.str]:
            '''The host and port to connect to through remote JMX.

            Only one of ``jmxURL`` and ``hostPort`` can be specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html#cfn-applicationinsights-application-jmxprometheusexporter-hostport
            '''
            result = self._values.get("host_port")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def jmxurl(self) -> typing.Optional[builtins.str]:
            '''The complete JMX URL to connect to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html#cfn-applicationinsights-application-jmxprometheusexporter-jmxurl
            '''
            result = self._values.get("jmxurl")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prometheus_port(self) -> typing.Optional[builtins.str]:
            '''The target port to send Prometheus metrics to.

            If not specified, the default port ``9404`` is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html#cfn-applicationinsights-application-jmxprometheusexporter-prometheusport
            '''
            result = self._values.get("prometheus_port")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JMXPrometheusExporterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.LogPatternProperty",
        jsii_struct_bases=[],
        name_mapping={
            "pattern": "pattern",
            "pattern_name": "patternName",
            "rank": "rank",
        },
    )
    class LogPatternProperty:
        def __init__(
            self,
            *,
            pattern: builtins.str,
            pattern_name: builtins.str,
            rank: jsii.Number,
        ) -> None:
            '''The ``AWS::ApplicationInsights::Application LogPattern`` property type specifies an object that defines the log patterns that belong to a ``LogPatternSet`` .

            :param pattern: A regular expression that defines the log pattern. A log pattern can contain up to 50 characters, and it cannot be empty.
            :param pattern_name: The name of the log pattern. A log pattern name can contain up to 50 characters, and it cannot be empty. The characters can be Unicode letters, digits, or one of the following symbols: period, dash, underscore.
            :param rank: The rank of the log pattern.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                log_pattern_property = applicationinsights.CfnApplication.LogPatternProperty(
                    pattern="pattern",
                    pattern_name="patternName",
                    rank=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.LogPatternProperty.__init__)
                check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
                check_type(argname="argument pattern_name", value=pattern_name, expected_type=type_hints["pattern_name"])
                check_type(argname="argument rank", value=rank, expected_type=type_hints["rank"])
            self._values: typing.Dict[str, typing.Any] = {
                "pattern": pattern,
                "pattern_name": pattern_name,
                "rank": rank,
            }

        @builtins.property
        def pattern(self) -> builtins.str:
            '''A regular expression that defines the log pattern.

            A log pattern can contain up to 50 characters, and it cannot be empty.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html#cfn-applicationinsights-application-logpattern-pattern
            '''
            result = self._values.get("pattern")
            assert result is not None, "Required property 'pattern' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def pattern_name(self) -> builtins.str:
            '''The name of the log pattern.

            A log pattern name can contain up to 50 characters, and it cannot be empty. The characters can be Unicode letters, digits, or one of the following symbols: period, dash, underscore.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html#cfn-applicationinsights-application-logpattern-patternname
            '''
            result = self._values.get("pattern_name")
            assert result is not None, "Required property 'pattern_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def rank(self) -> jsii.Number:
            '''The rank of the log pattern.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html#cfn-applicationinsights-application-logpattern-rank
            '''
            result = self._values.get("rank")
            assert result is not None, "Required property 'rank' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogPatternProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.LogPatternSetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_patterns": "logPatterns",
            "pattern_set_name": "patternSetName",
        },
    )
    class LogPatternSetProperty:
        def __init__(
            self,
            *,
            log_patterns: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnApplication.LogPatternProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]],
            pattern_set_name: builtins.str,
        ) -> None:
            '''The ``AWS::ApplicationInsights::Application LogPatternSet`` property type specifies the log pattern set.

            :param log_patterns: A list of objects that define the log patterns that belong to ``LogPatternSet`` .
            :param pattern_set_name: The name of the log pattern. A log pattern name can contain up to 30 characters, and it cannot be empty. The characters can be Unicode letters, digits, or one of the following symbols: period, dash, underscore.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                log_pattern_set_property = applicationinsights.CfnApplication.LogPatternSetProperty(
                    log_patterns=[applicationinsights.CfnApplication.LogPatternProperty(
                        pattern="pattern",
                        pattern_name="patternName",
                        rank=123
                    )],
                    pattern_set_name="patternSetName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.LogPatternSetProperty.__init__)
                check_type(argname="argument log_patterns", value=log_patterns, expected_type=type_hints["log_patterns"])
                check_type(argname="argument pattern_set_name", value=pattern_set_name, expected_type=type_hints["pattern_set_name"])
            self._values: typing.Dict[str, typing.Any] = {
                "log_patterns": log_patterns,
                "pattern_set_name": pattern_set_name,
            }

        @builtins.property
        def log_patterns(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogPatternProperty", _IResolvable_da3f097b]]]:
            '''A list of objects that define the log patterns that belong to ``LogPatternSet`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html#cfn-applicationinsights-application-logpatternset-logpatterns
            '''
            result = self._values.get("log_patterns")
            assert result is not None, "Required property 'log_patterns' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogPatternProperty", _IResolvable_da3f097b]]], result)

        @builtins.property
        def pattern_set_name(self) -> builtins.str:
            '''The name of the log pattern.

            A log pattern name can contain up to 30 characters, and it cannot be empty. The characters can be Unicode letters, digits, or one of the following symbols: period, dash, underscore.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html#cfn-applicationinsights-application-logpatternset-patternsetname
            '''
            result = self._values.get("pattern_set_name")
            assert result is not None, "Required property 'pattern_set_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogPatternSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.LogProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_type": "logType",
            "encoding": "encoding",
            "log_group_name": "logGroupName",
            "log_path": "logPath",
            "pattern_set": "patternSet",
        },
    )
    class LogProperty:
        def __init__(
            self,
            *,
            log_type: builtins.str,
            encoding: typing.Optional[builtins.str] = None,
            log_group_name: typing.Optional[builtins.str] = None,
            log_path: typing.Optional[builtins.str] = None,
            pattern_set: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``AWS::ApplicationInsights::Application Log`` property type specifies a log to monitor for the component.

            :param log_type: The log type decides the log patterns against which Application Insights analyzes the log. The log type is selected from the following: ``SQL_SERVER`` , ``MYSQL`` , ``MYSQL_SLOW_QUERY`` , ``POSTGRESQL`` , ``ORACLE_ALERT`` , ``ORACLE_LISTENER`` , ``IIS`` , ``APPLICATION`` , ``WINDOWS_EVENTS`` , ``WINDOWS_EVENTS_ACTIVE_DIRECTORY`` , ``WINDOWS_EVENTS_DNS`` , ``WINDOWS_EVENTS_IIS`` , ``WINDOWS_EVENTS_SHAREPOINT`` , ``SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP`` , ``SQL_SERVER_FAILOVER_CLUSTER_INSTANCE`` , ``STEP_FUNCTION`` , ``API_GATEWAY_ACCESS`` , ``API_GATEWAY_EXECUTION`` , ``SAP_HANA_LOGS`` , ``SAP_HANA_TRACE`` , ``SAP_HANA_HIGH_AVAILABILITY`` , and ``DEFAULT`` .
            :param encoding: The type of encoding of the logs to be monitored. The specified encoding should be included in the list of CloudWatch agent supported encodings. If not provided, CloudWatch Application Insights uses the default encoding type for the log type: - ``APPLICATION/DEFAULT`` : utf-8 encoding - ``SQL_SERVER`` : utf-16 encoding - ``IIS`` : ascii encoding
            :param log_group_name: The CloudWatch log group name to be associated with the monitored log.
            :param log_path: The path of the logs to be monitored. The log path must be an absolute Windows or Linux system file path. For more information, see `CloudWatch Agent Configuration File: Logs Section <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html#CloudWatch-Agent-Configuration-File-Logssection>`_ .
            :param pattern_set: The log pattern set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                log_property = applicationinsights.CfnApplication.LogProperty(
                    log_type="logType",
                
                    # the properties below are optional
                    encoding="encoding",
                    log_group_name="logGroupName",
                    log_path="logPath",
                    pattern_set="patternSet"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.LogProperty.__init__)
                check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
                check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
                check_type(argname="argument log_path", value=log_path, expected_type=type_hints["log_path"])
                check_type(argname="argument pattern_set", value=pattern_set, expected_type=type_hints["pattern_set"])
            self._values: typing.Dict[str, typing.Any] = {
                "log_type": log_type,
            }
            if encoding is not None:
                self._values["encoding"] = encoding
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name
            if log_path is not None:
                self._values["log_path"] = log_path
            if pattern_set is not None:
                self._values["pattern_set"] = pattern_set

        @builtins.property
        def log_type(self) -> builtins.str:
            '''The log type decides the log patterns against which Application Insights analyzes the log.

            The log type is selected from the following: ``SQL_SERVER`` , ``MYSQL`` , ``MYSQL_SLOW_QUERY`` , ``POSTGRESQL`` , ``ORACLE_ALERT`` , ``ORACLE_LISTENER`` , ``IIS`` , ``APPLICATION`` , ``WINDOWS_EVENTS`` , ``WINDOWS_EVENTS_ACTIVE_DIRECTORY`` , ``WINDOWS_EVENTS_DNS`` , ``WINDOWS_EVENTS_IIS`` , ``WINDOWS_EVENTS_SHAREPOINT`` , ``SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP`` , ``SQL_SERVER_FAILOVER_CLUSTER_INSTANCE`` , ``STEP_FUNCTION`` , ``API_GATEWAY_ACCESS`` , ``API_GATEWAY_EXECUTION`` , ``SAP_HANA_LOGS`` , ``SAP_HANA_TRACE`` , ``SAP_HANA_HIGH_AVAILABILITY`` , and ``DEFAULT`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-logtype
            '''
            result = self._values.get("log_type")
            assert result is not None, "Required property 'log_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def encoding(self) -> typing.Optional[builtins.str]:
            '''The type of encoding of the logs to be monitored.

            The specified encoding should be included in the list of CloudWatch agent supported encodings. If not provided, CloudWatch Application Insights uses the default encoding type for the log type:

            - ``APPLICATION/DEFAULT`` : utf-8 encoding
            - ``SQL_SERVER`` : utf-16 encoding
            - ``IIS`` : ascii encoding

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-encoding
            '''
            result = self._values.get("encoding")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''The CloudWatch log group name to be associated with the monitored log.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_path(self) -> typing.Optional[builtins.str]:
            '''The path of the logs to be monitored.

            The log path must be an absolute Windows or Linux system file path. For more information, see `CloudWatch Agent Configuration File: Logs Section <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html#CloudWatch-Agent-Configuration-File-Logssection>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-logpath
            '''
            result = self._values.get("log_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pattern_set(self) -> typing.Optional[builtins.str]:
            '''The log pattern set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-patternset
            '''
            result = self._values.get("pattern_set")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alarm_metrics": "alarmMetrics",
            "logs": "logs",
            "windows_events": "windowsEvents",
        },
    )
    class SubComponentConfigurationDetailsProperty:
        def __init__(
            self,
            *,
            alarm_metrics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnApplication.AlarmMetricProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnApplication.LogProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
            windows_events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnApplication.WindowsEventProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''The ``AWS::ApplicationInsights::Application SubComponentConfigurationDetails`` property type specifies the configuration settings of the sub-components.

            :param alarm_metrics: A list of metrics to monitor for the component. All component types can use ``AlarmMetrics`` .
            :param logs: A list of logs to monitor for the component. Only Amazon EC2 instances can use ``Logs`` .
            :param windows_events: A list of Windows Events to monitor for the component. Only Amazon EC2 instances running on Windows can use ``WindowsEvents`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                sub_component_configuration_details_property = applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                    alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                        alarm_metric_name="alarmMetricName"
                    )],
                    logs=[applicationinsights.CfnApplication.LogProperty(
                        log_type="logType",
                
                        # the properties below are optional
                        encoding="encoding",
                        log_group_name="logGroupName",
                        log_path="logPath",
                        pattern_set="patternSet"
                    )],
                    windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                        event_levels=["eventLevels"],
                        event_name="eventName",
                        log_group_name="logGroupName",
                
                        # the properties below are optional
                        pattern_set="patternSet"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.SubComponentConfigurationDetailsProperty.__init__)
                check_type(argname="argument alarm_metrics", value=alarm_metrics, expected_type=type_hints["alarm_metrics"])
                check_type(argname="argument logs", value=logs, expected_type=type_hints["logs"])
                check_type(argname="argument windows_events", value=windows_events, expected_type=type_hints["windows_events"])
            self._values: typing.Dict[str, typing.Any] = {}
            if alarm_metrics is not None:
                self._values["alarm_metrics"] = alarm_metrics
            if logs is not None:
                self._values["logs"] = logs
            if windows_events is not None:
                self._values["windows_events"] = windows_events

        @builtins.property
        def alarm_metrics(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.AlarmMetricProperty", _IResolvable_da3f097b]]]]:
            '''A list of metrics to monitor for the component.

            All component types can use ``AlarmMetrics`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html#cfn-applicationinsights-application-subcomponentconfigurationdetails-alarmmetrics
            '''
            result = self._values.get("alarm_metrics")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.AlarmMetricProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def logs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogProperty", _IResolvable_da3f097b]]]]:
            '''A list of logs to monitor for the component.

            Only Amazon EC2 instances can use ``Logs`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html#cfn-applicationinsights-application-subcomponentconfigurationdetails-logs
            '''
            result = self._values.get("logs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.LogProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def windows_events(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.WindowsEventProperty", _IResolvable_da3f097b]]]]:
            '''A list of Windows Events to monitor for the component.

            Only Amazon EC2 instances running on Windows can use ``WindowsEvents`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html#cfn-applicationinsights-application-subcomponentconfigurationdetails-windowsevents
            '''
            result = self._values.get("windows_events")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnApplication.WindowsEventProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubComponentConfigurationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "sub_component_configuration_details": "subComponentConfigurationDetails",
            "sub_component_type": "subComponentType",
        },
    )
    class SubComponentTypeConfigurationProperty:
        def __init__(
            self,
            *,
            sub_component_configuration_details: typing.Union[typing.Union["CfnApplication.SubComponentConfigurationDetailsProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b],
            sub_component_type: builtins.str,
        ) -> None:
            '''The ``AWS::ApplicationInsights::Application SubComponentTypeConfiguration`` property type specifies the sub-component configurations for a component.

            :param sub_component_configuration_details: The configuration settings of the sub-components.
            :param sub_component_type: The sub-component type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                sub_component_type_configuration_property = applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                    sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                        alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                            alarm_metric_name="alarmMetricName"
                        )],
                        logs=[applicationinsights.CfnApplication.LogProperty(
                            log_type="logType",
                
                            # the properties below are optional
                            encoding="encoding",
                            log_group_name="logGroupName",
                            log_path="logPath",
                            pattern_set="patternSet"
                        )],
                        windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                            event_levels=["eventLevels"],
                            event_name="eventName",
                            log_group_name="logGroupName",
                
                            # the properties below are optional
                            pattern_set="patternSet"
                        )]
                    ),
                    sub_component_type="subComponentType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.SubComponentTypeConfigurationProperty.__init__)
                check_type(argname="argument sub_component_configuration_details", value=sub_component_configuration_details, expected_type=type_hints["sub_component_configuration_details"])
                check_type(argname="argument sub_component_type", value=sub_component_type, expected_type=type_hints["sub_component_type"])
            self._values: typing.Dict[str, typing.Any] = {
                "sub_component_configuration_details": sub_component_configuration_details,
                "sub_component_type": sub_component_type,
            }

        @builtins.property
        def sub_component_configuration_details(
            self,
        ) -> typing.Union["CfnApplication.SubComponentConfigurationDetailsProperty", _IResolvable_da3f097b]:
            '''The configuration settings of the sub-components.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html#cfn-applicationinsights-application-subcomponenttypeconfiguration-subcomponentconfigurationdetails
            '''
            result = self._values.get("sub_component_configuration_details")
            assert result is not None, "Required property 'sub_component_configuration_details' is missing"
            return typing.cast(typing.Union["CfnApplication.SubComponentConfigurationDetailsProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def sub_component_type(self) -> builtins.str:
            '''The sub-component type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html#cfn-applicationinsights-application-subcomponenttypeconfiguration-subcomponenttype
            '''
            result = self._values.get("sub_component_type")
            assert result is not None, "Required property 'sub_component_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubComponentTypeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplication.WindowsEventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "event_levels": "eventLevels",
            "event_name": "eventName",
            "log_group_name": "logGroupName",
            "pattern_set": "patternSet",
        },
    )
    class WindowsEventProperty:
        def __init__(
            self,
            *,
            event_levels: typing.Sequence[builtins.str],
            event_name: builtins.str,
            log_group_name: builtins.str,
            pattern_set: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``AWS::ApplicationInsights::Application WindowsEvent`` property type specifies a Windows Event to monitor for the component.

            :param event_levels: The levels of event to log. You must specify each level to log. Possible values include ``INFORMATION`` , ``WARNING`` , ``ERROR`` , ``CRITICAL`` , and ``VERBOSE`` . This field is required for each type of Windows Event to log.
            :param event_name: The type of Windows Events to log, equivalent to the Windows Event log channel name. For example, System, Security, CustomEventName, and so on. This field is required for each type of Windows event to log.
            :param log_group_name: The CloudWatch log group name to be associated with the monitored log.
            :param pattern_set: The log pattern set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationinsights as applicationinsights
                
                windows_event_property = applicationinsights.CfnApplication.WindowsEventProperty(
                    event_levels=["eventLevels"],
                    event_name="eventName",
                    log_group_name="logGroupName",
                
                    # the properties below are optional
                    pattern_set="patternSet"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnApplication.WindowsEventProperty.__init__)
                check_type(argname="argument event_levels", value=event_levels, expected_type=type_hints["event_levels"])
                check_type(argname="argument event_name", value=event_name, expected_type=type_hints["event_name"])
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
                check_type(argname="argument pattern_set", value=pattern_set, expected_type=type_hints["pattern_set"])
            self._values: typing.Dict[str, typing.Any] = {
                "event_levels": event_levels,
                "event_name": event_name,
                "log_group_name": log_group_name,
            }
            if pattern_set is not None:
                self._values["pattern_set"] = pattern_set

        @builtins.property
        def event_levels(self) -> typing.List[builtins.str]:
            '''The levels of event to log.

            You must specify each level to log. Possible values include ``INFORMATION`` , ``WARNING`` , ``ERROR`` , ``CRITICAL`` , and ``VERBOSE`` . This field is required for each type of Windows Event to log.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-eventlevels
            '''
            result = self._values.get("event_levels")
            assert result is not None, "Required property 'event_levels' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def event_name(self) -> builtins.str:
            '''The type of Windows Events to log, equivalent to the Windows Event log channel name.

            For example, System, Security, CustomEventName, and so on. This field is required for each type of Windows event to log.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-eventname
            '''
            result = self._values.get("event_name")
            assert result is not None, "Required property 'event_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_group_name(self) -> builtins.str:
            '''The CloudWatch log group name to be associated with the monitored log.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-loggroupname
            '''
            result = self._values.get("log_group_name")
            assert result is not None, "Required property 'log_group_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def pattern_set(self) -> typing.Optional[builtins.str]:
            '''The log pattern set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-patternset
            '''
            result = self._values.get("pattern_set")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WindowsEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationinsights.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "resource_group_name": "resourceGroupName",
        "auto_configuration_enabled": "autoConfigurationEnabled",
        "component_monitoring_settings": "componentMonitoringSettings",
        "custom_components": "customComponents",
        "cwe_monitor_enabled": "cweMonitorEnabled",
        "grouping_type": "groupingType",
        "log_pattern_sets": "logPatternSets",
        "ops_center_enabled": "opsCenterEnabled",
        "ops_item_sns_topic_arn": "opsItemSnsTopicArn",
        "tags": "tags",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        resource_group_name: builtins.str,
        auto_configuration_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        component_monitoring_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnApplication.ComponentMonitoringSettingProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        custom_components: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnApplication.CustomComponentProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        cwe_monitor_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        grouping_type: typing.Optional[builtins.str] = None,
        log_pattern_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnApplication.LogPatternSetProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        ops_center_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ops_item_sns_topic_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param resource_group_name: The name of the resource group used for the application.
        :param auto_configuration_enabled: If set to ``true`` , the application components will be configured with the monitoring configuration recommended by Application Insights.
        :param component_monitoring_settings: The monitoring settings of the components.
        :param custom_components: Describes a custom component by grouping similar standalone instances to monitor.
        :param cwe_monitor_enabled: Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as ``instance terminated`` , ``failed deployment`` , and others.
        :param grouping_type: ``AWS::ApplicationInsights::Application.GroupingType``.
        :param log_pattern_sets: The log pattern sets.
        :param ops_center_enabled: Indicates whether Application Insights will create OpsItems for any problem that is detected by Application Insights for an application.
        :param ops_item_sns_topic_arn: The SNS topic provided to Application Insights that is associated with the created OpsItems to receive SNS notifications for opsItem updates.
        :param tags: An array of ``Tags`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_applicationinsights as applicationinsights
            
            cfn_application_props = applicationinsights.CfnApplicationProps(
                resource_group_name="resourceGroupName",
            
                # the properties below are optional
                auto_configuration_enabled=False,
                component_monitoring_settings=[applicationinsights.CfnApplication.ComponentMonitoringSettingProperty(
                    component_configuration_mode="componentConfigurationMode",
                    tier="tier",
            
                    # the properties below are optional
                    component_arn="componentArn",
                    component_name="componentName",
                    custom_component_configuration=applicationinsights.CfnApplication.ComponentConfigurationProperty(
                        configuration_details=applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                            alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                alarm_metric_name="alarmMetricName"
                            )],
                            alarms=[applicationinsights.CfnApplication.AlarmProperty(
                                alarm_name="alarmName",
            
                                # the properties below are optional
                                severity="severity"
                            )],
                            ha_cluster_prometheus_exporter=applicationinsights.CfnApplication.HAClusterPrometheusExporterProperty(
                                prometheus_port="prometheusPort"
                            ),
                            hana_prometheus_exporter=applicationinsights.CfnApplication.HANAPrometheusExporterProperty(
                                agree_to_install_hanadb_client=False,
                                hana_port="hanaPort",
                                hana_secret_name="hanaSecretName",
                                hanasid="hanasid",
            
                                # the properties below are optional
                                prometheus_port="prometheusPort"
                            ),
                            jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                                host_port="hostPort",
                                jmxurl="jmxurl",
                                prometheus_port="prometheusPort"
                            ),
                            logs=[applicationinsights.CfnApplication.LogProperty(
                                log_type="logType",
            
                                # the properties below are optional
                                encoding="encoding",
                                log_group_name="logGroupName",
                                log_path="logPath",
                                pattern_set="patternSet"
                            )],
                            windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                event_levels=["eventLevels"],
                                event_name="eventName",
                                log_group_name="logGroupName",
            
                                # the properties below are optional
                                pattern_set="patternSet"
                            )]
                        ),
                        sub_component_type_configurations=[applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                            sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                                alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                    alarm_metric_name="alarmMetricName"
                                )],
                                logs=[applicationinsights.CfnApplication.LogProperty(
                                    log_type="logType",
            
                                    # the properties below are optional
                                    encoding="encoding",
                                    log_group_name="logGroupName",
                                    log_path="logPath",
                                    pattern_set="patternSet"
                                )],
                                windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                    event_levels=["eventLevels"],
                                    event_name="eventName",
                                    log_group_name="logGroupName",
            
                                    # the properties below are optional
                                    pattern_set="patternSet"
                                )]
                            ),
                            sub_component_type="subComponentType"
                        )]
                    ),
                    default_overwrite_component_configuration=applicationinsights.CfnApplication.ComponentConfigurationProperty(
                        configuration_details=applicationinsights.CfnApplication.ConfigurationDetailsProperty(
                            alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                alarm_metric_name="alarmMetricName"
                            )],
                            alarms=[applicationinsights.CfnApplication.AlarmProperty(
                                alarm_name="alarmName",
            
                                # the properties below are optional
                                severity="severity"
                            )],
                            ha_cluster_prometheus_exporter=applicationinsights.CfnApplication.HAClusterPrometheusExporterProperty(
                                prometheus_port="prometheusPort"
                            ),
                            hana_prometheus_exporter=applicationinsights.CfnApplication.HANAPrometheusExporterProperty(
                                agree_to_install_hanadb_client=False,
                                hana_port="hanaPort",
                                hana_secret_name="hanaSecretName",
                                hanasid="hanasid",
            
                                # the properties below are optional
                                prometheus_port="prometheusPort"
                            ),
                            jmx_prometheus_exporter=applicationinsights.CfnApplication.JMXPrometheusExporterProperty(
                                host_port="hostPort",
                                jmxurl="jmxurl",
                                prometheus_port="prometheusPort"
                            ),
                            logs=[applicationinsights.CfnApplication.LogProperty(
                                log_type="logType",
            
                                # the properties below are optional
                                encoding="encoding",
                                log_group_name="logGroupName",
                                log_path="logPath",
                                pattern_set="patternSet"
                            )],
                            windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                event_levels=["eventLevels"],
                                event_name="eventName",
                                log_group_name="logGroupName",
            
                                # the properties below are optional
                                pattern_set="patternSet"
                            )]
                        ),
                        sub_component_type_configurations=[applicationinsights.CfnApplication.SubComponentTypeConfigurationProperty(
                            sub_component_configuration_details=applicationinsights.CfnApplication.SubComponentConfigurationDetailsProperty(
                                alarm_metrics=[applicationinsights.CfnApplication.AlarmMetricProperty(
                                    alarm_metric_name="alarmMetricName"
                                )],
                                logs=[applicationinsights.CfnApplication.LogProperty(
                                    log_type="logType",
            
                                    # the properties below are optional
                                    encoding="encoding",
                                    log_group_name="logGroupName",
                                    log_path="logPath",
                                    pattern_set="patternSet"
                                )],
                                windows_events=[applicationinsights.CfnApplication.WindowsEventProperty(
                                    event_levels=["eventLevels"],
                                    event_name="eventName",
                                    log_group_name="logGroupName",
            
                                    # the properties below are optional
                                    pattern_set="patternSet"
                                )]
                            ),
                            sub_component_type="subComponentType"
                        )]
                    )
                )],
                custom_components=[applicationinsights.CfnApplication.CustomComponentProperty(
                    component_name="componentName",
                    resource_list=["resourceList"]
                )],
                cwe_monitor_enabled=False,
                grouping_type="groupingType",
                log_pattern_sets=[applicationinsights.CfnApplication.LogPatternSetProperty(
                    log_patterns=[applicationinsights.CfnApplication.LogPatternProperty(
                        pattern="pattern",
                        pattern_name="patternName",
                        rank=123
                    )],
                    pattern_set_name="patternSetName"
                )],
                ops_center_enabled=False,
                ops_item_sns_topic_arn="opsItemSnsTopicArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnApplicationProps.__init__)
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument auto_configuration_enabled", value=auto_configuration_enabled, expected_type=type_hints["auto_configuration_enabled"])
            check_type(argname="argument component_monitoring_settings", value=component_monitoring_settings, expected_type=type_hints["component_monitoring_settings"])
            check_type(argname="argument custom_components", value=custom_components, expected_type=type_hints["custom_components"])
            check_type(argname="argument cwe_monitor_enabled", value=cwe_monitor_enabled, expected_type=type_hints["cwe_monitor_enabled"])
            check_type(argname="argument grouping_type", value=grouping_type, expected_type=type_hints["grouping_type"])
            check_type(argname="argument log_pattern_sets", value=log_pattern_sets, expected_type=type_hints["log_pattern_sets"])
            check_type(argname="argument ops_center_enabled", value=ops_center_enabled, expected_type=type_hints["ops_center_enabled"])
            check_type(argname="argument ops_item_sns_topic_arn", value=ops_item_sns_topic_arn, expected_type=type_hints["ops_item_sns_topic_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource_group_name": resource_group_name,
        }
        if auto_configuration_enabled is not None:
            self._values["auto_configuration_enabled"] = auto_configuration_enabled
        if component_monitoring_settings is not None:
            self._values["component_monitoring_settings"] = component_monitoring_settings
        if custom_components is not None:
            self._values["custom_components"] = custom_components
        if cwe_monitor_enabled is not None:
            self._values["cwe_monitor_enabled"] = cwe_monitor_enabled
        if grouping_type is not None:
            self._values["grouping_type"] = grouping_type
        if log_pattern_sets is not None:
            self._values["log_pattern_sets"] = log_pattern_sets
        if ops_center_enabled is not None:
            self._values["ops_center_enabled"] = ops_center_enabled
        if ops_item_sns_topic_arn is not None:
            self._values["ops_item_sns_topic_arn"] = ops_item_sns_topic_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''The name of the resource group used for the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-resourcegroupname
        '''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_configuration_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If set to ``true`` , the application components will be configured with the monitoring configuration recommended by Application Insights.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-autoconfigurationenabled
        '''
        result = self._values.get("auto_configuration_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def component_monitoring_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnApplication.ComponentMonitoringSettingProperty, _IResolvable_da3f097b]]]]:
        '''The monitoring settings of the components.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-componentmonitoringsettings
        '''
        result = self._values.get("component_monitoring_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnApplication.ComponentMonitoringSettingProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def custom_components(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnApplication.CustomComponentProperty, _IResolvable_da3f097b]]]]:
        '''Describes a custom component by grouping similar standalone instances to monitor.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-customcomponents
        '''
        result = self._values.get("custom_components")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnApplication.CustomComponentProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def cwe_monitor_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as ``instance terminated`` , ``failed deployment`` , and others.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-cwemonitorenabled
        '''
        result = self._values.get("cwe_monitor_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def grouping_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::ApplicationInsights::Application.GroupingType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-groupingtype
        '''
        result = self._values.get("grouping_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_pattern_sets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnApplication.LogPatternSetProperty, _IResolvable_da3f097b]]]]:
        '''The log pattern sets.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-logpatternsets
        '''
        result = self._values.get("log_pattern_sets")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnApplication.LogPatternSetProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def ops_center_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether Application Insights will create OpsItems for any problem that is detected by Application Insights for an application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-opscenterenabled
        '''
        result = self._values.get("ops_center_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def ops_item_sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The SNS topic provided to Application Insights that is associated with the created OpsItems to receive SNS notifications for opsItem updates.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-opsitemsnstopicarn
        '''
        result = self._values.get("ops_item_sns_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of ``Tags`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
]

publication.publish()
