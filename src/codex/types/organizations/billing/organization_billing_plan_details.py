# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["OrganizationBillingPlanDetails"]


class OrganizationBillingPlanDetails(BaseModel):
    current_billing_period_credits_answers: float

    current_billing_period_credits_cents: float

    current_billing_period_total_cents: float

    current_billing_period_usage_answers: float

    current_billing_period_usage_cents: float

    invoice_end_date: datetime

    invoice_issue_date: datetime

    invoice_start_date: datetime

    name: str

    is_enterprise: Optional[bool] = None
