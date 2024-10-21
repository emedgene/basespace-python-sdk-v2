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

class V2IcaCompleteUploadRequest(object):
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
        'folder_name': 'str',
        'upload_session_id': 'str',
        'uploaded_file_names': 'list[str]'
    }

    attribute_map = {
        'folder_name': 'FolderName',
        'upload_session_id': 'UploadSessionId',
        'uploaded_file_names': 'UploadedFileNames'
    }

    def __init__(self, folder_name=None, upload_session_id=None, uploaded_file_names=None):  # noqa: E501
        """V2IcaCompleteUploadRequest - a model defined in Swagger"""  # noqa: E501
        self._folder_name = None
        self._upload_session_id = None
        self._uploaded_file_names = None
        self.discriminator = None
        self.folder_name = folder_name
        self.upload_session_id = upload_session_id
        self.uploaded_file_names = uploaded_file_names

    @property
    def folder_name(self):
        """Gets the folder_name of this V2IcaCompleteUploadRequest.  # noqa: E501


        :return: The folder_name of this V2IcaCompleteUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """Sets the folder_name of this V2IcaCompleteUploadRequest.


        :param folder_name: The folder_name of this V2IcaCompleteUploadRequest.  # noqa: E501
        :type: str
        """
        if folder_name is None:
            raise ValueError("Invalid value for `folder_name`, must not be `None`")  # noqa: E501

        self._folder_name = folder_name

    @property
    def upload_session_id(self):
        """Gets the upload_session_id of this V2IcaCompleteUploadRequest.  # noqa: E501

        The Id of upload session  # noqa: E501

        :return: The upload_session_id of this V2IcaCompleteUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._upload_session_id

    @upload_session_id.setter
    def upload_session_id(self, upload_session_id):
        """Sets the upload_session_id of this V2IcaCompleteUploadRequest.

        The Id of upload session  # noqa: E501

        :param upload_session_id: The upload_session_id of this V2IcaCompleteUploadRequest.  # noqa: E501
        :type: str
        """
        if upload_session_id is None:
            raise ValueError("Invalid value for `upload_session_id`, must not be `None`")  # noqa: E501

        self._upload_session_id = upload_session_id

    @property
    def uploaded_file_names(self):
        """Gets the uploaded_file_names of this V2IcaCompleteUploadRequest.  # noqa: E501

        The names of uploaded files  # noqa: E501

        :return: The uploaded_file_names of this V2IcaCompleteUploadRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._uploaded_file_names

    @uploaded_file_names.setter
    def uploaded_file_names(self, uploaded_file_names):
        """Sets the uploaded_file_names of this V2IcaCompleteUploadRequest.

        The names of uploaded files  # noqa: E501

        :param uploaded_file_names: The uploaded_file_names of this V2IcaCompleteUploadRequest.  # noqa: E501
        :type: list[str]
        """
        if uploaded_file_names is None:
            raise ValueError("Invalid value for `uploaded_file_names`, must not be `None`")  # noqa: E501

        self._uploaded_file_names = uploaded_file_names

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
        if issubclass(V2IcaCompleteUploadRequest, dict):
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
        if not isinstance(other, V2IcaCompleteUploadRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
