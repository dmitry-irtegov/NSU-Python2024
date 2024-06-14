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

    def test_two_transactions(self):
        storage = Storage({1: 2, (3,): 4, None: "6", "7": self})
        with storage.edit() as _:
            with pytest.raises(RuntimeError):
                with storage.edit() as _:
                    pass

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

    def test_transaction_cancel(self):
        storage = Storage({})
        with storage.edit() as se:
            se[1] = 20
            se[-1] = -20
            if se[-1] < 0:
                se.cancel()
            se[-1] = 100
        assert 1 not in storage
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

    def test_consecutive_transactions_one_fail(self):
        original = {1: 2}
        storage = Storage(original)
        with pytest.raises(Exception):
            with storage.edit() as se:
                se[1] = 20
                se[2] = 30
                assert storage[1] == 2
                assert 2 not in storage
                raise Exception()
        assert storage[1] == 2
        assert 2 not in storage
        with storage.edit() as se:
            del se[1]
            se[2] = 25
            assert storage[1] == 2
            assert 2 not in storage
        assert 1 not in storage
        assert storage[2] == 25

    def test_two_nested_transactions(self):
        storage = Storage({1: 2, (3,): 4, None: "6", "7": self})
        with storage.edit() as se:
            with se.nested() as _:
                with pytest.raises(RuntimeError):
                    with se.nested() as _:
                        pass

    def test_nested_transaction_cant_edit(self):
        storage = Storage({1: 2})
        with pytest.raises(RuntimeError):
            with storage.edit() as se1:
                with se1.nested() as _:
                    se1[3] = 4
        with pytest.raises(RuntimeError):
            with storage.edit() as se1:
                with se1.nested() as _:
                    del se1[1]

    def test_nested_transactions_good(self):
        original = {1: 2, 2: 3, "s": set()}
        storage = Storage(original)
        with storage.edit() as se1:
            se1[1] = 20
            se1["s"].add(se1[2])
            with se1.nested() as se2:
                se2[2] = 25
                se2["s"].add(se2[2])
        assert storage[1] == 20
        assert storage[2] == 25
        assert storage["s"] == {original[2], storage[2]}

    def test_nested_transaction_fail_get_caught(self):
        original = {1: 1, 2: 2, "s": set()}
        storage = Storage(original)
        with storage.edit() as se1:
            se1[1] = 20
            with pytest.raises(Exception):
                with se1.nested() as se2:
                    se2[6] = 6
                    raise Exception()
            se1[2] = 25
        assert storage[1] == 20
        assert storage[2] == 25
        assert 6 not in storage

    def test_nested_transaction_fail_get_uncaught(self):
        original = {1: 1, 2: 2, "s": set()}
        storage = Storage(original)
        with pytest.raises(Exception):
            with storage.edit() as se1:
                se1[1] = 20
                with se1.nested() as se2:
                    se2[6] = 6
                    raise Exception()
                se1[2] = 25
        assert storage[1] == 1
        assert storage[2] == 2
        assert 6 not in storage

    def test_nested_transaction_good_outer_fail(self):
        original = {1: 1, 2: 2, "s": set()}
        storage = Storage(original)
        with pytest.raises(Exception):
            with storage.edit() as se1:
                se1[1] = 20
                with se1.nested() as se2:
                    se2[6] = 6
                se1[2] = 25
                raise Exception()
        assert storage[1] == 1
        assert storage[2] == 2
        assert 6 not in storage

    def test_nested_transaction_consecutive(self):
        original = {1: 1, 2: 2, "s": set()}
        storage = Storage(original)
        with storage.edit() as se:
            se[1] = 20
            with se.nested() as sn1:
                sn1[2] = 30
            with se.nested() as sn2:
                sn2[3] = 40
        assert storage[1] == 20
        assert storage[2] == 30
        assert storage[3] == 40

    def test_nested_transaction_consecutive_fail(self):
        original = {1: 1, 2: 2, "s": set()}
        storage = Storage(original)
        with storage.edit() as se:
            se[1] = 20
            with pytest.raises(Exception):
                with se.nested() as sn1:
                    sn1[2] = 30
                    raise Exception()
            with se.nested() as sn2:
                sn2[3] = 40
        assert storage[1] == 20
        assert storage[2] == 2
        assert storage[3] == 40
