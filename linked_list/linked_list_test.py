import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.llist = LinkedList()
    def tearDown(self):
        del self.llist
    def test_add_first(self):
        self.assertEqual(self.llist.__repr__(), 'None')
        self.llist.add_first(4)
        self.llist.add_first(3)
        self.llist.add_first(2)
        self.llist.add_first(1)
        self.assertEqual(self.llist.__repr__(), '1 -> 2 -> 3 -> 4 -> None')
    def test_pop(self):
        self.assertEqual(self.llist.pop(), None)
        self.llist.add_first(2)
        self.llist.add_first(1)
        self.llist.pop()
        self.assertEqual(self.llist.__repr__(), '2 -> None')
    def test_append(self):
        self.assertEqual(self.llist.__repr__(), 'None')
        self.llist.append(1)
        self.llist.append(2)
        self.assertEqual(self.llist.__repr__(),'1 -> 2 -> None')
