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

class CreateMpmModelDto(object):
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
        'name': 'str',
        'model_type': 'str',
        'main_evaluation_metric_type': 'str',
        'model_periodicity': 'str'
    }

    attribute_map = {
        'name': 'name',
        'model_type': 'modelType',
        'main_evaluation_metric_type': 'mainEvaluationMetricType',
        'model_periodicity': 'modelPeriodicity'
    }

    def __init__(self, name=None, model_type=None, main_evaluation_metric_type=None, model_periodicity=None):  # noqa: E501
        """CreateMpmModelDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._model_type = None
        self._main_evaluation_metric_type = None
        self._model_periodicity = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if model_type is not None:
            self.model_type = model_type
        if main_evaluation_metric_type is not None:
            self.main_evaluation_metric_type = main_evaluation_metric_type
        if model_periodicity is not None:
            self.model_periodicity = model_periodicity

    @property
    def name(self):
        """Gets the name of this CreateMpmModelDto.  # noqa: E501


        :return: The name of this CreateMpmModelDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateMpmModelDto.


        :param name: The name of this CreateMpmModelDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def model_type(self):
        """Gets the model_type of this CreateMpmModelDto.  # noqa: E501


        :return: The model_type of this CreateMpmModelDto.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this CreateMpmModelDto.


        :param model_type: The model_type of this CreateMpmModelDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["REGRESSION", "CLASSIFICATION"]  # noqa: E501
        if model_type not in allowed_values:
            raise ValueError(
                "Invalid value for `model_type` ({0}), must be one of {1}"  # noqa: E501
                .format(model_type, allowed_values)
            )

        self._model_type = model_type

    @property
    def main_evaluation_metric_type(self):
        """Gets the main_evaluation_metric_type of this CreateMpmModelDto.  # noqa: E501


        :return: The main_evaluation_metric_type of this CreateMpmModelDto.  # noqa: E501
        :rtype: str
        """
        return self._main_evaluation_metric_type

    @main_evaluation_metric_type.setter
    def main_evaluation_metric_type(self, main_evaluation_metric_type):
        """Sets the main_evaluation_metric_type of this CreateMpmModelDto.


        :param main_evaluation_metric_type: The main_evaluation_metric_type of this CreateMpmModelDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["FEATURE_DRIFT"]  # noqa: E501
        if main_evaluation_metric_type not in allowed_values:
            raise ValueError(
                "Invalid value for `main_evaluation_metric_type` ({0}), must be one of {1}"  # noqa: E501
                .format(main_evaluation_metric_type, allowed_values)
            )

        self._main_evaluation_metric_type = main_evaluation_metric_type

    @property
    def model_periodicity(self):
        """Gets the model_periodicity of this CreateMpmModelDto.  # noqa: E501


        :return: The model_periodicity of this CreateMpmModelDto.  # noqa: E501
        :rtype: str
        """
        return self._model_periodicity

    @model_periodicity.setter
    def model_periodicity(self, model_periodicity):
        """Sets the model_periodicity of this CreateMpmModelDto.


        :param model_periodicity: The model_periodicity of this CreateMpmModelDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["DAY", "WEEK", "MONTH"]  # noqa: E501
        if model_periodicity not in allowed_values:
            raise ValueError(
                "Invalid value for `model_periodicity` ({0}), must be one of {1}"  # noqa: E501
                .format(model_periodicity, allowed_values)
            )

        self._model_periodicity = model_periodicity

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
        if issubclass(CreateMpmModelDto, dict):
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
        if not isinstance(other, CreateMpmModelDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
