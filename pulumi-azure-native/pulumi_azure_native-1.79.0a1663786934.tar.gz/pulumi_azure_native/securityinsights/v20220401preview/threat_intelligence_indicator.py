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
from ._inputs import *

__all__ = ['ThreatIntelligenceIndicatorArgs', 'ThreatIntelligenceIndicator']

@pulumi.input_type
class ThreatIntelligenceIndicatorArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 confidence: Optional[pulumi.Input[int]] = None,
                 created: Optional[pulumi.Input[str]] = None,
                 created_by_ref: Optional[pulumi.Input[str]] = None,
                 defanged: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 extensions: Optional[Any] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 external_last_updated_time_utc: Optional[pulumi.Input[str]] = None,
                 external_references: Optional[pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceExternalReferenceArgs']]]] = None,
                 granular_markings: Optional[pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceGranularMarkingModelArgs']]]] = None,
                 indicator_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kill_chain_phases: Optional[pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceKillChainPhaseArgs']]]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 language: Optional[pulumi.Input[str]] = None,
                 last_updated_time_utc: Optional[pulumi.Input[str]] = None,
                 modified: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 object_marking_refs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 parsed_pattern: Optional[pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceParsedPatternArgs']]]] = None,
                 pattern: Optional[pulumi.Input[str]] = None,
                 pattern_type: Optional[pulumi.Input[str]] = None,
                 pattern_version: Optional[pulumi.Input[str]] = None,
                 revoked: Optional[pulumi.Input[bool]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 threat_intelligence_tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 threat_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 valid_from: Optional[pulumi.Input[str]] = None,
                 valid_until: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ThreatIntelligenceIndicator resource.
        :param pulumi.Input[str] kind: The kind of the threat intelligence entity
               Expected value is 'indicator'.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[int] confidence: Confidence of threat intelligence entity
        :param pulumi.Input[str] created: Created by
        :param pulumi.Input[str] created_by_ref: Created by reference of threat intelligence entity
        :param pulumi.Input[bool] defanged: Is threat intelligence entity defanged
        :param pulumi.Input[str] description: Description of a threat intelligence entity
        :param pulumi.Input[str] display_name: Display name of a threat intelligence entity
        :param Any extensions: Extensions map
        :param pulumi.Input[str] external_id: External ID of threat intelligence entity
        :param pulumi.Input[str] external_last_updated_time_utc: External last updated time in UTC
        :param pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceExternalReferenceArgs']]] external_references: External References
        :param pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceGranularMarkingModelArgs']]] granular_markings: Granular Markings
        :param pulumi.Input[Sequence[pulumi.Input[str]]] indicator_types: Indicator types of threat intelligence entities
        :param pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceKillChainPhaseArgs']]] kill_chain_phases: Kill chain phases
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: Labels  of threat intelligence entity
        :param pulumi.Input[str] language: Language of threat intelligence entity
        :param pulumi.Input[str] last_updated_time_utc: Last updated time in UTC
        :param pulumi.Input[str] modified: Modified by
        :param pulumi.Input[str] name: Threat intelligence indicator name field.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] object_marking_refs: Threat intelligence entity object marking references
        :param pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceParsedPatternArgs']]] parsed_pattern: Parsed patterns
        :param pulumi.Input[str] pattern: Pattern of a threat intelligence entity
        :param pulumi.Input[str] pattern_type: Pattern type of a threat intelligence entity
        :param pulumi.Input[str] pattern_version: Pattern version of a threat intelligence entity
        :param pulumi.Input[bool] revoked: Is threat intelligence entity revoked
        :param pulumi.Input[str] source: Source of a threat intelligence entity
        :param pulumi.Input[Sequence[pulumi.Input[str]]] threat_intelligence_tags: List of tags
        :param pulumi.Input[Sequence[pulumi.Input[str]]] threat_types: Threat types
        :param pulumi.Input[str] valid_from: Valid from
        :param pulumi.Input[str] valid_until: Valid until
        """
        pulumi.set(__self__, "kind", 'indicator')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if confidence is not None:
            pulumi.set(__self__, "confidence", confidence)
        if created is not None:
            pulumi.set(__self__, "created", created)
        if created_by_ref is not None:
            pulumi.set(__self__, "created_by_ref", created_by_ref)
        if defanged is not None:
            pulumi.set(__self__, "defanged", defanged)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if extensions is not None:
            pulumi.set(__self__, "extensions", extensions)
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if external_last_updated_time_utc is not None:
            pulumi.set(__self__, "external_last_updated_time_utc", external_last_updated_time_utc)
        if external_references is not None:
            pulumi.set(__self__, "external_references", external_references)
        if granular_markings is not None:
            pulumi.set(__self__, "granular_markings", granular_markings)
        if indicator_types is not None:
            pulumi.set(__self__, "indicator_types", indicator_types)
        if kill_chain_phases is not None:
            pulumi.set(__self__, "kill_chain_phases", kill_chain_phases)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if language is not None:
            pulumi.set(__self__, "language", language)
        if last_updated_time_utc is not None:
            pulumi.set(__self__, "last_updated_time_utc", last_updated_time_utc)
        if modified is not None:
            pulumi.set(__self__, "modified", modified)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if object_marking_refs is not None:
            pulumi.set(__self__, "object_marking_refs", object_marking_refs)
        if parsed_pattern is not None:
            pulumi.set(__self__, "parsed_pattern", parsed_pattern)
        if pattern is not None:
            pulumi.set(__self__, "pattern", pattern)
        if pattern_type is not None:
            pulumi.set(__self__, "pattern_type", pattern_type)
        if pattern_version is not None:
            pulumi.set(__self__, "pattern_version", pattern_version)
        if revoked is not None:
            pulumi.set(__self__, "revoked", revoked)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if threat_intelligence_tags is not None:
            pulumi.set(__self__, "threat_intelligence_tags", threat_intelligence_tags)
        if threat_types is not None:
            pulumi.set(__self__, "threat_types", threat_types)
        if valid_from is not None:
            pulumi.set(__self__, "valid_from", valid_from)
        if valid_until is not None:
            pulumi.set(__self__, "valid_until", valid_until)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The kind of the threat intelligence entity
        Expected value is 'indicator'.
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
    @pulumi.getter
    def confidence(self) -> Optional[pulumi.Input[int]]:
        """
        Confidence of threat intelligence entity
        """
        return pulumi.get(self, "confidence")

    @confidence.setter
    def confidence(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "confidence", value)

    @property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[str]]:
        """
        Created by
        """
        return pulumi.get(self, "created")

    @created.setter
    def created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created", value)

    @property
    @pulumi.getter(name="createdByRef")
    def created_by_ref(self) -> Optional[pulumi.Input[str]]:
        """
        Created by reference of threat intelligence entity
        """
        return pulumi.get(self, "created_by_ref")

    @created_by_ref.setter
    def created_by_ref(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by_ref", value)

    @property
    @pulumi.getter
    def defanged(self) -> Optional[pulumi.Input[bool]]:
        """
        Is threat intelligence entity defanged
        """
        return pulumi.get(self, "defanged")

    @defanged.setter
    def defanged(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "defanged", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of a threat intelligence entity
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of a threat intelligence entity
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def extensions(self) -> Optional[Any]:
        """
        Extensions map
        """
        return pulumi.get(self, "extensions")

    @extensions.setter
    def extensions(self, value: Optional[Any]):
        pulumi.set(self, "extensions", value)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[str]]:
        """
        External ID of threat intelligence entity
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter(name="externalLastUpdatedTimeUtc")
    def external_last_updated_time_utc(self) -> Optional[pulumi.Input[str]]:
        """
        External last updated time in UTC
        """
        return pulumi.get(self, "external_last_updated_time_utc")

    @external_last_updated_time_utc.setter
    def external_last_updated_time_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_last_updated_time_utc", value)

    @property
    @pulumi.getter(name="externalReferences")
    def external_references(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceExternalReferenceArgs']]]]:
        """
        External References
        """
        return pulumi.get(self, "external_references")

    @external_references.setter
    def external_references(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceExternalReferenceArgs']]]]):
        pulumi.set(self, "external_references", value)

    @property
    @pulumi.getter(name="granularMarkings")
    def granular_markings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceGranularMarkingModelArgs']]]]:
        """
        Granular Markings
        """
        return pulumi.get(self, "granular_markings")

    @granular_markings.setter
    def granular_markings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceGranularMarkingModelArgs']]]]):
        pulumi.set(self, "granular_markings", value)

    @property
    @pulumi.getter(name="indicatorTypes")
    def indicator_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Indicator types of threat intelligence entities
        """
        return pulumi.get(self, "indicator_types")

    @indicator_types.setter
    def indicator_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "indicator_types", value)

    @property
    @pulumi.getter(name="killChainPhases")
    def kill_chain_phases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceKillChainPhaseArgs']]]]:
        """
        Kill chain phases
        """
        return pulumi.get(self, "kill_chain_phases")

    @kill_chain_phases.setter
    def kill_chain_phases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceKillChainPhaseArgs']]]]):
        pulumi.set(self, "kill_chain_phases", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Labels  of threat intelligence entity
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def language(self) -> Optional[pulumi.Input[str]]:
        """
        Language of threat intelligence entity
        """
        return pulumi.get(self, "language")

    @language.setter
    def language(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "language", value)

    @property
    @pulumi.getter(name="lastUpdatedTimeUtc")
    def last_updated_time_utc(self) -> Optional[pulumi.Input[str]]:
        """
        Last updated time in UTC
        """
        return pulumi.get(self, "last_updated_time_utc")

    @last_updated_time_utc.setter
    def last_updated_time_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_updated_time_utc", value)

    @property
    @pulumi.getter
    def modified(self) -> Optional[pulumi.Input[str]]:
        """
        Modified by
        """
        return pulumi.get(self, "modified")

    @modified.setter
    def modified(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modified", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Threat intelligence indicator name field.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="objectMarkingRefs")
    def object_marking_refs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Threat intelligence entity object marking references
        """
        return pulumi.get(self, "object_marking_refs")

    @object_marking_refs.setter
    def object_marking_refs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "object_marking_refs", value)

    @property
    @pulumi.getter(name="parsedPattern")
    def parsed_pattern(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceParsedPatternArgs']]]]:
        """
        Parsed patterns
        """
        return pulumi.get(self, "parsed_pattern")

    @parsed_pattern.setter
    def parsed_pattern(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ThreatIntelligenceParsedPatternArgs']]]]):
        pulumi.set(self, "parsed_pattern", value)

    @property
    @pulumi.getter
    def pattern(self) -> Optional[pulumi.Input[str]]:
        """
        Pattern of a threat intelligence entity
        """
        return pulumi.get(self, "pattern")

    @pattern.setter
    def pattern(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pattern", value)

    @property
    @pulumi.getter(name="patternType")
    def pattern_type(self) -> Optional[pulumi.Input[str]]:
        """
        Pattern type of a threat intelligence entity
        """
        return pulumi.get(self, "pattern_type")

    @pattern_type.setter
    def pattern_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pattern_type", value)

    @property
    @pulumi.getter(name="patternVersion")
    def pattern_version(self) -> Optional[pulumi.Input[str]]:
        """
        Pattern version of a threat intelligence entity
        """
        return pulumi.get(self, "pattern_version")

    @pattern_version.setter
    def pattern_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pattern_version", value)

    @property
    @pulumi.getter
    def revoked(self) -> Optional[pulumi.Input[bool]]:
        """
        Is threat intelligence entity revoked
        """
        return pulumi.get(self, "revoked")

    @revoked.setter
    def revoked(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "revoked", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        Source of a threat intelligence entity
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="threatIntelligenceTags")
    def threat_intelligence_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of tags
        """
        return pulumi.get(self, "threat_intelligence_tags")

    @threat_intelligence_tags.setter
    def threat_intelligence_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "threat_intelligence_tags", value)

    @property
    @pulumi.getter(name="threatTypes")
    def threat_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Threat types
        """
        return pulumi.get(self, "threat_types")

    @threat_types.setter
    def threat_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "threat_types", value)

    @property
    @pulumi.getter(name="validFrom")
    def valid_from(self) -> Optional[pulumi.Input[str]]:
        """
        Valid from
        """
        return pulumi.get(self, "valid_from")

    @valid_from.setter
    def valid_from(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "valid_from", value)

    @property
    @pulumi.getter(name="validUntil")
    def valid_until(self) -> Optional[pulumi.Input[str]]:
        """
        Valid until
        """
        return pulumi.get(self, "valid_until")

    @valid_until.setter
    def valid_until(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "valid_until", value)


class ThreatIntelligenceIndicator(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 confidence: Optional[pulumi.Input[int]] = None,
                 created: Optional[pulumi.Input[str]] = None,
                 created_by_ref: Optional[pulumi.Input[str]] = None,
                 defanged: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 extensions: Optional[Any] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 external_last_updated_time_utc: Optional[pulumi.Input[str]] = None,
                 external_references: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThreatIntelligenceExternalReferenceArgs']]]]] = None,
                 granular_markings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThreatIntelligenceGranularMarkingModelArgs']]]]] = None,
                 indicator_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kill_chain_phases: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThreatIntelligenceKillChainPhaseArgs']]]]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 language: Optional[pulumi.Input[str]] = None,
                 last_updated_time_utc: Optional[pulumi.Input[str]] = None,
                 modified: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 object_marking_refs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 parsed_pattern: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThreatIntelligenceParsedPatternArgs']]]]] = None,
                 pattern: Optional[pulumi.Input[str]] = None,
                 pattern_type: Optional[pulumi.Input[str]] = None,
                 pattern_version: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 revoked: Optional[pulumi.Input[bool]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 threat_intelligence_tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 threat_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 valid_from: Optional[pulumi.Input[str]] = None,
                 valid_until: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Threat intelligence information object.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] confidence: Confidence of threat intelligence entity
        :param pulumi.Input[str] created: Created by
        :param pulumi.Input[str] created_by_ref: Created by reference of threat intelligence entity
        :param pulumi.Input[bool] defanged: Is threat intelligence entity defanged
        :param pulumi.Input[str] description: Description of a threat intelligence entity
        :param pulumi.Input[str] display_name: Display name of a threat intelligence entity
        :param Any extensions: Extensions map
        :param pulumi.Input[str] external_id: External ID of threat intelligence entity
        :param pulumi.Input[str] external_last_updated_time_utc: External last updated time in UTC
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThreatIntelligenceExternalReferenceArgs']]]] external_references: External References
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThreatIntelligenceGranularMarkingModelArgs']]]] granular_markings: Granular Markings
        :param pulumi.Input[Sequence[pulumi.Input[str]]] indicator_types: Indicator types of threat intelligence entities
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThreatIntelligenceKillChainPhaseArgs']]]] kill_chain_phases: Kill chain phases
        :param pulumi.Input[str] kind: The kind of the threat intelligence entity
               Expected value is 'indicator'.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: Labels  of threat intelligence entity
        :param pulumi.Input[str] language: Language of threat intelligence entity
        :param pulumi.Input[str] last_updated_time_utc: Last updated time in UTC
        :param pulumi.Input[str] modified: Modified by
        :param pulumi.Input[str] name: Threat intelligence indicator name field.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] object_marking_refs: Threat intelligence entity object marking references
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThreatIntelligenceParsedPatternArgs']]]] parsed_pattern: Parsed patterns
        :param pulumi.Input[str] pattern: Pattern of a threat intelligence entity
        :param pulumi.Input[str] pattern_type: Pattern type of a threat intelligence entity
        :param pulumi.Input[str] pattern_version: Pattern version of a threat intelligence entity
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[bool] revoked: Is threat intelligence entity revoked
        :param pulumi.Input[str] source: Source of a threat intelligence entity
        :param pulumi.Input[Sequence[pulumi.Input[str]]] threat_intelligence_tags: List of tags
        :param pulumi.Input[Sequence[pulumi.Input[str]]] threat_types: Threat types
        :param pulumi.Input[str] valid_from: Valid from
        :param pulumi.Input[str] valid_until: Valid until
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ThreatIntelligenceIndicatorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Threat intelligence information object.

        :param str resource_name: The name of the resource.
        :param ThreatIntelligenceIndicatorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ThreatIntelligenceIndicatorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 confidence: Optional[pulumi.Input[int]] = None,
                 created: Optional[pulumi.Input[str]] = None,
                 created_by_ref: Optional[pulumi.Input[str]] = None,
                 defanged: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 extensions: Optional[Any] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 external_last_updated_time_utc: Optional[pulumi.Input[str]] = None,
                 external_references: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThreatIntelligenceExternalReferenceArgs']]]]] = None,
                 granular_markings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThreatIntelligenceGranularMarkingModelArgs']]]]] = None,
                 indicator_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kill_chain_phases: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThreatIntelligenceKillChainPhaseArgs']]]]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 language: Optional[pulumi.Input[str]] = None,
                 last_updated_time_utc: Optional[pulumi.Input[str]] = None,
                 modified: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 object_marking_refs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 parsed_pattern: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ThreatIntelligenceParsedPatternArgs']]]]] = None,
                 pattern: Optional[pulumi.Input[str]] = None,
                 pattern_type: Optional[pulumi.Input[str]] = None,
                 pattern_version: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 revoked: Optional[pulumi.Input[bool]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 threat_intelligence_tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 threat_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 valid_from: Optional[pulumi.Input[str]] = None,
                 valid_until: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ThreatIntelligenceIndicatorArgs.__new__(ThreatIntelligenceIndicatorArgs)

            __props__.__dict__["confidence"] = confidence
            __props__.__dict__["created"] = created
            __props__.__dict__["created_by_ref"] = created_by_ref
            __props__.__dict__["defanged"] = defanged
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["extensions"] = extensions
            __props__.__dict__["external_id"] = external_id
            __props__.__dict__["external_last_updated_time_utc"] = external_last_updated_time_utc
            __props__.__dict__["external_references"] = external_references
            __props__.__dict__["granular_markings"] = granular_markings
            __props__.__dict__["indicator_types"] = indicator_types
            __props__.__dict__["kill_chain_phases"] = kill_chain_phases
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'indicator'
            __props__.__dict__["labels"] = labels
            __props__.__dict__["language"] = language
            __props__.__dict__["last_updated_time_utc"] = last_updated_time_utc
            __props__.__dict__["modified"] = modified
            __props__.__dict__["name"] = name
            __props__.__dict__["object_marking_refs"] = object_marking_refs
            __props__.__dict__["parsed_pattern"] = parsed_pattern
            __props__.__dict__["pattern"] = pattern
            __props__.__dict__["pattern_type"] = pattern_type
            __props__.__dict__["pattern_version"] = pattern_version
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["revoked"] = revoked
            __props__.__dict__["source"] = source
            __props__.__dict__["threat_intelligence_tags"] = threat_intelligence_tags
            __props__.__dict__["threat_types"] = threat_types
            __props__.__dict__["valid_from"] = valid_from
            __props__.__dict__["valid_until"] = valid_until
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:ThreatIntelligenceIndicator"), pulumi.Alias(type_="azure-native:securityinsights/v20190101preview:ThreatIntelligenceIndicator"), pulumi.Alias(type_="azure-native:securityinsights/v20210401:ThreatIntelligenceIndicator"), pulumi.Alias(type_="azure-native:securityinsights/v20210901preview:ThreatIntelligenceIndicator"), pulumi.Alias(type_="azure-native:securityinsights/v20211001:ThreatIntelligenceIndicator"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:ThreatIntelligenceIndicator"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:ThreatIntelligenceIndicator"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:ThreatIntelligenceIndicator"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:ThreatIntelligenceIndicator"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:ThreatIntelligenceIndicator"), pulumi.Alias(type_="azure-native:securityinsights/v20220801:ThreatIntelligenceIndicator"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:ThreatIntelligenceIndicator"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:ThreatIntelligenceIndicator")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ThreatIntelligenceIndicator, __self__).__init__(
            'azure-native:securityinsights/v20220401preview:ThreatIntelligenceIndicator',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ThreatIntelligenceIndicator':
        """
        Get an existing ThreatIntelligenceIndicator resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ThreatIntelligenceIndicatorArgs.__new__(ThreatIntelligenceIndicatorArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ThreatIntelligenceIndicator(resource_name, opts=opts, __props__=__props__)

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
        The kind of the entity.
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

