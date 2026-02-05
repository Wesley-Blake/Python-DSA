from hash_table import HashTable

def test_should_create_hasttable():
    assert HashTable(size=100) is not None
def test_size():
    assert len(HashTable(size=100)) == 100
