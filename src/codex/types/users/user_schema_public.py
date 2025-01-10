# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UserSchemaPublic"]


class UserSchemaPublic(BaseModel):
    id: str

    api_key: str

    email: str

    name: Optional[str] = None
