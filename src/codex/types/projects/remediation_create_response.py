# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RemediationCreateResponse"]


class RemediationCreateResponse(BaseModel):
    id: str

    answered_at: Optional[datetime] = None

    answered_by: Optional[str] = None

    created_at: datetime

    last_edited_at: Optional[datetime] = None

    last_edited_by: Optional[str] = None

    project_id: str

    question: str

    status: Literal["ACTIVE", "DRAFT", "ACTIVE_WITH_DRAFT", "NOT_STARTED", "PAUSED"]

    answer: Optional[str] = None

    draft_answer: Optional[str] = None
