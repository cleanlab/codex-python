# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ProjectListResponse", "Project", "ProjectConfig"]


class ProjectConfig(BaseModel):
    max_distance: Optional[float] = None


class Project(BaseModel):
    id: str

    config: ProjectConfig

    created_at: datetime

    created_by_user_id: str

    name: str

    organization_id: str

    updated_at: datetime

    description: Optional[str] = None

    unanswered_entries_count: Optional[int] = None


class ProjectListResponse(BaseModel):
    projects: List[Project]

    total_count: int
