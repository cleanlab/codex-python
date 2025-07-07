# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["ProjectValidateResponse", "DeterministicGuardrailsResults", "EvalScores"]


class DeterministicGuardrailsResults(BaseModel):
    guardrail_name: str

    should_guardrail: bool

    matches: Optional[List[str]] = None


class EvalScores(BaseModel):
    score: Optional[float] = None

    triggered: bool

    triggered_escalation: bool

    triggered_guardrail: bool

    failed: Optional[bool] = None

    log: Optional[object] = None


class ProjectValidateResponse(BaseModel):
    deterministic_guardrails_results: Optional[Dict[str, DeterministicGuardrailsResults]] = None
    """Results from deterministic guardrails applied to the response."""

    escalated_to_sme: bool
    """
    True if the question should be escalated to Codex for an SME to review, False
    otherwise. When True, a lookup is performed, which logs this query in the
    project for SMEs to answer, if it does not already exist.
    """

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

    should_guardrail: bool
    """
    True if the response should be guardrailed by the AI system, False if the
    response is okay to return to the user.
    """
