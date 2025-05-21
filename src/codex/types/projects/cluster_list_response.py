# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "ClusterListResponse",
    "ManagedMetadata",
    "ManagedMetadataContentStructureScores",
    "ManagedMetadataContextSufficiency",
    "ManagedMetadataHTMLFormatScores",
    "ManagedMetadataQueryEaseCustomized",
    "ManagedMetadataResponseGroundedness",
    "ManagedMetadataResponseHelpfulness",
    "ManagedMetadataTrustworthiness",
]


class ManagedMetadataContentStructureScores(BaseModel):
    average: Optional[float] = None
    """The average of all scores."""

    latest: Optional[float] = None
    """The most recent score."""

    max: Optional[float] = None
    """The maximum score."""

    min: Optional[float] = None
    """The minimum score."""

    scores: Optional[List[float]] = None


class ManagedMetadataContextSufficiency(BaseModel):
    average: Optional[float] = None
    """The average of all scores."""

    latest: Optional[float] = None
    """The most recent score."""

    max: Optional[float] = None
    """The maximum score."""

    min: Optional[float] = None
    """The minimum score."""

    scores: Optional[List[float]] = None


class ManagedMetadataHTMLFormatScores(BaseModel):
    average: Optional[float] = None
    """The average of all scores."""

    latest: Optional[float] = None
    """The most recent score."""

    max: Optional[float] = None
    """The maximum score."""

    min: Optional[float] = None
    """The minimum score."""

    scores: Optional[List[float]] = None


class ManagedMetadataQueryEaseCustomized(BaseModel):
    average: Optional[float] = None
    """The average of all scores."""

    latest: Optional[float] = None
    """The most recent score."""

    max: Optional[float] = None
    """The maximum score."""

    min: Optional[float] = None
    """The minimum score."""

    scores: Optional[List[float]] = None


class ManagedMetadataResponseGroundedness(BaseModel):
    average: Optional[float] = None
    """The average of all scores."""

    latest: Optional[float] = None
    """The most recent score."""

    max: Optional[float] = None
    """The maximum score."""

    min: Optional[float] = None
    """The minimum score."""

    scores: Optional[List[float]] = None


class ManagedMetadataResponseHelpfulness(BaseModel):
    average: Optional[float] = None
    """The average of all scores."""

    latest: Optional[float] = None
    """The most recent score."""

    max: Optional[float] = None
    """The maximum score."""

    min: Optional[float] = None
    """The minimum score."""

    scores: Optional[List[float]] = None


class ManagedMetadataTrustworthiness(BaseModel):
    average: Optional[float] = None
    """The average of all scores."""

    latest: Optional[float] = None
    """The most recent score."""

    max: Optional[float] = None
    """The maximum score."""

    min: Optional[float] = None
    """The minimum score."""

    scores: Optional[List[float]] = None


class ManagedMetadata(BaseModel):
    latest_context: Optional[str] = None
    """The most recent context string."""

    latest_entry_point: Optional[str] = None
    """The most recent entry point string."""

    latest_llm_response: Optional[str] = None
    """The most recent LLM response string."""

    latest_location: Optional[str] = None
    """The most recent location string."""

    content_structure_scores: Optional[ManagedMetadataContentStructureScores] = None
    """Holds a list of scores and computes aggregate statistics."""

    context_sufficiency: Optional[ManagedMetadataContextSufficiency] = None
    """Holds a list of scores and computes aggregate statistics."""

    contexts: Optional[List[str]] = None

    entry_points: Optional[List[str]] = None

    html_format_scores: Optional[ManagedMetadataHTMLFormatScores] = None
    """Holds a list of scores and computes aggregate statistics."""

    llm_responses: Optional[List[str]] = None

    locations: Optional[List[str]] = None

    query_ease_customized: Optional[ManagedMetadataQueryEaseCustomized] = None
    """Holds a list of scores and computes aggregate statistics."""

    response_groundedness: Optional[ManagedMetadataResponseGroundedness] = None
    """Holds a list of scores and computes aggregate statistics."""

    response_helpfulness: Optional[ManagedMetadataResponseHelpfulness] = None
    """Holds a list of scores and computes aggregate statistics."""

    trustworthiness: Optional[ManagedMetadataTrustworthiness] = None
    """Holds a list of scores and computes aggregate statistics."""


class ClusterListResponse(BaseModel):
    id: str

    cluster_frequency_count: int

    created_at: datetime

    managed_metadata: ManagedMetadata
    """Extract system-defined, managed metadata from client_query_metadata."""

    project_id: str

    question: str

    state: Literal["unanswered", "draft", "published", "published_with_draft"]

    answer: Optional[str] = None

    answered_at: Optional[datetime] = None

    client_query_metadata: Optional[List[object]] = None

    content_structure_score: Optional[float] = None

    draft_answer: Optional[str] = None

    draft_answer_last_edited: Optional[datetime] = None

    eval_issue_type: Optional[str] = None

    eval_score: Optional[float] = None

    frequency_count: Optional[int] = None
    """number of times the entry matched for a /query request"""

    html_format_score: Optional[float] = None

    representative_entry_id: Optional[str] = None
