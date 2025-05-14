# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ProjectValidateResponse", "EvalScores"]


class EvalScores(BaseModel):
    failed: bool

    score: Optional[float] = None

    log: Optional[object] = None


class ProjectValidateResponse(BaseModel):
    eval_scores: Dict[str, EvalScores]
    """
    Evaluation scores for the original response along with a boolean flag, `failed`,
    indicating whether the score is below the threshold.
    """

    expert_answer: Optional[str] = None
    """
    Alternate SME-provided answer from Codex if the response was flagged as bad and
    an answer was found in the Codex Project, or None otherwise.
    """

    is_bad_response: bool
    """True if the response is flagged as potentially bad, False otherwise.

    When True, a lookup is performed, which logs this query in the project for SMEs
    to answer, if it does not already exist.
    """
