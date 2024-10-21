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

class V1pre3TrashItem(object):
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
        'included_samples': 'list[SampleCompact]',
        'included_app_results': 'list[V1pre3AppResultCompact]',
        'included_app_sessions': 'list[AppSessionCompact]',
        'user_deleted_by': 'V1pre3UserCompact',
        'id': 'str',
        'name': 'str',
        'href': 'str',
        'date_deleted': 'datetime',
        'total_size': 'int',
        'deleted_run': 'V1pre3RunCompact',
        'deleted_app_session': 'AppSessionCompact',
        'deleted_project': 'V1pre3ProjectCompact',
        'deleted_sample': 'SampleCompact',
        'deleted_app_result': 'V1pre3AppResultCompact',
        'deleted_dataset': 'V2DatasetCompact',
        'is_visible_in_trash': 'bool',
        'child_count': 'int',
        'completed_child_events': 'int',
        'trash_status': 'str',
        'href_post_restore_from_trash': 'str',
        'includes': 'list[str]'
    }

    attribute_map = {
        'included_samples': 'IncludedSamples',
        'included_app_results': 'IncludedAppResults',
        'included_app_sessions': 'IncludedAppSessions',
        'user_deleted_by': 'UserDeletedBy',
        'id': 'Id',
        'name': 'Name',
        'href': 'Href',
        'date_deleted': 'DateDeleted',
        'total_size': 'TotalSize',
        'deleted_run': 'DeletedRun',
        'deleted_app_session': 'DeletedAppSession',
        'deleted_project': 'DeletedProject',
        'deleted_sample': 'DeletedSample',
        'deleted_app_result': 'DeletedAppResult',
        'deleted_dataset': 'DeletedDataset',
        'is_visible_in_trash': 'IsVisibleInTrash',
        'child_count': 'ChildCount',
        'completed_child_events': 'CompletedChildEvents',
        'trash_status': 'TrashStatus',
        'href_post_restore_from_trash': 'HrefPostRestoreFromTrash',
        'includes': 'Includes'
    }

    def __init__(self, included_samples=None, included_app_results=None, included_app_sessions=None, user_deleted_by=None, id=None, name=None, href=None, date_deleted=None, total_size=None, deleted_run=None, deleted_app_session=None, deleted_project=None, deleted_sample=None, deleted_app_result=None, deleted_dataset=None, is_visible_in_trash=None, child_count=None, completed_child_events=None, trash_status=None, href_post_restore_from_trash=None, includes=None):  # noqa: E501
        """V1pre3TrashItem - a model defined in Swagger"""  # noqa: E501
        self._included_samples = None
        self._included_app_results = None
        self._included_app_sessions = None
        self._user_deleted_by = None
        self._id = None
        self._name = None
        self._href = None
        self._date_deleted = None
        self._total_size = None
        self._deleted_run = None
        self._deleted_app_session = None
        self._deleted_project = None
        self._deleted_sample = None
        self._deleted_app_result = None
        self._deleted_dataset = None
        self._is_visible_in_trash = None
        self._child_count = None
        self._completed_child_events = None
        self._trash_status = None
        self._href_post_restore_from_trash = None
        self._includes = None
        self.discriminator = None
        if included_samples is not None:
            self.included_samples = included_samples
        if included_app_results is not None:
            self.included_app_results = included_app_results
        if included_app_sessions is not None:
            self.included_app_sessions = included_app_sessions
        if user_deleted_by is not None:
            self.user_deleted_by = user_deleted_by
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if href is not None:
            self.href = href
        if date_deleted is not None:
            self.date_deleted = date_deleted
        if total_size is not None:
            self.total_size = total_size
        if deleted_run is not None:
            self.deleted_run = deleted_run
        if deleted_app_session is not None:
            self.deleted_app_session = deleted_app_session
        if deleted_project is not None:
            self.deleted_project = deleted_project
        if deleted_sample is not None:
            self.deleted_sample = deleted_sample
        if deleted_app_result is not None:
            self.deleted_app_result = deleted_app_result
        if deleted_dataset is not None:
            self.deleted_dataset = deleted_dataset
        if is_visible_in_trash is not None:
            self.is_visible_in_trash = is_visible_in_trash
        if child_count is not None:
            self.child_count = child_count
        if completed_child_events is not None:
            self.completed_child_events = completed_child_events
        if trash_status is not None:
            self.trash_status = trash_status
        if href_post_restore_from_trash is not None:
            self.href_post_restore_from_trash = href_post_restore_from_trash
        if includes is not None:
            self.includes = includes

    @property
    def included_samples(self):
        """Gets the included_samples of this V1pre3TrashItem.  # noqa: E501


        :return: The included_samples of this V1pre3TrashItem.  # noqa: E501
        :rtype: list[SampleCompact]
        """
        return self._included_samples

    @included_samples.setter
    def included_samples(self, included_samples):
        """Sets the included_samples of this V1pre3TrashItem.


        :param included_samples: The included_samples of this V1pre3TrashItem.  # noqa: E501
        :type: list[SampleCompact]
        """

        self._included_samples = included_samples

    @property
    def included_app_results(self):
        """Gets the included_app_results of this V1pre3TrashItem.  # noqa: E501


        :return: The included_app_results of this V1pre3TrashItem.  # noqa: E501
        :rtype: list[V1pre3AppResultCompact]
        """
        return self._included_app_results

    @included_app_results.setter
    def included_app_results(self, included_app_results):
        """Sets the included_app_results of this V1pre3TrashItem.


        :param included_app_results: The included_app_results of this V1pre3TrashItem.  # noqa: E501
        :type: list[V1pre3AppResultCompact]
        """

        self._included_app_results = included_app_results

    @property
    def included_app_sessions(self):
        """Gets the included_app_sessions of this V1pre3TrashItem.  # noqa: E501


        :return: The included_app_sessions of this V1pre3TrashItem.  # noqa: E501
        :rtype: list[AppSessionCompact]
        """
        return self._included_app_sessions

    @included_app_sessions.setter
    def included_app_sessions(self, included_app_sessions):
        """Sets the included_app_sessions of this V1pre3TrashItem.


        :param included_app_sessions: The included_app_sessions of this V1pre3TrashItem.  # noqa: E501
        :type: list[AppSessionCompact]
        """

        self._included_app_sessions = included_app_sessions

    @property
    def user_deleted_by(self):
        """Gets the user_deleted_by of this V1pre3TrashItem.  # noqa: E501


        :return: The user_deleted_by of this V1pre3TrashItem.  # noqa: E501
        :rtype: V1pre3UserCompact
        """
        return self._user_deleted_by

    @user_deleted_by.setter
    def user_deleted_by(self, user_deleted_by):
        """Sets the user_deleted_by of this V1pre3TrashItem.


        :param user_deleted_by: The user_deleted_by of this V1pre3TrashItem.  # noqa: E501
        :type: V1pre3UserCompact
        """

        self._user_deleted_by = user_deleted_by

    @property
    def id(self):
        """Gets the id of this V1pre3TrashItem.  # noqa: E501


        :return: The id of this V1pre3TrashItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1pre3TrashItem.


        :param id: The id of this V1pre3TrashItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this V1pre3TrashItem.  # noqa: E501


        :return: The name of this V1pre3TrashItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1pre3TrashItem.


        :param name: The name of this V1pre3TrashItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def href(self):
        """Gets the href of this V1pre3TrashItem.  # noqa: E501


        :return: The href of this V1pre3TrashItem.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this V1pre3TrashItem.


        :param href: The href of this V1pre3TrashItem.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def date_deleted(self):
        """Gets the date_deleted of this V1pre3TrashItem.  # noqa: E501


        :return: The date_deleted of this V1pre3TrashItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_deleted

    @date_deleted.setter
    def date_deleted(self, date_deleted):
        """Sets the date_deleted of this V1pre3TrashItem.


        :param date_deleted: The date_deleted of this V1pre3TrashItem.  # noqa: E501
        :type: datetime
        """

        self._date_deleted = date_deleted

    @property
    def total_size(self):
        """Gets the total_size of this V1pre3TrashItem.  # noqa: E501


        :return: The total_size of this V1pre3TrashItem.  # noqa: E501
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this V1pre3TrashItem.


        :param total_size: The total_size of this V1pre3TrashItem.  # noqa: E501
        :type: int
        """

        self._total_size = total_size

    @property
    def deleted_run(self):
        """Gets the deleted_run of this V1pre3TrashItem.  # noqa: E501


        :return: The deleted_run of this V1pre3TrashItem.  # noqa: E501
        :rtype: V1pre3RunCompact
        """
        return self._deleted_run

    @deleted_run.setter
    def deleted_run(self, deleted_run):
        """Sets the deleted_run of this V1pre3TrashItem.


        :param deleted_run: The deleted_run of this V1pre3TrashItem.  # noqa: E501
        :type: V1pre3RunCompact
        """

        self._deleted_run = deleted_run

    @property
    def deleted_app_session(self):
        """Gets the deleted_app_session of this V1pre3TrashItem.  # noqa: E501


        :return: The deleted_app_session of this V1pre3TrashItem.  # noqa: E501
        :rtype: AppSessionCompact
        """
        return self._deleted_app_session

    @deleted_app_session.setter
    def deleted_app_session(self, deleted_app_session):
        """Sets the deleted_app_session of this V1pre3TrashItem.


        :param deleted_app_session: The deleted_app_session of this V1pre3TrashItem.  # noqa: E501
        :type: AppSessionCompact
        """

        self._deleted_app_session = deleted_app_session

    @property
    def deleted_project(self):
        """Gets the deleted_project of this V1pre3TrashItem.  # noqa: E501


        :return: The deleted_project of this V1pre3TrashItem.  # noqa: E501
        :rtype: V1pre3ProjectCompact
        """
        return self._deleted_project

    @deleted_project.setter
    def deleted_project(self, deleted_project):
        """Sets the deleted_project of this V1pre3TrashItem.


        :param deleted_project: The deleted_project of this V1pre3TrashItem.  # noqa: E501
        :type: V1pre3ProjectCompact
        """

        self._deleted_project = deleted_project

    @property
    def deleted_sample(self):
        """Gets the deleted_sample of this V1pre3TrashItem.  # noqa: E501


        :return: The deleted_sample of this V1pre3TrashItem.  # noqa: E501
        :rtype: SampleCompact
        """
        return self._deleted_sample

    @deleted_sample.setter
    def deleted_sample(self, deleted_sample):
        """Sets the deleted_sample of this V1pre3TrashItem.


        :param deleted_sample: The deleted_sample of this V1pre3TrashItem.  # noqa: E501
        :type: SampleCompact
        """

        self._deleted_sample = deleted_sample

    @property
    def deleted_app_result(self):
        """Gets the deleted_app_result of this V1pre3TrashItem.  # noqa: E501


        :return: The deleted_app_result of this V1pre3TrashItem.  # noqa: E501
        :rtype: V1pre3AppResultCompact
        """
        return self._deleted_app_result

    @deleted_app_result.setter
    def deleted_app_result(self, deleted_app_result):
        """Sets the deleted_app_result of this V1pre3TrashItem.


        :param deleted_app_result: The deleted_app_result of this V1pre3TrashItem.  # noqa: E501
        :type: V1pre3AppResultCompact
        """

        self._deleted_app_result = deleted_app_result

    @property
    def deleted_dataset(self):
        """Gets the deleted_dataset of this V1pre3TrashItem.  # noqa: E501


        :return: The deleted_dataset of this V1pre3TrashItem.  # noqa: E501
        :rtype: V2DatasetCompact
        """
        return self._deleted_dataset

    @deleted_dataset.setter
    def deleted_dataset(self, deleted_dataset):
        """Sets the deleted_dataset of this V1pre3TrashItem.


        :param deleted_dataset: The deleted_dataset of this V1pre3TrashItem.  # noqa: E501
        :type: V2DatasetCompact
        """

        self._deleted_dataset = deleted_dataset

    @property
    def is_visible_in_trash(self):
        """Gets the is_visible_in_trash of this V1pre3TrashItem.  # noqa: E501


        :return: The is_visible_in_trash of this V1pre3TrashItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_visible_in_trash

    @is_visible_in_trash.setter
    def is_visible_in_trash(self, is_visible_in_trash):
        """Sets the is_visible_in_trash of this V1pre3TrashItem.


        :param is_visible_in_trash: The is_visible_in_trash of this V1pre3TrashItem.  # noqa: E501
        :type: bool
        """

        self._is_visible_in_trash = is_visible_in_trash

    @property
    def child_count(self):
        """Gets the child_count of this V1pre3TrashItem.  # noqa: E501


        :return: The child_count of this V1pre3TrashItem.  # noqa: E501
        :rtype: int
        """
        return self._child_count

    @child_count.setter
    def child_count(self, child_count):
        """Sets the child_count of this V1pre3TrashItem.


        :param child_count: The child_count of this V1pre3TrashItem.  # noqa: E501
        :type: int
        """

        self._child_count = child_count

    @property
    def completed_child_events(self):
        """Gets the completed_child_events of this V1pre3TrashItem.  # noqa: E501


        :return: The completed_child_events of this V1pre3TrashItem.  # noqa: E501
        :rtype: int
        """
        return self._completed_child_events

    @completed_child_events.setter
    def completed_child_events(self, completed_child_events):
        """Sets the completed_child_events of this V1pre3TrashItem.


        :param completed_child_events: The completed_child_events of this V1pre3TrashItem.  # noqa: E501
        :type: int
        """

        self._completed_child_events = completed_child_events

    @property
    def trash_status(self):
        """Gets the trash_status of this V1pre3TrashItem.  # noqa: E501


        :return: The trash_status of this V1pre3TrashItem.  # noqa: E501
        :rtype: str
        """
        return self._trash_status

    @trash_status.setter
    def trash_status(self, trash_status):
        """Sets the trash_status of this V1pre3TrashItem.


        :param trash_status: The trash_status of this V1pre3TrashItem.  # noqa: E501
        :type: str
        """

        self._trash_status = trash_status

    @property
    def href_post_restore_from_trash(self):
        """Gets the href_post_restore_from_trash of this V1pre3TrashItem.  # noqa: E501


        :return: The href_post_restore_from_trash of this V1pre3TrashItem.  # noqa: E501
        :rtype: str
        """
        return self._href_post_restore_from_trash

    @href_post_restore_from_trash.setter
    def href_post_restore_from_trash(self, href_post_restore_from_trash):
        """Sets the href_post_restore_from_trash of this V1pre3TrashItem.


        :param href_post_restore_from_trash: The href_post_restore_from_trash of this V1pre3TrashItem.  # noqa: E501
        :type: str
        """

        self._href_post_restore_from_trash = href_post_restore_from_trash

    @property
    def includes(self):
        """Gets the includes of this V1pre3TrashItem.  # noqa: E501


        :return: The includes of this V1pre3TrashItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._includes

    @includes.setter
    def includes(self, includes):
        """Sets the includes of this V1pre3TrashItem.


        :param includes: The includes of this V1pre3TrashItem.  # noqa: E501
        :type: list[str]
        """

        self._includes = includes

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
        if issubclass(V1pre3TrashItem, dict):
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
        if not isinstance(other, V1pre3TrashItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
