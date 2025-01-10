# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccessKeyCreateParams"]


class AccessKeyCreateParams(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
