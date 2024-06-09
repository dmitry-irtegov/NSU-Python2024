import time
from collections.abc import Mapping
from itertools import chain
from threading import Lock
# from multiprocessing import Lock ?
from typing import Any

from storage_transaction import StorageTransaction


class Storage(Mapping):
    def __init__(self, initial: dict[Any, Any] | None = None):
        if initial is None:
            self._dict = {}
        else:
            self._dict = initial.copy()
        self._key_modifications: dict[Any, int] = {i: 0 for i in self._dict}
        self._last_modification: int = 0
        self._update_lock = Lock()

    def __getitem__(self, __key):
        return self._dict[__key]

    def __len__(self):
        return len(self._dict)

    def __iter__(self):
        return iter(self._dict)

    def edit(self) -> StorageTransaction:
        return StorageTransaction(self)

    def get_key_modification_time(self, key: Any) -> int | None:
        return self._key_modifications.get(key, None)

    def update(self, transaction_start_time: int, changes: dict[Any, Any], deleted: set[Any]) -> None:
        with self._update_lock:
            for k in chain(changes.keys(), deleted):
                if self._key_modifications.get(k, 0) > transaction_start_time:
                    raise RuntimeError(f'value of key {repr(k)} externally modified during transaction')
            ns = time.time_ns()
            for k, v in changes.items():
                self._dict[k] = v
                self._key_modifications[k] = ns
            for k in deleted:
                self._dict.pop(k, None)
                self._key_modifications[k] = ns

    def __repr__(self):
        return repr(self._dict)

    def __str__(self):
        return str(self._dict)
