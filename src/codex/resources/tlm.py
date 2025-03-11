# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import tlm_score_params, tlm_prompt_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.tlm_score_response import TlmScoreResponse
from ..types.tlm_prompt_response import TlmPromptResponse

__all__ = ["TlmResource", "AsyncTlmResource"]


class TlmResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TlmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return TlmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TlmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return TlmResourceWithStreamingResponse(self)

    def prompt(
        self,
        *,
        prompt: str,
        constrain_outputs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        options: Optional[tlm_prompt_params.Options] | NotGiven = NOT_GIVEN,
        quality_preset: Literal["best", "high", "medium", "low", "base"] | NotGiven = NOT_GIVEN,
        task: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TlmPromptResponse:
        """
        Prompts the TLM API.

        Args:
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
                "base" preset, a cheaper self-reflection will be used to compute the
                trustworthiness score.

              By default, the TLM uses the "medium" quality preset. The default base LLM
              `model` used is "gpt-4o-mini", and `max_tokens` is 512 for all quality presets.
              You can set custom values for these arguments regardless of the quality preset
              specified.

              Args: model ({"gpt-4o-mini", "gpt-4o", "o3-mini", "o1", "o1-mini", "o1-preview",
              "gpt-3.5-turbo-16k", "gpt-4", "gpt-4.5-preview", "claude-3.7-sonnet",
              "claude-3.5-sonnet-v2", "claude-3.5-sonnet", "claude-3.5-haiku",
              "claude-3-haiku", "nova-micro", "nova-lite", "nova-pro"}, default =
              "gpt-4o-mini"): Underlying base LLM to use (better models yield better results,
              faster models yield faster/cheaper results). - Models still in beta: "o1",
              "o3-mini", "o1-mini", "gpt-4.5-preview", "claude-3.7-sonnet",
              "claude-3.5-sonnet-v2", "claude-3.5-haiku", "nova-micro", "nova-lite",
              "nova-pro". - Recommended models for accuracy: "gpt-4o", "o3-mini", "o1",
              "claude-3.7-sonnet". - Recommended models for low latency/costs: "nova-micro",
              "gpt-4o-mini".

                  max_tokens (int, default = 512): the maximum number of tokens that can be generated in the TLM response (and in internal trustworthiness scoring).
                  Higher values here may produce better (more reliable) TLM responses and trustworthiness scores, but at higher costs/runtimes.
                  If you experience token/rate limit errors while using TLM, try lowering this number.
                  For OpenAI models, this parameter must be between 64 and 4096. For Claude models, this parameter must be between 64 and 512.

                  num_candidate_responses (int, default = 1): how many alternative candidate responses are internally generated by TLM.
                  TLM scores the trustworthiness of each candidate response, and then returns the most trustworthy one.
                  Higher values here can produce better (more accurate) responses from the TLM, but at higher costs/runtimes (and internally consumes more tokens).
                  This parameter must be between 1 and 20.
                  When it is 1, TLM simply returns a standard LLM response and does not attempt to auto-improve it.

                  num_consistency_samples (int, default = 8): the amount of internal sampling to evaluate LLM response consistency.
                  Must be between 0 and 20. Higher values produce more reliable TLM trustworthiness scores, but at higher costs/runtimes.
                  This consistency helps quantify the epistemic uncertainty associated with
                  strange prompts or prompts that are too vague/open-ended to receive a clearly defined 'good' response.
                  TLM internally measures consistency via the degree of contradiction between sampled responses that the model considers equally plausible.

                  use_self_reflection (bool, default = `True`): whether the LLM is asked to self-reflect upon the response it
                  generated and self-evaluate this response.
                  Setting this False disables self-reflection and may worsen trustworthiness scores, but will reduce costs/runtimes.
                  Self-reflection helps quantify aleatoric uncertainty associated with challenging prompts
                  and catches answers that are obviously incorrect/bad.

                  similarity_measure ({"semantic", "string", "embedding", "embedding_large"}, default = "semantic"): how the trustworthiness scoring algorithm measures
                  similarity between sampled responses considered by the model in the consistency assessment.
                  Supported similarity measures include "semantic" (based on natural language inference), "string" (based on character/word overlap),
                  "embedding" (based on embedding similarity), and "embedding_large" (based on embedding similarity with a larger embedding model).
                  Set this to "string" to improve latency/costs.

                  reasoning_effort ({"none", "low", "medium", "high"}, default = "high"): how much the LLM can reason (number of thinking tokens)
                  when considering alternative possible responses and double-checking responses.
                  Higher efforts here may produce better TLM trustworthiness scores and LLM responses. Reduce this value to improve latency/costs.

                  log (list[str], default = []): optionally specify additional logs or metadata that TLM should return.
                  For instance, include "explanation" here to get explanations of why a response is scored with low trustworthiness.

                  custom_eval_criteria (list[dict[str, Any]], default = []): optionally specify custom evalution criteria.
                  The expected input format is a list of dictionaries, where each dictionary has the following keys:
                  - name: Name of the evaluation criteria.
                  - criteria: Instructions specifying the evaluation criteria.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/tlm/prompt",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "constrain_outputs": constrain_outputs,
                    "options": options,
                    "quality_preset": quality_preset,
                    "task": task,
                },
                tlm_prompt_params.TlmPromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TlmPromptResponse,
        )

    def score(
        self,
        *,
        prompt: str,
        response: str,
        constrain_outputs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        options: Optional[tlm_score_params.Options] | NotGiven = NOT_GIVEN,
        quality_preset: Literal["best", "high", "medium", "low", "base"] | NotGiven = NOT_GIVEN,
        task: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TlmScoreResponse:
        """
        Scores the TLM API.

        TODO:

        - Track query count in DB
        - Enforce hard cap on queries for users w/o credit card on file

        Args:
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
                "base" preset, a cheaper self-reflection will be used to compute the
                trustworthiness score.

              By default, the TLM uses the "medium" quality preset. The default base LLM
              `model` used is "gpt-4o-mini", and `max_tokens` is 512 for all quality presets.
              You can set custom values for these arguments regardless of the quality preset
              specified.

              Args: model ({"gpt-4o-mini", "gpt-4o", "o3-mini", "o1", "o1-mini", "o1-preview",
              "gpt-3.5-turbo-16k", "gpt-4", "gpt-4.5-preview", "claude-3.7-sonnet",
              "claude-3.5-sonnet-v2", "claude-3.5-sonnet", "claude-3.5-haiku",
              "claude-3-haiku", "nova-micro", "nova-lite", "nova-pro"}, default =
              "gpt-4o-mini"): Underlying base LLM to use (better models yield better results,
              faster models yield faster/cheaper results). - Models still in beta: "o1",
              "o3-mini", "o1-mini", "gpt-4.5-preview", "claude-3.7-sonnet",
              "claude-3.5-sonnet-v2", "claude-3.5-haiku", "nova-micro", "nova-lite",
              "nova-pro". - Recommended models for accuracy: "gpt-4o", "o3-mini", "o1",
              "claude-3.7-sonnet". - Recommended models for low latency/costs: "nova-micro",
              "gpt-4o-mini".

                  max_tokens (int, default = 512): the maximum number of tokens that can be generated in the TLM response (and in internal trustworthiness scoring).
                  Higher values here may produce better (more reliable) TLM responses and trustworthiness scores, but at higher costs/runtimes.
                  If you experience token/rate limit errors while using TLM, try lowering this number.
                  For OpenAI models, this parameter must be between 64 and 4096. For Claude models, this parameter must be between 64 and 512.

                  num_candidate_responses (int, default = 1): how many alternative candidate responses are internally generated by TLM.
                  TLM scores the trustworthiness of each candidate response, and then returns the most trustworthy one.
                  Higher values here can produce better (more accurate) responses from the TLM, but at higher costs/runtimes (and internally consumes more tokens).
                  This parameter must be between 1 and 20.
                  When it is 1, TLM simply returns a standard LLM response and does not attempt to auto-improve it.

                  num_consistency_samples (int, default = 8): the amount of internal sampling to evaluate LLM response consistency.
                  Must be between 0 and 20. Higher values produce more reliable TLM trustworthiness scores, but at higher costs/runtimes.
                  This consistency helps quantify the epistemic uncertainty associated with
                  strange prompts or prompts that are too vague/open-ended to receive a clearly defined 'good' response.
                  TLM internally measures consistency via the degree of contradiction between sampled responses that the model considers equally plausible.

                  use_self_reflection (bool, default = `True`): whether the LLM is asked to self-reflect upon the response it
                  generated and self-evaluate this response.
                  Setting this False disables self-reflection and may worsen trustworthiness scores, but will reduce costs/runtimes.
                  Self-reflection helps quantify aleatoric uncertainty associated with challenging prompts
                  and catches answers that are obviously incorrect/bad.

                  similarity_measure ({"semantic", "string", "embedding", "embedding_large"}, default = "semantic"): how the trustworthiness scoring algorithm measures
                  similarity between sampled responses considered by the model in the consistency assessment.
                  Supported similarity measures include "semantic" (based on natural language inference), "string" (based on character/word overlap),
                  "embedding" (based on embedding similarity), and "embedding_large" (based on embedding similarity with a larger embedding model).
                  Set this to "string" to improve latency/costs.

                  reasoning_effort ({"none", "low", "medium", "high"}, default = "high"): how much the LLM can reason (number of thinking tokens)
                  when considering alternative possible responses and double-checking responses.
                  Higher efforts here may produce better TLM trustworthiness scores and LLM responses. Reduce this value to improve latency/costs.

                  log (list[str], default = []): optionally specify additional logs or metadata that TLM should return.
                  For instance, include "explanation" here to get explanations of why a response is scored with low trustworthiness.

                  custom_eval_criteria (list[dict[str, Any]], default = []): optionally specify custom evalution criteria.
                  The expected input format is a list of dictionaries, where each dictionary has the following keys:
                  - name: Name of the evaluation criteria.
                  - criteria: Instructions specifying the evaluation criteria.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/tlm/score",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "response": response,
                    "constrain_outputs": constrain_outputs,
                    "options": options,
                    "quality_preset": quality_preset,
                    "task": task,
                },
                tlm_score_params.TlmScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TlmScoreResponse,
        )


class AsyncTlmResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTlmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTlmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTlmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncTlmResourceWithStreamingResponse(self)

    async def prompt(
        self,
        *,
        prompt: str,
        constrain_outputs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        options: Optional[tlm_prompt_params.Options] | NotGiven = NOT_GIVEN,
        quality_preset: Literal["best", "high", "medium", "low", "base"] | NotGiven = NOT_GIVEN,
        task: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TlmPromptResponse:
        """
        Prompts the TLM API.

        Args:
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
                "base" preset, a cheaper self-reflection will be used to compute the
                trustworthiness score.

              By default, the TLM uses the "medium" quality preset. The default base LLM
              `model` used is "gpt-4o-mini", and `max_tokens` is 512 for all quality presets.
              You can set custom values for these arguments regardless of the quality preset
              specified.

              Args: model ({"gpt-4o-mini", "gpt-4o", "o3-mini", "o1", "o1-mini", "o1-preview",
              "gpt-3.5-turbo-16k", "gpt-4", "gpt-4.5-preview", "claude-3.7-sonnet",
              "claude-3.5-sonnet-v2", "claude-3.5-sonnet", "claude-3.5-haiku",
              "claude-3-haiku", "nova-micro", "nova-lite", "nova-pro"}, default =
              "gpt-4o-mini"): Underlying base LLM to use (better models yield better results,
              faster models yield faster/cheaper results). - Models still in beta: "o1",
              "o3-mini", "o1-mini", "gpt-4.5-preview", "claude-3.7-sonnet",
              "claude-3.5-sonnet-v2", "claude-3.5-haiku", "nova-micro", "nova-lite",
              "nova-pro". - Recommended models for accuracy: "gpt-4o", "o3-mini", "o1",
              "claude-3.7-sonnet". - Recommended models for low latency/costs: "nova-micro",
              "gpt-4o-mini".

                  max_tokens (int, default = 512): the maximum number of tokens that can be generated in the TLM response (and in internal trustworthiness scoring).
                  Higher values here may produce better (more reliable) TLM responses and trustworthiness scores, but at higher costs/runtimes.
                  If you experience token/rate limit errors while using TLM, try lowering this number.
                  For OpenAI models, this parameter must be between 64 and 4096. For Claude models, this parameter must be between 64 and 512.

                  num_candidate_responses (int, default = 1): how many alternative candidate responses are internally generated by TLM.
                  TLM scores the trustworthiness of each candidate response, and then returns the most trustworthy one.
                  Higher values here can produce better (more accurate) responses from the TLM, but at higher costs/runtimes (and internally consumes more tokens).
                  This parameter must be between 1 and 20.
                  When it is 1, TLM simply returns a standard LLM response and does not attempt to auto-improve it.

                  num_consistency_samples (int, default = 8): the amount of internal sampling to evaluate LLM response consistency.
                  Must be between 0 and 20. Higher values produce more reliable TLM trustworthiness scores, but at higher costs/runtimes.
                  This consistency helps quantify the epistemic uncertainty associated with
                  strange prompts or prompts that are too vague/open-ended to receive a clearly defined 'good' response.
                  TLM internally measures consistency via the degree of contradiction between sampled responses that the model considers equally plausible.

                  use_self_reflection (bool, default = `True`): whether the LLM is asked to self-reflect upon the response it
                  generated and self-evaluate this response.
                  Setting this False disables self-reflection and may worsen trustworthiness scores, but will reduce costs/runtimes.
                  Self-reflection helps quantify aleatoric uncertainty associated with challenging prompts
                  and catches answers that are obviously incorrect/bad.

                  similarity_measure ({"semantic", "string", "embedding", "embedding_large"}, default = "semantic"): how the trustworthiness scoring algorithm measures
                  similarity between sampled responses considered by the model in the consistency assessment.
                  Supported similarity measures include "semantic" (based on natural language inference), "string" (based on character/word overlap),
                  "embedding" (based on embedding similarity), and "embedding_large" (based on embedding similarity with a larger embedding model).
                  Set this to "string" to improve latency/costs.

                  reasoning_effort ({"none", "low", "medium", "high"}, default = "high"): how much the LLM can reason (number of thinking tokens)
                  when considering alternative possible responses and double-checking responses.
                  Higher efforts here may produce better TLM trustworthiness scores and LLM responses. Reduce this value to improve latency/costs.

                  log (list[str], default = []): optionally specify additional logs or metadata that TLM should return.
                  For instance, include "explanation" here to get explanations of why a response is scored with low trustworthiness.

                  custom_eval_criteria (list[dict[str, Any]], default = []): optionally specify custom evalution criteria.
                  The expected input format is a list of dictionaries, where each dictionary has the following keys:
                  - name: Name of the evaluation criteria.
                  - criteria: Instructions specifying the evaluation criteria.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/tlm/prompt",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "constrain_outputs": constrain_outputs,
                    "options": options,
                    "quality_preset": quality_preset,
                    "task": task,
                },
                tlm_prompt_params.TlmPromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TlmPromptResponse,
        )

    async def score(
        self,
        *,
        prompt: str,
        response: str,
        constrain_outputs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        options: Optional[tlm_score_params.Options] | NotGiven = NOT_GIVEN,
        quality_preset: Literal["best", "high", "medium", "low", "base"] | NotGiven = NOT_GIVEN,
        task: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TlmScoreResponse:
        """
        Scores the TLM API.

        TODO:

        - Track query count in DB
        - Enforce hard cap on queries for users w/o credit card on file

        Args:
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
                "base" preset, a cheaper self-reflection will be used to compute the
                trustworthiness score.

              By default, the TLM uses the "medium" quality preset. The default base LLM
              `model` used is "gpt-4o-mini", and `max_tokens` is 512 for all quality presets.
              You can set custom values for these arguments regardless of the quality preset
              specified.

              Args: model ({"gpt-4o-mini", "gpt-4o", "o3-mini", "o1", "o1-mini", "o1-preview",
              "gpt-3.5-turbo-16k", "gpt-4", "gpt-4.5-preview", "claude-3.7-sonnet",
              "claude-3.5-sonnet-v2", "claude-3.5-sonnet", "claude-3.5-haiku",
              "claude-3-haiku", "nova-micro", "nova-lite", "nova-pro"}, default =
              "gpt-4o-mini"): Underlying base LLM to use (better models yield better results,
              faster models yield faster/cheaper results). - Models still in beta: "o1",
              "o3-mini", "o1-mini", "gpt-4.5-preview", "claude-3.7-sonnet",
              "claude-3.5-sonnet-v2", "claude-3.5-haiku", "nova-micro", "nova-lite",
              "nova-pro". - Recommended models for accuracy: "gpt-4o", "o3-mini", "o1",
              "claude-3.7-sonnet". - Recommended models for low latency/costs: "nova-micro",
              "gpt-4o-mini".

                  max_tokens (int, default = 512): the maximum number of tokens that can be generated in the TLM response (and in internal trustworthiness scoring).
                  Higher values here may produce better (more reliable) TLM responses and trustworthiness scores, but at higher costs/runtimes.
                  If you experience token/rate limit errors while using TLM, try lowering this number.
                  For OpenAI models, this parameter must be between 64 and 4096. For Claude models, this parameter must be between 64 and 512.

                  num_candidate_responses (int, default = 1): how many alternative candidate responses are internally generated by TLM.
                  TLM scores the trustworthiness of each candidate response, and then returns the most trustworthy one.
                  Higher values here can produce better (more accurate) responses from the TLM, but at higher costs/runtimes (and internally consumes more tokens).
                  This parameter must be between 1 and 20.
                  When it is 1, TLM simply returns a standard LLM response and does not attempt to auto-improve it.

                  num_consistency_samples (int, default = 8): the amount of internal sampling to evaluate LLM response consistency.
                  Must be between 0 and 20. Higher values produce more reliable TLM trustworthiness scores, but at higher costs/runtimes.
                  This consistency helps quantify the epistemic uncertainty associated with
                  strange prompts or prompts that are too vague/open-ended to receive a clearly defined 'good' response.
                  TLM internally measures consistency via the degree of contradiction between sampled responses that the model considers equally plausible.

                  use_self_reflection (bool, default = `True`): whether the LLM is asked to self-reflect upon the response it
                  generated and self-evaluate this response.
                  Setting this False disables self-reflection and may worsen trustworthiness scores, but will reduce costs/runtimes.
                  Self-reflection helps quantify aleatoric uncertainty associated with challenging prompts
                  and catches answers that are obviously incorrect/bad.

                  similarity_measure ({"semantic", "string", "embedding", "embedding_large"}, default = "semantic"): how the trustworthiness scoring algorithm measures
                  similarity between sampled responses considered by the model in the consistency assessment.
                  Supported similarity measures include "semantic" (based on natural language inference), "string" (based on character/word overlap),
                  "embedding" (based on embedding similarity), and "embedding_large" (based on embedding similarity with a larger embedding model).
                  Set this to "string" to improve latency/costs.

                  reasoning_effort ({"none", "low", "medium", "high"}, default = "high"): how much the LLM can reason (number of thinking tokens)
                  when considering alternative possible responses and double-checking responses.
                  Higher efforts here may produce better TLM trustworthiness scores and LLM responses. Reduce this value to improve latency/costs.

                  log (list[str], default = []): optionally specify additional logs or metadata that TLM should return.
                  For instance, include "explanation" here to get explanations of why a response is scored with low trustworthiness.

                  custom_eval_criteria (list[dict[str, Any]], default = []): optionally specify custom evalution criteria.
                  The expected input format is a list of dictionaries, where each dictionary has the following keys:
                  - name: Name of the evaluation criteria.
                  - criteria: Instructions specifying the evaluation criteria.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/tlm/score",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "response": response,
                    "constrain_outputs": constrain_outputs,
                    "options": options,
                    "quality_preset": quality_preset,
                    "task": task,
                },
                tlm_score_params.TlmScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TlmScoreResponse,
        )


class TlmResourceWithRawResponse:
    def __init__(self, tlm: TlmResource) -> None:
        self._tlm = tlm

        self.prompt = to_raw_response_wrapper(
            tlm.prompt,
        )
        self.score = to_raw_response_wrapper(
            tlm.score,
        )


class AsyncTlmResourceWithRawResponse:
    def __init__(self, tlm: AsyncTlmResource) -> None:
        self._tlm = tlm

        self.prompt = async_to_raw_response_wrapper(
            tlm.prompt,
        )
        self.score = async_to_raw_response_wrapper(
            tlm.score,
        )


class TlmResourceWithStreamingResponse:
    def __init__(self, tlm: TlmResource) -> None:
        self._tlm = tlm

        self.prompt = to_streamed_response_wrapper(
            tlm.prompt,
        )
        self.score = to_streamed_response_wrapper(
            tlm.score,
        )


class AsyncTlmResourceWithStreamingResponse:
    def __init__(self, tlm: AsyncTlmResource) -> None:
        self._tlm = tlm

        self.prompt = async_to_streamed_response_wrapper(
            tlm.prompt,
        )
        self.score = async_to_streamed_response_wrapper(
            tlm.score,
        )
