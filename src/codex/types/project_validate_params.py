# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProjectValidateParams", "Options"]


class ProjectValidateParams(TypedDict, total=False):
    context: Required[str]

    prompt: Required[str]

    query: Required[str]

    response: Required[str]

    use_llm_matching: bool

    constrain_outputs: Optional[List[str]]

    custom_eval_thresholds: Optional[Dict[str, float]]
    """Optional custom thresholds for specific evals.

    Keys should match with the keys in the `eval_scores` dictionary.
    """

    custom_metadata: Optional[object]
    """Arbitrary metadata supplied by the user/system"""

    eval_scores: Optional[Dict[str, float]]
    """Scores assessing different aspects of the RAG system.

    If not provided, TLM will be used to generate scores.
    """

    options: Optional[Options]
    """
    Typed dict of advanced configuration options for the Trustworthy Language Model.
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

    Args: model ({"gpt-4o-mini", "gpt-4o", "gpt-4.1", "gpt-4.1-mini",
    "gpt-4.1-nano", "o4-mini", "o3", "o3-mini", "o1", "o1-mini", "gpt-4",
    "gpt-4.5-preview", "gpt-3.5-turbo-16k", "claude-3.7-sonnet",
    "claude-3.5-sonnet-v2", "claude-3.5-sonnet", "claude-3.5-haiku",
    "claude-3-haiku", "nova-micro", "nova-lite", "nova-pro"}, default =
    "gpt-4o-mini"): Underlying base LLM to use (better models yield better results,
    faster models yield faster/cheaper results). - Models still in beta: "o3", "o1",
    "o4-mini", "o3-mini", "o1-mini", "gpt-4.1", "gpt-4.1-mini", "gpt-4.1-nano",
    "gpt-4.5-preview", "claude-3.7-sonnet", "claude-3.5-sonnet-v2",
    "claude-3.5-haiku", "nova-micro", "nova-lite", "nova-pro". - Recommended models
    for accuracy: "gpt-4.1", "o4-mini", "o3", "claude-3.7-sonnet",
    "claude-3.5-sonnet-v2". - Recommended models for low latency/costs:
    "gpt-4.1-nano", "nova-micro".

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
        Supported similarity measures include: "semantic" (based on natural language inference),
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
    """

    quality_preset: Literal["best", "high", "medium", "low", "base"]
    """The quality preset to use for the TLM or Trustworthy RAG API."""

    task: Optional[str]

    x_client_library_version: Annotated[str, PropertyInfo(alias="x-client-library-version")]

    x_integration_type: Annotated[str, PropertyInfo(alias="x-integration-type")]

    x_source: Annotated[str, PropertyInfo(alias="x-source")]

    x_stainless_package_version: Annotated[str, PropertyInfo(alias="x-stainless-package-version")]


class Options(TypedDict, total=False):
    custom_eval_criteria: Iterable[object]

    log: List[str]

    max_tokens: int

    model: str

    num_candidate_responses: int

    num_consistency_samples: int

    reasoning_effort: str

    similarity_measure: str

    use_self_reflection: bool
