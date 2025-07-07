# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "QueryLogListGroupsResponse",
    "FormattedEscalationEvalScores",
    "FormattedEvalScores",
    "FormattedGuardrailEvalScores",
    "FormattedNonGuardrailEvalScores",
    "Context",
    "DeterministicGuardrailsResults",
]


class FormattedEscalationEvalScores(BaseModel):
    score: float

    status: Literal["pass", "fail"]


class FormattedEvalScores(BaseModel):
    score: float

    status: Literal["pass", "fail"]


class FormattedGuardrailEvalScores(BaseModel):
    score: float

    status: Literal["pass", "fail"]


class FormattedNonGuardrailEvalScores(BaseModel):
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

    matches: Optional[List[str]] = None


class QueryLogListGroupsResponse(BaseModel):
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

    formatted_non_guardrail_eval_scores: Optional[Dict[str, FormattedNonGuardrailEvalScores]] = None

    is_bad_response: bool

    needs_review: bool

    project_id: str

    question: str

    remediation_id: str

    remediation_status: Literal["ACTIVE", "DRAFT", "ACTIVE_WITH_DRAFT", "NOT_STARTED", "PAUSED", "NO_ACTION_NEEDED"]

    total_count: int

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

    eval_issue_labels: Optional[List[str]] = None
    """Labels derived from evaluation scores"""

    eval_scores: Optional[Dict[str, float]] = None
    """Evaluation scores for the original response"""

    eval_thresholds: Optional[Dict[str, Dict[str, Union[float, str]]]] = None
    """Evaluation thresholds and directions at time of creation"""

    evaluated_response: Optional[str] = None
    """The response being evaluated from the RAG system (before any remediation)"""

    guardrail_evals: Optional[List[str]] = None
    """Evals that should trigger guardrail"""

    guardrailed: Optional[bool] = None
    """If true, the response was guardrailed"""

    primary_eval_issue: Optional[str] = None
    """Primary issue identified in evaluation"""

    primary_eval_issue_score: Optional[float] = None
    """Score of the primary eval issue"""
