from collections.abc import MutableMapping
from contextlib import AbstractContextManager
import time
from itertools import chain
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from storage import Storage


class StorageTransaction(MutableMapping, AbstractContextManager):
    # noinspection PyProtectedMember
    def __init__(self, storage: "Storage"):
        self._storage = storage
        self._changed: dict[Any, Any] = {}
        self._deleted: set[Any] = set()
        self._orig_dict = storage._dict[0]
        self._cancel = False
        self._transaction_start = -1
        self._orig_keys: set[Any] = set()

    # noinspection PyProtectedMember
    def _check_modification_time(self, key):
        modification_time = self._storage._dict[1].get(key, 0)
        if modification_time > self._transaction_start:
            raise RuntimeError(f'value of key {repr(key)} externally modified during transaction')

    def __getitem__(self, __key) -> Any:
        if __key in self._deleted or __key in self._changed:
            return self._changed[__key]
        item = self._orig_dict[__key]
        self._check_modification_time(__key)
        return item

    def __setitem__(self, __key, __value):
        if self._transaction_start < 0:
            raise RuntimeError('transaction invalid')
        self._deleted.discard(__key)
        self._changed[__key] = __value

    def __delitem__(self, __key):
        if self._transaction_start < 0:
            raise RuntimeError('transaction invalid')
        if __key in self._deleted or __key in self._changed or __key not in self._orig_keys:
            del self._changed[__key]
        self._deleted.add(__key)

    def __len__(self):
        return len(self._orig_keys | self._changed.keys() - self._deleted)

    def __iter__(self):
        return iter(self._orig_keys | self._changed.keys() - self._deleted)

    # noinspection PyProtectedMember
    def __enter__(self):
        self._transaction_start = time.time_ns()
        self._orig_keys = set(self._storage._dict[0].keys())
        return self

    # noinspection PyProtectedMember
    @staticmethod
    def _update_storage(st: "Storage", transaction_start_time: int, changes: dict[Any, Any], deleted: set[Any]):
        with st._update_lock:
            for k in chain(changes.keys(), deleted):
                if st._dict[1].get(k, 0) > transaction_start_time:
                    raise RuntimeError(f'value of key {repr(k)} externally modified during transaction')
            ns = time.time_ns()
            old = st._dict
            new_dict = (old[0].copy(), old[1].copy())
            for k, v in changes.items():
                new_dict[0][k] = v
                new_dict[1][k] = ns
            for k in deleted:
                new_dict[0].pop(k, None)
                new_dict[1][k] = ns
            st._dict = new_dict

    def __exit__(self, __exc_type, __exc_value, __traceback):
        transaction_start = self._transaction_start
        self._transaction_start = -2
        if not self._cancel and __exc_type is None:
            self._update_storage(self._storage, transaction_start, self._changed, self._deleted)
        self._changed = {}
        self._deleted = set()
        self.orig_keys = set()

    def cancel(self):
        self._cancel = True
