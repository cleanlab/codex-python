# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Entry"]


class Entry(BaseModel):
    created_at: datetime

    question: str

    id: Optional[str] = None

    answer: Optional[str] = None

    answered_at: Optional[datetime] = None
