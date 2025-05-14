# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPageClusters, AsyncOffsetPageClusters
from ..._base_client import AsyncPaginator, make_request_options
from ...types.projects import cluster_list_params
from ...types.projects.cluster_list_response import ClusterListResponse
from ...types.projects.cluster_list_variants_response import ClusterListVariantsResponse

__all__ = ["ClustersResource", "AsyncClustersResource"]


class ClustersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClustersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return ClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return ClustersResourceWithStreamingResponse(self)

    def list(
        self,
        project_id: str,
        *,
        eval_issue_types: List[
            Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "unsupported"]
        ]
        | NotGiven = NOT_GIVEN,
        instruction_adherence_failure: Optional[Literal["html_format", "content_structure"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        sort: Optional[
            Literal[
                "created_at",
                "answered_at",
                "cluster_frequency_count",
                "custom_rank",
                "eval_score",
                "html_format_score",
                "content_structure_score",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        states: List[Literal["unanswered", "draft", "published", "published_with_draft"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPageClusters[ClusterListResponse]:
        """
        List knowledge entries for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get_api_list(
            f"/api/projects/{project_id}/entries/clusters",
            page=SyncOffsetPageClusters[ClusterListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "eval_issue_types": eval_issue_types,
                        "instruction_adherence_failure": instruction_adherence_failure,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "sort": sort,
                        "states": states,
                    },
                    cluster_list_params.ClusterListParams,
                ),
            ),
            model=ClusterListResponse,
        )

    def list_variants(
        self,
        representative_entry_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClusterListVariantsResponse:
        """
        Get Cluster Variants Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not representative_entry_id:
            raise ValueError(
                f"Expected a non-empty value for `representative_entry_id` but received {representative_entry_id!r}"
            )
        return self._get(
            f"/api/projects/{project_id}/entries/clusters/{representative_entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClusterListVariantsResponse,
        )


class AsyncClustersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClustersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncClustersResourceWithStreamingResponse(self)

    def list(
        self,
        project_id: str,
        *,
        eval_issue_types: List[
            Literal["hallucination", "search_failure", "unhelpful", "difficult_query", "unsupported"]
        ]
        | NotGiven = NOT_GIVEN,
        instruction_adherence_failure: Optional[Literal["html_format", "content_structure"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        sort: Optional[
            Literal[
                "created_at",
                "answered_at",
                "cluster_frequency_count",
                "custom_rank",
                "eval_score",
                "html_format_score",
                "content_structure_score",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        states: List[Literal["unanswered", "draft", "published", "published_with_draft"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ClusterListResponse, AsyncOffsetPageClusters[ClusterListResponse]]:
        """
        List knowledge entries for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get_api_list(
            f"/api/projects/{project_id}/entries/clusters",
            page=AsyncOffsetPageClusters[ClusterListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "eval_issue_types": eval_issue_types,
                        "instruction_adherence_failure": instruction_adherence_failure,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "sort": sort,
                        "states": states,
                    },
                    cluster_list_params.ClusterListParams,
                ),
            ),
            model=ClusterListResponse,
        )

    async def list_variants(
        self,
        representative_entry_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClusterListVariantsResponse:
        """
        Get Cluster Variants Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not representative_entry_id:
            raise ValueError(
                f"Expected a non-empty value for `representative_entry_id` but received {representative_entry_id!r}"
            )
        return await self._get(
            f"/api/projects/{project_id}/entries/clusters/{representative_entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClusterListVariantsResponse,
        )


class ClustersResourceWithRawResponse:
    def __init__(self, clusters: ClustersResource) -> None:
        self._clusters = clusters

        self.list = to_raw_response_wrapper(
            clusters.list,
        )
        self.list_variants = to_raw_response_wrapper(
            clusters.list_variants,
        )


class AsyncClustersResourceWithRawResponse:
    def __init__(self, clusters: AsyncClustersResource) -> None:
        self._clusters = clusters

        self.list = async_to_raw_response_wrapper(
            clusters.list,
        )
        self.list_variants = async_to_raw_response_wrapper(
            clusters.list_variants,
        )


class ClustersResourceWithStreamingResponse:
    def __init__(self, clusters: ClustersResource) -> None:
        self._clusters = clusters

        self.list = to_streamed_response_wrapper(
            clusters.list,
        )
        self.list_variants = to_streamed_response_wrapper(
            clusters.list_variants,
        )


class AsyncClustersResourceWithStreamingResponse:
    def __init__(self, clusters: AsyncClustersResource) -> None:
        self._clusters = clusters

        self.list = async_to_streamed_response_wrapper(
            clusters.list,
        )
        self.list_variants = async_to_streamed_response_wrapper(
            clusters.list_variants,
        )
