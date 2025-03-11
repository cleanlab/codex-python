# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from codex import Codex, AsyncCodex
from codex.types import TlmScoreResponse, TlmPromptResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTlm:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_prompt(self, client: Codex) -> None:
        tlm = client.tlm.prompt(
            prompt="prompt",
        )
        assert_matches_type(TlmPromptResponse, tlm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_prompt_with_all_params(self, client: Codex) -> None:
        tlm = client.tlm.prompt(
            prompt="prompt",
            constrain_outputs=["string"],
            options={
                "custom_eval_criteria": [{}],
                "log": ["string"],
                "max_tokens": 0,
                "model": "model",
                "num_candidate_responses": 0,
                "num_consistency_samples": 0,
                "reasoning_effort": "reasoning_effort",
                "similarity_measure": "similarity_measure",
                "use_self_reflection": True,
            },
            quality_preset="best",
            task="task",
        )
        assert_matches_type(TlmPromptResponse, tlm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_prompt(self, client: Codex) -> None:
        response = client.tlm.with_raw_response.prompt(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tlm = response.parse()
        assert_matches_type(TlmPromptResponse, tlm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_prompt(self, client: Codex) -> None:
        with client.tlm.with_streaming_response.prompt(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tlm = response.parse()
            assert_matches_type(TlmPromptResponse, tlm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_score(self, client: Codex) -> None:
        tlm = client.tlm.score(
            prompt="prompt",
            response="response",
        )
        assert_matches_type(TlmScoreResponse, tlm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_score_with_all_params(self, client: Codex) -> None:
        tlm = client.tlm.score(
            prompt="prompt",
            response="response",
            constrain_outputs=["string"],
            options={
                "custom_eval_criteria": [{}],
                "log": ["string"],
                "max_tokens": 0,
                "model": "model",
                "num_candidate_responses": 0,
                "num_consistency_samples": 0,
                "reasoning_effort": "reasoning_effort",
                "similarity_measure": "similarity_measure",
                "use_self_reflection": True,
            },
            quality_preset="best",
            task="task",
        )
        assert_matches_type(TlmScoreResponse, tlm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_score(self, client: Codex) -> None:
        response = client.tlm.with_raw_response.score(
            prompt="prompt",
            response="response",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tlm = response.parse()
        assert_matches_type(TlmScoreResponse, tlm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_score(self, client: Codex) -> None:
        with client.tlm.with_streaming_response.score(
            prompt="prompt",
            response="response",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tlm = response.parse()
            assert_matches_type(TlmScoreResponse, tlm, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTlm:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_prompt(self, async_client: AsyncCodex) -> None:
        tlm = await async_client.tlm.prompt(
            prompt="prompt",
        )
        assert_matches_type(TlmPromptResponse, tlm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_prompt_with_all_params(self, async_client: AsyncCodex) -> None:
        tlm = await async_client.tlm.prompt(
            prompt="prompt",
            constrain_outputs=["string"],
            options={
                "custom_eval_criteria": [{}],
                "log": ["string"],
                "max_tokens": 0,
                "model": "model",
                "num_candidate_responses": 0,
                "num_consistency_samples": 0,
                "reasoning_effort": "reasoning_effort",
                "similarity_measure": "similarity_measure",
                "use_self_reflection": True,
            },
            quality_preset="best",
            task="task",
        )
        assert_matches_type(TlmPromptResponse, tlm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_prompt(self, async_client: AsyncCodex) -> None:
        response = await async_client.tlm.with_raw_response.prompt(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tlm = await response.parse()
        assert_matches_type(TlmPromptResponse, tlm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_prompt(self, async_client: AsyncCodex) -> None:
        async with async_client.tlm.with_streaming_response.prompt(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tlm = await response.parse()
            assert_matches_type(TlmPromptResponse, tlm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_score(self, async_client: AsyncCodex) -> None:
        tlm = await async_client.tlm.score(
            prompt="prompt",
            response="response",
        )
        assert_matches_type(TlmScoreResponse, tlm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_score_with_all_params(self, async_client: AsyncCodex) -> None:
        tlm = await async_client.tlm.score(
            prompt="prompt",
            response="response",
            constrain_outputs=["string"],
            options={
                "custom_eval_criteria": [{}],
                "log": ["string"],
                "max_tokens": 0,
                "model": "model",
                "num_candidate_responses": 0,
                "num_consistency_samples": 0,
                "reasoning_effort": "reasoning_effort",
                "similarity_measure": "similarity_measure",
                "use_self_reflection": True,
            },
            quality_preset="best",
            task="task",
        )
        assert_matches_type(TlmScoreResponse, tlm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_score(self, async_client: AsyncCodex) -> None:
        response = await async_client.tlm.with_raw_response.score(
            prompt="prompt",
            response="response",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tlm = await response.parse()
        assert_matches_type(TlmScoreResponse, tlm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_score(self, async_client: AsyncCodex) -> None:
        async with async_client.tlm.with_streaming_response.score(
            prompt="prompt",
            response="response",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tlm = await response.parse()
            assert_matches_type(TlmScoreResponse, tlm, path=["response"])

        assert cast(Any, response.is_closed) is True
