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

class CreateTemplateDto(object):
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
        'create_template_mode': 'str',
        'name': 'str',
        'description': 'str',
        'cookiecutter_config_path': 'str',
        'terraform_script_directory': 'str',
        'terraform_env_directory': 'str',
        'version': 'TemplateVersion',
        'repository_name': 'str',
        'new_repository': 'bool',
        'template_categories': 'list[str]',
        'provision_with_retry': 'bool'
    }

    attribute_map = {
        'create_template_mode': 'createTemplateMode',
        'name': 'name',
        'description': 'description',
        'cookiecutter_config_path': 'cookiecutterConfigPath',
        'terraform_script_directory': 'terraformScriptDirectory',
        'terraform_env_directory': 'terraformEnvDirectory',
        'version': 'version',
        'repository_name': 'repositoryName',
        'new_repository': 'newRepository',
        'template_categories': 'templateCategories',
        'provision_with_retry': 'provisionWithRetry'
    }

    discriminator_value_class_map = {
          'CreateEmptyTemplateDto': 'CreateEmptyTemplateDto',
'CreateBaseTemplateDto': 'CreateBaseTemplateDto',
'CreateCloneTemplateDto': 'CreateCloneTemplateDto'    }

    def __init__(self, create_template_mode=None, name=None, description=None, cookiecutter_config_path=None, terraform_script_directory=None, terraform_env_directory=None, version=None, repository_name=None, new_repository=None, template_categories=None, provision_with_retry=None):  # noqa: E501
        """CreateTemplateDto - a model defined in Swagger"""  # noqa: E501
        self._create_template_mode = None
        self._name = None
        self._description = None
        self._cookiecutter_config_path = None
        self._terraform_script_directory = None
        self._terraform_env_directory = None
        self._version = None
        self._repository_name = None
        self._new_repository = None
        self._template_categories = None
        self._provision_with_retry = None
        self.discriminator = 'createTemplateMode'
        if create_template_mode is not None:
            self.create_template_mode = create_template_mode
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if cookiecutter_config_path is not None:
            self.cookiecutter_config_path = cookiecutter_config_path
        if terraform_script_directory is not None:
            self.terraform_script_directory = terraform_script_directory
        if terraform_env_directory is not None:
            self.terraform_env_directory = terraform_env_directory
        if version is not None:
            self.version = version
        if repository_name is not None:
            self.repository_name = repository_name
        if new_repository is not None:
            self.new_repository = new_repository
        if template_categories is not None:
            self.template_categories = template_categories
        if provision_with_retry is not None:
            self.provision_with_retry = provision_with_retry

    @property
    def create_template_mode(self):
        """Gets the create_template_mode of this CreateTemplateDto.  # noqa: E501


        :return: The create_template_mode of this CreateTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._create_template_mode

    @create_template_mode.setter
    def create_template_mode(self, create_template_mode):
        """Sets the create_template_mode of this CreateTemplateDto.


        :param create_template_mode: The create_template_mode of this CreateTemplateDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["EMPTY_BLUEPRINT", "BASE_BLUEPRINT", "CLONE_BLUEPRINT"]  # noqa: E501
        if create_template_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `create_template_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(create_template_mode, allowed_values)
            )

        self._create_template_mode = create_template_mode

    @property
    def name(self):
        """Gets the name of this CreateTemplateDto.  # noqa: E501


        :return: The name of this CreateTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTemplateDto.


        :param name: The name of this CreateTemplateDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateTemplateDto.  # noqa: E501


        :return: The description of this CreateTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTemplateDto.


        :param description: The description of this CreateTemplateDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def cookiecutter_config_path(self):
        """Gets the cookiecutter_config_path of this CreateTemplateDto.  # noqa: E501


        :return: The cookiecutter_config_path of this CreateTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._cookiecutter_config_path

    @cookiecutter_config_path.setter
    def cookiecutter_config_path(self, cookiecutter_config_path):
        """Sets the cookiecutter_config_path of this CreateTemplateDto.


        :param cookiecutter_config_path: The cookiecutter_config_path of this CreateTemplateDto.  # noqa: E501
        :type: str
        """

        self._cookiecutter_config_path = cookiecutter_config_path

    @property
    def terraform_script_directory(self):
        """Gets the terraform_script_directory of this CreateTemplateDto.  # noqa: E501


        :return: The terraform_script_directory of this CreateTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._terraform_script_directory

    @terraform_script_directory.setter
    def terraform_script_directory(self, terraform_script_directory):
        """Sets the terraform_script_directory of this CreateTemplateDto.


        :param terraform_script_directory: The terraform_script_directory of this CreateTemplateDto.  # noqa: E501
        :type: str
        """

        self._terraform_script_directory = terraform_script_directory

    @property
    def terraform_env_directory(self):
        """Gets the terraform_env_directory of this CreateTemplateDto.  # noqa: E501


        :return: The terraform_env_directory of this CreateTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._terraform_env_directory

    @terraform_env_directory.setter
    def terraform_env_directory(self, terraform_env_directory):
        """Sets the terraform_env_directory of this CreateTemplateDto.


        :param terraform_env_directory: The terraform_env_directory of this CreateTemplateDto.  # noqa: E501
        :type: str
        """

        self._terraform_env_directory = terraform_env_directory

    @property
    def version(self):
        """Gets the version of this CreateTemplateDto.  # noqa: E501


        :return: The version of this CreateTemplateDto.  # noqa: E501
        :rtype: TemplateVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateTemplateDto.


        :param version: The version of this CreateTemplateDto.  # noqa: E501
        :type: TemplateVersion
        """

        self._version = version

    @property
    def repository_name(self):
        """Gets the repository_name of this CreateTemplateDto.  # noqa: E501


        :return: The repository_name of this CreateTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        """Sets the repository_name of this CreateTemplateDto.


        :param repository_name: The repository_name of this CreateTemplateDto.  # noqa: E501
        :type: str
        """

        self._repository_name = repository_name

    @property
    def new_repository(self):
        """Gets the new_repository of this CreateTemplateDto.  # noqa: E501


        :return: The new_repository of this CreateTemplateDto.  # noqa: E501
        :rtype: bool
        """
        return self._new_repository

    @new_repository.setter
    def new_repository(self, new_repository):
        """Sets the new_repository of this CreateTemplateDto.


        :param new_repository: The new_repository of this CreateTemplateDto.  # noqa: E501
        :type: bool
        """

        self._new_repository = new_repository

    @property
    def template_categories(self):
        """Gets the template_categories of this CreateTemplateDto.  # noqa: E501


        :return: The template_categories of this CreateTemplateDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._template_categories

    @template_categories.setter
    def template_categories(self, template_categories):
        """Sets the template_categories of this CreateTemplateDto.


        :param template_categories: The template_categories of this CreateTemplateDto.  # noqa: E501
        :type: list[str]
        """

        self._template_categories = template_categories

    @property
    def provision_with_retry(self):
        """Gets the provision_with_retry of this CreateTemplateDto.  # noqa: E501


        :return: The provision_with_retry of this CreateTemplateDto.  # noqa: E501
        :rtype: bool
        """
        return self._provision_with_retry

    @provision_with_retry.setter
    def provision_with_retry(self, provision_with_retry):
        """Sets the provision_with_retry of this CreateTemplateDto.


        :param provision_with_retry: The provision_with_retry of this CreateTemplateDto.  # noqa: E501
        :type: bool
        """

        self._provision_with_retry = provision_with_retry

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(CreateTemplateDto, dict):
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
        if not isinstance(other, CreateTemplateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
