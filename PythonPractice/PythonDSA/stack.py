stack = []
stack.append("a")
stack.append("b")
stack.append("c")
print("Initial stack:", stack)

#peek
topElement = stack[-1]
print("Top element (peek):", topElement)

#pop
poppesdElement = stack.pop()
print("Popped element:", poppesdElement)
print("Stack after pop:", stack)

#isEmpty
isEmpty = not bool(stack)
print("Is the stack empty?", isEmpty)

#size
size = len(stack)
print("Size of the stack:", size)

#creating a stack class: 
class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)

# Create a stack
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())

#Stack Implementation using Linked List
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0


