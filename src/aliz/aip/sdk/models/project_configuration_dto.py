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

class ProjectConfigurationDto(object):
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
        'approval_workflow_status': 'ApprovalWorkflowStatusDto',
        'git_settings': 'GitSettingsDto'
    }

    attribute_map = {
        'approval_workflow_status': 'approvalWorkflowStatus',
        'git_settings': 'gitSettings'
    }

    def __init__(self, approval_workflow_status=None, git_settings=None):  # noqa: E501
        """ProjectConfigurationDto - a model defined in Swagger"""  # noqa: E501
        self._approval_workflow_status = None
        self._git_settings = None
        self.discriminator = None
        if approval_workflow_status is not None:
            self.approval_workflow_status = approval_workflow_status
        if git_settings is not None:
            self.git_settings = git_settings

    @property
    def approval_workflow_status(self):
        """Gets the approval_workflow_status of this ProjectConfigurationDto.  # noqa: E501


        :return: The approval_workflow_status of this ProjectConfigurationDto.  # noqa: E501
        :rtype: ApprovalWorkflowStatusDto
        """
        return self._approval_workflow_status

    @approval_workflow_status.setter
    def approval_workflow_status(self, approval_workflow_status):
        """Sets the approval_workflow_status of this ProjectConfigurationDto.


        :param approval_workflow_status: The approval_workflow_status of this ProjectConfigurationDto.  # noqa: E501
        :type: ApprovalWorkflowStatusDto
        """

        self._approval_workflow_status = approval_workflow_status

    @property
    def git_settings(self):
        """Gets the git_settings of this ProjectConfigurationDto.  # noqa: E501


        :return: The git_settings of this ProjectConfigurationDto.  # noqa: E501
        :rtype: GitSettingsDto
        """
        return self._git_settings

    @git_settings.setter
    def git_settings(self, git_settings):
        """Sets the git_settings of this ProjectConfigurationDto.


        :param git_settings: The git_settings of this ProjectConfigurationDto.  # noqa: E501
        :type: GitSettingsDto
        """

        self._git_settings = git_settings

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
        if issubclass(ProjectConfigurationDto, dict):
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
        if not isinstance(other, ProjectConfigurationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
