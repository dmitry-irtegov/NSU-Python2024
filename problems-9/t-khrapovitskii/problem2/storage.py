from collections.abc import Mapping
from threading import Lock
# from multiprocessing import Lock ?
from typing import Any

from storage_transaction import StorageTransaction


class Storage(Mapping):
    def __init__(self, initial: dict[Any, Any] | None = None):
        if initial is None:
            self._dict: tuple[dict[Any, Any], dict[Any, int]] = ({}, {})
        else:
            self._dict = (initial.copy(), {i: 0 for i in initial})
        self._last_modification: int = 0
        self._update_lock = Lock()

    def __getitem__(self, __key):
        return self._dict[0][__key]

    def __len__(self):
        return len(self._dict[0])

    def __iter__(self):
        return iter(self._dict[0])

    def edit(self) -> StorageTransaction:
        return StorageTransaction(self)

    def __repr__(self):
        return repr(self._dict)

    def __str__(self):
        return str(self._dict)
