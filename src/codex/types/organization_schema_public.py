# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OrganizationSchemaPublic"]


class OrganizationSchemaPublic(BaseModel):
    id: str

    created_at: datetime

    name: str

    payment_status: Literal["NULL", "FIRST_OVERAGE_LENIENT", "SECOND_OVERAGE_USAGE_BLOCKED"]

    updated_at: datetime
