# FIFO - First in first out
# define
from collections import deque

q = deque()
print(q)

# Enqueue - add element to the right - O(1)

q.append(1)
q.append(2)
q.append(3)
q.append(4)
q

# Dequeue (pop left) - remove element from the left - O(1)

q.popleft()
q.popleft()
q 

# peek from the left side - O(1)

q[0]

# peek from the right side - O(1)

q[-1]