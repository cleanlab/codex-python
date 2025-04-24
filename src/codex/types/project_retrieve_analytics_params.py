# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProjectRetrieveAnalyticsParams"]


class ProjectRetrieveAnalyticsParams(TypedDict, total=False):
    end: int
    """End timestamp in seconds since epoch"""

    start: int
    """Start timestamp in seconds since epoch"""
