# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.projects import eval_list_params, eval_create_params, eval_update_params
from ...types.project_return_schema import ProjectReturnSchema
from ...types.projects.eval_list_response import EvalListResponse

__all__ = ["EvalsResource", "AsyncEvalsResource"]


class EvalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return EvalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return EvalsResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: str,
        *,
        criteria: str,
        eval_key: str,
        name: str,
        context_identifier: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        guardrailed_fallback_message: Optional[str] | Omit = omit,
        is_default: bool | Omit = omit,
        priority: Optional[int] | Omit = omit,
        query_identifier: Optional[str] | Omit = omit,
        response_identifier: Optional[str] | Omit = omit,
        should_escalate: bool | Omit = omit,
        should_guardrail: bool | Omit = omit,
        threshold: float | Omit = omit,
        threshold_direction: Literal["above", "below"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectReturnSchema:
        """
        Create a new custom eval for a project.

        Args:
          criteria: The evaluation criteria text that describes what aspect is being evaluated and
              how

          eval_key: Unique key for eval metric - currently maps to the TrustworthyRAG name property
              and eval_scores dictionary key to check against threshold

          name: Display name/label for the evaluation metric

          context_identifier: The exact string used in your evaluation criteria to reference the retrieved
              context.

          enabled: Allows the evaluation to be disabled without removing it

          guardrailed_fallback_message: Fallback message to use if this eval fails and causes the response to be
              guardrailed

          is_default: Whether the eval is a default, built-in eval or a custom eval

          priority: Priority order for evals (lower number = higher priority) to determine primary
              eval issue to surface

          query_identifier: The exact string used in your evaluation criteria to reference the user's query.

          response_identifier: The exact string used in your evaluation criteria to reference the RAG/LLM
              response.

          should_escalate: If true, failing this eval means the question should be escalated to Codex for
              an SME to review

          should_guardrail: If true, failing this eval means the response should be guardrailed

          threshold: Threshold value that determines if the evaluation fails

          threshold_direction: Whether the evaluation fails when score is above or below the threshold

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/api/projects/{project_id}/evals",
            body=maybe_transform(
                {
                    "criteria": criteria,
                    "eval_key": eval_key,
                    "name": name,
                    "context_identifier": context_identifier,
                    "enabled": enabled,
                    "guardrailed_fallback_message": guardrailed_fallback_message,
                    "is_default": is_default,
                    "priority": priority,
                    "query_identifier": query_identifier,
                    "response_identifier": response_identifier,
                    "should_escalate": should_escalate,
                    "should_guardrail": should_guardrail,
                    "threshold": threshold,
                    "threshold_direction": threshold_direction,
                },
                eval_create_params.EvalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectReturnSchema,
        )

    @overload
    def update(
        self,
        path_eval_key: str,
        *,
        project_id: str,
        criteria: str,
        body_eval_key: str,
        name: str,
        context_identifier: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        guardrailed_fallback_message: Optional[str] | Omit = omit,
        is_default: bool | Omit = omit,
        priority: Optional[int] | Omit = omit,
        query_identifier: Optional[str] | Omit = omit,
        response_identifier: Optional[str] | Omit = omit,
        should_escalate: bool | Omit = omit,
        should_guardrail: bool | Omit = omit,
        threshold: float | Omit = omit,
        threshold_direction: Literal["above", "below"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectReturnSchema:
        """
        Update an existing eval for a project.

        Args:
          criteria: The evaluation criteria text that describes what aspect is being evaluated and
              how

          body_eval_key: Unique key for eval metric - currently maps to the TrustworthyRAG name property
              and eval_scores dictionary key to check against threshold

          name: Display name/label for the evaluation metric

          context_identifier: The exact string used in your evaluation criteria to reference the retrieved
              context.

          enabled: Allows the evaluation to be disabled without removing it

          guardrailed_fallback_message: Fallback message to use if this eval fails and causes the response to be
              guardrailed

          is_default: Whether the eval is a default, built-in eval or a custom eval

          priority: Priority order for evals (lower number = higher priority) to determine primary
              eval issue to surface

          query_identifier: The exact string used in your evaluation criteria to reference the user's query.

          response_identifier: The exact string used in your evaluation criteria to reference the RAG/LLM
              response.

          should_escalate: If true, failing this eval means the question should be escalated to Codex for
              an SME to review

          should_guardrail: If true, failing this eval means the response should be guardrailed

          threshold: Threshold value that determines if the evaluation fails

          threshold_direction: Whether the evaluation fails when score is above or below the threshold

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        path_eval_key: str,
        *,
        project_id: str,
        body_eval_key: str,
        enabled: bool | Omit = omit,
        guardrailed_fallback_message: Optional[str] | Omit = omit,
        priority: Optional[int] | Omit = omit,
        should_escalate: bool | Omit = omit,
        should_guardrail: bool | Omit = omit,
        threshold: float | Omit = omit,
        threshold_direction: Literal["above", "below"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectReturnSchema:
        """
        Update an existing eval for a project.

        Args:
          body_eval_key: Unique key for eval metric - currently maps to the TrustworthyRAG name property
              and eval_scores dictionary key to check against threshold

          enabled: Allows the evaluation to be disabled without removing it

          guardrailed_fallback_message: Fallback message to use if this eval fails and causes the response to be
              guardrailed

          priority: Priority order for evals (lower number = higher priority) to determine primary
              eval issue to surface

          should_escalate: If true, failing this eval means the question should be escalated to Codex for
              an SME to review

          should_guardrail: If true, failing this eval means the response should be guardrailed

          threshold: Threshold value that determines if the evaluation fails

          threshold_direction: Whether the evaluation fails when score is above or below the threshold

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["project_id", "criteria", "body_eval_key", "name"], ["project_id", "body_eval_key"])
    def update(
        self,
        path_eval_key: str,
        *,
        project_id: str,
        criteria: str | Omit = omit,
        body_eval_key: str,
        name: str | Omit = omit,
        context_identifier: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        guardrailed_fallback_message: Optional[str] | Omit = omit,
        is_default: bool | Omit = omit,
        priority: Optional[int] | Omit = omit,
        query_identifier: Optional[str] | Omit = omit,
        response_identifier: Optional[str] | Omit = omit,
        should_escalate: bool | Omit = omit,
        should_guardrail: bool | Omit = omit,
        threshold: float | Omit = omit,
        threshold_direction: Literal["above", "below"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectReturnSchema:
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not path_eval_key:
            raise ValueError(f"Expected a non-empty value for `path_eval_key` but received {path_eval_key!r}")
        return self._put(
            f"/api/projects/{project_id}/evals/{path_eval_key}",
            body=maybe_transform(
                {
                    "criteria": criteria,
                    "body_eval_key": body_eval_key,
                    "name": name,
                    "context_identifier": context_identifier,
                    "enabled": enabled,
                    "guardrailed_fallback_message": guardrailed_fallback_message,
                    "is_default": is_default,
                    "priority": priority,
                    "query_identifier": query_identifier,
                    "response_identifier": response_identifier,
                    "should_escalate": should_escalate,
                    "should_guardrail": should_guardrail,
                    "threshold": threshold,
                    "threshold_direction": threshold_direction,
                },
                eval_update_params.EvalUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectReturnSchema,
        )

    def list(
        self,
        project_id: str,
        *,
        guardrails_only: bool | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvalListResponse:
        """
        Get the evaluations config for a project with optional pagination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/api/projects/{project_id}/evals",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "guardrails_only": guardrails_only,
                        "limit": limit,
                        "offset": offset,
                    },
                    eval_list_params.EvalListParams,
                ),
            ),
            cast_to=EvalListResponse,
        )

    def delete(
        self,
        eval_key: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectReturnSchema:
        """
        Remove a custom eval for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not eval_key:
            raise ValueError(f"Expected a non-empty value for `eval_key` but received {eval_key!r}")
        return self._delete(
            f"/api/projects/{project_id}/evals/{eval_key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectReturnSchema,
        )


class AsyncEvalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncEvalsResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: str,
        *,
        criteria: str,
        eval_key: str,
        name: str,
        context_identifier: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        guardrailed_fallback_message: Optional[str] | Omit = omit,
        is_default: bool | Omit = omit,
        priority: Optional[int] | Omit = omit,
        query_identifier: Optional[str] | Omit = omit,
        response_identifier: Optional[str] | Omit = omit,
        should_escalate: bool | Omit = omit,
        should_guardrail: bool | Omit = omit,
        threshold: float | Omit = omit,
        threshold_direction: Literal["above", "below"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectReturnSchema:
        """
        Create a new custom eval for a project.

        Args:
          criteria: The evaluation criteria text that describes what aspect is being evaluated and
              how

          eval_key: Unique key for eval metric - currently maps to the TrustworthyRAG name property
              and eval_scores dictionary key to check against threshold

          name: Display name/label for the evaluation metric

          context_identifier: The exact string used in your evaluation criteria to reference the retrieved
              context.

          enabled: Allows the evaluation to be disabled without removing it

          guardrailed_fallback_message: Fallback message to use if this eval fails and causes the response to be
              guardrailed

          is_default: Whether the eval is a default, built-in eval or a custom eval

          priority: Priority order for evals (lower number = higher priority) to determine primary
              eval issue to surface

          query_identifier: The exact string used in your evaluation criteria to reference the user's query.

          response_identifier: The exact string used in your evaluation criteria to reference the RAG/LLM
              response.

          should_escalate: If true, failing this eval means the question should be escalated to Codex for
              an SME to review

          should_guardrail: If true, failing this eval means the response should be guardrailed

          threshold: Threshold value that determines if the evaluation fails

          threshold_direction: Whether the evaluation fails when score is above or below the threshold

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/api/projects/{project_id}/evals",
            body=await async_maybe_transform(
                {
                    "criteria": criteria,
                    "eval_key": eval_key,
                    "name": name,
                    "context_identifier": context_identifier,
                    "enabled": enabled,
                    "guardrailed_fallback_message": guardrailed_fallback_message,
                    "is_default": is_default,
                    "priority": priority,
                    "query_identifier": query_identifier,
                    "response_identifier": response_identifier,
                    "should_escalate": should_escalate,
                    "should_guardrail": should_guardrail,
                    "threshold": threshold,
                    "threshold_direction": threshold_direction,
                },
                eval_create_params.EvalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectReturnSchema,
        )

    @overload
    async def update(
        self,
        path_eval_key: str,
        *,
        project_id: str,
        criteria: str,
        body_eval_key: str,
        name: str,
        context_identifier: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        guardrailed_fallback_message: Optional[str] | Omit = omit,
        is_default: bool | Omit = omit,
        priority: Optional[int] | Omit = omit,
        query_identifier: Optional[str] | Omit = omit,
        response_identifier: Optional[str] | Omit = omit,
        should_escalate: bool | Omit = omit,
        should_guardrail: bool | Omit = omit,
        threshold: float | Omit = omit,
        threshold_direction: Literal["above", "below"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectReturnSchema:
        """
        Update an existing eval for a project.

        Args:
          criteria: The evaluation criteria text that describes what aspect is being evaluated and
              how

          body_eval_key: Unique key for eval metric - currently maps to the TrustworthyRAG name property
              and eval_scores dictionary key to check against threshold

          name: Display name/label for the evaluation metric

          context_identifier: The exact string used in your evaluation criteria to reference the retrieved
              context.

          enabled: Allows the evaluation to be disabled without removing it

          guardrailed_fallback_message: Fallback message to use if this eval fails and causes the response to be
              guardrailed

          is_default: Whether the eval is a default, built-in eval or a custom eval

          priority: Priority order for evals (lower number = higher priority) to determine primary
              eval issue to surface

          query_identifier: The exact string used in your evaluation criteria to reference the user's query.

          response_identifier: The exact string used in your evaluation criteria to reference the RAG/LLM
              response.

          should_escalate: If true, failing this eval means the question should be escalated to Codex for
              an SME to review

          should_guardrail: If true, failing this eval means the response should be guardrailed

          threshold: Threshold value that determines if the evaluation fails

          threshold_direction: Whether the evaluation fails when score is above or below the threshold

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        path_eval_key: str,
        *,
        project_id: str,
        body_eval_key: str,
        enabled: bool | Omit = omit,
        guardrailed_fallback_message: Optional[str] | Omit = omit,
        priority: Optional[int] | Omit = omit,
        should_escalate: bool | Omit = omit,
        should_guardrail: bool | Omit = omit,
        threshold: float | Omit = omit,
        threshold_direction: Literal["above", "below"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectReturnSchema:
        """
        Update an existing eval for a project.

        Args:
          body_eval_key: Unique key for eval metric - currently maps to the TrustworthyRAG name property
              and eval_scores dictionary key to check against threshold

          enabled: Allows the evaluation to be disabled without removing it

          guardrailed_fallback_message: Fallback message to use if this eval fails and causes the response to be
              guardrailed

          priority: Priority order for evals (lower number = higher priority) to determine primary
              eval issue to surface

          should_escalate: If true, failing this eval means the question should be escalated to Codex for
              an SME to review

          should_guardrail: If true, failing this eval means the response should be guardrailed

          threshold: Threshold value that determines if the evaluation fails

          threshold_direction: Whether the evaluation fails when score is above or below the threshold

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["project_id", "criteria", "body_eval_key", "name"], ["project_id", "body_eval_key"])
    async def update(
        self,
        path_eval_key: str,
        *,
        project_id: str,
        criteria: str | Omit = omit,
        body_eval_key: str,
        name: str | Omit = omit,
        context_identifier: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        guardrailed_fallback_message: Optional[str] | Omit = omit,
        is_default: bool | Omit = omit,
        priority: Optional[int] | Omit = omit,
        query_identifier: Optional[str] | Omit = omit,
        response_identifier: Optional[str] | Omit = omit,
        should_escalate: bool | Omit = omit,
        should_guardrail: bool | Omit = omit,
        threshold: float | Omit = omit,
        threshold_direction: Literal["above", "below"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectReturnSchema:
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not path_eval_key:
            raise ValueError(f"Expected a non-empty value for `path_eval_key` but received {path_eval_key!r}")
        return await self._put(
            f"/api/projects/{project_id}/evals/{path_eval_key}",
            body=await async_maybe_transform(
                {
                    "criteria": criteria,
                    "body_eval_key": body_eval_key,
                    "name": name,
                    "context_identifier": context_identifier,
                    "enabled": enabled,
                    "guardrailed_fallback_message": guardrailed_fallback_message,
                    "is_default": is_default,
                    "priority": priority,
                    "query_identifier": query_identifier,
                    "response_identifier": response_identifier,
                    "should_escalate": should_escalate,
                    "should_guardrail": should_guardrail,
                    "threshold": threshold,
                    "threshold_direction": threshold_direction,
                },
                eval_update_params.EvalUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectReturnSchema,
        )

    async def list(
        self,
        project_id: str,
        *,
        guardrails_only: bool | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvalListResponse:
        """
        Get the evaluations config for a project with optional pagination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/evals",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "guardrails_only": guardrails_only,
                        "limit": limit,
                        "offset": offset,
                    },
                    eval_list_params.EvalListParams,
                ),
            ),
            cast_to=EvalListResponse,
        )

    async def delete(
        self,
        eval_key: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectReturnSchema:
        """
        Remove a custom eval for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not eval_key:
            raise ValueError(f"Expected a non-empty value for `eval_key` but received {eval_key!r}")
        return await self._delete(
            f"/api/projects/{project_id}/evals/{eval_key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectReturnSchema,
        )


class EvalsResourceWithRawResponse:
    def __init__(self, evals: EvalsResource) -> None:
        self._evals = evals

        self.create = to_raw_response_wrapper(
            evals.create,
        )
        self.update = to_raw_response_wrapper(
            evals.update,
        )
        self.list = to_raw_response_wrapper(
            evals.list,
        )
        self.delete = to_raw_response_wrapper(
            evals.delete,
        )


class AsyncEvalsResourceWithRawResponse:
    def __init__(self, evals: AsyncEvalsResource) -> None:
        self._evals = evals

        self.create = async_to_raw_response_wrapper(
            evals.create,
        )
        self.update = async_to_raw_response_wrapper(
            evals.update,
        )
        self.list = async_to_raw_response_wrapper(
            evals.list,
        )
        self.delete = async_to_raw_response_wrapper(
            evals.delete,
        )


class EvalsResourceWithStreamingResponse:
    def __init__(self, evals: EvalsResource) -> None:
        self._evals = evals

        self.create = to_streamed_response_wrapper(
            evals.create,
        )
        self.update = to_streamed_response_wrapper(
            evals.update,
        )
        self.list = to_streamed_response_wrapper(
            evals.list,
        )
        self.delete = to_streamed_response_wrapper(
            evals.delete,
        )


class AsyncEvalsResourceWithStreamingResponse:
    def __init__(self, evals: AsyncEvalsResource) -> None:
        self._evals = evals

        self.create = async_to_streamed_response_wrapper(
            evals.create,
        )
        self.update = async_to_streamed_response_wrapper(
            evals.update,
        )
        self.list = async_to_streamed_response_wrapper(
            evals.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            evals.delete,
        )
