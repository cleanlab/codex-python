# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
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
    project_detect_params,
    project_update_params,
    project_validate_params,
    project_invite_sme_params,
    project_retrieve_analytics_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
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
from ...types.project_detect_response import ProjectDetectResponse
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
        auto_clustering_enabled: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        auto_clustering_enabled: Optional[bool] | Omit = omit,
        config: Optional[project_update_params.Config] | Omit = omit,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                    "auto_clustering_enabled": auto_clustering_enabled,
                    "config": config,
                    "description": description,
                    "name": name,
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
        include_unaddressed_counts: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        organization_id: str | Omit = omit,
        query: Optional[str] | Omit = omit,
        sort: Literal["created_at", "updated_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def detect(
        self,
        project_id: str,
        *,
        context: str,
        query: str,
        response: project_detect_params.Response,
        constrain_outputs: Optional[SequenceNotStr[str]] | Omit = omit,
        eval_config: project_detect_params.EvalConfig | Omit = omit,
        messages: Iterable[project_detect_params.Message] | Omit = omit,
        options: Optional[project_detect_params.Options] | Omit = omit,
        quality_preset: Literal["best", "high", "medium", "low", "base"] | Omit = omit,
        rewritten_question: Optional[str] | Omit = omit,
        task: Optional[str] | Omit = omit,
        tools: Optional[Iterable[project_detect_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectDetectResponse:
        """
        Detect whether a response, given the provided query and context, is potentially
        bad. No query is logged in the project for this API route. Optionally, users can
        add custom evals for each request, or swap in different settings for the current
        project's evals.

        Args:
          eval_config: All of the evals that should be used for this query

          messages: Message history to provide conversation context for the query. Messages contain
              up to and including the latest user prompt to the LLM.

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

              - **best:** `num_consistency_samples` = 8, `num_self_reflections` = 3,
                `reasoning_effort` = `"high"`.
              - **high:** `num_consistency_samples` = 4, `num_self_reflections` = 3,
                `reasoning_effort` = `"high"`.
              - **medium:** `num_consistency_samples` = 0, `num_self_reflections` = 3,
                `reasoning_effort` = `"high"`.
              - **low:** `num_consistency_samples` = 0, `num_self_reflections` = 3,
                `reasoning_effort` = `"none"`.
              - **base:** `num_consistency_samples` = 0, `num_self_reflections` = 1,
                `reasoning_effort` = `"none"`.

              By default, TLM uses the: "medium" `quality_preset`, "gpt-4.1-mini" base
              `model`, and `max_tokens` is set to 512. You can set custom values for these
              arguments regardless of the quality preset specified.

              Args: model ({"gpt-5", "gpt-5-mini", "gpt-5-nano", "gpt-4.1", "gpt-4.1-mini",
              "gpt-4.1-nano", "o4-mini", "o3", "gpt-4.5-preview", "gpt-4o-mini", "gpt-4o",
              "o3-mini", "o1", "o1-mini", "gpt-4", "gpt-3.5-turbo-16k", "claude-opus-4-0",
              "claude-sonnet-4-0", "claude-3.7-sonnet", "claude-3.5-sonnet-v2",
              "claude-3.5-sonnet", "claude-3.5-haiku", "claude-3-haiku", "nova-micro",
              "nova-lite", "nova-pro"}, default = "gpt-4.1-mini"): Underlying base LLM to use
              (better models yield better results, faster models yield faster results). -
              Models still in beta: "o3", "o1", "o4-mini", "o3-mini", "o1-mini",
              "gpt-4.5-preview", "claude-opus-4-0", "claude-sonnet-4-0", "claude-3.7-sonnet",
              "claude-3.5-haiku". - Recommended models for accuracy: "gpt-5", "gpt-4.1",
              "o4-mini", "o3", "claude-opus-4-0", "claude-sonnet-4-0". - Recommended models
              for low latency/costs: "gpt-4.1-nano", "nova-micro".

                  log (list[str], default = []): optionally specify additional logs or metadata that TLM should return.
                  For instance, include "explanation" here to get explanations of why a response is scored with low trustworthiness.

                  custom_eval_criteria (list[dict[str, Any]], default = []): optionally specify custom evalution criteria beyond the built-in trustworthiness scoring.
                  The expected input format is a list of dictionaries, where each dictionary has the following keys:
                  - name: Name of the evaluation criteria.
                  - criteria: Instructions specifying the evaluation criteria.

                  max_tokens (int, default = 512): the maximum number of tokens that can be generated in the response from `TLM.prompt()` as well as during internal trustworthiness scoring.
                  If you experience token/rate-limit errors, try lowering this number.
                  For OpenAI models, this parameter must be between 64 and 4096. For Claude models, this parameter must be between 64 and 512.

                  reasoning_effort ({"none", "low", "medium", "high"}, default = "high"): how much internal LLM calls are allowed to reason (number of thinking tokens)
                  when generating alternative possible responses and reflecting on responses during trustworthiness scoring.
                  Reduce this value to reduce runtimes. Higher values may improve trust scoring.

                  num_self_reflections (int, default = 3): the number of different evaluations to perform where the LLM reflects on the response, a factor affecting trust scoring.
                  The maximum number currently supported is 3. Lower values can reduce runtimes.
                  Reflection helps quantify aleatoric uncertainty associated with challenging prompts and catches responses that are noticeably incorrect/bad upon further analysis.
                  This parameter has no effect when `disable_trustworthiness` is True.

                  num_consistency_samples (int, default = 8): the amount of internal sampling to measure LLM response consistency, a factor affecting trust scoring.
                  Must be between 0 and 20. Lower values can reduce runtimes.
                  Measuring consistency helps quantify the epistemic uncertainty associated with
                  strange prompts or prompts that are too vague/open-ended to receive a clearly defined 'good' response.
                  TLM measures consistency via the degree of contradiction between sampled responses that the model considers plausible.
                  This parameter has no effect when `disable_trustworthiness` is True.

                  similarity_measure ({"semantic", "string", "embedding", "embedding_large", "code", "discrepancy"}, default = "discrepancy"): how the
                  trustworthiness scoring's consistency algorithm measures similarity between alternative responses considered plausible by the model.
                  Supported similarity measures include - "semantic" (based on natural language inference),
                  "embedding" (based on vector embedding similarity), "embedding_large" (based on a larger embedding model),
                  "code" (based on model-based analysis designed to compare code), "discrepancy" (based on model-based analysis of possible discrepancies),
                  and "string" (based on character/word overlap). Set this to "string" for minimal runtimes.
                  This parameter has no effect when `num_consistency_samples = 0`.

                  num_candidate_responses (int, default = 1): how many alternative candidate responses are internally generated in `TLM.prompt()`.
                  `TLM.prompt()` scores the trustworthiness of each candidate response, and then returns the most trustworthy one.
                  You can auto-improve responses by increasing this parameter, but at higher runtimes/costs.
                  This parameter must be between 1 and 20. It has no effect on `TLM.score()`.
                  When this parameter is 1, `TLM.prompt()` simply returns a standard LLM response and does not attempt to auto-improve it.
                  This parameter has no effect when `disable_trustworthiness` is True.

                  disable_trustworthiness (bool, default = False): if True, TLM will not compute trust scores,
                  useful if you only want to compute custom evaluation criteria.

          quality_preset: The quality preset to use for the TLM or Trustworthy RAG API.

          rewritten_question: The re-written query if it was provided by the client to Codex from a user to be
              used instead of the original query.

          tools: Tools to use for the LLM call. If not provided, it is assumed no tools were
              provided to the LLM.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/api/projects/{project_id}/detect",
            body=maybe_transform(
                {
                    "context": context,
                    "query": query,
                    "response": response,
                    "constrain_outputs": constrain_outputs,
                    "eval_config": eval_config,
                    "messages": messages,
                    "options": options,
                    "quality_preset": quality_preset,
                    "rewritten_question": rewritten_question,
                    "task": task,
                    "tools": tools,
                },
                project_detect_params.ProjectDetectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDetectResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def invite_sme(
        self,
        project_id: str,
        *,
        email: str,
        page_type: Literal["query_log", "remediation", "prioritized_issue"],
        url_query_string: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        end: Optional[int] | Omit = omit,
        metadata_filters: Optional[str] | Omit = omit,
        start: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectRetrieveAnalyticsResponse:
        """
        Retrieve analytics data for a project including queries, bad responses, and
        answers published.

            **Metadata Filtering:**
            - Filter by custom metadata fields using key-value pairs
            - Supports single values: `{"department": "Engineering"}`
            - Supports multiple values: `{"priority": ["high", "medium"]}`
            - Supports null/missing values: `{"department": []}` or `{"department": [null]}`

            **Available Metadata Fields:**
            - Only metadata keys that exist on query logs are returned in `metadata_fields`
            - Fields with ≤12 unique values show as "select" type with checkbox options
            - Fields with >12 unique values show as "input" type for text search
            - Fields with no data are excluded from the response entirely

            **Null Value Behavior:**
            - Empty arrays `[]` are automatically converted to `[null]` to filter for records where the metadata field is missing or null
            - Use `[null]` explicitly to filter for records where the field is missing or null
            - Use `["value1", null, "value2"]` to include both specific values and null values
            - Records match if the metadata field is null, missing from custom_metadata, or custom_metadata itself is null

            **Date Filtering:**
            - Provide `start` only: filter logs created at or after this timestamp
            - Provide `end` only: filter logs created at or before this timestamp
            - Provide both: filter logs created within the time range
            - Provide neither: include all logs regardless of creation time

        Args:
          end: Filter logs created at or before this timestamp (epoch seconds). Can be used
              alone for upper-bound filtering.

          metadata_filters:
              Metadata filters as JSON string. Examples:
                      - Single value: '{"department": "Engineering"}'
                      - Multiple values: '{"priority": ["high", "medium"]}'
                      - Null/missing values: '{"department": []}' or '{"department": [null]}'
                      - Mixed values: '{"status": ["active", null, "pending"]}'

          start: Filter logs created at or after this timestamp (epoch seconds). Can be used
              alone for lower-bound filtering.

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
                        "metadata_filters": metadata_filters,
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
        query: str,
        response: project_validate_params.Response,
        use_llm_matching: Optional[bool] | Omit = omit,
        constrain_outputs: Optional[SequenceNotStr[str]] | Omit = omit,
        custom_eval_thresholds: Optional[Dict[str, float]] | Omit = omit,
        custom_metadata: Optional[object] | Omit = omit,
        eval_scores: Optional[Dict[str, float]] | Omit = omit,
        messages: Iterable[project_validate_params.Message] | Omit = omit,
        options: Optional[project_validate_params.Options] | Omit = omit,
        quality_preset: Literal["best", "high", "medium", "low", "base"] | Omit = omit,
        rewritten_question: Optional[str] | Omit = omit,
        task: Optional[str] | Omit = omit,
        tools: Optional[Iterable[project_validate_params.Tool]] | Omit = omit,
        x_client_library_version: str | Omit = omit,
        x_integration_type: str | Omit = omit,
        x_source: str | Omit = omit,
        x_stainless_package_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          messages: Message history to provide conversation context for the query. Messages contain
              up to and including the latest user prompt to the LLM.

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

              - **best:** `num_consistency_samples` = 8, `num_self_reflections` = 3,
                `reasoning_effort` = `"high"`.
              - **high:** `num_consistency_samples` = 4, `num_self_reflections` = 3,
                `reasoning_effort` = `"high"`.
              - **medium:** `num_consistency_samples` = 0, `num_self_reflections` = 3,
                `reasoning_effort` = `"high"`.
              - **low:** `num_consistency_samples` = 0, `num_self_reflections` = 3,
                `reasoning_effort` = `"none"`.
              - **base:** `num_consistency_samples` = 0, `num_self_reflections` = 1,
                `reasoning_effort` = `"none"`.

              By default, TLM uses the: "medium" `quality_preset`, "gpt-4.1-mini" base
              `model`, and `max_tokens` is set to 512. You can set custom values for these
              arguments regardless of the quality preset specified.

              Args: model ({"gpt-5", "gpt-5-mini", "gpt-5-nano", "gpt-4.1", "gpt-4.1-mini",
              "gpt-4.1-nano", "o4-mini", "o3", "gpt-4.5-preview", "gpt-4o-mini", "gpt-4o",
              "o3-mini", "o1", "o1-mini", "gpt-4", "gpt-3.5-turbo-16k", "claude-opus-4-0",
              "claude-sonnet-4-0", "claude-3.7-sonnet", "claude-3.5-sonnet-v2",
              "claude-3.5-sonnet", "claude-3.5-haiku", "claude-3-haiku", "nova-micro",
              "nova-lite", "nova-pro"}, default = "gpt-4.1-mini"): Underlying base LLM to use
              (better models yield better results, faster models yield faster results). -
              Models still in beta: "o3", "o1", "o4-mini", "o3-mini", "o1-mini",
              "gpt-4.5-preview", "claude-opus-4-0", "claude-sonnet-4-0", "claude-3.7-sonnet",
              "claude-3.5-haiku". - Recommended models for accuracy: "gpt-5", "gpt-4.1",
              "o4-mini", "o3", "claude-opus-4-0", "claude-sonnet-4-0". - Recommended models
              for low latency/costs: "gpt-4.1-nano", "nova-micro".

                  log (list[str], default = []): optionally specify additional logs or metadata that TLM should return.
                  For instance, include "explanation" here to get explanations of why a response is scored with low trustworthiness.

                  custom_eval_criteria (list[dict[str, Any]], default = []): optionally specify custom evalution criteria beyond the built-in trustworthiness scoring.
                  The expected input format is a list of dictionaries, where each dictionary has the following keys:
                  - name: Name of the evaluation criteria.
                  - criteria: Instructions specifying the evaluation criteria.

                  max_tokens (int, default = 512): the maximum number of tokens that can be generated in the response from `TLM.prompt()` as well as during internal trustworthiness scoring.
                  If you experience token/rate-limit errors, try lowering this number.
                  For OpenAI models, this parameter must be between 64 and 4096. For Claude models, this parameter must be between 64 and 512.

                  reasoning_effort ({"none", "low", "medium", "high"}, default = "high"): how much internal LLM calls are allowed to reason (number of thinking tokens)
                  when generating alternative possible responses and reflecting on responses during trustworthiness scoring.
                  Reduce this value to reduce runtimes. Higher values may improve trust scoring.

                  num_self_reflections (int, default = 3): the number of different evaluations to perform where the LLM reflects on the response, a factor affecting trust scoring.
                  The maximum number currently supported is 3. Lower values can reduce runtimes.
                  Reflection helps quantify aleatoric uncertainty associated with challenging prompts and catches responses that are noticeably incorrect/bad upon further analysis.
                  This parameter has no effect when `disable_trustworthiness` is True.

                  num_consistency_samples (int, default = 8): the amount of internal sampling to measure LLM response consistency, a factor affecting trust scoring.
                  Must be between 0 and 20. Lower values can reduce runtimes.
                  Measuring consistency helps quantify the epistemic uncertainty associated with
                  strange prompts or prompts that are too vague/open-ended to receive a clearly defined 'good' response.
                  TLM measures consistency via the degree of contradiction between sampled responses that the model considers plausible.
                  This parameter has no effect when `disable_trustworthiness` is True.

                  similarity_measure ({"semantic", "string", "embedding", "embedding_large", "code", "discrepancy"}, default = "discrepancy"): how the
                  trustworthiness scoring's consistency algorithm measures similarity between alternative responses considered plausible by the model.
                  Supported similarity measures include - "semantic" (based on natural language inference),
                  "embedding" (based on vector embedding similarity), "embedding_large" (based on a larger embedding model),
                  "code" (based on model-based analysis designed to compare code), "discrepancy" (based on model-based analysis of possible discrepancies),
                  and "string" (based on character/word overlap). Set this to "string" for minimal runtimes.
                  This parameter has no effect when `num_consistency_samples = 0`.

                  num_candidate_responses (int, default = 1): how many alternative candidate responses are internally generated in `TLM.prompt()`.
                  `TLM.prompt()` scores the trustworthiness of each candidate response, and then returns the most trustworthy one.
                  You can auto-improve responses by increasing this parameter, but at higher runtimes/costs.
                  This parameter must be between 1 and 20. It has no effect on `TLM.score()`.
                  When this parameter is 1, `TLM.prompt()` simply returns a standard LLM response and does not attempt to auto-improve it.
                  This parameter has no effect when `disable_trustworthiness` is True.

                  disable_trustworthiness (bool, default = False): if True, TLM will not compute trust scores,
                  useful if you only want to compute custom evaluation criteria.

          quality_preset: The quality preset to use for the TLM or Trustworthy RAG API.

          rewritten_question: The re-written query if it was provided by the client to Codex from a user to be
              used instead of the original query.

          tools: Tools to use for the LLM call. If not provided, it is assumed no tools were
              provided to the LLM.

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
                    "query": query,
                    "response": response,
                    "constrain_outputs": constrain_outputs,
                    "custom_eval_thresholds": custom_eval_thresholds,
                    "custom_metadata": custom_metadata,
                    "eval_scores": eval_scores,
                    "messages": messages,
                    "options": options,
                    "quality_preset": quality_preset,
                    "rewritten_question": rewritten_question,
                    "task": task,
                    "tools": tools,
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
        auto_clustering_enabled: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        auto_clustering_enabled: Optional[bool] | Omit = omit,
        config: Optional[project_update_params.Config] | Omit = omit,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                    "auto_clustering_enabled": auto_clustering_enabled,
                    "config": config,
                    "description": description,
                    "name": name,
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
        include_unaddressed_counts: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        organization_id: str | Omit = omit,
        query: Optional[str] | Omit = omit,
        sort: Literal["created_at", "updated_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    async def detect(
        self,
        project_id: str,
        *,
        context: str,
        query: str,
        response: project_detect_params.Response,
        constrain_outputs: Optional[SequenceNotStr[str]] | Omit = omit,
        eval_config: project_detect_params.EvalConfig | Omit = omit,
        messages: Iterable[project_detect_params.Message] | Omit = omit,
        options: Optional[project_detect_params.Options] | Omit = omit,
        quality_preset: Literal["best", "high", "medium", "low", "base"] | Omit = omit,
        rewritten_question: Optional[str] | Omit = omit,
        task: Optional[str] | Omit = omit,
        tools: Optional[Iterable[project_detect_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectDetectResponse:
        """
        Detect whether a response, given the provided query and context, is potentially
        bad. No query is logged in the project for this API route. Optionally, users can
        add custom evals for each request, or swap in different settings for the current
        project's evals.

        Args:
          eval_config: All of the evals that should be used for this query

          messages: Message history to provide conversation context for the query. Messages contain
              up to and including the latest user prompt to the LLM.

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

              - **best:** `num_consistency_samples` = 8, `num_self_reflections` = 3,
                `reasoning_effort` = `"high"`.
              - **high:** `num_consistency_samples` = 4, `num_self_reflections` = 3,
                `reasoning_effort` = `"high"`.
              - **medium:** `num_consistency_samples` = 0, `num_self_reflections` = 3,
                `reasoning_effort` = `"high"`.
              - **low:** `num_consistency_samples` = 0, `num_self_reflections` = 3,
                `reasoning_effort` = `"none"`.
              - **base:** `num_consistency_samples` = 0, `num_self_reflections` = 1,
                `reasoning_effort` = `"none"`.

              By default, TLM uses the: "medium" `quality_preset`, "gpt-4.1-mini" base
              `model`, and `max_tokens` is set to 512. You can set custom values for these
              arguments regardless of the quality preset specified.

              Args: model ({"gpt-5", "gpt-5-mini", "gpt-5-nano", "gpt-4.1", "gpt-4.1-mini",
              "gpt-4.1-nano", "o4-mini", "o3", "gpt-4.5-preview", "gpt-4o-mini", "gpt-4o",
              "o3-mini", "o1", "o1-mini", "gpt-4", "gpt-3.5-turbo-16k", "claude-opus-4-0",
              "claude-sonnet-4-0", "claude-3.7-sonnet", "claude-3.5-sonnet-v2",
              "claude-3.5-sonnet", "claude-3.5-haiku", "claude-3-haiku", "nova-micro",
              "nova-lite", "nova-pro"}, default = "gpt-4.1-mini"): Underlying base LLM to use
              (better models yield better results, faster models yield faster results). -
              Models still in beta: "o3", "o1", "o4-mini", "o3-mini", "o1-mini",
              "gpt-4.5-preview", "claude-opus-4-0", "claude-sonnet-4-0", "claude-3.7-sonnet",
              "claude-3.5-haiku". - Recommended models for accuracy: "gpt-5", "gpt-4.1",
              "o4-mini", "o3", "claude-opus-4-0", "claude-sonnet-4-0". - Recommended models
              for low latency/costs: "gpt-4.1-nano", "nova-micro".

                  log (list[str], default = []): optionally specify additional logs or metadata that TLM should return.
                  For instance, include "explanation" here to get explanations of why a response is scored with low trustworthiness.

                  custom_eval_criteria (list[dict[str, Any]], default = []): optionally specify custom evalution criteria beyond the built-in trustworthiness scoring.
                  The expected input format is a list of dictionaries, where each dictionary has the following keys:
                  - name: Name of the evaluation criteria.
                  - criteria: Instructions specifying the evaluation criteria.

                  max_tokens (int, default = 512): the maximum number of tokens that can be generated in the response from `TLM.prompt()` as well as during internal trustworthiness scoring.
                  If you experience token/rate-limit errors, try lowering this number.
                  For OpenAI models, this parameter must be between 64 and 4096. For Claude models, this parameter must be between 64 and 512.

                  reasoning_effort ({"none", "low", "medium", "high"}, default = "high"): how much internal LLM calls are allowed to reason (number of thinking tokens)
                  when generating alternative possible responses and reflecting on responses during trustworthiness scoring.
                  Reduce this value to reduce runtimes. Higher values may improve trust scoring.

                  num_self_reflections (int, default = 3): the number of different evaluations to perform where the LLM reflects on the response, a factor affecting trust scoring.
                  The maximum number currently supported is 3. Lower values can reduce runtimes.
                  Reflection helps quantify aleatoric uncertainty associated with challenging prompts and catches responses that are noticeably incorrect/bad upon further analysis.
                  This parameter has no effect when `disable_trustworthiness` is True.

                  num_consistency_samples (int, default = 8): the amount of internal sampling to measure LLM response consistency, a factor affecting trust scoring.
                  Must be between 0 and 20. Lower values can reduce runtimes.
                  Measuring consistency helps quantify the epistemic uncertainty associated with
                  strange prompts or prompts that are too vague/open-ended to receive a clearly defined 'good' response.
                  TLM measures consistency via the degree of contradiction between sampled responses that the model considers plausible.
                  This parameter has no effect when `disable_trustworthiness` is True.

                  similarity_measure ({"semantic", "string", "embedding", "embedding_large", "code", "discrepancy"}, default = "discrepancy"): how the
                  trustworthiness scoring's consistency algorithm measures similarity between alternative responses considered plausible by the model.
                  Supported similarity measures include - "semantic" (based on natural language inference),
                  "embedding" (based on vector embedding similarity), "embedding_large" (based on a larger embedding model),
                  "code" (based on model-based analysis designed to compare code), "discrepancy" (based on model-based analysis of possible discrepancies),
                  and "string" (based on character/word overlap). Set this to "string" for minimal runtimes.
                  This parameter has no effect when `num_consistency_samples = 0`.

                  num_candidate_responses (int, default = 1): how many alternative candidate responses are internally generated in `TLM.prompt()`.
                  `TLM.prompt()` scores the trustworthiness of each candidate response, and then returns the most trustworthy one.
                  You can auto-improve responses by increasing this parameter, but at higher runtimes/costs.
                  This parameter must be between 1 and 20. It has no effect on `TLM.score()`.
                  When this parameter is 1, `TLM.prompt()` simply returns a standard LLM response and does not attempt to auto-improve it.
                  This parameter has no effect when `disable_trustworthiness` is True.

                  disable_trustworthiness (bool, default = False): if True, TLM will not compute trust scores,
                  useful if you only want to compute custom evaluation criteria.

          quality_preset: The quality preset to use for the TLM or Trustworthy RAG API.

          rewritten_question: The re-written query if it was provided by the client to Codex from a user to be
              used instead of the original query.

          tools: Tools to use for the LLM call. If not provided, it is assumed no tools were
              provided to the LLM.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/api/projects/{project_id}/detect",
            body=await async_maybe_transform(
                {
                    "context": context,
                    "query": query,
                    "response": response,
                    "constrain_outputs": constrain_outputs,
                    "eval_config": eval_config,
                    "messages": messages,
                    "options": options,
                    "quality_preset": quality_preset,
                    "rewritten_question": rewritten_question,
                    "task": task,
                    "tools": tools,
                },
                project_detect_params.ProjectDetectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDetectResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    async def invite_sme(
        self,
        project_id: str,
        *,
        email: str,
        page_type: Literal["query_log", "remediation", "prioritized_issue"],
        url_query_string: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        end: Optional[int] | Omit = omit,
        metadata_filters: Optional[str] | Omit = omit,
        start: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectRetrieveAnalyticsResponse:
        """
        Retrieve analytics data for a project including queries, bad responses, and
        answers published.

            **Metadata Filtering:**
            - Filter by custom metadata fields using key-value pairs
            - Supports single values: `{"department": "Engineering"}`
            - Supports multiple values: `{"priority": ["high", "medium"]}`
            - Supports null/missing values: `{"department": []}` or `{"department": [null]}`

            **Available Metadata Fields:**
            - Only metadata keys that exist on query logs are returned in `metadata_fields`
            - Fields with ≤12 unique values show as "select" type with checkbox options
            - Fields with >12 unique values show as "input" type for text search
            - Fields with no data are excluded from the response entirely

            **Null Value Behavior:**
            - Empty arrays `[]` are automatically converted to `[null]` to filter for records where the metadata field is missing or null
            - Use `[null]` explicitly to filter for records where the field is missing or null
            - Use `["value1", null, "value2"]` to include both specific values and null values
            - Records match if the metadata field is null, missing from custom_metadata, or custom_metadata itself is null

            **Date Filtering:**
            - Provide `start` only: filter logs created at or after this timestamp
            - Provide `end` only: filter logs created at or before this timestamp
            - Provide both: filter logs created within the time range
            - Provide neither: include all logs regardless of creation time

        Args:
          end: Filter logs created at or before this timestamp (epoch seconds). Can be used
              alone for upper-bound filtering.

          metadata_filters:
              Metadata filters as JSON string. Examples:
                      - Single value: '{"department": "Engineering"}'
                      - Multiple values: '{"priority": ["high", "medium"]}'
                      - Null/missing values: '{"department": []}' or '{"department": [null]}'
                      - Mixed values: '{"status": ["active", null, "pending"]}'

          start: Filter logs created at or after this timestamp (epoch seconds). Can be used
              alone for lower-bound filtering.

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
                        "metadata_filters": metadata_filters,
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
        query: str,
        response: project_validate_params.Response,
        use_llm_matching: Optional[bool] | Omit = omit,
        constrain_outputs: Optional[SequenceNotStr[str]] | Omit = omit,
        custom_eval_thresholds: Optional[Dict[str, float]] | Omit = omit,
        custom_metadata: Optional[object] | Omit = omit,
        eval_scores: Optional[Dict[str, float]] | Omit = omit,
        messages: Iterable[project_validate_params.Message] | Omit = omit,
        options: Optional[project_validate_params.Options] | Omit = omit,
        quality_preset: Literal["best", "high", "medium", "low", "base"] | Omit = omit,
        rewritten_question: Optional[str] | Omit = omit,
        task: Optional[str] | Omit = omit,
        tools: Optional[Iterable[project_validate_params.Tool]] | Omit = omit,
        x_client_library_version: str | Omit = omit,
        x_integration_type: str | Omit = omit,
        x_source: str | Omit = omit,
        x_stainless_package_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          messages: Message history to provide conversation context for the query. Messages contain
              up to and including the latest user prompt to the LLM.

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

              - **best:** `num_consistency_samples` = 8, `num_self_reflections` = 3,
                `reasoning_effort` = `"high"`.
              - **high:** `num_consistency_samples` = 4, `num_self_reflections` = 3,
                `reasoning_effort` = `"high"`.
              - **medium:** `num_consistency_samples` = 0, `num_self_reflections` = 3,
                `reasoning_effort` = `"high"`.
              - **low:** `num_consistency_samples` = 0, `num_self_reflections` = 3,
                `reasoning_effort` = `"none"`.
              - **base:** `num_consistency_samples` = 0, `num_self_reflections` = 1,
                `reasoning_effort` = `"none"`.

              By default, TLM uses the: "medium" `quality_preset`, "gpt-4.1-mini" base
              `model`, and `max_tokens` is set to 512. You can set custom values for these
              arguments regardless of the quality preset specified.

              Args: model ({"gpt-5", "gpt-5-mini", "gpt-5-nano", "gpt-4.1", "gpt-4.1-mini",
              "gpt-4.1-nano", "o4-mini", "o3", "gpt-4.5-preview", "gpt-4o-mini", "gpt-4o",
              "o3-mini", "o1", "o1-mini", "gpt-4", "gpt-3.5-turbo-16k", "claude-opus-4-0",
              "claude-sonnet-4-0", "claude-3.7-sonnet", "claude-3.5-sonnet-v2",
              "claude-3.5-sonnet", "claude-3.5-haiku", "claude-3-haiku", "nova-micro",
              "nova-lite", "nova-pro"}, default = "gpt-4.1-mini"): Underlying base LLM to use
              (better models yield better results, faster models yield faster results). -
              Models still in beta: "o3", "o1", "o4-mini", "o3-mini", "o1-mini",
              "gpt-4.5-preview", "claude-opus-4-0", "claude-sonnet-4-0", "claude-3.7-sonnet",
              "claude-3.5-haiku". - Recommended models for accuracy: "gpt-5", "gpt-4.1",
              "o4-mini", "o3", "claude-opus-4-0", "claude-sonnet-4-0". - Recommended models
              for low latency/costs: "gpt-4.1-nano", "nova-micro".

                  log (list[str], default = []): optionally specify additional logs or metadata that TLM should return.
                  For instance, include "explanation" here to get explanations of why a response is scored with low trustworthiness.

                  custom_eval_criteria (list[dict[str, Any]], default = []): optionally specify custom evalution criteria beyond the built-in trustworthiness scoring.
                  The expected input format is a list of dictionaries, where each dictionary has the following keys:
                  - name: Name of the evaluation criteria.
                  - criteria: Instructions specifying the evaluation criteria.

                  max_tokens (int, default = 512): the maximum number of tokens that can be generated in the response from `TLM.prompt()` as well as during internal trustworthiness scoring.
                  If you experience token/rate-limit errors, try lowering this number.
                  For OpenAI models, this parameter must be between 64 and 4096. For Claude models, this parameter must be between 64 and 512.

                  reasoning_effort ({"none", "low", "medium", "high"}, default = "high"): how much internal LLM calls are allowed to reason (number of thinking tokens)
                  when generating alternative possible responses and reflecting on responses during trustworthiness scoring.
                  Reduce this value to reduce runtimes. Higher values may improve trust scoring.

                  num_self_reflections (int, default = 3): the number of different evaluations to perform where the LLM reflects on the response, a factor affecting trust scoring.
                  The maximum number currently supported is 3. Lower values can reduce runtimes.
                  Reflection helps quantify aleatoric uncertainty associated with challenging prompts and catches responses that are noticeably incorrect/bad upon further analysis.
                  This parameter has no effect when `disable_trustworthiness` is True.

                  num_consistency_samples (int, default = 8): the amount of internal sampling to measure LLM response consistency, a factor affecting trust scoring.
                  Must be between 0 and 20. Lower values can reduce runtimes.
                  Measuring consistency helps quantify the epistemic uncertainty associated with
                  strange prompts or prompts that are too vague/open-ended to receive a clearly defined 'good' response.
                  TLM measures consistency via the degree of contradiction between sampled responses that the model considers plausible.
                  This parameter has no effect when `disable_trustworthiness` is True.

                  similarity_measure ({"semantic", "string", "embedding", "embedding_large", "code", "discrepancy"}, default = "discrepancy"): how the
                  trustworthiness scoring's consistency algorithm measures similarity between alternative responses considered plausible by the model.
                  Supported similarity measures include - "semantic" (based on natural language inference),
                  "embedding" (based on vector embedding similarity), "embedding_large" (based on a larger embedding model),
                  "code" (based on model-based analysis designed to compare code), "discrepancy" (based on model-based analysis of possible discrepancies),
                  and "string" (based on character/word overlap). Set this to "string" for minimal runtimes.
                  This parameter has no effect when `num_consistency_samples = 0`.

                  num_candidate_responses (int, default = 1): how many alternative candidate responses are internally generated in `TLM.prompt()`.
                  `TLM.prompt()` scores the trustworthiness of each candidate response, and then returns the most trustworthy one.
                  You can auto-improve responses by increasing this parameter, but at higher runtimes/costs.
                  This parameter must be between 1 and 20. It has no effect on `TLM.score()`.
                  When this parameter is 1, `TLM.prompt()` simply returns a standard LLM response and does not attempt to auto-improve it.
                  This parameter has no effect when `disable_trustworthiness` is True.

                  disable_trustworthiness (bool, default = False): if True, TLM will not compute trust scores,
                  useful if you only want to compute custom evaluation criteria.

          quality_preset: The quality preset to use for the TLM or Trustworthy RAG API.

          rewritten_question: The re-written query if it was provided by the client to Codex from a user to be
              used instead of the original query.

          tools: Tools to use for the LLM call. If not provided, it is assumed no tools were
              provided to the LLM.

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
                    "query": query,
                    "response": response,
                    "constrain_outputs": constrain_outputs,
                    "custom_eval_thresholds": custom_eval_thresholds,
                    "custom_metadata": custom_metadata,
                    "eval_scores": eval_scores,
                    "messages": messages,
                    "options": options,
                    "quality_preset": quality_preset,
                    "rewritten_question": rewritten_question,
                    "task": task,
                    "tools": tools,
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
        self.detect = to_raw_response_wrapper(
            projects.detect,
        )
        self.export = to_raw_response_wrapper(
            projects.export,
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
        self.detect = async_to_raw_response_wrapper(
            projects.detect,
        )
        self.export = async_to_raw_response_wrapper(
            projects.export,
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
        self.detect = to_streamed_response_wrapper(
            projects.detect,
        )
        self.export = to_streamed_response_wrapper(
            projects.export,
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
        self.detect = async_to_streamed_response_wrapper(
            projects.detect,
        )
        self.export = async_to_streamed_response_wrapper(
            projects.export,
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
    def evals(self) -> AsyncEvalsResourceWithStreamingResponse:
        return AsyncEvalsResourceWithStreamingResponse(self._projects.evals)

    @cached_property
    def query_logs(self) -> AsyncQueryLogsResourceWithStreamingResponse:
        return AsyncQueryLogsResourceWithStreamingResponse(self._projects.query_logs)

    @cached_property
    def remediations(self) -> AsyncRemediationsResourceWithStreamingResponse:
        return AsyncRemediationsResourceWithStreamingResponse(self._projects.remediations)
