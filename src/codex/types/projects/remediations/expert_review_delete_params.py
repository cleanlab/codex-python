# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ExpertReviewDeleteParams"]


class ExpertReviewDeleteParams(TypedDict, total=False):
    project_id: Required[str]

    original_query_log_id: Optional[str]
