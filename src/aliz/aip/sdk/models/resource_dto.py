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

class ResourceDto(object):
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
        'name': 'str',
        'domain_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'domain_id': 'domainId',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, domain_id=None, type=None):  # noqa: E501
        """ResourceDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._domain_id = None
        self._type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if domain_id is not None:
            self.domain_id = domain_id
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this ResourceDto.  # noqa: E501


        :return: The id of this ResourceDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceDto.


        :param id: The id of this ResourceDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ResourceDto.  # noqa: E501


        :return: The name of this ResourceDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceDto.


        :param name: The name of this ResourceDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def domain_id(self):
        """Gets the domain_id of this ResourceDto.  # noqa: E501


        :return: The domain_id of this ResourceDto.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ResourceDto.


        :param domain_id: The domain_id of this ResourceDto.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def type(self):
        """Gets the type of this ResourceDto.  # noqa: E501


        :return: The type of this ResourceDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceDto.


        :param type: The type of this ResourceDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["DOMAIN", "FOLDER", "WORKSPACE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(ResourceDto, dict):
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
        if not isinstance(other, ResourceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
