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
from ....pagination import SyncOffsetPageExpertReviews, AsyncOffsetPageExpertReviews
from ...._base_client import AsyncPaginator, make_request_options
from ....types.projects.remediations import (
    expert_review_edit_params,
    expert_review_list_params,
    expert_review_create_params,
    expert_review_delete_params,
)
from ....types.projects.remediations.expert_review_edit_response import ExpertReviewEditResponse
from ....types.projects.remediations.expert_review_list_response import ExpertReviewListResponse
from ....types.projects.remediations.expert_review_create_response import ExpertReviewCreateResponse
from ....types.projects.remediations.expert_review_retrieve_response import ExpertReviewRetrieveResponse

__all__ = ["ExpertReviewsResource", "AsyncExpertReviewsResource"]


class ExpertReviewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExpertReviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return ExpertReviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExpertReviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return ExpertReviewsResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: str,
        *,
        original_query_log_id: str,
        review_status: Literal["good", "bad"],
        generate_guidance: bool | Omit = omit,
        explanation: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertReviewCreateResponse:
        """
        Create Expert Review Route

        Args:
          original_query_log_id: ID of the original query log

          review_status: Expert review status - 'good' or 'bad'

          explanation: Optional explanation for expert review

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/api/projects/{project_id}/expert_reviews/",
            body=maybe_transform(
                {
                    "original_query_log_id": original_query_log_id,
                    "review_status": review_status,
                    "explanation": explanation,
                },
                expert_review_create_params.ExpertReviewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"generate_guidance": generate_guidance}, expert_review_create_params.ExpertReviewCreateParams
                ),
            ),
            cast_to=ExpertReviewCreateResponse,
        )

    def retrieve(
        self,
        expert_review_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertReviewRetrieveResponse:
        """
        Get Expert Review Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_review_id:
            raise ValueError(f"Expected a non-empty value for `expert_review_id` but received {expert_review_id!r}")
        return self._get(
            f"/api/projects/{project_id}/expert_reviews/{expert_review_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertReviewRetrieveResponse,
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
        review_status: Optional[List[Literal["good", "bad"]]] | Omit = omit,
        sort: Optional[Literal["created_at", "last_edited_at", "resolved_logs_count"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPageExpertReviews[ExpertReviewListResponse]:
        """
        List Expert Reviews Route

        Args:
          created_at_end: Filter expert reviews created at or before this timestamp

          created_at_start: Filter expert reviews created at or after this timestamp

          last_edited_at_end: Filter expert reviews last edited at or before this timestamp

          last_edited_at_start: Filter expert reviews last edited at or after this timestamp

          last_edited_by: Filter expert reviews last edited by user ID

          order: Sort order

          review_status: Filter expert reviews by review status

          sort: Sort expert reviews by field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get_api_list(
            f"/api/projects/{project_id}/expert_reviews/",
            page=SyncOffsetPageExpertReviews[ExpertReviewListResponse],
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
                        "review_status": review_status,
                        "sort": sort,
                    },
                    expert_review_list_params.ExpertReviewListParams,
                ),
            ),
            model=ExpertReviewListResponse,
        )

    def delete(
        self,
        expert_review_id: str,
        *,
        project_id: str,
        original_query_log_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Expert Review Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_review_id:
            raise ValueError(f"Expected a non-empty value for `expert_review_id` but received {expert_review_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/projects/{project_id}/expert_reviews/{expert_review_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"original_query_log_id": original_query_log_id},
                    expert_review_delete_params.ExpertReviewDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def edit(
        self,
        expert_review_id: str,
        *,
        project_id: str,
        explanation: Optional[str] | Omit = omit,
        review_status: Optional[Literal["good", "bad"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertReviewEditResponse:
        """
        Update Expert Review Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_review_id:
            raise ValueError(f"Expected a non-empty value for `expert_review_id` but received {expert_review_id!r}")
        return self._patch(
            f"/api/projects/{project_id}/expert_reviews/{expert_review_id}",
            body=maybe_transform(
                {
                    "explanation": explanation,
                    "review_status": review_status,
                },
                expert_review_edit_params.ExpertReviewEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertReviewEditResponse,
        )


class AsyncExpertReviewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExpertReviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExpertReviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExpertReviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncExpertReviewsResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: str,
        *,
        original_query_log_id: str,
        review_status: Literal["good", "bad"],
        generate_guidance: bool | Omit = omit,
        explanation: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertReviewCreateResponse:
        """
        Create Expert Review Route

        Args:
          original_query_log_id: ID of the original query log

          review_status: Expert review status - 'good' or 'bad'

          explanation: Optional explanation for expert review

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/api/projects/{project_id}/expert_reviews/",
            body=await async_maybe_transform(
                {
                    "original_query_log_id": original_query_log_id,
                    "review_status": review_status,
                    "explanation": explanation,
                },
                expert_review_create_params.ExpertReviewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"generate_guidance": generate_guidance}, expert_review_create_params.ExpertReviewCreateParams
                ),
            ),
            cast_to=ExpertReviewCreateResponse,
        )

    async def retrieve(
        self,
        expert_review_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertReviewRetrieveResponse:
        """
        Get Expert Review Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_review_id:
            raise ValueError(f"Expected a non-empty value for `expert_review_id` but received {expert_review_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/expert_reviews/{expert_review_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertReviewRetrieveResponse,
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
        review_status: Optional[List[Literal["good", "bad"]]] | Omit = omit,
        sort: Optional[Literal["created_at", "last_edited_at", "resolved_logs_count"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ExpertReviewListResponse, AsyncOffsetPageExpertReviews[ExpertReviewListResponse]]:
        """
        List Expert Reviews Route

        Args:
          created_at_end: Filter expert reviews created at or before this timestamp

          created_at_start: Filter expert reviews created at or after this timestamp

          last_edited_at_end: Filter expert reviews last edited at or before this timestamp

          last_edited_at_start: Filter expert reviews last edited at or after this timestamp

          last_edited_by: Filter expert reviews last edited by user ID

          order: Sort order

          review_status: Filter expert reviews by review status

          sort: Sort expert reviews by field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get_api_list(
            f"/api/projects/{project_id}/expert_reviews/",
            page=AsyncOffsetPageExpertReviews[ExpertReviewListResponse],
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
                        "review_status": review_status,
                        "sort": sort,
                    },
                    expert_review_list_params.ExpertReviewListParams,
                ),
            ),
            model=ExpertReviewListResponse,
        )

    async def delete(
        self,
        expert_review_id: str,
        *,
        project_id: str,
        original_query_log_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Expert Review Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_review_id:
            raise ValueError(f"Expected a non-empty value for `expert_review_id` but received {expert_review_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/projects/{project_id}/expert_reviews/{expert_review_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"original_query_log_id": original_query_log_id},
                    expert_review_delete_params.ExpertReviewDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def edit(
        self,
        expert_review_id: str,
        *,
        project_id: str,
        explanation: Optional[str] | Omit = omit,
        review_status: Optional[Literal["good", "bad"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpertReviewEditResponse:
        """
        Update Expert Review Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not expert_review_id:
            raise ValueError(f"Expected a non-empty value for `expert_review_id` but received {expert_review_id!r}")
        return await self._patch(
            f"/api/projects/{project_id}/expert_reviews/{expert_review_id}",
            body=await async_maybe_transform(
                {
                    "explanation": explanation,
                    "review_status": review_status,
                },
                expert_review_edit_params.ExpertReviewEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpertReviewEditResponse,
        )


class ExpertReviewsResourceWithRawResponse:
    def __init__(self, expert_reviews: ExpertReviewsResource) -> None:
        self._expert_reviews = expert_reviews

        self.create = to_raw_response_wrapper(
            expert_reviews.create,
        )
        self.retrieve = to_raw_response_wrapper(
            expert_reviews.retrieve,
        )
        self.list = to_raw_response_wrapper(
            expert_reviews.list,
        )
        self.delete = to_raw_response_wrapper(
            expert_reviews.delete,
        )
        self.edit = to_raw_response_wrapper(
            expert_reviews.edit,
        )


class AsyncExpertReviewsResourceWithRawResponse:
    def __init__(self, expert_reviews: AsyncExpertReviewsResource) -> None:
        self._expert_reviews = expert_reviews

        self.create = async_to_raw_response_wrapper(
            expert_reviews.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            expert_reviews.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            expert_reviews.list,
        )
        self.delete = async_to_raw_response_wrapper(
            expert_reviews.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            expert_reviews.edit,
        )


class ExpertReviewsResourceWithStreamingResponse:
    def __init__(self, expert_reviews: ExpertReviewsResource) -> None:
        self._expert_reviews = expert_reviews

        self.create = to_streamed_response_wrapper(
            expert_reviews.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            expert_reviews.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            expert_reviews.list,
        )
        self.delete = to_streamed_response_wrapper(
            expert_reviews.delete,
        )
        self.edit = to_streamed_response_wrapper(
            expert_reviews.edit,
        )


class AsyncExpertReviewsResourceWithStreamingResponse:
    def __init__(self, expert_reviews: AsyncExpertReviewsResource) -> None:
        self._expert_reviews = expert_reviews

        self.create = async_to_streamed_response_wrapper(
            expert_reviews.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            expert_reviews.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            expert_reviews.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            expert_reviews.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            expert_reviews.edit,
        )
