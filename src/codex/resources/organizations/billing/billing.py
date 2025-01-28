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
from .card_details import (
    CardDetailsResource,
    AsyncCardDetailsResource,
    CardDetailsResourceWithRawResponse,
    AsyncCardDetailsResourceWithRawResponse,
    CardDetailsResourceWithStreamingResponse,
    AsyncCardDetailsResourceWithStreamingResponse,
)
from .plan_details import (
    PlanDetailsResource,
    AsyncPlanDetailsResource,
    PlanDetailsResourceWithRawResponse,
    AsyncPlanDetailsResourceWithRawResponse,
    PlanDetailsResourceWithStreamingResponse,
    AsyncPlanDetailsResourceWithStreamingResponse,
)
from .setup_intent import (
    SetupIntentResource,
    AsyncSetupIntentResource,
    SetupIntentResourceWithRawResponse,
    AsyncSetupIntentResourceWithRawResponse,
    SetupIntentResourceWithStreamingResponse,
    AsyncSetupIntentResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.organizations.organization_billing_usage_schema import OrganizationBillingUsageSchema
from ....types.organizations.organization_billing_invoices_schema import OrganizationBillingInvoicesSchema

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def card_details(self) -> CardDetailsResource:
        return CardDetailsResource(self._client)

    @cached_property
    def setup_intent(self) -> SetupIntentResource:
        return SetupIntentResource(self._client)

    @cached_property
    def plan_details(self) -> PlanDetailsResource:
        return PlanDetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return BillingResourceWithStreamingResponse(self)

    def invoices(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationBillingInvoicesSchema:
        """
        Get invoices iFrame URL for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            f"/api/organizations/{organization_id}/billing/invoices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationBillingInvoicesSchema,
        )

    def usage(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationBillingUsageSchema:
        """
        Get usage iFrame URL for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            f"/api/organizations/{organization_id}/billing/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationBillingUsageSchema,
        )


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def card_details(self) -> AsyncCardDetailsResource:
        return AsyncCardDetailsResource(self._client)

    @cached_property
    def setup_intent(self) -> AsyncSetupIntentResource:
        return AsyncSetupIntentResource(self._client)

    @cached_property
    def plan_details(self) -> AsyncPlanDetailsResource:
        return AsyncPlanDetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncBillingResourceWithStreamingResponse(self)

    async def invoices(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationBillingInvoicesSchema:
        """
        Get invoices iFrame URL for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            f"/api/organizations/{organization_id}/billing/invoices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationBillingInvoicesSchema,
        )

    async def usage(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationBillingUsageSchema:
        """
        Get usage iFrame URL for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            f"/api/organizations/{organization_id}/billing/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationBillingUsageSchema,
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.invoices = to_raw_response_wrapper(
            billing.invoices,
        )
        self.usage = to_raw_response_wrapper(
            billing.usage,
        )

    @cached_property
    def card_details(self) -> CardDetailsResourceWithRawResponse:
        return CardDetailsResourceWithRawResponse(self._billing.card_details)

    @cached_property
    def setup_intent(self) -> SetupIntentResourceWithRawResponse:
        return SetupIntentResourceWithRawResponse(self._billing.setup_intent)

    @cached_property
    def plan_details(self) -> PlanDetailsResourceWithRawResponse:
        return PlanDetailsResourceWithRawResponse(self._billing.plan_details)


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.invoices = async_to_raw_response_wrapper(
            billing.invoices,
        )
        self.usage = async_to_raw_response_wrapper(
            billing.usage,
        )

    @cached_property
    def card_details(self) -> AsyncCardDetailsResourceWithRawResponse:
        return AsyncCardDetailsResourceWithRawResponse(self._billing.card_details)

    @cached_property
    def setup_intent(self) -> AsyncSetupIntentResourceWithRawResponse:
        return AsyncSetupIntentResourceWithRawResponse(self._billing.setup_intent)

    @cached_property
    def plan_details(self) -> AsyncPlanDetailsResourceWithRawResponse:
        return AsyncPlanDetailsResourceWithRawResponse(self._billing.plan_details)


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.invoices = to_streamed_response_wrapper(
            billing.invoices,
        )
        self.usage = to_streamed_response_wrapper(
            billing.usage,
        )

    @cached_property
    def card_details(self) -> CardDetailsResourceWithStreamingResponse:
        return CardDetailsResourceWithStreamingResponse(self._billing.card_details)

    @cached_property
    def setup_intent(self) -> SetupIntentResourceWithStreamingResponse:
        return SetupIntentResourceWithStreamingResponse(self._billing.setup_intent)

    @cached_property
    def plan_details(self) -> PlanDetailsResourceWithStreamingResponse:
        return PlanDetailsResourceWithStreamingResponse(self._billing.plan_details)


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.invoices = async_to_streamed_response_wrapper(
            billing.invoices,
        )
        self.usage = async_to_streamed_response_wrapper(
            billing.usage,
        )

    @cached_property
    def card_details(self) -> AsyncCardDetailsResourceWithStreamingResponse:
        return AsyncCardDetailsResourceWithStreamingResponse(self._billing.card_details)

    @cached_property
    def setup_intent(self) -> AsyncSetupIntentResourceWithStreamingResponse:
        return AsyncSetupIntentResourceWithStreamingResponse(self._billing.setup_intent)

    @cached_property
    def plan_details(self) -> AsyncPlanDetailsResourceWithStreamingResponse:
        return AsyncPlanDetailsResourceWithStreamingResponse(self._billing.plan_details)
