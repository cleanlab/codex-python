# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ClusterListParams"]


class ClusterListParams(TypedDict, total=False):
    eval_issue_types: List[Literal["hallucination", "search_failure", "unhelpful"]]

    limit: int

    offset: int

    order: Literal["asc", "desc"]

    sort: Optional[Literal["created_at", "answered_at", "cluster_frequency_count", "custom_rank", "eval_score"]]

    states: List[Literal["unanswered", "draft", "published", "published_with_draft"]]
