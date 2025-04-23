# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ...types import user_activate_account_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .verification import (
    VerificationResource,
    AsyncVerificationResource,
    VerificationResourceWithRawResponse,
    AsyncVerificationResourceWithRawResponse,
    VerificationResourceWithStreamingResponse,
    AsyncVerificationResourceWithStreamingResponse,
)
from .myself.myself import (
    MyselfResource,
    AsyncMyselfResource,
    MyselfResourceWithRawResponse,
    AsyncMyselfResourceWithRawResponse,
    MyselfResourceWithStreamingResponse,
    AsyncMyselfResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.users.user_schema_public import UserSchemaPublic

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def myself(self) -> MyselfResource:
        return MyselfResource(self._client)

    @cached_property
    def verification(self) -> VerificationResource:
        return VerificationResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def activate_account(
        self,
        *,
        first_name: str,
        last_name: str,
        account_activated_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        discovery_source: Optional[str] | NotGiven = NOT_GIVEN,
        is_account_activated: bool | NotGiven = NOT_GIVEN,
        phone_number: Optional[str] | NotGiven = NOT_GIVEN,
        user_provided_company_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserSchemaPublic:
        """
        Activate an authenticated user's account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/api/users/activate_account",
            body=maybe_transform(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "account_activated_at": account_activated_at,
                    "discovery_source": discovery_source,
                    "is_account_activated": is_account_activated,
                    "phone_number": phone_number,
                    "user_provided_company_name": user_provided_company_name,
                },
                user_activate_account_params.UserActivateAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserSchemaPublic,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def myself(self) -> AsyncMyselfResource:
        return AsyncMyselfResource(self._client)

    @cached_property
    def verification(self) -> AsyncVerificationResource:
        return AsyncVerificationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cleanlab/codex-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cleanlab/codex-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def activate_account(
        self,
        *,
        first_name: str,
        last_name: str,
        account_activated_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        discovery_source: Optional[str] | NotGiven = NOT_GIVEN,
        is_account_activated: bool | NotGiven = NOT_GIVEN,
        phone_number: Optional[str] | NotGiven = NOT_GIVEN,
        user_provided_company_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserSchemaPublic:
        """
        Activate an authenticated user's account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/api/users/activate_account",
            body=await async_maybe_transform(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "account_activated_at": account_activated_at,
                    "discovery_source": discovery_source,
                    "is_account_activated": is_account_activated,
                    "phone_number": phone_number,
                    "user_provided_company_name": user_provided_company_name,
                },
                user_activate_account_params.UserActivateAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserSchemaPublic,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.activate_account = to_raw_response_wrapper(
            users.activate_account,
        )

    @cached_property
    def myself(self) -> MyselfResourceWithRawResponse:
        return MyselfResourceWithRawResponse(self._users.myself)

    @cached_property
    def verification(self) -> VerificationResourceWithRawResponse:
        return VerificationResourceWithRawResponse(self._users.verification)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.activate_account = async_to_raw_response_wrapper(
            users.activate_account,
        )

    @cached_property
    def myself(self) -> AsyncMyselfResourceWithRawResponse:
        return AsyncMyselfResourceWithRawResponse(self._users.myself)

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithRawResponse:
        return AsyncVerificationResourceWithRawResponse(self._users.verification)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.activate_account = to_streamed_response_wrapper(
            users.activate_account,
        )

    @cached_property
    def myself(self) -> MyselfResourceWithStreamingResponse:
        return MyselfResourceWithStreamingResponse(self._users.myself)

    @cached_property
    def verification(self) -> VerificationResourceWithStreamingResponse:
        return VerificationResourceWithStreamingResponse(self._users.verification)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.activate_account = async_to_streamed_response_wrapper(
            users.activate_account,
        )

    @cached_property
    def myself(self) -> AsyncMyselfResourceWithStreamingResponse:
        return AsyncMyselfResourceWithStreamingResponse(self._users.myself)

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithStreamingResponse:
        return AsyncVerificationResourceWithStreamingResponse(self._users.verification)
