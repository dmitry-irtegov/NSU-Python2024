from collections.abc import MutableMapping
from contextlib import AbstractContextManager
from threading import Lock
from typing import Any, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from storage import Storage


class StorageTransaction(MutableMapping, AbstractContextManager):
    def __init__(self, storage: Union["Storage", "StorageTransaction"]):
        self._parent = storage
        self._cancel = False
        self._transaction: StorageTransaction | None = None
        self._transaction_lock = Lock()
        self._transaction_run = False
        self._dict = {}

    def __getitem__(self, __key) -> Any:
        if self._transaction_run < 0:
            raise RuntimeError('transaction invalid')
        return self._dict[__key]

    def __setitem__(self, __key, __value):
        if not self._transaction_run:
            raise RuntimeError('transaction invalid')
        if self._transaction:
            raise RuntimeError('nested transaction exists')
        self._dict[__key] = __value

    def __delitem__(self, __key):
        if not self._transaction_run:
            raise RuntimeError('transaction invalid')
        if self._transaction:
            raise RuntimeError('nested transaction exists')
        del self._dict[__key]

    def __len__(self):
        if not self._transaction_run:
            raise RuntimeError('transaction invalid')
        return len(self._dict)

    def __iter__(self):
        if not self._transaction_run:
            raise RuntimeError('transaction invalid')
        return iter(self._dict)

    # noinspection PyProtectedMember
    def __enter__(self):
        self._transaction_run = True
        self._dict = self._parent._dict.copy()
        return self

    def __exit__(self, __exc_type, __exc_value, __traceback):
        self._transaction_run = False
        if not self._cancel and __exc_type is None:
            self._parent._dict = self._dict
        self._dict = {}
        self._parent._transaction = None

    def cancel(self):
        self._cancel = True

    def nested(self):
        with self._transaction_lock:
            if self._transaction:
                raise RuntimeError('nested transaction already exist')
            self._transaction = StorageTransaction(self)
        return self._transaction

    def __repr__(self):
        return repr(self._dict)

    def __str__(self):
        return str(self._dict)
