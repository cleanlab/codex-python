# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ClusterListResponse"]


class ClusterListResponse(BaseModel):
    id: str

    cluster_frequency_count: int

    created_at: datetime

    project_id: str

    question: str

    state: Literal["unanswered", "draft", "published", "published_with_draft"]

    answer: Optional[str] = None

    answered_at: Optional[datetime] = None

    client_query_metadata: Optional[List[object]] = None

    draft_answer: Optional[str] = None

    draft_answer_last_edited: Optional[datetime] = None

    frequency_count: Optional[int] = None
    """number of times the entry matched for a /query request"""

    representative_entry_id: Optional[str] = None
