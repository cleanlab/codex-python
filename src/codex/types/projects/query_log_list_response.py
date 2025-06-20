# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["QueryLogListResponse", "QueryLog", "QueryLogContext"]


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


class QueryLog(BaseModel):
    id: str

    created_at: datetime

    formatted_eval_scores: Optional[Dict[str, Dict[str, Union[float, Literal["pass", "fail"]]]]] = None
    """Format evaluation scores for frontend display with pass/fail status.

    Returns: Dictionary mapping eval keys to their formatted representation: {
    "eval_key": { "score": float, "status": "pass" | "fail" } } Returns None if
    eval_scores is None.
    """

    is_bad_response: bool
    """If an eval with should_escalate=True failed"""

    project_id: str

    question: str

    remediation_id: str

    was_cache_hit: Optional[bool] = None
    """If similar query already answered, or None if cache was not checked"""

    context: Optional[List[QueryLogContext]] = None
    """RAG context used for the query"""

    custom_metadata: Optional[object] = None
    """Arbitrary metadata supplied by the user/system"""

    custom_metadata_keys: Optional[List[str]] = None
    """Keys of the custom metadata"""

    eval_issue_labels: Optional[List[str]] = None
    """Labels derived from evaluation scores"""

    eval_scores: Optional[Dict[str, float]] = None
    """Evaluation scores for the original response"""

    eval_thresholds: Optional[Dict[str, Dict[str, Union[float, str]]]] = None
    """Evaluation thresholds and directions at time of creation"""

    evaluated_response: Optional[str] = None
    """The response being evaluated from the RAG system (before any remediation)"""

    primary_eval_issue: Optional[str] = None
    """Primary issue identified in evaluation"""

    primary_eval_issue_score: Optional[float] = None
    """Score of the primary eval issue"""


class QueryLogListResponse(BaseModel):
    custom_metadata_columns: List[str]

    query_logs: List[QueryLog]

    total_count: int
