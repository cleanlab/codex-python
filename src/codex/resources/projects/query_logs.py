# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.projects import query_log_list_params, query_log_list_groups_params, query_log_list_by_group_params
from ...types.projects.query_log_list_response import QueryLogListResponse
from ...types.projects.query_log_retrieve_response import QueryLogRetrieveResponse
from ...types.projects.query_log_list_groups_response import QueryLogListGroupsResponse
from ...types.projects.query_log_list_by_group_response import QueryLogListByGroupResponse
from ...types.projects.query_log_start_remediation_response import QueryLogStartRemediationResponse

__all__ = ["QueryLogsResource", "AsyncQueryLogsResource"]


class QueryLogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueryLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return QueryLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueryLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return QueryLogsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        query_log_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryLogRetrieveResponse:
        """
        Get Query Log Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not query_log_id:
            raise ValueError(f"Expected a non-empty value for `query_log_id` but received {query_log_id!r}")
        return self._get(
            f"/api/projects/{project_id}/query_logs/{query_log_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryLogRetrieveResponse,
        )

    def list(
        self,
        project_id: str,
        *,
        created_at_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        custom_metadata: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        primary_eval_issue: Optional[
            List[Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "unsupported"]]
        ]
        | NotGiven = NOT_GIVEN,
        sort: Optional[Literal["created_at", "primary_eval_issue_score"]] | NotGiven = NOT_GIVEN,
        was_cache_hit: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryLogListResponse:
        """
        List query logs by project ID.

        Args:
          created_at_end: Filter logs created at or before this timestamp

          created_at_start: Filter logs created at or after this timestamp

          custom_metadata: Filter by custom metadata as JSON string: {"key1": "value1", "key2": "value2"}

          primary_eval_issue: Filter logs that have ANY of these primary evaluation issues (OR operation)

          was_cache_hit: Filter by cache hit status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/api/projects/{project_id}/query_logs/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_end": created_at_end,
                        "created_at_start": created_at_start,
                        "custom_metadata": custom_metadata,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "primary_eval_issue": primary_eval_issue,
                        "sort": sort,
                        "was_cache_hit": was_cache_hit,
                    },
                    query_log_list_params.QueryLogListParams,
                ),
            ),
            cast_to=QueryLogListResponse,
        )

    def list_by_group(
        self,
        project_id: str,
        *,
        created_at_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        custom_metadata: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        primary_eval_issue: Optional[
            List[Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "unsupported"]]
        ]
        | NotGiven = NOT_GIVEN,
        remediation_ids: List[str] | NotGiven = NOT_GIVEN,
        sort: Optional[Literal["created_at", "primary_eval_issue_score"]] | NotGiven = NOT_GIVEN,
        was_cache_hit: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryLogListByGroupResponse:
        """
        List query log group by remediation ID.

        Args:
          created_at_end: Filter logs created at or before this timestamp

          created_at_start: Filter logs created at or after this timestamp

          custom_metadata: Filter by custom metadata as JSON string: {"key1": "value1", "key2": "value2"}

          primary_eval_issue: Filter logs that have ANY of these primary evaluation issues (OR operation)

          remediation_ids: List of groups to list child logs for

          was_cache_hit: Filter by cache hit status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/api/projects/{project_id}/query_logs/logs_by_group",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_end": created_at_end,
                        "created_at_start": created_at_start,
                        "custom_metadata": custom_metadata,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "primary_eval_issue": primary_eval_issue,
                        "remediation_ids": remediation_ids,
                        "sort": sort,
                        "was_cache_hit": was_cache_hit,
                    },
                    query_log_list_by_group_params.QueryLogListByGroupParams,
                ),
            ),
            cast_to=QueryLogListByGroupResponse,
        )

    def list_groups(
        self,
        project_id: str,
        *,
        created_at_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        custom_metadata: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        primary_eval_issue: Optional[
            List[Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "unsupported"]]
        ]
        | NotGiven = NOT_GIVEN,
        sort: Optional[Literal["created_at", "primary_eval_issue_score", "total_count", "custom_rank"]]
        | NotGiven = NOT_GIVEN,
        was_cache_hit: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryLogListGroupsResponse:
        """
        List query log groups by project ID.

        Args:
          created_at_end: Filter logs created at or before this timestamp

          created_at_start: Filter logs created at or after this timestamp

          custom_metadata: Filter by custom metadata as JSON string: {"key1": "value1", "key2": "value2"}

          primary_eval_issue: Filter logs that have ANY of these primary evaluation issues (OR operation)

          was_cache_hit: Filter by cache hit status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/api/projects/{project_id}/query_logs/groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_end": created_at_end,
                        "created_at_start": created_at_start,
                        "custom_metadata": custom_metadata,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "primary_eval_issue": primary_eval_issue,
                        "sort": sort,
                        "was_cache_hit": was_cache_hit,
                    },
                    query_log_list_groups_params.QueryLogListGroupsParams,
                ),
            ),
            cast_to=QueryLogListGroupsResponse,
        )

    def start_remediation(
        self,
        query_log_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryLogStartRemediationResponse:
        """
        Start Remediation Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not query_log_id:
            raise ValueError(f"Expected a non-empty value for `query_log_id` but received {query_log_id!r}")
        return self._post(
            f"/api/projects/{project_id}/query_logs/{query_log_id}/start_remediation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryLogStartRemediationResponse,
        )


class AsyncQueryLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueryLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueryLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueryLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncQueryLogsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        query_log_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryLogRetrieveResponse:
        """
        Get Query Log Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not query_log_id:
            raise ValueError(f"Expected a non-empty value for `query_log_id` but received {query_log_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/query_logs/{query_log_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryLogRetrieveResponse,
        )

    async def list(
        self,
        project_id: str,
        *,
        created_at_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        custom_metadata: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        primary_eval_issue: Optional[
            List[Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "unsupported"]]
        ]
        | NotGiven = NOT_GIVEN,
        sort: Optional[Literal["created_at", "primary_eval_issue_score"]] | NotGiven = NOT_GIVEN,
        was_cache_hit: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryLogListResponse:
        """
        List query logs by project ID.

        Args:
          created_at_end: Filter logs created at or before this timestamp

          created_at_start: Filter logs created at or after this timestamp

          custom_metadata: Filter by custom metadata as JSON string: {"key1": "value1", "key2": "value2"}

          primary_eval_issue: Filter logs that have ANY of these primary evaluation issues (OR operation)

          was_cache_hit: Filter by cache hit status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/query_logs/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "created_at_end": created_at_end,
                        "created_at_start": created_at_start,
                        "custom_metadata": custom_metadata,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "primary_eval_issue": primary_eval_issue,
                        "sort": sort,
                        "was_cache_hit": was_cache_hit,
                    },
                    query_log_list_params.QueryLogListParams,
                ),
            ),
            cast_to=QueryLogListResponse,
        )

    async def list_by_group(
        self,
        project_id: str,
        *,
        created_at_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        custom_metadata: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        primary_eval_issue: Optional[
            List[Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "unsupported"]]
        ]
        | NotGiven = NOT_GIVEN,
        remediation_ids: List[str] | NotGiven = NOT_GIVEN,
        sort: Optional[Literal["created_at", "primary_eval_issue_score"]] | NotGiven = NOT_GIVEN,
        was_cache_hit: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryLogListByGroupResponse:
        """
        List query log group by remediation ID.

        Args:
          created_at_end: Filter logs created at or before this timestamp

          created_at_start: Filter logs created at or after this timestamp

          custom_metadata: Filter by custom metadata as JSON string: {"key1": "value1", "key2": "value2"}

          primary_eval_issue: Filter logs that have ANY of these primary evaluation issues (OR operation)

          remediation_ids: List of groups to list child logs for

          was_cache_hit: Filter by cache hit status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/query_logs/logs_by_group",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "created_at_end": created_at_end,
                        "created_at_start": created_at_start,
                        "custom_metadata": custom_metadata,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "primary_eval_issue": primary_eval_issue,
                        "remediation_ids": remediation_ids,
                        "sort": sort,
                        "was_cache_hit": was_cache_hit,
                    },
                    query_log_list_by_group_params.QueryLogListByGroupParams,
                ),
            ),
            cast_to=QueryLogListByGroupResponse,
        )

    async def list_groups(
        self,
        project_id: str,
        *,
        created_at_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        custom_metadata: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        primary_eval_issue: Optional[
            List[Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "unsupported"]]
        ]
        | NotGiven = NOT_GIVEN,
        sort: Optional[Literal["created_at", "primary_eval_issue_score", "total_count", "custom_rank"]]
        | NotGiven = NOT_GIVEN,
        was_cache_hit: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryLogListGroupsResponse:
        """
        List query log groups by project ID.

        Args:
          created_at_end: Filter logs created at or before this timestamp

          created_at_start: Filter logs created at or after this timestamp

          custom_metadata: Filter by custom metadata as JSON string: {"key1": "value1", "key2": "value2"}

          primary_eval_issue: Filter logs that have ANY of these primary evaluation issues (OR operation)

          was_cache_hit: Filter by cache hit status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/query_logs/groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "created_at_end": created_at_end,
                        "created_at_start": created_at_start,
                        "custom_metadata": custom_metadata,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "primary_eval_issue": primary_eval_issue,
                        "sort": sort,
                        "was_cache_hit": was_cache_hit,
                    },
                    query_log_list_groups_params.QueryLogListGroupsParams,
                ),
            ),
            cast_to=QueryLogListGroupsResponse,
        )

    async def start_remediation(
        self,
        query_log_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryLogStartRemediationResponse:
        """
        Start Remediation Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not query_log_id:
            raise ValueError(f"Expected a non-empty value for `query_log_id` but received {query_log_id!r}")
        return await self._post(
            f"/api/projects/{project_id}/query_logs/{query_log_id}/start_remediation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryLogStartRemediationResponse,
        )


class QueryLogsResourceWithRawResponse:
    def __init__(self, query_logs: QueryLogsResource) -> None:
        self._query_logs = query_logs

        self.retrieve = to_raw_response_wrapper(
            query_logs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            query_logs.list,
        )
        self.list_by_group = to_raw_response_wrapper(
            query_logs.list_by_group,
        )
        self.list_groups = to_raw_response_wrapper(
            query_logs.list_groups,
        )
        self.start_remediation = to_raw_response_wrapper(
            query_logs.start_remediation,
        )


class AsyncQueryLogsResourceWithRawResponse:
    def __init__(self, query_logs: AsyncQueryLogsResource) -> None:
        self._query_logs = query_logs

        self.retrieve = async_to_raw_response_wrapper(
            query_logs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            query_logs.list,
        )
        self.list_by_group = async_to_raw_response_wrapper(
            query_logs.list_by_group,
        )
        self.list_groups = async_to_raw_response_wrapper(
            query_logs.list_groups,
        )
        self.start_remediation = async_to_raw_response_wrapper(
            query_logs.start_remediation,
        )


class QueryLogsResourceWithStreamingResponse:
    def __init__(self, query_logs: QueryLogsResource) -> None:
        self._query_logs = query_logs

        self.retrieve = to_streamed_response_wrapper(
            query_logs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            query_logs.list,
        )
        self.list_by_group = to_streamed_response_wrapper(
            query_logs.list_by_group,
        )
        self.list_groups = to_streamed_response_wrapper(
            query_logs.list_groups,
        )
        self.start_remediation = to_streamed_response_wrapper(
            query_logs.start_remediation,
        )


class AsyncQueryLogsResourceWithStreamingResponse:
    def __init__(self, query_logs: AsyncQueryLogsResource) -> None:
        self._query_logs = query_logs

        self.retrieve = async_to_streamed_response_wrapper(
            query_logs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            query_logs.list,
        )
        self.list_by_group = async_to_streamed_response_wrapper(
            query_logs.list_by_group,
        )
        self.list_groups = async_to_streamed_response_wrapper(
            query_logs.list_groups,
        )
        self.start_remediation = async_to_streamed_response_wrapper(
            query_logs.start_remediation,
        )
