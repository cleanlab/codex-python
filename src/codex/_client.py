# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import tlm, health
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.users import users
from .resources.projects import projects
from .resources.organizations import organizations

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Codex",
    "AsyncCodex",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api-codex.cleanlab.ai",
    "staging": "https://api-codex-staging-o3gxj3oajfu.cleanlab.ai",
    "local": "http://localhost:8080",
}


class Codex(SyncAPIClient):
    health: health.HealthResource
    organizations: organizations.OrganizationsResource
    users: users.UsersResource
    projects: projects.ProjectsResource
    tlm: tlm.TlmResource
    with_raw_response: CodexWithRawResponse
    with_streaming_response: CodexWithStreamedResponse

    # client options
    auth_token: str | None
    api_key: str | None
    access_key: str | None

    _environment: Literal["production", "staging", "local"] | NotGiven

    def __init__(
        self,
        *,
        auth_token: str | None = None,
        api_key: str | None = None,
        access_key: str | None = None,
        environment: Literal["production", "staging", "local"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Codex client instance."""
        self.auth_token = auth_token

        self.api_key = api_key

        self.access_key = access_key

        self._environment = environment

        base_url_env = os.environ.get("CODEX_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `CODEX_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.health = health.HealthResource(self)
        self.organizations = organizations.OrganizationsResource(self)
        self.users = users.UsersResource(self)
        self.projects = projects.ProjectsResource(self)
        self.tlm = tlm.TlmResource(self)
        self.with_raw_response = CodexWithRawResponse(self)
        self.with_streaming_response = CodexWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._http_bearer, **self._authenticated_api_key, **self._public_access_key}

    @property
    def _http_bearer(self) -> dict[str, str]:
        auth_token = self.auth_token
        if auth_token is None:
            return {}
        return {"Authorization": f"Bearer {auth_token}"}

    @property
    def _authenticated_api_key(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-API-Key": api_key}

    @property
    def _public_access_key(self) -> dict[str, str]:
        access_key = self.access_key
        if access_key is None:
            return {}
        return {"X-Access-Key": access_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.auth_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        if self.api_key and headers.get("X-API-Key"):
            return
        if isinstance(custom_headers.get("X-API-Key"), Omit):
            return

        if self.access_key and headers.get("X-Access-Key"):
            return
        if isinstance(custom_headers.get("X-Access-Key"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected one of auth_token, api_key or access_key to be set. Or for one of the `Authorization`, `X-API-Key` or `X-Access-Key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        auth_token: str | None = None,
        api_key: str | None = None,
        access_key: str | None = None,
        environment: Literal["production", "staging", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            auth_token=auth_token or self.auth_token,
            api_key=api_key or self.api_key,
            access_key=access_key or self.access_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncCodex(AsyncAPIClient):
    health: health.AsyncHealthResource
    organizations: organizations.AsyncOrganizationsResource
    users: users.AsyncUsersResource
    projects: projects.AsyncProjectsResource
    tlm: tlm.AsyncTlmResource
    with_raw_response: AsyncCodexWithRawResponse
    with_streaming_response: AsyncCodexWithStreamedResponse

    # client options
    auth_token: str | None
    api_key: str | None
    access_key: str | None

    _environment: Literal["production", "staging", "local"] | NotGiven

    def __init__(
        self,
        *,
        auth_token: str | None = None,
        api_key: str | None = None,
        access_key: str | None = None,
        environment: Literal["production", "staging", "local"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncCodex client instance."""
        self.auth_token = auth_token

        self.api_key = api_key

        self.access_key = access_key

        self._environment = environment

        base_url_env = os.environ.get("CODEX_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `CODEX_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.health = health.AsyncHealthResource(self)
        self.organizations = organizations.AsyncOrganizationsResource(self)
        self.users = users.AsyncUsersResource(self)
        self.projects = projects.AsyncProjectsResource(self)
        self.tlm = tlm.AsyncTlmResource(self)
        self.with_raw_response = AsyncCodexWithRawResponse(self)
        self.with_streaming_response = AsyncCodexWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._http_bearer, **self._authenticated_api_key, **self._public_access_key}

    @property
    def _http_bearer(self) -> dict[str, str]:
        auth_token = self.auth_token
        if auth_token is None:
            return {}
        return {"Authorization": f"Bearer {auth_token}"}

    @property
    def _authenticated_api_key(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-API-Key": api_key}

    @property
    def _public_access_key(self) -> dict[str, str]:
        access_key = self.access_key
        if access_key is None:
            return {}
        return {"X-Access-Key": access_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.auth_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        if self.api_key and headers.get("X-API-Key"):
            return
        if isinstance(custom_headers.get("X-API-Key"), Omit):
            return

        if self.access_key and headers.get("X-Access-Key"):
            return
        if isinstance(custom_headers.get("X-Access-Key"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected one of auth_token, api_key or access_key to be set. Or for one of the `Authorization`, `X-API-Key` or `X-Access-Key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        auth_token: str | None = None,
        api_key: str | None = None,
        access_key: str | None = None,
        environment: Literal["production", "staging", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            auth_token=auth_token or self.auth_token,
            api_key=api_key or self.api_key,
            access_key=access_key or self.access_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class CodexWithRawResponse:
    def __init__(self, client: Codex) -> None:
        self.health = health.HealthResourceWithRawResponse(client.health)
        self.organizations = organizations.OrganizationsResourceWithRawResponse(client.organizations)
        self.users = users.UsersResourceWithRawResponse(client.users)
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)
        self.tlm = tlm.TlmResourceWithRawResponse(client.tlm)


class AsyncCodexWithRawResponse:
    def __init__(self, client: AsyncCodex) -> None:
        self.health = health.AsyncHealthResourceWithRawResponse(client.health)
        self.organizations = organizations.AsyncOrganizationsResourceWithRawResponse(client.organizations)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)
        self.tlm = tlm.AsyncTlmResourceWithRawResponse(client.tlm)


class CodexWithStreamedResponse:
    def __init__(self, client: Codex) -> None:
        self.health = health.HealthResourceWithStreamingResponse(client.health)
        self.organizations = organizations.OrganizationsResourceWithStreamingResponse(client.organizations)
        self.users = users.UsersResourceWithStreamingResponse(client.users)
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)
        self.tlm = tlm.TlmResourceWithStreamingResponse(client.tlm)


class AsyncCodexWithStreamedResponse:
    def __init__(self, client: AsyncCodex) -> None:
        self.health = health.AsyncHealthResourceWithStreamingResponse(client.health)
        self.organizations = organizations.AsyncOrganizationsResourceWithStreamingResponse(client.organizations)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.tlm = tlm.AsyncTlmResourceWithStreamingResponse(client.tlm)


Client = Codex

AsyncClient = AsyncCodex
