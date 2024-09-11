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

class V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList(object):
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
        'items': 'list[V1pre3ApplicationCompact]',
        'displayed_count': 'int',
        'total_count': 'int',
        'offset': 'int',
        'limit': 'int',
        'sort_dir': 'str',
        'sort_by': 'str'
    }

    attribute_map = {
        'items': 'Items',
        'displayed_count': 'DisplayedCount',
        'total_count': 'TotalCount',
        'offset': 'Offset',
        'limit': 'Limit',
        'sort_dir': 'SortDir',
        'sort_by': 'SortBy'
    }

    def __init__(self, items=None, displayed_count=None, total_count=None, offset=None, limit=None, sort_dir=None, sort_by=None):  # noqa: E501
        """V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList - a model defined in Swagger"""  # noqa: E501
        self._items = None
        self._displayed_count = None
        self._total_count = None
        self._offset = None
        self._limit = None
        self._sort_dir = None
        self._sort_by = None
        self.discriminator = None
        self.items = items
        if displayed_count is not None:
            self.displayed_count = displayed_count
        if total_count is not None:
            self.total_count = total_count
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_by is not None:
            self.sort_by = sort_by

    @property
    def items(self):
        """Gets the items of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501


        :return: The items of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501
        :rtype: list[V1pre3ApplicationCompact]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.


        :param items: The items of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501
        :type: list[V1pre3ApplicationCompact]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def displayed_count(self):
        """Gets the displayed_count of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501


        :return: The displayed_count of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501
        :rtype: int
        """
        return self._displayed_count

    @displayed_count.setter
    def displayed_count(self, displayed_count):
        """Sets the displayed_count of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.


        :param displayed_count: The displayed_count of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501
        :type: int
        """

        self._displayed_count = displayed_count

    @property
    def total_count(self):
        """Gets the total_count of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501


        :return: The total_count of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.


        :param total_count: The total_count of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def offset(self):
        """Gets the offset of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501


        :return: The offset of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.


        :param offset: The offset of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501


        :return: The limit of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.


        :param limit: The limit of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def sort_dir(self):
        """Gets the sort_dir of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501


        :return: The sort_dir of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.


        :param sort_dir: The sort_dir of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501
        :type: str
        """
        allowed_values = ["Asc", "Desc"]  # noqa: E501
        if sort_dir not in allowed_values:
            raise ValueError(
                "Invalid value for `sort_dir` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_dir, allowed_values)
            )

        self._sort_dir = sort_dir

    @property
    def sort_by(self):
        """Gets the sort_by of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501


        :return: The sort_by of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.


        :param sort_by: The sort_by of this V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList.  # noqa: E501
        :type: str
        """
        allowed_values = ["DateCreated", "DatePublished", "Id", "Name", "VersionNumber"]  # noqa: E501
        if sort_by not in allowed_values:
            raise ValueError(
                "Invalid value for `sort_by` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_by, allowed_values)
            )

        self._sort_by = sort_by

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
        if issubclass(V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList, dict):
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
        if not isinstance(other, V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsResourceList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
