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

class V2PostBioSamplesBulkUpdateRequest(object):
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
        'ids': 'list[str]',
        'default_project_id': 'str',
        'container_name': 'str',
        'container_position': 'str'
    }

    attribute_map = {
        'ids': 'Ids',
        'default_project_id': 'DefaultProjectId',
        'container_name': 'ContainerName',
        'container_position': 'ContainerPosition'
    }

    def __init__(self, ids=None, default_project_id=None, container_name=None, container_position=None):  # noqa: E501
        """V2PostBioSamplesBulkUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._ids = None
        self._default_project_id = None
        self._container_name = None
        self._container_position = None
        self.discriminator = None
        self.ids = ids
        self.default_project_id = default_project_id
        self.container_name = container_name
        self.container_position = container_position

    @property
    def ids(self):
        """Gets the ids of this V2PostBioSamplesBulkUpdateRequest.  # noqa: E501

        List the IDs of the biosamples to be updated  # noqa: E501

        :return: The ids of this V2PostBioSamplesBulkUpdateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this V2PostBioSamplesBulkUpdateRequest.

        List the IDs of the biosamples to be updated  # noqa: E501

        :param ids: The ids of this V2PostBioSamplesBulkUpdateRequest.  # noqa: E501
        :type: list[str]
        """
        if ids is None:
            raise ValueError("Invalid value for `ids`, must not be `None`")  # noqa: E501

        self._ids = ids

    @property
    def default_project_id(self):
        """Gets the default_project_id of this V2PostBioSamplesBulkUpdateRequest.  # noqa: E501

        Define the ID of the project to set as the default project  # noqa: E501

        :return: The default_project_id of this V2PostBioSamplesBulkUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._default_project_id

    @default_project_id.setter
    def default_project_id(self, default_project_id):
        """Sets the default_project_id of this V2PostBioSamplesBulkUpdateRequest.

        Define the ID of the project to set as the default project  # noqa: E501

        :param default_project_id: The default_project_id of this V2PostBioSamplesBulkUpdateRequest.  # noqa: E501
        :type: str
        """
        if default_project_id is None:
            raise ValueError("Invalid value for `default_project_id`, must not be `None`")  # noqa: E501

        self._default_project_id = default_project_id

    @property
    def container_name(self):
        """Gets the container_name of this V2PostBioSamplesBulkUpdateRequest.  # noqa: E501

        The name of the plate or tube containing the biosample, typically its barcode  # noqa: E501

        :return: The container_name of this V2PostBioSamplesBulkUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this V2PostBioSamplesBulkUpdateRequest.

        The name of the plate or tube containing the biosample, typically its barcode  # noqa: E501

        :param container_name: The container_name of this V2PostBioSamplesBulkUpdateRequest.  # noqa: E501
        :type: str
        """
        if container_name is None:
            raise ValueError("Invalid value for `container_name`, must not be `None`")  # noqa: E501

        self._container_name = container_name

    @property
    def container_position(self):
        """Gets the container_position of this V2PostBioSamplesBulkUpdateRequest.  # noqa: E501

        The location of the biosample within a plate or other container, typically the well it is in  # noqa: E501

        :return: The container_position of this V2PostBioSamplesBulkUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._container_position

    @container_position.setter
    def container_position(self, container_position):
        """Sets the container_position of this V2PostBioSamplesBulkUpdateRequest.

        The location of the biosample within a plate or other container, typically the well it is in  # noqa: E501

        :param container_position: The container_position of this V2PostBioSamplesBulkUpdateRequest.  # noqa: E501
        :type: str
        """
        if container_position is None:
            raise ValueError("Invalid value for `container_position`, must not be `None`")  # noqa: E501

        self._container_position = container_position

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
        if issubclass(V2PostBioSamplesBulkUpdateRequest, dict):
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
        if not isinstance(other, V2PostBioSamplesBulkUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
