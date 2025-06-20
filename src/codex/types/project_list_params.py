# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ProjectListParams"]


class ProjectListParams(TypedDict, total=False):
    include_unaddressed_counts: bool

    limit: int

    offset: int

    order: Literal["asc", "desc"]

    organization_id: str

    query: Optional[str]

    sort: Literal["created_at", "updated_at"]
