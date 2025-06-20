# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal

import httpx

from .evals import (
    EvalsResource,
    AsyncEvalsResource,
    EvalsResourceWithRawResponse,
    AsyncEvalsResourceWithRawResponse,
    EvalsResourceWithStreamingResponse,
    AsyncEvalsResourceWithStreamingResponse,
)
from ...types import (
    project_list_params,
    project_create_params,
    project_update_params,
    project_validate_params,
    project_invite_sme_params,
    project_increment_queries_params,
    project_retrieve_analytics_params,
)
from .entries import (
    EntriesResource,
    AsyncEntriesResource,
    EntriesResourceWithRawResponse,
    AsyncEntriesResourceWithRawResponse,
    EntriesResourceWithStreamingResponse,
    AsyncEntriesResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
from .clusters import (
    ClustersResource,
    AsyncClustersResource,
    ClustersResourceWithRawResponse,
    AsyncClustersResourceWithRawResponse,
    ClustersResourceWithStreamingResponse,
    AsyncClustersResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .query_logs import (
    QueryLogsResource,
    AsyncQueryLogsResource,
    QueryLogsResourceWithRawResponse,
    AsyncQueryLogsResourceWithRawResponse,
    QueryLogsResourceWithStreamingResponse,
    AsyncQueryLogsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .access_keys import (
    AccessKeysResource,
    AsyncAccessKeysResource,
    AccessKeysResourceWithRawResponse,
    AsyncAccessKeysResourceWithRawResponse,
    AccessKeysResourceWithStreamingResponse,
    AsyncAccessKeysResourceWithStreamingResponse,
)
from .remediations import (
    RemediationsResource,
    AsyncRemediationsResource,
    RemediationsResourceWithRawResponse,
    AsyncRemediationsResourceWithRawResponse,
    RemediationsResourceWithStreamingResponse,
    AsyncRemediationsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.project_list_response import ProjectListResponse
from ...types.project_return_schema import ProjectReturnSchema
from ...types.project_retrieve_response import ProjectRetrieveResponse
from ...types.project_validate_response import ProjectValidateResponse
from ...types.project_invite_sme_response import ProjectInviteSmeResponse
from ...types.project_retrieve_analytics_response import ProjectRetrieveAnalyticsResponse

__all__ = ["ProjectsResource", "AsyncProjectsResource"]


class ProjectsResource(SyncAPIResource):
    @cached_property
    def access_keys(self) -> AccessKeysResource:
        return AccessKeysResource(self._client)

    @cached_property
    def entries(self) -> EntriesResource:
        return EntriesResource(self._client)

    @cached_property
    def clusters(self) -> ClustersResource:
        return ClustersResource(self._client)

    @cached_property
    def evals(self) -> EvalsResource:
        return EvalsResource(self._client)

    @cached_property
    def query_logs(self) -> QueryLogsResource:
        return QueryLogsResource(self._client)

    @cached_property
    def remediations(self) -> RemediationsResource:
        return RemediationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return ProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return ProjectsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config: project_create_params.Config,
        name: str,
        organization_id: str,
        auto_clustering_enabled: bool | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectReturnSchema:
        """
        Create a new project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/projects/",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "organization_id": organization_id,
                    "auto_clustering_enabled": auto_clustering_enabled,
                    "description": description,
                },
                project_create_params.ProjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectReturnSchema,
        )

    def retrieve(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectRetrieveResponse:
        """
        Get a single project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/api/projects/{project_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRetrieveResponse,
        )

    def update(
        self,
        project_id: str,
        *,
        config: project_update_params.Config,
        name: str,
        auto_clustering_enabled: bool | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectReturnSchema:
        """
        Update a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._put(
            f"/api/projects/{project_id}",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "auto_clustering_enabled": auto_clustering_enabled,
                    "description": description,
                },
                project_update_params.ProjectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectReturnSchema,
        )

    def list(
        self,
        *,
        include_unaddressed_counts: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        query: Optional[str] | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectListResponse:
        """
        List projects for organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/projects/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_unaddressed_counts": include_unaddressed_counts,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "organization_id": organization_id,
                        "query": query,
                        "sort": sort,
                    },
                    project_list_params.ProjectListParams,
                ),
            ),
            cast_to=ProjectListResponse,
        )

    def delete(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/projects/{project_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def export(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Export all data for a project as a JSON file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/api/projects/{project_id}/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @typing_extensions.deprecated("deprecated")
    def increment_queries(
        self,
        project_id: str,
        *,
        count: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Increment the queries metric for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/api/projects/{project_id}/increment_queries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"count": count}, project_increment_queries_params.ProjectIncrementQueriesParams),
            ),
            cast_to=object,
        )

    def invite_sme(
        self,
        project_id: str,
        *,
        email: str,
        page_type: Literal["query_log", "remediation"],
        url_query_string: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectInviteSmeResponse:
        """
        Invite a subject matter expert to view a specific query log or remediation.

        Returns: SMERemediationNotificationResponse with status and notification details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/api/projects/{project_id}/notifications",
            body=maybe_transform(
                {
                    "email": email,
                    "page_type": page_type,
                    "url_query_string": url_query_string,
                },
                project_invite_sme_params.ProjectInviteSmeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectInviteSmeResponse,
        )

    def retrieve_analytics(
        self,
        project_id: str,
        *,
        end: int | NotGiven = NOT_GIVEN,
        start: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectRetrieveAnalyticsResponse:
        """
        Get Project Analytics Route

        Args:
          end: End timestamp in seconds since epoch

          start: Start timestamp in seconds since epoch

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/api/projects/{project_id}/analytics/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                    },
                    project_retrieve_analytics_params.ProjectRetrieveAnalyticsParams,
                ),
            ),
            cast_to=ProjectRetrieveAnalyticsResponse,
        )

    def validate(
        self,
        project_id: str,
        *,
        context: str,
        prompt: str,
        query: str,
        response: str,
        use_llm_matching: bool | NotGiven = NOT_GIVEN,
        constrain_outputs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        custom_eval_thresholds: Optional[Dict[str, float]] | NotGiven = NOT_GIVEN,
        custom_metadata: Optional[object] | NotGiven = NOT_GIVEN,
        eval_scores: Optional[Dict[str, float]] | NotGiven = NOT_GIVEN,
        messages: Optional[Iterable[project_validate_params.Message]] | NotGiven = NOT_GIVEN,
        options: Optional[project_validate_params.Options] | NotGiven = NOT_GIVEN,
        quality_preset: Literal["best", "high", "medium", "low", "base"] | NotGiven = NOT_GIVEN,
        task: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> ProjectValidateResponse:
        """
        Evaluate whether a response, given the provided query and context, is
        potentially bad. If the response is flagged as bad, a lookup is performed to
        find an alternate expert answer. If there is no expert answer available, this
        query will be recorded in the project for SMEs to answer.

        Args:
          custom_eval_thresholds: Optional custom thresholds for specific evals. Keys should match with the keys
              in the `eval_scores` dictionary.

          custom_metadata: Arbitrary metadata supplied by the user/system

          eval_scores: Scores assessing different aspects of the RAG system. If not provided, TLM will
              be used to generate scores.

          messages: Optional message history to provide conversation context for the query. Used to
              rewrite query into a self-contained version of itself. If not provided, the
              query will be treated as self-contained.

          options: Typed dict of advanced configuration options for the Trustworthy Language Model.
              Many of these configurations are determined by the quality preset selected
              (learn about quality presets in the TLM [initialization method](./#class-tlm)).
              Specifying TLMOptions values directly overrides any default values set from the
              quality preset.

              For all options described below, higher settings will lead to longer runtimes
              and may consume more tokens internally. You may not be able to run long prompts
              (or prompts with long responses) in your account, unless your token/rate limits
              are increased. If you hit token limit issues, try lower/less expensive
              TLMOptions to be able to run longer prompts/responses, or contact Cleanlab to
              increase your limits.

              The default values corresponding to each quality preset are:

              - **best:** `num_candidate_responses` = 6, `num_consistency_samples` = 8,
                `use_self_reflection` = True. This preset improves LLM responses.
              - **high:** `num_candidate_responses` = 4, `num_consistency_samples` = 8,
                `use_self_reflection` = True. This preset improves LLM responses.
              - **medium:** `num_candidate_responses` = 1, `num_consistency_samples` = 8,
                `use_self_reflection` = True.
              - **low:** `num_candidate_responses` = 1, `num_consistency_samples` = 4,
                `use_self_reflection` = True.
              - **base:** `num_candidate_responses` = 1, `num_consistency_samples` = 0,
                `use_self_reflection` = False. When using `get_trustworthiness_score()` on
                "base" preset, a faster self-reflection is employed.

              By default, TLM uses the: "medium" `quality_preset`, "gpt-4.1-mini" base
              `model`, and `max_tokens` is set to 512. You can set custom values for these
              arguments regardless of the quality preset specified.

              Args: model ({"gpt-4.1", "gpt-4.1-mini", "gpt-4.1-nano", "o4-mini", "o3",
              "gpt-4.5-preview", "gpt-4o-mini", "gpt-4o", "o3-mini", "o1", "o1-mini", "gpt-4",
              "gpt-3.5-turbo-16k", "claude-opus-4-0", "claude-sonnet-4-0",
              "claude-3.7-sonnet", "claude-3.5-sonnet-v2", "claude-3.5-sonnet",
              "claude-3.5-haiku", "claude-3-haiku", "nova-micro", "nova-lite", "nova-pro"},
              default = "gpt-4.1-mini"): Underlying base LLM to use (better models yield
              better results, faster models yield faster results). - Models still in beta:
              "o3", "o1", "o4-mini", "o3-mini", "o1-mini", "gpt-4.5-preview",
              "claude-opus-4-0", "claude-sonnet-4-0", "claude-3.7-sonnet",
              "claude-3.5-haiku". - Recommended models for accuracy: "gpt-4.1", "o4-mini",
              "o3", "claude-opus-4-0", "claude-sonnet-4-0". - Recommended models for low
              latency/costs: "gpt-4.1-nano", "nova-micro".

                  max_tokens (int, default = 512): the maximum number of tokens that can be generated in the TLM response (and in internal trustworthiness scoring).
                  Higher values here may produce better (more reliable) TLM responses and trustworthiness scores, but at higher runtimes/costs.
                  If you experience token/rate limit errors while using TLM, try lowering this number.
                  For OpenAI models, this parameter must be between 64 and 4096. For Claude models, this parameter must be between 64 and 512.

                  num_candidate_responses (int, default = 1): how many alternative candidate responses are internally generated in `TLM.prompt()`.
                  `TLM.prompt()` scores the trustworthiness of each candidate response, and then returns the most trustworthy one.
                  This parameter must be between 1 and 20. It has no effect on `TLM.score()`.
                  Higher values here can produce more accurate responses from `TLM.prompt()`, but at higher runtimes/costs.
                  When it is 1, `TLM.prompt()` simply returns a standard LLM response and does not attempt to auto-improve it.

                  num_consistency_samples (int, default = 8): the amount of internal sampling to measure LLM response consistency, a factor affecting trustworthiness scoring.
                  Must be between 0 and 20. Higher values produce more reliable TLM trustworthiness scores, but at higher runtimes/costs.
                  Measuring consistency helps quantify the epistemic uncertainty associated with
                  strange prompts or prompts that are too vague/open-ended to receive a clearly defined 'good' response.
                  TLM measures consistency via the degree of contradiction between sampled responses that the model considers plausible.

                  use_self_reflection (bool, default = `True`): whether the LLM is asked to reflect on the given response and directly evaluate correctness/confidence.
                  Setting this False disables reflection and will reduce runtimes/costs, but potentially also the reliability of trustworthiness scores.
                  Reflection helps quantify aleatoric uncertainty associated with challenging prompts
                  and catches responses that are noticeably incorrect/bad upon further analysis.

                  similarity_measure ({"semantic", "string", "embedding", "embedding_large", "code", "discrepancy"}, default = "semantic"): how the
                  trustworthiness scoring's consistency algorithm measures similarity between alternative responses considered plausible by the model.
                  Supported similarity measures include - "semantic" (based on natural language inference),
                  "embedding" (based on vector embedding similarity), "embedding_large" (based on a larger embedding model),
                  "code" (based on model-based analysis designed to compare code), "discrepancy" (based on model-based analysis of possible discrepancies),
                  and "string" (based on character/word overlap). Set this to "string" for minimal runtimes/costs.

                  reasoning_effort ({"none", "low", "medium", "high"}, default = "high"): how much internal LLM calls are allowed to reason (number of thinking tokens)
                  when generating alternative possible responses and reflecting on responses during trustworthiness scoring.
                  Higher reasoning efforts may yield more reliable TLM trustworthiness scores. Reduce this value to reduce runtimes/costs.

                  log (list[str], default = []): optionally specify additional logs or metadata that TLM should return.
                  For instance, include "explanation" here to get explanations of why a response is scored with low trustworthiness.

                  custom_eval_criteria (list[dict[str, Any]], default = []): optionally specify custom evalution criteria beyond the built-in trustworthiness scoring.
                  The expected input format is a list of dictionaries, where each dictionary has the following keys:
                  - name: Name of the evaluation criteria.
                  - criteria: Instructions specifying the evaluation criteria.

          quality_preset: The quality preset to use for the TLM or Trustworthy RAG API.

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
            f"/api/projects/{project_id}/validate",
            body=maybe_transform(
                {
                    "context": context,
                    "prompt": prompt,
                    "query": query,
                    "response": response,
                    "constrain_outputs": constrain_outputs,
                    "custom_eval_thresholds": custom_eval_thresholds,
                    "custom_metadata": custom_metadata,
                    "eval_scores": eval_scores,
                    "messages": messages,
                    "options": options,
                    "quality_preset": quality_preset,
                    "task": task,
                },
                project_validate_params.ProjectValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"use_llm_matching": use_llm_matching}, project_validate_params.ProjectValidateParams
                ),
            ),
            cast_to=ProjectValidateResponse,
        )


class AsyncProjectsResource(AsyncAPIResource):
    @cached_property
    def access_keys(self) -> AsyncAccessKeysResource:
        return AsyncAccessKeysResource(self._client)

    @cached_property
    def entries(self) -> AsyncEntriesResource:
        return AsyncEntriesResource(self._client)

    @cached_property
    def clusters(self) -> AsyncClustersResource:
        return AsyncClustersResource(self._client)

    @cached_property
    def evals(self) -> AsyncEvalsResource:
        return AsyncEvalsResource(self._client)

    @cached_property
    def query_logs(self) -> AsyncQueryLogsResource:
        return AsyncQueryLogsResource(self._client)

    @cached_property
    def remediations(self) -> AsyncRemediationsResource:
        return AsyncRemediationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncProjectsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config: project_create_params.Config,
        name: str,
        organization_id: str,
        auto_clustering_enabled: bool | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectReturnSchema:
        """
        Create a new project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/projects/",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "organization_id": organization_id,
                    "auto_clustering_enabled": auto_clustering_enabled,
                    "description": description,
                },
                project_create_params.ProjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectReturnSchema,
        )

    async def retrieve(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectRetrieveResponse:
        """
        Get a single project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/api/projects/{project_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRetrieveResponse,
        )

    async def update(
        self,
        project_id: str,
        *,
        config: project_update_params.Config,
        name: str,
        auto_clustering_enabled: bool | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectReturnSchema:
        """
        Update a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._put(
            f"/api/projects/{project_id}",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "auto_clustering_enabled": auto_clustering_enabled,
                    "description": description,
                },
                project_update_params.ProjectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectReturnSchema,
        )

    async def list(
        self,
        *,
        include_unaddressed_counts: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        query: Optional[str] | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectListResponse:
        """
        List projects for organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/projects/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_unaddressed_counts": include_unaddressed_counts,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "organization_id": organization_id,
                        "query": query,
                        "sort": sort,
                    },
                    project_list_params.ProjectListParams,
                ),
            ),
            cast_to=ProjectListResponse,
        )

    async def delete(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/projects/{project_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def export(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Export all data for a project as a JSON file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @typing_extensions.deprecated("deprecated")
    async def increment_queries(
        self,
        project_id: str,
        *,
        count: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Increment the queries metric for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/api/projects/{project_id}/increment_queries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"count": count}, project_increment_queries_params.ProjectIncrementQueriesParams
                ),
            ),
            cast_to=object,
        )

    async def invite_sme(
        self,
        project_id: str,
        *,
        email: str,
        page_type: Literal["query_log", "remediation"],
        url_query_string: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectInviteSmeResponse:
        """
        Invite a subject matter expert to view a specific query log or remediation.

        Returns: SMERemediationNotificationResponse with status and notification details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/api/projects/{project_id}/notifications",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "page_type": page_type,
                    "url_query_string": url_query_string,
                },
                project_invite_sme_params.ProjectInviteSmeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectInviteSmeResponse,
        )

    async def retrieve_analytics(
        self,
        project_id: str,
        *,
        end: int | NotGiven = NOT_GIVEN,
        start: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectRetrieveAnalyticsResponse:
        """
        Get Project Analytics Route

        Args:
          end: End timestamp in seconds since epoch

          start: Start timestamp in seconds since epoch

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/analytics/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                    },
                    project_retrieve_analytics_params.ProjectRetrieveAnalyticsParams,
                ),
            ),
            cast_to=ProjectRetrieveAnalyticsResponse,
        )

    async def validate(
        self,
        project_id: str,
        *,
        context: str,
        prompt: str,
        query: str,
        response: str,
        use_llm_matching: bool | NotGiven = NOT_GIVEN,
        constrain_outputs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        custom_eval_thresholds: Optional[Dict[str, float]] | NotGiven = NOT_GIVEN,
        custom_metadata: Optional[object] | NotGiven = NOT_GIVEN,
        eval_scores: Optional[Dict[str, float]] | NotGiven = NOT_GIVEN,
        messages: Optional[Iterable[project_validate_params.Message]] | NotGiven = NOT_GIVEN,
        options: Optional[project_validate_params.Options] | NotGiven = NOT_GIVEN,
        quality_preset: Literal["best", "high", "medium", "low", "base"] | NotGiven = NOT_GIVEN,
        task: Optional[str] | NotGiven = NOT_GIVEN,
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
    ) -> ProjectValidateResponse:
        """
        Evaluate whether a response, given the provided query and context, is
        potentially bad. If the response is flagged as bad, a lookup is performed to
        find an alternate expert answer. If there is no expert answer available, this
        query will be recorded in the project for SMEs to answer.

        Args:
          custom_eval_thresholds: Optional custom thresholds for specific evals. Keys should match with the keys
              in the `eval_scores` dictionary.

          custom_metadata: Arbitrary metadata supplied by the user/system

          eval_scores: Scores assessing different aspects of the RAG system. If not provided, TLM will
              be used to generate scores.

          messages: Optional message history to provide conversation context for the query. Used to
              rewrite query into a self-contained version of itself. If not provided, the
              query will be treated as self-contained.

          options: Typed dict of advanced configuration options for the Trustworthy Language Model.
              Many of these configurations are determined by the quality preset selected
              (learn about quality presets in the TLM [initialization method](./#class-tlm)).
              Specifying TLMOptions values directly overrides any default values set from the
              quality preset.

              For all options described below, higher settings will lead to longer runtimes
              and may consume more tokens internally. You may not be able to run long prompts
              (or prompts with long responses) in your account, unless your token/rate limits
              are increased. If you hit token limit issues, try lower/less expensive
              TLMOptions to be able to run longer prompts/responses, or contact Cleanlab to
              increase your limits.

              The default values corresponding to each quality preset are:

              - **best:** `num_candidate_responses` = 6, `num_consistency_samples` = 8,
                `use_self_reflection` = True. This preset improves LLM responses.
              - **high:** `num_candidate_responses` = 4, `num_consistency_samples` = 8,
                `use_self_reflection` = True. This preset improves LLM responses.
              - **medium:** `num_candidate_responses` = 1, `num_consistency_samples` = 8,
                `use_self_reflection` = True.
              - **low:** `num_candidate_responses` = 1, `num_consistency_samples` = 4,
                `use_self_reflection` = True.
              - **base:** `num_candidate_responses` = 1, `num_consistency_samples` = 0,
                `use_self_reflection` = False. When using `get_trustworthiness_score()` on
                "base" preset, a faster self-reflection is employed.

              By default, TLM uses the: "medium" `quality_preset`, "gpt-4.1-mini" base
              `model`, and `max_tokens` is set to 512. You can set custom values for these
              arguments regardless of the quality preset specified.

              Args: model ({"gpt-4.1", "gpt-4.1-mini", "gpt-4.1-nano", "o4-mini", "o3",
              "gpt-4.5-preview", "gpt-4o-mini", "gpt-4o", "o3-mini", "o1", "o1-mini", "gpt-4",
              "gpt-3.5-turbo-16k", "claude-opus-4-0", "claude-sonnet-4-0",
              "claude-3.7-sonnet", "claude-3.5-sonnet-v2", "claude-3.5-sonnet",
              "claude-3.5-haiku", "claude-3-haiku", "nova-micro", "nova-lite", "nova-pro"},
              default = "gpt-4.1-mini"): Underlying base LLM to use (better models yield
              better results, faster models yield faster results). - Models still in beta:
              "o3", "o1", "o4-mini", "o3-mini", "o1-mini", "gpt-4.5-preview",
              "claude-opus-4-0", "claude-sonnet-4-0", "claude-3.7-sonnet",
              "claude-3.5-haiku". - Recommended models for accuracy: "gpt-4.1", "o4-mini",
              "o3", "claude-opus-4-0", "claude-sonnet-4-0". - Recommended models for low
              latency/costs: "gpt-4.1-nano", "nova-micro".

                  max_tokens (int, default = 512): the maximum number of tokens that can be generated in the TLM response (and in internal trustworthiness scoring).
                  Higher values here may produce better (more reliable) TLM responses and trustworthiness scores, but at higher runtimes/costs.
                  If you experience token/rate limit errors while using TLM, try lowering this number.
                  For OpenAI models, this parameter must be between 64 and 4096. For Claude models, this parameter must be between 64 and 512.

                  num_candidate_responses (int, default = 1): how many alternative candidate responses are internally generated in `TLM.prompt()`.
                  `TLM.prompt()` scores the trustworthiness of each candidate response, and then returns the most trustworthy one.
                  This parameter must be between 1 and 20. It has no effect on `TLM.score()`.
                  Higher values here can produce more accurate responses from `TLM.prompt()`, but at higher runtimes/costs.
                  When it is 1, `TLM.prompt()` simply returns a standard LLM response and does not attempt to auto-improve it.

                  num_consistency_samples (int, default = 8): the amount of internal sampling to measure LLM response consistency, a factor affecting trustworthiness scoring.
                  Must be between 0 and 20. Higher values produce more reliable TLM trustworthiness scores, but at higher runtimes/costs.
                  Measuring consistency helps quantify the epistemic uncertainty associated with
                  strange prompts or prompts that are too vague/open-ended to receive a clearly defined 'good' response.
                  TLM measures consistency via the degree of contradiction between sampled responses that the model considers plausible.

                  use_self_reflection (bool, default = `True`): whether the LLM is asked to reflect on the given response and directly evaluate correctness/confidence.
                  Setting this False disables reflection and will reduce runtimes/costs, but potentially also the reliability of trustworthiness scores.
                  Reflection helps quantify aleatoric uncertainty associated with challenging prompts
                  and catches responses that are noticeably incorrect/bad upon further analysis.

                  similarity_measure ({"semantic", "string", "embedding", "embedding_large", "code", "discrepancy"}, default = "semantic"): how the
                  trustworthiness scoring's consistency algorithm measures similarity between alternative responses considered plausible by the model.
                  Supported similarity measures include - "semantic" (based on natural language inference),
                  "embedding" (based on vector embedding similarity), "embedding_large" (based on a larger embedding model),
                  "code" (based on model-based analysis designed to compare code), "discrepancy" (based on model-based analysis of possible discrepancies),
                  and "string" (based on character/word overlap). Set this to "string" for minimal runtimes/costs.

                  reasoning_effort ({"none", "low", "medium", "high"}, default = "high"): how much internal LLM calls are allowed to reason (number of thinking tokens)
                  when generating alternative possible responses and reflecting on responses during trustworthiness scoring.
                  Higher reasoning efforts may yield more reliable TLM trustworthiness scores. Reduce this value to reduce runtimes/costs.

                  log (list[str], default = []): optionally specify additional logs or metadata that TLM should return.
                  For instance, include "explanation" here to get explanations of why a response is scored with low trustworthiness.

                  custom_eval_criteria (list[dict[str, Any]], default = []): optionally specify custom evalution criteria beyond the built-in trustworthiness scoring.
                  The expected input format is a list of dictionaries, where each dictionary has the following keys:
                  - name: Name of the evaluation criteria.
                  - criteria: Instructions specifying the evaluation criteria.

          quality_preset: The quality preset to use for the TLM or Trustworthy RAG API.

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
            f"/api/projects/{project_id}/validate",
            body=await async_maybe_transform(
                {
                    "context": context,
                    "prompt": prompt,
                    "query": query,
                    "response": response,
                    "constrain_outputs": constrain_outputs,
                    "custom_eval_thresholds": custom_eval_thresholds,
                    "custom_metadata": custom_metadata,
                    "eval_scores": eval_scores,
                    "messages": messages,
                    "options": options,
                    "quality_preset": quality_preset,
                    "task": task,
                },
                project_validate_params.ProjectValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"use_llm_matching": use_llm_matching}, project_validate_params.ProjectValidateParams
                ),
            ),
            cast_to=ProjectValidateResponse,
        )


class ProjectsResourceWithRawResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.create = to_raw_response_wrapper(
            projects.create,
        )
        self.retrieve = to_raw_response_wrapper(
            projects.retrieve,
        )
        self.update = to_raw_response_wrapper(
            projects.update,
        )
        self.list = to_raw_response_wrapper(
            projects.list,
        )
        self.delete = to_raw_response_wrapper(
            projects.delete,
        )
        self.export = to_raw_response_wrapper(
            projects.export,
        )
        self.increment_queries = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                projects.increment_queries  # pyright: ignore[reportDeprecated],
            )
        )
        self.invite_sme = to_raw_response_wrapper(
            projects.invite_sme,
        )
        self.retrieve_analytics = to_raw_response_wrapper(
            projects.retrieve_analytics,
        )
        self.validate = to_raw_response_wrapper(
            projects.validate,
        )

    @cached_property
    def access_keys(self) -> AccessKeysResourceWithRawResponse:
        return AccessKeysResourceWithRawResponse(self._projects.access_keys)

    @cached_property
    def entries(self) -> EntriesResourceWithRawResponse:
        return EntriesResourceWithRawResponse(self._projects.entries)

    @cached_property
    def clusters(self) -> ClustersResourceWithRawResponse:
        return ClustersResourceWithRawResponse(self._projects.clusters)

    @cached_property
    def evals(self) -> EvalsResourceWithRawResponse:
        return EvalsResourceWithRawResponse(self._projects.evals)

    @cached_property
    def query_logs(self) -> QueryLogsResourceWithRawResponse:
        return QueryLogsResourceWithRawResponse(self._projects.query_logs)

    @cached_property
    def remediations(self) -> RemediationsResourceWithRawResponse:
        return RemediationsResourceWithRawResponse(self._projects.remediations)


class AsyncProjectsResourceWithRawResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.create = async_to_raw_response_wrapper(
            projects.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            projects.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            projects.update,
        )
        self.list = async_to_raw_response_wrapper(
            projects.list,
        )
        self.delete = async_to_raw_response_wrapper(
            projects.delete,
        )
        self.export = async_to_raw_response_wrapper(
            projects.export,
        )
        self.increment_queries = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                projects.increment_queries  # pyright: ignore[reportDeprecated],
            )
        )
        self.invite_sme = async_to_raw_response_wrapper(
            projects.invite_sme,
        )
        self.retrieve_analytics = async_to_raw_response_wrapper(
            projects.retrieve_analytics,
        )
        self.validate = async_to_raw_response_wrapper(
            projects.validate,
        )

    @cached_property
    def access_keys(self) -> AsyncAccessKeysResourceWithRawResponse:
        return AsyncAccessKeysResourceWithRawResponse(self._projects.access_keys)

    @cached_property
    def entries(self) -> AsyncEntriesResourceWithRawResponse:
        return AsyncEntriesResourceWithRawResponse(self._projects.entries)

    @cached_property
    def clusters(self) -> AsyncClustersResourceWithRawResponse:
        return AsyncClustersResourceWithRawResponse(self._projects.clusters)

    @cached_property
    def evals(self) -> AsyncEvalsResourceWithRawResponse:
        return AsyncEvalsResourceWithRawResponse(self._projects.evals)

    @cached_property
    def query_logs(self) -> AsyncQueryLogsResourceWithRawResponse:
        return AsyncQueryLogsResourceWithRawResponse(self._projects.query_logs)

    @cached_property
    def remediations(self) -> AsyncRemediationsResourceWithRawResponse:
        return AsyncRemediationsResourceWithRawResponse(self._projects.remediations)


class ProjectsResourceWithStreamingResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.create = to_streamed_response_wrapper(
            projects.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            projects.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            projects.update,
        )
        self.list = to_streamed_response_wrapper(
            projects.list,
        )
        self.delete = to_streamed_response_wrapper(
            projects.delete,
        )
        self.export = to_streamed_response_wrapper(
            projects.export,
        )
        self.increment_queries = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                projects.increment_queries  # pyright: ignore[reportDeprecated],
            )
        )
        self.invite_sme = to_streamed_response_wrapper(
            projects.invite_sme,
        )
        self.retrieve_analytics = to_streamed_response_wrapper(
            projects.retrieve_analytics,
        )
        self.validate = to_streamed_response_wrapper(
            projects.validate,
        )

    @cached_property
    def access_keys(self) -> AccessKeysResourceWithStreamingResponse:
        return AccessKeysResourceWithStreamingResponse(self._projects.access_keys)

    @cached_property
    def entries(self) -> EntriesResourceWithStreamingResponse:
        return EntriesResourceWithStreamingResponse(self._projects.entries)

    @cached_property
    def clusters(self) -> ClustersResourceWithStreamingResponse:
        return ClustersResourceWithStreamingResponse(self._projects.clusters)

    @cached_property
    def evals(self) -> EvalsResourceWithStreamingResponse:
        return EvalsResourceWithStreamingResponse(self._projects.evals)

    @cached_property
    def query_logs(self) -> QueryLogsResourceWithStreamingResponse:
        return QueryLogsResourceWithStreamingResponse(self._projects.query_logs)

    @cached_property
    def remediations(self) -> RemediationsResourceWithStreamingResponse:
        return RemediationsResourceWithStreamingResponse(self._projects.remediations)


class AsyncProjectsResourceWithStreamingResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.create = async_to_streamed_response_wrapper(
            projects.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            projects.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            projects.update,
        )
        self.list = async_to_streamed_response_wrapper(
            projects.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            projects.delete,
        )
        self.export = async_to_streamed_response_wrapper(
            projects.export,
        )
        self.increment_queries = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                projects.increment_queries  # pyright: ignore[reportDeprecated],
            )
        )
        self.invite_sme = async_to_streamed_response_wrapper(
            projects.invite_sme,
        )
        self.retrieve_analytics = async_to_streamed_response_wrapper(
            projects.retrieve_analytics,
        )
        self.validate = async_to_streamed_response_wrapper(
            projects.validate,
        )

    @cached_property
    def access_keys(self) -> AsyncAccessKeysResourceWithStreamingResponse:
        return AsyncAccessKeysResourceWithStreamingResponse(self._projects.access_keys)

    @cached_property
    def entries(self) -> AsyncEntriesResourceWithStreamingResponse:
        return AsyncEntriesResourceWithStreamingResponse(self._projects.entries)

    @cached_property
    def clusters(self) -> AsyncClustersResourceWithStreamingResponse:
        return AsyncClustersResourceWithStreamingResponse(self._projects.clusters)

    @cached_property
    def evals(self) -> AsyncEvalsResourceWithStreamingResponse:
        return AsyncEvalsResourceWithStreamingResponse(self._projects.evals)

    @cached_property
    def query_logs(self) -> AsyncQueryLogsResourceWithStreamingResponse:
        return AsyncQueryLogsResourceWithStreamingResponse(self._projects.query_logs)

    @cached_property
    def remediations(self) -> AsyncRemediationsResourceWithStreamingResponse:
        return AsyncRemediationsResourceWithStreamingResponse(self._projects.remediations)
