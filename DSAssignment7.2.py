class Node:
    def __init__(self, data):
        # Initialize a new node with data and a next pointer
        self.data = data
        self.next = None


class QueueList:
    def __init__(self):
        # Initialize an empty linked list with head and tail set to None
        self.head = None
        self.tail = None

    def insert_end(self, data):
        """Inserts a new node with data at the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            # If the list is empty, new node becomes both head and tail
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def remove_beginning(self):
        """Removes the node at the beginning of the linked list."""
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head is None:
            # If list becomes empty after removal, update the tail
            self.tail = None

    def traverse(self):
        """Traverses the linked list and prints its elements."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
if __name__ == "__main__":
    linked_list = QueueList()
    linked_list.insert_end(3)
    linked_list.traverse()  # Output: 1 -> 3 -> None

    linked_list.remove_beginning()
    linked_list.traverse()  # Output: None