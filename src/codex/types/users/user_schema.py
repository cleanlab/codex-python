# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["UserSchema"]


class UserSchema(BaseModel):
    id: str

    api_key: str

    api_key_timestamp: datetime

    created_at: datetime

    email: str

    name: Optional[str] = None

    updated_at: datetime
