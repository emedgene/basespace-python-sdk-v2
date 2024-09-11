# coding: utf-8

"""
    Basespace API

    Basespace REST API  # noqa: E501

    OpenAPI spec version: 5.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V2RunInstrumentCompact(object):
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
        'id': 'int',
        'name': 'str',
        'number': 'int',
        'type': 'str',
        'platform_name': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'number': 'Number',
        'type': 'Type',
        'platform_name': 'PlatformName'
    }

    def __init__(self, id=None, name=None, number=None, type=None, platform_name=None):  # noqa: E501
        """V2RunInstrumentCompact - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._number = None
        self._type = None
        self._platform_name = None
        self.discriminator = None
        self.id = id
        if name is not None:
            self.name = name
        if number is not None:
            self.number = number
        if type is not None:
            self.type = type
        if platform_name is not None:
            self.platform_name = platform_name

    @property
    def id(self):
        """Gets the id of this V2RunInstrumentCompact.  # noqa: E501


        :return: The id of this V2RunInstrumentCompact.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V2RunInstrumentCompact.


        :param id: The id of this V2RunInstrumentCompact.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this V2RunInstrumentCompact.  # noqa: E501


        :return: The name of this V2RunInstrumentCompact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2RunInstrumentCompact.


        :param name: The name of this V2RunInstrumentCompact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this V2RunInstrumentCompact.  # noqa: E501


        :return: The number of this V2RunInstrumentCompact.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this V2RunInstrumentCompact.


        :param number: The number of this V2RunInstrumentCompact.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def type(self):
        """Gets the type of this V2RunInstrumentCompact.  # noqa: E501


        :return: The type of this V2RunInstrumentCompact.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V2RunInstrumentCompact.


        :param type: The type of this V2RunInstrumentCompact.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def platform_name(self):
        """Gets the platform_name of this V2RunInstrumentCompact.  # noqa: E501


        :return: The platform_name of this V2RunInstrumentCompact.  # noqa: E501
        :rtype: str
        """
        return self._platform_name

    @platform_name.setter
    def platform_name(self, platform_name):
        """Sets the platform_name of this V2RunInstrumentCompact.


        :param platform_name: The platform_name of this V2RunInstrumentCompact.  # noqa: E501
        :type: str
        """

        self._platform_name = platform_name

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
        if issubclass(V2RunInstrumentCompact, dict):
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
        if not isinstance(other, V2RunInstrumentCompact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
