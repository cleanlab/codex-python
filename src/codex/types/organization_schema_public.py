# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["OrganizationSchemaPublic"]


class OrganizationSchemaPublic(BaseModel):
    id: str

    created_at: datetime

    name: str

    updated_at: datetime
