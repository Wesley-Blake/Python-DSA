from heap import Heap

def test_heap_heapify():
    heap_heapify = Heap()
    heap_heapify.heapify([1,2,3])
    assert len(heap_heapify._heap) == 3
