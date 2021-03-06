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

class AuthorizeManagedServiceDto(object):
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
        'principals': 'list[ManagedServiceUserDto]'
    }

    attribute_map = {
        'principals': 'principals'
    }

    def __init__(self, principals=None):  # noqa: E501
        """AuthorizeManagedServiceDto - a model defined in Swagger"""  # noqa: E501
        self._principals = None
        self.discriminator = None
        if principals is not None:
            self.principals = principals

    @property
    def principals(self):
        """Gets the principals of this AuthorizeManagedServiceDto.  # noqa: E501


        :return: The principals of this AuthorizeManagedServiceDto.  # noqa: E501
        :rtype: list[ManagedServiceUserDto]
        """
        return self._principals

    @principals.setter
    def principals(self, principals):
        """Sets the principals of this AuthorizeManagedServiceDto.


        :param principals: The principals of this AuthorizeManagedServiceDto.  # noqa: E501
        :type: list[ManagedServiceUserDto]
        """

        self._principals = principals

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
        if issubclass(AuthorizeManagedServiceDto, dict):
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
        if not isinstance(other, AuthorizeManagedServiceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
