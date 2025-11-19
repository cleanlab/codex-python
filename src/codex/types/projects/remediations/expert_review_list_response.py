# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ExpertReviewListResponse"]


class ExpertReviewListResponse(BaseModel):
    id: str

    created_at: datetime

    evaluated_response: Optional[str] = None

    last_edited_at: datetime

    last_edited_by: Optional[str] = None

    project_id: str

    query: str

    resolved_logs_count: int

    review_status: Literal["good", "bad"]
    """Expert review status - 'good' or 'bad'"""

    deleted_at: Optional[datetime] = None

    explanation: Optional[str] = None
    """Optional explanation for expert review"""
