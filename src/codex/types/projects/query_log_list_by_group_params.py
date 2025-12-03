# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["QueryLogListByGroupParams"]


class QueryLogListByGroupParams(TypedDict, total=False):
    created_at_end: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter logs created at or before this timestamp"""

    created_at_start: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter logs created at or after this timestamp"""

    custom_metadata: Optional[str]
    """Filter by custom metadata as JSON string: {"key1": "value1", "key2": "value2"}"""

    expert_review_status: Optional[Literal["good", "bad"]]
    """Filter by expert review status"""

    failed_evals: Optional[SequenceNotStr[str]]
    """Filter by evals that failed"""

    guardrailed: Optional[bool]
    """Filter by guardrailed status"""

    has_tool_calls: Optional[bool]
    """Filter by whether the query log has tool calls"""

    limit: int

    needs_review: Optional[bool]
    """Filter logs that need review"""

    offset: int

    order: Literal["asc", "desc"]

    passed_evals: Optional[SequenceNotStr[str]]
    """Filter by evals that passed"""

    primary_eval_issue: Optional[
        List[Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "ungrounded"]]
    ]
    """Filter logs that have ANY of these primary evaluation issues (OR operation)"""

    remediation_ids: SequenceNotStr[str]
    """List of groups to list child logs for"""

    search_text: Optional[str]
    """
    Case-insensitive search across evaluated_response and question fields
    (original_question if available, otherwise question)
    """

    sort: Optional[str]
    """Field or score to sort by.

    Available fields: 'created_at', 'primary_eval_issue_score'.

    For eval scores, use '.eval.' prefix followed by the eval name.

    Default eval scores: '.eval.trustworthiness', '.eval.context_sufficiency',
    '.eval.response_helpfulness', '.eval.query_ease', '.eval.response_groundedness'.

    Custom eval scores: '.eval.custom_eval_1', '.eval.custom_eval_2', etc.
    """

    tool_call_names: Optional[SequenceNotStr[str]]
    """Filter by names of tools called in the assistant response"""

    was_cache_hit: Optional[bool]
    """Filter by cache hit status"""
