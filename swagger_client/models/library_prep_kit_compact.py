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

class LibraryPrepKitCompact(object):
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
        'name': 'str',
        'user_owned_by': 'V1pre3UserCompact',
        'valid_indexing_strategies': 'str',
        'valid_read_types': 'str',
        'num_index_cycles': 'int',
        'adapter_sequence_read1': 'str',
        'adapter_sequence_read2': 'str',
        'date_modified': 'datetime',
        'state': 'str',
        'default_read1_cycles': 'int',
        'default_read2_cycles': 'int',
        'protocol_version': 'str',
        'library_type': 'str',
        'prep_kit_family_slug': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'href': 'Href',
        'name': 'Name',
        'user_owned_by': 'UserOwnedBy',
        'valid_indexing_strategies': 'ValidIndexingStrategies',
        'valid_read_types': 'ValidReadTypes',
        'num_index_cycles': 'NumIndexCycles',
        'adapter_sequence_read1': 'AdapterSequenceRead1',
        'adapter_sequence_read2': 'AdapterSequenceRead2',
        'date_modified': 'DateModified',
        'state': 'State',
        'default_read1_cycles': 'DefaultRead1Cycles',
        'default_read2_cycles': 'DefaultRead2Cycles',
        'protocol_version': 'ProtocolVersion',
        'library_type': 'LibraryType',
        'prep_kit_family_slug': 'PrepKitFamilySlug'
    }

    def __init__(self, id=None, href=None, name=None, user_owned_by=None, valid_indexing_strategies=None, valid_read_types=None, num_index_cycles=None, adapter_sequence_read1=None, adapter_sequence_read2=None, date_modified=None, state=None, default_read1_cycles=None, default_read2_cycles=None, protocol_version=None, library_type=None, prep_kit_family_slug=None):  # noqa: E501
        """LibraryPrepKitCompact - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._name = None
        self._user_owned_by = None
        self._valid_indexing_strategies = None
        self._valid_read_types = None
        self._num_index_cycles = None
        self._adapter_sequence_read1 = None
        self._adapter_sequence_read2 = None
        self._date_modified = None
        self._state = None
        self._default_read1_cycles = None
        self._default_read2_cycles = None
        self._protocol_version = None
        self._library_type = None
        self._prep_kit_family_slug = None
        self.discriminator = None
        self.id = id
        if href is not None:
            self.href = href
        if name is not None:
            self.name = name
        if user_owned_by is not None:
            self.user_owned_by = user_owned_by
        if valid_indexing_strategies is not None:
            self.valid_indexing_strategies = valid_indexing_strategies
        if valid_read_types is not None:
            self.valid_read_types = valid_read_types
        if num_index_cycles is not None:
            self.num_index_cycles = num_index_cycles
        if adapter_sequence_read1 is not None:
            self.adapter_sequence_read1 = adapter_sequence_read1
        if adapter_sequence_read2 is not None:
            self.adapter_sequence_read2 = adapter_sequence_read2
        if date_modified is not None:
            self.date_modified = date_modified
        if state is not None:
            self.state = state
        if default_read1_cycles is not None:
            self.default_read1_cycles = default_read1_cycles
        if default_read2_cycles is not None:
            self.default_read2_cycles = default_read2_cycles
        if protocol_version is not None:
            self.protocol_version = protocol_version
        if library_type is not None:
            self.library_type = library_type
        if prep_kit_family_slug is not None:
            self.prep_kit_family_slug = prep_kit_family_slug

    @property
    def id(self):
        """Gets the id of this LibraryPrepKitCompact.  # noqa: E501


        :return: The id of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LibraryPrepKitCompact.


        :param id: The id of this LibraryPrepKitCompact.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def href(self):
        """Gets the href of this LibraryPrepKitCompact.  # noqa: E501


        :return: The href of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this LibraryPrepKitCompact.


        :param href: The href of this LibraryPrepKitCompact.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def name(self):
        """Gets the name of this LibraryPrepKitCompact.  # noqa: E501


        :return: The name of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LibraryPrepKitCompact.


        :param name: The name of this LibraryPrepKitCompact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def user_owned_by(self):
        """Gets the user_owned_by of this LibraryPrepKitCompact.  # noqa: E501


        :return: The user_owned_by of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: V1pre3UserCompact
        """
        return self._user_owned_by

    @user_owned_by.setter
    def user_owned_by(self, user_owned_by):
        """Sets the user_owned_by of this LibraryPrepKitCompact.


        :param user_owned_by: The user_owned_by of this LibraryPrepKitCompact.  # noqa: E501
        :type: V1pre3UserCompact
        """

        self._user_owned_by = user_owned_by

    @property
    def valid_indexing_strategies(self):
        """Gets the valid_indexing_strategies of this LibraryPrepKitCompact.  # noqa: E501


        :return: The valid_indexing_strategies of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: str
        """
        return self._valid_indexing_strategies

    @valid_indexing_strategies.setter
    def valid_indexing_strategies(self, valid_indexing_strategies):
        """Sets the valid_indexing_strategies of this LibraryPrepKitCompact.


        :param valid_indexing_strategies: The valid_indexing_strategies of this LibraryPrepKitCompact.  # noqa: E501
        :type: str
        """

        self._valid_indexing_strategies = valid_indexing_strategies

    @property
    def valid_read_types(self):
        """Gets the valid_read_types of this LibraryPrepKitCompact.  # noqa: E501


        :return: The valid_read_types of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: str
        """
        return self._valid_read_types

    @valid_read_types.setter
    def valid_read_types(self, valid_read_types):
        """Sets the valid_read_types of this LibraryPrepKitCompact.


        :param valid_read_types: The valid_read_types of this LibraryPrepKitCompact.  # noqa: E501
        :type: str
        """

        self._valid_read_types = valid_read_types

    @property
    def num_index_cycles(self):
        """Gets the num_index_cycles of this LibraryPrepKitCompact.  # noqa: E501


        :return: The num_index_cycles of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: int
        """
        return self._num_index_cycles

    @num_index_cycles.setter
    def num_index_cycles(self, num_index_cycles):
        """Sets the num_index_cycles of this LibraryPrepKitCompact.


        :param num_index_cycles: The num_index_cycles of this LibraryPrepKitCompact.  # noqa: E501
        :type: int
        """

        self._num_index_cycles = num_index_cycles

    @property
    def adapter_sequence_read1(self):
        """Gets the adapter_sequence_read1 of this LibraryPrepKitCompact.  # noqa: E501


        :return: The adapter_sequence_read1 of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: str
        """
        return self._adapter_sequence_read1

    @adapter_sequence_read1.setter
    def adapter_sequence_read1(self, adapter_sequence_read1):
        """Sets the adapter_sequence_read1 of this LibraryPrepKitCompact.


        :param adapter_sequence_read1: The adapter_sequence_read1 of this LibraryPrepKitCompact.  # noqa: E501
        :type: str
        """

        self._adapter_sequence_read1 = adapter_sequence_read1

    @property
    def adapter_sequence_read2(self):
        """Gets the adapter_sequence_read2 of this LibraryPrepKitCompact.  # noqa: E501


        :return: The adapter_sequence_read2 of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: str
        """
        return self._adapter_sequence_read2

    @adapter_sequence_read2.setter
    def adapter_sequence_read2(self, adapter_sequence_read2):
        """Sets the adapter_sequence_read2 of this LibraryPrepKitCompact.


        :param adapter_sequence_read2: The adapter_sequence_read2 of this LibraryPrepKitCompact.  # noqa: E501
        :type: str
        """

        self._adapter_sequence_read2 = adapter_sequence_read2

    @property
    def date_modified(self):
        """Gets the date_modified of this LibraryPrepKitCompact.  # noqa: E501


        :return: The date_modified of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this LibraryPrepKitCompact.


        :param date_modified: The date_modified of this LibraryPrepKitCompact.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def state(self):
        """Gets the state of this LibraryPrepKitCompact.  # noqa: E501


        :return: The state of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this LibraryPrepKitCompact.


        :param state: The state of this LibraryPrepKitCompact.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def default_read1_cycles(self):
        """Gets the default_read1_cycles of this LibraryPrepKitCompact.  # noqa: E501


        :return: The default_read1_cycles of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: int
        """
        return self._default_read1_cycles

    @default_read1_cycles.setter
    def default_read1_cycles(self, default_read1_cycles):
        """Sets the default_read1_cycles of this LibraryPrepKitCompact.


        :param default_read1_cycles: The default_read1_cycles of this LibraryPrepKitCompact.  # noqa: E501
        :type: int
        """

        self._default_read1_cycles = default_read1_cycles

    @property
    def default_read2_cycles(self):
        """Gets the default_read2_cycles of this LibraryPrepKitCompact.  # noqa: E501


        :return: The default_read2_cycles of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: int
        """
        return self._default_read2_cycles

    @default_read2_cycles.setter
    def default_read2_cycles(self, default_read2_cycles):
        """Sets the default_read2_cycles of this LibraryPrepKitCompact.


        :param default_read2_cycles: The default_read2_cycles of this LibraryPrepKitCompact.  # noqa: E501
        :type: int
        """

        self._default_read2_cycles = default_read2_cycles

    @property
    def protocol_version(self):
        """Gets the protocol_version of this LibraryPrepKitCompact.  # noqa: E501


        :return: The protocol_version of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: str
        """
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, protocol_version):
        """Sets the protocol_version of this LibraryPrepKitCompact.


        :param protocol_version: The protocol_version of this LibraryPrepKitCompact.  # noqa: E501
        :type: str
        """

        self._protocol_version = protocol_version

    @property
    def library_type(self):
        """Gets the library_type of this LibraryPrepKitCompact.  # noqa: E501


        :return: The library_type of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: str
        """
        return self._library_type

    @library_type.setter
    def library_type(self, library_type):
        """Sets the library_type of this LibraryPrepKitCompact.


        :param library_type: The library_type of this LibraryPrepKitCompact.  # noqa: E501
        :type: str
        """

        self._library_type = library_type

    @property
    def prep_kit_family_slug(self):
        """Gets the prep_kit_family_slug of this LibraryPrepKitCompact.  # noqa: E501


        :return: The prep_kit_family_slug of this LibraryPrepKitCompact.  # noqa: E501
        :rtype: str
        """
        return self._prep_kit_family_slug

    @prep_kit_family_slug.setter
    def prep_kit_family_slug(self, prep_kit_family_slug):
        """Sets the prep_kit_family_slug of this LibraryPrepKitCompact.


        :param prep_kit_family_slug: The prep_kit_family_slug of this LibraryPrepKitCompact.  # noqa: E501
        :type: str
        """

        self._prep_kit_family_slug = prep_kit_family_slug

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
        if issubclass(LibraryPrepKitCompact, dict):
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
        if not isinstance(other, LibraryPrepKitCompact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
