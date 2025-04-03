# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.projects import entry_query_params, entry_create_params, entry_update_params
from ...types.projects.entry import Entry
from ...types.projects.entry_query_response import EntryQueryResponse

__all__ = ["EntriesResource", "AsyncEntriesResource"]


class EntriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return EntriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return EntriesResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: str,
        *,
        question: str,
        answer: Optional[str] | NotGiven = NOT_GIVEN,
        client_query_metadata: Iterable[object] | NotGiven = NOT_GIVEN,
        draft_answer: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> Entry:
        """
        Create a new knowledge entry for a project.

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
            f"/api/projects/{project_id}/entries/",
            body=maybe_transform(
                {
                    "question": question,
                    "answer": answer,
                    "client_query_metadata": client_query_metadata,
                    "draft_answer": draft_answer,
                },
                entry_create_params.EntryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    def retrieve(
        self,
        entry_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entry:
        """
        Get a knowledge entry for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return self._get(
            f"/api/projects/{project_id}/entries/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    def update(
        self,
        entry_id: str,
        *,
        project_id: str,
        answer: Optional[str] | NotGiven = NOT_GIVEN,
        draft_answer: Optional[str] | NotGiven = NOT_GIVEN,
        question: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entry:
        """
        Update a knowledge entry for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return self._put(
            f"/api/projects/{project_id}/entries/{entry_id}",
            body=maybe_transform(
                {
                    "answer": answer,
                    "draft_answer": draft_answer,
                    "question": question,
                },
                entry_update_params.EntryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    def delete(
        self,
        entry_id: str,
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
        Delete a knowledge entry for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/projects/{project_id}/entries/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def query(
        self,
        project_id: str,
        *,
        question: str,
        client_metadata: Optional[object] | NotGiven = NOT_GIVEN,
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
    ) -> EntryQueryResponse:
        """
        Query Entries Route

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
            f"/api/projects/{project_id}/entries/query",
            body=maybe_transform(
                {
                    "question": question,
                    "client_metadata": client_metadata,
                },
                entry_query_params.EntryQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntryQueryResponse,
        )


class AsyncEntriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncEntriesResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: str,
        *,
        question: str,
        answer: Optional[str] | NotGiven = NOT_GIVEN,
        client_query_metadata: Iterable[object] | NotGiven = NOT_GIVEN,
        draft_answer: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> Entry:
        """
        Create a new knowledge entry for a project.

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
            f"/api/projects/{project_id}/entries/",
            body=await async_maybe_transform(
                {
                    "question": question,
                    "answer": answer,
                    "client_query_metadata": client_query_metadata,
                    "draft_answer": draft_answer,
                },
                entry_create_params.EntryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    async def retrieve(
        self,
        entry_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entry:
        """
        Get a knowledge entry for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/entries/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    async def update(
        self,
        entry_id: str,
        *,
        project_id: str,
        answer: Optional[str] | NotGiven = NOT_GIVEN,
        draft_answer: Optional[str] | NotGiven = NOT_GIVEN,
        question: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entry:
        """
        Update a knowledge entry for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return await self._put(
            f"/api/projects/{project_id}/entries/{entry_id}",
            body=await async_maybe_transform(
                {
                    "answer": answer,
                    "draft_answer": draft_answer,
                    "question": question,
                },
                entry_update_params.EntryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    async def delete(
        self,
        entry_id: str,
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
        Delete a knowledge entry for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/projects/{project_id}/entries/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def query(
        self,
        project_id: str,
        *,
        question: str,
        client_metadata: Optional[object] | NotGiven = NOT_GIVEN,
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
    ) -> EntryQueryResponse:
        """
        Query Entries Route

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
            f"/api/projects/{project_id}/entries/query",
            body=await async_maybe_transform(
                {
                    "question": question,
                    "client_metadata": client_metadata,
                },
                entry_query_params.EntryQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntryQueryResponse,
        )


class EntriesResourceWithRawResponse:
    def __init__(self, entries: EntriesResource) -> None:
        self._entries = entries

        self.create = to_raw_response_wrapper(
            entries.create,
        )
        self.retrieve = to_raw_response_wrapper(
            entries.retrieve,
        )
        self.update = to_raw_response_wrapper(
            entries.update,
        )
        self.delete = to_raw_response_wrapper(
            entries.delete,
        )
        self.query = to_raw_response_wrapper(
            entries.query,
        )


class AsyncEntriesResourceWithRawResponse:
    def __init__(self, entries: AsyncEntriesResource) -> None:
        self._entries = entries

        self.create = async_to_raw_response_wrapper(
            entries.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            entries.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            entries.update,
        )
        self.delete = async_to_raw_response_wrapper(
            entries.delete,
        )
        self.query = async_to_raw_response_wrapper(
            entries.query,
        )


class EntriesResourceWithStreamingResponse:
    def __init__(self, entries: EntriesResource) -> None:
        self._entries = entries

        self.create = to_streamed_response_wrapper(
            entries.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            entries.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            entries.update,
        )
        self.delete = to_streamed_response_wrapper(
            entries.delete,
        )
        self.query = to_streamed_response_wrapper(
            entries.query,
        )


class AsyncEntriesResourceWithStreamingResponse:
    def __init__(self, entries: AsyncEntriesResource) -> None:
        self._entries = entries

        self.create = async_to_streamed_response_wrapper(
            entries.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            entries.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            entries.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            entries.delete,
        )
        self.query = async_to_streamed_response_wrapper(
            entries.query,
        )
