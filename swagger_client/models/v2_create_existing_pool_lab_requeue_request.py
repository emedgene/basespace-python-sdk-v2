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

class V2CreateExistingPoolLabRequeueRequest(object):
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
        'requested_additional_yield': 'int',
        'limsid': 'str'
    }

    attribute_map = {
        'requested_additional_yield': 'RequestedAdditionalYield',
        'limsid': 'LIMSId'
    }

    def __init__(self, requested_additional_yield=None, limsid=None):  # noqa: E501
        """V2CreateExistingPoolLabRequeueRequest - a model defined in Swagger"""  # noqa: E501
        self._requested_additional_yield = None
        self._limsid = None
        self.discriminator = None
        self.requested_additional_yield = requested_additional_yield
        self.limsid = limsid

    @property
    def requested_additional_yield(self):
        """Gets the requested_additional_yield of this V2CreateExistingPoolLabRequeueRequest.  # noqa: E501


        :return: The requested_additional_yield of this V2CreateExistingPoolLabRequeueRequest.  # noqa: E501
        :rtype: int
        """
        return self._requested_additional_yield

    @requested_additional_yield.setter
    def requested_additional_yield(self, requested_additional_yield):
        """Sets the requested_additional_yield of this V2CreateExistingPoolLabRequeueRequest.


        :param requested_additional_yield: The requested_additional_yield of this V2CreateExistingPoolLabRequeueRequest.  # noqa: E501
        :type: int
        """
        if requested_additional_yield is None:
            raise ValueError("Invalid value for `requested_additional_yield`, must not be `None`")  # noqa: E501

        self._requested_additional_yield = requested_additional_yield

    @property
    def limsid(self):
        """Gets the limsid of this V2CreateExistingPoolLabRequeueRequest.  # noqa: E501


        :return: The limsid of this V2CreateExistingPoolLabRequeueRequest.  # noqa: E501
        :rtype: str
        """
        return self._limsid

    @limsid.setter
    def limsid(self, limsid):
        """Sets the limsid of this V2CreateExistingPoolLabRequeueRequest.


        :param limsid: The limsid of this V2CreateExistingPoolLabRequeueRequest.  # noqa: E501
        :type: str
        """
        if limsid is None:
            raise ValueError("Invalid value for `limsid`, must not be `None`")  # noqa: E501

        self._limsid = limsid

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
        if issubclass(V2CreateExistingPoolLabRequeueRequest, dict):
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
        if not isinstance(other, V2CreateExistingPoolLabRequeueRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
