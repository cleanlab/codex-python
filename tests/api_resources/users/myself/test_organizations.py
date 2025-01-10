# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from codex import CleanlabCodex, AsyncCleanlabCodex
from tests.utils import assert_matches_type
from codex.types.users.myself import UserOrganizationsSchema

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: CleanlabCodex) -> None:
        organization = client.users.myself.organizations.list()
        assert_matches_type(UserOrganizationsSchema, organization, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: CleanlabCodex) -> None:
        response = client.users.myself.organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(UserOrganizationsSchema, organization, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: CleanlabCodex) -> None:
        with client.users.myself.organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(UserOrganizationsSchema, organization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCleanlabCodex) -> None:
        organization = await async_client.users.myself.organizations.list()
        assert_matches_type(UserOrganizationsSchema, organization, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCleanlabCodex) -> None:
        response = await async_client.users.myself.organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(UserOrganizationsSchema, organization, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCleanlabCodex) -> None:
        async with async_client.users.myself.organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(UserOrganizationsSchema, organization, path=["response"])

        assert cast(Any, response.is_closed) is True
