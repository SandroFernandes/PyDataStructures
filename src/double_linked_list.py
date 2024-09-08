class Node:
    """
    A node in a doubly linked list.

    Attributes:
        data: The data stored in the node.
        prev: Reference to the previous node in the list.
        next: Reference to the next node in the list.
    """

    def __init__(self, data):
        """
        Initialize a new node.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    """
    A doubly linked list implementation.

    This class represents a doubly linked list, where each node contains
    references to both the next and previous nodes in the list.

    Attributes:
        head: The first node in the list.
        tail: The last node in the list.

    >>> dll = DoubleLinkedList()
    >>> dll.display_forward()
    None
    """

    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        """
        Insert a new node with the given data at the beginning of the list.

        Args:
            data: The data to be inserted.

        >>> dll = DoubleLinkedList()
        >>> dll.insert_at_beginning(1)
        >>> dll.display_forward()
        1 <-> None
        >>> dll.insert_at_beginning(2)
        >>> dll.display_forward()
        2 <-> 1 <-> None
        """
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node with the given data at the end of the list.

        Args:
            data: The data to be inserted.

        >>> dll = DoubleLinkedList()
        >>> dll.insert_at_end(1)
        >>> dll.display_forward()
        1 <-> None
        >>> dll.insert_at_end(2)
        >>> dll.display_forward()
        1 <-> 2 <-> None
        """
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_node(self, key):
        """
        Delete the first occurrence of a node with the given key.

        Args:
            key: The data value to search for and delete.

        >>> dll = DoubleLinkedList()
        >>> dll.insert_at_end(1)
        >>> dll.insert_at_end(2)
        >>> dll.insert_at_end(3)
        >>> dll.delete_node(2)
        >>> dll.display_forward()
        1 <-> 3 <-> None
        >>> dll.delete_node(1)
        >>> dll.display_forward()
        3 <-> None
        >>> dll.delete_node(3)
        >>> dll.display_forward()
        None
        """
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def display_forward(self):
        """
        Display the list contents from head to tail.

        Prints the data of each node in the list, separated by ' <-> '.

        >>> dll = DoubleLinkedList()
        >>> dll.insert_at_end(1)
        >>> dll.insert_at_end(2)
        >>> dll.insert_at_end(3)
        >>> dll.display_forward()
        1 <-> 2 <-> 3 <-> None
        """
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        """
        Display the list contents from tail to head.

        Prints the data of each node in the list, separated by ' <-> '.

        >>> dll = DoubleLinkedList()
        >>> dll.insert_at_end(1)
        >>> dll.insert_at_end(2)
        >>> dll.insert_at_end(3)
        >>> dll.display_backward()
        3 <-> 2 <-> 1 <-> None
        """
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

