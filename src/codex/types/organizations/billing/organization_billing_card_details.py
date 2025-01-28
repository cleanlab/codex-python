# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["OrganizationBillingCardDetails", "BillingDetails", "CardDetails"]


class BillingDetails(BaseModel):
    address_city: Optional[str] = None

    address_country: str

    address_line1: Optional[str] = None

    address_line2: Optional[str] = None

    address_postal_code: str

    address_state: Optional[str] = None

    name: Optional[str] = None


class CardDetails(BaseModel):
    brand: str

    exp_month: int

    exp_year: int

    last4: str


class OrganizationBillingCardDetails(BaseModel):
    billing_details: BillingDetails

    card_details: CardDetails
