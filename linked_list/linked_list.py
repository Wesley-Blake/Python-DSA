from __future__ import annotations
from typing import Any

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, data: Any = None):
        self.head = Node(data)
        self.tail = self.head
    def __repr__(self):
        node = self.head
        result = []
        while node != None:
            result.append(str(node.data))
            node = node.next
        return ' -> '.join(result)
    def add_first(self, data):
        first = Node(data)
        first.next = self.head
        self.head = first
    def pop(self):
        if self.head.data != None and self.head.next != None:
            result = self.head.data
            self.head = self.head.next
            return result
    def append(self, data):
        if self.tail.data == None:
            self.head = Node(data)
            self.tail = head
        else:
            last = self.tail
            last.next = Node(data)
            self.tail = last.next
