# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from codex import Codex, AsyncCodex
from tests.utils import assert_matches_type
from codex._utils import parse_datetime
from codex.types.users import UserSchemaPublic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_activate_account(self, client: Codex) -> None:
        user = client.users.activate_account(
            first_name="first_name",
            last_name="last_name",
        )
        assert_matches_type(UserSchemaPublic, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_activate_account_with_all_params(self, client: Codex) -> None:
        user = client.users.activate_account(
            first_name="first_name",
            last_name="last_name",
            account_activated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            discovery_source="discovery_source",
            is_account_activated=True,
            phone_number="phone_number",
            user_provided_company_name="user_provided_company_name",
        )
        assert_matches_type(UserSchemaPublic, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_activate_account(self, client: Codex) -> None:
        response = client.users.with_raw_response.activate_account(
            first_name="first_name",
            last_name="last_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserSchemaPublic, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_activate_account(self, client: Codex) -> None:
        with client.users.with_streaming_response.activate_account(
            first_name="first_name",
            last_name="last_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserSchemaPublic, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_activate_account(self, async_client: AsyncCodex) -> None:
        user = await async_client.users.activate_account(
            first_name="first_name",
            last_name="last_name",
        )
        assert_matches_type(UserSchemaPublic, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_activate_account_with_all_params(self, async_client: AsyncCodex) -> None:
        user = await async_client.users.activate_account(
            first_name="first_name",
            last_name="last_name",
            account_activated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            discovery_source="discovery_source",
            is_account_activated=True,
            phone_number="phone_number",
            user_provided_company_name="user_provided_company_name",
        )
        assert_matches_type(UserSchemaPublic, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_activate_account(self, async_client: AsyncCodex) -> None:
        response = await async_client.users.with_raw_response.activate_account(
            first_name="first_name",
            last_name="last_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserSchemaPublic, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_activate_account(self, async_client: AsyncCodex) -> None:
        async with async_client.users.with_streaming_response.activate_account(
            first_name="first_name",
            last_name="last_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserSchemaPublic, user, path=["response"])

        assert cast(Any, response.is_closed) is True
