import pytest
from heap import Heap, heap_error

class TestHeap:
    """Test cases for Heap class"""

    def test_heap_initialization(self):
        """Test that Heap initializes with empty list"""
        heap = Heap()
        assert heap._heap == []

    def test_heap_heapify_with_valid_list(self):
        """Test heapify with valid list input"""
        heap = Heap()
        heap.heapify([1, 2, 3])
        assert len(heap._heap) == 3
        assert heap._heap == [1, 2, 3]

    def test_heap_heapify_with_single_element(self):
        """Test heapify with single element list"""
        heap = Heap()
        heap.heapify([42])
        assert len(heap._heap) == 1
        assert heap._heap == [42]

    def test_heap_heapify_with_empty_list(self):
        """Test heapify with empty list"""
        heap = Heap()
        heap.heapify([])
        assert len(heap._heap) == 0
        assert heap._heap == []

    def test_heap_heapify_with_non_list_input(self):
        """Test heapify raises error with non-list input"""
        heap = Heap()
        with pytest.raises(heap_error):
            heap.heapify(1)

    def test_heap_heapify_with_string_input(self):
        """Test heapify raises error with string input"""
        heap = Heap()
        with pytest.raises(heap_error):
            heap.heapify("not_a_list")

    def test_heap_heapify_called_twice_raises_error(self):
        """Test that calling heapify twice raises error"""
        heap = Heap()
        heap.heapify([1, 2, 3])
        with pytest.raises(heap_error):
            heap.heapify([4, 5, 6])
