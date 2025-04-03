# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EntryCreateParams"]


class EntryCreateParams(TypedDict, total=False):
    question: Required[str]

    answer: Optional[str]

    client_query_metadata: Iterable[object]

    draft_answer: Optional[str]

    x_client_library_version: Annotated[str, PropertyInfo(alias="x-client-library-version")]

    x_integration_type: Annotated[str, PropertyInfo(alias="x-integration-type")]

    x_source: Annotated[str, PropertyInfo(alias="x-source")]

    x_stainless_package_version: Annotated[str, PropertyInfo(alias="x-stainless-package-version")]
