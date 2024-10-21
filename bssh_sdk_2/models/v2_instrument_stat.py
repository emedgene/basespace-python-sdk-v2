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

class V2InstrumentStat(object):
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
        'instrument_id': 'int',
        'name': 'str',
        'serial_number': 'str',
        'instrument_type': 'str',
        'total_run_time': 'float',
        'from_date': 'DateTimeOffset',
        'to_date': 'DateTimeOffset',
        'incomplete_runs_excluded': 'bool',
        'bins': 'list[V2InstrumentStatsBin]'
    }

    attribute_map = {
        'instrument_id': 'InstrumentId',
        'name': 'Name',
        'serial_number': 'SerialNumber',
        'instrument_type': 'InstrumentType',
        'total_run_time': 'TotalRunTime',
        'from_date': 'FromDate',
        'to_date': 'ToDate',
        'incomplete_runs_excluded': 'IncompleteRunsExcluded',
        'bins': 'Bins'
    }

    def __init__(self, instrument_id=None, name=None, serial_number=None, instrument_type=None, total_run_time=None, from_date=None, to_date=None, incomplete_runs_excluded=None, bins=None):  # noqa: E501
        """V2InstrumentStat - a model defined in Swagger"""  # noqa: E501
        self._instrument_id = None
        self._name = None
        self._serial_number = None
        self._instrument_type = None
        self._total_run_time = None
        self._from_date = None
        self._to_date = None
        self._incomplete_runs_excluded = None
        self._bins = None
        self.discriminator = None
        self.instrument_id = instrument_id
        self.name = name
        self.serial_number = serial_number
        self.instrument_type = instrument_type
        self.total_run_time = total_run_time
        self.from_date = from_date
        self.to_date = to_date
        self.incomplete_runs_excluded = incomplete_runs_excluded
        self.bins = bins

    @property
    def instrument_id(self):
        """Gets the instrument_id of this V2InstrumentStat.  # noqa: E501


        :return: The instrument_id of this V2InstrumentStat.  # noqa: E501
        :rtype: int
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """Sets the instrument_id of this V2InstrumentStat.


        :param instrument_id: The instrument_id of this V2InstrumentStat.  # noqa: E501
        :type: int
        """
        if instrument_id is None:
            raise ValueError("Invalid value for `instrument_id`, must not be `None`")  # noqa: E501

        self._instrument_id = instrument_id

    @property
    def name(self):
        """Gets the name of this V2InstrumentStat.  # noqa: E501


        :return: The name of this V2InstrumentStat.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2InstrumentStat.


        :param name: The name of this V2InstrumentStat.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def serial_number(self):
        """Gets the serial_number of this V2InstrumentStat.  # noqa: E501


        :return: The serial_number of this V2InstrumentStat.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this V2InstrumentStat.


        :param serial_number: The serial_number of this V2InstrumentStat.  # noqa: E501
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def instrument_type(self):
        """Gets the instrument_type of this V2InstrumentStat.  # noqa: E501


        :return: The instrument_type of this V2InstrumentStat.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this V2InstrumentStat.


        :param instrument_type: The instrument_type of this V2InstrumentStat.  # noqa: E501
        :type: str
        """
        if instrument_type is None:
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501

        self._instrument_type = instrument_type

    @property
    def total_run_time(self):
        """Gets the total_run_time of this V2InstrumentStat.  # noqa: E501


        :return: The total_run_time of this V2InstrumentStat.  # noqa: E501
        :rtype: float
        """
        return self._total_run_time

    @total_run_time.setter
    def total_run_time(self, total_run_time):
        """Sets the total_run_time of this V2InstrumentStat.


        :param total_run_time: The total_run_time of this V2InstrumentStat.  # noqa: E501
        :type: float
        """
        if total_run_time is None:
            raise ValueError("Invalid value for `total_run_time`, must not be `None`")  # noqa: E501

        self._total_run_time = total_run_time

    @property
    def from_date(self):
        """Gets the from_date of this V2InstrumentStat.  # noqa: E501


        :return: The from_date of this V2InstrumentStat.  # noqa: E501
        :rtype: DateTimeOffset
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this V2InstrumentStat.


        :param from_date: The from_date of this V2InstrumentStat.  # noqa: E501
        :type: DateTimeOffset
        """
        if from_date is None:
            raise ValueError("Invalid value for `from_date`, must not be `None`")  # noqa: E501

        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this V2InstrumentStat.  # noqa: E501


        :return: The to_date of this V2InstrumentStat.  # noqa: E501
        :rtype: DateTimeOffset
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this V2InstrumentStat.


        :param to_date: The to_date of this V2InstrumentStat.  # noqa: E501
        :type: DateTimeOffset
        """
        if to_date is None:
            raise ValueError("Invalid value for `to_date`, must not be `None`")  # noqa: E501

        self._to_date = to_date

    @property
    def incomplete_runs_excluded(self):
        """Gets the incomplete_runs_excluded of this V2InstrumentStat.  # noqa: E501


        :return: The incomplete_runs_excluded of this V2InstrumentStat.  # noqa: E501
        :rtype: bool
        """
        return self._incomplete_runs_excluded

    @incomplete_runs_excluded.setter
    def incomplete_runs_excluded(self, incomplete_runs_excluded):
        """Sets the incomplete_runs_excluded of this V2InstrumentStat.


        :param incomplete_runs_excluded: The incomplete_runs_excluded of this V2InstrumentStat.  # noqa: E501
        :type: bool
        """
        if incomplete_runs_excluded is None:
            raise ValueError("Invalid value for `incomplete_runs_excluded`, must not be `None`")  # noqa: E501

        self._incomplete_runs_excluded = incomplete_runs_excluded

    @property
    def bins(self):
        """Gets the bins of this V2InstrumentStat.  # noqa: E501


        :return: The bins of this V2InstrumentStat.  # noqa: E501
        :rtype: list[V2InstrumentStatsBin]
        """
        return self._bins

    @bins.setter
    def bins(self, bins):
        """Sets the bins of this V2InstrumentStat.


        :param bins: The bins of this V2InstrumentStat.  # noqa: E501
        :type: list[V2InstrumentStatsBin]
        """
        if bins is None:
            raise ValueError("Invalid value for `bins`, must not be `None`")  # noqa: E501

        self._bins = bins

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
        if issubclass(V2InstrumentStat, dict):
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
        if not isinstance(other, V2InstrumentStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
