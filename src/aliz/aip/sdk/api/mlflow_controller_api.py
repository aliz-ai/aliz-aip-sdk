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


class MlflowControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_mlflow_users(self, body, domain_id, instance_id, **kwargs):  # noqa: E501
        """add_mlflow_users  # noqa: E501

        Grant access to principals  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_mlflow_users(body, domain_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthorizeManagedServiceUsersDto body: (required)
        :param str domain_id: Domain identifier (required)
        :param str instance_id: Instance id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_mlflow_users_with_http_info(body, domain_id, instance_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_mlflow_users_with_http_info(body, domain_id, instance_id, **kwargs)  # noqa: E501
            return data

    def add_mlflow_users_with_http_info(self, body, domain_id, instance_id, **kwargs):  # noqa: E501
        """add_mlflow_users  # noqa: E501

        Grant access to principals  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_mlflow_users_with_http_info(body, domain_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthorizeManagedServiceUsersDto body: (required)
        :param str domain_id: Domain identifier (required)
        :param str instance_id: Instance id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'domain_id', 'instance_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_mlflow_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_mlflow_users`")  # noqa: E501
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or
                params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `add_mlflow_users`")  # noqa: E501
        # verify the required parameter 'instance_id' is set
        if ('instance_id' not in params or
                params['instance_id'] is None):
            raise ValueError("Missing the required parameter `instance_id` when calling `add_mlflow_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']  # noqa: E501
        if 'instance_id' in params:
            path_params['instanceId'] = params['instance_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-key']  # noqa: E501

        return self.api_client.call_api(
            '/api/mlflow/v1/domains/{domainId}/instances/{instanceId}/principals', 'POST',
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

    def create_mlflow_instance(self, body, domain_id, version, **kwargs):  # noqa: E501
        """create_mlflow_instance  # noqa: E501

        Create a instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_mlflow_instance(body, domain_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateManagedServiceDto body: (required)
        :param str domain_id: Domain identifier (required)
        :param str version: Version of the template (required)
        :return: ManagedInstanceDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_mlflow_instance_with_http_info(body, domain_id, version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_mlflow_instance_with_http_info(body, domain_id, version, **kwargs)  # noqa: E501
            return data

    def create_mlflow_instance_with_http_info(self, body, domain_id, version, **kwargs):  # noqa: E501
        """create_mlflow_instance  # noqa: E501

        Create a instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_mlflow_instance_with_http_info(body, domain_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateManagedServiceDto body: (required)
        :param str domain_id: Domain identifier (required)
        :param str version: Version of the template (required)
        :return: ManagedInstanceDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'domain_id', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_mlflow_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_mlflow_instance`")  # noqa: E501
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or
                params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `create_mlflow_instance`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `create_mlflow_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']  # noqa: E501
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

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
            '/api/mlflow/v1/domains/{domainId}/versions/{version}/instances', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ManagedInstanceDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_mlflow_instance(self, domain_id, instance_id, **kwargs):  # noqa: E501
        """delete_mlflow_instance  # noqa: E501

        Delete instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_mlflow_instance(domain_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Domain identifier (required)
        :param str instance_id: Instance id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_mlflow_instance_with_http_info(domain_id, instance_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_mlflow_instance_with_http_info(domain_id, instance_id, **kwargs)  # noqa: E501
            return data

    def delete_mlflow_instance_with_http_info(self, domain_id, instance_id, **kwargs):  # noqa: E501
        """delete_mlflow_instance  # noqa: E501

        Delete instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_mlflow_instance_with_http_info(domain_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Domain identifier (required)
        :param str instance_id: Instance id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id', 'instance_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_mlflow_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or
                params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `delete_mlflow_instance`")  # noqa: E501
        # verify the required parameter 'instance_id' is set
        if ('instance_id' not in params or
                params['instance_id'] is None):
            raise ValueError("Missing the required parameter `instance_id` when calling `delete_mlflow_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']  # noqa: E501
        if 'instance_id' in params:
            path_params['instanceId'] = params['instance_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearer-key']  # noqa: E501

        return self.api_client.call_api(
            '/api/mlflow/v1/domains/{domainId}/instances/{instanceId}', 'DELETE',
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

    def get_mlflow_instance(self, domain_id, instance_id, **kwargs):  # noqa: E501
        """get_mlflow_instance  # noqa: E501

        Get instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mlflow_instance(domain_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Domain identifier (required)
        :param str instance_id: Instance id (required)
        :return: ManagedInstanceDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_mlflow_instance_with_http_info(domain_id, instance_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_mlflow_instance_with_http_info(domain_id, instance_id, **kwargs)  # noqa: E501
            return data

    def get_mlflow_instance_with_http_info(self, domain_id, instance_id, **kwargs):  # noqa: E501
        """get_mlflow_instance  # noqa: E501

        Get instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mlflow_instance_with_http_info(domain_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Domain identifier (required)
        :param str instance_id: Instance id (required)
        :return: ManagedInstanceDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id', 'instance_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_mlflow_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or
                params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `get_mlflow_instance`")  # noqa: E501
        # verify the required parameter 'instance_id' is set
        if ('instance_id' not in params or
                params['instance_id'] is None):
            raise ValueError("Missing the required parameter `instance_id` when calling `get_mlflow_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']  # noqa: E501
        if 'instance_id' in params:
            path_params['instanceId'] = params['instance_id']  # noqa: E501

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
            '/api/mlflow/v1/domains/{domainId}/instances/{instanceId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ManagedInstanceDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_mlflow_variables(self, domain_id, version, **kwargs):  # noqa: E501
        """Get instance variables  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mlflow_variables(domain_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Domain identifier (required)
        :param str version: Version of the template (required)
        :return: CookieCutterContent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_mlflow_variables_with_http_info(domain_id, version, **kwargs)  # noqa: E501
        else:
            (data) = self.get_mlflow_variables_with_http_info(domain_id, version, **kwargs)  # noqa: E501
            return data

    def get_mlflow_variables_with_http_info(self, domain_id, version, **kwargs):  # noqa: E501
        """Get instance variables  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mlflow_variables_with_http_info(domain_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Domain identifier (required)
        :param str version: Version of the template (required)
        :return: CookieCutterContent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_mlflow_variables" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or
                params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `get_mlflow_variables`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `get_mlflow_variables`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']  # noqa: E501
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

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
            '/api/mlflow/v1/domains/{domainId}/versions/{version}/variables', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CookieCutterContent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_versions(self, **kwargs):  # noqa: E501
        """Get versions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_versions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[TemplateVersion]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_versions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_versions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_versions_with_http_info(self, **kwargs):  # noqa: E501
        """Get versions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_versions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[TemplateVersion]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_versions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/mlflow/v1/versions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TemplateVersion]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_mlflow_instances(self, domain_id, **kwargs):  # noqa: E501
        """list_mlflow_instances  # noqa: E501

        List instances  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_mlflow_instances(domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Domain identifier (required)
        :param str state:
        :return: list[ManagedInstanceDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_mlflow_instances_with_http_info(domain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_mlflow_instances_with_http_info(domain_id, **kwargs)  # noqa: E501
            return data

    def list_mlflow_instances_with_http_info(self, domain_id, **kwargs):  # noqa: E501
        """list_mlflow_instances  # noqa: E501

        List instances  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_mlflow_instances_with_http_info(domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Domain identifier (required)
        :param str state:
        :return: list[ManagedInstanceDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id', 'state']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_mlflow_instances" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or
                params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `list_mlflow_instances`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']  # noqa: E501

        query_params = []
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501

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
            '/api/mlflow/v1/domains/{domainId}/instances', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ManagedInstanceDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_mlflow_users(self, domain_id, instance_id, **kwargs):  # noqa: E501
        """list_mlflow_users  # noqa: E501

        Get principals  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_mlflow_users(domain_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Domain identifier (required)
        :param str instance_id: Instance id (required)
        :return: AuthorizeManagedServiceDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_mlflow_users_with_http_info(domain_id, instance_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_mlflow_users_with_http_info(domain_id, instance_id, **kwargs)  # noqa: E501
            return data

    def list_mlflow_users_with_http_info(self, domain_id, instance_id, **kwargs):  # noqa: E501
        """list_mlflow_users  # noqa: E501

        Get principals  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_mlflow_users_with_http_info(domain_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_id: Domain identifier (required)
        :param str instance_id: Instance id (required)
        :return: AuthorizeManagedServiceDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id', 'instance_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_mlflow_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or
                params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `list_mlflow_users`")  # noqa: E501
        # verify the required parameter 'instance_id' is set
        if ('instance_id' not in params or
                params['instance_id'] is None):
            raise ValueError("Missing the required parameter `instance_id` when calling `list_mlflow_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']  # noqa: E501
        if 'instance_id' in params:
            path_params['instanceId'] = params['instance_id']  # noqa: E501

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
            '/api/mlflow/v1/domains/{domainId}/instances/{instanceId}/principals', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthorizeManagedServiceDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_mlflow_users(self, body, domain_id, instance_id, **kwargs):  # noqa: E501
        """remove_mlflow_users  # noqa: E501

        Revoke access from principals  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_mlflow_users(body, domain_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthorizeManagedServiceUsersDto body: (required)
        :param str domain_id: Domain identifier (required)
        :param str instance_id: Instance id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_mlflow_users_with_http_info(body, domain_id, instance_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_mlflow_users_with_http_info(body, domain_id, instance_id, **kwargs)  # noqa: E501
            return data

    def remove_mlflow_users_with_http_info(self, body, domain_id, instance_id, **kwargs):  # noqa: E501
        """remove_mlflow_users  # noqa: E501

        Revoke access from principals  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_mlflow_users_with_http_info(body, domain_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthorizeManagedServiceUsersDto body: (required)
        :param str domain_id: Domain identifier (required)
        :param str instance_id: Instance id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'domain_id', 'instance_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_mlflow_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `remove_mlflow_users`")  # noqa: E501
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or
                params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `remove_mlflow_users`")  # noqa: E501
        # verify the required parameter 'instance_id' is set
        if ('instance_id' not in params or
                params['instance_id'] is None):
            raise ValueError("Missing the required parameter `instance_id` when calling `remove_mlflow_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']  # noqa: E501
        if 'instance_id' in params:
            path_params['instanceId'] = params['instance_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer-key']  # noqa: E501

        return self.api_client.call_api(
            '/api/mlflow/v1/domains/{domainId}/instances/{instanceId}/principals', 'DELETE',
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
