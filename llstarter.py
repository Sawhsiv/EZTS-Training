class Node:
    def __init__(self,data):
        self.value=data
        self.next=None

Head=Tail=Node(10)

Tail.next=Node(20)
Tail=Tail.next

Tail.next=Node(30)
Tail=Tail.next

Tail.next=Node(40)
Tail=Tail.next