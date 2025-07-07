# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Type, Generic, Mapping, TypeVar, Optional, cast
from typing_extensions import override

from httpx import Response

from ._utils import is_mapping
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncMyOffsetPageTopLevelArray",
    "AsyncMyOffsetPageTopLevelArray",
    "SyncOffsetPageClusters",
    "AsyncOffsetPageClusters",
    "SyncOffsetPageQueryLogs",
    "AsyncOffsetPageQueryLogs",
    "SyncOffsetPageRemediations",
    "AsyncOffsetPageRemediations",
    "SyncOffsetPageQueryLogGroups",
    "AsyncOffsetPageQueryLogGroups",
    "SyncOffsetPageQueryLogsByGroup",
    "AsyncOffsetPageQueryLogsByGroup",
]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)

_T = TypeVar("_T")


class SyncMyOffsetPageTopLevelArray(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        return PageInfo(params={"offset": current_count})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class AsyncMyOffsetPageTopLevelArray(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        return PageInfo(params={"offset": current_count})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class SyncOffsetPageClusters(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    clusters: List[_T]
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        clusters = self.clusters
        if not clusters:
            return []
        return clusters

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageClusters(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    clusters: List[_T]
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        clusters = self.clusters
        if not clusters:
            return []
        return clusters

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncOffsetPageQueryLogs(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    query_logs: List[_T]
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        query_logs = self.query_logs
        if not query_logs:
            return []
        return query_logs

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageQueryLogs(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    query_logs: List[_T]
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        query_logs = self.query_logs
        if not query_logs:
            return []
        return query_logs

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncOffsetPageRemediations(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    remediations: List[_T]
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        remediations = self.remediations
        if not remediations:
            return []
        return remediations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageRemediations(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    remediations: List[_T]
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        remediations = self.remediations
        if not remediations:
            return []
        return remediations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncOffsetPageQueryLogGroups(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    query_log_groups: List[_T]
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        query_log_groups = self.query_log_groups
        if not query_log_groups:
            return []
        return query_log_groups

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageQueryLogGroups(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    query_log_groups: List[_T]
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        query_log_groups = self.query_log_groups
        if not query_log_groups:
            return []
        return query_log_groups

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncOffsetPageQueryLogsByGroup(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    query_logs_by_group: List[_T]
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        query_logs_by_group = self.query_logs_by_group
        if not query_logs_by_group:
            return []
        return query_logs_by_group

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPageQueryLogsByGroup(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    query_logs_by_group: List[_T]
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        query_logs_by_group = self.query_logs_by_group
        if not query_logs_by_group:
            return []
        return query_logs_by_group

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None
