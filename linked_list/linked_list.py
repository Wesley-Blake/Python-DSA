from __future__ import annotations
from typing import Any

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, data: Any = None):
        self.head = Node(data)
    def __repr__(self):
        node = self.head
        result = []
        while node != None:
            result.append(str(node.data))
            node = node.next
        return ' -> '.join(result)
    def __iter__(self):
        node = self.head
        while node != None:
            yield node
            node = node.next
    def add_first(self, data):
        if self.head.data == None:
            first = Node(data)
            first.next = self.head
            self.head = first
        else:
            first = Node(data)
            first.next = self.head
            self.head = first
    def pop(self):
        if self.head.data != None and self.head.next != None:
            result = self.head.data
            self.head = self.head.next
            return result
    def append(self, data):
        node = self.head
        if node.data == None and node.next == None:
            self.add_first(data)
            return 0
        for i in self.__iter__():
            if i.next.data == None:
                i.next = Node(data)
                i.next.next = Node()
                break
