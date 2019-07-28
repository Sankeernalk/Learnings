class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Node1(Node):
    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next


class Node2(Node1):
    def remove_duplicates(self):
        els = []
        node = self
        previous = None
        while node != None:
            if node.val in els:
                previous.next = node.next
            else:
                els.append(node.val)
            previous = node
            node = node.next


if __name__ == "__main__":
    node1 = Node2(1)
    node2 = Node2(2)
    node3 = Node2(3)
    node4 = Node2(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node1.remove_duplicates()
    node1.traverse()


A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print(A0)
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
print(A2)
A6 = [[i,i*i] for i in A1]
print(A6)