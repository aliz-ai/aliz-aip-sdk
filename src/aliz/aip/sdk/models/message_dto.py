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

class MessageDto(object):
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
        'attributes': 'dict(str, str)',
        'message_id': 'str',
        'publish_time': 'str',
        'data': 'str'
    }

    attribute_map = {
        'attributes': 'attributes',
        'message_id': 'messageId',
        'publish_time': 'publishTime',
        'data': 'data'
    }

    def __init__(self, attributes=None, message_id=None, publish_time=None, data=None):  # noqa: E501
        """MessageDto - a model defined in Swagger"""  # noqa: E501
        self._attributes = None
        self._message_id = None
        self._publish_time = None
        self._data = None
        self.discriminator = None
        if attributes is not None:
            self.attributes = attributes
        if message_id is not None:
            self.message_id = message_id
        if publish_time is not None:
            self.publish_time = publish_time
        if data is not None:
            self.data = data

    @property
    def attributes(self):
        """Gets the attributes of this MessageDto.  # noqa: E501


        :return: The attributes of this MessageDto.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this MessageDto.


        :param attributes: The attributes of this MessageDto.  # noqa: E501
        :type: dict(str, str)
        """

        self._attributes = attributes

    @property
    def message_id(self):
        """Gets the message_id of this MessageDto.  # noqa: E501


        :return: The message_id of this MessageDto.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this MessageDto.


        :param message_id: The message_id of this MessageDto.  # noqa: E501
        :type: str
        """

        self._message_id = message_id

    @property
    def publish_time(self):
        """Gets the publish_time of this MessageDto.  # noqa: E501


        :return: The publish_time of this MessageDto.  # noqa: E501
        :rtype: str
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this MessageDto.


        :param publish_time: The publish_time of this MessageDto.  # noqa: E501
        :type: str
        """

        self._publish_time = publish_time

    @property
    def data(self):
        """Gets the data of this MessageDto.  # noqa: E501


        :return: The data of this MessageDto.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this MessageDto.


        :param data: The data of this MessageDto.  # noqa: E501
        :type: str
        """

        self._data = data

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
        if issubclass(MessageDto, dict):
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
        if not isinstance(other, MessageDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
