# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from codex import Codex, AsyncCodex
from tests.utils import assert_matches_type
from codex.types.users import VerificationResendResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_resend(self, client: Codex) -> None:
        verification = client.users.verification.resend()
        assert_matches_type(VerificationResendResponse, verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_resend(self, client: Codex) -> None:
        response = client.users.verification.with_raw_response.resend()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationResendResponse, verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_resend(self, client: Codex) -> None:
        with client.users.verification.with_streaming_response.resend() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationResendResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVerification:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_resend(self, async_client: AsyncCodex) -> None:
        verification = await async_client.users.verification.resend()
        assert_matches_type(VerificationResendResponse, verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_resend(self, async_client: AsyncCodex) -> None:
        response = await async_client.users.verification.with_raw_response.resend()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationResendResponse, verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_resend(self, async_client: AsyncCodex) -> None:
        async with async_client.users.verification.with_streaming_response.resend() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationResendResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True
