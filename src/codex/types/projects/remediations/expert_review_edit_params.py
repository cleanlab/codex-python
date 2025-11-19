# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExpertReviewEditParams"]


class ExpertReviewEditParams(TypedDict, total=False):
    project_id: Required[str]

    explanation: Optional[str]

    review_status: Optional[Literal["good", "bad"]]
