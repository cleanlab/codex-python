# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ProjectInviteSmeResponse"]


class ProjectInviteSmeResponse(BaseModel):
    recipient_email: str

    status: str
