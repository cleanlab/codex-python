# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProjectCreateParams", "Config"]


class ProjectCreateParams(TypedDict, total=False):
    config: Required[Config]

    name: Required[str]

    organization_id: Required[str]

    description: Optional[str]


class Config(TypedDict, total=False):
    clustering_use_llm_matching: bool

    llm_matching_model: str

    llm_matching_quality_preset: str

    lower_llm_match_distance_threshold: float

    max_distance: float

    query_use_llm_matching: bool

    upper_llm_match_distance_threshold: float
