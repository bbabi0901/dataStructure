class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    # n번째 Node를 구하는 함수
    def get_at(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    # Linked list를 끝까지 순회하는 함수
    def traverse(self):
        result = []
        curr = self.head
        while curr.next :
            result.append(curr.data)
            curr = curr.next
        return result

    def insert_at(self, pos, new_node):
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, new_node)

    def insert_after(self, prev, new_node):
        new_node.next = prev.next
        if prev.next is None:
            self.tail = new_node
        prev.next = new_node
        self.nodeCount += 1
        return True

    # n번째의 Node를 pop하고 node의 data를 반환하는 함수
    def pop_after(self, prev):
        target = prev.next
        if prev is self.tail:
            raise IndexError
        if target is self.tail:
            self.tail = prev
        prev.next = target.next
        self.nodeCount -= 1
        return target.data

    def pop_at(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos - 1)
        return self.popAfter(prev)