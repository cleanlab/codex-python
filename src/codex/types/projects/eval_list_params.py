# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["EvalListParams"]


class EvalListParams(TypedDict, total=False):
    guardrails_only: bool

    limit: Optional[int]

    offset: int
