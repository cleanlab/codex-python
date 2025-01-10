# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ...._models import BaseModel

__all__ = ["UserOrganizationsSchema", "Organization"]


class Organization(BaseModel):
    created_at: datetime

    organization_id: str

    updated_at: datetime

    user_id: str


class UserOrganizationsSchema(BaseModel):
    organizations: List[Organization]
