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
from swagger_client.models.microsoft_ingestion_api_models_common_identified_resource import MicrosoftIngestionApiModelsCommonIdentifiedResource  # noqa: F401,E501

class MicrosoftIngestionApiModelsCommonEntityResource(MicrosoftIngestionApiModelsCommonIdentifiedResource):
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
        'odata_etag': 'str'
    }
    if hasattr(MicrosoftIngestionApiModelsCommonIdentifiedResource, "swagger_types"):
        swagger_types.update(MicrosoftIngestionApiModelsCommonIdentifiedResource.swagger_types)

    attribute_map = {
        'odata_etag': '@odata.etag'
    }
    if hasattr(MicrosoftIngestionApiModelsCommonIdentifiedResource, "attribute_map"):
        attribute_map.update(MicrosoftIngestionApiModelsCommonIdentifiedResource.attribute_map)

    def __init__(self, odata_etag=None, *args, **kwargs):  # noqa: E501
        """MicrosoftIngestionApiModelsCommonEntityResource - a model defined in Swagger"""  # noqa: E501
        self._odata_etag = None
        self.discriminator = None
        if odata_etag is not None:
            self.odata_etag = odata_etag
        MicrosoftIngestionApiModelsCommonIdentifiedResource.__init__(self, *args, **kwargs)

    @property
    def odata_etag(self):
        """Gets the odata_etag of this MicrosoftIngestionApiModelsCommonEntityResource.  # noqa: E501


        :return: The odata_etag of this MicrosoftIngestionApiModelsCommonEntityResource.  # noqa: E501
        :rtype: str
        """
        return self._odata_etag

    @odata_etag.setter
    def odata_etag(self, odata_etag):
        """Sets the odata_etag of this MicrosoftIngestionApiModelsCommonEntityResource.


        :param odata_etag: The odata_etag of this MicrosoftIngestionApiModelsCommonEntityResource.  # noqa: E501
        :type: str
        """

        self._odata_etag = odata_etag

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
        if issubclass(MicrosoftIngestionApiModelsCommonEntityResource, dict):
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
        if not isinstance(other, MicrosoftIngestionApiModelsCommonEntityResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
