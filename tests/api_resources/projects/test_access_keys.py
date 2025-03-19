# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from codex import Codex, AsyncCodex
from tests.utils import assert_matches_type
from codex._utils import parse_datetime
from codex.types.projects import (
    AccessKeySchema,
    AccessKeyListResponse,
    AccessKeyRetrieveProjectIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Codex) -> None:
        access_key = client.projects.access_keys.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Codex) -> None:
        access_key = client.projects.access_keys.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            description="description",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            x_client_library_version="x-client-library-version",
            x_integration_type="x-integration-type",
            x_source="x-source",
            x_stainless_package_version="x-stainless-package-version",
        )
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Codex) -> None:
        response = client.projects.access_keys.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = response.parse()
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Codex) -> None:
        with client.projects.access_keys.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = response.parse()
            assert_matches_type(AccessKeySchema, access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.access_keys.with_raw_response.create(
                project_id="",
                name="name",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Codex) -> None:
        access_key = client.projects.access_keys.retrieve(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Codex) -> None:
        response = client.projects.access_keys.with_raw_response.retrieve(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = response.parse()
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Codex) -> None:
        with client.projects.access_keys.with_streaming_response.retrieve(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = response.parse()
            assert_matches_type(AccessKeySchema, access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.access_keys.with_raw_response.retrieve(
                access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_key_id` but received ''"):
            client.projects.access_keys.with_raw_response.retrieve(
                access_key_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Codex) -> None:
        access_key = client.projects.access_keys.update(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Codex) -> None:
        access_key = client.projects.access_keys.update(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            description="description",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Codex) -> None:
        response = client.projects.access_keys.with_raw_response.update(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = response.parse()
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Codex) -> None:
        with client.projects.access_keys.with_streaming_response.update(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = response.parse()
            assert_matches_type(AccessKeySchema, access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.access_keys.with_raw_response.update(
                access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_key_id` but received ''"):
            client.projects.access_keys.with_raw_response.update(
                access_key_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                name="name",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Codex) -> None:
        access_key = client.projects.access_keys.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccessKeyListResponse, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Codex) -> None:
        response = client.projects.access_keys.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = response.parse()
        assert_matches_type(AccessKeyListResponse, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Codex) -> None:
        with client.projects.access_keys.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = response.parse()
            assert_matches_type(AccessKeyListResponse, access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.access_keys.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Codex) -> None:
        access_key = client.projects.access_keys.delete(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert access_key is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Codex) -> None:
        response = client.projects.access_keys.with_raw_response.delete(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = response.parse()
        assert access_key is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Codex) -> None:
        with client.projects.access_keys.with_streaming_response.delete(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = response.parse()
            assert access_key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.access_keys.with_raw_response.delete(
                access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_key_id` but received ''"):
            client.projects.access_keys.with_raw_response.delete(
                access_key_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_project_id(self, client: Codex) -> None:
        access_key = client.projects.access_keys.retrieve_project_id()
        assert_matches_type(AccessKeyRetrieveProjectIDResponse, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_project_id(self, client: Codex) -> None:
        response = client.projects.access_keys.with_raw_response.retrieve_project_id()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = response.parse()
        assert_matches_type(AccessKeyRetrieveProjectIDResponse, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_project_id(self, client: Codex) -> None:
        with client.projects.access_keys.with_streaming_response.retrieve_project_id() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = response.parse()
            assert_matches_type(AccessKeyRetrieveProjectIDResponse, access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_revoke(self, client: Codex) -> None:
        access_key = client.projects.access_keys.revoke(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert access_key is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_revoke(self, client: Codex) -> None:
        response = client.projects.access_keys.with_raw_response.revoke(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = response.parse()
        assert access_key is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_revoke(self, client: Codex) -> None:
        with client.projects.access_keys.with_streaming_response.revoke(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = response.parse()
            assert access_key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_revoke(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.access_keys.with_raw_response.revoke(
                access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_key_id` but received ''"):
            client.projects.access_keys.with_raw_response.revoke(
                access_key_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncAccessKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCodex) -> None:
        access_key = await async_client.projects.access_keys.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCodex) -> None:
        access_key = await async_client.projects.access_keys.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            description="description",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            x_client_library_version="x-client-library-version",
            x_integration_type="x-integration-type",
            x_source="x-source",
            x_stainless_package_version="x-stainless-package-version",
        )
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.access_keys.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = await response.parse()
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.access_keys.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = await response.parse()
            assert_matches_type(AccessKeySchema, access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.access_keys.with_raw_response.create(
                project_id="",
                name="name",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCodex) -> None:
        access_key = await async_client.projects.access_keys.retrieve(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.access_keys.with_raw_response.retrieve(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = await response.parse()
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.access_keys.with_streaming_response.retrieve(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = await response.parse()
            assert_matches_type(AccessKeySchema, access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.access_keys.with_raw_response.retrieve(
                access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_key_id` but received ''"):
            await async_client.projects.access_keys.with_raw_response.retrieve(
                access_key_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCodex) -> None:
        access_key = await async_client.projects.access_keys.update(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCodex) -> None:
        access_key = await async_client.projects.access_keys.update(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            description="description",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.access_keys.with_raw_response.update(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = await response.parse()
        assert_matches_type(AccessKeySchema, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.access_keys.with_streaming_response.update(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = await response.parse()
            assert_matches_type(AccessKeySchema, access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.access_keys.with_raw_response.update(
                access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_key_id` but received ''"):
            await async_client.projects.access_keys.with_raw_response.update(
                access_key_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                name="name",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCodex) -> None:
        access_key = await async_client.projects.access_keys.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccessKeyListResponse, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.access_keys.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = await response.parse()
        assert_matches_type(AccessKeyListResponse, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.access_keys.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = await response.parse()
            assert_matches_type(AccessKeyListResponse, access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.access_keys.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCodex) -> None:
        access_key = await async_client.projects.access_keys.delete(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert access_key is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.access_keys.with_raw_response.delete(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = await response.parse()
        assert access_key is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.access_keys.with_streaming_response.delete(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = await response.parse()
            assert access_key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.access_keys.with_raw_response.delete(
                access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_key_id` but received ''"):
            await async_client.projects.access_keys.with_raw_response.delete(
                access_key_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_project_id(self, async_client: AsyncCodex) -> None:
        access_key = await async_client.projects.access_keys.retrieve_project_id()
        assert_matches_type(AccessKeyRetrieveProjectIDResponse, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_project_id(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.access_keys.with_raw_response.retrieve_project_id()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = await response.parse()
        assert_matches_type(AccessKeyRetrieveProjectIDResponse, access_key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_project_id(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.access_keys.with_streaming_response.retrieve_project_id() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = await response.parse()
            assert_matches_type(AccessKeyRetrieveProjectIDResponse, access_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_revoke(self, async_client: AsyncCodex) -> None:
        access_key = await async_client.projects.access_keys.revoke(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert access_key is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncCodex) -> None:
        response = await async_client.projects.access_keys.with_raw_response.revoke(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_key = await response.parse()
        assert access_key is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncCodex) -> None:
        async with async_client.projects.access_keys.with_streaming_response.revoke(
            access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_key = await response.parse()
            assert access_key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.access_keys.with_raw_response.revoke(
                access_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_key_id` but received ''"):
            await async_client.projects.access_keys.with_raw_response.revoke(
                access_key_id="",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
