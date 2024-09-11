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

class ApplicationScreenshotsV2ApiResponse(object):
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
        'response': 'ApplicationScreenshots',
        'response_status': 'object'
    }

    attribute_map = {
        'response': 'Response',
        'response_status': 'ResponseStatus'
    }

    def __init__(self, response=None, response_status=None):  # noqa: E501
        """ApplicationScreenshotsV2ApiResponse - a model defined in Swagger"""  # noqa: E501
        self._response = None
        self._response_status = None
        self.discriminator = None
        self.response = response
        self.response_status = response_status

    @property
    def response(self):
        """Gets the response of this ApplicationScreenshotsV2ApiResponse.  # noqa: E501


        :return: The response of this ApplicationScreenshotsV2ApiResponse.  # noqa: E501
        :rtype: ApplicationScreenshots
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this ApplicationScreenshotsV2ApiResponse.


        :param response: The response of this ApplicationScreenshotsV2ApiResponse.  # noqa: E501
        :type: ApplicationScreenshots
        """
        if response is None:
            raise ValueError("Invalid value for `response`, must not be `None`")  # noqa: E501

        self._response = response

    @property
    def response_status(self):
        """Gets the response_status of this ApplicationScreenshotsV2ApiResponse.  # noqa: E501


        :return: The response_status of this ApplicationScreenshotsV2ApiResponse.  # noqa: E501
        :rtype: object
        """
        return self._response_status

    @response_status.setter
    def response_status(self, response_status):
        """Sets the response_status of this ApplicationScreenshotsV2ApiResponse.


        :param response_status: The response_status of this ApplicationScreenshotsV2ApiResponse.  # noqa: E501
        :type: object
        """
        if response_status is None:
            raise ValueError("Invalid value for `response_status`, must not be `None`")  # noqa: E501

        self._response_status = response_status

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
        if issubclass(ApplicationScreenshotsV2ApiResponse, dict):
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
        if not isinstance(other, ApplicationScreenshotsV2ApiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
