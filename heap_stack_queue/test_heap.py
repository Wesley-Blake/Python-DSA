from heap import Heap

def test_heap_heapify():
    heap_heapify = Heap()
    heap_heapify.heapify([1,2,3])
    assert len(heap_heapify._heap) == 3
def test_fail_heap_heapify():
    failed_heap = Heap()
    failed_heap.heapify(1)
