# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ProjectReturnSchema", "Config"]


class Config(BaseModel):
    max_distance: Optional[float] = None


class ProjectReturnSchema(BaseModel):
    id: str

    config: Config

    created_at: datetime

    created_by_user_id: str

    name: str

    organization_id: str

    updated_at: datetime

    description: Optional[str] = None
