# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserActivateAccountParams"]


class UserActivateAccountParams(TypedDict, total=False):
    first_name: Required[str]

    last_name: Required[str]

    account_activated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    discovery_source: Optional[str]

    is_account_activated: bool

    phone_number: Optional[str]

    user_provided_company_name: Optional[str]
