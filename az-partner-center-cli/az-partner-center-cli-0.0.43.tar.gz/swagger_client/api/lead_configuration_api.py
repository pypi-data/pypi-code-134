# coding: utf-8

"""
    https://api.partner.microsoft.com/v1.0/ingestion

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class LeadConfigurationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def products_product_id_leadconfiguration_get(self, product_id, authorization, **kwargs):  # noqa: E501
        """Returns the LeadConfiguration associated with the product  # noqa: E501

        Sample request:                    GET /products/{productID}/leadconfiguration    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_product_id_leadconfiguration_get(product_id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_id: ID of product (required)
        :param str authorization: User authorization (required)
        :param str client_request_id: ID of request provIDed by user
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.products_product_id_leadconfiguration_get_with_http_info(product_id, authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.products_product_id_leadconfiguration_get_with_http_info(product_id, authorization, **kwargs)  # noqa: E501
            return data

    def products_product_id_leadconfiguration_get_with_http_info(self, product_id, authorization, **kwargs):  # noqa: E501
        """Returns the LeadConfiguration associated with the product  # noqa: E501

        Sample request:                    GET /products/{productID}/leadconfiguration    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_product_id_leadconfiguration_get_with_http_info(product_id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_id: ID of product (required)
        :param str authorization: User authorization (required)
        :param str client_request_id: ID of request provIDed by user
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'authorization', 'client_request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method products_product_id_leadconfiguration_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params or
                params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `products_product_id_leadconfiguration_get`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `products_product_id_leadconfiguration_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'product_id' in params:
            path_params['productID'] = params['product_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'client_request_id' in params:
            header_params['Client-Request-ID'] = params['client_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/products/{productID}/leadconfiguration', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def products_product_id_leadconfiguration_post(self, authorization, product_id, **kwargs):  # noqa: E501
        """Creates a new LeadConfiguration associated with the product  # noqa: E501

        Sample request:                    POST /products/{productID}/leadconfiguration    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_product_id_leadconfiguration_post(authorization, product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: User authorization (required)
        :param str product_id: ID of product (required)
        :param ProductIDLeadconfigurationBody body: Request body of a Microsoft.Ingestion.Api.Models.LeadManagement.BaseLeadConfiguration
        :param str client_request_id: ID of request provIDed by user
        :return: ProductIDLeadconfigurationBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.products_product_id_leadconfiguration_post_with_http_info(authorization, product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.products_product_id_leadconfiguration_post_with_http_info(authorization, product_id, **kwargs)  # noqa: E501
            return data

    def products_product_id_leadconfiguration_post_with_http_info(self, authorization, product_id, **kwargs):  # noqa: E501
        """Creates a new LeadConfiguration associated with the product  # noqa: E501

        Sample request:                    POST /products/{productID}/leadconfiguration    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_product_id_leadconfiguration_post_with_http_info(authorization, product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: User authorization (required)
        :param str product_id: ID of product (required)
        :param ProductIDLeadconfigurationBody body: Request body of a Microsoft.Ingestion.Api.Models.LeadManagement.BaseLeadConfiguration
        :param str client_request_id: ID of request provIDed by user
        :return: ProductIDLeadconfigurationBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'product_id', 'body', 'client_request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method products_product_id_leadconfiguration_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `products_product_id_leadconfiguration_post`")  # noqa: E501
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params or
                params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `products_product_id_leadconfiguration_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'product_id' in params:
            path_params['productID'] = params['product_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'client_request_id' in params:
            header_params['Client-Request-ID'] = params['client_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/products/{productID}/leadconfiguration', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProductIDLeadconfigurationBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
