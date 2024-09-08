# Simple implementation of a singly linked list in Python

class Node:
    """ Create a node with data and a reference to the next node. """

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class SinglyLinkedList:
    """ Create a singly linked list with a head node.

        Returns:
            SinglyLinkedList: A new instance of a singly linked list.

        Examples:
            >>> sll = SinglyLinkedList()
            >>> sll.append(1)
            >>> sll.append(2)
            >>> sll.prepend(3)
            >>> print(sll)
            3 → 1 → 2 → None
            >>> len(sll)
            3
            >>> sll.find(2)
            True
            >>> sll.reverse()
            >>> print(sll)
            2 → 1 → 3 → None
            >>> sll.sort()
            >>> print(sll)
            1 → 2 → 3 → None
    """

    def __init__(self):
        """ Initialize an empty singly linked list. """
        self.head = None

    def append(self, data):
        """ Append a new node to the end of the list.

        Returns:
            None

        Examples:
            >>> sll = SinglyLinkedList()
            >>> sll.append(1)
            >>> sll.append(2)
            >>> sll.append(3)
            >>> print(sll)
            1 → 2 → 3 → None
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """ Prepend a new node to the beginning of the list.

        Returns:
            None

        Examples:
            >>> sll = SinglyLinkedList()
            >>> sll.prepend(1)
            >>> sll.prepend(2)
            >>> sll.prepend(3)
            >>> print(sll)
            3 → 2 → 1 → None
        """

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_data(self, find_value, insert_value):
        """ Insert a new node after a given node with a specific value.

        Returns:
            None

        Examples:
            >>> sll = SinglyLinkedList()
            >>> sll.append(1)
            >>> sll.append(2)
            >>> sll.append(3)
            >>> sll.insert_after_data(2,4)
            >>> print(sll)
            1 → 2 → 4 → 3 → None

        """
        if not self.head:
            return

        current_node = self.head
        while current_node:
            if current_node.data == find_value:
                new_node = Node(insert_value)
                new_node.next = current_node.next
                current_node.next = new_node
                break
            current_node = current_node.next

    def insert_before_data(self, find_value, insert_value):
        """ Insert a new node before a given node with a specific value.

        Returns:
            None

            Examples:
            >>> sll = SinglyLinkedList()
            >>> sll.append(1)
            >>> sll.append(2)
            >>> sll.append(3)
            >>> sll.insert_before_data(2,4)
            >>> print(sll)
            1 → 4 → 2 → 3 → None

         """
        if self.head is None:
            return

        if self.head.data == find_value:
            self.prepend(insert_value)
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.data == find_value:
                new_node = Node(insert_value)
                new_node.next = current_node.next
                current_node.next = new_node
                break
            current_node = current_node.next

    def delete_with_value(self, data):
        """ Delete the first node with a given value.

        Returns:
            None

        Examples:
            >>> sll = SinglyLinkedList()
            >>> sll.append(1)
            >>> sll.append(2)
            >>> sll.append(3)
            >>> sll.delete_with_value(2)
            >>> print(sll)
            1 → 3 → None
        """

        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

    def find(self, data):
        """ Check if a node with a given value exists in the list.

        Returns:
                bool: True if the value exists, False otherwise.

        Examples:
            >>> sll = SinglyLinkedList()
            >>> sll.append(1)
            >>> sll.append(2)
            >>> sll.append(3)
            >>> sll.find(2)
            True
        """

        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def reverse(self):
        """ Reverse the list in place.

        Returns:
            None

        Examples:
            >>> sll = SinglyLinkedList()
            >>> sll.append(1)
            >>> sll.append(2)
            >>> sll.append(3)
            >>> sll.reverse()
            >>> print(sll)
            3 → 2 → 1 → None
        """
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def sort(self, order="ascending"):
        """ Sort the list in ascending order.

        Args:
            order (str): The order to sort the list. Default is 'ascending' so no need to specify.
            order (str): descending: Sort the list in descending order.

        Returns:
            None

        Examples:
            >>> sll = SinglyLinkedList()
            >>> sll.append(3)
            >>> sll.append(1)
            >>> sll.append(2)
            >>> sll.sort()
            >>> print(sll)
            1 → 2 → 3 → None
            >>> sll.sort("descending")
            >>> print(sll)
            3 → 2 → 1 → None
        """

        if not self.head:
            return

        if order not in ["ascending", "descending"]:
            raise ValueError("Invalid order value. Use 'ascending' or 'descending'.")

        def compare(x, y):
            if order == "ascending":
                return x > y
            else:  # order is "descending"
                return x < y

        current_node = self.head
        while current_node:
            next_node = current_node.next
            while next_node:
                if compare(current_node.data, next_node.data):
                    current_node.data, next_node.data = next_node.data, current_node.data
                next_node = next_node.next
            current_node = current_node.next

    def __iter__(self):
        """ Return an iterator for the list.

        Returns:
            self: The iterator object.

        Examples:
            >>> sll = SinglyLinkedList()
            >>> sll.append(1)
            >>> sll.append(2)
            >>> iter_sll = iter(sll)
            >>> next(iter_sll)
            1
            >>> next(iter_sll)
            2
            >>> next(iter_sll)
            Traceback (most recent call last):
            ...
            StopIteration
        """

        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def __len__(self):
        """ Return the length of the list.

         Returns:
            int: The length of the list.

        Examples:
            >>> sll = SinglyLinkedList()
            >>> sll.append(1)
            >>> sll.append(2)
            >>> len(sll)
            2
        """

        return sum(1 for _ in self)

    def __str__(self):
        """ Return a string representation of the list.

        Returns:
            str: A string representation of the list.

        Examples:
            >>> sll = SinglyLinkedList()
            >>> sll.append(1)
            >>> sll.append(2)
            >>> sll.append(3)
            >>> print(sll)
            1 → 2 → 3 → None
        """

        return self.__repr__()

    def __repr__(self):
        """ Return a string representation of the list.

        Returns:
            str: A string representation of the list.

        Examples:
            >>> sll = SinglyLinkedList()
            >>> sll.append(1)
            >>> sll.append(2)
            >>> sll.append(3)
            >>> print(sll)
            1 → 2 → 3 → None
        """

        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        nodes.append("None")
        return ' → '.join(nodes)
