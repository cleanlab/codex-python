# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EntryNotifySmeParams", "ViewContext"]


class EntryNotifySmeParams(TypedDict, total=False):
    project_id: Required[str]

    email: Required[str]

    view_context: Required[ViewContext]


class ViewContext(TypedDict, total=False):
    page: Required[int]

    filter: Literal[
        "unanswered",
        "answered",
        "all",
        "hallucination",
        "search_failure",
        "unhelpful",
        "difficult_query",
        "unsupported",
    ]
