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

class V2CreateBiologicalSampleRequest(object):
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
        'bio_sample_name': 'str',
        'default_project_id': 'str',
        'subject_id': 'str',
        'container_name': 'str',
        'container_position': 'str'
    }

    attribute_map = {
        'bio_sample_name': 'BioSampleName',
        'default_project_id': 'DefaultProjectId',
        'subject_id': 'SubjectId',
        'container_name': 'ContainerName',
        'container_position': 'ContainerPosition'
    }

    def __init__(self, bio_sample_name=None, default_project_id=None, subject_id=None, container_name=None, container_position=None):  # noqa: E501
        """V2CreateBiologicalSampleRequest - a model defined in Swagger"""  # noqa: E501
        self._bio_sample_name = None
        self._default_project_id = None
        self._subject_id = None
        self._container_name = None
        self._container_position = None
        self.discriminator = None
        self.bio_sample_name = bio_sample_name
        self.default_project_id = default_project_id
        self.subject_id = subject_id
        self.container_name = container_name
        self.container_position = container_position

    @property
    def bio_sample_name(self):
        """Gets the bio_sample_name of this V2CreateBiologicalSampleRequest.  # noqa: E501


        :return: The bio_sample_name of this V2CreateBiologicalSampleRequest.  # noqa: E501
        :rtype: str
        """
        return self._bio_sample_name

    @bio_sample_name.setter
    def bio_sample_name(self, bio_sample_name):
        """Sets the bio_sample_name of this V2CreateBiologicalSampleRequest.


        :param bio_sample_name: The bio_sample_name of this V2CreateBiologicalSampleRequest.  # noqa: E501
        :type: str
        """
        if bio_sample_name is None:
            raise ValueError("Invalid value for `bio_sample_name`, must not be `None`")  # noqa: E501

        self._bio_sample_name = bio_sample_name

    @property
    def default_project_id(self):
        """Gets the default_project_id of this V2CreateBiologicalSampleRequest.  # noqa: E501


        :return: The default_project_id of this V2CreateBiologicalSampleRequest.  # noqa: E501
        :rtype: str
        """
        return self._default_project_id

    @default_project_id.setter
    def default_project_id(self, default_project_id):
        """Sets the default_project_id of this V2CreateBiologicalSampleRequest.


        :param default_project_id: The default_project_id of this V2CreateBiologicalSampleRequest.  # noqa: E501
        :type: str
        """
        if default_project_id is None:
            raise ValueError("Invalid value for `default_project_id`, must not be `None`")  # noqa: E501

        self._default_project_id = default_project_id

    @property
    def subject_id(self):
        """Gets the subject_id of this V2CreateBiologicalSampleRequest.  # noqa: E501


        :return: The subject_id of this V2CreateBiologicalSampleRequest.  # noqa: E501
        :rtype: str
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this V2CreateBiologicalSampleRequest.


        :param subject_id: The subject_id of this V2CreateBiologicalSampleRequest.  # noqa: E501
        :type: str
        """
        if subject_id is None:
            raise ValueError("Invalid value for `subject_id`, must not be `None`")  # noqa: E501

        self._subject_id = subject_id

    @property
    def container_name(self):
        """Gets the container_name of this V2CreateBiologicalSampleRequest.  # noqa: E501


        :return: The container_name of this V2CreateBiologicalSampleRequest.  # noqa: E501
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this V2CreateBiologicalSampleRequest.


        :param container_name: The container_name of this V2CreateBiologicalSampleRequest.  # noqa: E501
        :type: str
        """
        if container_name is None:
            raise ValueError("Invalid value for `container_name`, must not be `None`")  # noqa: E501

        self._container_name = container_name

    @property
    def container_position(self):
        """Gets the container_position of this V2CreateBiologicalSampleRequest.  # noqa: E501


        :return: The container_position of this V2CreateBiologicalSampleRequest.  # noqa: E501
        :rtype: str
        """
        return self._container_position

    @container_position.setter
    def container_position(self, container_position):
        """Sets the container_position of this V2CreateBiologicalSampleRequest.


        :param container_position: The container_position of this V2CreateBiologicalSampleRequest.  # noqa: E501
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
        if issubclass(V2CreateBiologicalSampleRequest, dict):
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
        if not isinstance(other, V2CreateBiologicalSampleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other