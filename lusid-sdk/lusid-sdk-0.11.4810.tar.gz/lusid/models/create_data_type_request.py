# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4810
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class CreateDataTypeRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'scope': 'str',
        'code': 'str',
        'type_value_range': 'str',
        'display_name': 'str',
        'description': 'str',
        'value_type': 'str',
        'acceptable_values': 'list[str]',
        'unit_schema': 'str',
        'acceptable_units': 'list[CreateUnitDefinition]',
        'reference_data': 'ReferenceData'
    }

    attribute_map = {
        'scope': 'scope',
        'code': 'code',
        'type_value_range': 'typeValueRange',
        'display_name': 'displayName',
        'description': 'description',
        'value_type': 'valueType',
        'acceptable_values': 'acceptableValues',
        'unit_schema': 'unitSchema',
        'acceptable_units': 'acceptableUnits',
        'reference_data': 'referenceData'
    }

    required_map = {
        'scope': 'required',
        'code': 'required',
        'type_value_range': 'required',
        'display_name': 'required',
        'description': 'required',
        'value_type': 'required',
        'acceptable_values': 'optional',
        'unit_schema': 'optional',
        'acceptable_units': 'optional',
        'reference_data': 'optional'
    }

    def __init__(self, scope=None, code=None, type_value_range=None, display_name=None, description=None, value_type=None, acceptable_values=None, unit_schema=None, acceptable_units=None, reference_data=None, local_vars_configuration=None):  # noqa: E501
        """CreateDataTypeRequest - a model defined in OpenAPI"
        
        :param scope:  The scope that the data type will be created in. (required)
        :type scope: str
        :param code:  The code of the data type. Together with the scope this uniquely defines the data type. (required)
        :type code: str
        :param type_value_range:  Indicates the range of data acceptable by a data type. The available values are: Open, Closed (required)
        :type type_value_range: str
        :param display_name:  The display name of the data type. (required)
        :type display_name: str
        :param description:  The description of the data type. (required)
        :type description: str
        :param value_type:  The expected type of the values. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel (required)
        :type value_type: str
        :param acceptable_values:  The acceptable set of values for this data type. Only applies to 'open' value type range.
        :type acceptable_values: list[str]
        :param unit_schema:  The schema of the data type's units. The available values are: NoUnits, Basic, Iso4217Currency
        :type unit_schema: str
        :param acceptable_units:  The definitions of the acceptable units.
        :type acceptable_units: list[lusid.CreateUnitDefinition]
        :param reference_data: 
        :type reference_data: lusid.ReferenceData

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._scope = None
        self._code = None
        self._type_value_range = None
        self._display_name = None
        self._description = None
        self._value_type = None
        self._acceptable_values = None
        self._unit_schema = None
        self._acceptable_units = None
        self._reference_data = None
        self.discriminator = None

        self.scope = scope
        self.code = code
        self.type_value_range = type_value_range
        self.display_name = display_name
        self.description = description
        self.value_type = value_type
        self.acceptable_values = acceptable_values
        if unit_schema is not None:
            self.unit_schema = unit_schema
        self.acceptable_units = acceptable_units
        if reference_data is not None:
            self.reference_data = reference_data

    @property
    def scope(self):
        """Gets the scope of this CreateDataTypeRequest.  # noqa: E501

        The scope that the data type will be created in.  # noqa: E501

        :return: The scope of this CreateDataTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this CreateDataTypeRequest.

        The scope that the data type will be created in.  # noqa: E501

        :param scope: The scope of this CreateDataTypeRequest.  # noqa: E501
        :type scope: str
        """
        if self.local_vars_configuration.client_side_validation and scope is None:  # noqa: E501
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and len(scope) > 64):
            raise ValueError("Invalid value for `scope`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and len(scope) < 1):
            raise ValueError("Invalid value for `scope`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', scope)):  # noqa: E501
            raise ValueError(r"Invalid value for `scope`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._scope = scope

    @property
    def code(self):
        """Gets the code of this CreateDataTypeRequest.  # noqa: E501

        The code of the data type. Together with the scope this uniquely defines the data type.  # noqa: E501

        :return: The code of this CreateDataTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreateDataTypeRequest.

        The code of the data type. Together with the scope this uniquely defines the data type.  # noqa: E501

        :param code: The code of this CreateDataTypeRequest.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 64):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 1):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._code = code

    @property
    def type_value_range(self):
        """Gets the type_value_range of this CreateDataTypeRequest.  # noqa: E501

        Indicates the range of data acceptable by a data type. The available values are: Open, Closed  # noqa: E501

        :return: The type_value_range of this CreateDataTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._type_value_range

    @type_value_range.setter
    def type_value_range(self, type_value_range):
        """Sets the type_value_range of this CreateDataTypeRequest.

        Indicates the range of data acceptable by a data type. The available values are: Open, Closed  # noqa: E501

        :param type_value_range: The type_value_range of this CreateDataTypeRequest.  # noqa: E501
        :type type_value_range: str
        """
        if self.local_vars_configuration.client_side_validation and type_value_range is None:  # noqa: E501
            raise ValueError("Invalid value for `type_value_range`, must not be `None`")  # noqa: E501
        allowed_values = ["Open", "Closed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type_value_range not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type_value_range` ({0}), must be one of {1}"  # noqa: E501
                .format(type_value_range, allowed_values)
            )

        self._type_value_range = type_value_range

    @property
    def display_name(self):
        """Gets the display_name of this CreateDataTypeRequest.  # noqa: E501

        The display name of the data type.  # noqa: E501

        :return: The display_name of this CreateDataTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateDataTypeRequest.

        The display name of the data type.  # noqa: E501

        :param display_name: The display_name of this CreateDataTypeRequest.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 512):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and not re.search(r'^[\s\S]*$', display_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `display_name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this CreateDataTypeRequest.  # noqa: E501

        The description of the data type.  # noqa: E501

        :return: The description of this CreateDataTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDataTypeRequest.

        The description of the data type.  # noqa: E501

        :param description: The description of this CreateDataTypeRequest.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    @property
    def value_type(self):
        """Gets the value_type of this CreateDataTypeRequest.  # noqa: E501

        The expected type of the values. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel  # noqa: E501

        :return: The value_type of this CreateDataTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this CreateDataTypeRequest.

        The expected type of the values. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel  # noqa: E501

        :param value_type: The value_type of this CreateDataTypeRequest.  # noqa: E501
        :type value_type: str
        """
        if self.local_vars_configuration.client_side_validation and value_type is None:  # noqa: E501
            raise ValueError("Invalid value for `value_type`, must not be `None`")  # noqa: E501
        allowed_values = ["String", "Int", "Decimal", "DateTime", "Boolean", "Map", "List", "PropertyArray", "Percentage", "Code", "Id", "Uri", "CurrencyAndAmount", "TradePrice", "Currency", "MetricValue", "ResourceId", "ResultValue", "CutLocalTime", "DateOrCutLabel"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and value_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(value_type, allowed_values)
            )

        self._value_type = value_type

    @property
    def acceptable_values(self):
        """Gets the acceptable_values of this CreateDataTypeRequest.  # noqa: E501

        The acceptable set of values for this data type. Only applies to 'open' value type range.  # noqa: E501

        :return: The acceptable_values of this CreateDataTypeRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._acceptable_values

    @acceptable_values.setter
    def acceptable_values(self, acceptable_values):
        """Sets the acceptable_values of this CreateDataTypeRequest.

        The acceptable set of values for this data type. Only applies to 'open' value type range.  # noqa: E501

        :param acceptable_values: The acceptable_values of this CreateDataTypeRequest.  # noqa: E501
        :type acceptable_values: list[str]
        """

        self._acceptable_values = acceptable_values

    @property
    def unit_schema(self):
        """Gets the unit_schema of this CreateDataTypeRequest.  # noqa: E501

        The schema of the data type's units. The available values are: NoUnits, Basic, Iso4217Currency  # noqa: E501

        :return: The unit_schema of this CreateDataTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._unit_schema

    @unit_schema.setter
    def unit_schema(self, unit_schema):
        """Sets the unit_schema of this CreateDataTypeRequest.

        The schema of the data type's units. The available values are: NoUnits, Basic, Iso4217Currency  # noqa: E501

        :param unit_schema: The unit_schema of this CreateDataTypeRequest.  # noqa: E501
        :type unit_schema: str
        """
        allowed_values = ["NoUnits", "Basic", "Iso4217Currency"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and unit_schema not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `unit_schema` ({0}), must be one of {1}"  # noqa: E501
                .format(unit_schema, allowed_values)
            )

        self._unit_schema = unit_schema

    @property
    def acceptable_units(self):
        """Gets the acceptable_units of this CreateDataTypeRequest.  # noqa: E501

        The definitions of the acceptable units.  # noqa: E501

        :return: The acceptable_units of this CreateDataTypeRequest.  # noqa: E501
        :rtype: list[lusid.CreateUnitDefinition]
        """
        return self._acceptable_units

    @acceptable_units.setter
    def acceptable_units(self, acceptable_units):
        """Sets the acceptable_units of this CreateDataTypeRequest.

        The definitions of the acceptable units.  # noqa: E501

        :param acceptable_units: The acceptable_units of this CreateDataTypeRequest.  # noqa: E501
        :type acceptable_units: list[lusid.CreateUnitDefinition]
        """

        self._acceptable_units = acceptable_units

    @property
    def reference_data(self):
        """Gets the reference_data of this CreateDataTypeRequest.  # noqa: E501


        :return: The reference_data of this CreateDataTypeRequest.  # noqa: E501
        :rtype: lusid.ReferenceData
        """
        return self._reference_data

    @reference_data.setter
    def reference_data(self, reference_data):
        """Sets the reference_data of this CreateDataTypeRequest.


        :param reference_data: The reference_data of this CreateDataTypeRequest.  # noqa: E501
        :type reference_data: lusid.ReferenceData
        """

        self._reference_data = reference_data

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateDataTypeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDataTypeRequest):
            return True

        return self.to_dict() != other.to_dict()
