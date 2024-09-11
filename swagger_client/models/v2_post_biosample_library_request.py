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

class V2PostBiosampleLibraryRequest(object):
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
        'project_id': 'str',
        'index1': 'str',
        'index2': 'str',
        'status': 'str',
        'library_name': 'str',
        'library_prep_id': 'str'
    }

    attribute_map = {
        'project_id': 'ProjectId',
        'index1': 'Index1',
        'index2': 'Index2',
        'status': 'Status',
        'library_name': 'LibraryName',
        'library_prep_id': 'LibraryPrepId'
    }

    def __init__(self, project_id=None, index1=None, index2=None, status=None, library_name=None, library_prep_id=None):  # noqa: E501
        """V2PostBiosampleLibraryRequest - a model defined in Swagger"""  # noqa: E501
        self._project_id = None
        self._index1 = None
        self._index2 = None
        self._status = None
        self._library_name = None
        self._library_prep_id = None
        self.discriminator = None
        self.project_id = project_id
        self.index1 = index1
        self.index2 = index2
        self.status = status
        self.library_name = library_name
        self.library_prep_id = library_prep_id

    @property
    def project_id(self):
        """Gets the project_id of this V2PostBiosampleLibraryRequest.  # noqa: E501


        :return: The project_id of this V2PostBiosampleLibraryRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this V2PostBiosampleLibraryRequest.


        :param project_id: The project_id of this V2PostBiosampleLibraryRequest.  # noqa: E501
        :type: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def index1(self):
        """Gets the index1 of this V2PostBiosampleLibraryRequest.  # noqa: E501


        :return: The index1 of this V2PostBiosampleLibraryRequest.  # noqa: E501
        :rtype: str
        """
        return self._index1

    @index1.setter
    def index1(self, index1):
        """Sets the index1 of this V2PostBiosampleLibraryRequest.


        :param index1: The index1 of this V2PostBiosampleLibraryRequest.  # noqa: E501
        :type: str
        """
        if index1 is None:
            raise ValueError("Invalid value for `index1`, must not be `None`")  # noqa: E501

        self._index1 = index1

    @property
    def index2(self):
        """Gets the index2 of this V2PostBiosampleLibraryRequest.  # noqa: E501


        :return: The index2 of this V2PostBiosampleLibraryRequest.  # noqa: E501
        :rtype: str
        """
        return self._index2

    @index2.setter
    def index2(self, index2):
        """Sets the index2 of this V2PostBiosampleLibraryRequest.


        :param index2: The index2 of this V2PostBiosampleLibraryRequest.  # noqa: E501
        :type: str
        """
        if index2 is None:
            raise ValueError("Invalid value for `index2`, must not be `None`")  # noqa: E501

        self._index2 = index2

    @property
    def status(self):
        """Gets the status of this V2PostBiosampleLibraryRequest.  # noqa: E501


        :return: The status of this V2PostBiosampleLibraryRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V2PostBiosampleLibraryRequest.


        :param status: The status of this V2PostBiosampleLibraryRequest.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def library_name(self):
        """Gets the library_name of this V2PostBiosampleLibraryRequest.  # noqa: E501


        :return: The library_name of this V2PostBiosampleLibraryRequest.  # noqa: E501
        :rtype: str
        """
        return self._library_name

    @library_name.setter
    def library_name(self, library_name):
        """Sets the library_name of this V2PostBiosampleLibraryRequest.


        :param library_name: The library_name of this V2PostBiosampleLibraryRequest.  # noqa: E501
        :type: str
        """
        if library_name is None:
            raise ValueError("Invalid value for `library_name`, must not be `None`")  # noqa: E501

        self._library_name = library_name

    @property
    def library_prep_id(self):
        """Gets the library_prep_id of this V2PostBiosampleLibraryRequest.  # noqa: E501


        :return: The library_prep_id of this V2PostBiosampleLibraryRequest.  # noqa: E501
        :rtype: str
        """
        return self._library_prep_id

    @library_prep_id.setter
    def library_prep_id(self, library_prep_id):
        """Sets the library_prep_id of this V2PostBiosampleLibraryRequest.


        :param library_prep_id: The library_prep_id of this V2PostBiosampleLibraryRequest.  # noqa: E501
        :type: str
        """
        if library_prep_id is None:
            raise ValueError("Invalid value for `library_prep_id`, must not be `None`")  # noqa: E501

        self._library_prep_id = library_prep_id

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
        if issubclass(V2PostBiosampleLibraryRequest, dict):
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
        if not isinstance(other, V2PostBiosampleLibraryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other