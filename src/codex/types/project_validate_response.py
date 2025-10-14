# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["ProjectValidateResponse", "DeterministicGuardrailsResults", "EvalScores"]


class DeterministicGuardrailsResults(BaseModel):
    guardrail_name: str

    should_guardrail: bool

    fallback_message: Optional[str] = None

    matches: Optional[List[str]] = None


class EvalScores(BaseModel):
    guardrailed_fallback_message: Optional[str] = None

    score: Optional[float] = None

    triggered: bool

    triggered_escalation: bool

    triggered_guardrail: bool

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
    Alternate SME-provided answer from Codex if a relevant answer was found in the
    Codex Project, or None otherwise.
    """

    expert_guardrail_override_explanation: Optional[str] = None
    """
    Explanation of why the response was either guardrailed or not guardrailed by
    expert review. Expert review will override the original guardrail decision.
    """

    log_id: str
    """The UUID of the query log entry created for this validation request."""

    should_guardrail: bool
    """
    True if the response should be guardrailed by the AI system, False if the
    response is okay to return to the user.
    """
