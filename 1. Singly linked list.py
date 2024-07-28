
# singly linked list

    #defind
class singlyNode:
    
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return str(self.val)
    
head = singlyNode(1)
A = singlyNode(5)
B = singlyNode(3)
C = singlyNode(2)

head.next = A
A.next = B
B.next = C

# traverse the list O(n)
curr = head
while curr:
    print(curr)
    curr = curr.next
    
# display the list O(n)
def Display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next 
    print(' -> '.join(elements))
    
Display(head)

# search for node value O(n)
def Search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False
print(Search(head, 9))

# reverse a linked list
def Reverse(head):
    prev = None
    current =  head
    while current:
        next_node = current.next 
        current.next = prev
        prev = current
        current = next_node
    return prev    
Display(Reverse(head))
