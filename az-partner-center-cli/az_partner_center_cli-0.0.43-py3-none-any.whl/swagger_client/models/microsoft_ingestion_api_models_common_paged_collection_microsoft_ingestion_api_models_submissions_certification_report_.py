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
from swagger_client.models.microsoft_ingestion_api_models_common_paged_collection import MicrosoftIngestionApiModelsCommonPagedCollection  # noqa: F401,E501

class MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsCertificationReport_(MicrosoftIngestionApiModelsCommonPagedCollection):
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
        'value': 'list[MicrosoftIngestionApiModelsSubmissionsCertificationReport]'
    }
    if hasattr(MicrosoftIngestionApiModelsCommonPagedCollection, "swagger_types"):
        swagger_types.update(MicrosoftIngestionApiModelsCommonPagedCollection.swagger_types)

    attribute_map = {
        'value': 'value'
    }
    if hasattr(MicrosoftIngestionApiModelsCommonPagedCollection, "attribute_map"):
        attribute_map.update(MicrosoftIngestionApiModelsCommonPagedCollection.attribute_map)

    def __init__(self, value=None, *args, **kwargs):  # noqa: E501
        """MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsCertificationReport_ - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self.discriminator = None
        if value is not None:
            self.value = value
        MicrosoftIngestionApiModelsCommonPagedCollection.__init__(self, *args, **kwargs)

    @property
    def value(self):
        """Gets the value of this MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsCertificationReport_.  # noqa: E501


        :return: The value of this MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsCertificationReport_.  # noqa: E501
        :rtype: list[MicrosoftIngestionApiModelsSubmissionsCertificationReport]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsCertificationReport_.


        :param value: The value of this MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsCertificationReport_.  # noqa: E501
        :type: list[MicrosoftIngestionApiModelsSubmissionsCertificationReport]
        """

        self._value = value

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
        if issubclass(MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsCertificationReport_, dict):
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
        if not isinstance(other, MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsCertificationReport_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
