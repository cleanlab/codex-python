# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TlmPromptResponse"]


class TlmPromptResponse(BaseModel):
    response: str

    trustworthiness_score: float

    log: Optional[object] = None
