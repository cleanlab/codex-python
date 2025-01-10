# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from codex import Cleanlab, AsyncCleanlab
from tests.utils import assert_matches_type
from codex.types.users import UserSchema

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKey:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_refresh(self, client: Cleanlab) -> None:
        api_key = client.users.myself.api_key.refresh()
        assert_matches_type(UserSchema, api_key, path=["response"])

    @parametrize
    def test_raw_response_refresh(self, client: Cleanlab) -> None:
        response = client.users.myself.api_key.with_raw_response.refresh()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(UserSchema, api_key, path=["response"])

    @parametrize
    def test_streaming_response_refresh(self, client: Cleanlab) -> None:
        with client.users.myself.api_key.with_streaming_response.refresh() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(UserSchema, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPIKey:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_refresh(self, async_client: AsyncCleanlab) -> None:
        api_key = await async_client.users.myself.api_key.refresh()
        assert_matches_type(UserSchema, api_key, path=["response"])

    @parametrize
    async def test_raw_response_refresh(self, async_client: AsyncCleanlab) -> None:
        response = await async_client.users.myself.api_key.with_raw_response.refresh()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(UserSchema, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_refresh(self, async_client: AsyncCleanlab) -> None:
        async with async_client.users.myself.api_key.with_streaming_response.refresh() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(UserSchema, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True
