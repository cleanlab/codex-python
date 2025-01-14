# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.projects import (
    knowledge_list_params,
    knowledge_query_params,
    knowledge_create_params,
    knowledge_update_params,
    knowledge_add_question_params,
)
from ...types.projects.entry import Entry
from ...types.projects.list_knowledge_response import ListKnowledgeResponse

__all__ = ["KnowledgeResource", "AsyncKnowledgeResource"]


class KnowledgeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KnowledgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return KnowledgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowledgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return KnowledgeResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: int,
        *,
        question: str,
        answer: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entry:
        """
        Create a knowledge entry for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/api/projects/{project_id}/knowledge/",
            body=maybe_transform(
                {
                    "question": question,
                    "answer": answer,
                },
                knowledge_create_params.KnowledgeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    def retrieve(
        self,
        entry_id: str,
        *,
        project_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entry:
        """
        Get a knowledge entry for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return self._get(
            f"/api/projects/{project_id}/knowledge/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    def update(
        self,
        entry_id: str,
        *,
        project_id: int,
        answer: Optional[str] | NotGiven = NOT_GIVEN,
        question: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entry:
        """
        Update a knowledge entry for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return self._put(
            f"/api/projects/{project_id}/knowledge/{entry_id}",
            body=maybe_transform(
                {
                    "answer": answer,
                    "question": question,
                },
                knowledge_update_params.KnowledgeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    def list(
        self,
        project_id: int,
        *,
        answered_only: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "answered_at"] | NotGiven = NOT_GIVEN,
        unanswered_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListKnowledgeResponse:
        """
        List knowledge entries for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/projects/{project_id}/knowledge/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "answered_only": answered_only,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "sort": sort,
                        "unanswered_only": unanswered_only,
                    },
                    knowledge_list_params.KnowledgeListParams,
                ),
            ),
            cast_to=ListKnowledgeResponse,
        )

    def delete(
        self,
        entry_id: str,
        *,
        project_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a knowledge entry for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/projects/{project_id}/knowledge/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def add_question(
        self,
        project_id: int,
        *,
        question: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entry:
        """
        Add a question to a project.

        Returns: 201 Created if a new question was added 200 OK if the question already
        existed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/api/projects/{project_id}/knowledge/add_question",
            body=maybe_transform({"question": question}, knowledge_add_question_params.KnowledgeAddQuestionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    def query(
        self,
        project_id: int,
        *,
        question: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Entry]:
        """
        Query knowledge for a project.

        Returns the matching entry if found and answered, otherwise returns None. This
        allows the client to distinguish between: (1) no matching question found
        (returns None), and (2) matching question found but not yet answered (returns
        Entry with answer=None).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/api/projects/{project_id}/knowledge/query",
            body=maybe_transform({"question": question}, knowledge_query_params.KnowledgeQueryParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )


class AsyncKnowledgeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKnowledgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKnowledgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowledgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncKnowledgeResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: int,
        *,
        question: str,
        answer: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entry:
        """
        Create a knowledge entry for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/api/projects/{project_id}/knowledge/",
            body=await async_maybe_transform(
                {
                    "question": question,
                    "answer": answer,
                },
                knowledge_create_params.KnowledgeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    async def retrieve(
        self,
        entry_id: str,
        *,
        project_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entry:
        """
        Get a knowledge entry for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return await self._get(
            f"/api/projects/{project_id}/knowledge/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    async def update(
        self,
        entry_id: str,
        *,
        project_id: int,
        answer: Optional[str] | NotGiven = NOT_GIVEN,
        question: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entry:
        """
        Update a knowledge entry for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return await self._put(
            f"/api/projects/{project_id}/knowledge/{entry_id}",
            body=await async_maybe_transform(
                {
                    "answer": answer,
                    "question": question,
                },
                knowledge_update_params.KnowledgeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    async def list(
        self,
        project_id: int,
        *,
        answered_only: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "answered_at"] | NotGiven = NOT_GIVEN,
        unanswered_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListKnowledgeResponse:
        """
        List knowledge entries for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/projects/{project_id}/knowledge/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "answered_only": answered_only,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "sort": sort,
                        "unanswered_only": unanswered_only,
                    },
                    knowledge_list_params.KnowledgeListParams,
                ),
            ),
            cast_to=ListKnowledgeResponse,
        )

    async def delete(
        self,
        entry_id: str,
        *,
        project_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a knowledge entry for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/projects/{project_id}/knowledge/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def add_question(
        self,
        project_id: int,
        *,
        question: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entry:
        """
        Add a question to a project.

        Returns: 201 Created if a new question was added 200 OK if the question already
        existed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/api/projects/{project_id}/knowledge/add_question",
            body=await async_maybe_transform(
                {"question": question}, knowledge_add_question_params.KnowledgeAddQuestionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )

    async def query(
        self,
        project_id: int,
        *,
        question: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Entry]:
        """
        Query knowledge for a project.

        Returns the matching entry if found and answered, otherwise returns None. This
        allows the client to distinguish between: (1) no matching question found
        (returns None), and (2) matching question found but not yet answered (returns
        Entry with answer=None).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/api/projects/{project_id}/knowledge/query",
            body=await async_maybe_transform({"question": question}, knowledge_query_params.KnowledgeQueryParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entry,
        )


class KnowledgeResourceWithRawResponse:
    def __init__(self, knowledge: KnowledgeResource) -> None:
        self._knowledge = knowledge

        self.create = to_raw_response_wrapper(
            knowledge.create,
        )
        self.retrieve = to_raw_response_wrapper(
            knowledge.retrieve,
        )
        self.update = to_raw_response_wrapper(
            knowledge.update,
        )
        self.list = to_raw_response_wrapper(
            knowledge.list,
        )
        self.delete = to_raw_response_wrapper(
            knowledge.delete,
        )
        self.add_question = to_raw_response_wrapper(
            knowledge.add_question,
        )
        self.query = to_raw_response_wrapper(
            knowledge.query,
        )


class AsyncKnowledgeResourceWithRawResponse:
    def __init__(self, knowledge: AsyncKnowledgeResource) -> None:
        self._knowledge = knowledge

        self.create = async_to_raw_response_wrapper(
            knowledge.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            knowledge.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            knowledge.update,
        )
        self.list = async_to_raw_response_wrapper(
            knowledge.list,
        )
        self.delete = async_to_raw_response_wrapper(
            knowledge.delete,
        )
        self.add_question = async_to_raw_response_wrapper(
            knowledge.add_question,
        )
        self.query = async_to_raw_response_wrapper(
            knowledge.query,
        )


class KnowledgeResourceWithStreamingResponse:
    def __init__(self, knowledge: KnowledgeResource) -> None:
        self._knowledge = knowledge

        self.create = to_streamed_response_wrapper(
            knowledge.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            knowledge.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            knowledge.update,
        )
        self.list = to_streamed_response_wrapper(
            knowledge.list,
        )
        self.delete = to_streamed_response_wrapper(
            knowledge.delete,
        )
        self.add_question = to_streamed_response_wrapper(
            knowledge.add_question,
        )
        self.query = to_streamed_response_wrapper(
            knowledge.query,
        )


class AsyncKnowledgeResourceWithStreamingResponse:
    def __init__(self, knowledge: AsyncKnowledgeResource) -> None:
        self._knowledge = knowledge

        self.create = async_to_streamed_response_wrapper(
            knowledge.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            knowledge.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            knowledge.update,
        )
        self.list = async_to_streamed_response_wrapper(
            knowledge.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            knowledge.delete,
        )
        self.add_question = async_to_streamed_response_wrapper(
            knowledge.add_question,
        )
        self.query = async_to_streamed_response_wrapper(
            knowledge.query,
        )
