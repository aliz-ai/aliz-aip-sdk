# coding: utf-8

"""
    Aliz AIP REST API

    AIP Workspace API.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: aip-support@aliz.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MpmHistoricalPlotDataDto(object):
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
        '_date': 'datetime',
        'plot_data_items': 'dict(str, list[object])',
        'class_names': 'list[str]'
    }

    attribute_map = {
        '_date': 'date',
        'plot_data_items': 'plotDataItems',
        'class_names': 'classNames'
    }

    def __init__(self, _date=None, plot_data_items=None, class_names=None):  # noqa: E501
        """MpmHistoricalPlotDataDto - a model defined in Swagger"""  # noqa: E501
        self.__date = None
        self._plot_data_items = None
        self._class_names = None
        self.discriminator = None
        if _date is not None:
            self._date = _date
        if plot_data_items is not None:
            self.plot_data_items = plot_data_items
        if class_names is not None:
            self.class_names = class_names

    @property
    def _date(self):
        """Gets the _date of this MpmHistoricalPlotDataDto.  # noqa: E501


        :return: The _date of this MpmHistoricalPlotDataDto.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this MpmHistoricalPlotDataDto.


        :param _date: The _date of this MpmHistoricalPlotDataDto.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def plot_data_items(self):
        """Gets the plot_data_items of this MpmHistoricalPlotDataDto.  # noqa: E501


        :return: The plot_data_items of this MpmHistoricalPlotDataDto.  # noqa: E501
        :rtype: dict(str, list[object])
        """
        return self._plot_data_items

    @plot_data_items.setter
    def plot_data_items(self, plot_data_items):
        """Sets the plot_data_items of this MpmHistoricalPlotDataDto.


        :param plot_data_items: The plot_data_items of this MpmHistoricalPlotDataDto.  # noqa: E501
        :type: dict(str, list[object])
        """

        self._plot_data_items = plot_data_items

    @property
    def class_names(self):
        """Gets the class_names of this MpmHistoricalPlotDataDto.  # noqa: E501


        :return: The class_names of this MpmHistoricalPlotDataDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._class_names

    @class_names.setter
    def class_names(self, class_names):
        """Sets the class_names of this MpmHistoricalPlotDataDto.


        :param class_names: The class_names of this MpmHistoricalPlotDataDto.  # noqa: E501
        :type: list[str]
        """

        self._class_names = class_names

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
        if issubclass(MpmHistoricalPlotDataDto, dict):
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
        if not isinstance(other, MpmHistoricalPlotDataDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
