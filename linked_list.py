from __future__ import annotations
from typing import Any

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, node: Any = None):
        self.head = Node(node)
        self.tail = self.head
    def __repr__(self):
        node = self.head
        result = ""
        while node != None:
            result += str(node.data) + " -> "
            node = node.next
        result += "None"
        return result
    def add(self, node):
        self.tail.next == Node(node)


if __name__ == "__main__":
    llist = LinkedList([1,2,3])
    llist.add(24)
    llist.add("this")
    llist.add([])
    llist.add([{"test": 1, "test": 2}])
    print(llist)
