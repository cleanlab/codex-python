# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.projects import eval_create_params, eval_update_params
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
        context_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        priority: Optional[int] | NotGiven = NOT_GIVEN,
        query_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        response_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        should_escalate: bool | NotGiven = NOT_GIVEN,
        threshold: float | NotGiven = NOT_GIVEN,
        threshold_direction: Literal["above", "below"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          is_default: Whether the eval is a default, built-in eval or a custom eval

          priority: Priority order for evals (lower number = higher priority) to determine primary
              eval issue to surface

          query_identifier: The exact string used in your evaluation criteria to reference the user's query.

          response_identifier: The exact string used in your evaluation criteria to reference the RAG/LLM
              response.

          should_escalate: If true, failing this eval means the response is considered bad and can trigger
              escalation to Codex/SME

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
                    "is_default": is_default,
                    "priority": priority,
                    "query_identifier": query_identifier,
                    "response_identifier": response_identifier,
                    "should_escalate": should_escalate,
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
        context_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        priority: Optional[int] | NotGiven = NOT_GIVEN,
        query_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        response_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        should_escalate: bool | NotGiven = NOT_GIVEN,
        threshold: float | NotGiven = NOT_GIVEN,
        threshold_direction: Literal["above", "below"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          is_default: Whether the eval is a default, built-in eval or a custom eval

          priority: Priority order for evals (lower number = higher priority) to determine primary
              eval issue to surface

          query_identifier: The exact string used in your evaluation criteria to reference the user's query.

          response_identifier: The exact string used in your evaluation criteria to reference the RAG/LLM
              response.

          should_escalate: If true, failing this eval means the response is considered bad and can trigger
              escalation to Codex/SME

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
        enabled: bool | NotGiven = NOT_GIVEN,
        priority: Optional[int] | NotGiven = NOT_GIVEN,
        should_escalate: bool | NotGiven = NOT_GIVEN,
        threshold: float | NotGiven = NOT_GIVEN,
        threshold_direction: Literal["above", "below"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectReturnSchema:
        """
        Update an existing eval for a project.

        Args:
          body_eval_key: Unique key for eval metric - currently maps to the TrustworthyRAG name property
              and eval_scores dictionary key to check against threshold

          enabled: Allows the evaluation to be disabled without removing it

          priority: Priority order for evals (lower number = higher priority) to determine primary
              eval issue to surface

          should_escalate: If true, failing this eval means the response is considered bad and can trigger
              escalation to Codex/SME

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
        criteria: str | NotGiven = NOT_GIVEN,
        body_eval_key: str,
        name: str | NotGiven = NOT_GIVEN,
        context_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        priority: Optional[int] | NotGiven = NOT_GIVEN,
        query_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        response_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        should_escalate: bool | NotGiven = NOT_GIVEN,
        threshold: float | NotGiven = NOT_GIVEN,
        threshold_direction: Literal["above", "below"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
                    "is_default": is_default,
                    "priority": priority,
                    "query_identifier": query_identifier,
                    "response_identifier": response_identifier,
                    "should_escalate": should_escalate,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalListResponse:
        """
        Get the evaluations config for a project.

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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        context_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        priority: Optional[int] | NotGiven = NOT_GIVEN,
        query_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        response_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        should_escalate: bool | NotGiven = NOT_GIVEN,
        threshold: float | NotGiven = NOT_GIVEN,
        threshold_direction: Literal["above", "below"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          is_default: Whether the eval is a default, built-in eval or a custom eval

          priority: Priority order for evals (lower number = higher priority) to determine primary
              eval issue to surface

          query_identifier: The exact string used in your evaluation criteria to reference the user's query.

          response_identifier: The exact string used in your evaluation criteria to reference the RAG/LLM
              response.

          should_escalate: If true, failing this eval means the response is considered bad and can trigger
              escalation to Codex/SME

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
                    "is_default": is_default,
                    "priority": priority,
                    "query_identifier": query_identifier,
                    "response_identifier": response_identifier,
                    "should_escalate": should_escalate,
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
        context_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        priority: Optional[int] | NotGiven = NOT_GIVEN,
        query_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        response_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        should_escalate: bool | NotGiven = NOT_GIVEN,
        threshold: float | NotGiven = NOT_GIVEN,
        threshold_direction: Literal["above", "below"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          is_default: Whether the eval is a default, built-in eval or a custom eval

          priority: Priority order for evals (lower number = higher priority) to determine primary
              eval issue to surface

          query_identifier: The exact string used in your evaluation criteria to reference the user's query.

          response_identifier: The exact string used in your evaluation criteria to reference the RAG/LLM
              response.

          should_escalate: If true, failing this eval means the response is considered bad and can trigger
              escalation to Codex/SME

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
        enabled: bool | NotGiven = NOT_GIVEN,
        priority: Optional[int] | NotGiven = NOT_GIVEN,
        should_escalate: bool | NotGiven = NOT_GIVEN,
        threshold: float | NotGiven = NOT_GIVEN,
        threshold_direction: Literal["above", "below"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectReturnSchema:
        """
        Update an existing eval for a project.

        Args:
          body_eval_key: Unique key for eval metric - currently maps to the TrustworthyRAG name property
              and eval_scores dictionary key to check against threshold

          enabled: Allows the evaluation to be disabled without removing it

          priority: Priority order for evals (lower number = higher priority) to determine primary
              eval issue to surface

          should_escalate: If true, failing this eval means the response is considered bad and can trigger
              escalation to Codex/SME

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
        criteria: str | NotGiven = NOT_GIVEN,
        body_eval_key: str,
        name: str | NotGiven = NOT_GIVEN,
        context_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        priority: Optional[int] | NotGiven = NOT_GIVEN,
        query_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        response_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        should_escalate: bool | NotGiven = NOT_GIVEN,
        threshold: float | NotGiven = NOT_GIVEN,
        threshold_direction: Literal["above", "below"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
                    "is_default": is_default,
                    "priority": priority,
                    "query_identifier": query_identifier,
                    "response_identifier": response_identifier,
                    "should_escalate": should_escalate,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalListResponse:
        """
        Get the evaluations config for a project.

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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
