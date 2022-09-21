# coding: utf-8

"""
    https://api.partner.microsoft.com/v1.0/ingestion

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.microsoft_ingestion_api_models_lead_management_base_lead_configuration import MicrosoftIngestionApiModelsLeadManagementBaseLeadConfiguration  # noqa: F401,E501

class MicrosoftIngestionApiModelsLeadManagementSalesForceLeadConfiguration(MicrosoftIngestionApiModelsLeadManagementBaseLeadConfiguration):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'resource_type': 'str',
        'object_identifier': 'str'
    }
    if hasattr(MicrosoftIngestionApiModelsLeadManagementBaseLeadConfiguration, "swagger_types"):
        swagger_types.update(MicrosoftIngestionApiModelsLeadManagementBaseLeadConfiguration.swagger_types)

    attribute_map = {
        'resource_type': 'resourceType',
        'object_identifier': 'objectIdentifier'
    }
    if hasattr(MicrosoftIngestionApiModelsLeadManagementBaseLeadConfiguration, "attribute_map"):
        attribute_map.update(MicrosoftIngestionApiModelsLeadManagementBaseLeadConfiguration.attribute_map)

    def __init__(self, resource_type=None, object_identifier=None, *args, **kwargs):  # noqa: E501
        """MicrosoftIngestionApiModelsLeadManagementSalesForceLeadConfiguration - a model defined in Swagger"""  # noqa: E501
        self._resource_type = None
        self._object_identifier = None
        self.discriminator = None
        if resource_type is not None:
            self.resource_type = resource_type
        if object_identifier is not None:
            self.object_identifier = object_identifier
        MicrosoftIngestionApiModelsLeadManagementBaseLeadConfiguration.__init__(self, *args, **kwargs)

    @property
    def resource_type(self):
        """Gets the resource_type of this MicrosoftIngestionApiModelsLeadManagementSalesForceLeadConfiguration.  # noqa: E501


        :return: The resource_type of this MicrosoftIngestionApiModelsLeadManagementSalesForceLeadConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this MicrosoftIngestionApiModelsLeadManagementSalesForceLeadConfiguration.


        :param resource_type: The resource_type of this MicrosoftIngestionApiModelsLeadManagementSalesForceLeadConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["SalesForceLeadConfiguration"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def object_identifier(self):
        """Gets the object_identifier of this MicrosoftIngestionApiModelsLeadManagementSalesForceLeadConfiguration.  # noqa: E501


        :return: The object_identifier of this MicrosoftIngestionApiModelsLeadManagementSalesForceLeadConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._object_identifier

    @object_identifier.setter
    def object_identifier(self, object_identifier):
        """Sets the object_identifier of this MicrosoftIngestionApiModelsLeadManagementSalesForceLeadConfiguration.


        :param object_identifier: The object_identifier of this MicrosoftIngestionApiModelsLeadManagementSalesForceLeadConfiguration.  # noqa: E501
        :type: str
        """

        self._object_identifier = object_identifier

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MicrosoftIngestionApiModelsLeadManagementSalesForceLeadConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MicrosoftIngestionApiModelsLeadManagementSalesForceLeadConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
