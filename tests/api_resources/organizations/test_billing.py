# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from codex import Codex, AsyncCodex
from tests.utils import assert_matches_type
from codex.types.organizations import OrganizationBillingUsageSchema, OrganizationBillingInvoicesSchema

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBilling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_invoices(self, client: Codex) -> None:
        billing = client.organizations.billing.invoices(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationBillingInvoicesSchema, billing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_invoices(self, client: Codex) -> None:
        response = client.organizations.billing.with_raw_response.invoices(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(OrganizationBillingInvoicesSchema, billing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_invoices(self, client: Codex) -> None:
        with client.organizations.billing.with_streaming_response.invoices(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(OrganizationBillingInvoicesSchema, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_invoices(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.billing.with_raw_response.invoices(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_usage(self, client: Codex) -> None:
        billing = client.organizations.billing.usage(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationBillingUsageSchema, billing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_usage(self, client: Codex) -> None:
        response = client.organizations.billing.with_raw_response.usage(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(OrganizationBillingUsageSchema, billing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_usage(self, client: Codex) -> None:
        with client.organizations.billing.with_streaming_response.usage(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(OrganizationBillingUsageSchema, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_usage(self, client: Codex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.billing.with_raw_response.usage(
                "",
            )


class TestAsyncBilling:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_invoices(self, async_client: AsyncCodex) -> None:
        billing = await async_client.organizations.billing.invoices(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationBillingInvoicesSchema, billing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_invoices(self, async_client: AsyncCodex) -> None:
        response = await async_client.organizations.billing.with_raw_response.invoices(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(OrganizationBillingInvoicesSchema, billing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_invoices(self, async_client: AsyncCodex) -> None:
        async with async_client.organizations.billing.with_streaming_response.invoices(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(OrganizationBillingInvoicesSchema, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_invoices(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.billing.with_raw_response.invoices(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_usage(self, async_client: AsyncCodex) -> None:
        billing = await async_client.organizations.billing.usage(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationBillingUsageSchema, billing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_usage(self, async_client: AsyncCodex) -> None:
        response = await async_client.organizations.billing.with_raw_response.usage(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(OrganizationBillingUsageSchema, billing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_usage(self, async_client: AsyncCodex) -> None:
        async with async_client.organizations.billing.with_streaming_response.usage(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(OrganizationBillingUsageSchema, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_usage(self, async_client: AsyncCodex) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.billing.with_raw_response.usage(
                "",
            )
