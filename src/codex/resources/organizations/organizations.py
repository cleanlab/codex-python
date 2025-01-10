# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .billing import (
    BillingResource,
    AsyncBillingResource,
    BillingResourceWithRawResponse,
    AsyncBillingResourceWithRawResponse,
    BillingResourceWithStreamingResponse,
    AsyncBillingResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.organization_schema_public import OrganizationSchemaPublic

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def billing(self) -> BillingResource:
        return BillingResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/codex-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/codex-python#with_streaming_response
        """
        return OrganizationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationSchemaPublic:
        """
        Get a single organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            f"/api/organizations/{organization_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationSchemaPublic,
        )


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def billing(self) -> AsyncBillingResource:
        return AsyncBillingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/codex-python#with_streaming_response
        """
        return AsyncOrganizationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationSchemaPublic:
        """
        Get a single organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            f"/api/organizations/{organization_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationSchemaPublic,
        )


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.retrieve = to_raw_response_wrapper(
            organizations.retrieve,
        )

    @cached_property
    def billing(self) -> BillingResourceWithRawResponse:
        return BillingResourceWithRawResponse(self._organizations.billing)


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.retrieve = async_to_raw_response_wrapper(
            organizations.retrieve,
        )

    @cached_property
    def billing(self) -> AsyncBillingResourceWithRawResponse:
        return AsyncBillingResourceWithRawResponse(self._organizations.billing)


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.retrieve = to_streamed_response_wrapper(
            organizations.retrieve,
        )

    @cached_property
    def billing(self) -> BillingResourceWithStreamingResponse:
        return BillingResourceWithStreamingResponse(self._organizations.billing)


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.retrieve = async_to_streamed_response_wrapper(
            organizations.retrieve,
        )

    @cached_property
    def billing(self) -> AsyncBillingResourceWithStreamingResponse:
        return AsyncBillingResourceWithStreamingResponse(self._organizations.billing)
