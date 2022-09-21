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

class MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity(object):
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
        'recurring_unit': 'str',
        'is_infinite': 'bool',
        'quantity': 'float'
    }

    attribute_map = {
        'recurring_unit': 'recurringUnit',
        'is_infinite': 'isInfinite',
        'quantity': 'quantity'
    }

    def __init__(self, recurring_unit=None, is_infinite=None, quantity=None):  # noqa: E501
        """MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity - a model defined in Swagger"""  # noqa: E501
        self._recurring_unit = None
        self._is_infinite = None
        self._quantity = None
        self.discriminator = None
        if recurring_unit is not None:
            self.recurring_unit = recurring_unit
        if is_infinite is not None:
            self.is_infinite = is_infinite
        if quantity is not None:
            self.quantity = quantity

    @property
    def recurring_unit(self):
        """Gets the recurring_unit of this MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity.  # noqa: E501


        :return: The recurring_unit of this MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity.  # noqa: E501
        :rtype: str
        """
        return self._recurring_unit

    @recurring_unit.setter
    def recurring_unit(self, recurring_unit):
        """Sets the recurring_unit of this MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity.


        :param recurring_unit: The recurring_unit of this MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity.  # noqa: E501
        :type: str
        """

        self._recurring_unit = recurring_unit

    @property
    def is_infinite(self):
        """Gets the is_infinite of this MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity.  # noqa: E501


        :return: The is_infinite of this MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity.  # noqa: E501
        :rtype: bool
        """
        return self._is_infinite

    @is_infinite.setter
    def is_infinite(self, is_infinite):
        """Sets the is_infinite of this MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity.


        :param is_infinite: The is_infinite of this MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity.  # noqa: E501
        :type: bool
        """

        self._is_infinite = is_infinite

    @property
    def quantity(self):
        """Gets the quantity of this MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity.  # noqa: E501


        :return: The quantity of this MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity.


        :param quantity: The quantity of this MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

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
        if issubclass(MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity, dict):
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
        if not isinstance(other, MicrosoftIngestionApiModelsAvailabilitiesIncludedBaseQuantity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
