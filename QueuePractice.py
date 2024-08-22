#Initiate queue class
class Queue:
#CONSTRUCTOR
#Initialize contstructor function
    def __init__(self):
#Assign constructor to list
        self.items = []
#ENQUEUE
#Create enqueue function
    def enqueue(self, item):
#Add current attribute to end of queue
        self.items.append(item)
#DEQUEUE
#Create dequeue function
    def dequeue(self):
#If the function is not empty
        if not self.is_empty():
#Delete item at the beginning of the list
            return self.items.pop(0)
#Otherwise
        else:
#Output queue is empty
            raise IndexError("Queue is empty")
#EMPTY LIST
#Create empty list function
    def is_empty(self):
#Determine if queue is empty
        return len(self.items) == 0
#SIZE
#Create size function
    def size(self):
#Output the queue size
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")


#Check for script direction
if __name__ == "__main__":
#Initialize queue instance
    q = Queue()
#Check empty
    print("Before Queue;Is the queue empty?:", q.is_empty())
#Enqueue
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
#Check empty
    print("After enqueue; Is the queue empty?:", q.is_empty())
#Size
    print("First item in queue:", q.peek())
    print("Queue size:", q.size())
#Dequeue
    q.dequeue()
    q.dequeue()
    q.dequeue()
#Check empty
    print("After queue; Is the queue empty?:", q.is_empty())