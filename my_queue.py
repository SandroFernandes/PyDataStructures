class Queue:
    """
    A simple implementation of a queue data structure.
    """

    def __init__(self):
        """
        Initializes an empty queue.

        Example:
            >>> q = Queue()
            >>> q.is_empty()
            True
        """
        self.items = []
        self._index = 0

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.

        Example:
            >>> q = Queue()
            >>> q.is_empty()
            True
            >>> q.enqueue(1)
            >>> q.is_empty()
            False
        """
        return len(self.items) == 0

    def enqueue(self, item):
        """
        Adds an item to the end of the queue.

        Args:
            item: The item to be added to the queue.

        Example:
            >>> q = Queue()
            >>> q.enqueue(1)
            >>> q.enqueue(2)
            >>> str(q)
            '[1, 2]'
        """
        self.items.append(item)

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.

        Returns:
            The item from the front of the queue.

        Raises:
            IndexError: If the queue is empty.

        Example:
            >>> q = Queue()
            >>> q.enqueue(1)
            >>> q.enqueue(2)
            >>> q.dequeue()
            1
            >>> str(q)
            '[2]'
        """
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def peek(self):
        """
        Returns the item at the front of the queue without removing it.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.

        Example:
            >>> q = Queue()
            >>> q.enqueue(1)
            >>> q.enqueue(2)
            >>> q.peek()
            1
        """
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from an empty queue")

    def size(self):
        """
        Returns the number of items in the queue.

        Returns:
            int: The number of items in the queue.

        Example:
            >>> q = Queue()
            >>> q.enqueue(1)
            >>> q.enqueue(2)
            >>> q.size()
            2
        """
        return len(self.items)

    def __str__(self):
        """
        Returns a string representation of the queue.

        Returns:
            str: A string representation of the queue.

        Example:
            >>> q = Queue()
            >>> q.enqueue(1)
            >>> q.enqueue(2)
            >>> str(q)
            '[1, 2]'
        """
        return str(self.items)

    def __iter__(self):
        """
        Returns an iterator for the queue.

        This method allows the queue to be used in a for loop.

        Returns:
            iterator: An iterator over the queue's items.

        Example:
            >>> q = Queue()
            >>> q.enqueue(1)
            >>> q.enqueue(2)
            >>> q.enqueue(3)
            >>> for item in q:
            ...     print(item)
            1
            2
            3
        """
        return iter(self.items)

    def next(self):
        """
        Removes and returns the item from the front of the queue.
        This method is an alias for dequeue() to demonstrate
        different naming conventions.

        Returns:
            The item from the front of the queue.

        Raises:
            IndexError: If the queue is empty.

        Example:
            >>> q = Queue()
            >>> q.enqueue(1)
            >>> q.enqueue(2)
            >>> q.next()
            1
            >>> str(q)
            '[2]'
        """
        return self.dequeue()
