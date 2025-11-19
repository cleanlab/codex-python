# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from codex import Codex, AsyncCodex
from tests.utils import assert_matches_type
from codex._utils import parse_datetime
from codex.pagination import SyncOffsetPageExpertReviews, AsyncOffsetPageExpertReviews
from codex.types.projects.remediations import (
    ExpertReviewEditResponse,
    ExpertReviewListResponse,
    ExpertReviewCreateResponse,
    ExpertReviewRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExpertReviews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Codex) -> None:
        expert_review = client.projects.remediations.expert_reviews.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            original_query_log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            review_status="good",
        )
        assert_matches_type(ExpertReviewCreateResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Codex) -> None:
        expert_review = client.projects.remediations.expert_reviews.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            original_query_log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            review_status="good",
            generate_guidance=True,
            explanation="explanation",
        )
        assert_matches_type(ExpertReviewCreateResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Codex) -> None:
        response = client.projects.remediations.expert_reviews.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            original_query_log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            review_status="good",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_review = response.parse()
        assert_matches_type(ExpertReviewCreateResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Codex) -> None:
        with client.projects.remediations.expert_reviews.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            original_query_log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            review_status="good",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_review = response.parse()
            assert_matches_type(ExpertReviewCreateResponse, expert_review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.expert_reviews.with_raw_response.create(
                project_id="",
                original_query_log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                review_status="good",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Codex) -> None:
        expert_review = client.projects.remediations.expert_reviews.retrieve(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpertReviewRetrieveResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Codex) -> None:
        response = client.projects.remediations.expert_reviews.with_raw_response.retrieve(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_review = response.parse()
        assert_matches_type(ExpertReviewRetrieveResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Codex) -> None:
        with client.projects.remediations.expert_reviews.with_streaming_response.retrieve(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_review = response.parse()
            assert_matches_type(ExpertReviewRetrieveResponse, expert_review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.expert_reviews.with_raw_response.retrieve(
                expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_review_id` but received ''"):
            client.projects.remediations.expert_reviews.with_raw_response.retrieve(
                expert_review_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Codex) -> None:
        expert_review = client.projects.remediations.expert_reviews.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncOffsetPageExpertReviews[ExpertReviewListResponse], expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Codex) -> None:
        expert_review = client.projects.remediations.expert_reviews.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_edited_at_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_edited_at_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_edited_by="last_edited_by",
            limit=1,
            offset=0,
            order="asc",
            review_status=["good"],
            sort="created_at",
        )
        assert_matches_type(SyncOffsetPageExpertReviews[ExpertReviewListResponse], expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Codex) -> None:
        response = client.projects.remediations.expert_reviews.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_review = response.parse()
        assert_matches_type(SyncOffsetPageExpertReviews[ExpertReviewListResponse], expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Codex) -> None:
        with client.projects.remediations.expert_reviews.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_review = response.parse()
            assert_matches_type(SyncOffsetPageExpertReviews[ExpertReviewListResponse], expert_review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.expert_reviews.with_raw_response.list(
                project_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Codex) -> None:
        expert_review = client.projects.remediations.expert_reviews.delete(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert expert_review is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Codex) -> None:
        expert_review = client.projects.remediations.expert_reviews.delete(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            original_query_log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert expert_review is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Codex) -> None:
        response = client.projects.remediations.expert_reviews.with_raw_response.delete(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_review = response.parse()
        assert expert_review is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Codex) -> None:
        with client.projects.remediations.expert_reviews.with_streaming_response.delete(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_review = response.parse()
            assert expert_review is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.expert_reviews.with_raw_response.delete(
                expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_review_id` but received ''"):
            client.projects.remediations.expert_reviews.with_raw_response.delete(
                expert_review_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_edit(self, client: Codex) -> None:
        expert_review = client.projects.remediations.expert_reviews.edit(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpertReviewEditResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_edit_with_all_params(self, client: Codex) -> None:
        expert_review = client.projects.remediations.expert_reviews.edit(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            explanation="explanation",
            review_status="good",
        )
        assert_matches_type(ExpertReviewEditResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_edit(self, client: Codex) -> None:
        response = client.projects.remediations.expert_reviews.with_raw_response.edit(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_review = response.parse()
        assert_matches_type(ExpertReviewEditResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_edit(self, client: Codex) -> None:
        with client.projects.remediations.expert_reviews.with_streaming_response.edit(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_review = response.parse()
            assert_matches_type(ExpertReviewEditResponse, expert_review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_edit(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.remediations.expert_reviews.with_raw_response.edit(
                expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_review_id` but received ''"):
            client.projects.remediations.expert_reviews.with_raw_response.edit(
                expert_review_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncExpertReviews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCodex) -> None:
        expert_review = await async_client.projects.remediations.expert_reviews.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            original_query_log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            review_status="good",
        )
        assert_matches_type(ExpertReviewCreateResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCodex) -> None:
        expert_review = await async_client.projects.remediations.expert_reviews.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            original_query_log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            review_status="good",
            generate_guidance=True,
            explanation="explanation",
        )
        assert_matches_type(ExpertReviewCreateResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.expert_reviews.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            original_query_log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            review_status="good",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_review = await response.parse()
        assert_matches_type(ExpertReviewCreateResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.expert_reviews.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            original_query_log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            review_status="good",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_review = await response.parse()
            assert_matches_type(ExpertReviewCreateResponse, expert_review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.expert_reviews.with_raw_response.create(
                project_id="",
                original_query_log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                review_status="good",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCodex) -> None:
        expert_review = await async_client.projects.remediations.expert_reviews.retrieve(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpertReviewRetrieveResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.expert_reviews.with_raw_response.retrieve(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_review = await response.parse()
        assert_matches_type(ExpertReviewRetrieveResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.expert_reviews.with_streaming_response.retrieve(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_review = await response.parse()
            assert_matches_type(ExpertReviewRetrieveResponse, expert_review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.expert_reviews.with_raw_response.retrieve(
                expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_review_id` but received ''"):
            await async_client.projects.remediations.expert_reviews.with_raw_response.retrieve(
                expert_review_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCodex) -> None:
        expert_review = await async_client.projects.remediations.expert_reviews.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncOffsetPageExpertReviews[ExpertReviewListResponse], expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCodex) -> None:
        expert_review = await async_client.projects.remediations.expert_reviews.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_edited_at_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_edited_at_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_edited_by="last_edited_by",
            limit=1,
            offset=0,
            order="asc",
            review_status=["good"],
            sort="created_at",
        )
        assert_matches_type(AsyncOffsetPageExpertReviews[ExpertReviewListResponse], expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.expert_reviews.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_review = await response.parse()
        assert_matches_type(AsyncOffsetPageExpertReviews[ExpertReviewListResponse], expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.expert_reviews.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_review = await response.parse()
            assert_matches_type(
                AsyncOffsetPageExpertReviews[ExpertReviewListResponse], expert_review, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.expert_reviews.with_raw_response.list(
                project_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCodex) -> None:
        expert_review = await async_client.projects.remediations.expert_reviews.delete(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert expert_review is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCodex) -> None:
        expert_review = await async_client.projects.remediations.expert_reviews.delete(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            original_query_log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert expert_review is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.expert_reviews.with_raw_response.delete(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_review = await response.parse()
        assert expert_review is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.expert_reviews.with_streaming_response.delete(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_review = await response.parse()
            assert expert_review is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.expert_reviews.with_raw_response.delete(
                expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_review_id` but received ''"):
            await async_client.projects.remediations.expert_reviews.with_raw_response.delete(
                expert_review_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCodex) -> None:
        expert_review = await async_client.projects.remediations.expert_reviews.edit(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExpertReviewEditResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCodex) -> None:
        expert_review = await async_client.projects.remediations.expert_reviews.edit(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            explanation="explanation",
            review_status="good",
        )
        assert_matches_type(ExpertReviewEditResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.remediations.expert_reviews.with_raw_response.edit(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expert_review = await response.parse()
        assert_matches_type(ExpertReviewEditResponse, expert_review, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.remediations.expert_reviews.with_streaming_response.edit(
            expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expert_review = await response.parse()
            assert_matches_type(ExpertReviewEditResponse, expert_review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.remediations.expert_reviews.with_raw_response.edit(
                expert_review_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expert_review_id` but received ''"):
            await async_client.projects.remediations.expert_reviews.with_raw_response.edit(
                expert_review_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
