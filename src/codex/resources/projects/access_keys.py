# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.projects import access_key_create_params, access_key_update_params
from ...types.projects.access_key_schema import AccessKeySchema
from ...types.projects.access_key_list_response import AccessKeyListResponse
from ...types.projects.access_key_retrieve_project_id_response import AccessKeyRetrieveProjectIDResponse

__all__ = ["AccessKeysResource", "AsyncAccessKeysResource"]


class AccessKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AccessKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AccessKeysResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: str,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        x_client_library_version: str | NotGiven = NOT_GIVEN,
        x_integration_type: str | NotGiven = NOT_GIVEN,
        x_source: str | NotGiven = NOT_GIVEN,
        x_stainless_package_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessKeySchema:
        """
        Create a new access key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "x-client-library-version": x_client_library_version,
                    "x-integration-type": x_integration_type,
                    "x-source": x_source,
                    "x-stainless-package-version": x_stainless_package_version,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            f"/api/projects/{project_id}/access_keys/",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "expires_at": expires_at,
                },
                access_key_create_params.AccessKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessKeySchema,
        )

    def retrieve(
        self,
        access_key_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessKeySchema:
        """
        Get a single access key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not access_key_id:
            raise ValueError(f"Expected a non-empty value for `access_key_id` but received {access_key_id!r}")
        return self._get(
            f"/api/projects/{project_id}/access_keys/{access_key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessKeySchema,
        )

    def update(
        self,
        access_key_id: str,
        *,
        project_id: str,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessKeySchema:
        """
        Update an existing access key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not access_key_id:
            raise ValueError(f"Expected a non-empty value for `access_key_id` but received {access_key_id!r}")
        return self._put(
            f"/api/projects/{project_id}/access_keys/{access_key_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "expires_at": expires_at,
                },
                access_key_update_params.AccessKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessKeySchema,
        )

    def list(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessKeyListResponse:
        """
        List all access keys for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/api/projects/{project_id}/access_keys/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessKeyListResponse,
        )

    def delete(
        self,
        access_key_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an existing access key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not access_key_id:
            raise ValueError(f"Expected a non-empty value for `access_key_id` but received {access_key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/projects/{project_id}/access_keys/{access_key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_project_id(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessKeyRetrieveProjectIDResponse:
        """Get the project ID from an access key."""
        return self._get(
            "/api/projects/id_from_access_key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessKeyRetrieveProjectIDResponse,
        )

    def revoke(
        self,
        access_key_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Revoke an access key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not access_key_id:
            raise ValueError(f"Expected a non-empty value for `access_key_id` but received {access_key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/api/projects/{project_id}/access_keys/{access_key_id}/revoke",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAccessKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccessKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncAccessKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: str,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        x_client_library_version: str | NotGiven = NOT_GIVEN,
        x_integration_type: str | NotGiven = NOT_GIVEN,
        x_source: str | NotGiven = NOT_GIVEN,
        x_stainless_package_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessKeySchema:
        """
        Create a new access key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "x-client-library-version": x_client_library_version,
                    "x-integration-type": x_integration_type,
                    "x-source": x_source,
                    "x-stainless-package-version": x_stainless_package_version,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            f"/api/projects/{project_id}/access_keys/",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "expires_at": expires_at,
                },
                access_key_create_params.AccessKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessKeySchema,
        )

    async def retrieve(
        self,
        access_key_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessKeySchema:
        """
        Get a single access key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not access_key_id:
            raise ValueError(f"Expected a non-empty value for `access_key_id` but received {access_key_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/access_keys/{access_key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessKeySchema,
        )

    async def update(
        self,
        access_key_id: str,
        *,
        project_id: str,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessKeySchema:
        """
        Update an existing access key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not access_key_id:
            raise ValueError(f"Expected a non-empty value for `access_key_id` but received {access_key_id!r}")
        return await self._put(
            f"/api/projects/{project_id}/access_keys/{access_key_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "expires_at": expires_at,
                },
                access_key_update_params.AccessKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessKeySchema,
        )

    async def list(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessKeyListResponse:
        """
        List all access keys for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/access_keys/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessKeyListResponse,
        )

    async def delete(
        self,
        access_key_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an existing access key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not access_key_id:
            raise ValueError(f"Expected a non-empty value for `access_key_id` but received {access_key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/projects/{project_id}/access_keys/{access_key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_project_id(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessKeyRetrieveProjectIDResponse:
        """Get the project ID from an access key."""
        return await self._get(
            "/api/projects/id_from_access_key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessKeyRetrieveProjectIDResponse,
        )

    async def revoke(
        self,
        access_key_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Revoke an access key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not access_key_id:
            raise ValueError(f"Expected a non-empty value for `access_key_id` but received {access_key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/api/projects/{project_id}/access_keys/{access_key_id}/revoke",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AccessKeysResourceWithRawResponse:
    def __init__(self, access_keys: AccessKeysResource) -> None:
        self._access_keys = access_keys

        self.create = to_raw_response_wrapper(
            access_keys.create,
        )
        self.retrieve = to_raw_response_wrapper(
            access_keys.retrieve,
        )
        self.update = to_raw_response_wrapper(
            access_keys.update,
        )
        self.list = to_raw_response_wrapper(
            access_keys.list,
        )
        self.delete = to_raw_response_wrapper(
            access_keys.delete,
        )
        self.retrieve_project_id = to_raw_response_wrapper(
            access_keys.retrieve_project_id,
        )
        self.revoke = to_raw_response_wrapper(
            access_keys.revoke,
        )


class AsyncAccessKeysResourceWithRawResponse:
    def __init__(self, access_keys: AsyncAccessKeysResource) -> None:
        self._access_keys = access_keys

        self.create = async_to_raw_response_wrapper(
            access_keys.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            access_keys.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            access_keys.update,
        )
        self.list = async_to_raw_response_wrapper(
            access_keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            access_keys.delete,
        )
        self.retrieve_project_id = async_to_raw_response_wrapper(
            access_keys.retrieve_project_id,
        )
        self.revoke = async_to_raw_response_wrapper(
            access_keys.revoke,
        )


class AccessKeysResourceWithStreamingResponse:
    def __init__(self, access_keys: AccessKeysResource) -> None:
        self._access_keys = access_keys

        self.create = to_streamed_response_wrapper(
            access_keys.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            access_keys.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            access_keys.update,
        )
        self.list = to_streamed_response_wrapper(
            access_keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            access_keys.delete,
        )
        self.retrieve_project_id = to_streamed_response_wrapper(
            access_keys.retrieve_project_id,
        )
        self.revoke = to_streamed_response_wrapper(
            access_keys.revoke,
        )


class AsyncAccessKeysResourceWithStreamingResponse:
    def __init__(self, access_keys: AsyncAccessKeysResource) -> None:
        self._access_keys = access_keys

        self.create = async_to_streamed_response_wrapper(
            access_keys.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            access_keys.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            access_keys.update,
        )
        self.list = async_to_streamed_response_wrapper(
            access_keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            access_keys.delete,
        )
        self.retrieve_project_id = async_to_streamed_response_wrapper(
            access_keys.retrieve_project_id,
        )
        self.revoke = async_to_streamed_response_wrapper(
            access_keys.revoke,
        )
