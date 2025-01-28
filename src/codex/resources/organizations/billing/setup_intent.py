# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.organizations.billing.organization_billing_setup_intent import OrganizationBillingSetupIntent

__all__ = ["SetupIntentResource", "AsyncSetupIntentResource"]


class SetupIntentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SetupIntentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return SetupIntentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SetupIntentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return SetupIntentResourceWithStreamingResponse(self)

    def create(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationBillingSetupIntent:
        """
        Create a setup intent for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._post(
            f"/api/organizations/{organization_id}/billing/setup-intent",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationBillingSetupIntent,
        )


class AsyncSetupIntentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSetupIntentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSetupIntentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSetupIntentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncSetupIntentResourceWithStreamingResponse(self)

    async def create(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationBillingSetupIntent:
        """
        Create a setup intent for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._post(
            f"/api/organizations/{organization_id}/billing/setup-intent",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationBillingSetupIntent,
        )


class SetupIntentResourceWithRawResponse:
    def __init__(self, setup_intent: SetupIntentResource) -> None:
        self._setup_intent = setup_intent

        self.create = to_raw_response_wrapper(
            setup_intent.create,
        )


class AsyncSetupIntentResourceWithRawResponse:
    def __init__(self, setup_intent: AsyncSetupIntentResource) -> None:
        self._setup_intent = setup_intent

        self.create = async_to_raw_response_wrapper(
            setup_intent.create,
        )


class SetupIntentResourceWithStreamingResponse:
    def __init__(self, setup_intent: SetupIntentResource) -> None:
        self._setup_intent = setup_intent

        self.create = to_streamed_response_wrapper(
            setup_intent.create,
        )


class AsyncSetupIntentResourceWithStreamingResponse:
    def __init__(self, setup_intent: AsyncSetupIntentResource) -> None:
        self._setup_intent = setup_intent

        self.create = async_to_streamed_response_wrapper(
            setup_intent.create,
        )
