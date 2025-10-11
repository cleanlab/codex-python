# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ProjectRetrieveAnalyticsParams"]


class ProjectRetrieveAnalyticsParams(TypedDict, total=False):
    end: Optional[int]
    """Filter logs created at or before this timestamp (epoch seconds).

    Can be used alone for upper-bound filtering.
    """

    metadata_filters: Optional[str]
    """Metadata filters as JSON string.

    Examples: - Single value: '{"department": "Engineering"}' - Multiple values:
    '{"priority": ["high", "medium"]}' - Null/missing values: '{"department": []}'
    or '{"department": [null]}' - Mixed values: '{"status": ["active", null,
    "pending"]}'
    """

    start: Optional[int]
    """Filter logs created at or after this timestamp (epoch seconds).

    Can be used alone for lower-bound filtering.
    """
