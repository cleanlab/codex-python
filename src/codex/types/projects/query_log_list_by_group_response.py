# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "QueryLogListByGroupResponse",
    "QueryLogsByGroup",
    "QueryLogsByGroupQueryLog",
    "QueryLogsByGroupQueryLogFormattedEscalationEvalScores",
    "QueryLogsByGroupQueryLogFormattedEvalScores",
    "QueryLogsByGroupQueryLogFormattedGuardrailEvalScores",
    "QueryLogsByGroupQueryLogFormattedNonGuardrailEvalScores",
    "QueryLogsByGroupQueryLogContext",
    "QueryLogsByGroupQueryLogDeterministicGuardrailsResults",
    "QueryLogsByGroupQueryLogEvaluatedResponseToolCall",
    "QueryLogsByGroupQueryLogEvaluatedResponseToolCallFunction",
    "QueryLogsByGroupQueryLogMessage",
    "QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutput",
    "QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputAudio",
    "QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1",
    "QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam",
    "QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartRefusalParam",
    "QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputFunctionCall",
    "QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputToolCall",
    "QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputToolCallFunction",
    "QueryLogsByGroupQueryLogMessageChatCompletionToolMessageParam",
    "QueryLogsByGroupQueryLogMessageChatCompletionToolMessageParamContentUnionMember1",
    "QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutput",
    "QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1",
    "QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam",
    "QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParam",
    "QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParamImageURL",
    "QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParam",
    "QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio",
    "QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1File",
    "QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1FileFile",
    "QueryLogsByGroupQueryLogMessageChatCompletionSystemMessageParam",
    "QueryLogsByGroupQueryLogMessageChatCompletionSystemMessageParamContentUnionMember1",
    "QueryLogsByGroupQueryLogMessageChatCompletionFunctionMessageParam",
    "QueryLogsByGroupQueryLogMessageChatCompletionDeveloperMessageParam",
    "QueryLogsByGroupQueryLogMessageChatCompletionDeveloperMessageParamContentUnionMember1",
    "QueryLogsByGroupQueryLogTool",
    "QueryLogsByGroupQueryLogToolFunction",
]


class QueryLogsByGroupQueryLogFormattedEscalationEvalScores(BaseModel):
    score: float

    status: Literal["pass", "fail"]


class QueryLogsByGroupQueryLogFormattedEvalScores(BaseModel):
    score: float

    status: Literal["pass", "fail"]


class QueryLogsByGroupQueryLogFormattedGuardrailEvalScores(BaseModel):
    score: float

    status: Literal["pass", "fail"]


class QueryLogsByGroupQueryLogFormattedNonGuardrailEvalScores(BaseModel):
    score: float

    status: Literal["pass", "fail"]


class QueryLogsByGroupQueryLogContext(BaseModel):
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


class QueryLogsByGroupQueryLogDeterministicGuardrailsResults(BaseModel):
    guardrail_name: str

    should_guardrail: bool

    matches: Optional[List[str]] = None


class QueryLogsByGroupQueryLogEvaluatedResponseToolCallFunction(BaseModel):
    arguments: str

    name: str


class QueryLogsByGroupQueryLogEvaluatedResponseToolCall(BaseModel):
    id: str

    function: QueryLogsByGroupQueryLogEvaluatedResponseToolCallFunction

    type: Literal["function"]


class QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputAudio(BaseModel):
    id: str


class QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam(
    BaseModel
):
    text: str

    type: Literal["text"]


class QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartRefusalParam(
    BaseModel
):
    refusal: str

    type: Literal["refusal"]


QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1: TypeAlias = Union[
    QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam,
    QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1ChatCompletionContentPartRefusalParam,
]


class QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputFunctionCall(BaseModel):
    arguments: str

    name: str


class QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputToolCallFunction(BaseModel):
    arguments: str

    name: str


class QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputToolCall(BaseModel):
    id: str

    function: QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputToolCallFunction

    type: Literal["function"]


class QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutput(BaseModel):
    role: Literal["assistant"]

    audio: Optional[QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputAudio] = None

    content: Union[
        str, List[QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputContentUnionMember1], None
    ] = None

    function_call: Optional[QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputFunctionCall] = None

    name: Optional[str] = None

    refusal: Optional[str] = None

    tool_calls: Optional[List[QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutputToolCall]] = None


class QueryLogsByGroupQueryLogMessageChatCompletionToolMessageParamContentUnionMember1(BaseModel):
    text: str

    type: Literal["text"]


class QueryLogsByGroupQueryLogMessageChatCompletionToolMessageParam(BaseModel):
    content: Union[str, List[QueryLogsByGroupQueryLogMessageChatCompletionToolMessageParamContentUnionMember1]]

    role: Literal["tool"]

    tool_call_id: str


class QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam(
    BaseModel
):
    text: str

    type: Literal["text"]


class QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[Literal["auto", "low", "high"]] = None


class QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParam(
    BaseModel
):
    image_url: QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParamImageURL

    type: Literal["image_url"]


class QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio(
    BaseModel
):
    data: str

    format: Literal["wav", "mp3"]


class QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParam(
    BaseModel
):
    input_audio: QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio

    type: Literal["input_audio"]


class QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1FileFile(BaseModel):
    file_data: Optional[str] = None

    file_id: Optional[str] = None

    filename: Optional[str] = None


class QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1File(BaseModel):
    file: QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1FileFile

    type: Literal["file"]


QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1: TypeAlias = Union[
    QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartTextParam,
    QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartImageParam,
    QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1ChatCompletionContentPartInputAudioParam,
    QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1File,
]


class QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutput(BaseModel):
    content: Union[str, List[QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutputContentUnionMember1]]

    role: Literal["user"]

    name: Optional[str] = None


class QueryLogsByGroupQueryLogMessageChatCompletionSystemMessageParamContentUnionMember1(BaseModel):
    text: str

    type: Literal["text"]


class QueryLogsByGroupQueryLogMessageChatCompletionSystemMessageParam(BaseModel):
    content: Union[str, List[QueryLogsByGroupQueryLogMessageChatCompletionSystemMessageParamContentUnionMember1]]

    role: Literal["system"]

    name: Optional[str] = None


class QueryLogsByGroupQueryLogMessageChatCompletionFunctionMessageParam(BaseModel):
    content: Optional[str] = None

    name: str

    role: Literal["function"]


class QueryLogsByGroupQueryLogMessageChatCompletionDeveloperMessageParamContentUnionMember1(BaseModel):
    text: str

    type: Literal["text"]


class QueryLogsByGroupQueryLogMessageChatCompletionDeveloperMessageParam(BaseModel):
    content: Union[str, List[QueryLogsByGroupQueryLogMessageChatCompletionDeveloperMessageParamContentUnionMember1]]

    role: Literal["developer"]

    name: Optional[str] = None


QueryLogsByGroupQueryLogMessage: TypeAlias = Union[
    QueryLogsByGroupQueryLogMessageChatCompletionAssistantMessageParamOutput,
    QueryLogsByGroupQueryLogMessageChatCompletionToolMessageParam,
    QueryLogsByGroupQueryLogMessageChatCompletionUserMessageParamOutput,
    QueryLogsByGroupQueryLogMessageChatCompletionSystemMessageParam,
    QueryLogsByGroupQueryLogMessageChatCompletionFunctionMessageParam,
    QueryLogsByGroupQueryLogMessageChatCompletionDeveloperMessageParam,
]


class QueryLogsByGroupQueryLogToolFunction(BaseModel):
    name: str

    description: Optional[str] = None

    parameters: Optional[object] = None

    strict: Optional[bool] = None


class QueryLogsByGroupQueryLogTool(BaseModel):
    function: QueryLogsByGroupQueryLogToolFunction

    type: Literal["function"]


class QueryLogsByGroupQueryLog(BaseModel):
    id: str

    created_at: datetime

    formatted_escalation_eval_scores: Optional[Dict[str, QueryLogsByGroupQueryLogFormattedEscalationEvalScores]] = None

    formatted_eval_scores: Optional[Dict[str, QueryLogsByGroupQueryLogFormattedEvalScores]] = None
    """Format evaluation scores for frontend display with pass/fail status.

    Returns: Dictionary mapping eval keys to their formatted representation: {
    "eval_key": { "score": float, "status": "pass" | "fail" } } Returns None if
    eval_scores is None.
    """

    formatted_guardrail_eval_scores: Optional[Dict[str, QueryLogsByGroupQueryLogFormattedGuardrailEvalScores]] = None

    formatted_messages: Optional[str] = None

    formatted_non_guardrail_eval_scores: Optional[
        Dict[str, QueryLogsByGroupQueryLogFormattedNonGuardrailEvalScores]
    ] = None

    formatted_original_question: Optional[str] = None

    is_bad_response: bool

    needs_review: bool

    project_id: str

    question: str

    remediation_id: str

    remediation_status: Literal["ACTIVE", "DRAFT", "ACTIVE_WITH_DRAFT", "NOT_STARTED", "PAUSED", "NO_ACTION_NEEDED"]

    was_cache_hit: Optional[bool] = None
    """If similar query already answered, or None if cache was not checked"""

    context: Optional[List[QueryLogsByGroupQueryLogContext]] = None
    """RAG context used for the query"""

    custom_metadata: Optional[object] = None
    """Arbitrary metadata supplied by the user/system"""

    custom_metadata_keys: Optional[List[str]] = None
    """Keys of the custom metadata"""

    deterministic_guardrails_results: Optional[Dict[str, QueryLogsByGroupQueryLogDeterministicGuardrailsResults]] = None
    """Results of deterministic guardrails applied to the query"""

    escalated: Optional[bool] = None
    """If true, the question was escalated to Codex for an SME to review"""

    escalation_evals: Optional[List[str]] = None
    """Evals that should trigger escalation to SME"""

    eval_issue_labels: Optional[List[str]] = None
    """Labels derived from evaluation scores"""

    eval_scores: Optional[Dict[str, float]] = None
    """Evaluation scores for the original response"""

    eval_thresholds: Optional[Dict[str, Dict[str, Union[float, str]]]] = None
    """Evaluation thresholds and directions at time of creation"""

    evaluated_response: Optional[str] = None
    """The response being evaluated from the RAG system (before any remediation)"""

    evaluated_response_tool_calls: Optional[List[QueryLogsByGroupQueryLogEvaluatedResponseToolCall]] = None
    """Tool calls from the evaluated response, if any.

    Used to log tool calls in the query log.
    """

    guardrail_evals: Optional[List[str]] = None
    """Evals that should trigger guardrail"""

    guardrailed: Optional[bool] = None
    """If true, the response was guardrailed"""

    messages: Optional[List[QueryLogsByGroupQueryLogMessage]] = None
    """Message history to provide conversation context for the query.

    Used for TrustworthyRAG and to rewrite query into a self-contained version of
    itself.
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

    tools: Optional[List[QueryLogsByGroupQueryLogTool]] = None
    """Tools to use for the LLM call.

    If not provided, it is assumed no tools were provided to the LLM.
    """


class QueryLogsByGroup(BaseModel):
    query_logs: List[QueryLogsByGroupQueryLog]

    total_count: int


class QueryLogListByGroupResponse(BaseModel):
    custom_metadata_columns: List[str]

    query_logs_by_group: Dict[str, QueryLogsByGroup]
