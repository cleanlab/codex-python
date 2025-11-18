# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from codex import Codex, AsyncCodex
from tests.utils import assert_matches_type
from codex._utils import parse_datetime
from codex.pagination import SyncOffsetPageExpertAnswers, AsyncOffsetPageExpertAnswers
from codex.types.projects.remediations import (
    ExpertAnswerListResponse,
    ExpertAnswerPauseResponse,
    ExpertAnswerCreateResponse,
    ExpertAnswerPublishResponse,
    ExpertAnswerUnpauseResponse,
    ExpertAnswerRetrieveResponse,
    ExpertAnswerEditAnswerResponse,
    ExpertAnswerEditDraftAnswerResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExpertAnswers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Codex) -> None:
        expert_answer = client.projects.remediations.expert_answers.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
        )
        assert_matches_type(ExpertAnswerCreateResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Codex) -> None:
        expert_answer = client.projects.remediations.expert_answers.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
            answer="answer",
            draft_answer="draft_answer",
        )
        assert_matches_type(ExpertAnswerCreateResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Codex) -> None:
        response = client.projects.remediations.expert_answers.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = response.parse()
        assert_matches_type(ExpertAnswerCreateResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Codex) -> None:
        with client.projects.remediations.expert_answers.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = response.parse()
            assert_matches_type(ExpertAnswerCreateResponse, expert_answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.create(
                project_id="",
                query="x",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Codex) -> None:
        expert_answer = client.projects.remediations.expert_answers.retrieve(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpertAnswerRetrieveResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Codex) -> None:
        response = client.projects.remediations.expert_answers.with_raw_response.retrieve(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = response.parse()
        assert_matches_type(ExpertAnswerRetrieveResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Codex) -> None:
        with client.projects.remediations.expert_answers.with_streaming_response.retrieve(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = response.parse()
            assert_matches_type(ExpertAnswerRetrieveResponse, expert_answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.retrieve(
                expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_answer_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.retrieve(
                expert_answer_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Codex) -> None:
        expert_answer = client.projects.remediations.expert_answers.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncOffsetPageExpertAnswers[ExpertAnswerListResponse], expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Codex) -> None:
        expert_answer = client.projects.remediations.expert_answers.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_edited_at_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_edited_at_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_edited_by="last_edited_by",
            limit=1,
            offset=0,
            order="asc",
            sort="created_at",
            status=["ACTIVE"],
        )
        assert_matches_type(SyncOffsetPageExpertAnswers[ExpertAnswerListResponse], expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Codex) -> None:
        response = client.projects.remediations.expert_answers.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = response.parse()
        assert_matches_type(SyncOffsetPageExpertAnswers[ExpertAnswerListResponse], expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Codex) -> None:
        with client.projects.remediations.expert_answers.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = response.parse()
            assert_matches_type(SyncOffsetPageExpertAnswers[ExpertAnswerListResponse], expert_answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.list(
                project_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Codex) -> None:
        expert_answer = client.projects.remediations.expert_answers.delete(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert expert_answer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Codex) -> None:
        response = client.projects.remediations.expert_answers.with_raw_response.delete(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = response.parse()
        assert expert_answer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Codex) -> None:
        with client.projects.remediations.expert_answers.with_streaming_response.delete(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = response.parse()
            assert expert_answer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.delete(
                expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_answer_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.delete(
                expert_answer_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_edit_answer(self, client: Codex) -> None:
        expert_answer = client.projects.remediations.expert_answers.edit_answer(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            answer="answer",
        )
        assert_matches_type(ExpertAnswerEditAnswerResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_edit_answer(self, client: Codex) -> None:
        response = client.projects.remediations.expert_answers.with_raw_response.edit_answer(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            answer="answer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = response.parse()
        assert_matches_type(ExpertAnswerEditAnswerResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_edit_answer(self, client: Codex) -> None:
        with client.projects.remediations.expert_answers.with_streaming_response.edit_answer(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            answer="answer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = response.parse()
            assert_matches_type(ExpertAnswerEditAnswerResponse, expert_answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_edit_answer(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.edit_answer(
                expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
                answer="answer",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_answer_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.edit_answer(
                expert_answer_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                answer="answer",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_edit_draft_answer(self, client: Codex) -> None:
        expert_answer = client.projects.remediations.expert_answers.edit_draft_answer(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            draft_answer="draft_answer",
        )
        assert_matches_type(ExpertAnswerEditDraftAnswerResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_edit_draft_answer(self, client: Codex) -> None:
        response = client.projects.remediations.expert_answers.with_raw_response.edit_draft_answer(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            draft_answer="draft_answer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = response.parse()
        assert_matches_type(ExpertAnswerEditDraftAnswerResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_edit_draft_answer(self, client: Codex) -> None:
        with client.projects.remediations.expert_answers.with_streaming_response.edit_draft_answer(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            draft_answer="draft_answer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = response.parse()
            assert_matches_type(ExpertAnswerEditDraftAnswerResponse, expert_answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_edit_draft_answer(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.edit_draft_answer(
                expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
                draft_answer="draft_answer",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_answer_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.edit_draft_answer(
                expert_answer_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                draft_answer="draft_answer",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_pause(self, client: Codex) -> None:
        expert_answer = client.projects.remediations.expert_answers.pause(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpertAnswerPauseResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_pause(self, client: Codex) -> None:
        response = client.projects.remediations.expert_answers.with_raw_response.pause(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = response.parse()
        assert_matches_type(ExpertAnswerPauseResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_pause(self, client: Codex) -> None:
        with client.projects.remediations.expert_answers.with_streaming_response.pause(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = response.parse()
            assert_matches_type(ExpertAnswerPauseResponse, expert_answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_pause(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.pause(
                expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_answer_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.pause(
                expert_answer_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_publish(self, client: Codex) -> None:
        expert_answer = client.projects.remediations.expert_answers.publish(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpertAnswerPublishResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_publish(self, client: Codex) -> None:
        response = client.projects.remediations.expert_answers.with_raw_response.publish(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = response.parse()
        assert_matches_type(ExpertAnswerPublishResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_publish(self, client: Codex) -> None:
        with client.projects.remediations.expert_answers.with_streaming_response.publish(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = response.parse()
            assert_matches_type(ExpertAnswerPublishResponse, expert_answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_publish(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.publish(
                expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_answer_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.publish(
                expert_answer_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unpause(self, client: Codex) -> None:
        expert_answer = client.projects.remediations.expert_answers.unpause(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpertAnswerUnpauseResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unpause(self, client: Codex) -> None:
        response = client.projects.remediations.expert_answers.with_raw_response.unpause(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = response.parse()
        assert_matches_type(ExpertAnswerUnpauseResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unpause(self, client: Codex) -> None:
        with client.projects.remediations.expert_answers.with_streaming_response.unpause(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = response.parse()
            assert_matches_type(ExpertAnswerUnpauseResponse, expert_answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unpause(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.unpause(
                expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_answer_id` but received ''"):
            client.projects.remediations.expert_answers.with_raw_response.unpause(
                expert_answer_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncExpertAnswers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCodex) -> None:
        expert_answer = await async_client.projects.remediations.expert_answers.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
        )
        assert_matches_type(ExpertAnswerCreateResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCodex) -> None:
        expert_answer = await async_client.projects.remediations.expert_answers.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
            answer="answer",
            draft_answer="draft_answer",
        )
        assert_matches_type(ExpertAnswerCreateResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.expert_answers.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = await response.parse()
        assert_matches_type(ExpertAnswerCreateResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.expert_answers.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = await response.parse()
            assert_matches_type(ExpertAnswerCreateResponse, expert_answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.create(
                project_id="",
                query="x",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCodex) -> None:
        expert_answer = await async_client.projects.remediations.expert_answers.retrieve(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpertAnswerRetrieveResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.expert_answers.with_raw_response.retrieve(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = await response.parse()
        assert_matches_type(ExpertAnswerRetrieveResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.expert_answers.with_streaming_response.retrieve(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = await response.parse()
            assert_matches_type(ExpertAnswerRetrieveResponse, expert_answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.retrieve(
                expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_answer_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.retrieve(
                expert_answer_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCodex) -> None:
        expert_answer = await async_client.projects.remediations.expert_answers.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncOffsetPageExpertAnswers[ExpertAnswerListResponse], expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCodex) -> None:
        expert_answer = await async_client.projects.remediations.expert_answers.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_edited_at_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_edited_at_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_edited_by="last_edited_by",
            limit=1,
            offset=0,
            order="asc",
            sort="created_at",
            status=["ACTIVE"],
        )
        assert_matches_type(AsyncOffsetPageExpertAnswers[ExpertAnswerListResponse], expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.expert_answers.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = await response.parse()
        assert_matches_type(AsyncOffsetPageExpertAnswers[ExpertAnswerListResponse], expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.expert_answers.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = await response.parse()
            assert_matches_type(
                AsyncOffsetPageExpertAnswers[ExpertAnswerListResponse], expert_answer, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.list(
                project_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCodex) -> None:
        expert_answer = await async_client.projects.remediations.expert_answers.delete(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert expert_answer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.expert_answers.with_raw_response.delete(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = await response.parse()
        assert expert_answer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.expert_answers.with_streaming_response.delete(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = await response.parse()
            assert expert_answer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.delete(
                expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_answer_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.delete(
                expert_answer_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_edit_answer(self, async_client: AsyncCodex) -> None:
        expert_answer = await async_client.projects.remediations.expert_answers.edit_answer(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            answer="answer",
        )
        assert_matches_type(ExpertAnswerEditAnswerResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_edit_answer(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.expert_answers.with_raw_response.edit_answer(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            answer="answer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = await response.parse()
        assert_matches_type(ExpertAnswerEditAnswerResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_edit_answer(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.expert_answers.with_streaming_response.edit_answer(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            answer="answer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = await response.parse()
            assert_matches_type(ExpertAnswerEditAnswerResponse, expert_answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_edit_answer(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.edit_answer(
                expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
                answer="answer",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_answer_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.edit_answer(
                expert_answer_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                answer="answer",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_edit_draft_answer(self, async_client: AsyncCodex) -> None:
        expert_answer = await async_client.projects.remediations.expert_answers.edit_draft_answer(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            draft_answer="draft_answer",
        )
        assert_matches_type(ExpertAnswerEditDraftAnswerResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_edit_draft_answer(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.expert_answers.with_raw_response.edit_draft_answer(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            draft_answer="draft_answer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = await response.parse()
        assert_matches_type(ExpertAnswerEditDraftAnswerResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_edit_draft_answer(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.expert_answers.with_streaming_response.edit_draft_answer(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            draft_answer="draft_answer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = await response.parse()
            assert_matches_type(ExpertAnswerEditDraftAnswerResponse, expert_answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_edit_draft_answer(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.edit_draft_answer(
                expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
                draft_answer="draft_answer",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_answer_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.edit_draft_answer(
                expert_answer_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                draft_answer="draft_answer",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_pause(self, async_client: AsyncCodex) -> None:
        expert_answer = await async_client.projects.remediations.expert_answers.pause(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpertAnswerPauseResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.expert_answers.with_raw_response.pause(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = await response.parse()
        assert_matches_type(ExpertAnswerPauseResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.expert_answers.with_streaming_response.pause(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = await response.parse()
            assert_matches_type(ExpertAnswerPauseResponse, expert_answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_pause(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.pause(
                expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_answer_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.pause(
                expert_answer_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_publish(self, async_client: AsyncCodex) -> None:
        expert_answer = await async_client.projects.remediations.expert_answers.publish(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpertAnswerPublishResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.expert_answers.with_raw_response.publish(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = await response.parse()
        assert_matches_type(ExpertAnswerPublishResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.expert_answers.with_streaming_response.publish(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = await response.parse()
            assert_matches_type(ExpertAnswerPublishResponse, expert_answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_publish(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.publish(
                expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_answer_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.publish(
                expert_answer_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unpause(self, async_client: AsyncCodex) -> None:
        expert_answer = await async_client.projects.remediations.expert_answers.unpause(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpertAnswerUnpauseResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unpause(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.expert_answers.with_raw_response.unpause(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_answer = await response.parse()
        assert_matches_type(ExpertAnswerUnpauseResponse, expert_answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unpause(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.expert_answers.with_streaming_response.unpause(
            expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_answer = await response.parse()
            assert_matches_type(ExpertAnswerUnpauseResponse, expert_answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unpause(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.unpause(
                expert_answer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_answer_id` but received ''"):
            await async_client.projects.remediations.expert_answers.with_raw_response.unpause(
                expert_answer_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
