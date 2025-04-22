# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.users.user_schema import UserSchema
from ....types.users.user_schema_public import UserSchemaPublic

__all__ = ["APIKeyResource", "AsyncAPIKeyResource"]


class APIKeyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return APIKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return APIKeyResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserSchemaPublic:
        """Get user when authenticated with API key."""
        return self._get(
            "/api/users/myself/api-key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserSchemaPublic,
        )

    def refresh(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserSchema:
        """Refresh the API key for an authenticated user"""
        return self._post(
            "/api/users/myself/api-key/refresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserSchema,
        )


class AsyncAPIKeyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncAPIKeyResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserSchemaPublic:
        """Get user when authenticated with API key."""
        return await self._get(
            "/api/users/myself/api-key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserSchemaPublic,
        )

    async def refresh(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserSchema:
        """Refresh the API key for an authenticated user"""
        return await self._post(
            "/api/users/myself/api-key/refresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserSchema,
        )


class APIKeyResourceWithRawResponse:
    def __init__(self, api_key: APIKeyResource) -> None:
        self._api_key = api_key

        self.retrieve = to_raw_response_wrapper(
            api_key.retrieve,
        )
        self.refresh = to_raw_response_wrapper(
            api_key.refresh,
        )


class AsyncAPIKeyResourceWithRawResponse:
    def __init__(self, api_key: AsyncAPIKeyResource) -> None:
        self._api_key = api_key

        self.retrieve = async_to_raw_response_wrapper(
            api_key.retrieve,
        )
        self.refresh = async_to_raw_response_wrapper(
            api_key.refresh,
        )


class APIKeyResourceWithStreamingResponse:
    def __init__(self, api_key: APIKeyResource) -> None:
        self._api_key = api_key

        self.retrieve = to_streamed_response_wrapper(
            api_key.retrieve,
        )
        self.refresh = to_streamed_response_wrapper(
            api_key.refresh,
        )


class AsyncAPIKeyResourceWithStreamingResponse:
    def __init__(self, api_key: AsyncAPIKeyResource) -> None:
        self._api_key = api_key

        self.retrieve = async_to_streamed_response_wrapper(
            api_key.retrieve,
        )
        self.refresh = async_to_streamed_response_wrapper(
            api_key.refresh,
        )
