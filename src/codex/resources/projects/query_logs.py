# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import (
    SyncOffsetPageQueryLogs,
    AsyncOffsetPageQueryLogs,
    SyncOffsetPageQueryLogGroups,
    AsyncOffsetPageQueryLogGroups,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.projects import (
    query_log_list_params,
    query_log_list_groups_params,
    query_log_list_by_group_params,
    query_log_update_metadata_params,
    query_log_add_user_feedback_params,
)
from ...types.projects.query_log_list_response import QueryLogListResponse
from ...types.projects.query_log_retrieve_response import QueryLogRetrieveResponse
from ...types.projects.query_log_list_groups_response import QueryLogListGroupsResponse
from ...types.projects.query_log_list_by_group_response import QueryLogListByGroupResponse
from ...types.projects.query_log_update_metadata_response import QueryLogUpdateMetadataResponse
from ...types.projects.query_log_add_user_feedback_response import QueryLogAddUserFeedbackResponse
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        created_at_end: Union[str, datetime, None] | Omit = omit,
        created_at_start: Union[str, datetime, None] | Omit = omit,
        custom_metadata: Optional[str] | Omit = omit,
        expert_review_status: Optional[Literal["good", "bad"]] | Omit = omit,
        failed_evals: Optional[SequenceNotStr[str]] | Omit = omit,
        guardrailed: Optional[bool] | Omit = omit,
        has_tool_calls: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        passed_evals: Optional[SequenceNotStr[str]] | Omit = omit,
        primary_eval_issue: Optional[
            List[Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "ungrounded"]]
        ]
        | Omit = omit,
        search_text: Optional[str] | Omit = omit,
        sort: Optional[str] | Omit = omit,
        tool_call_names: Optional[SequenceNotStr[str]] | Omit = omit,
        was_cache_hit: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPageQueryLogs[QueryLogListResponse]:
        """
        List query logs by project ID.

        Args:
          created_at_end: Filter logs created at or before this timestamp

          created_at_start: Filter logs created at or after this timestamp

          custom_metadata: Filter by custom metadata as JSON string: {"key1": "value1", "key2": "value2"}

          expert_review_status: Filter by expert review status

          failed_evals: Filter by evals that failed

          guardrailed: Filter by guardrailed status

          has_tool_calls: Filter by whether the query log has tool calls

          passed_evals: Filter by evals that passed

          primary_eval_issue: Filter logs that have ANY of these primary evaluation issues (OR operation)

          search_text: Case-insensitive search across evaluated_response and question fields
              (original_question if available, otherwise question)

          sort: Field or score to sort by.

              Available fields: 'created_at', 'primary_eval_issue_score'.

              For eval scores, use '.eval.' prefix followed by the eval name.

              Default eval scores: '.eval.trustworthiness', '.eval.context_sufficiency',
              '.eval.response_helpfulness', '.eval.query_ease', '.eval.response_groundedness'.

              Custom eval scores: '.eval.custom_eval_1', '.eval.custom_eval_2', etc.

          tool_call_names: Filter by names of tools called in the assistant response

          was_cache_hit: Filter by cache hit status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get_api_list(
            f"/api/projects/{project_id}/query_logs/",
            page=SyncOffsetPageQueryLogs[QueryLogListResponse],
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
                        "expert_review_status": expert_review_status,
                        "failed_evals": failed_evals,
                        "guardrailed": guardrailed,
                        "has_tool_calls": has_tool_calls,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "passed_evals": passed_evals,
                        "primary_eval_issue": primary_eval_issue,
                        "search_text": search_text,
                        "sort": sort,
                        "tool_call_names": tool_call_names,
                        "was_cache_hit": was_cache_hit,
                    },
                    query_log_list_params.QueryLogListParams,
                ),
            ),
            model=QueryLogListResponse,
        )

    def add_user_feedback(
        self,
        query_log_id: str,
        *,
        project_id: str,
        key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryLogAddUserFeedbackResponse:
        """
        Add User Feedback Route

        Args:
          key: A key describing the criteria of the feedback, eg 'rating'

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
            f"/api/projects/{project_id}/query_logs/{query_log_id}/user_feedback",
            body=maybe_transform({"key": key}, query_log_add_user_feedback_params.QueryLogAddUserFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryLogAddUserFeedbackResponse,
        )

    def list_by_group(
        self,
        project_id: str,
        *,
        created_at_end: Union[str, datetime, None] | Omit = omit,
        created_at_start: Union[str, datetime, None] | Omit = omit,
        custom_metadata: Optional[str] | Omit = omit,
        expert_review_status: Optional[Literal["good", "bad"]] | Omit = omit,
        failed_evals: Optional[SequenceNotStr[str]] | Omit = omit,
        guardrailed: Optional[bool] | Omit = omit,
        has_tool_calls: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        needs_review: Optional[bool] | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        passed_evals: Optional[SequenceNotStr[str]] | Omit = omit,
        primary_eval_issue: Optional[
            List[Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "ungrounded"]]
        ]
        | Omit = omit,
        remediation_ids: SequenceNotStr[str] | Omit = omit,
        search_text: Optional[str] | Omit = omit,
        sort: Optional[str] | Omit = omit,
        tool_call_names: Optional[SequenceNotStr[str]] | Omit = omit,
        was_cache_hit: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryLogListByGroupResponse:
        """
        List query log group by remediation ID.

        Args:
          created_at_end: Filter logs created at or before this timestamp

          created_at_start: Filter logs created at or after this timestamp

          custom_metadata: Filter by custom metadata as JSON string: {"key1": "value1", "key2": "value2"}

          expert_review_status: Filter by expert review status

          failed_evals: Filter by evals that failed

          guardrailed: Filter by guardrailed status

          has_tool_calls: Filter by whether the query log has tool calls

          needs_review: Filter logs that need review

          passed_evals: Filter by evals that passed

          primary_eval_issue: Filter logs that have ANY of these primary evaluation issues (OR operation)

          remediation_ids: List of groups to list child logs for

          search_text: Case-insensitive search across evaluated_response and question fields
              (original_question if available, otherwise question)

          sort: Field or score to sort by.

              Available fields: 'created_at', 'primary_eval_issue_score'.

              For eval scores, use '.eval.' prefix followed by the eval name.

              Default eval scores: '.eval.trustworthiness', '.eval.context_sufficiency',
              '.eval.response_helpfulness', '.eval.query_ease', '.eval.response_groundedness'.

              Custom eval scores: '.eval.custom_eval_1', '.eval.custom_eval_2', etc.

          tool_call_names: Filter by names of tools called in the assistant response

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
                        "expert_review_status": expert_review_status,
                        "failed_evals": failed_evals,
                        "guardrailed": guardrailed,
                        "has_tool_calls": has_tool_calls,
                        "limit": limit,
                        "needs_review": needs_review,
                        "offset": offset,
                        "order": order,
                        "passed_evals": passed_evals,
                        "primary_eval_issue": primary_eval_issue,
                        "remediation_ids": remediation_ids,
                        "search_text": search_text,
                        "sort": sort,
                        "tool_call_names": tool_call_names,
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
        created_at_end: Union[str, datetime, None] | Omit = omit,
        created_at_start: Union[str, datetime, None] | Omit = omit,
        custom_metadata: Optional[str] | Omit = omit,
        expert_review_status: Optional[Literal["good", "bad"]] | Omit = omit,
        failed_evals: Optional[SequenceNotStr[str]] | Omit = omit,
        guardrailed: Optional[bool] | Omit = omit,
        has_tool_calls: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        needs_review: Optional[bool] | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        passed_evals: Optional[SequenceNotStr[str]] | Omit = omit,
        primary_eval_issue: Optional[
            List[Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "ungrounded"]]
        ]
        | Omit = omit,
        search_text: Optional[str] | Omit = omit,
        sort: Optional[str] | Omit = omit,
        tool_call_names: Optional[SequenceNotStr[str]] | Omit = omit,
        was_cache_hit: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPageQueryLogGroups[QueryLogListGroupsResponse]:
        """
        List query log groups by project ID.

        Args:
          created_at_end: Filter logs created at or before this timestamp

          created_at_start: Filter logs created at or after this timestamp

          custom_metadata: Filter by custom metadata as JSON string: {"key1": "value1", "key2": "value2"}

          expert_review_status: Filter by expert review status

          failed_evals: Filter by evals that failed

          guardrailed: Filter by guardrailed status

          has_tool_calls: Filter by whether the query log has tool calls

          needs_review: Filter log groups that need review

          passed_evals: Filter by evals that passed

          primary_eval_issue: Filter logs that have ANY of these primary evaluation issues (OR operation)

          search_text: Case-insensitive search across evaluated_response and question fields
              (original_question if available, otherwise question)

          sort: Field or score to sort by.

              Available fields: 'created_at', 'custom_rank', 'impact_score',
              'primary_eval_issue_score', 'total_count'.

              For eval scores, use '.eval.' prefix followed by the eval name.

              Default eval scores: '.eval.trustworthiness', '.eval.context_sufficiency',
              '.eval.response_helpfulness', '.eval.query_ease', '.eval.response_groundedness'.

              Custom eval scores: '.eval.custom_eval_1', '.eval.custom_eval_2', etc.

          tool_call_names: Filter by names of tools called in the assistant response

          was_cache_hit: Filter by cache hit status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get_api_list(
            f"/api/projects/{project_id}/query_logs/groups",
            page=SyncOffsetPageQueryLogGroups[QueryLogListGroupsResponse],
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
                        "expert_review_status": expert_review_status,
                        "failed_evals": failed_evals,
                        "guardrailed": guardrailed,
                        "has_tool_calls": has_tool_calls,
                        "limit": limit,
                        "needs_review": needs_review,
                        "offset": offset,
                        "order": order,
                        "passed_evals": passed_evals,
                        "primary_eval_issue": primary_eval_issue,
                        "search_text": search_text,
                        "sort": sort,
                        "tool_call_names": tool_call_names,
                        "was_cache_hit": was_cache_hit,
                    },
                    query_log_list_groups_params.QueryLogListGroupsParams,
                ),
            ),
            model=QueryLogListGroupsResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def update_metadata(
        self,
        query_log_id: str,
        *,
        project_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryLogUpdateMetadataResponse:
        """
        Update Metadata Route

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
        return self._put(
            f"/api/projects/{project_id}/query_logs/{query_log_id}/metadata",
            body=maybe_transform(body, query_log_update_metadata_params.QueryLogUpdateMetadataParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryLogUpdateMetadataResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def list(
        self,
        project_id: str,
        *,
        created_at_end: Union[str, datetime, None] | Omit = omit,
        created_at_start: Union[str, datetime, None] | Omit = omit,
        custom_metadata: Optional[str] | Omit = omit,
        expert_review_status: Optional[Literal["good", "bad"]] | Omit = omit,
        failed_evals: Optional[SequenceNotStr[str]] | Omit = omit,
        guardrailed: Optional[bool] | Omit = omit,
        has_tool_calls: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        passed_evals: Optional[SequenceNotStr[str]] | Omit = omit,
        primary_eval_issue: Optional[
            List[Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "ungrounded"]]
        ]
        | Omit = omit,
        search_text: Optional[str] | Omit = omit,
        sort: Optional[str] | Omit = omit,
        tool_call_names: Optional[SequenceNotStr[str]] | Omit = omit,
        was_cache_hit: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[QueryLogListResponse, AsyncOffsetPageQueryLogs[QueryLogListResponse]]:
        """
        List query logs by project ID.

        Args:
          created_at_end: Filter logs created at or before this timestamp

          created_at_start: Filter logs created at or after this timestamp

          custom_metadata: Filter by custom metadata as JSON string: {"key1": "value1", "key2": "value2"}

          expert_review_status: Filter by expert review status

          failed_evals: Filter by evals that failed

          guardrailed: Filter by guardrailed status

          has_tool_calls: Filter by whether the query log has tool calls

          passed_evals: Filter by evals that passed

          primary_eval_issue: Filter logs that have ANY of these primary evaluation issues (OR operation)

          search_text: Case-insensitive search across evaluated_response and question fields
              (original_question if available, otherwise question)

          sort: Field or score to sort by.

              Available fields: 'created_at', 'primary_eval_issue_score'.

              For eval scores, use '.eval.' prefix followed by the eval name.

              Default eval scores: '.eval.trustworthiness', '.eval.context_sufficiency',
              '.eval.response_helpfulness', '.eval.query_ease', '.eval.response_groundedness'.

              Custom eval scores: '.eval.custom_eval_1', '.eval.custom_eval_2', etc.

          tool_call_names: Filter by names of tools called in the assistant response

          was_cache_hit: Filter by cache hit status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get_api_list(
            f"/api/projects/{project_id}/query_logs/",
            page=AsyncOffsetPageQueryLogs[QueryLogListResponse],
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
                        "expert_review_status": expert_review_status,
                        "failed_evals": failed_evals,
                        "guardrailed": guardrailed,
                        "has_tool_calls": has_tool_calls,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "passed_evals": passed_evals,
                        "primary_eval_issue": primary_eval_issue,
                        "search_text": search_text,
                        "sort": sort,
                        "tool_call_names": tool_call_names,
                        "was_cache_hit": was_cache_hit,
                    },
                    query_log_list_params.QueryLogListParams,
                ),
            ),
            model=QueryLogListResponse,
        )

    async def add_user_feedback(
        self,
        query_log_id: str,
        *,
        project_id: str,
        key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryLogAddUserFeedbackResponse:
        """
        Add User Feedback Route

        Args:
          key: A key describing the criteria of the feedback, eg 'rating'

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
            f"/api/projects/{project_id}/query_logs/{query_log_id}/user_feedback",
            body=await async_maybe_transform(
                {"key": key}, query_log_add_user_feedback_params.QueryLogAddUserFeedbackParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryLogAddUserFeedbackResponse,
        )

    async def list_by_group(
        self,
        project_id: str,
        *,
        created_at_end: Union[str, datetime, None] | Omit = omit,
        created_at_start: Union[str, datetime, None] | Omit = omit,
        custom_metadata: Optional[str] | Omit = omit,
        expert_review_status: Optional[Literal["good", "bad"]] | Omit = omit,
        failed_evals: Optional[SequenceNotStr[str]] | Omit = omit,
        guardrailed: Optional[bool] | Omit = omit,
        has_tool_calls: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        needs_review: Optional[bool] | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        passed_evals: Optional[SequenceNotStr[str]] | Omit = omit,
        primary_eval_issue: Optional[
            List[Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "ungrounded"]]
        ]
        | Omit = omit,
        remediation_ids: SequenceNotStr[str] | Omit = omit,
        search_text: Optional[str] | Omit = omit,
        sort: Optional[str] | Omit = omit,
        tool_call_names: Optional[SequenceNotStr[str]] | Omit = omit,
        was_cache_hit: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryLogListByGroupResponse:
        """
        List query log group by remediation ID.

        Args:
          created_at_end: Filter logs created at or before this timestamp

          created_at_start: Filter logs created at or after this timestamp

          custom_metadata: Filter by custom metadata as JSON string: {"key1": "value1", "key2": "value2"}

          expert_review_status: Filter by expert review status

          failed_evals: Filter by evals that failed

          guardrailed: Filter by guardrailed status

          has_tool_calls: Filter by whether the query log has tool calls

          needs_review: Filter logs that need review

          passed_evals: Filter by evals that passed

          primary_eval_issue: Filter logs that have ANY of these primary evaluation issues (OR operation)

          remediation_ids: List of groups to list child logs for

          search_text: Case-insensitive search across evaluated_response and question fields
              (original_question if available, otherwise question)

          sort: Field or score to sort by.

              Available fields: 'created_at', 'primary_eval_issue_score'.

              For eval scores, use '.eval.' prefix followed by the eval name.

              Default eval scores: '.eval.trustworthiness', '.eval.context_sufficiency',
              '.eval.response_helpfulness', '.eval.query_ease', '.eval.response_groundedness'.

              Custom eval scores: '.eval.custom_eval_1', '.eval.custom_eval_2', etc.

          tool_call_names: Filter by names of tools called in the assistant response

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
                        "expert_review_status": expert_review_status,
                        "failed_evals": failed_evals,
                        "guardrailed": guardrailed,
                        "has_tool_calls": has_tool_calls,
                        "limit": limit,
                        "needs_review": needs_review,
                        "offset": offset,
                        "order": order,
                        "passed_evals": passed_evals,
                        "primary_eval_issue": primary_eval_issue,
                        "remediation_ids": remediation_ids,
                        "search_text": search_text,
                        "sort": sort,
                        "tool_call_names": tool_call_names,
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
        created_at_end: Union[str, datetime, None] | Omit = omit,
        created_at_start: Union[str, datetime, None] | Omit = omit,
        custom_metadata: Optional[str] | Omit = omit,
        expert_review_status: Optional[Literal["good", "bad"]] | Omit = omit,
        failed_evals: Optional[SequenceNotStr[str]] | Omit = omit,
        guardrailed: Optional[bool] | Omit = omit,
        has_tool_calls: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        needs_review: Optional[bool] | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        passed_evals: Optional[SequenceNotStr[str]] | Omit = omit,
        primary_eval_issue: Optional[
            List[Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "ungrounded"]]
        ]
        | Omit = omit,
        search_text: Optional[str] | Omit = omit,
        sort: Optional[str] | Omit = omit,
        tool_call_names: Optional[SequenceNotStr[str]] | Omit = omit,
        was_cache_hit: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[QueryLogListGroupsResponse, AsyncOffsetPageQueryLogGroups[QueryLogListGroupsResponse]]:
        """
        List query log groups by project ID.

        Args:
          created_at_end: Filter logs created at or before this timestamp

          created_at_start: Filter logs created at or after this timestamp

          custom_metadata: Filter by custom metadata as JSON string: {"key1": "value1", "key2": "value2"}

          expert_review_status: Filter by expert review status

          failed_evals: Filter by evals that failed

          guardrailed: Filter by guardrailed status

          has_tool_calls: Filter by whether the query log has tool calls

          needs_review: Filter log groups that need review

          passed_evals: Filter by evals that passed

          primary_eval_issue: Filter logs that have ANY of these primary evaluation issues (OR operation)

          search_text: Case-insensitive search across evaluated_response and question fields
              (original_question if available, otherwise question)

          sort: Field or score to sort by.

              Available fields: 'created_at', 'custom_rank', 'impact_score',
              'primary_eval_issue_score', 'total_count'.

              For eval scores, use '.eval.' prefix followed by the eval name.

              Default eval scores: '.eval.trustworthiness', '.eval.context_sufficiency',
              '.eval.response_helpfulness', '.eval.query_ease', '.eval.response_groundedness'.

              Custom eval scores: '.eval.custom_eval_1', '.eval.custom_eval_2', etc.

          tool_call_names: Filter by names of tools called in the assistant response

          was_cache_hit: Filter by cache hit status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get_api_list(
            f"/api/projects/{project_id}/query_logs/groups",
            page=AsyncOffsetPageQueryLogGroups[QueryLogListGroupsResponse],
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
                        "expert_review_status": expert_review_status,
                        "failed_evals": failed_evals,
                        "guardrailed": guardrailed,
                        "has_tool_calls": has_tool_calls,
                        "limit": limit,
                        "needs_review": needs_review,
                        "offset": offset,
                        "order": order,
                        "passed_evals": passed_evals,
                        "primary_eval_issue": primary_eval_issue,
                        "search_text": search_text,
                        "sort": sort,
                        "tool_call_names": tool_call_names,
                        "was_cache_hit": was_cache_hit,
                    },
                    query_log_list_groups_params.QueryLogListGroupsParams,
                ),
            ),
            model=QueryLogListGroupsResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    async def update_metadata(
        self,
        query_log_id: str,
        *,
        project_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryLogUpdateMetadataResponse:
        """
        Update Metadata Route

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
        return await self._put(
            f"/api/projects/{project_id}/query_logs/{query_log_id}/metadata",
            body=await async_maybe_transform(body, query_log_update_metadata_params.QueryLogUpdateMetadataParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryLogUpdateMetadataResponse,
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
        self.add_user_feedback = to_raw_response_wrapper(
            query_logs.add_user_feedback,
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
        self.update_metadata = to_raw_response_wrapper(
            query_logs.update_metadata,
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
        self.add_user_feedback = async_to_raw_response_wrapper(
            query_logs.add_user_feedback,
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
        self.update_metadata = async_to_raw_response_wrapper(
            query_logs.update_metadata,
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
        self.add_user_feedback = to_streamed_response_wrapper(
            query_logs.add_user_feedback,
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
        self.update_metadata = to_streamed_response_wrapper(
            query_logs.update_metadata,
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
        self.add_user_feedback = async_to_streamed_response_wrapper(
            query_logs.add_user_feedback,
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
        self.update_metadata = async_to_streamed_response_wrapper(
            query_logs.update_metadata,
        )
