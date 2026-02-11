class heap_error(Exception):
    pass

class Heap:
    def __init__(self):
        self._heap = []
    def heapify(self, args_list):
        if len(self._heap) == 0 and isinstance(args_list, list):
            self._heap = args_list
        else:
            raise heap_error
