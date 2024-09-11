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

class V1pre3AppResultCompact(object):
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
        'id': 'str',
        'href': 'str',
        'user_owned_by': 'V1pre3UserCompact',
        'name': 'str',
        'status': 'str',
        'status_summary': 'str',
        'date_created': 'datetime',
        'total_size': 'int',
        'app_session': 'AppSessionCompact',
        'projects': 'list[V1pre3ProjectCompact]',
        'is_deleted': 'bool'
    }

    attribute_map = {
        'id': 'Id',
        'href': 'Href',
        'user_owned_by': 'UserOwnedBy',
        'name': 'Name',
        'status': 'Status',
        'status_summary': 'StatusSummary',
        'date_created': 'DateCreated',
        'total_size': 'TotalSize',
        'app_session': 'AppSession',
        'projects': 'Projects',
        'is_deleted': 'IsDeleted'
    }

    def __init__(self, id=None, href=None, user_owned_by=None, name=None, status=None, status_summary=None, date_created=None, total_size=None, app_session=None, projects=None, is_deleted=None):  # noqa: E501
        """V1pre3AppResultCompact - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._user_owned_by = None
        self._name = None
        self._status = None
        self._status_summary = None
        self._date_created = None
        self._total_size = None
        self._app_session = None
        self._projects = None
        self._is_deleted = None
        self.discriminator = None
        self.id = id
        if href is not None:
            self.href = href
        if user_owned_by is not None:
            self.user_owned_by = user_owned_by
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if status_summary is not None:
            self.status_summary = status_summary
        if date_created is not None:
            self.date_created = date_created
        if total_size is not None:
            self.total_size = total_size
        if app_session is not None:
            self.app_session = app_session
        if projects is not None:
            self.projects = projects
        if is_deleted is not None:
            self.is_deleted = is_deleted

    @property
    def id(self):
        """Gets the id of this V1pre3AppResultCompact.  # noqa: E501


        :return: The id of this V1pre3AppResultCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1pre3AppResultCompact.


        :param id: The id of this V1pre3AppResultCompact.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def href(self):
        """Gets the href of this V1pre3AppResultCompact.  # noqa: E501


        :return: The href of this V1pre3AppResultCompact.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this V1pre3AppResultCompact.


        :param href: The href of this V1pre3AppResultCompact.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def user_owned_by(self):
        """Gets the user_owned_by of this V1pre3AppResultCompact.  # noqa: E501


        :return: The user_owned_by of this V1pre3AppResultCompact.  # noqa: E501
        :rtype: V1pre3UserCompact
        """
        return self._user_owned_by

    @user_owned_by.setter
    def user_owned_by(self, user_owned_by):
        """Sets the user_owned_by of this V1pre3AppResultCompact.


        :param user_owned_by: The user_owned_by of this V1pre3AppResultCompact.  # noqa: E501
        :type: V1pre3UserCompact
        """

        self._user_owned_by = user_owned_by

    @property
    def name(self):
        """Gets the name of this V1pre3AppResultCompact.  # noqa: E501


        :return: The name of this V1pre3AppResultCompact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1pre3AppResultCompact.


        :param name: The name of this V1pre3AppResultCompact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this V1pre3AppResultCompact.  # noqa: E501


        :return: The status of this V1pre3AppResultCompact.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1pre3AppResultCompact.


        :param status: The status of this V1pre3AppResultCompact.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_summary(self):
        """Gets the status_summary of this V1pre3AppResultCompact.  # noqa: E501


        :return: The status_summary of this V1pre3AppResultCompact.  # noqa: E501
        :rtype: str
        """
        return self._status_summary

    @status_summary.setter
    def status_summary(self, status_summary):
        """Sets the status_summary of this V1pre3AppResultCompact.


        :param status_summary: The status_summary of this V1pre3AppResultCompact.  # noqa: E501
        :type: str
        """

        self._status_summary = status_summary

    @property
    def date_created(self):
        """Gets the date_created of this V1pre3AppResultCompact.  # noqa: E501


        :return: The date_created of this V1pre3AppResultCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this V1pre3AppResultCompact.


        :param date_created: The date_created of this V1pre3AppResultCompact.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def total_size(self):
        """Gets the total_size of this V1pre3AppResultCompact.  # noqa: E501


        :return: The total_size of this V1pre3AppResultCompact.  # noqa: E501
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this V1pre3AppResultCompact.


        :param total_size: The total_size of this V1pre3AppResultCompact.  # noqa: E501
        :type: int
        """

        self._total_size = total_size

    @property
    def app_session(self):
        """Gets the app_session of this V1pre3AppResultCompact.  # noqa: E501


        :return: The app_session of this V1pre3AppResultCompact.  # noqa: E501
        :rtype: AppSessionCompact
        """
        return self._app_session

    @app_session.setter
    def app_session(self, app_session):
        """Sets the app_session of this V1pre3AppResultCompact.


        :param app_session: The app_session of this V1pre3AppResultCompact.  # noqa: E501
        :type: AppSessionCompact
        """

        self._app_session = app_session

    @property
    def projects(self):
        """Gets the projects of this V1pre3AppResultCompact.  # noqa: E501


        :return: The projects of this V1pre3AppResultCompact.  # noqa: E501
        :rtype: list[V1pre3ProjectCompact]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this V1pre3AppResultCompact.


        :param projects: The projects of this V1pre3AppResultCompact.  # noqa: E501
        :type: list[V1pre3ProjectCompact]
        """

        self._projects = projects

    @property
    def is_deleted(self):
        """Gets the is_deleted of this V1pre3AppResultCompact.  # noqa: E501


        :return: The is_deleted of this V1pre3AppResultCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this V1pre3AppResultCompact.


        :param is_deleted: The is_deleted of this V1pre3AppResultCompact.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

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
        if issubclass(V1pre3AppResultCompact, dict):
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
        if not isinstance(other, V1pre3AppResultCompact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other