# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from codex import Codex, AsyncCodex
from codex.types import ProjectReturnSchema
from tests.utils import assert_matches_type
from codex.types.projects import EvalListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Codex) -> None:
        eval = client.projects.evals.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            eval_key="eval_key",
            name="name",
        )
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Codex) -> None:
        eval = client.projects.evals.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            eval_key="eval_key",
            name="name",
            context_identifier="context_identifier",
            enabled=True,
            is_default=True,
            priority=0,
            query_identifier="query_identifier",
            response_identifier="response_identifier",
            should_escalate=True,
            threshold=0,
            threshold_direction="above",
        )
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Codex) -> None:
        response = client.projects.evals.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            eval_key="eval_key",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Codex) -> None:
        with client.projects.evals.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            eval_key="eval_key",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(ProjectReturnSchema, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.evals.with_raw_response.create(
                project_id="",
                criteria="criteria",
                eval_key="eval_key",
                name="name",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_1(self, client: Codex) -> None:
        eval = client.projects.evals.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            body_eval_key="eval_key",
            name="name",
        )
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Codex) -> None:
        eval = client.projects.evals.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            body_eval_key="eval_key",
            name="name",
            context_identifier="context_identifier",
            enabled=True,
            is_default=True,
            priority=0,
            query_identifier="query_identifier",
            response_identifier="response_identifier",
            should_escalate=True,
            threshold=0,
            threshold_direction="above",
        )
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_1(self, client: Codex) -> None:
        response = client.projects.evals.with_raw_response.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            body_eval_key="eval_key",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Codex) -> None:
        with client.projects.evals.with_streaming_response.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            body_eval_key="eval_key",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(ProjectReturnSchema, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_1(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.evals.with_raw_response.update(
                path_eval_key="eval_key",
                project_id="",
                criteria="criteria",
                body_eval_key="eval_key",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_eval_key` but received ''"):
            client.projects.evals.with_raw_response.update(
                path_eval_key="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                criteria="criteria",
                body_eval_key="eval_key",
                name="name",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_2(self, client: Codex) -> None:
        eval = client.projects.evals.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_eval_key="eval_key",
        )
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Codex) -> None:
        eval = client.projects.evals.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_eval_key="eval_key",
            enabled=True,
            priority=0,
            should_escalate=True,
            threshold=0,
            threshold_direction="above",
        )
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_2(self, client: Codex) -> None:
        response = client.projects.evals.with_raw_response.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_eval_key="eval_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Codex) -> None:
        with client.projects.evals.with_streaming_response.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_eval_key="eval_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(ProjectReturnSchema, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_2(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.evals.with_raw_response.update(
                path_eval_key="eval_key",
                project_id="",
                body_eval_key="eval_key",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_eval_key` but received ''"):
            client.projects.evals.with_raw_response.update(
                path_eval_key="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body_eval_key="eval_key",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Codex) -> None:
        eval = client.projects.evals.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EvalListResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Codex) -> None:
        response = client.projects.evals.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(EvalListResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Codex) -> None:
        with client.projects.evals.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(EvalListResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.evals.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Codex) -> None:
        eval = client.projects.evals.delete(
            eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Codex) -> None:
        response = client.projects.evals.with_raw_response.delete(
            eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Codex) -> None:
        with client.projects.evals.with_streaming_response.delete(
            eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(ProjectReturnSchema, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.evals.with_raw_response.delete(
                eval_key="eval_key",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_key` but received ''"):
            client.projects.evals.with_raw_response.delete(
                eval_key="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncEvals:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCodex) -> None:
        eval = await async_client.projects.evals.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            eval_key="eval_key",
            name="name",
        )
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCodex) -> None:
        eval = await async_client.projects.evals.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            eval_key="eval_key",
            name="name",
            context_identifier="context_identifier",
            enabled=True,
            is_default=True,
            priority=0,
            query_identifier="query_identifier",
            response_identifier="response_identifier",
            should_escalate=True,
            threshold=0,
            threshold_direction="above",
        )
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.evals.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            eval_key="eval_key",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.evals.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            eval_key="eval_key",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(ProjectReturnSchema, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.evals.with_raw_response.create(
                project_id="",
                criteria="criteria",
                eval_key="eval_key",
                name="name",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCodex) -> None:
        eval = await async_client.projects.evals.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            body_eval_key="eval_key",
            name="name",
        )
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncCodex) -> None:
        eval = await async_client.projects.evals.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            body_eval_key="eval_key",
            name="name",
            context_identifier="context_identifier",
            enabled=True,
            is_default=True,
            priority=0,
            query_identifier="query_identifier",
            response_identifier="response_identifier",
            should_escalate=True,
            threshold=0,
            threshold_direction="above",
        )
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.evals.with_raw_response.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            body_eval_key="eval_key",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.evals.with_streaming_response.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria="criteria",
            body_eval_key="eval_key",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(ProjectReturnSchema, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.evals.with_raw_response.update(
                path_eval_key="eval_key",
                project_id="",
                criteria="criteria",
                body_eval_key="eval_key",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_eval_key` but received ''"):
            await async_client.projects.evals.with_raw_response.update(
                path_eval_key="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                criteria="criteria",
                body_eval_key="eval_key",
                name="name",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCodex) -> None:
        eval = await async_client.projects.evals.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_eval_key="eval_key",
        )
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncCodex) -> None:
        eval = await async_client.projects.evals.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_eval_key="eval_key",
            enabled=True,
            priority=0,
            should_escalate=True,
            threshold=0,
            threshold_direction="above",
        )
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.evals.with_raw_response.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_eval_key="eval_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.evals.with_streaming_response.update(
            path_eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_eval_key="eval_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(ProjectReturnSchema, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.evals.with_raw_response.update(
                path_eval_key="eval_key",
                project_id="",
                body_eval_key="eval_key",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_eval_key` but received ''"):
            await async_client.projects.evals.with_raw_response.update(
                path_eval_key="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body_eval_key="eval_key",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCodex) -> None:
        eval = await async_client.projects.evals.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EvalListResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.evals.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(EvalListResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.evals.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(EvalListResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.evals.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCodex) -> None:
        eval = await async_client.projects.evals.delete(
            eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.evals.with_raw_response.delete(
            eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(ProjectReturnSchema, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.evals.with_streaming_response.delete(
            eval_key="eval_key",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(ProjectReturnSchema, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.evals.with_raw_response.delete(
                eval_key="eval_key",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_key` but received ''"):
            await async_client.projects.evals.with_raw_response.delete(
                eval_key="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
