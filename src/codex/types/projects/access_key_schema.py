# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AccessKeySchema"]


class AccessKeySchema(BaseModel):
    id: str

    token: str

    created_at: datetime

    last_used_at: Optional[datetime] = None

    name: str

    project_id: str

    status: Literal["active", "expired", "revoked"]

    updated_at: datetime

    description: Optional[str] = None

    expires_at: Optional[datetime] = None
