class Node:
    def __init__(self,value = None, next = None, prev = None):
        self.val = value
        self.next = next
        self.prev= prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        ind = 0
        temp = self.head
        while ind < index:
            ind += 1
            temp = temp.next
        return temp.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(value=val, next=self.head)
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        new_node = Node(value=val, prev=temp)
        temp.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        ind = 0
        temp = self.head
        while ind < index:
            temp = temp.next
            ind += 1
        new = Node(value = val, next=temp, prev=temp.prev)
        if temp.prev:
            temp.prev.next = new
        temp.prev = new
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        temp = self.head
        if index == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
        else:
            ind = 0 
            while ind < index:
                temp = temp.next
                ind += 1
            if temp.next:
                temp.next.prev = temp.prev
            if temp.prev:
                temp.prev.next = temp.next
        self.size -= 1