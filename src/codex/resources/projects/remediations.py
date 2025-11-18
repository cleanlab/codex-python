# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPageRemediations, AsyncOffsetPageRemediations
from ..._base_client import AsyncPaginator, make_request_options
from ...types.projects import (
    remediation_list_params,
    remediation_create_params,
    remediation_edit_answer_params,
    remediation_edit_draft_answer_params,
)
from ...types.projects.remediation_list_response import RemediationListResponse
from ...types.projects.remediation_pause_response import RemediationPauseResponse
from ...types.projects.remediation_create_response import RemediationCreateResponse
from ...types.projects.remediation_publish_response import RemediationPublishResponse
from ...types.projects.remediation_unpause_response import RemediationUnpauseResponse
from ...types.projects.remediation_retrieve_response import RemediationRetrieveResponse
from ...types.projects.remediation_edit_answer_response import RemediationEditAnswerResponse
from ...types.projects.remediation_edit_draft_answer_response import RemediationEditDraftAnswerResponse
from ...types.projects.remediation_list_resolved_logs_response import RemediationListResolvedLogsResponse
from ...types.projects.remediation_get_resolved_logs_count_response import RemediationGetResolvedLogsCountResponse

__all__ = ["RemediationsResource", "AsyncRemediationsResource"]


class RemediationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RemediationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return RemediationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RemediationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return RemediationsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def create(
        self,
        project_id: str,
        *,
        question: str,
        answer: Optional[str] | Omit = omit,
        draft_answer: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationCreateResponse:
        """
        Create Remediation Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/api/projects/{project_id}/remediations/",
            body=maybe_transform(
                {
                    "question": question,
                    "answer": answer,
                    "draft_answer": draft_answer,
                },
                remediation_create_params.RemediationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationCreateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def retrieve(
        self,
        remediation_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationRetrieveResponse:
        """
        Get Remediation Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return self._get(
            f"/api/projects/{project_id}/remediations/{remediation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationRetrieveResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def list(
        self,
        project_id: str,
        *,
        created_at_end: Union[str, datetime, None] | Omit = omit,
        created_at_start: Union[str, datetime, None] | Omit = omit,
        last_edited_at_end: Union[str, datetime, None] | Omit = omit,
        last_edited_at_start: Union[str, datetime, None] | Omit = omit,
        last_edited_by: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        sort: Optional[Literal["created_at", "last_edited_at", "resolved_logs_count"]] | Omit = omit,
        status: Optional[List[Literal["ACTIVE", "DRAFT", "ACTIVE_WITH_DRAFT", "PAUSED"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPageRemediations[RemediationListResponse]:
        """
        List remediations by project ID.

        Args:
          created_at_end: Filter remediations created at or before this timestamp

          created_at_start: Filter remediations created at or after this timestamp

          last_edited_at_end: Filter remediations last edited at or before this timestamp

          last_edited_at_start: Filter remediations last edited at or after this timestamp

          last_edited_by: Filter by last edited by user ID

          status: Filter remediations that have ANY of these statuses (OR operation)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get_api_list(
            f"/api/projects/{project_id}/remediations/",
            page=SyncOffsetPageRemediations[RemediationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_end": created_at_end,
                        "created_at_start": created_at_start,
                        "last_edited_at_end": last_edited_at_end,
                        "last_edited_at_start": last_edited_at_start,
                        "last_edited_by": last_edited_by,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "sort": sort,
                        "status": status,
                    },
                    remediation_list_params.RemediationListParams,
                ),
            ),
            model=RemediationListResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def delete(
        self,
        remediation_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Remediation Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/projects/{project_id}/remediations/{remediation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    def edit_answer(
        self,
        remediation_id: str,
        *,
        project_id: str,
        answer: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationEditAnswerResponse:
        """
        Edit Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return self._patch(
            f"/api/projects/{project_id}/remediations/{remediation_id}/edit_answer",
            body=maybe_transform({"answer": answer}, remediation_edit_answer_params.RemediationEditAnswerParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationEditAnswerResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def edit_draft_answer(
        self,
        remediation_id: str,
        *,
        project_id: str,
        draft_answer: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationEditDraftAnswerResponse:
        """
        Edit Draft Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return self._patch(
            f"/api/projects/{project_id}/remediations/{remediation_id}/edit_draft_answer",
            body=maybe_transform(
                {"draft_answer": draft_answer}, remediation_edit_draft_answer_params.RemediationEditDraftAnswerParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationEditDraftAnswerResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def get_resolved_logs_count(
        self,
        remediation_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationGetResolvedLogsCountResponse:
        """
        Get Remediation With Resolved Logs Count Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return self._get(
            f"/api/projects/{project_id}/remediations/{remediation_id}/resolved_logs_count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationGetResolvedLogsCountResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def list_resolved_logs(
        self,
        remediation_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationListResolvedLogsResponse:
        """
        List resolved logs by remediation ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return self._get(
            f"/api/projects/{project_id}/remediations/{remediation_id}/resolved_logs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationListResolvedLogsResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def pause(
        self,
        remediation_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationPauseResponse:
        """
        Pause Remediation Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return self._patch(
            f"/api/projects/{project_id}/remediations/{remediation_id}/pause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationPauseResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def publish(
        self,
        remediation_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationPublishResponse:
        """
        Publish Remediation Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return self._patch(
            f"/api/projects/{project_id}/remediations/{remediation_id}/publish",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationPublishResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def unpause(
        self,
        remediation_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationUnpauseResponse:
        """
        Unpause Remediation Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return self._patch(
            f"/api/projects/{project_id}/remediations/{remediation_id}/unpause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationUnpauseResponse,
        )


class AsyncRemediationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRemediationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRemediationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRemediationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncRemediationsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def create(
        self,
        project_id: str,
        *,
        question: str,
        answer: Optional[str] | Omit = omit,
        draft_answer: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationCreateResponse:
        """
        Create Remediation Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/api/projects/{project_id}/remediations/",
            body=await async_maybe_transform(
                {
                    "question": question,
                    "answer": answer,
                    "draft_answer": draft_answer,
                },
                remediation_create_params.RemediationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationCreateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def retrieve(
        self,
        remediation_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationRetrieveResponse:
        """
        Get Remediation Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/remediations/{remediation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationRetrieveResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def list(
        self,
        project_id: str,
        *,
        created_at_end: Union[str, datetime, None] | Omit = omit,
        created_at_start: Union[str, datetime, None] | Omit = omit,
        last_edited_at_end: Union[str, datetime, None] | Omit = omit,
        last_edited_at_start: Union[str, datetime, None] | Omit = omit,
        last_edited_by: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        sort: Optional[Literal["created_at", "last_edited_at", "resolved_logs_count"]] | Omit = omit,
        status: Optional[List[Literal["ACTIVE", "DRAFT", "ACTIVE_WITH_DRAFT", "PAUSED"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RemediationListResponse, AsyncOffsetPageRemediations[RemediationListResponse]]:
        """
        List remediations by project ID.

        Args:
          created_at_end: Filter remediations created at or before this timestamp

          created_at_start: Filter remediations created at or after this timestamp

          last_edited_at_end: Filter remediations last edited at or before this timestamp

          last_edited_at_start: Filter remediations last edited at or after this timestamp

          last_edited_by: Filter by last edited by user ID

          status: Filter remediations that have ANY of these statuses (OR operation)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get_api_list(
            f"/api/projects/{project_id}/remediations/",
            page=AsyncOffsetPageRemediations[RemediationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_end": created_at_end,
                        "created_at_start": created_at_start,
                        "last_edited_at_end": last_edited_at_end,
                        "last_edited_at_start": last_edited_at_start,
                        "last_edited_by": last_edited_by,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "sort": sort,
                        "status": status,
                    },
                    remediation_list_params.RemediationListParams,
                ),
            ),
            model=RemediationListResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def delete(
        self,
        remediation_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Remediation Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/projects/{project_id}/remediations/{remediation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    async def edit_answer(
        self,
        remediation_id: str,
        *,
        project_id: str,
        answer: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationEditAnswerResponse:
        """
        Edit Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return await self._patch(
            f"/api/projects/{project_id}/remediations/{remediation_id}/edit_answer",
            body=await async_maybe_transform(
                {"answer": answer}, remediation_edit_answer_params.RemediationEditAnswerParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationEditAnswerResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def edit_draft_answer(
        self,
        remediation_id: str,
        *,
        project_id: str,
        draft_answer: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationEditDraftAnswerResponse:
        """
        Edit Draft Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return await self._patch(
            f"/api/projects/{project_id}/remediations/{remediation_id}/edit_draft_answer",
            body=await async_maybe_transform(
                {"draft_answer": draft_answer}, remediation_edit_draft_answer_params.RemediationEditDraftAnswerParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationEditDraftAnswerResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def get_resolved_logs_count(
        self,
        remediation_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationGetResolvedLogsCountResponse:
        """
        Get Remediation With Resolved Logs Count Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/remediations/{remediation_id}/resolved_logs_count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationGetResolvedLogsCountResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def list_resolved_logs(
        self,
        remediation_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationListResolvedLogsResponse:
        """
        List resolved logs by remediation ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/remediations/{remediation_id}/resolved_logs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationListResolvedLogsResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def pause(
        self,
        remediation_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationPauseResponse:
        """
        Pause Remediation Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return await self._patch(
            f"/api/projects/{project_id}/remediations/{remediation_id}/pause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationPauseResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def publish(
        self,
        remediation_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationPublishResponse:
        """
        Publish Remediation Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return await self._patch(
            f"/api/projects/{project_id}/remediations/{remediation_id}/publish",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationPublishResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def unpause(
        self,
        remediation_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationUnpauseResponse:
        """
        Unpause Remediation Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return await self._patch(
            f"/api/projects/{project_id}/remediations/{remediation_id}/unpause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationUnpauseResponse,
        )


class RemediationsResourceWithRawResponse:
    def __init__(self, remediations: RemediationsResource) -> None:
        self._remediations = remediations

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                remediations.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                remediations.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                remediations.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                remediations.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit_answer = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                remediations.edit_answer,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit_draft_answer = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                remediations.edit_draft_answer,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_resolved_logs_count = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                remediations.get_resolved_logs_count,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_resolved_logs = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                remediations.list_resolved_logs,  # pyright: ignore[reportDeprecated],
            )
        )
        self.pause = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                remediations.pause,  # pyright: ignore[reportDeprecated],
            )
        )
        self.publish = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                remediations.publish,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unpause = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                remediations.unpause,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncRemediationsResourceWithRawResponse:
    def __init__(self, remediations: AsyncRemediationsResource) -> None:
        self._remediations = remediations

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                remediations.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                remediations.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                remediations.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                remediations.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit_answer = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                remediations.edit_answer,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit_draft_answer = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                remediations.edit_draft_answer,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_resolved_logs_count = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                remediations.get_resolved_logs_count,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_resolved_logs = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                remediations.list_resolved_logs,  # pyright: ignore[reportDeprecated],
            )
        )
        self.pause = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                remediations.pause,  # pyright: ignore[reportDeprecated],
            )
        )
        self.publish = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                remediations.publish,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unpause = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                remediations.unpause,  # pyright: ignore[reportDeprecated],
            )
        )


class RemediationsResourceWithStreamingResponse:
    def __init__(self, remediations: RemediationsResource) -> None:
        self._remediations = remediations

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                remediations.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                remediations.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                remediations.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                remediations.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit_answer = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                remediations.edit_answer,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit_draft_answer = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                remediations.edit_draft_answer,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_resolved_logs_count = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                remediations.get_resolved_logs_count,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_resolved_logs = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                remediations.list_resolved_logs,  # pyright: ignore[reportDeprecated],
            )
        )
        self.pause = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                remediations.pause,  # pyright: ignore[reportDeprecated],
            )
        )
        self.publish = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                remediations.publish,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unpause = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                remediations.unpause,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncRemediationsResourceWithStreamingResponse:
    def __init__(self, remediations: AsyncRemediationsResource) -> None:
        self._remediations = remediations

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                remediations.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                remediations.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                remediations.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                remediations.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit_answer = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                remediations.edit_answer,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit_draft_answer = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                remediations.edit_draft_answer,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_resolved_logs_count = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                remediations.get_resolved_logs_count,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_resolved_logs = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                remediations.list_resolved_logs,  # pyright: ignore[reportDeprecated],
            )
        )
        self.pause = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                remediations.pause,  # pyright: ignore[reportDeprecated],
            )
        )
        self.publish = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                remediations.publish,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unpause = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                remediations.unpause,  # pyright: ignore[reportDeprecated],
            )
        )
