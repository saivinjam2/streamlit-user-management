queue = []
queue.append('A')
queue.append('B')
queue.append('C')
print("Initial queue:", queue)

#peek
frontElement = queue[0]
print("Front element (peek):", frontElement)

#Dequeue
poppedElement = queue.pop(0)
print("Dequeued element:", poppedElement)
print("Queue after dequeue:", queue)

#isEmpty
isEmpty = not bool(queue)
print("Is the queue empty?", isEmpty)

#size
print("Size of the queue:", len(queue))

#Queue implementation using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            self.size += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return temp.data

    def peek(self):
        if self.front is None:
            return "Queue is empty"
        return self.front.data

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size
    
    def printQueue(self):
      temp = self.front
      while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
      print()

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", end="")
myQueue.printQueue()
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", end="")
myQueue.printQueue()
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())