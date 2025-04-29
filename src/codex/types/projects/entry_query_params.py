# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EntryQueryParams", "QueryMetadata", "QueryMetadataContextUnionMember3"]


class EntryQueryParams(TypedDict, total=False):
    question: Required[str]

    use_llm_matching: bool

    client_metadata: Optional[object]
    """Deprecated: Use query_metadata instead"""

    query_metadata: Optional[QueryMetadata]
    """Optional logging data that can be provided by the client."""

    x_client_library_version: Annotated[str, PropertyInfo(alias="x-client-library-version")]

    x_integration_type: Annotated[str, PropertyInfo(alias="x-integration-type")]

    x_source: Annotated[str, PropertyInfo(alias="x-source")]

    x_stainless_package_version: Annotated[str, PropertyInfo(alias="x-stainless-package-version")]


class QueryMetadataContextUnionMember3(TypedDict, total=False):
    content: Required[str]
    """The actual content/text of the document."""

    id: Optional[str]
    """Unique identifier for the document. Useful for tracking documents"""

    source: Optional[str]
    """Source or origin of the document. Useful for citations."""

    tags: Optional[List[str]]
    """Tags or categories for the document. Useful for filtering"""

    title: Optional[str]
    """Title or heading of the document. Useful for display and context."""


class QueryMetadata(TypedDict, total=False):
    context: Union[str, List[str], Iterable[object], Iterable[QueryMetadataContextUnionMember3], None]
    """RAG context used for the query"""

    custom_metadata: Optional[object]
    """Arbitrary metadata supplied by the user/system"""

    eval_scores: Optional[Dict[str, float]]
    """Evaluation scores for the original response"""

    evaluated_response: Optional[str]
    """The response being evaluated from the RAG system(before any remediation)"""
