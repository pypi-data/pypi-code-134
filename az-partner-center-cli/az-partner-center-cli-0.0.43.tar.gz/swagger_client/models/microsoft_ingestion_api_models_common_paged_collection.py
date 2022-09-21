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

class MicrosoftIngestionApiModelsCommonPagedCollection(object):
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
        'odata_next_link': 'str'
    }

    attribute_map = {
        'odata_next_link': '@odata.nextLink'
    }

    def __init__(self, odata_next_link=None):  # noqa: E501
        """MicrosoftIngestionApiModelsCommonPagedCollection - a model defined in Swagger"""  # noqa: E501
        self._odata_next_link = None
        self.discriminator = None
        if odata_next_link is not None:
            self.odata_next_link = odata_next_link

    @property
    def odata_next_link(self):
        """Gets the odata_next_link of this MicrosoftIngestionApiModelsCommonPagedCollection.  # noqa: E501


        :return: The odata_next_link of this MicrosoftIngestionApiModelsCommonPagedCollection.  # noqa: E501
        :rtype: str
        """
        return self._odata_next_link

    @odata_next_link.setter
    def odata_next_link(self, odata_next_link):
        """Sets the odata_next_link of this MicrosoftIngestionApiModelsCommonPagedCollection.


        :param odata_next_link: The odata_next_link of this MicrosoftIngestionApiModelsCommonPagedCollection.  # noqa: E501
        :type: str
        """

        self._odata_next_link = odata_next_link

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
        if issubclass(MicrosoftIngestionApiModelsCommonPagedCollection, dict):
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
        if not isinstance(other, MicrosoftIngestionApiModelsCommonPagedCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
