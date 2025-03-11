# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TlmScoreResponse"]


class TlmScoreResponse(BaseModel):
    trustworthiness_score: float

    log: Optional[object] = None
