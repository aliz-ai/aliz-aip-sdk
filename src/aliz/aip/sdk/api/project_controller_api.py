# coding: utf-8

"""
    Aliz AIP REST API

    AIP Workspace API.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: aip-support@aliz.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from aliz.aip.sdk.api_client import ApiClient


class ProjectControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def change_configuration(self, body, project_id, workspace_id, **kwargs):  # noqa: E501
        """change_configuration  # noqa: E501

        Change the approval workflow settings of an project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_configuration(body, project_id, workspace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectConfigurationDto body: (required)
        :param str project_id: Gcp project id (required)
        :param str workspace_id: Workspace id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_configuration_with_http_info(body, project_id, workspace_id, **kwargs)  # noqa: E501
        else:
            (data) = self.change_configuration_with_http_info(body, project_id, workspace_id, **kwargs)  # noqa: E501
            return data

    def change_configuration_with_http_info(self, body, project_id, workspace_id, **kwargs):  # noqa: E501
        """change_configuration  # noqa: E501

        Change the approval workflow settings of an project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_configuration_with_http_info(body, project_id, workspace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectConfigurationDto body: (required)
        :param str project_id: Gcp project id (required)
        :param str workspace_id: Workspace id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'project_id', 'workspace_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `change_configuration`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `change_configuration`")  # noqa: E501
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params or
                params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `change_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-key']  # noqa: E501

        return self.api_client.call_api(
            '/api/project/v1/workspaces/{workspaceId}/projects/{projectId}/config', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_project(self, domain_id, project_id, **kwargs):  # noqa: E501
        """create_project  # noqa: E501

        Creates GCP project if not exists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_project(domain_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Domain id (required)
        :param str project_id: Gcp project id (required)
        :return: ProjectDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_project_with_http_info(domain_id, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_project_with_http_info(domain_id, project_id, **kwargs)  # noqa: E501
            return data

    def create_project_with_http_info(self, domain_id, project_id, **kwargs):  # noqa: E501
        """create_project  # noqa: E501

        Creates GCP project if not exists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_project_with_http_info(domain_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Domain id (required)
        :param str project_id: Gcp project id (required)
        :return: ProjectDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or
                params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `create_project`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `create_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']  # noqa: E501
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-key']  # noqa: E501

        return self.api_client.call_api(
            '/api/project/v1/domains/{domainId}/projects/{projectId}/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_projects(self, domain_id, **kwargs):  # noqa: E501
        """get_all_projects  # noqa: E501

        Retrieves all available GCP projects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_projects(domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Domain id (required)
        :param bool only_unallocated: Show only projects not allocated to workspaces
        :return: list[ProjectDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_projects_with_http_info(domain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_projects_with_http_info(domain_id, **kwargs)  # noqa: E501
            return data

    def get_all_projects_with_http_info(self, domain_id, **kwargs):  # noqa: E501
        """get_all_projects  # noqa: E501

        Retrieves all available GCP projects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_projects_with_http_info(domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Domain id (required)
        :param bool only_unallocated: Show only projects not allocated to workspaces
        :return: list[ProjectDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id', 'only_unallocated']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_projects" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or
                params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `get_all_projects`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']  # noqa: E501

        query_params = []
        if 'only_unallocated' in params:
            query_params.append(('onlyUnallocated', params['only_unallocated']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-key']  # noqa: E501

        return self.api_client.call_api(
            '/api/project/v1/domains/{domainId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProjectDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def validate_project(self, project_id, domain_id, **kwargs):  # noqa: E501
        """validate_project  # noqa: E501

        Retrieves GCP project if exists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_project(project_id, domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: Gcp project id (required)
        :param str domain_id: Domain id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.validate_project_with_http_info(project_id, domain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.validate_project_with_http_info(project_id, domain_id, **kwargs)  # noqa: E501
            return data

    def validate_project_with_http_info(self, project_id, domain_id, **kwargs):  # noqa: E501
        """validate_project  # noqa: E501

        Retrieves GCP project if exists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_project_with_http_info(project_id, domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: Gcp project id (required)
        :param str domain_id: Domain id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'domain_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `validate_project`")  # noqa: E501
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or
                params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `validate_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-key']  # noqa: E501

        return self.api_client.call_api(
            '/api/project/v1/domains/{domainId}/projects/{projectId}/validate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
