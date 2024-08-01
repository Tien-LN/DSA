# define
class DoublyNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val 
        self.next = next
        self.prev = prev
        
    def __str__(self):
        return(str(self.val))
    
head = tail = DoublyNode(1)
print(head)

# Display O(n):
def Display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next 
    print(' <-> '.join(elements))

Display(head)

# Insert at beginning O(1)
def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next = head)
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, 7)
Display(head)

# Insert at end O(1)
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev = tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 15)
Display(head)