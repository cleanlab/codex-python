# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Entry"]


class Entry(BaseModel):
    id: str

    created_at: datetime

    project_id: str

    question: str

    state: Literal["unanswered", "draft", "published", "published_with_draft"]

    answer: Optional[str] = None

    answered_at: Optional[datetime] = None

    client_query_metadata: Optional[List[object]] = None

    draft_answer: Optional[str] = None

    draft_answer_last_edited: Optional[datetime] = None
