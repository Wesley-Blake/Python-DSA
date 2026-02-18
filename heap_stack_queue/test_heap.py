import pytest
from heap import Heap, heap_error

def test_heap_heapify():
    heap_heapify = Heap()
    heap_heapify.heapify([1,2,3])
    assert len(heap_heapify._heap) == 3
def test_fail_heap_heapify():
    failed_heap = Heap()
    with pytest.raises(heap_error):
        failed_heap.heapify(1)
