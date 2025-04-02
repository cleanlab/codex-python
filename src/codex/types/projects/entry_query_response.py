# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["EntryQueryResponse", "Entry"]


class Entry(BaseModel):
    id: str

    question: str

    answer: Optional[str] = None

    draft_answer: Optional[str] = None


class EntryQueryResponse(BaseModel):
    entry: Entry

    answer: Optional[str] = None
