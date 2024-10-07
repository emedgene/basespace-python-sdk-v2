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

class V2SubjectCompact(object):
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
        'user_subject_id': 'str',
        'description': 'str',
        'species': 'Species',
        'gender': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'href': 'Href',
        'user_owned_by': 'UserOwnedBy',
        'user_subject_id': 'UserSubjectId',
        'description': 'Description',
        'species': 'Species',
        'gender': 'Gender'
    }

    def __init__(self, id=None, href=None, user_owned_by=None, user_subject_id=None, description=None, species=None, gender=None):  # noqa: E501
        """V2SubjectCompact - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._user_owned_by = None
        self._user_subject_id = None
        self._description = None
        self._species = None
        self._gender = None
        self.discriminator = None
        self.id = id
        if href is not None:
            self.href = href
        if user_owned_by is not None:
            self.user_owned_by = user_owned_by
        if user_subject_id is not None:
            self.user_subject_id = user_subject_id
        if description is not None:
            self.description = description
        if species is not None:
            self.species = species
        if gender is not None:
            self.gender = gender

    @property
    def id(self):
        """Gets the id of this V2SubjectCompact.  # noqa: E501


        :return: The id of this V2SubjectCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V2SubjectCompact.


        :param id: The id of this V2SubjectCompact.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def href(self):
        """Gets the href of this V2SubjectCompact.  # noqa: E501


        :return: The href of this V2SubjectCompact.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this V2SubjectCompact.


        :param href: The href of this V2SubjectCompact.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def user_owned_by(self):
        """Gets the user_owned_by of this V2SubjectCompact.  # noqa: E501


        :return: The user_owned_by of this V2SubjectCompact.  # noqa: E501
        :rtype: V1pre3UserCompact
        """
        return self._user_owned_by

    @user_owned_by.setter
    def user_owned_by(self, user_owned_by):
        """Sets the user_owned_by of this V2SubjectCompact.


        :param user_owned_by: The user_owned_by of this V2SubjectCompact.  # noqa: E501
        :type: V1pre3UserCompact
        """

        self._user_owned_by = user_owned_by

    @property
    def user_subject_id(self):
        """Gets the user_subject_id of this V2SubjectCompact.  # noqa: E501


        :return: The user_subject_id of this V2SubjectCompact.  # noqa: E501
        :rtype: str
        """
        return self._user_subject_id

    @user_subject_id.setter
    def user_subject_id(self, user_subject_id):
        """Sets the user_subject_id of this V2SubjectCompact.


        :param user_subject_id: The user_subject_id of this V2SubjectCompact.  # noqa: E501
        :type: str
        """

        self._user_subject_id = user_subject_id

    @property
    def description(self):
        """Gets the description of this V2SubjectCompact.  # noqa: E501


        :return: The description of this V2SubjectCompact.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V2SubjectCompact.


        :param description: The description of this V2SubjectCompact.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def species(self):
        """Gets the species of this V2SubjectCompact.  # noqa: E501


        :return: The species of this V2SubjectCompact.  # noqa: E501
        :rtype: Species
        """
        return self._species

    @species.setter
    def species(self, species):
        """Sets the species of this V2SubjectCompact.


        :param species: The species of this V2SubjectCompact.  # noqa: E501
        :type: Species
        """

        self._species = species

    @property
    def gender(self):
        """Gets the gender of this V2SubjectCompact.  # noqa: E501


        :return: The gender of this V2SubjectCompact.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this V2SubjectCompact.


        :param gender: The gender of this V2SubjectCompact.  # noqa: E501
        :type: str
        """

        self._gender = gender

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
        if issubclass(V2SubjectCompact, dict):
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
        if not isinstance(other, V2SubjectCompact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other