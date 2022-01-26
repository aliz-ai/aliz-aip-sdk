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

class EnableMpmDto(object):
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
        'mpm_gcp_project_id': 'str',
        'zone': 'str'
    }

    attribute_map = {
        'mpm_gcp_project_id': 'mpmGcpProjectId',
        'zone': 'zone'
    }

    def __init__(self, mpm_gcp_project_id=None, zone=None):  # noqa: E501
        """EnableMpmDto - a model defined in Swagger"""  # noqa: E501
        self._mpm_gcp_project_id = None
        self._zone = None
        self.discriminator = None
        if mpm_gcp_project_id is not None:
            self.mpm_gcp_project_id = mpm_gcp_project_id
        if zone is not None:
            self.zone = zone

    @property
    def mpm_gcp_project_id(self):
        """Gets the mpm_gcp_project_id of this EnableMpmDto.  # noqa: E501


        :return: The mpm_gcp_project_id of this EnableMpmDto.  # noqa: E501
        :rtype: str
        """
        return self._mpm_gcp_project_id

    @mpm_gcp_project_id.setter
    def mpm_gcp_project_id(self, mpm_gcp_project_id):
        """Sets the mpm_gcp_project_id of this EnableMpmDto.


        :param mpm_gcp_project_id: The mpm_gcp_project_id of this EnableMpmDto.  # noqa: E501
        :type: str
        """

        self._mpm_gcp_project_id = mpm_gcp_project_id

    @property
    def zone(self):
        """Gets the zone of this EnableMpmDto.  # noqa: E501


        :return: The zone of this EnableMpmDto.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this EnableMpmDto.


        :param zone: The zone of this EnableMpmDto.  # noqa: E501
        :type: str
        """

        self._zone = zone

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
        if issubclass(EnableMpmDto, dict):
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
        if not isinstance(other, EnableMpmDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
