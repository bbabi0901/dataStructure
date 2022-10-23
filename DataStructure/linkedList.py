class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

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
        answer = []
        curr = self.head
        while curr != None:
            answer.append(curr.data)
            curr = curr.next
        return answer

    # n번째에 새로운 Node를 삽입하는 함수
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            # 꼬리면 newNode.next = None
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    # n번째의 Node를 pop하고 node의 data를 반환하는 함수
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        # n번째 있던 node(not data)
        n = self.getAt(pos)
        if pos == 1:
            if self.nodeCount == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        else:
            prev = self.getAt(pos - 1)
            if pos == self.nodeCount:
                self.tail = prev
                prev.next = None
            else:
                prev.next = n.next
        self.nodeCount -= 1
        return n.data

node1 = Node(1)
node2 = Node(3)
node1.next = node2

ll = LinkedList()
ll.head = node1
ll.tail = node2
ll.nodeCount = 2

print(ll.get_at(2).data)
print(ll.traverse())