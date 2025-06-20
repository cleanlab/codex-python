# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RemediationListResponse", "Remediation"]


class Remediation(BaseModel):
    id: str

    answered_at: Optional[datetime] = None

    answered_by: Optional[str] = None

    created_at: datetime

    last_edited_at: Optional[datetime] = None

    last_edited_by: Optional[str] = None

    project_id: str

    question: str

    resolved_logs_count: int

    status: Literal["ACTIVE", "DRAFT", "ACTIVE_WITH_DRAFT", "NOT_STARTED", "PAUSED"]

    answer: Optional[str] = None

    draft_answer: Optional[str] = None


class RemediationListResponse(BaseModel):
    remediations: List[Remediation]

    total_count: int
