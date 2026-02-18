import pytest
from hash_table import HashTable
from pytest_unordered import unordered

@pytest.fixture
def hash_table():
    sample_data = HashTable(capacity=100)
    sample_data["hola"] = "hello"
    sample_data[98.6] = 37
    sample_data[False] = True
    return sample_data
def test_should_create_hasttable():
    assert HashTable(capacity=100) is not None
def test_capacity():
    assert len(HashTable(capacity=100)) == 100
def test_should_create_empty_pairs():
    assert HashTable(capacity=3)._pairs == [None,None,None]
def test_should_insert_key_value_pairs():
    hash_table = HashTable(capacity=100)

    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True

    assert ("hola", "hello") in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs
def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=100).values
def test_should_insert_none_value():
    hash_table = HashTable(capacity=100)
    hash_table["key"] = None
    assert ("key", None) in hash_table.pairs
def test_should_find_value_by_key(hash_table):
    assert hash_table["hola"] == "hello"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True
def test_should_raise_error_on_missing_key():
    hash_table = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"
def test_should_find_key(hash_table):
    assert "hola" in hash_table
def test_should_not_find_key(hash_table):
    assert "missing_key" not in hash_table
def test_should_get_value(hash_table):
    assert hash_table.get("hola") == "hello"
def test_should_get_none_when_missing_key(hash_table):
    assert hash_table.get("missing_key") is None
def test_should_get_default_value_when_missing_key(hash_table):
    assert hash_table.get("missing_key", "default") == "default"
def test_should_get_value_with_default(hash_table):
    assert hash_table.get("hola", "default") == "hello"
def test_should_delete_key_value_pair(hash_table):
    assert "hola" in hash_table
    assert ("hola", "hello") in hash_table.pairs

    del hash_table["hola"]

    assert "hola" not in hash_table
    assert ("hola", "hello") not in hash_table.pairs
def test_should_raise_key_error_when_deleting(hash_table):
    with pytest.raises(KeyError) as exception_info:
        del hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"
def test_should_update_value(hash_table):
    hash_table["hola"] = "hallo"

    assert hash_table["hola"] == "hallo"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True
    assert len(hash_table) == 100
def test_should_return_copy_of_pairs(hash_table):
    assert hash_table.pairs is not hash_table.pairs
def test_should_not_include_blank_pairs(hash_table):
    assert None not in hash_table.pairs
def test_should_return_duplicate_values():
    hash_table = HashTable(capacity=100)
    hash_table["Alice"] = 24
    hash_table["Bob"] = 42
    hash_table["Joe"] = 42
    assert [24, 42, 42] == sorted(hash_table.values)
def test_should_create_empty_value_slots():
    assert HashTable(capacity=3)._pairs == [None, None, None]
def test_should_iterate_over_keys(hash_table):
    for key in hash_table.keys:
        assert key in ("hola", 98.6, False)
def test_should_iterate_over_values(hash_table):
    for value in hash_table.values:
        assert value in ("hello", 37, True)
def test_should_iterate_over_pairs(hash_table):
    for key, value in hash_table.pairs:
        assert key in hash_table.keys
        assert value in hash_table.values
def test_should_use_dict_literal_for_str(hash_table):
    assert str(hash_table) in {
        "{'hola': 'hello', 98.6: 37, False: True}",
        "{'hola': 'hello', False: True, 98.6: 37}",
        "{98.6: 37, 'hola': 'hello', False: True}",
        "{98.6: 37, False: True, 'hola': 'hello'}",
        "{False: True, 'hola': 'hello', 98.6: 37}",
        "{False: True, 98.6: 37, 'hola': 'hello'}",
    }
def test_should_create_hashtable_from_dict():
    dictionary = {"hola": "hello", 98.6: 37, False: True}

    hash_table = HashTable.from_dict(dictionary)

    assert len(hash_table) == len(dictionary) * 10
    for item in dictionary.keys():
        assert item in hash_table.keys
    for dict_key, dict_value in dictionary.items():
        assert dict_key in hash_table.keys
        assert dict_value in hash_table.values
    assert unordered(hash_table.values) == list(dictionary.values())
