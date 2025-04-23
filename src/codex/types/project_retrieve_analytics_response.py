# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = [
    "ProjectRetrieveAnalyticsResponse",
    "AnswersPublished",
    "AnswersPublishedAnswersByAuthor",
    "BadResponses",
    "Queries",
]


class AnswersPublishedAnswersByAuthor(BaseModel):
    answers_published: int

    name: str

    user_id: str


class AnswersPublished(BaseModel):
    answers_by_author: List[AnswersPublishedAnswersByAuthor]


class BadResponses(BaseModel):
    responses_by_type: Dict[str, int]

    total: int


class Queries(BaseModel):
    total: int


class ProjectRetrieveAnalyticsResponse(BaseModel):
    answers_published: AnswersPublished

    bad_responses: BadResponses

    queries: Queries
