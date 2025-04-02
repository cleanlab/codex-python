# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from codex import Codex, AsyncCodex
from codex.types import HealthCheckResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHealth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_check(self, client: Codex) -> None:
        health = client.health.check()
        assert_matches_type(HealthCheckResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_check(self, client: Codex) -> None:
        response = client.health.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = response.parse()
        assert_matches_type(HealthCheckResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_check(self, client: Codex) -> None:
        with client.health.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = response.parse()
            assert_matches_type(HealthCheckResponse, health, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_db(self, client: Codex) -> None:
        health = client.health.db()
        assert_matches_type(HealthCheckResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_db(self, client: Codex) -> None:
        response = client.health.with_raw_response.db()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = response.parse()
        assert_matches_type(HealthCheckResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_db(self, client: Codex) -> None:
        with client.health.with_streaming_response.db() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = response.parse()
            assert_matches_type(HealthCheckResponse, health, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHealth:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_check(self, async_client: AsyncCodex) -> None:
        health = await async_client.health.check()
        assert_matches_type(HealthCheckResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_check(self, async_client: AsyncCodex) -> None:
        response = await async_client.health.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = await response.parse()
        assert_matches_type(HealthCheckResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncCodex) -> None:
        async with async_client.health.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = await response.parse()
            assert_matches_type(HealthCheckResponse, health, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_db(self, async_client: AsyncCodex) -> None:
        health = await async_client.health.db()
        assert_matches_type(HealthCheckResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_db(self, async_client: AsyncCodex) -> None:
        response = await async_client.health.with_raw_response.db()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = await response.parse()
        assert_matches_type(HealthCheckResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_db(self, async_client: AsyncCodex) -> None:
        async with async_client.health.with_streaming_response.db() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = await response.parse()
            assert_matches_type(HealthCheckResponse, health, path=["response"])

        assert cast(Any, response.is_closed) is True
