# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CseCustomInsightArgs', 'CseCustomInsight']

@pulumi.input_type
class CseCustomInsightArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 enabled: pulumi.Input[bool],
                 ordered: pulumi.Input[bool],
                 severity: pulumi.Input[str],
                 tags: pulumi.Input[Sequence[pulumi.Input[str]]],
                 name: Optional[pulumi.Input[str]] = None,
                 rule_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 signal_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a CseCustomInsight resource.
        :param pulumi.Input[str] description: The description of the generated Insights
        :param pulumi.Input[bool] enabled: Whether the Custom Insight should generate Insights
        :param pulumi.Input[bool] ordered: Whether the signals matching the rule IDs/signal names must be in the same chronological order as they are listed in the Custom Insight
        :param pulumi.Input[str] severity: The severity of the generated Insights (HIGH, MEDIUM, or LOW)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the generated Insights
        :param pulumi.Input[str] name: The name of the Custom Insight and the generated Insights
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rule_ids: The Rule IDs to match to generate an Insight (exactly one of rule_ids or signal_names must be specified)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] signal_names: The Signal names to match to generate an Insight (exactly one of rule_ids or signal_names must be specified)
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "ordered", ordered)
        pulumi.set(__self__, "severity", severity)
        pulumi.set(__self__, "tags", tags)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rule_ids is not None:
            pulumi.set(__self__, "rule_ids", rule_ids)
        if signal_names is not None:
            pulumi.set(__self__, "signal_names", signal_names)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The description of the generated Insights
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Whether the Custom Insight should generate Insights
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def ordered(self) -> pulumi.Input[bool]:
        """
        Whether the signals matching the rule IDs/signal names must be in the same chronological order as they are listed in the Custom Insight
        """
        return pulumi.get(self, "ordered")

    @ordered.setter
    def ordered(self, value: pulumi.Input[bool]):
        pulumi.set(self, "ordered", value)

    @property
    @pulumi.getter
    def severity(self) -> pulumi.Input[str]:
        """
        The severity of the generated Insights (HIGH, MEDIUM, or LOW)
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: pulumi.Input[str]):
        pulumi.set(self, "severity", value)

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The tags of the generated Insights
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Custom Insight and the generated Insights
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="ruleIds")
    def rule_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The Rule IDs to match to generate an Insight (exactly one of rule_ids or signal_names must be specified)
        """
        return pulumi.get(self, "rule_ids")

    @rule_ids.setter
    def rule_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "rule_ids", value)

    @property
    @pulumi.getter(name="signalNames")
    def signal_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The Signal names to match to generate an Insight (exactly one of rule_ids or signal_names must be specified)
        """
        return pulumi.get(self, "signal_names")

    @signal_names.setter
    def signal_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "signal_names", value)


@pulumi.input_type
class _CseCustomInsightState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ordered: Optional[pulumi.Input[bool]] = None,
                 rule_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 severity: Optional[pulumi.Input[str]] = None,
                 signal_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering CseCustomInsight resources.
        :param pulumi.Input[str] description: The description of the generated Insights
        :param pulumi.Input[bool] enabled: Whether the Custom Insight should generate Insights
        :param pulumi.Input[str] name: The name of the Custom Insight and the generated Insights
        :param pulumi.Input[bool] ordered: Whether the signals matching the rule IDs/signal names must be in the same chronological order as they are listed in the Custom Insight
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rule_ids: The Rule IDs to match to generate an Insight (exactly one of rule_ids or signal_names must be specified)
        :param pulumi.Input[str] severity: The severity of the generated Insights (HIGH, MEDIUM, or LOW)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] signal_names: The Signal names to match to generate an Insight (exactly one of rule_ids or signal_names must be specified)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the generated Insights
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ordered is not None:
            pulumi.set(__self__, "ordered", ordered)
        if rule_ids is not None:
            pulumi.set(__self__, "rule_ids", rule_ids)
        if severity is not None:
            pulumi.set(__self__, "severity", severity)
        if signal_names is not None:
            pulumi.set(__self__, "signal_names", signal_names)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the generated Insights
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the Custom Insight should generate Insights
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Custom Insight and the generated Insights
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def ordered(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the signals matching the rule IDs/signal names must be in the same chronological order as they are listed in the Custom Insight
        """
        return pulumi.get(self, "ordered")

    @ordered.setter
    def ordered(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ordered", value)

    @property
    @pulumi.getter(name="ruleIds")
    def rule_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The Rule IDs to match to generate an Insight (exactly one of rule_ids or signal_names must be specified)
        """
        return pulumi.get(self, "rule_ids")

    @rule_ids.setter
    def rule_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "rule_ids", value)

    @property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[str]]:
        """
        The severity of the generated Insights (HIGH, MEDIUM, or LOW)
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "severity", value)

    @property
    @pulumi.getter(name="signalNames")
    def signal_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The Signal names to match to generate an Insight (exactly one of rule_ids or signal_names must be specified)
        """
        return pulumi.get(self, "signal_names")

    @signal_names.setter
    def signal_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "signal_names", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The tags of the generated Insights
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class CseCustomInsight(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ordered: Optional[pulumi.Input[bool]] = None,
                 rule_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 severity: Optional[pulumi.Input[str]] = None,
                 signal_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a Sumo Logic CSE Custom Insight.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        custom_insight = sumologic.CseCustomInsight("customInsight",
            description="Insight description",
            enabled=True,
            ordered=True,
            rule_ids=[
                "MATCH-S00001",
                "THRESHOLD-U00005",
            ],
            severity="HIGH",
            signal_names=[
                "Some Signal Name",
                "Wildcard Signal Name *",
            ],
            tags=["_mitreAttackTactic:TA0009"])
        ```

        ## Import

        Custom Insights can be imported using the field id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/cseCustomInsight:CseCustomInsight custom_insight id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the generated Insights
        :param pulumi.Input[bool] enabled: Whether the Custom Insight should generate Insights
        :param pulumi.Input[str] name: The name of the Custom Insight and the generated Insights
        :param pulumi.Input[bool] ordered: Whether the signals matching the rule IDs/signal names must be in the same chronological order as they are listed in the Custom Insight
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rule_ids: The Rule IDs to match to generate an Insight (exactly one of rule_ids or signal_names must be specified)
        :param pulumi.Input[str] severity: The severity of the generated Insights (HIGH, MEDIUM, or LOW)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] signal_names: The Signal names to match to generate an Insight (exactly one of rule_ids or signal_names must be specified)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the generated Insights
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CseCustomInsightArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Sumo Logic CSE Custom Insight.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        custom_insight = sumologic.CseCustomInsight("customInsight",
            description="Insight description",
            enabled=True,
            ordered=True,
            rule_ids=[
                "MATCH-S00001",
                "THRESHOLD-U00005",
            ],
            severity="HIGH",
            signal_names=[
                "Some Signal Name",
                "Wildcard Signal Name *",
            ],
            tags=["_mitreAttackTactic:TA0009"])
        ```

        ## Import

        Custom Insights can be imported using the field id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/cseCustomInsight:CseCustomInsight custom_insight id
        ```

        :param str resource_name: The name of the resource.
        :param CseCustomInsightArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CseCustomInsightArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ordered: Optional[pulumi.Input[bool]] = None,
                 rule_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 severity: Optional[pulumi.Input[str]] = None,
                 signal_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CseCustomInsightArgs.__new__(CseCustomInsightArgs)

            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["name"] = name
            if ordered is None and not opts.urn:
                raise TypeError("Missing required property 'ordered'")
            __props__.__dict__["ordered"] = ordered
            __props__.__dict__["rule_ids"] = rule_ids
            if severity is None and not opts.urn:
                raise TypeError("Missing required property 'severity'")
            __props__.__dict__["severity"] = severity
            __props__.__dict__["signal_names"] = signal_names
            if tags is None and not opts.urn:
                raise TypeError("Missing required property 'tags'")
            __props__.__dict__["tags"] = tags
        super(CseCustomInsight, __self__).__init__(
            'sumologic:index/cseCustomInsight:CseCustomInsight',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            ordered: Optional[pulumi.Input[bool]] = None,
            rule_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            severity: Optional[pulumi.Input[str]] = None,
            signal_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'CseCustomInsight':
        """
        Get an existing CseCustomInsight resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the generated Insights
        :param pulumi.Input[bool] enabled: Whether the Custom Insight should generate Insights
        :param pulumi.Input[str] name: The name of the Custom Insight and the generated Insights
        :param pulumi.Input[bool] ordered: Whether the signals matching the rule IDs/signal names must be in the same chronological order as they are listed in the Custom Insight
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rule_ids: The Rule IDs to match to generate an Insight (exactly one of rule_ids or signal_names must be specified)
        :param pulumi.Input[str] severity: The severity of the generated Insights (HIGH, MEDIUM, or LOW)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] signal_names: The Signal names to match to generate an Insight (exactly one of rule_ids or signal_names must be specified)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the generated Insights
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CseCustomInsightState.__new__(_CseCustomInsightState)

        __props__.__dict__["description"] = description
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["name"] = name
        __props__.__dict__["ordered"] = ordered
        __props__.__dict__["rule_ids"] = rule_ids
        __props__.__dict__["severity"] = severity
        __props__.__dict__["signal_names"] = signal_names
        __props__.__dict__["tags"] = tags
        return CseCustomInsight(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the generated Insights
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Whether the Custom Insight should generate Insights
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Custom Insight and the generated Insights
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def ordered(self) -> pulumi.Output[bool]:
        """
        Whether the signals matching the rule IDs/signal names must be in the same chronological order as they are listed in the Custom Insight
        """
        return pulumi.get(self, "ordered")

    @property
    @pulumi.getter(name="ruleIds")
    def rule_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The Rule IDs to match to generate an Insight (exactly one of rule_ids or signal_names must be specified)
        """
        return pulumi.get(self, "rule_ids")

    @property
    @pulumi.getter
    def severity(self) -> pulumi.Output[str]:
        """
        The severity of the generated Insights (HIGH, MEDIUM, or LOW)
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter(name="signalNames")
    def signal_names(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The Signal names to match to generate an Insight (exactly one of rule_ids or signal_names must be specified)
        """
        return pulumi.get(self, "signal_names")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[str]]:
        """
        The tags of the generated Insights
        """
        return pulumi.get(self, "tags")

