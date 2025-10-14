# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "QueryLogListResponse",
    "FormattedEscalationEvalScores",
    "FormattedEvalScores",
    "FormattedGuardrailEvalScores",
    "FormattedNonGuardrailEvalScores",
    "Context",
    "DeterministicGuardrailsResults",
    "EvaluatedResponseToolCall",
    "EvaluatedResponseToolCallFunction",
    "Message",
    "MessageChatCompletionAssistantMessageParamOutput",
    "MessageChatCompletionAssistantMessageParamOutputAudio",
    "MessageChatCompletionAssistantMessageParamOutputContentUnionMember1",
    "MessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam",
    "MessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartRefusalParam",
    "MessageChatCompletionAssistantMessageParamOutputFunctionCall",
    "MessageChatCompletionAssistantMessageParamOutputToolCall",
    "MessageChatCompletionAssistantMessageParamOutputToolCallFunction",
    "MessageChatCompletionToolMessageParam",
    "MessageChatCompletionToolMessageParamContentUnionMember1",
    "MessageChatCompletionUserMessageParamOutput",
    "MessageChatCompletionUserMessageParamOutputContentUnionMember1",
    "MessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam",
    "MessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParam",
    "MessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParamImageURL",
    "MessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParam",
    "MessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio",
    "MessageChatCompletionUserMessageParamOutputContentUnionMember1File",
    "MessageChatCompletionUserMessageParamOutputContentUnionMember1FileFile",
    "MessageChatCompletionSystemMessageParam",
    "MessageChatCompletionSystemMessageParamContentUnionMember1",
    "MessageChatCompletionFunctionMessageParam",
    "MessageChatCompletionDeveloperMessageParam",
    "MessageChatCompletionDeveloperMessageParamContentUnionMember1",
    "Tool",
    "ToolFunction",
]


class FormattedEscalationEvalScores(BaseModel):
    display_name: str

    score: float

    status: Literal["pass", "fail"]


class FormattedEvalScores(BaseModel):
    display_name: str

    score: float

    status: Literal["pass", "fail"]


class FormattedGuardrailEvalScores(BaseModel):
    display_name: str

    score: float

    status: Literal["pass", "fail"]


class FormattedNonGuardrailEvalScores(BaseModel):
    display_name: str

    score: float

    status: Literal["pass", "fail"]


class Context(BaseModel):
    content: str
    """The actual content/text of the document."""

    id: Optional[str] = None
    """Unique identifier for the document. Useful for tracking documents"""

    source: Optional[str] = None
    """Source or origin of the document. Useful for citations."""

    tags: Optional[List[str]] = None
    """Tags or categories for the document. Useful for filtering"""

    title: Optional[str] = None
    """Title or heading of the document. Useful for display and context."""


class DeterministicGuardrailsResults(BaseModel):
    guardrail_name: str

    should_guardrail: bool

    fallback_message: Optional[str] = None

    matches: Optional[List[str]] = None


class EvaluatedResponseToolCallFunction(BaseModel):
    arguments: str

    name: str


class EvaluatedResponseToolCall(BaseModel):
    id: str

    function: EvaluatedResponseToolCallFunction

    type: Literal["function"]


class MessageChatCompletionAssistantMessageParamOutputAudio(BaseModel):
    id: str


class MessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class MessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartRefusalParam(
    BaseModel
):
    refusal: str

    type: Literal["refusal"]


MessageChatCompletionAssistantMessageParamOutputContentUnionMember1: TypeAlias = Union[
    MessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam,
    MessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartRefusalParam,
]


class MessageChatCompletionAssistantMessageParamOutputFunctionCall(BaseModel):
    arguments: str

    name: str


class MessageChatCompletionAssistantMessageParamOutputToolCallFunction(BaseModel):
    arguments: str

    name: str


class MessageChatCompletionAssistantMessageParamOutputToolCall(BaseModel):
    id: str

    function: MessageChatCompletionAssistantMessageParamOutputToolCallFunction

    type: Literal["function"]


class MessageChatCompletionAssistantMessageParamOutput(BaseModel):
    role: Literal["assistant"]

    audio: Optional[MessageChatCompletionAssistantMessageParamOutputAudio] = None

    content: Union[str, List[MessageChatCompletionAssistantMessageParamOutputContentUnionMember1], None] = None

    function_call: Optional[MessageChatCompletionAssistantMessageParamOutputFunctionCall] = None

    name: Optional[str] = None

    refusal: Optional[str] = None

    tool_calls: Optional[List[MessageChatCompletionAssistantMessageParamOutputToolCall]] = None


class MessageChatCompletionToolMessageParamContentUnionMember1(BaseModel):
    text: str

    type: Literal["text"]


class MessageChatCompletionToolMessageParam(BaseModel):
    content: Union[str, List[MessageChatCompletionToolMessageParamContentUnionMember1]]

    role: Literal["tool"]

    tool_call_id: str


class MessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class MessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[Literal["auto", "low", "high"]] = None


class MessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParam(BaseModel):
    image_url: MessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParamImageURL

    type: Literal["image_url"]


class MessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio(
    BaseModel
):
    data: str

    format: Literal["wav", "mp3"]


class MessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParam(BaseModel):
    input_audio: (
        MessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio
    )

    type: Literal["input_audio"]


class MessageChatCompletionUserMessageParamOutputContentUnionMember1FileFile(BaseModel):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    filename: Optional[str] = None


class MessageChatCompletionUserMessageParamOutputContentUnionMember1File(BaseModel):
    file: MessageChatCompletionUserMessageParamOutputContentUnionMember1FileFile

    type: Literal["file"]


MessageChatCompletionUserMessageParamOutputContentUnionMember1: TypeAlias = Union[
    MessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam,
    MessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParam,
    MessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParam,
    MessageChatCompletionUserMessageParamOutputContentUnionMember1File,
]


class MessageChatCompletionUserMessageParamOutput(BaseModel):
    content: Union[str, List[MessageChatCompletionUserMessageParamOutputContentUnionMember1]]

    role: Literal["user"]

    name: Optional[str] = None


class MessageChatCompletionSystemMessageParamContentUnionMember1(BaseModel):
    text: str

    type: Literal["text"]


class MessageChatCompletionSystemMessageParam(BaseModel):
    content: Union[str, List[MessageChatCompletionSystemMessageParamContentUnionMember1]]

    role: Literal["system"]

    name: Optional[str] = None


class MessageChatCompletionFunctionMessageParam(BaseModel):
    content: Optional[str] = None

    name: str

    role: Literal["function"]


class MessageChatCompletionDeveloperMessageParamContentUnionMember1(BaseModel):
    text: str

    type: Literal["text"]


class MessageChatCompletionDeveloperMessageParam(BaseModel):
    content: Union[str, List[MessageChatCompletionDeveloperMessageParamContentUnionMember1]]

    role: Literal["developer"]

    name: Optional[str] = None


Message: TypeAlias = Union[
    MessageChatCompletionAssistantMessageParamOutput,
    MessageChatCompletionToolMessageParam,
    MessageChatCompletionUserMessageParamOutput,
    MessageChatCompletionSystemMessageParam,
    MessageChatCompletionFunctionMessageParam,
    MessageChatCompletionDeveloperMessageParam,
]


class ToolFunction(BaseModel):
    name: str

    description: Optional[str] = None

    parameters: Optional[object] = None

    strict: Optional[bool] = None


class Tool(BaseModel):
    function: ToolFunction

    type: Literal["function"]


class QueryLogListResponse(BaseModel):
    id: str

    created_at: datetime

    formatted_escalation_eval_scores: Optional[Dict[str, FormattedEscalationEvalScores]] = None

    formatted_eval_scores: Optional[Dict[str, FormattedEvalScores]] = None
    """Format evaluation scores for frontend display with pass/fail status.

    Returns: Dictionary mapping eval keys to their formatted representation: {
    "eval_key": { "score": float, "status": "pass" | "fail" } } Returns None if
    eval_scores is None.
    """

    formatted_guardrail_eval_scores: Optional[Dict[str, FormattedGuardrailEvalScores]] = None

    formatted_messages: Optional[str] = None

    formatted_non_guardrail_eval_scores: Optional[Dict[str, FormattedNonGuardrailEvalScores]] = None

    formatted_original_question: Optional[str] = None

    is_bad_response: bool

    project_id: str

    question: str

    remediation_id: str

    tool_call_names: Optional[List[str]] = None

    was_cache_hit: Optional[bool] = None
    """If similar query already answered, or None if cache was not checked"""

    context: Optional[List[Context]] = None
    """RAG context used for the query"""

    custom_metadata: Optional[object] = None
    """Arbitrary metadata supplied by the user/system"""

    custom_metadata_keys: Optional[List[str]] = None
    """Keys of the custom metadata"""

    deterministic_guardrails_results: Optional[Dict[str, DeterministicGuardrailsResults]] = None
    """Results of deterministic guardrails applied to the query"""

    escalated: Optional[bool] = None
    """If true, the question was escalated to Codex for an SME to review"""

    escalation_evals: Optional[List[str]] = None
    """Evals that should trigger escalation to SME"""

    eval_display_names: Optional[Dict[str, str]] = None
    """Mapping of eval keys to display names at time of creation"""

    eval_issue_labels: Optional[List[str]] = None
    """Labels derived from evaluation scores"""

    eval_scores: Optional[Dict[str, float]] = None
    """Evaluation scores for the original response"""

    eval_thresholds: Optional[Dict[str, Dict[str, Union[float, str]]]] = None
    """Evaluation thresholds and directions at time of creation"""

    evaluated_response: Optional[str] = None
    """The response being evaluated from the RAG system (before any remediation)"""

    evaluated_response_tool_calls: Optional[List[EvaluatedResponseToolCall]] = None
    """Tool calls from the evaluated response, if any.

    Used to log tool calls in the query log.
    """

    expert_guardrail_override_explanation: Optional[str] = None
    """
    Explanation of why the response was either guardrailed or not guardrailed by
    expert review. Expert review will override the original guardrail decision.
    """

    expert_override_log_id: Optional[str] = None
    """
    ID of the query log with expert review that overrode the original guardrail
    decision.
    """

    expert_review_created_at: Optional[datetime] = None
    """When the expert review was created"""

    expert_review_created_by_user_id: Optional[str] = None
    """ID of the user who created the expert review"""

    expert_review_explanation: Optional[str] = None
    """Expert explanation when marked as bad"""

    expert_review_status: Optional[Literal["good", "bad"]] = None
    """Expert review status: 'good' or 'bad'"""

    guardrail_evals: Optional[List[str]] = None
    """Evals that should trigger guardrail"""

    guardrailed: Optional[bool] = None
    """If true, the response was guardrailed"""

    messages: Optional[List[Message]] = None
    """Message history to provide conversation context for the query.

    Used for TrustworthyRAG and to rewrite query into a self-contained version of
    itself.
    """

    original_assistant_response: Optional[str] = None
    """The original assistant response that would have been displayed to the user.

    This may be `None` if this is a tool call step.
    """

    original_question: Optional[str] = None
    """The original question that was asked before any rewriting or processing.

    For all non-conversational RAG, original_question should be the same as the
    final question seen in Codex.
    """

    primary_eval_issue: Optional[str] = None
    """Primary issue identified in evaluation"""

    primary_eval_issue_score: Optional[float] = None
    """Score of the primary eval issue"""

    tools: Optional[List[Tool]] = None
    """Tools to use for the LLM call.

    If not provided, it is assumed no tools were provided to the LLM.
    """
