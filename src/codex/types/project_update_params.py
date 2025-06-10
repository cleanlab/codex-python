# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "ProjectUpdateParams",
    "Config",
    "ConfigEvalConfig",
    "ConfigEvalConfigCustomEvals",
    "ConfigEvalConfigCustomEvalsEvals",
    "ConfigEvalConfigDefaultEvals",
    "ConfigEvalConfigDefaultEvalsContextSufficiency",
    "ConfigEvalConfigDefaultEvalsQueryEase",
    "ConfigEvalConfigDefaultEvalsResponseGroundedness",
    "ConfigEvalConfigDefaultEvalsResponseHelpfulness",
    "ConfigEvalConfigDefaultEvalsTrustworthiness",
]


class ProjectUpdateParams(TypedDict, total=False):
    config: Required[Config]

    name: Required[str]

    auto_clustering_enabled: bool

    description: Optional[str]


class ConfigEvalConfigCustomEvalsEvals(TypedDict, total=False):
    criteria: Required[str]
    """
    The evaluation criteria text that describes what aspect is being evaluated and
    how
    """

    eval_key: Required[str]
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: Required[str]
    """Display name/label for the evaluation metric"""

    context_identifier: Optional[str]
    """
    The exact string used in your evaluation criteria to reference the retrieved
    context.
    """

    enabled: bool
    """Allows the evaluation to be disabled without removing it"""

    is_default: bool
    """Whether the eval is a default, built-in eval or a custom eval"""

    priority: Optional[int]
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    query_identifier: Optional[str]
    """
    The exact string used in your evaluation criteria to reference the user's query.
    """

    response_identifier: Optional[str]
    """
    The exact string used in your evaluation criteria to reference the RAG/LLM
    response.
    """

    should_escalate: bool
    """
    If true, failing this eval means the response is considered bad and can trigger
    escalation to Codex/SME
    """

    threshold: float
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Literal["above", "below"]
    """Whether the evaluation fails when score is above or below the threshold"""


class ConfigEvalConfigCustomEvals(TypedDict, total=False):
    evals: Dict[str, ConfigEvalConfigCustomEvalsEvals]


class ConfigEvalConfigDefaultEvalsContextSufficiency(TypedDict, total=False):
    eval_key: Required[str]
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: Required[str]
    """Display name/label for the evaluation metric"""

    enabled: bool
    """Allows the evaluation to be disabled without removing it"""

    priority: Optional[int]
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    should_escalate: bool
    """
    If true, failing this eval means the response is considered bad and can trigger
    escalation to Codex/SME
    """

    threshold: float
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Literal["above", "below"]
    """Whether the evaluation fails when score is above or below the threshold"""


class ConfigEvalConfigDefaultEvalsQueryEase(TypedDict, total=False):
    eval_key: Required[str]
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: Required[str]
    """Display name/label for the evaluation metric"""

    enabled: bool
    """Allows the evaluation to be disabled without removing it"""

    priority: Optional[int]
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    should_escalate: bool
    """
    If true, failing this eval means the response is considered bad and can trigger
    escalation to Codex/SME
    """

    threshold: float
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Literal["above", "below"]
    """Whether the evaluation fails when score is above or below the threshold"""


class ConfigEvalConfigDefaultEvalsResponseGroundedness(TypedDict, total=False):
    eval_key: Required[str]
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: Required[str]
    """Display name/label for the evaluation metric"""

    enabled: bool
    """Allows the evaluation to be disabled without removing it"""

    priority: Optional[int]
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    should_escalate: bool
    """
    If true, failing this eval means the response is considered bad and can trigger
    escalation to Codex/SME
    """

    threshold: float
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Literal["above", "below"]
    """Whether the evaluation fails when score is above or below the threshold"""


class ConfigEvalConfigDefaultEvalsResponseHelpfulness(TypedDict, total=False):
    eval_key: Required[str]
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: Required[str]
    """Display name/label for the evaluation metric"""

    enabled: bool
    """Allows the evaluation to be disabled without removing it"""

    priority: Optional[int]
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    should_escalate: bool
    """
    If true, failing this eval means the response is considered bad and can trigger
    escalation to Codex/SME
    """

    threshold: float
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Literal["above", "below"]
    """Whether the evaluation fails when score is above or below the threshold"""


class ConfigEvalConfigDefaultEvalsTrustworthiness(TypedDict, total=False):
    eval_key: Required[str]
    """
    Unique key for eval metric - currently maps to the TrustworthyRAG name property
    and eval_scores dictionary key to check against threshold
    """

    name: Required[str]
    """Display name/label for the evaluation metric"""

    enabled: bool
    """Allows the evaluation to be disabled without removing it"""

    priority: Optional[int]
    """
    Priority order for evals (lower number = higher priority) to determine primary
    eval issue to surface
    """

    should_escalate: bool
    """
    If true, failing this eval means the response is considered bad and can trigger
    escalation to Codex/SME
    """

    threshold: float
    """Threshold value that determines if the evaluation fails"""

    threshold_direction: Literal["above", "below"]
    """Whether the evaluation fails when score is above or below the threshold"""


class ConfigEvalConfigDefaultEvals(TypedDict, total=False):
    context_sufficiency: ConfigEvalConfigDefaultEvalsContextSufficiency
    """A pre-configured evaluation metric from TrustworthyRAG or built into the system.

    The evaluation criteria and identifiers are immutable and system-managed, while
    other properties like thresholds and priorities can be configured.
    """

    query_ease: ConfigEvalConfigDefaultEvalsQueryEase
    """A pre-configured evaluation metric from TrustworthyRAG or built into the system.

    The evaluation criteria and identifiers are immutable and system-managed, while
    other properties like thresholds and priorities can be configured.
    """

    response_groundedness: ConfigEvalConfigDefaultEvalsResponseGroundedness
    """A pre-configured evaluation metric from TrustworthyRAG or built into the system.

    The evaluation criteria and identifiers are immutable and system-managed, while
    other properties like thresholds and priorities can be configured.
    """

    response_helpfulness: ConfigEvalConfigDefaultEvalsResponseHelpfulness
    """A pre-configured evaluation metric from TrustworthyRAG or built into the system.

    The evaluation criteria and identifiers are immutable and system-managed, while
    other properties like thresholds and priorities can be configured.
    """

    trustworthiness: ConfigEvalConfigDefaultEvalsTrustworthiness
    """A pre-configured evaluation metric from TrustworthyRAG or built into the system.

    The evaluation criteria and identifiers are immutable and system-managed, while
    other properties like thresholds and priorities can be configured.
    """


class ConfigEvalConfig(TypedDict, total=False):
    custom_evals: ConfigEvalConfigCustomEvals
    """Configuration for custom evaluation metrics."""

    default_evals: ConfigEvalConfigDefaultEvals
    """Configuration for default evaluation metrics."""


class Config(TypedDict, total=False):
    clustering_use_llm_matching: bool

    eval_config: ConfigEvalConfig
    """Configuration for project-specific evaluation metrics"""

    llm_matching_model: str

    llm_matching_quality_preset: Literal["best", "high", "medium", "low", "base"]

    lower_llm_match_distance_threshold: float

    max_distance: float

    query_use_llm_matching: bool

    upper_llm_match_distance_threshold: float
