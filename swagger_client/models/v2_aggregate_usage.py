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

class V2AggregateUsage(object):
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
        'name': 'str',
        'aggregate_usage_type': 'str',
        'product_usages': 'list[V2ProductUsage]'
    }

    attribute_map = {
        'name': 'Name',
        'aggregate_usage_type': 'AggregateUsageType',
        'product_usages': 'ProductUsages'
    }

    def __init__(self, name=None, aggregate_usage_type=None, product_usages=None):  # noqa: E501
        """V2AggregateUsage - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._aggregate_usage_type = None
        self._product_usages = None
        self.discriminator = None
        self.name = name
        self.aggregate_usage_type = aggregate_usage_type
        self.product_usages = product_usages

    @property
    def name(self):
        """Gets the name of this V2AggregateUsage.  # noqa: E501


        :return: The name of this V2AggregateUsage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2AggregateUsage.


        :param name: The name of this V2AggregateUsage.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def aggregate_usage_type(self):
        """Gets the aggregate_usage_type of this V2AggregateUsage.  # noqa: E501


        :return: The aggregate_usage_type of this V2AggregateUsage.  # noqa: E501
        :rtype: str
        """
        return self._aggregate_usage_type

    @aggregate_usage_type.setter
    def aggregate_usage_type(self, aggregate_usage_type):
        """Sets the aggregate_usage_type of this V2AggregateUsage.


        :param aggregate_usage_type: The aggregate_usage_type of this V2AggregateUsage.  # noqa: E501
        :type: str
        """
        if aggregate_usage_type is None:
            raise ValueError("Invalid value for `aggregate_usage_type`, must not be `None`")  # noqa: E501

        self._aggregate_usage_type = aggregate_usage_type

    @property
    def product_usages(self):
        """Gets the product_usages of this V2AggregateUsage.  # noqa: E501


        :return: The product_usages of this V2AggregateUsage.  # noqa: E501
        :rtype: list[V2ProductUsage]
        """
        return self._product_usages

    @product_usages.setter
    def product_usages(self, product_usages):
        """Sets the product_usages of this V2AggregateUsage.


        :param product_usages: The product_usages of this V2AggregateUsage.  # noqa: E501
        :type: list[V2ProductUsage]
        """
        if product_usages is None:
            raise ValueError("Invalid value for `product_usages`, must not be `None`")  # noqa: E501

        self._product_usages = product_usages

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
        if issubclass(V2AggregateUsage, dict):
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
        if not isinstance(other, V2AggregateUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other