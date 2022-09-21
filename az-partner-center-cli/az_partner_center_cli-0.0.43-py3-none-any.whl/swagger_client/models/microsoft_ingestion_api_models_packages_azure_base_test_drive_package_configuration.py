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

class MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration(MicrosoftIngestionApiModelsPackagesBasePackageConfiguration):
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
        'azure_active_directory_application_id': 'str',
        'azure_active_directory_application_key': 'str',
        'azure_active_directory_tenant_id': 'str',
        'test_drive_duration': 'int'
    }
    if hasattr(MicrosoftIngestionApiModelsPackagesBasePackageConfiguration, "swagger_types"):
        swagger_types.update(MicrosoftIngestionApiModelsPackagesBasePackageConfiguration.swagger_types)

    attribute_map = {
        'azure_active_directory_application_id': 'azureActiveDirectoryApplicationID',
        'azure_active_directory_application_key': 'azureActiveDirectoryApplicationKey',
        'azure_active_directory_tenant_id': 'azureActiveDirectoryTenantID',
        'test_drive_duration': 'testDriveDuration'
    }
    if hasattr(MicrosoftIngestionApiModelsPackagesBasePackageConfiguration, "attribute_map"):
        attribute_map.update(MicrosoftIngestionApiModelsPackagesBasePackageConfiguration.attribute_map)

    def __init__(self, azure_active_directory_application_id=None, azure_active_directory_application_key=None, azure_active_directory_tenant_id=None, test_drive_duration=None, *args, **kwargs):  # noqa: E501
        """MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration - a model defined in Swagger"""  # noqa: E501
        self._azure_active_directory_application_id = None
        self._azure_active_directory_application_key = None
        self._azure_active_directory_tenant_id = None
        self._test_drive_duration = None
        self.discriminator = None
        if azure_active_directory_application_id is not None:
            self.azure_active_directory_application_id = azure_active_directory_application_id
        if azure_active_directory_application_key is not None:
            self.azure_active_directory_application_key = azure_active_directory_application_key
        if azure_active_directory_tenant_id is not None:
            self.azure_active_directory_tenant_id = azure_active_directory_tenant_id
        if test_drive_duration is not None:
            self.test_drive_duration = test_drive_duration
        MicrosoftIngestionApiModelsPackagesBasePackageConfiguration.__init__(self, *args, **kwargs)

    @property
    def azure_active_directory_application_id(self):
        """Gets the azure_active_directory_application_id of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.  # noqa: E501


        :return: The azure_active_directory_application_id of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._azure_active_directory_application_id

    @azure_active_directory_application_id.setter
    def azure_active_directory_application_id(self, azure_active_directory_application_id):
        """Sets the azure_active_directory_application_id of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.


        :param azure_active_directory_application_id: The azure_active_directory_application_id of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.  # noqa: E501
        :type: str
        """

        self._azure_active_directory_application_id = azure_active_directory_application_id

    @property
    def azure_active_directory_application_key(self):
        """Gets the azure_active_directory_application_key of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.  # noqa: E501


        :return: The azure_active_directory_application_key of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._azure_active_directory_application_key

    @azure_active_directory_application_key.setter
    def azure_active_directory_application_key(self, azure_active_directory_application_key):
        """Sets the azure_active_directory_application_key of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.


        :param azure_active_directory_application_key: The azure_active_directory_application_key of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.  # noqa: E501
        :type: str
        """

        self._azure_active_directory_application_key = azure_active_directory_application_key

    @property
    def azure_active_directory_tenant_id(self):
        """Gets the azure_active_directory_tenant_id of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.  # noqa: E501


        :return: The azure_active_directory_tenant_id of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._azure_active_directory_tenant_id

    @azure_active_directory_tenant_id.setter
    def azure_active_directory_tenant_id(self, azure_active_directory_tenant_id):
        """Sets the azure_active_directory_tenant_id of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.


        :param azure_active_directory_tenant_id: The azure_active_directory_tenant_id of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.  # noqa: E501
        :type: str
        """

        self._azure_active_directory_tenant_id = azure_active_directory_tenant_id

    @property
    def test_drive_duration(self):
        """Gets the test_drive_duration of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.  # noqa: E501


        :return: The test_drive_duration of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._test_drive_duration

    @test_drive_duration.setter
    def test_drive_duration(self, test_drive_duration):
        """Sets the test_drive_duration of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.


        :param test_drive_duration: The test_drive_duration of this MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration.  # noqa: E501
        :type: int
        """

        self._test_drive_duration = test_drive_duration

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
        if issubclass(MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration, dict):
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
        if not isinstance(other, MicrosoftIngestionApiModelsPackagesAzureBaseTestDrivePackageConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
