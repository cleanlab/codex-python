# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = [
    "ProjectRetrieveAnalyticsResponse",
    "AnswersPublished",
    "AnswersPublishedAnswersByAuthor",
    "BadResponses",
    "BadResponsesResponsesByType",
    "Queries",
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


class ProjectRetrieveAnalyticsResponse(BaseModel):
    answers_published: AnswersPublished

    bad_responses: BadResponses

    queries: Queries
