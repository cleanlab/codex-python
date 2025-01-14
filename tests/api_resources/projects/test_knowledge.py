# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from codex import Codex, AsyncCodex
from tests.utils import assert_matches_type
from codex.types.projects import (
    Entry,
    ListKnowledgeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledge:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Codex) -> None:
        knowledge = client.projects.knowledge.create(
            project_id=0,
            question="question",
        )
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Codex) -> None:
        knowledge = client.projects.knowledge.create(
            project_id=0,
            question="question",
            answer="answer",
        )
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Codex) -> None:
        response = client.projects.knowledge.with_raw_response.create(
            project_id=0,
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Codex) -> None:
        with client.projects.knowledge.with_streaming_response.create(
            project_id=0,
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(Entry, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Codex) -> None:
        knowledge = client.projects.knowledge.retrieve(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        )
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Codex) -> None:
        response = client.projects.knowledge.with_raw_response.retrieve(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Codex) -> None:
        with client.projects.knowledge.with_streaming_response.retrieve(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(Entry, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.projects.knowledge.with_raw_response.retrieve(
                entry_id="",
                project_id=0,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Codex) -> None:
        knowledge = client.projects.knowledge.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        )
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Codex) -> None:
        knowledge = client.projects.knowledge.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
            answer="answer",
            question="question",
        )
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Codex) -> None:
        response = client.projects.knowledge.with_raw_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Codex) -> None:
        with client.projects.knowledge.with_streaming_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(Entry, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.projects.knowledge.with_raw_response.update(
                entry_id="",
                project_id=0,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Codex) -> None:
        knowledge = client.projects.knowledge.list(
            project_id=0,
        )
        assert_matches_type(ListKnowledgeResponse, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Codex) -> None:
        knowledge = client.projects.knowledge.list(
            project_id=0,
            answered_only=True,
            limit=1,
            offset=0,
            order="asc",
            sort="created_at",
            unanswered_only=True,
        )
        assert_matches_type(ListKnowledgeResponse, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Codex) -> None:
        response = client.projects.knowledge.with_raw_response.list(
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(ListKnowledgeResponse, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Codex) -> None:
        with client.projects.knowledge.with_streaming_response.list(
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(ListKnowledgeResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Codex) -> None:
        knowledge = client.projects.knowledge.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        )
        assert knowledge is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Codex) -> None:
        response = client.projects.knowledge.with_raw_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert knowledge is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Codex) -> None:
        with client.projects.knowledge.with_streaming_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert knowledge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.projects.knowledge.with_raw_response.delete(
                entry_id="",
                project_id=0,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_add_question(self, client: Codex) -> None:
        knowledge = client.projects.knowledge.add_question(
            project_id=0,
            question="question",
        )
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_question(self, client: Codex) -> None:
        response = client.projects.knowledge.with_raw_response.add_question(
            project_id=0,
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_question(self, client: Codex) -> None:
        with client.projects.knowledge.with_streaming_response.add_question(
            project_id=0,
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(Entry, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_query(self, client: Codex) -> None:
        knowledge = client.projects.knowledge.query(
            project_id=0,
            question="question",
        )
        assert_matches_type(Optional[Entry], knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_query(self, client: Codex) -> None:
        response = client.projects.knowledge.with_raw_response.query(
            project_id=0,
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(Optional[Entry], knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_query(self, client: Codex) -> None:
        with client.projects.knowledge.with_streaming_response.query(
            project_id=0,
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(Optional[Entry], knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKnowledge:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCodex) -> None:
        knowledge = await async_client.projects.knowledge.create(
            project_id=0,
            question="question",
        )
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCodex) -> None:
        knowledge = await async_client.projects.knowledge.create(
            project_id=0,
            question="question",
            answer="answer",
        )
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.knowledge.with_raw_response.create(
            project_id=0,
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.knowledge.with_streaming_response.create(
            project_id=0,
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(Entry, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCodex) -> None:
        knowledge = await async_client.projects.knowledge.retrieve(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        )
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.knowledge.with_raw_response.retrieve(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.knowledge.with_streaming_response.retrieve(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(Entry, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.projects.knowledge.with_raw_response.retrieve(
                entry_id="",
                project_id=0,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCodex) -> None:
        knowledge = await async_client.projects.knowledge.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        )
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCodex) -> None:
        knowledge = await async_client.projects.knowledge.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
            answer="answer",
            question="question",
        )
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.knowledge.with_raw_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.knowledge.with_streaming_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(Entry, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.projects.knowledge.with_raw_response.update(
                entry_id="",
                project_id=0,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCodex) -> None:
        knowledge = await async_client.projects.knowledge.list(
            project_id=0,
        )
        assert_matches_type(ListKnowledgeResponse, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCodex) -> None:
        knowledge = await async_client.projects.knowledge.list(
            project_id=0,
            answered_only=True,
            limit=1,
            offset=0,
            order="asc",
            sort="created_at",
            unanswered_only=True,
        )
        assert_matches_type(ListKnowledgeResponse, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.knowledge.with_raw_response.list(
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(ListKnowledgeResponse, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.knowledge.with_streaming_response.list(
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(ListKnowledgeResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCodex) -> None:
        knowledge = await async_client.projects.knowledge.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        )
        assert knowledge is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.knowledge.with_raw_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert knowledge is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.knowledge.with_streaming_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert knowledge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.projects.knowledge.with_raw_response.delete(
                entry_id="",
                project_id=0,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_question(self, async_client: AsyncCodex) -> None:
        knowledge = await async_client.projects.knowledge.add_question(
            project_id=0,
            question="question",
        )
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_question(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.knowledge.with_raw_response.add_question(
            project_id=0,
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(Entry, knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_question(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.knowledge.with_streaming_response.add_question(
            project_id=0,
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(Entry, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_query(self, async_client: AsyncCodex) -> None:
        knowledge = await async_client.projects.knowledge.query(
            project_id=0,
            question="question",
        )
        assert_matches_type(Optional[Entry], knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.knowledge.with_raw_response.query(
            project_id=0,
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(Optional[Entry], knowledge, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.knowledge.with_streaming_response.query(
            project_id=0,
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(Optional[Entry], knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True
