stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

#[1,2,3] Bottom - Top

#Remove from top of stack
top = stack.pop()
print(top)

#Look at the top of stack without removing it
top = stack[-1]
print(top)
print(stack)