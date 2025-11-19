# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExpertReviewCreateParams"]


class ExpertReviewCreateParams(TypedDict, total=False):
    original_query_log_id: Required[str]
    """ID of the original query log"""

    review_status: Required[Literal["good", "bad"]]
    """Expert review status - 'good' or 'bad'"""

    generate_guidance: bool

    explanation: Optional[str]
    """Optional explanation for expert review"""
