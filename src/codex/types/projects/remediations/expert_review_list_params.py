# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ExpertReviewListParams"]


class ExpertReviewListParams(TypedDict, total=False):
    created_at_end: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter expert reviews created at or before this timestamp"""

    created_at_start: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter expert reviews created at or after this timestamp"""

    last_edited_at_end: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter expert reviews last edited at or before this timestamp"""

    last_edited_at_start: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter expert reviews last edited at or after this timestamp"""

    last_edited_by: Optional[str]
    """Filter expert reviews last edited by user ID"""

    limit: int

    offset: int

    order: Literal["asc", "desc"]
    """Sort order"""

    review_status: Optional[List[Literal["good", "bad"]]]
    """Filter expert reviews by review status"""

    sort: Optional[Literal["created_at", "last_edited_at", "resolved_logs_count"]]
    """Sort expert reviews by field"""
