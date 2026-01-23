#Trversal of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)  # Output: 7 -> 11 -> 3 -> 2 -> 9 -> null

#Find the lowest value in a linked list
def findLowestValue(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue

print(findLowestValue(node1))  # Output: 2

#deleteing a node from linked list
def deleteNode(head, target):
    if head.data == target:
        return head.next  # Deleted head node

    currentNode = head
    while currentNode.next and currentNode.next != target:
        currentNode = currentNode.next  # Bypass the target node
    if currentNode.next is None:
        return head
    
    currentNode.next = currentNode.next.next
    return head  # Target not found; return original head

node1 = deleteNode(node1, node4)
print("\nAfter deletion:")
traverseAndPrint(node1)

#Inserting a node in linked list
def insertNodeAtPosition(head, newNode, position):
  if position == 1:
    newNode.next = head
    return newNode

  currentNode = head
  for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  newNode.next = currentNode.next
  currentNode.next = newNode
  return head

newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)
print("\nAfter insertion:")
traverseAndPrint(node1)
