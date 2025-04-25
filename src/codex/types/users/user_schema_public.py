# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UserSchemaPublic"]


class UserSchemaPublic(BaseModel):
    id: str

    api_key: str

    email: str

    email_verified: bool

    first_name: Optional[str] = None

    is_account_activated: Optional[bool] = None

    last_name: Optional[str] = None

    name: Optional[str] = None

    phone_number: Optional[str] = None
