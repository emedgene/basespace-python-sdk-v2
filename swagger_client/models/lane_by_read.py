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

class LaneByRead(object):
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
        'read_number': 'int',
        'lane_number': 'int',
        'tile_count': 'int',
        'density': 'float',
        'density_deviation': 'float',
        'percent_pf': 'float',
        'percent_pf_deviation': 'float',
        'phasing': 'float',
        'pre_phasing': 'float',
        'reads': 'int',
        'reads_pf': 'int',
        'percent_gt_q30': 'float',
        'percent_gt_q30_last10_cycles': 'float',
        '_yield': 'float',
        'min_cycle_called': 'int',
        'max_cycle_called': 'int',
        'min_cycle_error': 'int',
        'max_cycle_error': 'int',
        'percent_aligned': 'float',
        'percent_aligned_deviation': 'float',
        'error_rate': 'float',
        'error_rate_deviation': 'float',
        'error_rate35': 'float',
        'error_rate35_deviation': 'float',
        'error_rate50': 'float',
        'error_rate50_deviation': 'float',
        'error_rate75': 'float',
        'error_rate75_deviation': 'float',
        'error_rate100': 'float',
        'error_rate100_deviation': 'float',
        'intensity_cycle1': 'float',
        'intensity_cycle1_deviation': 'float',
        'phasing_slope': 'float',
        'phasing_offset': 'float',
        'pre_phasing_slope': 'float',
        'pre_phasing_offset': 'float',
        'percent_no_calls': 'float',
        'cluster_density': 'float',
        'occupancy': 'float'
    }

    attribute_map = {
        'read_number': 'ReadNumber',
        'lane_number': 'LaneNumber',
        'tile_count': 'TileCount',
        'density': 'Density',
        'density_deviation': 'DensityDeviation',
        'percent_pf': 'PercentPf',
        'percent_pf_deviation': 'PercentPfDeviation',
        'phasing': 'Phasing',
        'pre_phasing': 'PrePhasing',
        'reads': 'Reads',
        'reads_pf': 'ReadsPf',
        'percent_gt_q30': 'PercentGtQ30',
        'percent_gt_q30_last10_cycles': 'PercentGtQ30Last10Cycles',
        '_yield': 'Yield',
        'min_cycle_called': 'MinCycleCalled',
        'max_cycle_called': 'MaxCycleCalled',
        'min_cycle_error': 'MinCycleError',
        'max_cycle_error': 'MaxCycleError',
        'percent_aligned': 'PercentAligned',
        'percent_aligned_deviation': 'PercentAlignedDeviation',
        'error_rate': 'ErrorRate',
        'error_rate_deviation': 'ErrorRateDeviation',
        'error_rate35': 'ErrorRate35',
        'error_rate35_deviation': 'ErrorRate35Deviation',
        'error_rate50': 'ErrorRate50',
        'error_rate50_deviation': 'ErrorRate50Deviation',
        'error_rate75': 'ErrorRate75',
        'error_rate75_deviation': 'ErrorRate75Deviation',
        'error_rate100': 'ErrorRate100',
        'error_rate100_deviation': 'ErrorRate100Deviation',
        'intensity_cycle1': 'IntensityCycle1',
        'intensity_cycle1_deviation': 'IntensityCycle1Deviation',
        'phasing_slope': 'PhasingSlope',
        'phasing_offset': 'PhasingOffset',
        'pre_phasing_slope': 'PrePhasingSlope',
        'pre_phasing_offset': 'PrePhasingOffset',
        'percent_no_calls': 'PercentNoCalls',
        'cluster_density': 'ClusterDensity',
        'occupancy': 'Occupancy'
    }

    def __init__(self, read_number=None, lane_number=None, tile_count=None, density=None, density_deviation=None, percent_pf=None, percent_pf_deviation=None, phasing=None, pre_phasing=None, reads=None, reads_pf=None, percent_gt_q30=None, percent_gt_q30_last10_cycles=None, _yield=None, min_cycle_called=None, max_cycle_called=None, min_cycle_error=None, max_cycle_error=None, percent_aligned=None, percent_aligned_deviation=None, error_rate=None, error_rate_deviation=None, error_rate35=None, error_rate35_deviation=None, error_rate50=None, error_rate50_deviation=None, error_rate75=None, error_rate75_deviation=None, error_rate100=None, error_rate100_deviation=None, intensity_cycle1=None, intensity_cycle1_deviation=None, phasing_slope=None, phasing_offset=None, pre_phasing_slope=None, pre_phasing_offset=None, percent_no_calls=None, cluster_density=None, occupancy=None):  # noqa: E501
        """LaneByRead - a model defined in Swagger"""  # noqa: E501
        self._read_number = None
        self._lane_number = None
        self._tile_count = None
        self._density = None
        self._density_deviation = None
        self._percent_pf = None
        self._percent_pf_deviation = None
        self._phasing = None
        self._pre_phasing = None
        self._reads = None
        self._reads_pf = None
        self._percent_gt_q30 = None
        self._percent_gt_q30_last10_cycles = None
        self.__yield = None
        self._min_cycle_called = None
        self._max_cycle_called = None
        self._min_cycle_error = None
        self._max_cycle_error = None
        self._percent_aligned = None
        self._percent_aligned_deviation = None
        self._error_rate = None
        self._error_rate_deviation = None
        self._error_rate35 = None
        self._error_rate35_deviation = None
        self._error_rate50 = None
        self._error_rate50_deviation = None
        self._error_rate75 = None
        self._error_rate75_deviation = None
        self._error_rate100 = None
        self._error_rate100_deviation = None
        self._intensity_cycle1 = None
        self._intensity_cycle1_deviation = None
        self._phasing_slope = None
        self._phasing_offset = None
        self._pre_phasing_slope = None
        self._pre_phasing_offset = None
        self._percent_no_calls = None
        self._cluster_density = None
        self._occupancy = None
        self.discriminator = None
        if read_number is not None:
            self.read_number = read_number
        if lane_number is not None:
            self.lane_number = lane_number
        if tile_count is not None:
            self.tile_count = tile_count
        if density is not None:
            self.density = density
        if density_deviation is not None:
            self.density_deviation = density_deviation
        if percent_pf is not None:
            self.percent_pf = percent_pf
        if percent_pf_deviation is not None:
            self.percent_pf_deviation = percent_pf_deviation
        if phasing is not None:
            self.phasing = phasing
        if pre_phasing is not None:
            self.pre_phasing = pre_phasing
        if reads is not None:
            self.reads = reads
        if reads_pf is not None:
            self.reads_pf = reads_pf
        if percent_gt_q30 is not None:
            self.percent_gt_q30 = percent_gt_q30
        if percent_gt_q30_last10_cycles is not None:
            self.percent_gt_q30_last10_cycles = percent_gt_q30_last10_cycles
        if _yield is not None:
            self._yield = _yield
        if min_cycle_called is not None:
            self.min_cycle_called = min_cycle_called
        if max_cycle_called is not None:
            self.max_cycle_called = max_cycle_called
        if min_cycle_error is not None:
            self.min_cycle_error = min_cycle_error
        if max_cycle_error is not None:
            self.max_cycle_error = max_cycle_error
        if percent_aligned is not None:
            self.percent_aligned = percent_aligned
        if percent_aligned_deviation is not None:
            self.percent_aligned_deviation = percent_aligned_deviation
        if error_rate is not None:
            self.error_rate = error_rate
        if error_rate_deviation is not None:
            self.error_rate_deviation = error_rate_deviation
        if error_rate35 is not None:
            self.error_rate35 = error_rate35
        if error_rate35_deviation is not None:
            self.error_rate35_deviation = error_rate35_deviation
        if error_rate50 is not None:
            self.error_rate50 = error_rate50
        if error_rate50_deviation is not None:
            self.error_rate50_deviation = error_rate50_deviation
        if error_rate75 is not None:
            self.error_rate75 = error_rate75
        if error_rate75_deviation is not None:
            self.error_rate75_deviation = error_rate75_deviation
        if error_rate100 is not None:
            self.error_rate100 = error_rate100
        if error_rate100_deviation is not None:
            self.error_rate100_deviation = error_rate100_deviation
        if intensity_cycle1 is not None:
            self.intensity_cycle1 = intensity_cycle1
        if intensity_cycle1_deviation is not None:
            self.intensity_cycle1_deviation = intensity_cycle1_deviation
        if phasing_slope is not None:
            self.phasing_slope = phasing_slope
        if phasing_offset is not None:
            self.phasing_offset = phasing_offset
        if pre_phasing_slope is not None:
            self.pre_phasing_slope = pre_phasing_slope
        if pre_phasing_offset is not None:
            self.pre_phasing_offset = pre_phasing_offset
        if percent_no_calls is not None:
            self.percent_no_calls = percent_no_calls
        if cluster_density is not None:
            self.cluster_density = cluster_density
        if occupancy is not None:
            self.occupancy = occupancy

    @property
    def read_number(self):
        """Gets the read_number of this LaneByRead.  # noqa: E501


        :return: The read_number of this LaneByRead.  # noqa: E501
        :rtype: int
        """
        return self._read_number

    @read_number.setter
    def read_number(self, read_number):
        """Sets the read_number of this LaneByRead.


        :param read_number: The read_number of this LaneByRead.  # noqa: E501
        :type: int
        """

        self._read_number = read_number

    @property
    def lane_number(self):
        """Gets the lane_number of this LaneByRead.  # noqa: E501


        :return: The lane_number of this LaneByRead.  # noqa: E501
        :rtype: int
        """
        return self._lane_number

    @lane_number.setter
    def lane_number(self, lane_number):
        """Sets the lane_number of this LaneByRead.


        :param lane_number: The lane_number of this LaneByRead.  # noqa: E501
        :type: int
        """

        self._lane_number = lane_number

    @property
    def tile_count(self):
        """Gets the tile_count of this LaneByRead.  # noqa: E501


        :return: The tile_count of this LaneByRead.  # noqa: E501
        :rtype: int
        """
        return self._tile_count

    @tile_count.setter
    def tile_count(self, tile_count):
        """Sets the tile_count of this LaneByRead.


        :param tile_count: The tile_count of this LaneByRead.  # noqa: E501
        :type: int
        """

        self._tile_count = tile_count

    @property
    def density(self):
        """Gets the density of this LaneByRead.  # noqa: E501


        :return: The density of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._density

    @density.setter
    def density(self, density):
        """Sets the density of this LaneByRead.


        :param density: The density of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._density = density

    @property
    def density_deviation(self):
        """Gets the density_deviation of this LaneByRead.  # noqa: E501


        :return: The density_deviation of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._density_deviation

    @density_deviation.setter
    def density_deviation(self, density_deviation):
        """Sets the density_deviation of this LaneByRead.


        :param density_deviation: The density_deviation of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._density_deviation = density_deviation

    @property
    def percent_pf(self):
        """Gets the percent_pf of this LaneByRead.  # noqa: E501


        :return: The percent_pf of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._percent_pf

    @percent_pf.setter
    def percent_pf(self, percent_pf):
        """Sets the percent_pf of this LaneByRead.


        :param percent_pf: The percent_pf of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._percent_pf = percent_pf

    @property
    def percent_pf_deviation(self):
        """Gets the percent_pf_deviation of this LaneByRead.  # noqa: E501


        :return: The percent_pf_deviation of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._percent_pf_deviation

    @percent_pf_deviation.setter
    def percent_pf_deviation(self, percent_pf_deviation):
        """Sets the percent_pf_deviation of this LaneByRead.


        :param percent_pf_deviation: The percent_pf_deviation of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._percent_pf_deviation = percent_pf_deviation

    @property
    def phasing(self):
        """Gets the phasing of this LaneByRead.  # noqa: E501


        :return: The phasing of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._phasing

    @phasing.setter
    def phasing(self, phasing):
        """Sets the phasing of this LaneByRead.


        :param phasing: The phasing of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._phasing = phasing

    @property
    def pre_phasing(self):
        """Gets the pre_phasing of this LaneByRead.  # noqa: E501


        :return: The pre_phasing of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._pre_phasing

    @pre_phasing.setter
    def pre_phasing(self, pre_phasing):
        """Sets the pre_phasing of this LaneByRead.


        :param pre_phasing: The pre_phasing of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._pre_phasing = pre_phasing

    @property
    def reads(self):
        """Gets the reads of this LaneByRead.  # noqa: E501


        :return: The reads of this LaneByRead.  # noqa: E501
        :rtype: int
        """
        return self._reads

    @reads.setter
    def reads(self, reads):
        """Sets the reads of this LaneByRead.


        :param reads: The reads of this LaneByRead.  # noqa: E501
        :type: int
        """

        self._reads = reads

    @property
    def reads_pf(self):
        """Gets the reads_pf of this LaneByRead.  # noqa: E501


        :return: The reads_pf of this LaneByRead.  # noqa: E501
        :rtype: int
        """
        return self._reads_pf

    @reads_pf.setter
    def reads_pf(self, reads_pf):
        """Sets the reads_pf of this LaneByRead.


        :param reads_pf: The reads_pf of this LaneByRead.  # noqa: E501
        :type: int
        """

        self._reads_pf = reads_pf

    @property
    def percent_gt_q30(self):
        """Gets the percent_gt_q30 of this LaneByRead.  # noqa: E501


        :return: The percent_gt_q30 of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._percent_gt_q30

    @percent_gt_q30.setter
    def percent_gt_q30(self, percent_gt_q30):
        """Sets the percent_gt_q30 of this LaneByRead.


        :param percent_gt_q30: The percent_gt_q30 of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._percent_gt_q30 = percent_gt_q30

    @property
    def percent_gt_q30_last10_cycles(self):
        """Gets the percent_gt_q30_last10_cycles of this LaneByRead.  # noqa: E501


        :return: The percent_gt_q30_last10_cycles of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._percent_gt_q30_last10_cycles

    @percent_gt_q30_last10_cycles.setter
    def percent_gt_q30_last10_cycles(self, percent_gt_q30_last10_cycles):
        """Sets the percent_gt_q30_last10_cycles of this LaneByRead.


        :param percent_gt_q30_last10_cycles: The percent_gt_q30_last10_cycles of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._percent_gt_q30_last10_cycles = percent_gt_q30_last10_cycles

    @property
    def _yield(self):
        """Gets the _yield of this LaneByRead.  # noqa: E501


        :return: The _yield of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self.__yield

    @_yield.setter
    def _yield(self, _yield):
        """Sets the _yield of this LaneByRead.


        :param _yield: The _yield of this LaneByRead.  # noqa: E501
        :type: float
        """

        self.__yield = _yield

    @property
    def min_cycle_called(self):
        """Gets the min_cycle_called of this LaneByRead.  # noqa: E501


        :return: The min_cycle_called of this LaneByRead.  # noqa: E501
        :rtype: int
        """
        return self._min_cycle_called

    @min_cycle_called.setter
    def min_cycle_called(self, min_cycle_called):
        """Sets the min_cycle_called of this LaneByRead.


        :param min_cycle_called: The min_cycle_called of this LaneByRead.  # noqa: E501
        :type: int
        """

        self._min_cycle_called = min_cycle_called

    @property
    def max_cycle_called(self):
        """Gets the max_cycle_called of this LaneByRead.  # noqa: E501


        :return: The max_cycle_called of this LaneByRead.  # noqa: E501
        :rtype: int
        """
        return self._max_cycle_called

    @max_cycle_called.setter
    def max_cycle_called(self, max_cycle_called):
        """Sets the max_cycle_called of this LaneByRead.


        :param max_cycle_called: The max_cycle_called of this LaneByRead.  # noqa: E501
        :type: int
        """

        self._max_cycle_called = max_cycle_called

    @property
    def min_cycle_error(self):
        """Gets the min_cycle_error of this LaneByRead.  # noqa: E501


        :return: The min_cycle_error of this LaneByRead.  # noqa: E501
        :rtype: int
        """
        return self._min_cycle_error

    @min_cycle_error.setter
    def min_cycle_error(self, min_cycle_error):
        """Sets the min_cycle_error of this LaneByRead.


        :param min_cycle_error: The min_cycle_error of this LaneByRead.  # noqa: E501
        :type: int
        """

        self._min_cycle_error = min_cycle_error

    @property
    def max_cycle_error(self):
        """Gets the max_cycle_error of this LaneByRead.  # noqa: E501


        :return: The max_cycle_error of this LaneByRead.  # noqa: E501
        :rtype: int
        """
        return self._max_cycle_error

    @max_cycle_error.setter
    def max_cycle_error(self, max_cycle_error):
        """Sets the max_cycle_error of this LaneByRead.


        :param max_cycle_error: The max_cycle_error of this LaneByRead.  # noqa: E501
        :type: int
        """

        self._max_cycle_error = max_cycle_error

    @property
    def percent_aligned(self):
        """Gets the percent_aligned of this LaneByRead.  # noqa: E501


        :return: The percent_aligned of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._percent_aligned

    @percent_aligned.setter
    def percent_aligned(self, percent_aligned):
        """Sets the percent_aligned of this LaneByRead.


        :param percent_aligned: The percent_aligned of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._percent_aligned = percent_aligned

    @property
    def percent_aligned_deviation(self):
        """Gets the percent_aligned_deviation of this LaneByRead.  # noqa: E501


        :return: The percent_aligned_deviation of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._percent_aligned_deviation

    @percent_aligned_deviation.setter
    def percent_aligned_deviation(self, percent_aligned_deviation):
        """Sets the percent_aligned_deviation of this LaneByRead.


        :param percent_aligned_deviation: The percent_aligned_deviation of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._percent_aligned_deviation = percent_aligned_deviation

    @property
    def error_rate(self):
        """Gets the error_rate of this LaneByRead.  # noqa: E501


        :return: The error_rate of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._error_rate

    @error_rate.setter
    def error_rate(self, error_rate):
        """Sets the error_rate of this LaneByRead.


        :param error_rate: The error_rate of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._error_rate = error_rate

    @property
    def error_rate_deviation(self):
        """Gets the error_rate_deviation of this LaneByRead.  # noqa: E501


        :return: The error_rate_deviation of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._error_rate_deviation

    @error_rate_deviation.setter
    def error_rate_deviation(self, error_rate_deviation):
        """Sets the error_rate_deviation of this LaneByRead.


        :param error_rate_deviation: The error_rate_deviation of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._error_rate_deviation = error_rate_deviation

    @property
    def error_rate35(self):
        """Gets the error_rate35 of this LaneByRead.  # noqa: E501


        :return: The error_rate35 of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._error_rate35

    @error_rate35.setter
    def error_rate35(self, error_rate35):
        """Sets the error_rate35 of this LaneByRead.


        :param error_rate35: The error_rate35 of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._error_rate35 = error_rate35

    @property
    def error_rate35_deviation(self):
        """Gets the error_rate35_deviation of this LaneByRead.  # noqa: E501


        :return: The error_rate35_deviation of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._error_rate35_deviation

    @error_rate35_deviation.setter
    def error_rate35_deviation(self, error_rate35_deviation):
        """Sets the error_rate35_deviation of this LaneByRead.


        :param error_rate35_deviation: The error_rate35_deviation of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._error_rate35_deviation = error_rate35_deviation

    @property
    def error_rate50(self):
        """Gets the error_rate50 of this LaneByRead.  # noqa: E501


        :return: The error_rate50 of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._error_rate50

    @error_rate50.setter
    def error_rate50(self, error_rate50):
        """Sets the error_rate50 of this LaneByRead.


        :param error_rate50: The error_rate50 of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._error_rate50 = error_rate50

    @property
    def error_rate50_deviation(self):
        """Gets the error_rate50_deviation of this LaneByRead.  # noqa: E501


        :return: The error_rate50_deviation of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._error_rate50_deviation

    @error_rate50_deviation.setter
    def error_rate50_deviation(self, error_rate50_deviation):
        """Sets the error_rate50_deviation of this LaneByRead.


        :param error_rate50_deviation: The error_rate50_deviation of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._error_rate50_deviation = error_rate50_deviation

    @property
    def error_rate75(self):
        """Gets the error_rate75 of this LaneByRead.  # noqa: E501


        :return: The error_rate75 of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._error_rate75

    @error_rate75.setter
    def error_rate75(self, error_rate75):
        """Sets the error_rate75 of this LaneByRead.


        :param error_rate75: The error_rate75 of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._error_rate75 = error_rate75

    @property
    def error_rate75_deviation(self):
        """Gets the error_rate75_deviation of this LaneByRead.  # noqa: E501


        :return: The error_rate75_deviation of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._error_rate75_deviation

    @error_rate75_deviation.setter
    def error_rate75_deviation(self, error_rate75_deviation):
        """Sets the error_rate75_deviation of this LaneByRead.


        :param error_rate75_deviation: The error_rate75_deviation of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._error_rate75_deviation = error_rate75_deviation

    @property
    def error_rate100(self):
        """Gets the error_rate100 of this LaneByRead.  # noqa: E501


        :return: The error_rate100 of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._error_rate100

    @error_rate100.setter
    def error_rate100(self, error_rate100):
        """Sets the error_rate100 of this LaneByRead.


        :param error_rate100: The error_rate100 of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._error_rate100 = error_rate100

    @property
    def error_rate100_deviation(self):
        """Gets the error_rate100_deviation of this LaneByRead.  # noqa: E501


        :return: The error_rate100_deviation of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._error_rate100_deviation

    @error_rate100_deviation.setter
    def error_rate100_deviation(self, error_rate100_deviation):
        """Sets the error_rate100_deviation of this LaneByRead.


        :param error_rate100_deviation: The error_rate100_deviation of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._error_rate100_deviation = error_rate100_deviation

    @property
    def intensity_cycle1(self):
        """Gets the intensity_cycle1 of this LaneByRead.  # noqa: E501


        :return: The intensity_cycle1 of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._intensity_cycle1

    @intensity_cycle1.setter
    def intensity_cycle1(self, intensity_cycle1):
        """Sets the intensity_cycle1 of this LaneByRead.


        :param intensity_cycle1: The intensity_cycle1 of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._intensity_cycle1 = intensity_cycle1

    @property
    def intensity_cycle1_deviation(self):
        """Gets the intensity_cycle1_deviation of this LaneByRead.  # noqa: E501


        :return: The intensity_cycle1_deviation of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._intensity_cycle1_deviation

    @intensity_cycle1_deviation.setter
    def intensity_cycle1_deviation(self, intensity_cycle1_deviation):
        """Sets the intensity_cycle1_deviation of this LaneByRead.


        :param intensity_cycle1_deviation: The intensity_cycle1_deviation of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._intensity_cycle1_deviation = intensity_cycle1_deviation

    @property
    def phasing_slope(self):
        """Gets the phasing_slope of this LaneByRead.  # noqa: E501


        :return: The phasing_slope of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._phasing_slope

    @phasing_slope.setter
    def phasing_slope(self, phasing_slope):
        """Sets the phasing_slope of this LaneByRead.


        :param phasing_slope: The phasing_slope of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._phasing_slope = phasing_slope

    @property
    def phasing_offset(self):
        """Gets the phasing_offset of this LaneByRead.  # noqa: E501


        :return: The phasing_offset of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._phasing_offset

    @phasing_offset.setter
    def phasing_offset(self, phasing_offset):
        """Sets the phasing_offset of this LaneByRead.


        :param phasing_offset: The phasing_offset of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._phasing_offset = phasing_offset

    @property
    def pre_phasing_slope(self):
        """Gets the pre_phasing_slope of this LaneByRead.  # noqa: E501


        :return: The pre_phasing_slope of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._pre_phasing_slope

    @pre_phasing_slope.setter
    def pre_phasing_slope(self, pre_phasing_slope):
        """Sets the pre_phasing_slope of this LaneByRead.


        :param pre_phasing_slope: The pre_phasing_slope of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._pre_phasing_slope = pre_phasing_slope

    @property
    def pre_phasing_offset(self):
        """Gets the pre_phasing_offset of this LaneByRead.  # noqa: E501


        :return: The pre_phasing_offset of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._pre_phasing_offset

    @pre_phasing_offset.setter
    def pre_phasing_offset(self, pre_phasing_offset):
        """Sets the pre_phasing_offset of this LaneByRead.


        :param pre_phasing_offset: The pre_phasing_offset of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._pre_phasing_offset = pre_phasing_offset

    @property
    def percent_no_calls(self):
        """Gets the percent_no_calls of this LaneByRead.  # noqa: E501


        :return: The percent_no_calls of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._percent_no_calls

    @percent_no_calls.setter
    def percent_no_calls(self, percent_no_calls):
        """Sets the percent_no_calls of this LaneByRead.


        :param percent_no_calls: The percent_no_calls of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._percent_no_calls = percent_no_calls

    @property
    def cluster_density(self):
        """Gets the cluster_density of this LaneByRead.  # noqa: E501


        :return: The cluster_density of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._cluster_density

    @cluster_density.setter
    def cluster_density(self, cluster_density):
        """Sets the cluster_density of this LaneByRead.


        :param cluster_density: The cluster_density of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._cluster_density = cluster_density

    @property
    def occupancy(self):
        """Gets the occupancy of this LaneByRead.  # noqa: E501


        :return: The occupancy of this LaneByRead.  # noqa: E501
        :rtype: float
        """
        return self._occupancy

    @occupancy.setter
    def occupancy(self, occupancy):
        """Sets the occupancy of this LaneByRead.


        :param occupancy: The occupancy of this LaneByRead.  # noqa: E501
        :type: float
        """

        self._occupancy = occupancy

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
        if issubclass(LaneByRead, dict):
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
        if not isinstance(other, LaneByRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
