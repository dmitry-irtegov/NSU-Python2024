import time
from threading import Thread

import pytest

from storage import Storage


# noinspection DuplicatedCode
class TestStorage:
    def test_storage_get(self):
        storage = Storage({1: 2, (3,): 4, None: "6", "7": self})
        assert storage.get(1) == 2
        assert storage.get((3,)) == 4
        assert storage.get(None) == "6"
        assert storage.get("7") is self

    def test_storage_len(self):
        storage = Storage({1: 2, (3,): 4, None: "6", "7": self})
        assert len(storage) == 4

    def test_storage_iter(self):
        storage = Storage({1: 2, (3,): 4, None: "6", "7": self})
        assert set(storage) == {1, (3,), None, "7"}

    def test_storage_mutate(self):
        storage = Storage({1: [1, 2, 3], 2: 0})
        storage[1].append(4)
        assert storage.get(1) == [1, 2, 3, 4]
        with pytest.raises(TypeError):
            storage[1] += [5]
        assert storage[1] == [1, 2, 3, 4, 5]  # This is cringe but logical
        with pytest.raises(TypeError):
            storage[2] += 5

    def test_transaction_get(self):
        original = {1: 2, (3,): 4, None: "6", "7": [1, 2, 3]}
        storage = Storage(original)
        with storage.edit() as se:
            assert se.get(1) == 2
            assert se[(3,)] == 4
            assert se[None] == "6"
            assert se.get("7") == [1, 2, 3]
            assert se.get(8, None) is None
        assert dict(storage) == original

    def test_transaction_set(self):
        original = {1: 2, (3,): 4, None: "6", "7": [1, 2, 3], "72": [1, 2, 3]}
        storage = Storage(original)
        with storage.edit() as se:
            se[1] = 20
            assert se[1] == 20
            assert storage[1] == original[1]
            se[(3,)] += 1
            se["7"].append(7)
            assert se["7"] == [1, 2, 3, 7]
            assert storage["7"] == [1, 2, 3, 7]
            se["72"] = se["72"] + [7]
            assert se.get("72") == [1, 2, 3, 7]
            assert storage.get("72") == [1, 2, 3]
            se["new"] = "N"
            assert se["new"] == "N"
            with pytest.raises(KeyError):
                assert storage["new"] == "N"
        assert storage[1] == 20
        assert storage["7"] == [1, 2, 3, 7]
        assert storage["7"] is original["7"]
        assert storage["72"] == [1, 2, 3, 7]
        assert storage["72"] is not original["7"]
        assert storage

    def test_transaction_del(self):
        original = {1: 2, (3,): 4, None: "6", "7": [1, 2, 3]}
        storage = Storage(original)
        with storage.edit() as se:
            del se[1]
            with pytest.raises(KeyError):
                assert se[1] == 2
                del se[0]
            assert storage[1] == 2
        assert 1 not in storage

    def test_transaction_change_delete(self):
        original = {1: 2, (3,): 4, None: "6", "7": [1, 2, 3]}
        storage = Storage(original)
        with storage.edit() as se:
            assert se._changed == {}
            assert se._deleted == set()
            se[1] = 20
            assert se._changed == {1: 20}
            assert se._deleted == set()
            del se[1]
            assert se._changed == {}
            assert se._deleted == {1}
            se[1] = 20
            assert se._changed == {1: 20}
            assert se._deleted == set()

    def test_transaction_cancel(self):
        original = {1: 2}
        storage = Storage(original)
        with storage.edit() as se:
            se[1] = 20
            se[-1] = -20
            if se[-1] < 0:
                se.cancel()
            se[-1] = 100
        assert storage[1] == 2
        assert -1 not in storage

    def test_transaction_exception(self):
        original = {"idx": 99999}
        storage = Storage(original)
        with pytest.raises(Exception):
            with storage.edit() as se:
                se["list"] = [1, 2, 3]
                se["list"][se["idx"]] = 0
                se[3] = 100
        assert storage["idx"] == original["idx"]
        assert -1 not in storage
        assert "list" not in storage

    def test_consecutive_transactions(self):
        original = {1: 2}
        storage = Storage(original)
        with storage.edit() as se:
            se[1] = 20
            se[2] = 30
            assert storage[1] == 2
            assert 2 not in storage
        assert storage[1] == 20
        assert storage[2] == 30
        with storage.edit() as se:
            del se[1]
            se[2] = 25
            assert storage[1] == 20
            assert storage[2] == 30
        assert 1 not in storage
        assert storage[2] == 25

    def test_inner_transactions_good(self):
        original = {1: 2, 2: 3, "s": set()}
        storage = Storage(original)
        with storage.edit() as se1:
            with storage.edit() as se2:
                se1[1] = 20
                se1["s"].add(se1[2])
                se2[2] = 25
                se2["s"].add(se2[2])
        assert storage[1] == 20
        assert storage[2] == 25
        assert storage["s"] == {original[2], storage[2]}

    def test_inner_transactions_fail_one_get_caught(self):
        original = {1: 1, 2: 2, "s": set()}
        storage = Storage(original)
        with storage.edit() as se1:
            with storage.edit() as se2:
                se2[2] = 25
                se2["s"].add(se2[1])
            se1[1] = 20  # this merged
            with pytest.raises(RuntimeError):
                se1["s"].add(se1[2])  # this raised and not merged
        assert storage[1] == 20
        assert storage[2] == 25
        assert storage["s"] == {1}

    def test_inner_transactions_fail_one_get_uncaught(self):
        original = {1: 1, 2: 2, "s": set()}
        storage = Storage(original)
        with pytest.raises(RuntimeError):
            with storage.edit() as se1:
                with storage.edit() as se2:
                    se2["s"].add(se2[1])
                    se2[2] = 25
                se1[1] = 20  # canceled on __exit__
                se1["s"].add(se1[2])  # canceled on __exit__
        assert storage[1] == 1
        assert storage[2] == 25
        assert storage["s"] == {1}

    def test_inner_transactions_fail_one_exit(self):
        original = {1: 1, 2: 2}
        storage = Storage(original)
        se1 = storage.edit()
        se1.__enter__()
        with storage.edit() as se2:
            se1[1] = 21
            se1[3] = 31
            se2[2] = 22
            se2[3] = 33
        with pytest.raises(RuntimeError):
            se1.__exit__(None, None, None)
        assert storage[1] == 1
        assert storage[2] == 22
        assert storage[3] == 33

    def test_thread_transactions_good(self):
        def do_transaction(storage: Storage, odd: int):
            with storage.edit() as se:
                for i in range(10000):
                    se[i * 2 + odd] = i
                    time.sleep(0.00001)

        st = Storage({})
        t1 = Thread(target=do_transaction, args=(st, 0))
        t2 = Thread(target=do_transaction, args=(st, 1))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        assert len(st) == 20000
        assert st[0] == 0
        assert st[1] == 0
        assert st[2] == 1
        assert st[3] == 1
        assert st[19998] == 9999
        assert st[19999] == 9999

    def test_thread_transactions_bad_exit(self):
        def do_transaction(storage: Storage, odd: int):
            with storage.edit() as se:
                se[-1] = odd
                for i in range(10000):
                    se[i * 2 + odd] = i
                    time.sleep(0.00005)

        st = Storage({})
        t1 = Thread(target=do_transaction, args=(st, 0))
        t2 = Thread(target=do_transaction, args=(st, 1))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        assert len(st) == 10001
        assert 1 not in st and st[0] == 0 or 0 not in st and st[1] == 0
        assert 19998 not in st and st[19999] == 9999 or 19999 not in st and st[19998] == 9999

    def test_thread_transactions_bad_set(self):
        def do_transaction(storage: Storage, odd: int):
            with storage.edit() as se:
                for i in range(10000):
                    se[i * 3] = i
                    se[i * 3 + odd] = i
                    time.sleep(0.00005)

        st = Storage({})
        t1 = Thread(target=do_transaction, args=(st, 0))
        t2 = Thread(target=do_transaction, args=(st, 1))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        assert len(st) == 20000
        assert st[0] == 0
        assert st[3] == 1
        assert st[29997] == 9999
        assert 1 not in st and st[2] == 0 or 2 not in st and st[1] == 0
        assert 29998 not in st and st[29999] == 9999 or 29999 not in st and st[29998] == 9999
