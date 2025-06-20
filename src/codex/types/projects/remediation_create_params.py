# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RemediationCreateParams"]


class RemediationCreateParams(TypedDict, total=False):
    question: Required[str]

    answer: Optional[str]

    draft_answer: Optional[str]
