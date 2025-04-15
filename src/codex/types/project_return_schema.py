# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ProjectReturnSchema", "Config"]


class Config(BaseModel):
    clustering_use_llm_matching: Optional[bool] = None

    llm_matching_model: Optional[str] = None

    llm_matching_quality_preset: Optional[str] = None

    lower_llm_match_distance_threshold: Optional[float] = None

    max_distance: Optional[float] = None

    query_use_llm_matching: Optional[bool] = None

    upper_llm_match_distance_threshold: Optional[float] = None


class ProjectReturnSchema(BaseModel):
    id: str

    config: Config

    created_at: datetime

    created_by_user_id: str

    name: str

    organization_id: str

    updated_at: datetime

    description: Optional[str] = None
