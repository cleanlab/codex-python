# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from codex import Codex, AsyncCodex
from tests.utils import assert_matches_type
from codex._utils import parse_datetime
from codex.types.projects import (
    RemediationListResponse,
    RemediationPauseResponse,
    RemediationCreateResponse,
    RemediationPublishResponse,
    RemediationUnpauseResponse,
    RemediationRetrieveResponse,
    RemediationEditAnswerResponse,
    RemediationEditDraftAnswerResponse,
    RemediationListResolvedLogsResponse,
    RemediationGetResolvedLogsCountResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRemediations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Codex) -> None:
        remediation = client.projects.remediations.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
        )
        assert_matches_type(RemediationCreateResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Codex) -> None:
        remediation = client.projects.remediations.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
            answer="answer",
            draft_answer="draft_answer",
        )
        assert_matches_type(RemediationCreateResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Codex) -> None:
        response = client.projects.remediations.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = response.parse()
        assert_matches_type(RemediationCreateResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Codex) -> None:
        with client.projects.remediations.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = response.parse()
            assert_matches_type(RemediationCreateResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.with_raw_response.create(
                project_id="",
                question="question",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Codex) -> None:
        remediation = client.projects.remediations.retrieve(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemediationRetrieveResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Codex) -> None:
        response = client.projects.remediations.with_raw_response.retrieve(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = response.parse()
        assert_matches_type(RemediationRetrieveResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Codex) -> None:
        with client.projects.remediations.with_streaming_response.retrieve(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = response.parse()
            assert_matches_type(RemediationRetrieveResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.with_raw_response.retrieve(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            client.projects.remediations.with_raw_response.retrieve(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Codex) -> None:
        remediation = client.projects.remediations.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemediationListResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Codex) -> None:
        remediation = client.projects.remediations.list(
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
        assert_matches_type(RemediationListResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Codex) -> None:
        response = client.projects.remediations.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = response.parse()
        assert_matches_type(RemediationListResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Codex) -> None:
        with client.projects.remediations.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = response.parse()
            assert_matches_type(RemediationListResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.with_raw_response.list(
                project_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Codex) -> None:
        remediation = client.projects.remediations.delete(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert remediation is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Codex) -> None:
        response = client.projects.remediations.with_raw_response.delete(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = response.parse()
        assert remediation is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Codex) -> None:
        with client.projects.remediations.with_streaming_response.delete(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = response.parse()
            assert remediation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.with_raw_response.delete(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            client.projects.remediations.with_raw_response.delete(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_answer(self, client: Codex) -> None:
        remediation = client.projects.remediations.edit_answer(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            answer="answer",
        )
        assert_matches_type(RemediationEditAnswerResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit_answer(self, client: Codex) -> None:
        response = client.projects.remediations.with_raw_response.edit_answer(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            answer="answer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = response.parse()
        assert_matches_type(RemediationEditAnswerResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit_answer(self, client: Codex) -> None:
        with client.projects.remediations.with_streaming_response.edit_answer(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            answer="answer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = response.parse()
            assert_matches_type(RemediationEditAnswerResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit_answer(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.with_raw_response.edit_answer(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
                answer="answer",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            client.projects.remediations.with_raw_response.edit_answer(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                answer="answer",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_draft_answer(self, client: Codex) -> None:
        remediation = client.projects.remediations.edit_draft_answer(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            draft_answer="draft_answer",
        )
        assert_matches_type(RemediationEditDraftAnswerResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit_draft_answer(self, client: Codex) -> None:
        response = client.projects.remediations.with_raw_response.edit_draft_answer(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            draft_answer="draft_answer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = response.parse()
        assert_matches_type(RemediationEditDraftAnswerResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit_draft_answer(self, client: Codex) -> None:
        with client.projects.remediations.with_streaming_response.edit_draft_answer(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            draft_answer="draft_answer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = response.parse()
            assert_matches_type(RemediationEditDraftAnswerResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit_draft_answer(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.with_raw_response.edit_draft_answer(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
                draft_answer="draft_answer",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            client.projects.remediations.with_raw_response.edit_draft_answer(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                draft_answer="draft_answer",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_resolved_logs_count(self, client: Codex) -> None:
        remediation = client.projects.remediations.get_resolved_logs_count(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemediationGetResolvedLogsCountResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_resolved_logs_count(self, client: Codex) -> None:
        response = client.projects.remediations.with_raw_response.get_resolved_logs_count(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = response.parse()
        assert_matches_type(RemediationGetResolvedLogsCountResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_resolved_logs_count(self, client: Codex) -> None:
        with client.projects.remediations.with_streaming_response.get_resolved_logs_count(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = response.parse()
            assert_matches_type(RemediationGetResolvedLogsCountResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_resolved_logs_count(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.with_raw_response.get_resolved_logs_count(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            client.projects.remediations.with_raw_response.get_resolved_logs_count(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_resolved_logs(self, client: Codex) -> None:
        remediation = client.projects.remediations.list_resolved_logs(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemediationListResolvedLogsResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_resolved_logs(self, client: Codex) -> None:
        response = client.projects.remediations.with_raw_response.list_resolved_logs(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = response.parse()
        assert_matches_type(RemediationListResolvedLogsResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_resolved_logs(self, client: Codex) -> None:
        with client.projects.remediations.with_streaming_response.list_resolved_logs(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = response.parse()
            assert_matches_type(RemediationListResolvedLogsResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_resolved_logs(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.with_raw_response.list_resolved_logs(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            client.projects.remediations.with_raw_response.list_resolved_logs(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_pause(self, client: Codex) -> None:
        remediation = client.projects.remediations.pause(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemediationPauseResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_pause(self, client: Codex) -> None:
        response = client.projects.remediations.with_raw_response.pause(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = response.parse()
        assert_matches_type(RemediationPauseResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_pause(self, client: Codex) -> None:
        with client.projects.remediations.with_streaming_response.pause(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = response.parse()
            assert_matches_type(RemediationPauseResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_pause(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.with_raw_response.pause(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            client.projects.remediations.with_raw_response.pause(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_publish(self, client: Codex) -> None:
        remediation = client.projects.remediations.publish(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemediationPublishResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_publish(self, client: Codex) -> None:
        response = client.projects.remediations.with_raw_response.publish(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = response.parse()
        assert_matches_type(RemediationPublishResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_publish(self, client: Codex) -> None:
        with client.projects.remediations.with_streaming_response.publish(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = response.parse()
            assert_matches_type(RemediationPublishResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_publish(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.with_raw_response.publish(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            client.projects.remediations.with_raw_response.publish(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_unpause(self, client: Codex) -> None:
        remediation = client.projects.remediations.unpause(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemediationUnpauseResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_unpause(self, client: Codex) -> None:
        response = client.projects.remediations.with_raw_response.unpause(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = response.parse()
        assert_matches_type(RemediationUnpauseResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_unpause(self, client: Codex) -> None:
        with client.projects.remediations.with_streaming_response.unpause(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = response.parse()
            assert_matches_type(RemediationUnpauseResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_unpause(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.with_raw_response.unpause(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            client.projects.remediations.with_raw_response.unpause(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncRemediations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCodex) -> None:
        remediation = await async_client.projects.remediations.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
        )
        assert_matches_type(RemediationCreateResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCodex) -> None:
        remediation = await async_client.projects.remediations.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
            answer="answer",
            draft_answer="draft_answer",
        )
        assert_matches_type(RemediationCreateResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = await response.parse()
        assert_matches_type(RemediationCreateResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = await response.parse()
            assert_matches_type(RemediationCreateResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.create(
                project_id="",
                question="question",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCodex) -> None:
        remediation = await async_client.projects.remediations.retrieve(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemediationRetrieveResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.with_raw_response.retrieve(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = await response.parse()
        assert_matches_type(RemediationRetrieveResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.with_streaming_response.retrieve(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = await response.parse()
            assert_matches_type(RemediationRetrieveResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.retrieve(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.retrieve(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCodex) -> None:
        remediation = await async_client.projects.remediations.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemediationListResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCodex) -> None:
        remediation = await async_client.projects.remediations.list(
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
        assert_matches_type(RemediationListResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = await response.parse()
        assert_matches_type(RemediationListResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = await response.parse()
            assert_matches_type(RemediationListResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.list(
                project_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCodex) -> None:
        remediation = await async_client.projects.remediations.delete(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert remediation is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.with_raw_response.delete(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = await response.parse()
        assert remediation is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.with_streaming_response.delete(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = await response.parse()
            assert remediation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.delete(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.delete(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_answer(self, async_client: AsyncCodex) -> None:
        remediation = await async_client.projects.remediations.edit_answer(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            answer="answer",
        )
        assert_matches_type(RemediationEditAnswerResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit_answer(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.with_raw_response.edit_answer(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            answer="answer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = await response.parse()
        assert_matches_type(RemediationEditAnswerResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit_answer(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.with_streaming_response.edit_answer(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            answer="answer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = await response.parse()
            assert_matches_type(RemediationEditAnswerResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit_answer(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.edit_answer(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
                answer="answer",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.edit_answer(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                answer="answer",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_draft_answer(self, async_client: AsyncCodex) -> None:
        remediation = await async_client.projects.remediations.edit_draft_answer(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            draft_answer="draft_answer",
        )
        assert_matches_type(RemediationEditDraftAnswerResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit_draft_answer(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.with_raw_response.edit_draft_answer(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            draft_answer="draft_answer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = await response.parse()
        assert_matches_type(RemediationEditDraftAnswerResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit_draft_answer(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.with_streaming_response.edit_draft_answer(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            draft_answer="draft_answer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = await response.parse()
            assert_matches_type(RemediationEditDraftAnswerResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit_draft_answer(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.edit_draft_answer(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
                draft_answer="draft_answer",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.edit_draft_answer(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                draft_answer="draft_answer",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_resolved_logs_count(self, async_client: AsyncCodex) -> None:
        remediation = await async_client.projects.remediations.get_resolved_logs_count(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemediationGetResolvedLogsCountResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_resolved_logs_count(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.with_raw_response.get_resolved_logs_count(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = await response.parse()
        assert_matches_type(RemediationGetResolvedLogsCountResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_resolved_logs_count(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.with_streaming_response.get_resolved_logs_count(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = await response.parse()
            assert_matches_type(RemediationGetResolvedLogsCountResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_resolved_logs_count(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.get_resolved_logs_count(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.get_resolved_logs_count(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_resolved_logs(self, async_client: AsyncCodex) -> None:
        remediation = await async_client.projects.remediations.list_resolved_logs(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemediationListResolvedLogsResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_resolved_logs(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.with_raw_response.list_resolved_logs(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = await response.parse()
        assert_matches_type(RemediationListResolvedLogsResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_resolved_logs(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.with_streaming_response.list_resolved_logs(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = await response.parse()
            assert_matches_type(RemediationListResolvedLogsResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_resolved_logs(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.list_resolved_logs(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.list_resolved_logs(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_pause(self, async_client: AsyncCodex) -> None:
        remediation = await async_client.projects.remediations.pause(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemediationPauseResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.with_raw_response.pause(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = await response.parse()
        assert_matches_type(RemediationPauseResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.with_streaming_response.pause(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = await response.parse()
            assert_matches_type(RemediationPauseResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_pause(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.pause(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.pause(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_publish(self, async_client: AsyncCodex) -> None:
        remediation = await async_client.projects.remediations.publish(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemediationPublishResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.with_raw_response.publish(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = await response.parse()
        assert_matches_type(RemediationPublishResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.with_streaming_response.publish(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = await response.parse()
            assert_matches_type(RemediationPublishResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_publish(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.publish(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.publish(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_unpause(self, async_client: AsyncCodex) -> None:
        remediation = await async_client.projects.remediations.unpause(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemediationUnpauseResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_unpause(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.with_raw_response.unpause(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = await response.parse()
        assert_matches_type(RemediationUnpauseResponse, remediation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_unpause(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.with_streaming_response.unpause(
            remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = await response.parse()
            assert_matches_type(RemediationUnpauseResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_unpause(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.unpause(
                remediation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            await async_client.projects.remediations.with_raw_response.unpause(
                remediation_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
