# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetAssessmentResult',
    'AwaitableGetAssessmentResult',
    'get_assessment',
    'get_assessment_output',
]

@pulumi.output_type
class GetAssessmentResult:
    """
    An assessment created for a group in the Migration project.
    """
    def __init__(__self__, azure_hybrid_use_benefit=None, azure_location=None, azure_offer_code=None, azure_pricing_tier=None, azure_storage_redundancy=None, confidence_rating_in_percentage=None, created_timestamp=None, currency=None, discount_percentage=None, e_tag=None, id=None, monthly_bandwidth_cost=None, monthly_compute_cost=None, monthly_storage_cost=None, name=None, number_of_machines=None, percentile=None, prices_timestamp=None, scaling_factor=None, sizing_criterion=None, stage=None, status=None, time_range=None, type=None, updated_timestamp=None):
        if azure_hybrid_use_benefit and not isinstance(azure_hybrid_use_benefit, str):
            raise TypeError("Expected argument 'azure_hybrid_use_benefit' to be a str")
        pulumi.set(__self__, "azure_hybrid_use_benefit", azure_hybrid_use_benefit)
        if azure_location and not isinstance(azure_location, str):
            raise TypeError("Expected argument 'azure_location' to be a str")
        pulumi.set(__self__, "azure_location", azure_location)
        if azure_offer_code and not isinstance(azure_offer_code, str):
            raise TypeError("Expected argument 'azure_offer_code' to be a str")
        pulumi.set(__self__, "azure_offer_code", azure_offer_code)
        if azure_pricing_tier and not isinstance(azure_pricing_tier, str):
            raise TypeError("Expected argument 'azure_pricing_tier' to be a str")
        pulumi.set(__self__, "azure_pricing_tier", azure_pricing_tier)
        if azure_storage_redundancy and not isinstance(azure_storage_redundancy, str):
            raise TypeError("Expected argument 'azure_storage_redundancy' to be a str")
        pulumi.set(__self__, "azure_storage_redundancy", azure_storage_redundancy)
        if confidence_rating_in_percentage and not isinstance(confidence_rating_in_percentage, float):
            raise TypeError("Expected argument 'confidence_rating_in_percentage' to be a float")
        pulumi.set(__self__, "confidence_rating_in_percentage", confidence_rating_in_percentage)
        if created_timestamp and not isinstance(created_timestamp, str):
            raise TypeError("Expected argument 'created_timestamp' to be a str")
        pulumi.set(__self__, "created_timestamp", created_timestamp)
        if currency and not isinstance(currency, str):
            raise TypeError("Expected argument 'currency' to be a str")
        pulumi.set(__self__, "currency", currency)
        if discount_percentage and not isinstance(discount_percentage, float):
            raise TypeError("Expected argument 'discount_percentage' to be a float")
        pulumi.set(__self__, "discount_percentage", discount_percentage)
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if monthly_bandwidth_cost and not isinstance(monthly_bandwidth_cost, float):
            raise TypeError("Expected argument 'monthly_bandwidth_cost' to be a float")
        pulumi.set(__self__, "monthly_bandwidth_cost", monthly_bandwidth_cost)
        if monthly_compute_cost and not isinstance(monthly_compute_cost, float):
            raise TypeError("Expected argument 'monthly_compute_cost' to be a float")
        pulumi.set(__self__, "monthly_compute_cost", monthly_compute_cost)
        if monthly_storage_cost and not isinstance(monthly_storage_cost, float):
            raise TypeError("Expected argument 'monthly_storage_cost' to be a float")
        pulumi.set(__self__, "monthly_storage_cost", monthly_storage_cost)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if number_of_machines and not isinstance(number_of_machines, int):
            raise TypeError("Expected argument 'number_of_machines' to be a int")
        pulumi.set(__self__, "number_of_machines", number_of_machines)
        if percentile and not isinstance(percentile, str):
            raise TypeError("Expected argument 'percentile' to be a str")
        pulumi.set(__self__, "percentile", percentile)
        if prices_timestamp and not isinstance(prices_timestamp, str):
            raise TypeError("Expected argument 'prices_timestamp' to be a str")
        pulumi.set(__self__, "prices_timestamp", prices_timestamp)
        if scaling_factor and not isinstance(scaling_factor, float):
            raise TypeError("Expected argument 'scaling_factor' to be a float")
        pulumi.set(__self__, "scaling_factor", scaling_factor)
        if sizing_criterion and not isinstance(sizing_criterion, str):
            raise TypeError("Expected argument 'sizing_criterion' to be a str")
        pulumi.set(__self__, "sizing_criterion", sizing_criterion)
        if stage and not isinstance(stage, str):
            raise TypeError("Expected argument 'stage' to be a str")
        pulumi.set(__self__, "stage", stage)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if time_range and not isinstance(time_range, str):
            raise TypeError("Expected argument 'time_range' to be a str")
        pulumi.set(__self__, "time_range", time_range)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_timestamp and not isinstance(updated_timestamp, str):
            raise TypeError("Expected argument 'updated_timestamp' to be a str")
        pulumi.set(__self__, "updated_timestamp", updated_timestamp)

    @property
    @pulumi.getter(name="azureHybridUseBenefit")
    def azure_hybrid_use_benefit(self) -> str:
        """
        AHUB discount on windows virtual machines.
        """
        return pulumi.get(self, "azure_hybrid_use_benefit")

    @property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> str:
        """
        Target Azure location for which the machines should be assessed. These enums are the same as used by Compute API.
        """
        return pulumi.get(self, "azure_location")

    @property
    @pulumi.getter(name="azureOfferCode")
    def azure_offer_code(self) -> str:
        """
        Offer code according to which cost estimation is done.
        """
        return pulumi.get(self, "azure_offer_code")

    @property
    @pulumi.getter(name="azurePricingTier")
    def azure_pricing_tier(self) -> str:
        """
        Pricing tier for Size evaluation.
        """
        return pulumi.get(self, "azure_pricing_tier")

    @property
    @pulumi.getter(name="azureStorageRedundancy")
    def azure_storage_redundancy(self) -> str:
        """
        Storage Redundancy type offered by Azure.
        """
        return pulumi.get(self, "azure_storage_redundancy")

    @property
    @pulumi.getter(name="confidenceRatingInPercentage")
    def confidence_rating_in_percentage(self) -> float:
        """
        Confidence rating percentage for assessment. Can be in the range [0, 100].
        """
        return pulumi.get(self, "confidence_rating_in_percentage")

    @property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> str:
        """
        Time when this project was created. Date-Time represented in ISO-8601 format.
        """
        return pulumi.get(self, "created_timestamp")

    @property
    @pulumi.getter
    def currency(self) -> str:
        """
        Currency to report prices in.
        """
        return pulumi.get(self, "currency")

    @property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> float:
        """
        Custom discount percentage to be applied on final costs. Can be in the range [0, 100].
        """
        return pulumi.get(self, "discount_percentage")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[str]:
        """
        For optimistic concurrency control.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Path reference to this assessment. /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessment/{assessmentName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="monthlyBandwidthCost")
    def monthly_bandwidth_cost(self) -> float:
        """
        Monthly network cost estimate for the machines that are part of this assessment as a group, for a 31-day month.
        """
        return pulumi.get(self, "monthly_bandwidth_cost")

    @property
    @pulumi.getter(name="monthlyComputeCost")
    def monthly_compute_cost(self) -> float:
        """
        Monthly compute cost estimate for the machines that are part of this assessment as a group, for a 31-day month.
        """
        return pulumi.get(self, "monthly_compute_cost")

    @property
    @pulumi.getter(name="monthlyStorageCost")
    def monthly_storage_cost(self) -> float:
        """
        Monthly storage cost estimate for the machines that are part of this assessment as a group, for a 31-day month.
        """
        return pulumi.get(self, "monthly_storage_cost")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Unique name of an assessment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numberOfMachines")
    def number_of_machines(self) -> int:
        """
        Number of assessed machines part of this assessment.
        """
        return pulumi.get(self, "number_of_machines")

    @property
    @pulumi.getter
    def percentile(self) -> str:
        """
        Percentile of performance data used to recommend Azure size.
        """
        return pulumi.get(self, "percentile")

    @property
    @pulumi.getter(name="pricesTimestamp")
    def prices_timestamp(self) -> str:
        """
        Time when the Azure Prices were queried. Date-Time represented in ISO-8601 format.
        """
        return pulumi.get(self, "prices_timestamp")

    @property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> float:
        """
        Scaling factor used over utilization data to add a performance buffer for new machines to be created in Azure. Min Value = 1.0, Max value = 1.9, Default = 1.3.
        """
        return pulumi.get(self, "scaling_factor")

    @property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(self) -> str:
        """
        Assessment sizing criterion.
        """
        return pulumi.get(self, "sizing_criterion")

    @property
    @pulumi.getter
    def stage(self) -> str:
        """
        User configurable setting that describes the status of the assessment.
        """
        return pulumi.get(self, "stage")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Whether the assessment has been created and is valid.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> str:
        """
        Time range of performance data used to recommend a size.
        """
        return pulumi.get(self, "time_range")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the object = [Microsoft.Migrate/projects/groups/assessments].
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> str:
        """
        Time when this project was last updated. Date-Time represented in ISO-8601 format.
        """
        return pulumi.get(self, "updated_timestamp")


class AwaitableGetAssessmentResult(GetAssessmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAssessmentResult(
            azure_hybrid_use_benefit=self.azure_hybrid_use_benefit,
            azure_location=self.azure_location,
            azure_offer_code=self.azure_offer_code,
            azure_pricing_tier=self.azure_pricing_tier,
            azure_storage_redundancy=self.azure_storage_redundancy,
            confidence_rating_in_percentage=self.confidence_rating_in_percentage,
            created_timestamp=self.created_timestamp,
            currency=self.currency,
            discount_percentage=self.discount_percentage,
            e_tag=self.e_tag,
            id=self.id,
            monthly_bandwidth_cost=self.monthly_bandwidth_cost,
            monthly_compute_cost=self.monthly_compute_cost,
            monthly_storage_cost=self.monthly_storage_cost,
            name=self.name,
            number_of_machines=self.number_of_machines,
            percentile=self.percentile,
            prices_timestamp=self.prices_timestamp,
            scaling_factor=self.scaling_factor,
            sizing_criterion=self.sizing_criterion,
            stage=self.stage,
            status=self.status,
            time_range=self.time_range,
            type=self.type,
            updated_timestamp=self.updated_timestamp)


def get_assessment(assessment_name: Optional[str] = None,
                   group_name: Optional[str] = None,
                   project_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAssessmentResult:
    """
    An assessment created for a group in the Migration project.


    :param str assessment_name: Unique name of an assessment within a project.
    :param str group_name: Unique name of a group within a project.
    :param str project_name: Name of the Azure Migrate project.
    :param str resource_group_name: Name of the Azure Resource Group that project is part of.
    """
    __args__ = dict()
    __args__['assessmentName'] = assessment_name
    __args__['groupName'] = group_name
    __args__['projectName'] = project_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:migrate/v20180202:getAssessment', __args__, opts=opts, typ=GetAssessmentResult).value

    return AwaitableGetAssessmentResult(
        azure_hybrid_use_benefit=__ret__.azure_hybrid_use_benefit,
        azure_location=__ret__.azure_location,
        azure_offer_code=__ret__.azure_offer_code,
        azure_pricing_tier=__ret__.azure_pricing_tier,
        azure_storage_redundancy=__ret__.azure_storage_redundancy,
        confidence_rating_in_percentage=__ret__.confidence_rating_in_percentage,
        created_timestamp=__ret__.created_timestamp,
        currency=__ret__.currency,
        discount_percentage=__ret__.discount_percentage,
        e_tag=__ret__.e_tag,
        id=__ret__.id,
        monthly_bandwidth_cost=__ret__.monthly_bandwidth_cost,
        monthly_compute_cost=__ret__.monthly_compute_cost,
        monthly_storage_cost=__ret__.monthly_storage_cost,
        name=__ret__.name,
        number_of_machines=__ret__.number_of_machines,
        percentile=__ret__.percentile,
        prices_timestamp=__ret__.prices_timestamp,
        scaling_factor=__ret__.scaling_factor,
        sizing_criterion=__ret__.sizing_criterion,
        stage=__ret__.stage,
        status=__ret__.status,
        time_range=__ret__.time_range,
        type=__ret__.type,
        updated_timestamp=__ret__.updated_timestamp)


@_utilities.lift_output_func(get_assessment)
def get_assessment_output(assessment_name: Optional[pulumi.Input[str]] = None,
                          group_name: Optional[pulumi.Input[str]] = None,
                          project_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAssessmentResult]:
    """
    An assessment created for a group in the Migration project.


    :param str assessment_name: Unique name of an assessment within a project.
    :param str group_name: Unique name of a group within a project.
    :param str project_name: Name of the Azure Migrate project.
    :param str resource_group_name: Name of the Azure Resource Group that project is part of.
    """
    ...
