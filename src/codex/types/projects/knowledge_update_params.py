# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["KnowledgeUpdateParams"]


class KnowledgeUpdateParams(TypedDict, total=False):
    project_id: Required[int]

    answer: Optional[str]

    question: Optional[str]
