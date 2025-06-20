# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProjectInviteSmeParams"]


class ProjectInviteSmeParams(TypedDict, total=False):
    email: Required[str]

    page_type: Required[Literal["query_log", "remediation"]]

    url_query_string: Required[str]
