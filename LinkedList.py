class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.size = 0 # node의 개수
        self.head = None



    def insert_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node  


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        # 맨 뒤의 node가 new_node를 가리켜야 한다.
        else:
            current = self.head
            while(current.next):
                current=current.next
            current.next = new_node

    def appendTail(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next            
    
    def get(self, idx): # 시간 복잡도 O(n)
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def insert(self, idx, value):
        new_node = Node(value)
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(idx-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node


    def remove(self, idx):
        if idx == 0:
            self.head = self.head.next # gabage collector가 알아서 처리해준다.
        else:
            current = self.head
            for _ in range(idx-1):
                current = current.next
            current.next = current.next.next

    
    def print(self):
        current = self.head
        while(current): # while하고 조건없이 current 하나만 달랑 들어가있는게 무슨 의미인지 잘 모르겠다... 사실 while 잘 써본적 없음
            print(current.value, end = "")
            current = current.next
            if current:
                print("->" , end="")
        print()


l1 = LinkedList()
l1.insert_back(1)
l1.insert_back(2)
l1.insert_back(3)
l1.insert_back(4)
l1.insert_back(5)
# l1.remove(3)

l1.print()


