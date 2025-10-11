# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ProjectRetrieveAnalyticsResponse",
    "AnswersPublished",
    "AnswersPublishedAnswersByAuthor",
    "BadResponses",
    "BadResponsesResponsesByType",
    "Queries",
    "MetadataField",
]


class AnswersPublishedAnswersByAuthor(BaseModel):
    answers_published: int

    email: str

    name: str

    user_id: str


class AnswersPublished(BaseModel):
    answers_by_author: List[AnswersPublishedAnswersByAuthor]


class BadResponsesResponsesByType(BaseModel):
    num_prevented: int

    total: int


class BadResponses(BaseModel):
    responses_by_type: Dict[str, BadResponsesResponsesByType]

    total: int


class Queries(BaseModel):
    total: int


class MetadataField(BaseModel):
    field_type: Literal["select", "input"]
    """Field type: 'select' for checkbox selection, 'input' for text input"""

    key: str
    """Metadata field key"""

    values: Optional[List[Optional[str]]] = None
    """Possible values for this metadata field (None if more than 12 values).

    Array elements may include null to represent logs where the metadata key is
    missing or null.
    """


class ProjectRetrieveAnalyticsResponse(BaseModel):
    answers_published: AnswersPublished

    bad_responses: BadResponses

    queries: Queries

    metadata_fields: Optional[List[MetadataField]] = None
    """Available metadata fields for filtering"""
