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

class V2RunSampleSheet(object):
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
        'needs_attention': 'bool',
        'format_version': 'str',
        'header_settings': 'list[StringStringKeyValuePair]',
        'read_settings': 'list[StringStringKeyValuePair]',
        'manifests': 'list[StringStringKeyValuePair]',
        'sequencing_settings': 'list[StringStringKeyValuePair]',
        'applications': 'list[V2RunSampleSheetApplication]'
    }

    attribute_map = {
        'needs_attention': 'NeedsAttention',
        'format_version': 'FormatVersion',
        'header_settings': 'HeaderSettings',
        'read_settings': 'ReadSettings',
        'manifests': 'Manifests',
        'sequencing_settings': 'SequencingSettings',
        'applications': 'Applications'
    }

    def __init__(self, needs_attention=None, format_version=None, header_settings=None, read_settings=None, manifests=None, sequencing_settings=None, applications=None):  # noqa: E501
        """V2RunSampleSheet - a model defined in Swagger"""  # noqa: E501
        self._needs_attention = None
        self._format_version = None
        self._header_settings = None
        self._read_settings = None
        self._manifests = None
        self._sequencing_settings = None
        self._applications = None
        self.discriminator = None
        self.needs_attention = needs_attention
        self.format_version = format_version
        if header_settings is not None:
            self.header_settings = header_settings
        if read_settings is not None:
            self.read_settings = read_settings
        if manifests is not None:
            self.manifests = manifests
        if sequencing_settings is not None:
            self.sequencing_settings = sequencing_settings
        if applications is not None:
            self.applications = applications

    @property
    def needs_attention(self):
        """Gets the needs_attention of this V2RunSampleSheet.  # noqa: E501


        :return: The needs_attention of this V2RunSampleSheet.  # noqa: E501
        :rtype: bool
        """
        return self._needs_attention

    @needs_attention.setter
    def needs_attention(self, needs_attention):
        """Sets the needs_attention of this V2RunSampleSheet.


        :param needs_attention: The needs_attention of this V2RunSampleSheet.  # noqa: E501
        :type: bool
        """
        if needs_attention is None:
            raise ValueError("Invalid value for `needs_attention`, must not be `None`")  # noqa: E501

        self._needs_attention = needs_attention

    @property
    def format_version(self):
        """Gets the format_version of this V2RunSampleSheet.  # noqa: E501


        :return: The format_version of this V2RunSampleSheet.  # noqa: E501
        :rtype: str
        """
        return self._format_version

    @format_version.setter
    def format_version(self, format_version):
        """Sets the format_version of this V2RunSampleSheet.


        :param format_version: The format_version of this V2RunSampleSheet.  # noqa: E501
        :type: str
        """
        if format_version is None:
            raise ValueError("Invalid value for `format_version`, must not be `None`")  # noqa: E501

        self._format_version = format_version

    @property
    def header_settings(self):
        """Gets the header_settings of this V2RunSampleSheet.  # noqa: E501


        :return: The header_settings of this V2RunSampleSheet.  # noqa: E501
        :rtype: list[StringStringKeyValuePair]
        """
        return self._header_settings

    @header_settings.setter
    def header_settings(self, header_settings):
        """Sets the header_settings of this V2RunSampleSheet.


        :param header_settings: The header_settings of this V2RunSampleSheet.  # noqa: E501
        :type: list[StringStringKeyValuePair]
        """

        self._header_settings = header_settings

    @property
    def read_settings(self):
        """Gets the read_settings of this V2RunSampleSheet.  # noqa: E501


        :return: The read_settings of this V2RunSampleSheet.  # noqa: E501
        :rtype: list[StringStringKeyValuePair]
        """
        return self._read_settings

    @read_settings.setter
    def read_settings(self, read_settings):
        """Sets the read_settings of this V2RunSampleSheet.


        :param read_settings: The read_settings of this V2RunSampleSheet.  # noqa: E501
        :type: list[StringStringKeyValuePair]
        """

        self._read_settings = read_settings

    @property
    def manifests(self):
        """Gets the manifests of this V2RunSampleSheet.  # noqa: E501


        :return: The manifests of this V2RunSampleSheet.  # noqa: E501
        :rtype: list[StringStringKeyValuePair]
        """
        return self._manifests

    @manifests.setter
    def manifests(self, manifests):
        """Sets the manifests of this V2RunSampleSheet.


        :param manifests: The manifests of this V2RunSampleSheet.  # noqa: E501
        :type: list[StringStringKeyValuePair]
        """

        self._manifests = manifests

    @property
    def sequencing_settings(self):
        """Gets the sequencing_settings of this V2RunSampleSheet.  # noqa: E501


        :return: The sequencing_settings of this V2RunSampleSheet.  # noqa: E501
        :rtype: list[StringStringKeyValuePair]
        """
        return self._sequencing_settings

    @sequencing_settings.setter
    def sequencing_settings(self, sequencing_settings):
        """Sets the sequencing_settings of this V2RunSampleSheet.


        :param sequencing_settings: The sequencing_settings of this V2RunSampleSheet.  # noqa: E501
        :type: list[StringStringKeyValuePair]
        """

        self._sequencing_settings = sequencing_settings

    @property
    def applications(self):
        """Gets the applications of this V2RunSampleSheet.  # noqa: E501


        :return: The applications of this V2RunSampleSheet.  # noqa: E501
        :rtype: list[V2RunSampleSheetApplication]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this V2RunSampleSheet.


        :param applications: The applications of this V2RunSampleSheet.  # noqa: E501
        :type: list[V2RunSampleSheetApplication]
        """

        self._applications = applications

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
        if issubclass(V2RunSampleSheet, dict):
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
        if not isinstance(other, V2RunSampleSheet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other