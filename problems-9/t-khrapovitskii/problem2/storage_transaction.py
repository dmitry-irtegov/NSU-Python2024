from collections.abc import MutableMapping
from contextlib import AbstractContextManager
import time
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from storage import Storage


class StorageTransaction(MutableMapping, AbstractContextManager):
    # noinspection PyProtectedMember
    def __init__(self, storage: "Storage"):
        self._storage = storage
        self._changed: dict[Any, Any] = {}
        self._deleted: set[Any] = set()
        self._orig_dict = storage._dict
        self._cancel = False
        self._transaction_start = -1
        self._orig_keys: set[Any] = set()

    def _check_modification_time(self, key):
        modification_time = self._storage.get_key_modification_time(key)
        if modification_time and modification_time > self._transaction_start:
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

    def __enter__(self):
        self._transaction_start = time.time_ns()
        # noinspection PyProtectedMember
        self._orig_keys = set(self._storage._dict.keys())
        return self

    def __exit__(self, __exc_type, __exc_value, __traceback):
        transaction_start = self._transaction_start
        self._transaction_start = -2
        if not self._cancel and __exc_type is None:
            self._storage.update(transaction_start, self._changed, self._deleted)
        self._changed = {}
        self._deleted = set()
        self.orig_keys = set()

    def cancel(self):
        self._cancel = True
