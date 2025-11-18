# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPageExpertAnswers, AsyncOffsetPageExpertAnswers
from ...._base_client import AsyncPaginator, make_request_options
from ....types.projects.remediations import (
    expert_answer_list_params,
    expert_answer_create_params,
    expert_answer_edit_answer_params,
    expert_answer_edit_draft_answer_params,
)
from ....types.projects.remediations.expert_answer_list_response import ExpertAnswerListResponse
from ....types.projects.remediations.expert_answer_pause_response import ExpertAnswerPauseResponse
from ....types.projects.remediations.expert_answer_create_response import ExpertAnswerCreateResponse
from ....types.projects.remediations.expert_answer_publish_response import ExpertAnswerPublishResponse
from ....types.projects.remediations.expert_answer_unpause_response import ExpertAnswerUnpauseResponse
from ....types.projects.remediations.expert_answer_retrieve_response import ExpertAnswerRetrieveResponse
from ....types.projects.remediations.expert_answer_edit_answer_response import ExpertAnswerEditAnswerResponse
from ....types.projects.remediations.expert_answer_edit_draft_answer_response import ExpertAnswerEditDraftAnswerResponse

__all__ = ["ExpertAnswersResource", "AsyncExpertAnswersResource"]


class ExpertAnswersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExpertAnswersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return ExpertAnswersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExpertAnswersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return ExpertAnswersResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: str,
        *,
        query: str,
        answer: Optional[str] | Omit = omit,
        draft_answer: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertAnswerCreateResponse:
        """
        Create Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/api/projects/{project_id}/expert_answers/",
            body=maybe_transform(
                {
                    "query": query,
                    "answer": answer,
                    "draft_answer": draft_answer,
                },
                expert_answer_create_params.ExpertAnswerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertAnswerCreateResponse,
        )

    def retrieve(
        self,
        expert_answer_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertAnswerRetrieveResponse:
        """
        Get Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_answer_id:
            raise ValueError(f"Expected a non-empty value for `expert_answer_id` but received {expert_answer_id!r}")
        return self._get(
            f"/api/projects/{project_id}/expert_answers/{expert_answer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertAnswerRetrieveResponse,
        )

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
    ) -> SyncOffsetPageExpertAnswers[ExpertAnswerListResponse]:
        """
        List Expert Answers Route

        Args:
          created_at_end: Filter remediations created at or before this timestamp

          created_at_start: Filter remediations created at or after this timestamp

          last_edited_at_end: Filter remediations last edited at or before this timestamp

          last_edited_at_start: Filter remediations last edited at or after this timestamp

          last_edited_by: Filter by last edited by user ID

          status: Filter expert answers that have ANY of these statuses (OR operation)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get_api_list(
            f"/api/projects/{project_id}/expert_answers/",
            page=SyncOffsetPageExpertAnswers[ExpertAnswerListResponse],
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
                    expert_answer_list_params.ExpertAnswerListParams,
                ),
            ),
            model=ExpertAnswerListResponse,
        )

    def delete(
        self,
        expert_answer_id: str,
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
        Delete Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_answer_id:
            raise ValueError(f"Expected a non-empty value for `expert_answer_id` but received {expert_answer_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/projects/{project_id}/expert_answers/{expert_answer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def edit_answer(
        self,
        expert_answer_id: str,
        *,
        project_id: str,
        answer: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertAnswerEditAnswerResponse:
        """
        Edit Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_answer_id:
            raise ValueError(f"Expected a non-empty value for `expert_answer_id` but received {expert_answer_id!r}")
        return self._patch(
            f"/api/projects/{project_id}/expert_answers/{expert_answer_id}/edit_expert_answer",
            body=maybe_transform({"answer": answer}, expert_answer_edit_answer_params.ExpertAnswerEditAnswerParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertAnswerEditAnswerResponse,
        )

    def edit_draft_answer(
        self,
        expert_answer_id: str,
        *,
        project_id: str,
        draft_answer: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertAnswerEditDraftAnswerResponse:
        """
        Edit Draft Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_answer_id:
            raise ValueError(f"Expected a non-empty value for `expert_answer_id` but received {expert_answer_id!r}")
        return self._patch(
            f"/api/projects/{project_id}/expert_answers/{expert_answer_id}/edit_draft_expert_answer",
            body=maybe_transform(
                {"draft_answer": draft_answer}, expert_answer_edit_draft_answer_params.ExpertAnswerEditDraftAnswerParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertAnswerEditDraftAnswerResponse,
        )

    def pause(
        self,
        expert_answer_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertAnswerPauseResponse:
        """
        Pause Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_answer_id:
            raise ValueError(f"Expected a non-empty value for `expert_answer_id` but received {expert_answer_id!r}")
        return self._patch(
            f"/api/projects/{project_id}/expert_answers/{expert_answer_id}/pause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertAnswerPauseResponse,
        )

    def publish(
        self,
        expert_answer_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertAnswerPublishResponse:
        """
        Publish Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_answer_id:
            raise ValueError(f"Expected a non-empty value for `expert_answer_id` but received {expert_answer_id!r}")
        return self._patch(
            f"/api/projects/{project_id}/expert_answers/{expert_answer_id}/publish",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertAnswerPublishResponse,
        )

    def unpause(
        self,
        expert_answer_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertAnswerUnpauseResponse:
        """
        Unpause Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_answer_id:
            raise ValueError(f"Expected a non-empty value for `expert_answer_id` but received {expert_answer_id!r}")
        return self._patch(
            f"/api/projects/{project_id}/expert_answers/{expert_answer_id}/unpause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertAnswerUnpauseResponse,
        )


class AsyncExpertAnswersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExpertAnswersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExpertAnswersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExpertAnswersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncExpertAnswersResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: str,
        *,
        query: str,
        answer: Optional[str] | Omit = omit,
        draft_answer: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertAnswerCreateResponse:
        """
        Create Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/api/projects/{project_id}/expert_answers/",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "answer": answer,
                    "draft_answer": draft_answer,
                },
                expert_answer_create_params.ExpertAnswerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertAnswerCreateResponse,
        )

    async def retrieve(
        self,
        expert_answer_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertAnswerRetrieveResponse:
        """
        Get Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_answer_id:
            raise ValueError(f"Expected a non-empty value for `expert_answer_id` but received {expert_answer_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/expert_answers/{expert_answer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertAnswerRetrieveResponse,
        )

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
    ) -> AsyncPaginator[ExpertAnswerListResponse, AsyncOffsetPageExpertAnswers[ExpertAnswerListResponse]]:
        """
        List Expert Answers Route

        Args:
          created_at_end: Filter remediations created at or before this timestamp

          created_at_start: Filter remediations created at or after this timestamp

          last_edited_at_end: Filter remediations last edited at or before this timestamp

          last_edited_at_start: Filter remediations last edited at or after this timestamp

          last_edited_by: Filter by last edited by user ID

          status: Filter expert answers that have ANY of these statuses (OR operation)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get_api_list(
            f"/api/projects/{project_id}/expert_answers/",
            page=AsyncOffsetPageExpertAnswers[ExpertAnswerListResponse],
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
                    expert_answer_list_params.ExpertAnswerListParams,
                ),
            ),
            model=ExpertAnswerListResponse,
        )

    async def delete(
        self,
        expert_answer_id: str,
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
        Delete Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_answer_id:
            raise ValueError(f"Expected a non-empty value for `expert_answer_id` but received {expert_answer_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/projects/{project_id}/expert_answers/{expert_answer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def edit_answer(
        self,
        expert_answer_id: str,
        *,
        project_id: str,
        answer: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertAnswerEditAnswerResponse:
        """
        Edit Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_answer_id:
            raise ValueError(f"Expected a non-empty value for `expert_answer_id` but received {expert_answer_id!r}")
        return await self._patch(
            f"/api/projects/{project_id}/expert_answers/{expert_answer_id}/edit_expert_answer",
            body=await async_maybe_transform(
                {"answer": answer}, expert_answer_edit_answer_params.ExpertAnswerEditAnswerParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertAnswerEditAnswerResponse,
        )

    async def edit_draft_answer(
        self,
        expert_answer_id: str,
        *,
        project_id: str,
        draft_answer: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertAnswerEditDraftAnswerResponse:
        """
        Edit Draft Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_answer_id:
            raise ValueError(f"Expected a non-empty value for `expert_answer_id` but received {expert_answer_id!r}")
        return await self._patch(
            f"/api/projects/{project_id}/expert_answers/{expert_answer_id}/edit_draft_expert_answer",
            body=await async_maybe_transform(
                {"draft_answer": draft_answer}, expert_answer_edit_draft_answer_params.ExpertAnswerEditDraftAnswerParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertAnswerEditDraftAnswerResponse,
        )

    async def pause(
        self,
        expert_answer_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertAnswerPauseResponse:
        """
        Pause Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_answer_id:
            raise ValueError(f"Expected a non-empty value for `expert_answer_id` but received {expert_answer_id!r}")
        return await self._patch(
            f"/api/projects/{project_id}/expert_answers/{expert_answer_id}/pause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertAnswerPauseResponse,
        )

    async def publish(
        self,
        expert_answer_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertAnswerPublishResponse:
        """
        Publish Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_answer_id:
            raise ValueError(f"Expected a non-empty value for `expert_answer_id` but received {expert_answer_id!r}")
        return await self._patch(
            f"/api/projects/{project_id}/expert_answers/{expert_answer_id}/publish",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertAnswerPublishResponse,
        )

    async def unpause(
        self,
        expert_answer_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertAnswerUnpauseResponse:
        """
        Unpause Expert Answer Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_answer_id:
            raise ValueError(f"Expected a non-empty value for `expert_answer_id` but received {expert_answer_id!r}")
        return await self._patch(
            f"/api/projects/{project_id}/expert_answers/{expert_answer_id}/unpause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertAnswerUnpauseResponse,
        )


class ExpertAnswersResourceWithRawResponse:
    def __init__(self, expert_answers: ExpertAnswersResource) -> None:
        self._expert_answers = expert_answers

        self.create = to_raw_response_wrapper(
            expert_answers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            expert_answers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            expert_answers.list,
        )
        self.delete = to_raw_response_wrapper(
            expert_answers.delete,
        )
        self.edit_answer = to_raw_response_wrapper(
            expert_answers.edit_answer,
        )
        self.edit_draft_answer = to_raw_response_wrapper(
            expert_answers.edit_draft_answer,
        )
        self.pause = to_raw_response_wrapper(
            expert_answers.pause,
        )
        self.publish = to_raw_response_wrapper(
            expert_answers.publish,
        )
        self.unpause = to_raw_response_wrapper(
            expert_answers.unpause,
        )


class AsyncExpertAnswersResourceWithRawResponse:
    def __init__(self, expert_answers: AsyncExpertAnswersResource) -> None:
        self._expert_answers = expert_answers

        self.create = async_to_raw_response_wrapper(
            expert_answers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            expert_answers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            expert_answers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            expert_answers.delete,
        )
        self.edit_answer = async_to_raw_response_wrapper(
            expert_answers.edit_answer,
        )
        self.edit_draft_answer = async_to_raw_response_wrapper(
            expert_answers.edit_draft_answer,
        )
        self.pause = async_to_raw_response_wrapper(
            expert_answers.pause,
        )
        self.publish = async_to_raw_response_wrapper(
            expert_answers.publish,
        )
        self.unpause = async_to_raw_response_wrapper(
            expert_answers.unpause,
        )


class ExpertAnswersResourceWithStreamingResponse:
    def __init__(self, expert_answers: ExpertAnswersResource) -> None:
        self._expert_answers = expert_answers

        self.create = to_streamed_response_wrapper(
            expert_answers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            expert_answers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            expert_answers.list,
        )
        self.delete = to_streamed_response_wrapper(
            expert_answers.delete,
        )
        self.edit_answer = to_streamed_response_wrapper(
            expert_answers.edit_answer,
        )
        self.edit_draft_answer = to_streamed_response_wrapper(
            expert_answers.edit_draft_answer,
        )
        self.pause = to_streamed_response_wrapper(
            expert_answers.pause,
        )
        self.publish = to_streamed_response_wrapper(
            expert_answers.publish,
        )
        self.unpause = to_streamed_response_wrapper(
            expert_answers.unpause,
        )


class AsyncExpertAnswersResourceWithStreamingResponse:
    def __init__(self, expert_answers: AsyncExpertAnswersResource) -> None:
        self._expert_answers = expert_answers

        self.create = async_to_streamed_response_wrapper(
            expert_answers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            expert_answers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            expert_answers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            expert_answers.delete,
        )
        self.edit_answer = async_to_streamed_response_wrapper(
            expert_answers.edit_answer,
        )
        self.edit_draft_answer = async_to_streamed_response_wrapper(
            expert_answers.edit_draft_answer,
        )
        self.pause = async_to_streamed_response_wrapper(
            expert_answers.pause,
        )
        self.publish = async_to_streamed_response_wrapper(
            expert_answers.publish,
        )
        self.unpause = async_to_streamed_response_wrapper(
            expert_answers.unpause,
        )
