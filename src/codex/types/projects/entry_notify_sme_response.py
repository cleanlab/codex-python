# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["EntryNotifySmeResponse"]


class EntryNotifySmeResponse(BaseModel):
    entry_id: str

    recipient_email: str

    status: str
