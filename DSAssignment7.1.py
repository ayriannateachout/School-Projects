class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

# Example usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    print("Enqueued 1")
    q.enqueue(2)
    print("Enqueued 2")
    q.enqueue(3)
    print("Enqueued 3")

    print("Queue size:", q.size())
    print("Front of queue:", q.peek())

    print("Dequeued:", q.dequeue())
    print("Dequeued:", q.dequeue())
    print("Dequeued:", q.dequeue())

    print("Is the queue empty?", q.is_empty())