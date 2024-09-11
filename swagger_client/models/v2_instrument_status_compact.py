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

class V2InstrumentStatusCompact(object):
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
        'serial_number': 'str',
        'instrument_type': 'str',
        'side_count': 'int',
        'software': 'list[V2Software]',
        'active_runs': 'list[V1pre3RunCompact]',
        'last_run_start_date': 'datetime',
        'last_dx_run_start_date': 'datetime',
        'last_diagnostics_date': 'datetime',
        'last_software_update_check_date': 'datetime',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'serial_number': 'SerialNumber',
        'instrument_type': 'InstrumentType',
        'side_count': 'SideCount',
        'software': 'Software',
        'active_runs': 'ActiveRuns',
        'last_run_start_date': 'LastRunStartDate',
        'last_dx_run_start_date': 'LastDxRunStartDate',
        'last_diagnostics_date': 'LastDiagnosticsDate',
        'last_software_update_check_date': 'LastSoftwareUpdateCheckDate',
        'id': 'Id',
        'name': 'Name'
    }

    def __init__(self, serial_number=None, instrument_type=None, side_count=None, software=None, active_runs=None, last_run_start_date=None, last_dx_run_start_date=None, last_diagnostics_date=None, last_software_update_check_date=None, id=None, name=None):  # noqa: E501
        """V2InstrumentStatusCompact - a model defined in Swagger"""  # noqa: E501
        self._serial_number = None
        self._instrument_type = None
        self._side_count = None
        self._software = None
        self._active_runs = None
        self._last_run_start_date = None
        self._last_dx_run_start_date = None
        self._last_diagnostics_date = None
        self._last_software_update_check_date = None
        self._id = None
        self._name = None
        self.discriminator = None
        self.serial_number = serial_number
        self.instrument_type = instrument_type
        self.side_count = side_count
        self.software = software
        self.active_runs = active_runs
        if last_run_start_date is not None:
            self.last_run_start_date = last_run_start_date
        if last_dx_run_start_date is not None:
            self.last_dx_run_start_date = last_dx_run_start_date
        if last_diagnostics_date is not None:
            self.last_diagnostics_date = last_diagnostics_date
        if last_software_update_check_date is not None:
            self.last_software_update_check_date = last_software_update_check_date
        self.id = id
        self.name = name

    @property
    def serial_number(self):
        """Gets the serial_number of this V2InstrumentStatusCompact.  # noqa: E501


        :return: The serial_number of this V2InstrumentStatusCompact.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this V2InstrumentStatusCompact.


        :param serial_number: The serial_number of this V2InstrumentStatusCompact.  # noqa: E501
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def instrument_type(self):
        """Gets the instrument_type of this V2InstrumentStatusCompact.  # noqa: E501


        :return: The instrument_type of this V2InstrumentStatusCompact.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this V2InstrumentStatusCompact.


        :param instrument_type: The instrument_type of this V2InstrumentStatusCompact.  # noqa: E501
        :type: str
        """
        if instrument_type is None:
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501

        self._instrument_type = instrument_type

    @property
    def side_count(self):
        """Gets the side_count of this V2InstrumentStatusCompact.  # noqa: E501


        :return: The side_count of this V2InstrumentStatusCompact.  # noqa: E501
        :rtype: int
        """
        return self._side_count

    @side_count.setter
    def side_count(self, side_count):
        """Sets the side_count of this V2InstrumentStatusCompact.


        :param side_count: The side_count of this V2InstrumentStatusCompact.  # noqa: E501
        :type: int
        """
        if side_count is None:
            raise ValueError("Invalid value for `side_count`, must not be `None`")  # noqa: E501

        self._side_count = side_count

    @property
    def software(self):
        """Gets the software of this V2InstrumentStatusCompact.  # noqa: E501


        :return: The software of this V2InstrumentStatusCompact.  # noqa: E501
        :rtype: list[V2Software]
        """
        return self._software

    @software.setter
    def software(self, software):
        """Sets the software of this V2InstrumentStatusCompact.


        :param software: The software of this V2InstrumentStatusCompact.  # noqa: E501
        :type: list[V2Software]
        """
        if software is None:
            raise ValueError("Invalid value for `software`, must not be `None`")  # noqa: E501

        self._software = software

    @property
    def active_runs(self):
        """Gets the active_runs of this V2InstrumentStatusCompact.  # noqa: E501


        :return: The active_runs of this V2InstrumentStatusCompact.  # noqa: E501
        :rtype: list[V1pre3RunCompact]
        """
        return self._active_runs

    @active_runs.setter
    def active_runs(self, active_runs):
        """Sets the active_runs of this V2InstrumentStatusCompact.


        :param active_runs: The active_runs of this V2InstrumentStatusCompact.  # noqa: E501
        :type: list[V1pre3RunCompact]
        """
        if active_runs is None:
            raise ValueError("Invalid value for `active_runs`, must not be `None`")  # noqa: E501

        self._active_runs = active_runs

    @property
    def last_run_start_date(self):
        """Gets the last_run_start_date of this V2InstrumentStatusCompact.  # noqa: E501


        :return: The last_run_start_date of this V2InstrumentStatusCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._last_run_start_date

    @last_run_start_date.setter
    def last_run_start_date(self, last_run_start_date):
        """Sets the last_run_start_date of this V2InstrumentStatusCompact.


        :param last_run_start_date: The last_run_start_date of this V2InstrumentStatusCompact.  # noqa: E501
        :type: datetime
        """

        self._last_run_start_date = last_run_start_date

    @property
    def last_dx_run_start_date(self):
        """Gets the last_dx_run_start_date of this V2InstrumentStatusCompact.  # noqa: E501


        :return: The last_dx_run_start_date of this V2InstrumentStatusCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._last_dx_run_start_date

    @last_dx_run_start_date.setter
    def last_dx_run_start_date(self, last_dx_run_start_date):
        """Sets the last_dx_run_start_date of this V2InstrumentStatusCompact.


        :param last_dx_run_start_date: The last_dx_run_start_date of this V2InstrumentStatusCompact.  # noqa: E501
        :type: datetime
        """

        self._last_dx_run_start_date = last_dx_run_start_date

    @property
    def last_diagnostics_date(self):
        """Gets the last_diagnostics_date of this V2InstrumentStatusCompact.  # noqa: E501


        :return: The last_diagnostics_date of this V2InstrumentStatusCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._last_diagnostics_date

    @last_diagnostics_date.setter
    def last_diagnostics_date(self, last_diagnostics_date):
        """Sets the last_diagnostics_date of this V2InstrumentStatusCompact.


        :param last_diagnostics_date: The last_diagnostics_date of this V2InstrumentStatusCompact.  # noqa: E501
        :type: datetime
        """

        self._last_diagnostics_date = last_diagnostics_date

    @property
    def last_software_update_check_date(self):
        """Gets the last_software_update_check_date of this V2InstrumentStatusCompact.  # noqa: E501


        :return: The last_software_update_check_date of this V2InstrumentStatusCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._last_software_update_check_date

    @last_software_update_check_date.setter
    def last_software_update_check_date(self, last_software_update_check_date):
        """Sets the last_software_update_check_date of this V2InstrumentStatusCompact.


        :param last_software_update_check_date: The last_software_update_check_date of this V2InstrumentStatusCompact.  # noqa: E501
        :type: datetime
        """

        self._last_software_update_check_date = last_software_update_check_date

    @property
    def id(self):
        """Gets the id of this V2InstrumentStatusCompact.  # noqa: E501


        :return: The id of this V2InstrumentStatusCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V2InstrumentStatusCompact.


        :param id: The id of this V2InstrumentStatusCompact.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this V2InstrumentStatusCompact.  # noqa: E501


        :return: The name of this V2InstrumentStatusCompact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2InstrumentStatusCompact.


        :param name: The name of this V2InstrumentStatusCompact.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(V2InstrumentStatusCompact, dict):
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
        if not isinstance(other, V2InstrumentStatusCompact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
