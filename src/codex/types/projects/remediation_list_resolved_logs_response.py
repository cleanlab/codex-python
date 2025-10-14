# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "RemediationListResolvedLogsResponse",
    "QueryLog",
    "QueryLogFormattedEscalationEvalScores",
    "QueryLogFormattedEvalScores",
    "QueryLogFormattedGuardrailEvalScores",
    "QueryLogFormattedNonGuardrailEvalScores",
    "QueryLogContext",
    "QueryLogDeterministicGuardrailsResults",
    "QueryLogEvaluatedResponseToolCall",
    "QueryLogEvaluatedResponseToolCallFunction",
    "QueryLogMessage",
    "QueryLogMessageChatCompletionAssistantMessageParamOutput",
    "QueryLogMessageChatCompletionAssistantMessageParamOutputAudio",
    "QueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1",
    "QueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam",
    "QueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartRefusalParam",
    "QueryLogMessageChatCompletionAssistantMessageParamOutputFunctionCall",
    "QueryLogMessageChatCompletionAssistantMessageParamOutputToolCall",
    "QueryLogMessageChatCompletionAssistantMessageParamOutputToolCallFunction",
    "QueryLogMessageChatCompletionToolMessageParam",
    "QueryLogMessageChatCompletionToolMessageParamContentUnionMember1",
    "QueryLogMessageChatCompletionUserMessageParamOutput",
    "QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1",
    "QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam",
    "QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParam",
    "QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParamImageURL",
    "QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParam",
    "QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio",
    "QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1File",
    "QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1FileFile",
    "QueryLogMessageChatCompletionSystemMessageParam",
    "QueryLogMessageChatCompletionSystemMessageParamContentUnionMember1",
    "QueryLogMessageChatCompletionFunctionMessageParam",
    "QueryLogMessageChatCompletionDeveloperMessageParam",
    "QueryLogMessageChatCompletionDeveloperMessageParamContentUnionMember1",
    "QueryLogTool",
    "QueryLogToolFunction",
]


class QueryLogFormattedEscalationEvalScores(BaseModel):
    display_name: str

    score: float

    status: Literal["pass", "fail"]


class QueryLogFormattedEvalScores(BaseModel):
    display_name: str

    score: float

    status: Literal["pass", "fail"]


class QueryLogFormattedGuardrailEvalScores(BaseModel):
    display_name: str

    score: float

    status: Literal["pass", "fail"]


class QueryLogFormattedNonGuardrailEvalScores(BaseModel):
    display_name: str

    score: float

    status: Literal["pass", "fail"]


class QueryLogContext(BaseModel):
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


class QueryLogDeterministicGuardrailsResults(BaseModel):
    guardrail_name: str

    should_guardrail: bool

    fallback_message: Optional[str] = None

    matches: Optional[List[str]] = None


class QueryLogEvaluatedResponseToolCallFunction(BaseModel):
    arguments: str

    name: str


class QueryLogEvaluatedResponseToolCall(BaseModel):
    id: str

    function: QueryLogEvaluatedResponseToolCallFunction

    type: Literal["function"]


class QueryLogMessageChatCompletionAssistantMessageParamOutputAudio(BaseModel):
    id: str


class QueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam(
    BaseModel
):
    text: str

    type: Literal["text"]


class QueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartRefusalParam(
    BaseModel
):
    refusal: str

    type: Literal["refusal"]


QueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1: TypeAlias = Union[
    QueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam,
    QueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartRefusalParam,
]


class QueryLogMessageChatCompletionAssistantMessageParamOutputFunctionCall(BaseModel):
    arguments: str

    name: str


class QueryLogMessageChatCompletionAssistantMessageParamOutputToolCallFunction(BaseModel):
    arguments: str

    name: str


class QueryLogMessageChatCompletionAssistantMessageParamOutputToolCall(BaseModel):
    id: str

    function: QueryLogMessageChatCompletionAssistantMessageParamOutputToolCallFunction

    type: Literal["function"]


class QueryLogMessageChatCompletionAssistantMessageParamOutput(BaseModel):
    role: Literal["assistant"]

    audio: Optional[QueryLogMessageChatCompletionAssistantMessageParamOutputAudio] = None

    content: Union[str, List[QueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1], None] = None

    function_call: Optional[QueryLogMessageChatCompletionAssistantMessageParamOutputFunctionCall] = None

    name: Optional[str] = None

    refusal: Optional[str] = None

    tool_calls: Optional[List[QueryLogMessageChatCompletionAssistantMessageParamOutputToolCall]] = None


class QueryLogMessageChatCompletionToolMessageParamContentUnionMember1(BaseModel):
    text: str

    type: Literal["text"]


class QueryLogMessageChatCompletionToolMessageParam(BaseModel):
    content: Union[str, List[QueryLogMessageChatCompletionToolMessageParamContentUnionMember1]]

    role: Literal["tool"]

    tool_call_id: str


class QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam(
    BaseModel
):
    text: str

    type: Literal["text"]


class QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[Literal["auto", "low", "high"]] = None


class QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParam(
    BaseModel
):
    image_url: QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParamImageURL

    type: Literal["image_url"]


class QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio(
    BaseModel
):
    data: str

    format: Literal["wav", "mp3"]


class QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParam(
    BaseModel
):
    input_audio: QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio

    type: Literal["input_audio"]


class QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1FileFile(BaseModel):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    filename: Optional[str] = None


class QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1File(BaseModel):
    file: QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1FileFile

    type: Literal["file"]


QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1: TypeAlias = Union[
    QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam,
    QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParam,
    QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParam,
    QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1File,
]


class QueryLogMessageChatCompletionUserMessageParamOutput(BaseModel):
    content: Union[str, List[QueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1]]

    role: Literal["user"]

    name: Optional[str] = None


class QueryLogMessageChatCompletionSystemMessageParamContentUnionMember1(BaseModel):
    text: str

    type: Literal["text"]


class QueryLogMessageChatCompletionSystemMessageParam(BaseModel):
    content: Union[str, List[QueryLogMessageChatCompletionSystemMessageParamContentUnionMember1]]

    role: Literal["system"]

    name: Optional[str] = None


class QueryLogMessageChatCompletionFunctionMessageParam(BaseModel):
    content: Optional[str] = None

    name: str

    role: Literal["function"]


class QueryLogMessageChatCompletionDeveloperMessageParamContentUnionMember1(BaseModel):
    text: str

    type: Literal["text"]


class QueryLogMessageChatCompletionDeveloperMessageParam(BaseModel):
    content: Union[str, List[QueryLogMessageChatCompletionDeveloperMessageParamContentUnionMember1]]

    role: Literal["developer"]

    name: Optional[str] = None


QueryLogMessage: TypeAlias = Union[
    QueryLogMessageChatCompletionAssistantMessageParamOutput,
    QueryLogMessageChatCompletionToolMessageParam,
    QueryLogMessageChatCompletionUserMessageParamOutput,
    QueryLogMessageChatCompletionSystemMessageParam,
    QueryLogMessageChatCompletionFunctionMessageParam,
    QueryLogMessageChatCompletionDeveloperMessageParam,
]


class QueryLogToolFunction(BaseModel):
    name: str

    description: Optional[str] = None

    parameters: Optional[object] = None

    strict: Optional[bool] = None


class QueryLogTool(BaseModel):
    function: QueryLogToolFunction

    type: Literal["function"]


class QueryLog(BaseModel):
    id: str

    created_at: datetime

    formatted_escalation_eval_scores: Optional[Dict[str, QueryLogFormattedEscalationEvalScores]] = None

    formatted_eval_scores: Optional[Dict[str, QueryLogFormattedEvalScores]] = None
    """Format evaluation scores for frontend display with pass/fail status.

    Returns: Dictionary mapping eval keys to their formatted representation: {
    "eval_key": { "score": float, "status": "pass" | "fail" } } Returns None if
    eval_scores is None.
    """

    formatted_guardrail_eval_scores: Optional[Dict[str, QueryLogFormattedGuardrailEvalScores]] = None

    formatted_messages: Optional[str] = None

    formatted_non_guardrail_eval_scores: Optional[Dict[str, QueryLogFormattedNonGuardrailEvalScores]] = None

    formatted_original_question: Optional[str] = None

    is_bad_response: bool

    project_id: str

    question: str

    remediation_id: str

    tool_call_names: Optional[List[str]] = None

    was_cache_hit: Optional[bool] = None
    """If similar query already answered, or None if cache was not checked"""

    context: Optional[List[QueryLogContext]] = None
    """RAG context used for the query"""

    custom_metadata: Optional[object] = None
    """Arbitrary metadata supplied by the user/system"""

    custom_metadata_keys: Optional[List[str]] = None
    """Keys of the custom metadata"""

    deterministic_guardrails_results: Optional[Dict[str, QueryLogDeterministicGuardrailsResults]] = None
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

    evaluated_response_tool_calls: Optional[List[QueryLogEvaluatedResponseToolCall]] = None
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

    messages: Optional[List[QueryLogMessage]] = None
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

    tools: Optional[List[QueryLogTool]] = None
    """Tools to use for the LLM call.

    If not provided, it is assumed no tools were provided to the LLM.
    """


class RemediationListResolvedLogsResponse(BaseModel):
    query_logs: List[QueryLog]

    total_count: int
