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

class V2ApplicationSettings(object):
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
        'redirect_uri': 'str',
        'client_id': 'str',
        'client_secret': 'str',
        'launch_sources': 'list[str]',
        'launch_permissions': 'list[str]',
        'invited_users': 'list[V2UserCompact]',
        'href_logo': 'str',
        'href_screenshot': 'str',
        'company_name': 'str',
        'category': 'str',
        'homepage_uri': 'str',
        'classifications': 'list[str]',
        'feature_flags': 'list[str]',
        'is_any_version_published': 'bool',
        'published_domain': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'href': 'Href',
        'redirect_uri': 'RedirectUri',
        'client_id': 'ClientId',
        'client_secret': 'ClientSecret',
        'launch_sources': 'LaunchSources',
        'launch_permissions': 'LaunchPermissions',
        'invited_users': 'InvitedUsers',
        'href_logo': 'HrefLogo',
        'href_screenshot': 'HrefScreenshot',
        'company_name': 'CompanyName',
        'category': 'Category',
        'homepage_uri': 'HomepageUri',
        'classifications': 'Classifications',
        'feature_flags': 'FeatureFlags',
        'is_any_version_published': 'IsAnyVersionPublished',
        'published_domain': 'PublishedDomain'
    }

    def __init__(self, id=None, href=None, redirect_uri=None, client_id=None, client_secret=None, launch_sources=None, launch_permissions=None, invited_users=None, href_logo=None, href_screenshot=None, company_name=None, category=None, homepage_uri=None, classifications=None, feature_flags=None, is_any_version_published=None, published_domain=None):  # noqa: E501
        """V2ApplicationSettings - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._redirect_uri = None
        self._client_id = None
        self._client_secret = None
        self._launch_sources = None
        self._launch_permissions = None
        self._invited_users = None
        self._href_logo = None
        self._href_screenshot = None
        self._company_name = None
        self._category = None
        self._homepage_uri = None
        self._classifications = None
        self._feature_flags = None
        self._is_any_version_published = None
        self._published_domain = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if launch_sources is not None:
            self.launch_sources = launch_sources
        if launch_permissions is not None:
            self.launch_permissions = launch_permissions
        if invited_users is not None:
            self.invited_users = invited_users
        if href_logo is not None:
            self.href_logo = href_logo
        if href_screenshot is not None:
            self.href_screenshot = href_screenshot
        if company_name is not None:
            self.company_name = company_name
        if category is not None:
            self.category = category
        if homepage_uri is not None:
            self.homepage_uri = homepage_uri
        if classifications is not None:
            self.classifications = classifications
        if feature_flags is not None:
            self.feature_flags = feature_flags
        if is_any_version_published is not None:
            self.is_any_version_published = is_any_version_published
        if published_domain is not None:
            self.published_domain = published_domain

    @property
    def id(self):
        """Gets the id of this V2ApplicationSettings.  # noqa: E501


        :return: The id of this V2ApplicationSettings.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V2ApplicationSettings.


        :param id: The id of this V2ApplicationSettings.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this V2ApplicationSettings.  # noqa: E501


        :return: The href of this V2ApplicationSettings.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this V2ApplicationSettings.


        :param href: The href of this V2ApplicationSettings.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this V2ApplicationSettings.  # noqa: E501


        :return: The redirect_uri of this V2ApplicationSettings.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this V2ApplicationSettings.


        :param redirect_uri: The redirect_uri of this V2ApplicationSettings.  # noqa: E501
        :type: str
        """

        self._redirect_uri = redirect_uri

    @property
    def client_id(self):
        """Gets the client_id of this V2ApplicationSettings.  # noqa: E501


        :return: The client_id of this V2ApplicationSettings.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this V2ApplicationSettings.


        :param client_id: The client_id of this V2ApplicationSettings.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this V2ApplicationSettings.  # noqa: E501


        :return: The client_secret of this V2ApplicationSettings.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this V2ApplicationSettings.


        :param client_secret: The client_secret of this V2ApplicationSettings.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

    @property
    def launch_sources(self):
        """Gets the launch_sources of this V2ApplicationSettings.  # noqa: E501


        :return: The launch_sources of this V2ApplicationSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._launch_sources

    @launch_sources.setter
    def launch_sources(self, launch_sources):
        """Sets the launch_sources of this V2ApplicationSettings.


        :param launch_sources: The launch_sources of this V2ApplicationSettings.  # noqa: E501
        :type: list[str]
        """

        self._launch_sources = launch_sources

    @property
    def launch_permissions(self):
        """Gets the launch_permissions of this V2ApplicationSettings.  # noqa: E501


        :return: The launch_permissions of this V2ApplicationSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._launch_permissions

    @launch_permissions.setter
    def launch_permissions(self, launch_permissions):
        """Sets the launch_permissions of this V2ApplicationSettings.


        :param launch_permissions: The launch_permissions of this V2ApplicationSettings.  # noqa: E501
        :type: list[str]
        """

        self._launch_permissions = launch_permissions

    @property
    def invited_users(self):
        """Gets the invited_users of this V2ApplicationSettings.  # noqa: E501


        :return: The invited_users of this V2ApplicationSettings.  # noqa: E501
        :rtype: list[V2UserCompact]
        """
        return self._invited_users

    @invited_users.setter
    def invited_users(self, invited_users):
        """Sets the invited_users of this V2ApplicationSettings.


        :param invited_users: The invited_users of this V2ApplicationSettings.  # noqa: E501
        :type: list[V2UserCompact]
        """

        self._invited_users = invited_users

    @property
    def href_logo(self):
        """Gets the href_logo of this V2ApplicationSettings.  # noqa: E501


        :return: The href_logo of this V2ApplicationSettings.  # noqa: E501
        :rtype: str
        """
        return self._href_logo

    @href_logo.setter
    def href_logo(self, href_logo):
        """Sets the href_logo of this V2ApplicationSettings.


        :param href_logo: The href_logo of this V2ApplicationSettings.  # noqa: E501
        :type: str
        """

        self._href_logo = href_logo

    @property
    def href_screenshot(self):
        """Gets the href_screenshot of this V2ApplicationSettings.  # noqa: E501


        :return: The href_screenshot of this V2ApplicationSettings.  # noqa: E501
        :rtype: str
        """
        return self._href_screenshot

    @href_screenshot.setter
    def href_screenshot(self, href_screenshot):
        """Sets the href_screenshot of this V2ApplicationSettings.


        :param href_screenshot: The href_screenshot of this V2ApplicationSettings.  # noqa: E501
        :type: str
        """

        self._href_screenshot = href_screenshot

    @property
    def company_name(self):
        """Gets the company_name of this V2ApplicationSettings.  # noqa: E501


        :return: The company_name of this V2ApplicationSettings.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this V2ApplicationSettings.


        :param company_name: The company_name of this V2ApplicationSettings.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def category(self):
        """Gets the category of this V2ApplicationSettings.  # noqa: E501


        :return: The category of this V2ApplicationSettings.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this V2ApplicationSettings.


        :param category: The category of this V2ApplicationSettings.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def homepage_uri(self):
        """Gets the homepage_uri of this V2ApplicationSettings.  # noqa: E501


        :return: The homepage_uri of this V2ApplicationSettings.  # noqa: E501
        :rtype: str
        """
        return self._homepage_uri

    @homepage_uri.setter
    def homepage_uri(self, homepage_uri):
        """Sets the homepage_uri of this V2ApplicationSettings.


        :param homepage_uri: The homepage_uri of this V2ApplicationSettings.  # noqa: E501
        :type: str
        """

        self._homepage_uri = homepage_uri

    @property
    def classifications(self):
        """Gets the classifications of this V2ApplicationSettings.  # noqa: E501


        :return: The classifications of this V2ApplicationSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        """Sets the classifications of this V2ApplicationSettings.


        :param classifications: The classifications of this V2ApplicationSettings.  # noqa: E501
        :type: list[str]
        """

        self._classifications = classifications

    @property
    def feature_flags(self):
        """Gets the feature_flags of this V2ApplicationSettings.  # noqa: E501


        :return: The feature_flags of this V2ApplicationSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._feature_flags

    @feature_flags.setter
    def feature_flags(self, feature_flags):
        """Sets the feature_flags of this V2ApplicationSettings.


        :param feature_flags: The feature_flags of this V2ApplicationSettings.  # noqa: E501
        :type: list[str]
        """

        self._feature_flags = feature_flags

    @property
    def is_any_version_published(self):
        """Gets the is_any_version_published of this V2ApplicationSettings.  # noqa: E501


        :return: The is_any_version_published of this V2ApplicationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._is_any_version_published

    @is_any_version_published.setter
    def is_any_version_published(self, is_any_version_published):
        """Sets the is_any_version_published of this V2ApplicationSettings.


        :param is_any_version_published: The is_any_version_published of this V2ApplicationSettings.  # noqa: E501
        :type: bool
        """

        self._is_any_version_published = is_any_version_published

    @property
    def published_domain(self):
        """Gets the published_domain of this V2ApplicationSettings.  # noqa: E501


        :return: The published_domain of this V2ApplicationSettings.  # noqa: E501
        :rtype: str
        """
        return self._published_domain

    @published_domain.setter
    def published_domain(self, published_domain):
        """Sets the published_domain of this V2ApplicationSettings.


        :param published_domain: The published_domain of this V2ApplicationSettings.  # noqa: E501
        :type: str
        """

        self._published_domain = published_domain

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
        if issubclass(V2ApplicationSettings, dict):
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
        if not isinstance(other, V2ApplicationSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other