# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from codex import Codex, AsyncCodex
from tests.utils import assert_matches_type
from codex.types.projects import (
    Entry,
    EntryQueryResponse,
    EntryNotifySmeResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Codex) -> None:
        entry = client.projects.entries.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
        )
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Codex) -> None:
        entry = client.projects.entries.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
            answer="answer",
            client_query_metadata=[{}],
            draft_answer="draft_answer",
            x_client_library_version="x-client-library-version",
            x_integration_type="x-integration-type",
            x_source="x-source",
            x_stainless_package_version="x-stainless-package-version",
        )
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Codex) -> None:
        response = client.projects.entries.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Codex) -> None:
        with client.projects.entries.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(Entry, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.entries.with_raw_response.create(
                project_id="",
                question="question",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Codex) -> None:
        entry = client.projects.entries.retrieve(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Codex) -> None:
        response = client.projects.entries.with_raw_response.retrieve(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Codex) -> None:
        with client.projects.entries.with_streaming_response.retrieve(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(Entry, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.entries.with_raw_response.retrieve(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.projects.entries.with_raw_response.retrieve(
                entry_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Codex) -> None:
        entry = client.projects.entries.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Codex) -> None:
        entry = client.projects.entries.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            answer="answer",
            draft_answer="draft_answer",
            question="question",
        )
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Codex) -> None:
        response = client.projects.entries.with_raw_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Codex) -> None:
        with client.projects.entries.with_streaming_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(Entry, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.entries.with_raw_response.update(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.projects.entries.with_raw_response.update(
                entry_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Codex) -> None:
        entry = client.projects.entries.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert entry is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Codex) -> None:
        response = client.projects.entries.with_raw_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert entry is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Codex) -> None:
        with client.projects.entries.with_streaming_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert entry is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.entries.with_raw_response.delete(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.projects.entries.with_raw_response.delete(
                entry_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_notify_sme(self, client: Codex) -> None:
        entry = client.projects.entries.notify_sme(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            view_context={"page": 0},
        )
        assert_matches_type(EntryNotifySmeResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_notify_sme_with_all_params(self, client: Codex) -> None:
        entry = client.projects.entries.notify_sme(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            view_context={
                "page": 0,
                "filter": "unanswered",
            },
        )
        assert_matches_type(EntryNotifySmeResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_notify_sme(self, client: Codex) -> None:
        response = client.projects.entries.with_raw_response.notify_sme(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            view_context={"page": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(EntryNotifySmeResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_notify_sme(self, client: Codex) -> None:
        with client.projects.entries.with_streaming_response.notify_sme(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            view_context={"page": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(EntryNotifySmeResponse, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_notify_sme(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.entries.with_raw_response.notify_sme(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
                email="email",
                view_context={"page": 0},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.projects.entries.with_raw_response.notify_sme(
                entry_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                email="email",
                view_context={"page": 0},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_publish_draft_answer(self, client: Codex) -> None:
        entry = client.projects.entries.publish_draft_answer(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_publish_draft_answer(self, client: Codex) -> None:
        response = client.projects.entries.with_raw_response.publish_draft_answer(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_publish_draft_answer(self, client: Codex) -> None:
        with client.projects.entries.with_streaming_response.publish_draft_answer(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(Entry, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_publish_draft_answer(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.entries.with_raw_response.publish_draft_answer(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.projects.entries.with_raw_response.publish_draft_answer(
                entry_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_query(self, client: Codex) -> None:
        with pytest.warns(DeprecationWarning):
            entry = client.projects.entries.query(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                question="question",
            )

        assert_matches_type(EntryQueryResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_query_with_all_params(self, client: Codex) -> None:
        with pytest.warns(DeprecationWarning):
            entry = client.projects.entries.query(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                question="question",
                use_llm_matching=True,
                client_metadata={},
                query_metadata={
                    "context": "string",
                    "custom_metadata": {},
                    "eval_scores": {"foo": 0},
                    "evaluated_response": "evaluated_response",
                    "messages": [
                        {
                            "content": "string",
                            "role": "developer",
                            "name": "name",
                        }
                    ],
                    "original_question": "original_question",
                },
                x_client_library_version="x-client-library-version",
                x_integration_type="x-integration-type",
                x_source="x-source",
                x_stainless_package_version="x-stainless-package-version",
            )

        assert_matches_type(EntryQueryResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_query(self, client: Codex) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.projects.entries.with_raw_response.query(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                question="question",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(EntryQueryResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_query(self, client: Codex) -> None:
        with pytest.warns(DeprecationWarning):
            with client.projects.entries.with_streaming_response.query(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                question="question",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                entry = response.parse()
                assert_matches_type(EntryQueryResponse, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_query(self, client: Codex) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
                client.projects.entries.with_raw_response.query(
                    project_id="",
                    question="question",
                )

    @pytest.mark.skip()
    @parametrize
    def test_method_unpublish_answer(self, client: Codex) -> None:
        entry = client.projects.entries.unpublish_answer(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_unpublish_answer(self, client: Codex) -> None:
        response = client.projects.entries.with_raw_response.unpublish_answer(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_unpublish_answer(self, client: Codex) -> None:
        with client.projects.entries.with_streaming_response.unpublish_answer(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(Entry, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_unpublish_answer(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.entries.with_raw_response.unpublish_answer(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.projects.entries.with_raw_response.unpublish_answer(
                entry_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncEntries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCodex) -> None:
        entry = await async_client.projects.entries.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
        )
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCodex) -> None:
        entry = await async_client.projects.entries.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
            answer="answer",
            client_query_metadata=[{}],
            draft_answer="draft_answer",
            x_client_library_version="x-client-library-version",
            x_integration_type="x-integration-type",
            x_source="x-source",
            x_stainless_package_version="x-stainless-package-version",
        )
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.entries.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.entries.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(Entry, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.entries.with_raw_response.create(
                project_id="",
                question="question",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCodex) -> None:
        entry = await async_client.projects.entries.retrieve(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.entries.with_raw_response.retrieve(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.entries.with_streaming_response.retrieve(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(Entry, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.entries.with_raw_response.retrieve(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.projects.entries.with_raw_response.retrieve(
                entry_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCodex) -> None:
        entry = await async_client.projects.entries.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCodex) -> None:
        entry = await async_client.projects.entries.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            answer="answer",
            draft_answer="draft_answer",
            question="question",
        )
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.entries.with_raw_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.entries.with_streaming_response.update(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(Entry, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.entries.with_raw_response.update(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.projects.entries.with_raw_response.update(
                entry_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCodex) -> None:
        entry = await async_client.projects.entries.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert entry is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.entries.with_raw_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert entry is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.entries.with_streaming_response.delete(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert entry is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.entries.with_raw_response.delete(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.projects.entries.with_raw_response.delete(
                entry_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_notify_sme(self, async_client: AsyncCodex) -> None:
        entry = await async_client.projects.entries.notify_sme(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            view_context={"page": 0},
        )
        assert_matches_type(EntryNotifySmeResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_notify_sme_with_all_params(self, async_client: AsyncCodex) -> None:
        entry = await async_client.projects.entries.notify_sme(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            view_context={
                "page": 0,
                "filter": "unanswered",
            },
        )
        assert_matches_type(EntryNotifySmeResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_notify_sme(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.entries.with_raw_response.notify_sme(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            view_context={"page": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(EntryNotifySmeResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_notify_sme(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.entries.with_streaming_response.notify_sme(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            view_context={"page": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(EntryNotifySmeResponse, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_notify_sme(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.entries.with_raw_response.notify_sme(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
                email="email",
                view_context={"page": 0},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.projects.entries.with_raw_response.notify_sme(
                entry_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                email="email",
                view_context={"page": 0},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_publish_draft_answer(self, async_client: AsyncCodex) -> None:
        entry = await async_client.projects.entries.publish_draft_answer(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_publish_draft_answer(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.entries.with_raw_response.publish_draft_answer(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_publish_draft_answer(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.entries.with_streaming_response.publish_draft_answer(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(Entry, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_publish_draft_answer(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.entries.with_raw_response.publish_draft_answer(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.projects.entries.with_raw_response.publish_draft_answer(
                entry_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_query(self, async_client: AsyncCodex) -> None:
        with pytest.warns(DeprecationWarning):
            entry = await async_client.projects.entries.query(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                question="question",
            )

        assert_matches_type(EntryQueryResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncCodex) -> None:
        with pytest.warns(DeprecationWarning):
            entry = await async_client.projects.entries.query(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                question="question",
                use_llm_matching=True,
                client_metadata={},
                query_metadata={
                    "context": "string",
                    "custom_metadata": {},
                    "eval_scores": {"foo": 0},
                    "evaluated_response": "evaluated_response",
                    "messages": [
                        {
                            "content": "string",
                            "role": "developer",
                            "name": "name",
                        }
                    ],
                    "original_question": "original_question",
                },
                x_client_library_version="x-client-library-version",
                x_integration_type="x-integration-type",
                x_source="x-source",
                x_stainless_package_version="x-stainless-package-version",
            )

        assert_matches_type(EntryQueryResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncCodex) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.projects.entries.with_raw_response.query(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                question="question",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(EntryQueryResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncCodex) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.projects.entries.with_streaming_response.query(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                question="question",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                entry = await response.parse()
                assert_matches_type(EntryQueryResponse, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_query(self, async_client: AsyncCodex) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
                await async_client.projects.entries.with_raw_response.query(
                    project_id="",
                    question="question",
                )

    @pytest.mark.skip()
    @parametrize
    async def test_method_unpublish_answer(self, async_client: AsyncCodex) -> None:
        entry = await async_client.projects.entries.unpublish_answer(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_unpublish_answer(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.entries.with_raw_response.unpublish_answer(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(Entry, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_unpublish_answer(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.entries.with_streaming_response.unpublish_answer(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(Entry, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_unpublish_answer(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.entries.with_raw_response.unpublish_answer(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.projects.entries.with_raw_response.unpublish_answer(
                entry_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
