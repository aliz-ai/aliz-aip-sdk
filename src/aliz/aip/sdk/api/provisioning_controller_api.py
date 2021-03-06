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


class ProvisioningControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_provision(self, workspace_id, project_id, **kwargs):  # noqa: E501
        """create_provision  # noqa: E501

        Deploy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_provision(workspace_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_id: ID of the workspace (required)
        :param str project_id: ID of GCP project (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_provision_with_http_info(workspace_id, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_provision_with_http_info(workspace_id, project_id, **kwargs)  # noqa: E501
            return data

    def create_provision_with_http_info(self, workspace_id, project_id, **kwargs):  # noqa: E501
        """create_provision  # noqa: E501

        Deploy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_provision_with_http_info(workspace_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_id: ID of the workspace (required)
        :param str project_id: ID of GCP project (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_provision" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params or
                params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `create_provision`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `create_provision`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']  # noqa: E501
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearer-key']  # noqa: E501

        return self.api_client.call_api(
            '/api/provisioning/v1/workspaces/{workspaceId}/projects/{projectId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def enable_provision(self, workspace_id, project_id, **kwargs):  # noqa: E501
        """enable_provision  # noqa: E501

        Deploy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enable_provision(workspace_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_id: ID of the workspace (required)
        :param str project_id: ID of GCP project (required)
        :return: ProjectDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.enable_provision_with_http_info(workspace_id, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.enable_provision_with_http_info(workspace_id, project_id, **kwargs)  # noqa: E501
            return data

    def enable_provision_with_http_info(self, workspace_id, project_id, **kwargs):  # noqa: E501
        """enable_provision  # noqa: E501

        Deploy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enable_provision_with_http_info(workspace_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_id: ID of the workspace (required)
        :param str project_id: ID of GCP project (required)
        :return: ProjectDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enable_provision" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params or
                params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `enable_provision`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `enable_provision`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']  # noqa: E501
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
            '/api/provisioning/v1/workspaces/{workspaceId}/projects/{projectId}/enable', 'POST',
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

    def finish_provisioning(self, workspace_id, provisioning_id, **kwargs):  # noqa: E501
        """finish_provisioning  # noqa: E501

        Finish  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.finish_provisioning(workspace_id, provisioning_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_id: ID of the workspace (required)
        :param str provisioning_id: ID of GCP project (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.finish_provisioning_with_http_info(workspace_id, provisioning_id, **kwargs)  # noqa: E501
        else:
            (data) = self.finish_provisioning_with_http_info(workspace_id, provisioning_id, **kwargs)  # noqa: E501
            return data

    def finish_provisioning_with_http_info(self, workspace_id, provisioning_id, **kwargs):  # noqa: E501
        """finish_provisioning  # noqa: E501

        Finish  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.finish_provisioning_with_http_info(workspace_id, provisioning_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_id: ID of the workspace (required)
        :param str provisioning_id: ID of GCP project (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'provisioning_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method finish_provisioning" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params or
                params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `finish_provisioning`")  # noqa: E501
        # verify the required parameter 'provisioning_id' is set
        if ('provisioning_id' not in params or
                params['provisioning_id'] is None):
            raise ValueError("Missing the required parameter `provisioning_id` when calling `finish_provisioning`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']  # noqa: E501
        if 'provisioning_id' in params:
            path_params['provisioningId'] = params['provisioning_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearer-key']  # noqa: E501

        return self.api_client.call_api(
            '/api/provisioning/v1/workspaces/{workspaceId}/provisionings/{provisioningId}/finish', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_details(self, workspace_id, provisioning_id, **kwargs):  # noqa: E501
        """get_details  # noqa: E501

        Get details of an provisioning  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_details(workspace_id, provisioning_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_id: ID of the workspace (required)
        :param str provisioning_id: ID of Provision (required)
        :return: ProvisioningDetailDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_details_with_http_info(workspace_id, provisioning_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_details_with_http_info(workspace_id, provisioning_id, **kwargs)  # noqa: E501
            return data

    def get_details_with_http_info(self, workspace_id, provisioning_id, **kwargs):  # noqa: E501
        """get_details  # noqa: E501

        Get details of an provisioning  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_details_with_http_info(workspace_id, provisioning_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_id: ID of the workspace (required)
        :param str provisioning_id: ID of Provision (required)
        :return: ProvisioningDetailDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'provisioning_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params or
                params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `get_details`")  # noqa: E501
        # verify the required parameter 'provisioning_id' is set
        if ('provisioning_id' not in params or
                params['provisioning_id'] is None):
            raise ValueError("Missing the required parameter `provisioning_id` when calling `get_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']  # noqa: E501
        if 'provisioning_id' in params:
            path_params['provisioningId'] = params['provisioning_id']  # noqa: E501

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
            '/api/provisioning/v1/workspaces/{workspaceId}/provisionings/{provisioningId}/details', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProvisioningDetailDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_provisions(self, workspace_id, project_id, **kwargs):  # noqa: E501
        """get_provisions  # noqa: E501

        Get Deploys  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provisions(workspace_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_id: ID of the workspace (required)
        :param str project_id: ID of GCP project (required)
        :return: list[ProvisionDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_provisions_with_http_info(workspace_id, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_provisions_with_http_info(workspace_id, project_id, **kwargs)  # noqa: E501
            return data

    def get_provisions_with_http_info(self, workspace_id, project_id, **kwargs):  # noqa: E501
        """get_provisions  # noqa: E501

        Get Deploys  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provisions_with_http_info(workspace_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_id: ID of the workspace (required)
        :param str project_id: ID of GCP project (required)
        :return: list[ProvisionDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_provisions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params or
                params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `get_provisions`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `get_provisions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']  # noqa: E501
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
            '/api/provisioning/v1/workspaces/{workspaceId}/projects/{projectId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProvisionDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def provisioning_finished(self, body, **kwargs):  # noqa: E501
        """provisioning_finished  # noqa: E501

        Provisioning finished  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.provisioning_finished(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PubSubMessageDto body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.provisioning_finished_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.provisioning_finished_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def provisioning_finished_with_http_info(self, body, **kwargs):  # noqa: E501
        """provisioning_finished  # noqa: E501

        Provisioning finished  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.provisioning_finished_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PubSubMessageDto body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method provisioning_finished" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `provisioning_finished`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/api/provisioning/v1/provisionings/finished', 'POST',
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
