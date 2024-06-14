from collections.abc import Mapping, Hashable
from threading import Lock
from typing import Any

from storage_transaction import StorageTransaction


class Storage(Mapping):
    def __init__(self, initial: dict[Hashable, Any] | None = None):
        if initial is None:
            self._dict: dict[Hashable, Any]
        else:
            self._dict = initial.copy()
        self._transaction: StorageTransaction | None = None
        self._transaction_lock = Lock()

    def __getitem__(self, __key):
        return self._dict[__key]

    def __len__(self):
        return len(self._dict)

    def __iter__(self):
        return iter(self._dict)

    def edit(self) -> StorageTransaction:
        with self._transaction_lock:
            if self._transaction:
                raise RuntimeError('transaction already exist')
            self._transaction = StorageTransaction(self)
        return self._transaction

    def __repr__(self):
        return repr(self._dict)

    def __str__(self):
        return str(self._dict)
