# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProjectListParams"]


class ProjectListParams(TypedDict, total=False):
    organization_id: Required[str]

    include_entry_counts: bool

    limit: int

    offset: int

    order: Literal["asc", "desc"]

    query: Optional[str]

    sort: Literal["created_at", "updated_at"]
