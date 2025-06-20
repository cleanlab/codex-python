# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "EntryQueryParams",
    "QueryMetadata",
    "QueryMetadataContextUnionMember3",
    "QueryMetadataMessage",
    "QueryMetadataMessageChatCompletionDeveloperMessageParam",
    "QueryMetadataMessageChatCompletionDeveloperMessageParamContentUnionMember1",
    "QueryMetadataMessageChatCompletionSystemMessageParam",
    "QueryMetadataMessageChatCompletionSystemMessageParamContentUnionMember1",
    "QueryMetadataMessageChatCompletionUserMessageParam",
    "QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1",
    "QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartTextParam",
    "QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartImageParam",
    "QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartImageParamImageURL",
    "QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartInputAudioParam",
    "QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio",
    "QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1File",
    "QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1FileFile",
    "QueryMetadataMessageChatCompletionAssistantMessageParam",
    "QueryMetadataMessageChatCompletionAssistantMessageParamAudio",
    "QueryMetadataMessageChatCompletionAssistantMessageParamContentUnionMember1",
    "QueryMetadataMessageChatCompletionAssistantMessageParamContentUnionMember1ChatCompletionContentPartTextParam",
    "QueryMetadataMessageChatCompletionAssistantMessageParamContentUnionMember1ChatCompletionContentPartRefusalParam",
    "QueryMetadataMessageChatCompletionAssistantMessageParamFunctionCall",
    "QueryMetadataMessageChatCompletionAssistantMessageParamToolCall",
    "QueryMetadataMessageChatCompletionAssistantMessageParamToolCallFunction",
    "QueryMetadataMessageChatCompletionToolMessageParam",
    "QueryMetadataMessageChatCompletionToolMessageParamContentUnionMember1",
    "QueryMetadataMessageChatCompletionFunctionMessageParam",
]


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


class QueryMetadataMessageChatCompletionDeveloperMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class QueryMetadataMessageChatCompletionDeveloperMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[QueryMetadataMessageChatCompletionDeveloperMessageParamContentUnionMember1]]]

    role: Required[Literal["developer"]]

    name: str


class QueryMetadataMessageChatCompletionSystemMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class QueryMetadataMessageChatCompletionSystemMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[QueryMetadataMessageChatCompletionSystemMessageParamContentUnionMember1]]]

    role: Required[Literal["system"]]

    name: str


class QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartTextParam(
    TypedDict, total=False
):
    text: Required[str]

    type: Required[Literal["text"]]


class QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartImageParamImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: Literal["auto", "low", "high"]


class QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartImageParam(
    TypedDict, total=False
):
    image_url: Required[
        QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartImageParamImageURL
    ]

    type: Required[Literal["image_url"]]


class QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio(
    TypedDict, total=False
):
    data: Required[str]

    format: Required[Literal["wav", "mp3"]]


class QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartInputAudioParam(
    TypedDict, total=False
):
    input_audio: Required[
        QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartInputAudioParamInputAudio
    ]

    type: Required[Literal["input_audio"]]


class QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1FileFile(TypedDict, total=False):
    file_data: str

    file_id: str

    filename: str


class QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1File(TypedDict, total=False):
    file: Required[QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1FileFile]

    type: Required[Literal["file"]]


QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1: TypeAlias = Union[
    QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartTextParam,
    QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartImageParam,
    QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1ChatCompletionContentPartInputAudioParam,
    QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1File,
]


class QueryMetadataMessageChatCompletionUserMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[QueryMetadataMessageChatCompletionUserMessageParamContentUnionMember1]]]

    role: Required[Literal["user"]]

    name: str


class QueryMetadataMessageChatCompletionAssistantMessageParamAudio(TypedDict, total=False):
    id: Required[str]


class QueryMetadataMessageChatCompletionAssistantMessageParamContentUnionMember1ChatCompletionContentPartTextParam(
    TypedDict, total=False
):
    text: Required[str]

    type: Required[Literal["text"]]


class QueryMetadataMessageChatCompletionAssistantMessageParamContentUnionMember1ChatCompletionContentPartRefusalParam(
    TypedDict, total=False
):
    refusal: Required[str]

    type: Required[Literal["refusal"]]


QueryMetadataMessageChatCompletionAssistantMessageParamContentUnionMember1: TypeAlias = Union[
    QueryMetadataMessageChatCompletionAssistantMessageParamContentUnionMember1ChatCompletionContentPartTextParam,
    QueryMetadataMessageChatCompletionAssistantMessageParamContentUnionMember1ChatCompletionContentPartRefusalParam,
]


class QueryMetadataMessageChatCompletionAssistantMessageParamFunctionCall(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class QueryMetadataMessageChatCompletionAssistantMessageParamToolCallFunction(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class QueryMetadataMessageChatCompletionAssistantMessageParamToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[QueryMetadataMessageChatCompletionAssistantMessageParamToolCallFunction]

    type: Required[Literal["function"]]


class QueryMetadataMessageChatCompletionAssistantMessageParam(TypedDict, total=False):
    role: Required[Literal["assistant"]]

    audio: Optional[QueryMetadataMessageChatCompletionAssistantMessageParamAudio]

    content: Union[str, Iterable[QueryMetadataMessageChatCompletionAssistantMessageParamContentUnionMember1], None]

    function_call: Optional[QueryMetadataMessageChatCompletionAssistantMessageParamFunctionCall]

    name: str

    refusal: Optional[str]

    tool_calls: Iterable[QueryMetadataMessageChatCompletionAssistantMessageParamToolCall]


class QueryMetadataMessageChatCompletionToolMessageParamContentUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class QueryMetadataMessageChatCompletionToolMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[QueryMetadataMessageChatCompletionToolMessageParamContentUnionMember1]]]

    role: Required[Literal["tool"]]

    tool_call_id: Required[str]


class QueryMetadataMessageChatCompletionFunctionMessageParam(TypedDict, total=False):
    content: Required[Optional[str]]

    name: Required[str]

    role: Required[Literal["function"]]


QueryMetadataMessage: TypeAlias = Union[
    QueryMetadataMessageChatCompletionDeveloperMessageParam,
    QueryMetadataMessageChatCompletionSystemMessageParam,
    QueryMetadataMessageChatCompletionUserMessageParam,
    QueryMetadataMessageChatCompletionAssistantMessageParam,
    QueryMetadataMessageChatCompletionToolMessageParam,
    QueryMetadataMessageChatCompletionFunctionMessageParam,
]


class QueryMetadata(TypedDict, total=False):
    context: Union[str, List[str], Iterable[object], Iterable[QueryMetadataContextUnionMember3], None]
    """RAG context used for the query"""

    custom_metadata: Optional[object]
    """Arbitrary metadata supplied by the user/system"""

    eval_scores: Optional[Dict[str, float]]
    """Evaluation scores for the original response"""

    evaluated_response: Optional[str]
    """The response being evaluated from the RAG system(before any remediation)"""

    messages: Optional[Iterable[QueryMetadataMessage]]
    """Optional message history to provide conversation context for the query.

    Used to rewrite query into a self-contained version of itself. If not provided,
    the query will be treated as self-contained.
    """

    original_question: Optional[str]
    """The original question that was asked before any rewriting or processing.

    For all non-conversational RAG, original_question should be the same as the
    final question seen in Codex.
    """
