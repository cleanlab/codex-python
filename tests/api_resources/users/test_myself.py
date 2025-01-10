# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from codex import CleanlabCodex, AsyncCleanlabCodex
from tests.utils import assert_matches_type
from codex.types.users import UserSchemaPublic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMyself:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: CleanlabCodex) -> None:
        myself = client.users.myself.retrieve()
        assert_matches_type(UserSchemaPublic, myself, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: CleanlabCodex) -> None:
        response = client.users.myself.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        myself = response.parse()
        assert_matches_type(UserSchemaPublic, myself, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: CleanlabCodex) -> None:
        with client.users.myself.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            myself = response.parse()
            assert_matches_type(UserSchemaPublic, myself, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMyself:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCleanlabCodex) -> None:
        myself = await async_client.users.myself.retrieve()
        assert_matches_type(UserSchemaPublic, myself, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCleanlabCodex) -> None:
        response = await async_client.users.myself.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        myself = await response.parse()
        assert_matches_type(UserSchemaPublic, myself, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCleanlabCodex) -> None:
        async with async_client.users.myself.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            myself = await response.parse()
            assert_matches_type(UserSchemaPublic, myself, path=["response"])

        assert cast(Any, response.is_closed) is True
