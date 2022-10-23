package main

import "fmt"

type Node struct {
	Data interface{}
	Next *Node
}

type LinkedList struct {
	NodeCount int
	Head      *Node
	Tail      *Node
}

func (ll *LinkedList) GetAt(pos int) *Node {
	if pos < 1 || pos > ll.NodeCount {
		return nil
	}
	curr := ll.Head
	for i := 1; i < pos; i++ {
		curr = curr.Next
	}
	return curr
}

func (ll *LinkedList) Traverse() []*Node {
	var answer []*Node
	curr := ll.Head
	for curr != nil {
		answer = append(answer, curr)
		curr = curr.Next
	}
	return answer
}

func (ll *LinkedList) InsertAt(pos int, newNode *Node) error {
	if pos < 1 || pos > ll.NodeCount+1 {
		return fmt.Errorf("Check Index")
	}
	if pos == 1 {
		newNode.Next = ll.Head
		ll.Head = newNode
	} else {
		if pos == ll.NodeCount+1 {
			newNode.Next = ll.Tail.Next
			ll.Tail = newNode
		} else {
			newNode.Next = ll.GetAt(pos - 1).Next
		}
		ll.GetAt(pos - 1).Next = newNode
	}
	ll.NodeCount += 1
	return nil
}

func (ll *LinkedList) PopAt(pos int) *Node {
	if pos < 1 || pos > ll.NodeCount {
		return nil
	}
	n := ll.GetAt(pos)
	if pos == 1 {
		if ll.NodeCount == 1 {
			ll.Head = nil
			ll.Tail = nil
		} else {
			ll.Head = ll.Head.Next
		}
	} else {
		prev := ll.GetAt(pos - 1)
		if pos == ll.NodeCount {
			prev.Next = nil
			ll.Tail = prev
		} else {
			prev.Next = n.Next
		}
	}
	ll.NodeCount -= 1
	return n
}

// 변수 선언시 *를 붙이면 pointer형 변수로 메모리 주소를 값으로 가진다.
// 이미 선언된 포인터 변수를 사용시 &를 붙이면 해당 변수의 메모리 주소.
// 이미 선언된 포인터 변수를 사용시 *를 붙이면 주소에 할당된 값.
func MakeNode(data interface{}) *Node {
	return &Node{data, nil}
}

func MakeLinkedList() *LinkedList {
	return &LinkedList{0, nil, nil}
}

func main() {
	node1 := MakeNode(1)
	node2 := MakeNode(2)
	node1.Next = node2

	list := MakeLinkedList()
	list.NodeCount = 2
	list.Head = node1
	list.Tail = node2

	fmt.Println(list.GetAt(1).Data)
	fmt.Println(list.Traverse())
	for _, node := range list.Traverse() {
		fmt.Println(node.Data)
	}
}
