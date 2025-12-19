# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["OrganizationListMembersResponse", "OrganizationListMembersResponseItem"]


class OrganizationListMembersResponseItem(BaseModel):
    """Schema for public organization member information."""

    email: str

    name: str

    user_id: str


OrganizationListMembersResponse: TypeAlias = List[OrganizationListMembersResponseItem]
