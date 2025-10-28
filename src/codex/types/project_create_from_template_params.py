# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProjectCreateFromTemplateParams"]


class ProjectCreateFromTemplateParams(TypedDict, total=False):
    organization_id: Required[str]

    template_project_id: str

    description: Optional[str]

    name: Optional[str]
