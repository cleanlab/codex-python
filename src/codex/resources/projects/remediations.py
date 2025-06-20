# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
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

    def create(
        self,
        project_id: str,
        *,
        question: str,
        answer: Optional[str] | NotGiven = NOT_GIVEN,
        draft_answer: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def list(
        self,
        project_id: str,
        *,
        created_at_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_edited_at_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_edited_at_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_edited_by: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        sort: Optional[Literal["created_at", "last_edited_at", "resolved_logs_count"]] | NotGiven = NOT_GIVEN,
        status: Optional[List[Literal["ACTIVE", "DRAFT", "ACTIVE_WITH_DRAFT", "PAUSED"]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RemediationListResponse:
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
        return self._get(
            f"/api/projects/{project_id}/remediations/",
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
            cast_to=RemediationListResponse,
        )

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def create(
        self,
        project_id: str,
        *,
        question: str,
        answer: Optional[str] | NotGiven = NOT_GIVEN,
        draft_answer: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def list(
        self,
        project_id: str,
        *,
        created_at_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_edited_at_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_edited_at_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        last_edited_by: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        sort: Optional[Literal["created_at", "last_edited_at", "resolved_logs_count"]] | NotGiven = NOT_GIVEN,
        status: Optional[List[Literal["ACTIVE", "DRAFT", "ACTIVE_WITH_DRAFT", "PAUSED"]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RemediationListResponse:
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
        return await self._get(
            f"/api/projects/{project_id}/remediations/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
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
            cast_to=RemediationListResponse,
        )

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

        self.create = to_raw_response_wrapper(
            remediations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            remediations.retrieve,
        )
        self.list = to_raw_response_wrapper(
            remediations.list,
        )
        self.delete = to_raw_response_wrapper(
            remediations.delete,
        )
        self.edit_answer = to_raw_response_wrapper(
            remediations.edit_answer,
        )
        self.edit_draft_answer = to_raw_response_wrapper(
            remediations.edit_draft_answer,
        )
        self.get_resolved_logs_count = to_raw_response_wrapper(
            remediations.get_resolved_logs_count,
        )
        self.list_resolved_logs = to_raw_response_wrapper(
            remediations.list_resolved_logs,
        )
        self.pause = to_raw_response_wrapper(
            remediations.pause,
        )
        self.publish = to_raw_response_wrapper(
            remediations.publish,
        )
        self.unpause = to_raw_response_wrapper(
            remediations.unpause,
        )


class AsyncRemediationsResourceWithRawResponse:
    def __init__(self, remediations: AsyncRemediationsResource) -> None:
        self._remediations = remediations

        self.create = async_to_raw_response_wrapper(
            remediations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            remediations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            remediations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            remediations.delete,
        )
        self.edit_answer = async_to_raw_response_wrapper(
            remediations.edit_answer,
        )
        self.edit_draft_answer = async_to_raw_response_wrapper(
            remediations.edit_draft_answer,
        )
        self.get_resolved_logs_count = async_to_raw_response_wrapper(
            remediations.get_resolved_logs_count,
        )
        self.list_resolved_logs = async_to_raw_response_wrapper(
            remediations.list_resolved_logs,
        )
        self.pause = async_to_raw_response_wrapper(
            remediations.pause,
        )
        self.publish = async_to_raw_response_wrapper(
            remediations.publish,
        )
        self.unpause = async_to_raw_response_wrapper(
            remediations.unpause,
        )


class RemediationsResourceWithStreamingResponse:
    def __init__(self, remediations: RemediationsResource) -> None:
        self._remediations = remediations

        self.create = to_streamed_response_wrapper(
            remediations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            remediations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            remediations.list,
        )
        self.delete = to_streamed_response_wrapper(
            remediations.delete,
        )
        self.edit_answer = to_streamed_response_wrapper(
            remediations.edit_answer,
        )
        self.edit_draft_answer = to_streamed_response_wrapper(
            remediations.edit_draft_answer,
        )
        self.get_resolved_logs_count = to_streamed_response_wrapper(
            remediations.get_resolved_logs_count,
        )
        self.list_resolved_logs = to_streamed_response_wrapper(
            remediations.list_resolved_logs,
        )
        self.pause = to_streamed_response_wrapper(
            remediations.pause,
        )
        self.publish = to_streamed_response_wrapper(
            remediations.publish,
        )
        self.unpause = to_streamed_response_wrapper(
            remediations.unpause,
        )


class AsyncRemediationsResourceWithStreamingResponse:
    def __init__(self, remediations: AsyncRemediationsResource) -> None:
        self._remediations = remediations

        self.create = async_to_streamed_response_wrapper(
            remediations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            remediations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            remediations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            remediations.delete,
        )
        self.edit_answer = async_to_streamed_response_wrapper(
            remediations.edit_answer,
        )
        self.edit_draft_answer = async_to_streamed_response_wrapper(
            remediations.edit_draft_answer,
        )
        self.get_resolved_logs_count = async_to_streamed_response_wrapper(
            remediations.get_resolved_logs_count,
        )
        self.list_resolved_logs = async_to_streamed_response_wrapper(
            remediations.list_resolved_logs,
        )
        self.pause = async_to_streamed_response_wrapper(
            remediations.pause,
        )
        self.publish = async_to_streamed_response_wrapper(
            remediations.publish,
        )
        self.unpause = async_to_streamed_response_wrapper(
            remediations.unpause,
        )
