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

class V2AppSessionCompact(object):
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
        'name': 'str',
        'href': 'str',
        'application': 'V1pre3ApplicationCompact',
        'user_created_by': 'V1pre3UserCompact',
        'execution_status': 'str',
        'qc_status': 'str',
        'status_summary': 'str',
        'purpose': 'str',
        'date_created': 'datetime',
        'date_modified': 'datetime',
        'date_completed': 'datetime',
        'date_started': 'datetime',
        'total_size': 'int',
        'href_ica_analysis': 'str',
        'properties': 'V2PropertyContainer',
        'is_deleted': 'bool',
        'delivery_status': 'str',
        'contains_comments': 'bool',
        'app_session_parent': 'V2AppSessionCompact',
        'app_session_root': 'V2AppSessionCompact',
        'href_comments': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'href': 'Href',
        'application': 'Application',
        'user_created_by': 'UserCreatedBy',
        'execution_status': 'ExecutionStatus',
        'qc_status': 'QcStatus',
        'status_summary': 'StatusSummary',
        'purpose': 'Purpose',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified',
        'date_completed': 'DateCompleted',
        'date_started': 'DateStarted',
        'total_size': 'TotalSize',
        'href_ica_analysis': 'HrefIcaAnalysis',
        'properties': 'Properties',
        'is_deleted': 'IsDeleted',
        'delivery_status': 'DeliveryStatus',
        'contains_comments': 'ContainsComments',
        'app_session_parent': 'AppSessionParent',
        'app_session_root': 'AppSessionRoot',
        'href_comments': 'HrefComments'
    }

    def __init__(self, id=None, name=None, href=None, application=None, user_created_by=None, execution_status=None, qc_status=None, status_summary=None, purpose=None, date_created=None, date_modified=None, date_completed=None, date_started=None, total_size=None, href_ica_analysis=None, properties=None, is_deleted=None, delivery_status=None, contains_comments=None, app_session_parent=None, app_session_root=None, href_comments=None):  # noqa: E501
        """V2AppSessionCompact - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._href = None
        self._application = None
        self._user_created_by = None
        self._execution_status = None
        self._qc_status = None
        self._status_summary = None
        self._purpose = None
        self._date_created = None
        self._date_modified = None
        self._date_completed = None
        self._date_started = None
        self._total_size = None
        self._href_ica_analysis = None
        self._properties = None
        self._is_deleted = None
        self._delivery_status = None
        self._contains_comments = None
        self._app_session_parent = None
        self._app_session_root = None
        self._href_comments = None
        self.discriminator = None
        self.id = id
        if name is not None:
            self.name = name
        self.href = href
        if application is not None:
            self.application = application
        if user_created_by is not None:
            self.user_created_by = user_created_by
        if execution_status is not None:
            self.execution_status = execution_status
        if qc_status is not None:
            self.qc_status = qc_status
        if status_summary is not None:
            self.status_summary = status_summary
        if purpose is not None:
            self.purpose = purpose
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified
        if date_completed is not None:
            self.date_completed = date_completed
        if date_started is not None:
            self.date_started = date_started
        if total_size is not None:
            self.total_size = total_size
        if href_ica_analysis is not None:
            self.href_ica_analysis = href_ica_analysis
        if properties is not None:
            self.properties = properties
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if delivery_status is not None:
            self.delivery_status = delivery_status
        if contains_comments is not None:
            self.contains_comments = contains_comments
        if app_session_parent is not None:
            self.app_session_parent = app_session_parent
        if app_session_root is not None:
            self.app_session_root = app_session_root
        if href_comments is not None:
            self.href_comments = href_comments

    @property
    def id(self):
        """Gets the id of this V2AppSessionCompact.  # noqa: E501


        :return: The id of this V2AppSessionCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V2AppSessionCompact.


        :param id: The id of this V2AppSessionCompact.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this V2AppSessionCompact.  # noqa: E501


        :return: The name of this V2AppSessionCompact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2AppSessionCompact.


        :param name: The name of this V2AppSessionCompact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def href(self):
        """Gets the href of this V2AppSessionCompact.  # noqa: E501


        :return: The href of this V2AppSessionCompact.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this V2AppSessionCompact.


        :param href: The href of this V2AppSessionCompact.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def application(self):
        """Gets the application of this V2AppSessionCompact.  # noqa: E501


        :return: The application of this V2AppSessionCompact.  # noqa: E501
        :rtype: V1pre3ApplicationCompact
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this V2AppSessionCompact.


        :param application: The application of this V2AppSessionCompact.  # noqa: E501
        :type: V1pre3ApplicationCompact
        """

        self._application = application

    @property
    def user_created_by(self):
        """Gets the user_created_by of this V2AppSessionCompact.  # noqa: E501


        :return: The user_created_by of this V2AppSessionCompact.  # noqa: E501
        :rtype: V1pre3UserCompact
        """
        return self._user_created_by

    @user_created_by.setter
    def user_created_by(self, user_created_by):
        """Sets the user_created_by of this V2AppSessionCompact.


        :param user_created_by: The user_created_by of this V2AppSessionCompact.  # noqa: E501
        :type: V1pre3UserCompact
        """

        self._user_created_by = user_created_by

    @property
    def execution_status(self):
        """Gets the execution_status of this V2AppSessionCompact.  # noqa: E501


        :return: The execution_status of this V2AppSessionCompact.  # noqa: E501
        :rtype: str
        """
        return self._execution_status

    @execution_status.setter
    def execution_status(self, execution_status):
        """Sets the execution_status of this V2AppSessionCompact.


        :param execution_status: The execution_status of this V2AppSessionCompact.  # noqa: E501
        :type: str
        """

        self._execution_status = execution_status

    @property
    def qc_status(self):
        """Gets the qc_status of this V2AppSessionCompact.  # noqa: E501


        :return: The qc_status of this V2AppSessionCompact.  # noqa: E501
        :rtype: str
        """
        return self._qc_status

    @qc_status.setter
    def qc_status(self, qc_status):
        """Sets the qc_status of this V2AppSessionCompact.


        :param qc_status: The qc_status of this V2AppSessionCompact.  # noqa: E501
        :type: str
        """

        self._qc_status = qc_status

    @property
    def status_summary(self):
        """Gets the status_summary of this V2AppSessionCompact.  # noqa: E501


        :return: The status_summary of this V2AppSessionCompact.  # noqa: E501
        :rtype: str
        """
        return self._status_summary

    @status_summary.setter
    def status_summary(self, status_summary):
        """Sets the status_summary of this V2AppSessionCompact.


        :param status_summary: The status_summary of this V2AppSessionCompact.  # noqa: E501
        :type: str
        """

        self._status_summary = status_summary

    @property
    def purpose(self):
        """Gets the purpose of this V2AppSessionCompact.  # noqa: E501


        :return: The purpose of this V2AppSessionCompact.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this V2AppSessionCompact.


        :param purpose: The purpose of this V2AppSessionCompact.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

    @property
    def date_created(self):
        """Gets the date_created of this V2AppSessionCompact.  # noqa: E501


        :return: The date_created of this V2AppSessionCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this V2AppSessionCompact.


        :param date_created: The date_created of this V2AppSessionCompact.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this V2AppSessionCompact.  # noqa: E501


        :return: The date_modified of this V2AppSessionCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this V2AppSessionCompact.


        :param date_modified: The date_modified of this V2AppSessionCompact.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def date_completed(self):
        """Gets the date_completed of this V2AppSessionCompact.  # noqa: E501


        :return: The date_completed of this V2AppSessionCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_completed

    @date_completed.setter
    def date_completed(self, date_completed):
        """Sets the date_completed of this V2AppSessionCompact.


        :param date_completed: The date_completed of this V2AppSessionCompact.  # noqa: E501
        :type: datetime
        """

        self._date_completed = date_completed

    @property
    def date_started(self):
        """Gets the date_started of this V2AppSessionCompact.  # noqa: E501


        :return: The date_started of this V2AppSessionCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_started

    @date_started.setter
    def date_started(self, date_started):
        """Sets the date_started of this V2AppSessionCompact.


        :param date_started: The date_started of this V2AppSessionCompact.  # noqa: E501
        :type: datetime
        """

        self._date_started = date_started

    @property
    def total_size(self):
        """Gets the total_size of this V2AppSessionCompact.  # noqa: E501


        :return: The total_size of this V2AppSessionCompact.  # noqa: E501
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this V2AppSessionCompact.


        :param total_size: The total_size of this V2AppSessionCompact.  # noqa: E501
        :type: int
        """

        self._total_size = total_size

    @property
    def href_ica_analysis(self):
        """Gets the href_ica_analysis of this V2AppSessionCompact.  # noqa: E501


        :return: The href_ica_analysis of this V2AppSessionCompact.  # noqa: E501
        :rtype: str
        """
        return self._href_ica_analysis

    @href_ica_analysis.setter
    def href_ica_analysis(self, href_ica_analysis):
        """Sets the href_ica_analysis of this V2AppSessionCompact.


        :param href_ica_analysis: The href_ica_analysis of this V2AppSessionCompact.  # noqa: E501
        :type: str
        """

        self._href_ica_analysis = href_ica_analysis

    @property
    def properties(self):
        """Gets the properties of this V2AppSessionCompact.  # noqa: E501


        :return: The properties of this V2AppSessionCompact.  # noqa: E501
        :rtype: V2PropertyContainer
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this V2AppSessionCompact.


        :param properties: The properties of this V2AppSessionCompact.  # noqa: E501
        :type: V2PropertyContainer
        """

        self._properties = properties

    @property
    def is_deleted(self):
        """Gets the is_deleted of this V2AppSessionCompact.  # noqa: E501


        :return: The is_deleted of this V2AppSessionCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this V2AppSessionCompact.


        :param is_deleted: The is_deleted of this V2AppSessionCompact.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def delivery_status(self):
        """Gets the delivery_status of this V2AppSessionCompact.  # noqa: E501


        :return: The delivery_status of this V2AppSessionCompact.  # noqa: E501
        :rtype: str
        """
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, delivery_status):
        """Sets the delivery_status of this V2AppSessionCompact.


        :param delivery_status: The delivery_status of this V2AppSessionCompact.  # noqa: E501
        :type: str
        """

        self._delivery_status = delivery_status

    @property
    def contains_comments(self):
        """Gets the contains_comments of this V2AppSessionCompact.  # noqa: E501


        :return: The contains_comments of this V2AppSessionCompact.  # noqa: E501
        :rtype: bool
        """
        return self._contains_comments

    @contains_comments.setter
    def contains_comments(self, contains_comments):
        """Sets the contains_comments of this V2AppSessionCompact.


        :param contains_comments: The contains_comments of this V2AppSessionCompact.  # noqa: E501
        :type: bool
        """

        self._contains_comments = contains_comments

    @property
    def app_session_parent(self):
        """Gets the app_session_parent of this V2AppSessionCompact.  # noqa: E501


        :return: The app_session_parent of this V2AppSessionCompact.  # noqa: E501
        :rtype: V2AppSessionCompact
        """
        return self._app_session_parent

    @app_session_parent.setter
    def app_session_parent(self, app_session_parent):
        """Sets the app_session_parent of this V2AppSessionCompact.


        :param app_session_parent: The app_session_parent of this V2AppSessionCompact.  # noqa: E501
        :type: V2AppSessionCompact
        """

        self._app_session_parent = app_session_parent

    @property
    def app_session_root(self):
        """Gets the app_session_root of this V2AppSessionCompact.  # noqa: E501


        :return: The app_session_root of this V2AppSessionCompact.  # noqa: E501
        :rtype: V2AppSessionCompact
        """
        return self._app_session_root

    @app_session_root.setter
    def app_session_root(self, app_session_root):
        """Sets the app_session_root of this V2AppSessionCompact.


        :param app_session_root: The app_session_root of this V2AppSessionCompact.  # noqa: E501
        :type: V2AppSessionCompact
        """

        self._app_session_root = app_session_root

    @property
    def href_comments(self):
        """Gets the href_comments of this V2AppSessionCompact.  # noqa: E501


        :return: The href_comments of this V2AppSessionCompact.  # noqa: E501
        :rtype: str
        """
        return self._href_comments

    @href_comments.setter
    def href_comments(self, href_comments):
        """Sets the href_comments of this V2AppSessionCompact.


        :param href_comments: The href_comments of this V2AppSessionCompact.  # noqa: E501
        :type: str
        """

        self._href_comments = href_comments

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
        if issubclass(V2AppSessionCompact, dict):
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
        if not isinstance(other, V2AppSessionCompact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
