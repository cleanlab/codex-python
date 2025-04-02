# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .entry import Entry
from ..._models import BaseModel

__all__ = ["ClusterListVariantsResponse"]


class ClusterListVariantsResponse(BaseModel):
    entries: List[Entry]

    total_count: int
