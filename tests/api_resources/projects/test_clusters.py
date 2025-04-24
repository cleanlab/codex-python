# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from codex import Codex, AsyncCodex
from tests.utils import assert_matches_type
from codex.pagination import SyncOffsetPageClusters, AsyncOffsetPageClusters
from codex.types.projects import ClusterListResponse, ClusterListVariantsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClusters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Codex) -> None:
        cluster = client.projects.clusters.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncOffsetPageClusters[ClusterListResponse], cluster, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Codex) -> None:
        cluster = client.projects.clusters.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            eval_issue_types=["hallucination"],
            instruction_adherence_failure="html_format",
            limit=1,
            offset=0,
            order="asc",
            sort="created_at",
            states=["unanswered"],
        )
        assert_matches_type(SyncOffsetPageClusters[ClusterListResponse], cluster, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Codex) -> None:
        response = client.projects.clusters.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(SyncOffsetPageClusters[ClusterListResponse], cluster, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Codex) -> None:
        with client.projects.clusters.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(SyncOffsetPageClusters[ClusterListResponse], cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.clusters.with_raw_response.list(
                project_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_variants(self, client: Codex) -> None:
        cluster = client.projects.clusters.list_variants(
            representative_entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ClusterListVariantsResponse, cluster, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_variants(self, client: Codex) -> None:
        response = client.projects.clusters.with_raw_response.list_variants(
            representative_entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(ClusterListVariantsResponse, cluster, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_variants(self, client: Codex) -> None:
        with client.projects.clusters.with_streaming_response.list_variants(
            representative_entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(ClusterListVariantsResponse, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_variants(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.clusters.with_raw_response.list_variants(
                representative_entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `representative_entry_id` but received ''"
        ):
            client.projects.clusters.with_raw_response.list_variants(
                representative_entry_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncClusters:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCodex) -> None:
        cluster = await async_client.projects.clusters.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncOffsetPageClusters[ClusterListResponse], cluster, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCodex) -> None:
        cluster = await async_client.projects.clusters.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            eval_issue_types=["hallucination"],
            instruction_adherence_failure="html_format",
            limit=1,
            offset=0,
            order="asc",
            sort="created_at",
            states=["unanswered"],
        )
        assert_matches_type(AsyncOffsetPageClusters[ClusterListResponse], cluster, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.clusters.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(AsyncOffsetPageClusters[ClusterListResponse], cluster, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.clusters.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(AsyncOffsetPageClusters[ClusterListResponse], cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.clusters.with_raw_response.list(
                project_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_variants(self, async_client: AsyncCodex) -> None:
        cluster = await async_client.projects.clusters.list_variants(
            representative_entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ClusterListVariantsResponse, cluster, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_variants(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.clusters.with_raw_response.list_variants(
            representative_entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(ClusterListVariantsResponse, cluster, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_variants(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.clusters.with_streaming_response.list_variants(
            representative_entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(ClusterListVariantsResponse, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_variants(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.clusters.with_raw_response.list_variants(
                representative_entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `representative_entry_id` but received ''"
        ):
            await async_client.projects.clusters.with_raw_response.list_variants(
                representative_entry_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
