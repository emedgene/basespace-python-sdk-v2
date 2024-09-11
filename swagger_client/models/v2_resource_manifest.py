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

class V2ResourceManifest(object):
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
        'items': 'list[V2ResourceManifestCompact]',
        'paging': 'V2ResourceManifestSortFieldsV2Paging',
        'resource_file_zipped': 'bool',
        'project': 'IProjectCompact',
        'app_session': 'IAppSessionCompact',
        'dataset': 'IDatasetCompact',
        'run': 'V2RunCompact',
        'href_files': 'str',
        'href_resource_manifest': 'str',
        'size_in_bytes': 'int'
    }

    attribute_map = {
        'items': 'Items',
        'paging': 'Paging',
        'resource_file_zipped': 'ResourceFileZipped',
        'project': 'Project',
        'app_session': 'AppSession',
        'dataset': 'Dataset',
        'run': 'Run',
        'href_files': 'HrefFiles',
        'href_resource_manifest': 'HrefResourceManifest',
        'size_in_bytes': 'SizeInBytes'
    }

    def __init__(self, items=None, paging=None, resource_file_zipped=None, project=None, app_session=None, dataset=None, run=None, href_files=None, href_resource_manifest=None, size_in_bytes=None):  # noqa: E501
        """V2ResourceManifest - a model defined in Swagger"""  # noqa: E501
        self._items = None
        self._paging = None
        self._resource_file_zipped = None
        self._project = None
        self._app_session = None
        self._dataset = None
        self._run = None
        self._href_files = None
        self._href_resource_manifest = None
        self._size_in_bytes = None
        self.discriminator = None
        self.items = items
        self.paging = paging
        self.resource_file_zipped = resource_file_zipped
        if project is not None:
            self.project = project
        if app_session is not None:
            self.app_session = app_session
        if dataset is not None:
            self.dataset = dataset
        if run is not None:
            self.run = run
        if href_files is not None:
            self.href_files = href_files
        if href_resource_manifest is not None:
            self.href_resource_manifest = href_resource_manifest
        if size_in_bytes is not None:
            self.size_in_bytes = size_in_bytes

    @property
    def items(self):
        """Gets the items of this V2ResourceManifest.  # noqa: E501


        :return: The items of this V2ResourceManifest.  # noqa: E501
        :rtype: list[V2ResourceManifestCompact]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this V2ResourceManifest.


        :param items: The items of this V2ResourceManifest.  # noqa: E501
        :type: list[V2ResourceManifestCompact]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def paging(self):
        """Gets the paging of this V2ResourceManifest.  # noqa: E501


        :return: The paging of this V2ResourceManifest.  # noqa: E501
        :rtype: V2ResourceManifestSortFieldsV2Paging
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this V2ResourceManifest.


        :param paging: The paging of this V2ResourceManifest.  # noqa: E501
        :type: V2ResourceManifestSortFieldsV2Paging
        """
        if paging is None:
            raise ValueError("Invalid value for `paging`, must not be `None`")  # noqa: E501

        self._paging = paging

    @property
    def resource_file_zipped(self):
        """Gets the resource_file_zipped of this V2ResourceManifest.  # noqa: E501


        :return: The resource_file_zipped of this V2ResourceManifest.  # noqa: E501
        :rtype: bool
        """
        return self._resource_file_zipped

    @resource_file_zipped.setter
    def resource_file_zipped(self, resource_file_zipped):
        """Sets the resource_file_zipped of this V2ResourceManifest.


        :param resource_file_zipped: The resource_file_zipped of this V2ResourceManifest.  # noqa: E501
        :type: bool
        """
        if resource_file_zipped is None:
            raise ValueError("Invalid value for `resource_file_zipped`, must not be `None`")  # noqa: E501

        self._resource_file_zipped = resource_file_zipped

    @property
    def project(self):
        """Gets the project of this V2ResourceManifest.  # noqa: E501


        :return: The project of this V2ResourceManifest.  # noqa: E501
        :rtype: IProjectCompact
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this V2ResourceManifest.


        :param project: The project of this V2ResourceManifest.  # noqa: E501
        :type: IProjectCompact
        """

        self._project = project

    @property
    def app_session(self):
        """Gets the app_session of this V2ResourceManifest.  # noqa: E501


        :return: The app_session of this V2ResourceManifest.  # noqa: E501
        :rtype: IAppSessionCompact
        """
        return self._app_session

    @app_session.setter
    def app_session(self, app_session):
        """Sets the app_session of this V2ResourceManifest.


        :param app_session: The app_session of this V2ResourceManifest.  # noqa: E501
        :type: IAppSessionCompact
        """

        self._app_session = app_session

    @property
    def dataset(self):
        """Gets the dataset of this V2ResourceManifest.  # noqa: E501


        :return: The dataset of this V2ResourceManifest.  # noqa: E501
        :rtype: IDatasetCompact
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this V2ResourceManifest.


        :param dataset: The dataset of this V2ResourceManifest.  # noqa: E501
        :type: IDatasetCompact
        """

        self._dataset = dataset

    @property
    def run(self):
        """Gets the run of this V2ResourceManifest.  # noqa: E501


        :return: The run of this V2ResourceManifest.  # noqa: E501
        :rtype: V2RunCompact
        """
        return self._run

    @run.setter
    def run(self, run):
        """Sets the run of this V2ResourceManifest.


        :param run: The run of this V2ResourceManifest.  # noqa: E501
        :type: V2RunCompact
        """

        self._run = run

    @property
    def href_files(self):
        """Gets the href_files of this V2ResourceManifest.  # noqa: E501


        :return: The href_files of this V2ResourceManifest.  # noqa: E501
        :rtype: str
        """
        return self._href_files

    @href_files.setter
    def href_files(self, href_files):
        """Sets the href_files of this V2ResourceManifest.


        :param href_files: The href_files of this V2ResourceManifest.  # noqa: E501
        :type: str
        """

        self._href_files = href_files

    @property
    def href_resource_manifest(self):
        """Gets the href_resource_manifest of this V2ResourceManifest.  # noqa: E501


        :return: The href_resource_manifest of this V2ResourceManifest.  # noqa: E501
        :rtype: str
        """
        return self._href_resource_manifest

    @href_resource_manifest.setter
    def href_resource_manifest(self, href_resource_manifest):
        """Sets the href_resource_manifest of this V2ResourceManifest.


        :param href_resource_manifest: The href_resource_manifest of this V2ResourceManifest.  # noqa: E501
        :type: str
        """

        self._href_resource_manifest = href_resource_manifest

    @property
    def size_in_bytes(self):
        """Gets the size_in_bytes of this V2ResourceManifest.  # noqa: E501


        :return: The size_in_bytes of this V2ResourceManifest.  # noqa: E501
        :rtype: int
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """Sets the size_in_bytes of this V2ResourceManifest.


        :param size_in_bytes: The size_in_bytes of this V2ResourceManifest.  # noqa: E501
        :type: int
        """

        self._size_in_bytes = size_in_bytes

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
        if issubclass(V2ResourceManifest, dict):
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
        if not isinstance(other, V2ResourceManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
