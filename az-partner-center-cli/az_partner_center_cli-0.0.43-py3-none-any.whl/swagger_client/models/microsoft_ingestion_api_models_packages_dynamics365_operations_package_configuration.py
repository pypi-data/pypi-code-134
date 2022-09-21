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
from swagger_client.models.microsoft_ingestion_api_models_packages_base_package_configuration import MicrosoftIngestionApiModelsPackagesBasePackageConfiguration  # noqa: F401,E501

class MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration(MicrosoftIngestionApiModelsPackagesBasePackageConfiguration):
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
        'release_version': 'str',
        'solution_identifier': 'str'
    }
    if hasattr(MicrosoftIngestionApiModelsPackagesBasePackageConfiguration, "swagger_types"):
        swagger_types.update(MicrosoftIngestionApiModelsPackagesBasePackageConfiguration.swagger_types)

    attribute_map = {
        'resource_type': 'resourceType',
        'release_version': 'releaseVersion',
        'solution_identifier': 'solutionIdentifier'
    }
    if hasattr(MicrosoftIngestionApiModelsPackagesBasePackageConfiguration, "attribute_map"):
        attribute_map.update(MicrosoftIngestionApiModelsPackagesBasePackageConfiguration.attribute_map)

    def __init__(self, resource_type=None, release_version=None, solution_identifier=None, *args, **kwargs):  # noqa: E501
        """MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration - a model defined in Swagger"""  # noqa: E501
        self._resource_type = None
        self._release_version = None
        self._solution_identifier = None
        self.discriminator = None
        if resource_type is not None:
            self.resource_type = resource_type
        if release_version is not None:
            self.release_version = release_version
        if solution_identifier is not None:
            self.solution_identifier = solution_identifier
        MicrosoftIngestionApiModelsPackagesBasePackageConfiguration.__init__(self, *args, **kwargs)

    @property
    def resource_type(self):
        """Gets the resource_type of this MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration.  # noqa: E501


        :return: The resource_type of this MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration.


        :param resource_type: The resource_type of this MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["Dynamics365OperationsPackageConfiguration"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def release_version(self):
        """Gets the release_version of this MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration.  # noqa: E501


        :return: The release_version of this MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        """Sets the release_version of this MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration.


        :param release_version: The release_version of this MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration.  # noqa: E501
        :type: str
        """

        self._release_version = release_version

    @property
    def solution_identifier(self):
        """Gets the solution_identifier of this MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration.  # noqa: E501


        :return: The solution_identifier of this MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._solution_identifier

    @solution_identifier.setter
    def solution_identifier(self, solution_identifier):
        """Sets the solution_identifier of this MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration.


        :param solution_identifier: The solution_identifier of this MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration.  # noqa: E501
        :type: str
        """

        self._solution_identifier = solution_identifier

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
        if issubclass(MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration, dict):
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
        if not isinstance(other, MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
