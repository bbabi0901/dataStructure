class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.node_count = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def reverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result

    def get_at(self, pos):
        if pos < 0 or pos > self.node_count:
            return None

        if pos > self.node_count // 2:
            i = 0
            curr = self.tail
            while i < self.node_count - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1
        return curr

    def insert_after(self, prev, new_node):
        next = prev.next
        new_node.next = next
        new_node.prev = prev
        prev.next = new_node
        next.prev = new_node
        self.node_count += 1
        return True

    def insert_before(self, next, new_node):
        prev = next.prev
        new_node.prev = prev
        new_node.next = next
        prev.next = new_node
        next.prev = new_node
        self.node_count += 1
        return True

    def insert_at(self, pos, new_node):
        if pos < 1 or pos > self.node_count + 1:
            return False
        prev = self.get_at(pos - 1)
        return self.insert_after(prev, new_node)

    def pop_after(self, prev):
        if prev is self.tail:
            raise IndexError
        target = prev.next
        next = target.next
        prev.next = next
        next.prev = prev
        self.node_count -= 1
        return target

    def pop_before(self, next):
        if next is self.head:
            raise IndexError
        target = next.prev
        prev = target.prev
        next.prev = prev
        prev.next = next
        self.node_count -= 1
        return target

    def pop_at(self, pos):
        if pos < 1 or pos > self.node_count + 1:
            raise IndexError
        prev = self.get_at(pos - 1)
        return self.pop_after(prev)

    def concat(self, dll):
        self.tail.prev.next = dll.head.next
        dll.head.next.prev = self.tail.prev
        self.tail = dll.tail
        self.node_count += dll.node_count