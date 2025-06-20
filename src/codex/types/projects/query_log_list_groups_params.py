# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["QueryLogListGroupsParams"]


class QueryLogListGroupsParams(TypedDict, total=False):
    created_at_end: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter logs created at or before this timestamp"""

    created_at_start: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter logs created at or after this timestamp"""

    custom_metadata: Optional[str]
    """Filter by custom metadata as JSON string: {"key1": "value1", "key2": "value2"}"""

    limit: int

    offset: int

    order: Literal["asc", "desc"]

    primary_eval_issue: Optional[
        List[Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "unsupported"]]
    ]
    """Filter logs that have ANY of these primary evaluation issues (OR operation)"""

    sort: Optional[Literal["created_at", "primary_eval_issue_score", "total_count", "custom_rank"]]

    was_cache_hit: Optional[bool]
    """Filter by cache hit status"""
