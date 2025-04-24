# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["OrganizationBillingSetupIntent"]


class OrganizationBillingSetupIntent(BaseModel):
    client_secret: str

    intent_id: str
