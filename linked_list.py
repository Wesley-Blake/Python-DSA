
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, node = None):
        self.head = Node(node)
    def __repr__(self):
        node = self.head
        result = ""
        while node != None:
            result += str(node.data) + " -> "
            node = node.next
        else:
            result += "None"
        return result
    def add(self, node):
        cnode = self.head
        while cnode != None:
            if cnode.next == None:
                cnode.next = Node(node)
                break
            else:
                cnode = cnode.next


if __name__ == "__main__":
    llist = LinkedList([1,2,3])
    llist.add(24)
    llist.add("this")
    llist.add([])
    llist.add({"test": 1, "test": 2})
    print(llist)
