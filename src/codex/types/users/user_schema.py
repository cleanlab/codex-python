# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["UserSchema"]


class UserSchema(BaseModel):
    id: str

    account_activated_at: Optional[datetime] = None

    api_key: str

    api_key_timestamp: datetime

    created_at: datetime

    discovery_source: Optional[str] = None

    email: str

    email_verified: bool

    updated_at: datetime

    user_provided_company_name: Optional[str] = None

    first_name: Optional[str] = None

    is_account_activated: Optional[bool] = None

    last_name: Optional[str] = None

    name: Optional[str] = None

    phone_number: Optional[str] = None
