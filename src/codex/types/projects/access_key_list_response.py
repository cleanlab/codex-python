# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .access_key_schema import AccessKeySchema

__all__ = ["AccessKeyListResponse"]

AccessKeyListResponse: TypeAlias = List[AccessKeySchema]
