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

class GetMpmEnabledStatusDto(object):
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
        'enabled_on_domain': 'bool',
        'service_status': 'str'
    }

    attribute_map = {
        'enabled_on_domain': 'enabledOnDomain',
        'service_status': 'serviceStatus'
    }

    def __init__(self, enabled_on_domain=None, service_status=None):  # noqa: E501
        """GetMpmEnabledStatusDto - a model defined in Swagger"""  # noqa: E501
        self._enabled_on_domain = None
        self._service_status = None
        self.discriminator = None
        if enabled_on_domain is not None:
            self.enabled_on_domain = enabled_on_domain
        if service_status is not None:
            self.service_status = service_status

    @property
    def enabled_on_domain(self):
        """Gets the enabled_on_domain of this GetMpmEnabledStatusDto.  # noqa: E501


        :return: The enabled_on_domain of this GetMpmEnabledStatusDto.  # noqa: E501
        :rtype: bool
        """
        return self._enabled_on_domain

    @enabled_on_domain.setter
    def enabled_on_domain(self, enabled_on_domain):
        """Sets the enabled_on_domain of this GetMpmEnabledStatusDto.


        :param enabled_on_domain: The enabled_on_domain of this GetMpmEnabledStatusDto.  # noqa: E501
        :type: bool
        """

        self._enabled_on_domain = enabled_on_domain

    @property
    def service_status(self):
        """Gets the service_status of this GetMpmEnabledStatusDto.  # noqa: E501


        :return: The service_status of this GetMpmEnabledStatusDto.  # noqa: E501
        :rtype: str
        """
        return self._service_status

    @service_status.setter
    def service_status(self, service_status):
        """Sets the service_status of this GetMpmEnabledStatusDto.


        :param service_status: The service_status of this GetMpmEnabledStatusDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEPLOY_PENDING", "DEPLOY_SUCCESS", "DEPLOY_ERROR", "DESTROY_PENDING", "DESTROY_ERROR"]  # noqa: E501
        if service_status not in allowed_values:
            raise ValueError(
                "Invalid value for `service_status` ({0}), must be one of {1}"  # noqa: E501
                .format(service_status, allowed_values)
            )

        self._service_status = service_status

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
        if issubclass(GetMpmEnabledStatusDto, dict):
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
        if not isinstance(other, GetMpmEnabledStatusDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
