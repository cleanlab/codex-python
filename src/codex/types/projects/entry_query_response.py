# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = [
    "EntryQueryResponse",
    "Entry",
    "EntryManagedMetadata",
    "EntryManagedMetadataContentStructureScores",
    "EntryManagedMetadataContextSufficiency",
    "EntryManagedMetadataHTMLFormatScores",
    "EntryManagedMetadataQueryEaseCustomized",
    "EntryManagedMetadataResponseGroundedness",
    "EntryManagedMetadataResponseHelpfulness",
    "EntryManagedMetadataTrustworthiness",
]


class EntryManagedMetadataContentStructureScores(BaseModel):
    average: Optional[float] = None
    """The average of all scores."""

    latest: Optional[float] = None
    """The most recent score."""

    max: Optional[float] = None
    """The maximum score."""

    min: Optional[float] = None
    """The minimum score."""

    scores: Optional[List[float]] = None


class EntryManagedMetadataContextSufficiency(BaseModel):
    average: Optional[float] = None
    """The average of all scores."""

    latest: Optional[float] = None
    """The most recent score."""

    max: Optional[float] = None
    """The maximum score."""

    min: Optional[float] = None
    """The minimum score."""

    scores: Optional[List[float]] = None


class EntryManagedMetadataHTMLFormatScores(BaseModel):
    average: Optional[float] = None
    """The average of all scores."""

    latest: Optional[float] = None
    """The most recent score."""

    max: Optional[float] = None
    """The maximum score."""

    min: Optional[float] = None
    """The minimum score."""

    scores: Optional[List[float]] = None


class EntryManagedMetadataQueryEaseCustomized(BaseModel):
    average: Optional[float] = None
    """The average of all scores."""

    latest: Optional[float] = None
    """The most recent score."""

    max: Optional[float] = None
    """The maximum score."""

    min: Optional[float] = None
    """The minimum score."""

    scores: Optional[List[float]] = None


class EntryManagedMetadataResponseGroundedness(BaseModel):
    average: Optional[float] = None
    """The average of all scores."""

    latest: Optional[float] = None
    """The most recent score."""

    max: Optional[float] = None
    """The maximum score."""

    min: Optional[float] = None
    """The minimum score."""

    scores: Optional[List[float]] = None


class EntryManagedMetadataResponseHelpfulness(BaseModel):
    average: Optional[float] = None
    """The average of all scores."""

    latest: Optional[float] = None
    """The most recent score."""

    max: Optional[float] = None
    """The maximum score."""

    min: Optional[float] = None
    """The minimum score."""

    scores: Optional[List[float]] = None


class EntryManagedMetadataTrustworthiness(BaseModel):
    average: Optional[float] = None
    """The average of all scores."""

    latest: Optional[float] = None
    """The most recent score."""

    max: Optional[float] = None
    """The maximum score."""

    min: Optional[float] = None
    """The minimum score."""

    scores: Optional[List[float]] = None


class EntryManagedMetadata(BaseModel):
    latest_context: Optional[str] = None
    """The most recent context string."""

    latest_entry_point: Optional[str] = None
    """The most recent entry point string."""

    latest_llm_response: Optional[str] = None
    """The most recent LLM response string."""

    latest_location: Optional[str] = None
    """The most recent location string."""

    content_structure_scores: Optional[EntryManagedMetadataContentStructureScores] = None
    """Holds a list of scores and computes aggregate statistics."""

    context_sufficiency: Optional[EntryManagedMetadataContextSufficiency] = None
    """Holds a list of scores and computes aggregate statistics."""

    contexts: Optional[List[str]] = None

    entry_points: Optional[List[str]] = None

    html_format_scores: Optional[EntryManagedMetadataHTMLFormatScores] = None
    """Holds a list of scores and computes aggregate statistics."""

    llm_responses: Optional[List[str]] = None

    locations: Optional[List[str]] = None

    query_ease_customized: Optional[EntryManagedMetadataQueryEaseCustomized] = None
    """Holds a list of scores and computes aggregate statistics."""

    response_groundedness: Optional[EntryManagedMetadataResponseGroundedness] = None
    """Holds a list of scores and computes aggregate statistics."""

    response_helpfulness: Optional[EntryManagedMetadataResponseHelpfulness] = None
    """Holds a list of scores and computes aggregate statistics."""

    trustworthiness: Optional[EntryManagedMetadataTrustworthiness] = None
    """Holds a list of scores and computes aggregate statistics."""


class Entry(BaseModel):
    id: str

    managed_metadata: EntryManagedMetadata
    """Extract system-defined, managed metadata from client_query_metadata."""

    question: str

    answer: Optional[str] = None

    client_query_metadata: Optional[List[object]] = None

    draft_answer: Optional[str] = None


class EntryQueryResponse(BaseModel):
    entry: Entry

    answer: Optional[str] = None
