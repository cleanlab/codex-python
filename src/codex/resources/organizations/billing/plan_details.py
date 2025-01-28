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
from ....types.organizations.billing.organization_billing_plan_details import OrganizationBillingPlanDetails

__all__ = ["PlanDetailsResource", "AsyncPlanDetailsResource"]


class PlanDetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlanDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return PlanDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlanDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return PlanDetailsResourceWithStreamingResponse(self)

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
    ) -> OrganizationBillingPlanDetails:
        """
        Get plan details for an organization.

        This includes the plan name,

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            f"/api/organizations/{organization_id}/billing/plan-details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationBillingPlanDetails,
        )


class AsyncPlanDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlanDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlanDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlanDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncPlanDetailsResourceWithStreamingResponse(self)

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
    ) -> OrganizationBillingPlanDetails:
        """
        Get plan details for an organization.

        This includes the plan name,

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            f"/api/organizations/{organization_id}/billing/plan-details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationBillingPlanDetails,
        )


class PlanDetailsResourceWithRawResponse:
    def __init__(self, plan_details: PlanDetailsResource) -> None:
        self._plan_details = plan_details

        self.retrieve = to_raw_response_wrapper(
            plan_details.retrieve,
        )


class AsyncPlanDetailsResourceWithRawResponse:
    def __init__(self, plan_details: AsyncPlanDetailsResource) -> None:
        self._plan_details = plan_details

        self.retrieve = async_to_raw_response_wrapper(
            plan_details.retrieve,
        )


class PlanDetailsResourceWithStreamingResponse:
    def __init__(self, plan_details: PlanDetailsResource) -> None:
        self._plan_details = plan_details

        self.retrieve = to_streamed_response_wrapper(
            plan_details.retrieve,
        )


class AsyncPlanDetailsResourceWithStreamingResponse:
    def __init__(self, plan_details: AsyncPlanDetailsResource) -> None:
        self._plan_details = plan_details

        self.retrieve = async_to_streamed_response_wrapper(
            plan_details.retrieve,
        )
