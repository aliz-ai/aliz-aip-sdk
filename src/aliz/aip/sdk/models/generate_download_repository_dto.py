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

class GenerateDownloadRepositoryDto(object):
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
        'cookie_cutter_content': 'dict(str, object)',
        'managed_service_dependencies': 'dict(str, str)',
        'blueprint_dependencies': 'dict(str, str)',
        'template_version_id': 'str',
        'repository_name': 'str',
        'new_repository': 'bool',
        'project_id': 'str',
        'placeholder_prefix': 'str',
        'placeholder_suffix': 'str'
    }

    attribute_map = {
        'cookie_cutter_content': 'cookieCutterContent',
        'managed_service_dependencies': 'managedServiceDependencies',
        'blueprint_dependencies': 'blueprintDependencies',
        'template_version_id': 'templateVersionId',
        'repository_name': 'repositoryName',
        'new_repository': 'newRepository',
        'project_id': 'projectId',
        'placeholder_prefix': 'placeholderPrefix',
        'placeholder_suffix': 'placeholderSuffix'
    }

    def __init__(self, cookie_cutter_content=None, managed_service_dependencies=None, blueprint_dependencies=None, template_version_id=None, repository_name=None, new_repository=None, project_id=None, placeholder_prefix=None, placeholder_suffix=None):  # noqa: E501
        """GenerateDownloadRepositoryDto - a model defined in Swagger"""  # noqa: E501
        self._cookie_cutter_content = None
        self._managed_service_dependencies = None
        self._blueprint_dependencies = None
        self._template_version_id = None
        self._repository_name = None
        self._new_repository = None
        self._project_id = None
        self._placeholder_prefix = None
        self._placeholder_suffix = None
        self.discriminator = None
        if cookie_cutter_content is not None:
            self.cookie_cutter_content = cookie_cutter_content
        if managed_service_dependencies is not None:
            self.managed_service_dependencies = managed_service_dependencies
        if blueprint_dependencies is not None:
            self.blueprint_dependencies = blueprint_dependencies
        if template_version_id is not None:
            self.template_version_id = template_version_id
        if repository_name is not None:
            self.repository_name = repository_name
        if new_repository is not None:
            self.new_repository = new_repository
        if project_id is not None:
            self.project_id = project_id
        if placeholder_prefix is not None:
            self.placeholder_prefix = placeholder_prefix
        if placeholder_suffix is not None:
            self.placeholder_suffix = placeholder_suffix

    @property
    def cookie_cutter_content(self):
        """Gets the cookie_cutter_content of this GenerateDownloadRepositoryDto.  # noqa: E501


        :return: The cookie_cutter_content of this GenerateDownloadRepositoryDto.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._cookie_cutter_content

    @cookie_cutter_content.setter
    def cookie_cutter_content(self, cookie_cutter_content):
        """Sets the cookie_cutter_content of this GenerateDownloadRepositoryDto.


        :param cookie_cutter_content: The cookie_cutter_content of this GenerateDownloadRepositoryDto.  # noqa: E501
        :type: dict(str, object)
        """

        self._cookie_cutter_content = cookie_cutter_content

    @property
    def managed_service_dependencies(self):
        """Gets the managed_service_dependencies of this GenerateDownloadRepositoryDto.  # noqa: E501


        :return: The managed_service_dependencies of this GenerateDownloadRepositoryDto.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._managed_service_dependencies

    @managed_service_dependencies.setter
    def managed_service_dependencies(self, managed_service_dependencies):
        """Sets the managed_service_dependencies of this GenerateDownloadRepositoryDto.


        :param managed_service_dependencies: The managed_service_dependencies of this GenerateDownloadRepositoryDto.  # noqa: E501
        :type: dict(str, str)
        """

        self._managed_service_dependencies = managed_service_dependencies

    @property
    def blueprint_dependencies(self):
        """Gets the blueprint_dependencies of this GenerateDownloadRepositoryDto.  # noqa: E501


        :return: The blueprint_dependencies of this GenerateDownloadRepositoryDto.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._blueprint_dependencies

    @blueprint_dependencies.setter
    def blueprint_dependencies(self, blueprint_dependencies):
        """Sets the blueprint_dependencies of this GenerateDownloadRepositoryDto.


        :param blueprint_dependencies: The blueprint_dependencies of this GenerateDownloadRepositoryDto.  # noqa: E501
        :type: dict(str, str)
        """

        self._blueprint_dependencies = blueprint_dependencies

    @property
    def template_version_id(self):
        """Gets the template_version_id of this GenerateDownloadRepositoryDto.  # noqa: E501


        :return: The template_version_id of this GenerateDownloadRepositoryDto.  # noqa: E501
        :rtype: str
        """
        return self._template_version_id

    @template_version_id.setter
    def template_version_id(self, template_version_id):
        """Sets the template_version_id of this GenerateDownloadRepositoryDto.


        :param template_version_id: The template_version_id of this GenerateDownloadRepositoryDto.  # noqa: E501
        :type: str
        """

        self._template_version_id = template_version_id

    @property
    def repository_name(self):
        """Gets the repository_name of this GenerateDownloadRepositoryDto.  # noqa: E501


        :return: The repository_name of this GenerateDownloadRepositoryDto.  # noqa: E501
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        """Sets the repository_name of this GenerateDownloadRepositoryDto.


        :param repository_name: The repository_name of this GenerateDownloadRepositoryDto.  # noqa: E501
        :type: str
        """

        self._repository_name = repository_name

    @property
    def new_repository(self):
        """Gets the new_repository of this GenerateDownloadRepositoryDto.  # noqa: E501


        :return: The new_repository of this GenerateDownloadRepositoryDto.  # noqa: E501
        :rtype: bool
        """
        return self._new_repository

    @new_repository.setter
    def new_repository(self, new_repository):
        """Sets the new_repository of this GenerateDownloadRepositoryDto.


        :param new_repository: The new_repository of this GenerateDownloadRepositoryDto.  # noqa: E501
        :type: bool
        """

        self._new_repository = new_repository

    @property
    def project_id(self):
        """Gets the project_id of this GenerateDownloadRepositoryDto.  # noqa: E501


        :return: The project_id of this GenerateDownloadRepositoryDto.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this GenerateDownloadRepositoryDto.


        :param project_id: The project_id of this GenerateDownloadRepositoryDto.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def placeholder_prefix(self):
        """Gets the placeholder_prefix of this GenerateDownloadRepositoryDto.  # noqa: E501


        :return: The placeholder_prefix of this GenerateDownloadRepositoryDto.  # noqa: E501
        :rtype: str
        """
        return self._placeholder_prefix

    @placeholder_prefix.setter
    def placeholder_prefix(self, placeholder_prefix):
        """Sets the placeholder_prefix of this GenerateDownloadRepositoryDto.


        :param placeholder_prefix: The placeholder_prefix of this GenerateDownloadRepositoryDto.  # noqa: E501
        :type: str
        """

        self._placeholder_prefix = placeholder_prefix

    @property
    def placeholder_suffix(self):
        """Gets the placeholder_suffix of this GenerateDownloadRepositoryDto.  # noqa: E501


        :return: The placeholder_suffix of this GenerateDownloadRepositoryDto.  # noqa: E501
        :rtype: str
        """
        return self._placeholder_suffix

    @placeholder_suffix.setter
    def placeholder_suffix(self, placeholder_suffix):
        """Sets the placeholder_suffix of this GenerateDownloadRepositoryDto.


        :param placeholder_suffix: The placeholder_suffix of this GenerateDownloadRepositoryDto.  # noqa: E501
        :type: str
        """

        self._placeholder_suffix = placeholder_suffix

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
        if issubclass(GenerateDownloadRepositoryDto, dict):
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
        if not isinstance(other, GenerateDownloadRepositoryDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
