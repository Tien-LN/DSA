# LIFO - last in first out
# define

stk = []
print(stk)

# Append to top of stack O(1)

stk.append(1)
stk.append(2)
stk.append(3)
stk.append(4)
print(stk)

# Pop from stack O(1)

stk.pop()
print(stk)

# Ask what's on top of stack O(1)

print(stk[-1]) # better check if stack is empty or not first

# Ask if stack is empty or not O(1)

if stk:                 # or we can compare length of stack with 0
    print(False)
else:
    print(True)
    
