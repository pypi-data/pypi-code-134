# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Sequence,
    Tuple,
    Optional,
    Iterator,
)

from google.cloud.bigtable_admin_v2.types import bigtable_instance_admin
from google.cloud.bigtable_admin_v2.types import instance


class ListAppProfilesPager:
    """A pager for iterating through ``list_app_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigtable_admin_v2.types.ListAppProfilesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``app_profiles`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAppProfiles`` requests and continue to iterate
    through the ``app_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigtable_admin_v2.types.ListAppProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., bigtable_instance_admin.ListAppProfilesResponse],
        request: bigtable_instance_admin.ListAppProfilesRequest,
        response: bigtable_instance_admin.ListAppProfilesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigtable_admin_v2.types.ListAppProfilesRequest):
                The initial request object.
            response (google.cloud.bigtable_admin_v2.types.ListAppProfilesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = bigtable_instance_admin.ListAppProfilesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[bigtable_instance_admin.ListAppProfilesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[instance.AppProfile]:
        for page in self.pages:
            yield from page.app_profiles

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAppProfilesAsyncPager:
    """A pager for iterating through ``list_app_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigtable_admin_v2.types.ListAppProfilesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``app_profiles`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAppProfiles`` requests and continue to iterate
    through the ``app_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigtable_admin_v2.types.ListAppProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[bigtable_instance_admin.ListAppProfilesResponse]
        ],
        request: bigtable_instance_admin.ListAppProfilesRequest,
        response: bigtable_instance_admin.ListAppProfilesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigtable_admin_v2.types.ListAppProfilesRequest):
                The initial request object.
            response (google.cloud.bigtable_admin_v2.types.ListAppProfilesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = bigtable_instance_admin.ListAppProfilesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[bigtable_instance_admin.ListAppProfilesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[instance.AppProfile]:
        async def async_generator():
            async for page in self.pages:
                for response in page.app_profiles:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHotTabletsPager:
    """A pager for iterating through ``list_hot_tablets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigtable_admin_v2.types.ListHotTabletsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``hot_tablets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListHotTablets`` requests and continue to iterate
    through the ``hot_tablets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigtable_admin_v2.types.ListHotTabletsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., bigtable_instance_admin.ListHotTabletsResponse],
        request: bigtable_instance_admin.ListHotTabletsRequest,
        response: bigtable_instance_admin.ListHotTabletsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigtable_admin_v2.types.ListHotTabletsRequest):
                The initial request object.
            response (google.cloud.bigtable_admin_v2.types.ListHotTabletsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = bigtable_instance_admin.ListHotTabletsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[bigtable_instance_admin.ListHotTabletsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[instance.HotTablet]:
        for page in self.pages:
            yield from page.hot_tablets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHotTabletsAsyncPager:
    """A pager for iterating through ``list_hot_tablets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigtable_admin_v2.types.ListHotTabletsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``hot_tablets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListHotTablets`` requests and continue to iterate
    through the ``hot_tablets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigtable_admin_v2.types.ListHotTabletsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[bigtable_instance_admin.ListHotTabletsResponse]
        ],
        request: bigtable_instance_admin.ListHotTabletsRequest,
        response: bigtable_instance_admin.ListHotTabletsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigtable_admin_v2.types.ListHotTabletsRequest):
                The initial request object.
            response (google.cloud.bigtable_admin_v2.types.ListHotTabletsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = bigtable_instance_admin.ListHotTabletsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[bigtable_instance_admin.ListHotTabletsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[instance.HotTablet]:
        async def async_generator():
            async for page in self.pages:
                for response in page.hot_tablets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
