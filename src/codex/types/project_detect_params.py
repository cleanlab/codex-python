# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import builtins
from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ProjectDetectParams",
    "Response",
    "ResponseChatCompletion",
    "ResponseChatCompletionChoice",
    "ResponseChatCompletionChoiceMessage",
    "ResponseChatCompletionChoiceMessageAnnotation",
    "ResponseChatCompletionChoiceMessageAnnotationURLCitation",
    "ResponseChatCompletionChoiceMessageAudio",
    "ResponseChatCompletionChoiceMessageFunctionCall",
    "ResponseChatCompletionChoiceMessageToolCall",
    "ResponseChatCompletionChoiceMessageToolCallFunction",
    "ResponseChatCompletionChoiceLogprobs",
    "ResponseChatCompletionChoiceLogprobsContent",
    "ResponseChatCompletionChoiceLogprobsContentTopLogprob",
    "ResponseChatCompletionChoiceLogprobsRefusal",
    "ResponseChatCompletionChoiceLogprobsRefusalTopLogprob",
    "ResponseChatCompletionUsage",
    "ResponseChatCompletionUsageCompletionTokensDetails",
    "ResponseChatCompletionUsagePromptTokensDetails",
    "EvalConfig",
    "EvalConfigCustomEvals",
    "EvalConfigCustomEvalsEvals",
    "EvalConfigDefaultEvals",
    "EvalConfigDefaultEvalsContextSufficiency",
    "EvalConfigDefaultEvalsQueryEase",
    "EvalConfigDefaultEvalsResponseGroundedness",
    "EvalConfigDefaultEvalsResponseHelpfulness",
    "EvalConfigDefaultEvalsTrustworthiness",
    "Message",
    "MessageChatCompletionAssistantMessageParamInput",
    "MessageChatCompletionAssistantMessageParamInputAudio",
    "MessageChatCompletionAssistantMessageParamInputContentUnionMember1",
    "MessageChatCompletionAssistantMessageParamInputContentUnionMember1ChatCompletionContentPartTextParam",
    "MessageChatCompletionAssistantMessageParamInputContentUnionMember1ChatCompletionContentPartRefusalParam",
    "MessageChatCompletionAssistantMessageParamInputFunctionCall",
    "MessageChatCompletionAssistantMessageParamInputToolCall",
    "MessageChatCompletionAssistantMessageParamInputToolCallFunction",
    "MessageChatCompletionToolMessageParam",
    "MessageChatCompletionToolMessageParamContentUnionMember1",
    "MessageChatCompletionUserMessageParamInput",
    "MessageChatCompletionUserMessageParamInputContentUnionMember1",
    "MessageChatCompletionUserMessageParamInputContentUnionMember1ChatCompletionContentPartTextParam",
    "MessageChatCompletionUserMessageParamInputContentUnionMember1ChatCompletionContentPartImageParam",
    "MessageChatCompletionUserMessageParamInputContentUnionMember1ChatCompletionContentPartImageParamImageURL",
    "MessageChatCompletionUserMessageParamInputContentUnionMember1ChatCompletionContentPartInputAudioParam",
    "MessageChatCompletionUserMessageParamInputContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio",
    "MessageChatCompletionUserMessageParamInputContentUnionMember1File",
    "MessageChatCompletionUserMessageParamInputContentUnionMember1FileFile",
    "MessageChatCompletionSystemMessageParam",
    "MessageChatCompletionSystemMessageParamContentUnionMember1",
    "MessageChatCompletionFunctionMessageParam",
    "MessageChatCompletionDeveloperMessageParam",
    "MessageChatCompletionDeveloperMessageParamContentUnionMember1",
    "Options",
    "Tool",
    "ToolFunction",
]


class ProjectDetectParams(TypedDict, total=False):
    context: Required[str]

    query: Required[str]

    response: Required[Response]

    constrain_outputs: Optional[SequenceNotStr[str]]

    eval_config: EvalConfig
    """All of the evals that should be used for this query"""

    messages: Iterable[Message]
    """Message history to provide conversation context for the query.

    Messages contain up to and including the latest user prompt to the LLM.
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
    """

    quality_preset: Literal["best", "high", "medium", "low", "base"]
    """The quality preset to use for the TLM or Trustworthy RAG API."""

    rewritten_question: Optional[str]
    """
    The re-written query if it was provided by the client to Codex from a user to be
    used instead of the original query.
    """

    task: Optional[str]

    tools: Optional[Iterable[Tool]]
    """Tools to use for the LLM call.

    If not provided, it is assumed no tools were provided to the LLM.
    """


class ResponseChatCompletionChoiceMessageAnnotationURLCitationTyped(TypedDict, total=False):
    end_index: Required[int]

    start_index: Required[int]

    title: Required[str]

    url: Required[str]


ResponseChatCompletionChoiceMessageAnnotationURLCitation: TypeAlias = Union[
    ResponseChatCompletionChoiceMessageAnnotationURLCitationTyped, Dict[str, object]
]


class ResponseChatCompletionChoiceMessageAnnotationTyped(TypedDict, total=False):
    type: Required[Literal["url_citation"]]

    url_citation: Required[ResponseChatCompletionChoiceMessageAnnotationURLCitation]


ResponseChatCompletionChoiceMessageAnnotation: TypeAlias = Union[
    ResponseChatCompletionChoiceMessageAnnotationTyped, Dict[str, object]
]


class ResponseChatCompletionChoiceMessageAudioTyped(TypedDict, total=False):
    id: Required[str]

    data: Required[str]

    expires_at: Required[int]

    transcript: Required[str]


ResponseChatCompletionChoiceMessageAudio: TypeAlias = Union[
    ResponseChatCompletionChoiceMessageAudioTyped, Dict[str, object]
]


class ResponseChatCompletionChoiceMessageFunctionCallTyped(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


ResponseChatCompletionChoiceMessageFunctionCall: TypeAlias = Union[
    ResponseChatCompletionChoiceMessageFunctionCallTyped, Dict[str, object]
]


class ResponseChatCompletionChoiceMessageToolCallFunctionTyped(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


ResponseChatCompletionChoiceMessageToolCallFunction: TypeAlias = Union[
    ResponseChatCompletionChoiceMessageToolCallFunctionTyped, Dict[str, object]
]


class ResponseChatCompletionChoiceMessageToolCallTyped(TypedDict, total=False):
    id: Required[str]

    function: Required[ResponseChatCompletionChoiceMessageToolCallFunction]

    type: Required[Literal["function"]]


ResponseChatCompletionChoiceMessageToolCall: TypeAlias = Union[
    ResponseChatCompletionChoiceMessageToolCallTyped, Dict[str, object]
]


class ResponseChatCompletionChoiceMessageTyped(TypedDict, total=False):
    role: Required[Literal["assistant"]]

    annotations: Optional[Iterable[ResponseChatCompletionChoiceMessageAnnotation]]

    audio: Optional[ResponseChatCompletionChoiceMessageAudio]

    content: Optional[str]

    function_call: Optional[ResponseChatCompletionChoiceMessageFunctionCall]

    refusal: Optional[str]

    tool_calls: Optional[Iterable[ResponseChatCompletionChoiceMessageToolCall]]


ResponseChatCompletionChoiceMessage: TypeAlias = Union[ResponseChatCompletionChoiceMessageTyped, Dict[str, object]]


class ResponseChatCompletionChoiceLogprobsContentTopLogprobTyped(TypedDict, total=False):
    token: Required[str]

    logprob: Required[float]

    bytes: Optional[Iterable[int]]


ResponseChatCompletionChoiceLogprobsContentTopLogprob: TypeAlias = Union[
    ResponseChatCompletionChoiceLogprobsContentTopLogprobTyped, Dict[str, object]
]


class ResponseChatCompletionChoiceLogprobsContentTyped(TypedDict, total=False):
    token: Required[str]

    logprob: Required[float]

    top_logprobs: Required[Iterable[ResponseChatCompletionChoiceLogprobsContentTopLogprob]]

    bytes: Optional[Iterable[int]]


ResponseChatCompletionChoiceLogprobsContent: TypeAlias = Union[
    ResponseChatCompletionChoiceLogprobsContentTyped, Dict[str, object]
]


class ResponseChatCompletionChoiceLogprobsRefusalTopLogprobTyped(TypedDict, total=False):
    token: Required[str]

    logprob: Required[float]

    bytes: Optional[Iterable[int]]


ResponseChatCompletionChoiceLogprobsRefusalTopLogprob: TypeAlias = Union[
    ResponseChatCompletionChoiceLogprobsRefusalTopLogprobTyped, Dict[str, object]
]


class ResponseChatCompletionChoiceLogprobsRefusalTyped(TypedDict, total=False):
    token: Required[str]

    logprob: Required[float]

    top_logprobs: Required[Iterable[ResponseChatCompletionChoiceLogprobsRefusalTopLogprob]]

    bytes: Optional[Iterable[int]]


ResponseChatCompletionChoiceLogprobsRefusal: TypeAlias = Union[
    ResponseChatCompletionChoiceLogprobsRefusalTyped, Dict[str, object]
]


class ResponseChatCompletionChoiceLogprobsTyped(TypedDict, total=False):
    content: Optional[Iterable[ResponseChatCompletionChoiceLogprobsContent]]

    refusal: Optional[Iterable[ResponseChatCompletionChoiceLogprobsRefusal]]


ResponseChatCompletionChoiceLogprobs: TypeAlias = Union[ResponseChatCompletionChoiceLogprobsTyped, Dict[str, object]]


class ResponseChatCompletionChoiceTyped(TypedDict, total=False):
    finish_reason: Required[Literal["stop", "length", "tool_calls", "content_filter", "function_call"]]

    index: Required[int]

    message: Required[ResponseChatCompletionChoiceMessage]

    logprobs: Optional[ResponseChatCompletionChoiceLogprobs]


ResponseChatCompletionChoice: TypeAlias = Union[ResponseChatCompletionChoiceTyped, Dict[str, object]]


class ResponseChatCompletionUsageCompletionTokensDetailsTyped(TypedDict, total=False):
    accepted_prediction_tokens: Optional[int]

    audio_tokens: Optional[int]

    reasoning_tokens: Optional[int]

    rejected_prediction_tokens: Optional[int]


ResponseChatCompletionUsageCompletionTokensDetails: TypeAlias = Union[
    ResponseChatCompletionUsageCompletionTokensDetailsTyped, Dict[str, object]
]


class ResponseChatCompletionUsagePromptTokensDetailsTyped(TypedDict, total=False):
    audio_tokens: Optional[int]

    cached_tokens: Optional[int]


ResponseChatCompletionUsagePromptTokensDetails: TypeAlias = Union[
    ResponseChatCompletionUsagePromptTokensDetailsTyped, Dict[str, object]
]


class ResponseChatCompletionUsageTyped(TypedDict, total=False):
    completion_tokens: Required[int]

    prompt_tokens: Required[int]

    total_tokens: Required[int]

    completion_tokens_details: Optional[ResponseChatCompletionUsageCompletionTokensDetails]

    prompt_tokens_details: Optional[ResponseChatCompletionUsagePromptTokensDetails]


ResponseChatCompletionUsage: TypeAlias = Union[ResponseChatCompletionUsageTyped, Dict[str, object]]


class ResponseChatCompletionTyped(TypedDict, total=False):
    id: Required[str]

    choices: Required[Iterable[ResponseChatCompletionChoice]]

    created: Required[int]

    model: Required[str]

    object: Required[Literal["chat.completion"]]

    service_tier: Optional[Literal["scale", "default"]]

    system_fingerprint: Optional[str]

    usage: Optional[ResponseChatCompletionUsage]


ResponseChatCompletion: TypeAlias = Union[ResponseChatCompletionTyped, Dict[str, builtins.object]]

Response: TypeAlias = Union[str, ResponseChatCompletion]


class EvalConfigCustomEvalsEvals(TypedDict, total=False):
    criteria: Required[str]
    """
    The evaluation criteria text that describes what aspect is being evaluated and
    how
    """

    eval_key: Required[str]
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: Required[str]
    """Display name/label for the evaluation metric"""

    context_identifier: Optional[str]
    """
    The exact string used in your evaluation criteria to reference the retrieved
    context.
    """

    enabled: bool
    """Allows the evaluation to be disabled without removing it"""

    guardrailed_fallback_message: Optional[str]
    """
    Fallback message to use if this eval fails and causes the response to be
    guardrailed
    """

    is_default: bool
    """Whether the eval is a default, built-in eval or a custom eval"""

    priority: Optional[int]
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    query_identifier: Optional[str]
    """
    The exact string used in your evaluation criteria to reference the user's query.
    """

    response_identifier: Optional[str]
    """
    The exact string used in your evaluation criteria to reference the RAG/LLM
    response.
    """

    should_escalate: bool
    """
    If true, failing this eval means the question should be escalated to Codex for
    an SME to review
    """

    should_guardrail: bool
    """If true, failing this eval means the response should be guardrailed"""

    threshold: float
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Literal["above", "below"]
    """Whether the evaluation fails when score is above or below the threshold"""


class EvalConfigCustomEvals(TypedDict, total=False):
    evals: Dict[str, EvalConfigCustomEvalsEvals]


class EvalConfigDefaultEvalsContextSufficiency(TypedDict, total=False):
    eval_key: Required[str]
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: Required[str]
    """Display name/label for the evaluation metric"""

    enabled: bool
    """Allows the evaluation to be disabled without removing it"""

    guardrailed_fallback_message: Optional[str]
    """
    Fallback message to use if this eval fails and causes the response to be
    guardrailed
    """

    priority: Optional[int]
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    should_escalate: bool
    """
    If true, failing this eval means the question should be escalated to Codex for
    an SME to review
    """

    should_guardrail: bool
    """If true, failing this eval means the response should be guardrailed"""

    threshold: float
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Literal["above", "below"]
    """Whether the evaluation fails when score is above or below the threshold"""


class EvalConfigDefaultEvalsQueryEase(TypedDict, total=False):
    eval_key: Required[str]
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: Required[str]
    """Display name/label for the evaluation metric"""

    enabled: bool
    """Allows the evaluation to be disabled without removing it"""

    guardrailed_fallback_message: Optional[str]
    """
    Fallback message to use if this eval fails and causes the response to be
    guardrailed
    """

    priority: Optional[int]
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    should_escalate: bool
    """
    If true, failing this eval means the question should be escalated to Codex for
    an SME to review
    """

    should_guardrail: bool
    """If true, failing this eval means the response should be guardrailed"""

    threshold: float
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Literal["above", "below"]
    """Whether the evaluation fails when score is above or below the threshold"""


class EvalConfigDefaultEvalsResponseGroundedness(TypedDict, total=False):
    eval_key: Required[str]
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: Required[str]
    """Display name/label for the evaluation metric"""

    enabled: bool
    """Allows the evaluation to be disabled without removing it"""

    guardrailed_fallback_message: Optional[str]
    """
    Fallback message to use if this eval fails and causes the response to be
    guardrailed
    """

    priority: Optional[int]
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    should_escalate: bool
    """
    If true, failing this eval means the question should be escalated to Codex for
    an SME to review
    """

    should_guardrail: bool
    """If true, failing this eval means the response should be guardrailed"""

    threshold: float
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Literal["above", "below"]
    """Whether the evaluation fails when score is above or below the threshold"""


class EvalConfigDefaultEvalsResponseHelpfulness(TypedDict, total=False):
    eval_key: Required[str]
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: Required[str]
    """Display name/label for the evaluation metric"""

    enabled: bool
    """Allows the evaluation to be disabled without removing it"""

    guardrailed_fallback_message: Optional[str]
    """
    Fallback message to use if this eval fails and causes the response to be
    guardrailed
    """

    priority: Optional[int]
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    should_escalate: bool
    """
    If true, failing this eval means the question should be escalated to Codex for
    an SME to review
    """

    should_guardrail: bool
    """If true, failing this eval means the response should be guardrailed"""

    threshold: float
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Literal["above", "below"]
    """Whether the evaluation fails when score is above or below the threshold"""


class EvalConfigDefaultEvalsTrustworthiness(TypedDict, total=False):
    eval_key: Required[str]
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: Required[str]
    """Display name/label for the evaluation metric"""

    enabled: bool
    """Allows the evaluation to be disabled without removing it"""

    guardrailed_fallback_message: Optional[str]
    """
    Fallback message to use if this eval fails and causes the response to be
    guardrailed
    """

    priority: Optional[int]
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    should_escalate: bool
    """
    If true, failing this eval means the question should be escalated to Codex for
    an SME to review
    """

    should_guardrail: bool
    """If true, failing this eval means the response should be guardrailed"""

    threshold: float
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Literal["above", "below"]
    """Whether the evaluation fails when score is above or below the threshold"""


class EvalConfigDefaultEvals(TypedDict, total=False):
    context_sufficiency: EvalConfigDefaultEvalsContextSufficiency
    """A pre-configured evaluation metric from TrustworthyRAG or built into the system.

    The evaluation criteria and identifiers are immutable and system-managed, while
    other properties like thresholds and priorities can be configured.
    """

    query_ease: EvalConfigDefaultEvalsQueryEase
    """A pre-configured evaluation metric from TrustworthyRAG or built into the system.

    The evaluation criteria and identifiers are immutable and system-managed, while
    other properties like thresholds and priorities can be configured.
    """

    response_groundedness: EvalConfigDefaultEvalsResponseGroundedness
    """A pre-configured evaluation metric from TrustworthyRAG or built into the system.

    The evaluation criteria and identifiers are immutable and system-managed, while
    other properties like thresholds and priorities can be configured.
    """

    response_helpfulness: EvalConfigDefaultEvalsResponseHelpfulness
    """A pre-configured evaluation metric from TrustworthyRAG or built into the system.

    The evaluation criteria and identifiers are immutable and system-managed, while
    other properties like thresholds and priorities can be configured.
    """

    trustworthiness: EvalConfigDefaultEvalsTrustworthiness
    """A pre-configured evaluation metric from TrustworthyRAG or built into the system.

    The evaluation criteria and identifiers are immutable and system-managed, while
    other properties like thresholds and priorities can be configured.
    """


class EvalConfig(TypedDict, total=False):
    custom_evals: EvalConfigCustomEvals
    """Configuration for custom evaluation metrics."""

    default_evals: EvalConfigDefaultEvals
    """Configuration for default evaluation metrics."""


class MessageChatCompletionAssistantMessageParamInputAudio(TypedDict, total=False):
    id: Required[str]


class MessageChatCompletionAssistantMessageParamInputContentUnionMember1ChatCompletionContentPartTextParam(
    TypedDict, total=False
):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageChatCompletionAssistantMessageParamInputContentUnionMember1ChatCompletionContentPartRefusalParam(
    TypedDict, total=False
):
    refusal: Required[str]

    type: Required[Literal["refusal"]]


MessageChatCompletionAssistantMessageParamInputContentUnionMember1: TypeAlias = Union[
    MessageChatCompletionAssistantMessageParamInputContentUnionMember1ChatCompletionContentPartTextParam,
    MessageChatCompletionAssistantMessageParamInputContentUnionMember1ChatCompletionContentPartRefusalParam,
]


class MessageChatCompletionAssistantMessageParamInputFunctionCall(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class MessageChatCompletionAssistantMessageParamInputToolCallFunction(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class MessageChatCompletionAssistantMessageParamInputToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[MessageChatCompletionAssistantMessageParamInputToolCallFunction]

    type: Required[Literal["function"]]


class MessageChatCompletionAssistantMessageParamInput(TypedDict, total=False):
    role: Required[Literal["assistant"]]

    audio: Optional[MessageChatCompletionAssistantMessageParamInputAudio]

    content: Union[str, Iterable[MessageChatCompletionAssistantMessageParamInputContentUnionMember1], None]

    function_call: Optional[MessageChatCompletionAssistantMessageParamInputFunctionCall]

    name: str

    refusal: Optional[str]

    tool_calls: Iterable[MessageChatCompletionAssistantMessageParamInputToolCall]


class MessageChatCompletionToolMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageChatCompletionToolMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageChatCompletionToolMessageParamContentUnionMember1]]]

    role: Required[Literal["tool"]]

    tool_call_id: Required[str]


class MessageChatCompletionUserMessageParamInputContentUnionMember1ChatCompletionContentPartTextParam(
    TypedDict, total=False
):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageChatCompletionUserMessageParamInputContentUnionMember1ChatCompletionContentPartImageParamImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: Literal["auto", "low", "high"]


class MessageChatCompletionUserMessageParamInputContentUnionMember1ChatCompletionContentPartImageParam(
    TypedDict, total=False
):
    image_url: Required[
        MessageChatCompletionUserMessageParamInputContentUnionMember1ChatCompletionContentPartImageParamImageURL
    ]

    type: Required[Literal["image_url"]]


class MessageChatCompletionUserMessageParamInputContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio(
    TypedDict, total=False
):
    data: Required[str]

    format: Required[Literal["wav", "mp3"]]


class MessageChatCompletionUserMessageParamInputContentUnionMember1ChatCompletionContentPartInputAudioParam(
    TypedDict, total=False
):
    input_audio: Required[
        MessageChatCompletionUserMessageParamInputContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio
    ]

    type: Required[Literal["input_audio"]]


class MessageChatCompletionUserMessageParamInputContentUnionMember1FileFile(TypedDict, total=False):
    file_data: str

    file_id: str

    filename: str


class MessageChatCompletionUserMessageParamInputContentUnionMember1File(TypedDict, total=False):
    file: Required[MessageChatCompletionUserMessageParamInputContentUnionMember1FileFile]

    type: Required[Literal["file"]]


MessageChatCompletionUserMessageParamInputContentUnionMember1: TypeAlias = Union[
    MessageChatCompletionUserMessageParamInputContentUnionMember1ChatCompletionContentPartTextParam,
    MessageChatCompletionUserMessageParamInputContentUnionMember1ChatCompletionContentPartImageParam,
    MessageChatCompletionUserMessageParamInputContentUnionMember1ChatCompletionContentPartInputAudioParam,
    MessageChatCompletionUserMessageParamInputContentUnionMember1File,
]


class MessageChatCompletionUserMessageParamInput(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageChatCompletionUserMessageParamInputContentUnionMember1]]]

    role: Required[Literal["user"]]

    name: str


class MessageChatCompletionSystemMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageChatCompletionSystemMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageChatCompletionSystemMessageParamContentUnionMember1]]]

    role: Required[Literal["system"]]

    name: str


class MessageChatCompletionFunctionMessageParam(TypedDict, total=False):
    content: Required[Optional[str]]

    name: Required[str]

    role: Required[Literal["function"]]


class MessageChatCompletionDeveloperMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageChatCompletionDeveloperMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageChatCompletionDeveloperMessageParamContentUnionMember1]]]

    role: Required[Literal["developer"]]

    name: str


Message: TypeAlias = Union[
    MessageChatCompletionAssistantMessageParamInput,
    MessageChatCompletionToolMessageParam,
    MessageChatCompletionUserMessageParamInput,
    MessageChatCompletionSystemMessageParam,
    MessageChatCompletionFunctionMessageParam,
    MessageChatCompletionDeveloperMessageParam,
]


class Options(TypedDict, total=False):
    custom_eval_criteria: Iterable[object]

    disable_persistence: bool

    disable_trustworthiness: bool

    log: SequenceNotStr[str]

    max_tokens: int

    model: str

    num_candidate_responses: int

    num_consistency_samples: int

    num_self_reflections: int

    reasoning_effort: str

    similarity_measure: str

    use_self_reflection: bool


class ToolFunction(TypedDict, total=False):
    name: Required[str]

    description: str

    parameters: object

    strict: Optional[bool]


class Tool(TypedDict, total=False):
    function: Required[ToolFunction]

    type: Required[Literal["function"]]
