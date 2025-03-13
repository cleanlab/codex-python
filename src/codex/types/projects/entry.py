# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Entry"]


class Entry(BaseModel):
    created_at: datetime

    question: str

    state: Literal["unanswered", "draft", "published", "published_with_draft"]

    id: Optional[str] = None

    answer: Optional[str] = None

    answered_at: Optional[datetime] = None

    draft_answer: Optional[str] = None

    draft_answer_last_edited: Optional[datetime] = None

    frequency_count: Optional[int] = None
