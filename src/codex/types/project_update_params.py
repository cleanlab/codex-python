# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProjectUpdateParams", "Config"]


class ProjectUpdateParams(TypedDict, total=False):
    config: Required[Config]

    name: Required[str]

    description: Optional[str]


class Config(TypedDict, total=False):
    max_distance: float
