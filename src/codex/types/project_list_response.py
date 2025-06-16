# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ProjectListResponse",
    "Project",
    "ProjectConfig",
    "ProjectConfigEvalConfig",
    "ProjectConfigEvalConfigCustomEvals",
    "ProjectConfigEvalConfigCustomEvalsEvals",
    "ProjectConfigEvalConfigDefaultEvals",
    "ProjectConfigEvalConfigDefaultEvalsContextSufficiency",
    "ProjectConfigEvalConfigDefaultEvalsQueryEase",
    "ProjectConfigEvalConfigDefaultEvalsResponseGroundedness",
    "ProjectConfigEvalConfigDefaultEvalsResponseHelpfulness",
    "ProjectConfigEvalConfigDefaultEvalsTrustworthiness",
]


class ProjectConfigEvalConfigCustomEvalsEvals(BaseModel):
    criteria: str
    """
    The evaluation criteria text that describes what aspect is being evaluated and
    how
    """

    eval_key: str
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: str
    """Display name/label for the evaluation metric"""

    context_identifier: Optional[str] = None
    """
    The exact string used in your evaluation criteria to reference the retrieved
    context.
    """

    enabled: Optional[bool] = None
    """Allows the evaluation to be disabled without removing it"""

    is_default: Optional[bool] = None
    """Whether the eval is a default, built-in eval or a custom eval"""

    priority: Optional[int] = None
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    query_identifier: Optional[str] = None
    """
    The exact string used in your evaluation criteria to reference the user's query.
    """

    response_identifier: Optional[str] = None
    """
    The exact string used in your evaluation criteria to reference the RAG/LLM
    response.
    """

    should_escalate: Optional[bool] = None
    """
    If true, failing this eval means the response is considered bad and can trigger
    escalation to Codex/SME
    """

    threshold: Optional[float] = None
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Optional[Literal["above", "below"]] = None
    """Whether the evaluation fails when score is above or below the threshold"""


class ProjectConfigEvalConfigCustomEvals(BaseModel):
    evals: Optional[Dict[str, ProjectConfigEvalConfigCustomEvalsEvals]] = None


class ProjectConfigEvalConfigDefaultEvalsContextSufficiency(BaseModel):
    eval_key: str
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: str
    """Display name/label for the evaluation metric"""

    enabled: Optional[bool] = None
    """Allows the evaluation to be disabled without removing it"""

    priority: Optional[int] = None
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    should_escalate: Optional[bool] = None
    """
    If true, failing this eval means the response is considered bad and can trigger
    escalation to Codex/SME
    """

    threshold: Optional[float] = None
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Optional[Literal["above", "below"]] = None
    """Whether the evaluation fails when score is above or below the threshold"""


class ProjectConfigEvalConfigDefaultEvalsQueryEase(BaseModel):
    eval_key: str
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: str
    """Display name/label for the evaluation metric"""

    enabled: Optional[bool] = None
    """Allows the evaluation to be disabled without removing it"""

    priority: Optional[int] = None
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    should_escalate: Optional[bool] = None
    """
    If true, failing this eval means the response is considered bad and can trigger
    escalation to Codex/SME
    """

    threshold: Optional[float] = None
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Optional[Literal["above", "below"]] = None
    """Whether the evaluation fails when score is above or below the threshold"""


class ProjectConfigEvalConfigDefaultEvalsResponseGroundedness(BaseModel):
    eval_key: str
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: str
    """Display name/label for the evaluation metric"""

    enabled: Optional[bool] = None
    """Allows the evaluation to be disabled without removing it"""

    priority: Optional[int] = None
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    should_escalate: Optional[bool] = None
    """
    If true, failing this eval means the response is considered bad and can trigger
    escalation to Codex/SME
    """

    threshold: Optional[float] = None
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Optional[Literal["above", "below"]] = None
    """Whether the evaluation fails when score is above or below the threshold"""


class ProjectConfigEvalConfigDefaultEvalsResponseHelpfulness(BaseModel):
    eval_key: str
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: str
    """Display name/label for the evaluation metric"""

    enabled: Optional[bool] = None
    """Allows the evaluation to be disabled without removing it"""

    priority: Optional[int] = None
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    should_escalate: Optional[bool] = None
    """
    If true, failing this eval means the response is considered bad and can trigger
    escalation to Codex/SME
    """

    threshold: Optional[float] = None
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Optional[Literal["above", "below"]] = None
    """Whether the evaluation fails when score is above or below the threshold"""


class ProjectConfigEvalConfigDefaultEvalsTrustworthiness(BaseModel):
    eval_key: str
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: str
    """Display name/label for the evaluation metric"""

    enabled: Optional[bool] = None
    """Allows the evaluation to be disabled without removing it"""

    priority: Optional[int] = None
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    should_escalate: Optional[bool] = None
    """
    If true, failing this eval means the response is considered bad and can trigger
    escalation to Codex/SME
    """

    threshold: Optional[float] = None
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Optional[Literal["above", "below"]] = None
    """Whether the evaluation fails when score is above or below the threshold"""


class ProjectConfigEvalConfigDefaultEvals(BaseModel):
    context_sufficiency: Optional[ProjectConfigEvalConfigDefaultEvalsContextSufficiency] = None
    """A pre-configured evaluation metric from TrustworthyRAG or built into the system.

    The evaluation criteria and identifiers are immutable and system-managed, while
    other properties like thresholds and priorities can be configured.
    """

    query_ease: Optional[ProjectConfigEvalConfigDefaultEvalsQueryEase] = None
    """A pre-configured evaluation metric from TrustworthyRAG or built into the system.

    The evaluation criteria and identifiers are immutable and system-managed, while
    other properties like thresholds and priorities can be configured.
    """

    response_groundedness: Optional[ProjectConfigEvalConfigDefaultEvalsResponseGroundedness] = None
    """A pre-configured evaluation metric from TrustworthyRAG or built into the system.

    The evaluation criteria and identifiers are immutable and system-managed, while
    other properties like thresholds and priorities can be configured.
    """

    response_helpfulness: Optional[ProjectConfigEvalConfigDefaultEvalsResponseHelpfulness] = None
    """A pre-configured evaluation metric from TrustworthyRAG or built into the system.

    The evaluation criteria and identifiers are immutable and system-managed, while
    other properties like thresholds and priorities can be configured.
    """

    trustworthiness: Optional[ProjectConfigEvalConfigDefaultEvalsTrustworthiness] = None
    """A pre-configured evaluation metric from TrustworthyRAG or built into the system.

    The evaluation criteria and identifiers are immutable and system-managed, while
    other properties like thresholds and priorities can be configured.
    """


class ProjectConfigEvalConfig(BaseModel):
    custom_evals: Optional[ProjectConfigEvalConfigCustomEvals] = None
    """Configuration for custom evaluation metrics."""

    default_evals: Optional[ProjectConfigEvalConfigDefaultEvals] = None
    """Configuration for default evaluation metrics."""


class ProjectConfig(BaseModel):
    clustering_use_llm_matching: Optional[bool] = None

    eval_config: Optional[ProjectConfigEvalConfig] = None
    """Configuration for project-specific evaluation metrics"""

    llm_matching_model: Optional[str] = None

    llm_matching_quality_preset: Optional[Literal["best", "high", "medium", "low", "base"]] = None

    lower_llm_match_distance_threshold: Optional[float] = None

    max_distance: Optional[float] = None

    query_use_llm_matching: Optional[bool] = None

    upper_llm_match_distance_threshold: Optional[float] = None


class Project(BaseModel):
    id: str

    config: ProjectConfig

    created_at: datetime

    created_by_user_id: str

    name: str

    organization_id: str

    updated_at: datetime

    auto_clustering_enabled: Optional[bool] = None

    description: Optional[str] = None

    unaddressed_count: Optional[int] = None


class ProjectListResponse(BaseModel):
    projects: List[Project]

    total_count: int
