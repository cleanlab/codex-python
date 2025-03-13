# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["EntryListParams"]


class EntryListParams(TypedDict, total=False):
    answered_only: bool

    limit: int

    offset: int

    order: Literal["asc", "desc"]

    sort: Literal["created_at", "answered_at"]

    states: List[Literal["unanswered", "draft", "published", "published_with_draft"]]

    unanswered_only: bool
