from collections.abc import Mapping
from threading import Lock
from typing import Any, Generic, ItemsView, Iterator, KeysView, TypeVar, ValuesView, overload

KT = TypeVar("KT")
VT = TypeVar("VT")
T = TypeVar("T")


class Transaction(Generic[KT, VT]):
    __slots__ = ("_merge")

    def __init__(self) -> None:
        self._merge: dict[KT, VT] = {}

    def __setitem__(self, __key: KT, __value: VT) -> None:
        self._merge[__key] = __value


class TransactionProxy(Generic[KT, VT]):
    __slots__ = ("_storage", "_transaction")

    def __init__(self, /, __storage: "Storage[KT, VT]") -> None:
        self._storage = __storage

    def __enter__(self) -> Transaction[KT, VT]:
        self._transaction = Transaction[KT, VT]()
        return self._transaction

    def __exit__(self, *exc: Any) -> None:
        if exc[0] is None:
            with self._storage._lock:
                self._storage._store.update(self._transaction._merge)


class Storage(Mapping[KT, VT]):
    __slots__ = ("_store", "_lock", "_transaction")

    def __init__(self) -> None:
        self._store = dict[KT, VT]()
        self._lock = Lock()

    def __getitem__(self, __key: KT) -> VT:
        return self._store[__key]

    def __iter__(self) -> Iterator[KT]:
        return iter(self._store)

    def __len__(self) -> int:
        return len(self._store)

    def __contains__(self, __key: object) -> bool:
        return __key in self._store

    def __eq__(self, __other: object) -> bool:
        if self is __other:
            return True

        if isinstance(__other, type(self)):
            return self._store == __other._store

        return False

    def __ne__(self, __value: object) -> bool:
        if self is __value:
            return False

        if isinstance(__value, type(self)):
            return self._store != __value._store

        return True

    def keys(self) -> KeysView[KT]:
        return self._store.keys()

    def items(self) -> ItemsView[KT, VT]:
        return self._store.items()

    def values(self) -> ValuesView[VT]:
        return self._store.values()

    @overload
    def get(self, __key: KT) -> VT | None: ...
    @overload
    def get(self, __key: KT, default: VT | T) -> VT | T: ...
    def get(self, __key, /, __default=None):
        return self._store.get(__key, __default)

    def edit(self) -> TransactionProxy[KT, VT]:
        return TransactionProxy(self)
