STACK_IS_EMPTY = "Stack is empty."
STACK_IS_LESS_THAN_TWO = "Stack has fewer than two elements."


class StackException(Exception):
    """Exception raised for errors related to stack operations."""

    def __init__(self, message: str):
        super(StackException, self).__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class Stack:
    """A simple stack implementation.

    This class provides a simple stack implementation.
    It allows you to push, pop items from the stack.
    You can also check if the stack is empty, peek at the top item, swap the top two items,
    dump, reverse, clone the entire stack, rever.

    Examples:
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> stack.peek()
        3
        >>> stack.pop()
        3
        >>> stack.pop()
        2
        >>> stack.is_empty()
        False
        >>> stack.dump()
        [1]
        >>> stack.size()
        0
        >>> str(stack)
        '[]'
    """

    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []
        self._index = 0

    def push(self, item):
        """Push an item onto the stack.

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> str(stack)
            '[1, 2]'
        """
        self.stack.append(item)

    def pop(self):
        """Pop an item from the stack.

        Raises:
            StackIsEmpty: If the stack is empty.

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.pop()
            2
            >>> stack.pop()
            1
            >>> stack.is_empty()
            True
        """
        if not self.is_empty():
            return self.stack.pop()
        raise StackException(STACK_IS_EMPTY)

    def is_empty(self):
        """Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.

        Examples:
            >>> stack = Stack()
            >>> stack.is_empty()
            True
            >>> stack.push(1)
            >>> stack.is_empty()
            False
        """
        return len(self.stack) == 0

    def peek(self):
        """Peek at the top item of the stack without removing it.

        Raises:
            StackIsEmpty: If the stack is empty.

        Returns:
            The top item of the stack.

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.peek()
            2
        """
        if not self.is_empty():
            return self.stack[-1]
        raise StackException(STACK_IS_EMPTY)

    def dump(self):
        """Clear the stack and return the previous contents.

        Returns:
            list: The previous contents of the stack.

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.dump()
            [1, 2]
            >>> stack.is_empty()
            True
        """
        tmp = self.stack[:]
        self.stack.clear()
        return tmp

    def size(self):
        """Get the number of items in the stack.

        Returns:
            int: The number of items in the stack.

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.size()
            1
        """
        return len(self.stack)

    def clear(self):
        """Clear all items from the stack.

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.clear()
            >>> stack.is_empty()
            True
        """
        self.stack.clear()

    def contains(self, item):
        """Check if the stack contains a specific item.

        Returns:
            bool: True if the item is in the stack, False otherwise.

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.contains(1)
            True
            >>> stack.contains(3)
            False
        """
        return item in self.stack

    def reverse(self):
        """Reverse the order of items in the stack.

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.push(3)
            >>> stack.reverse()
            >>> str(stack)
            '[3, 2, 1]'
        """
        self.stack.reverse()

    def clone(self):
        """Create a shallow copy of the stack.

        Returns:
            Stack: A new stack with the same items.

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack_clone = stack.clone()
            >>> str(stack_clone)
            '[1, 2]'
        """
        new_stack = Stack()
        new_stack.stack = self.stack[:]
        return new_stack

    def swap(self):
        """Swap the top two elements of the stack.

        Raises:
            StackExceprion: If the stack has fewer than two elements.

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> stack.swap()
            >>> stack.pop()
            1
            >>> stack.pop()
            2
        """
        if len(self.stack) < 2:
            raise StackException(STACK_IS_LESS_THAN_TWO)
        self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

    def __iter__(self):
        """Return an iterator for the stack.

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> for item in stack:
            ...print(item)
            1
            2
        """
        self._index = 0
        return self

    def __next__(self):
        """Get the next item from the stack.

        Raises:
            StopIteration: If there are no more items in the stack.

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> iterator = iter(stack)
            >>> next(iterator)
            1
            >>> next(iterator)
            2
            >>> next(iterator)
            Traceback (most recent call last):
                ...
            StopIteration
            >>>for item in stack:
            >>>    print(item)
            1
            2

        """
        if self._index < len(self.stack):
            result = self.stack[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __len__(self):
        """Get the number of items in the stack.

        Returns:
            int: The number of items in the stack.

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> len(stack)
            1
        """
        return self.size()

    def __str__(self):
        """Get a string representation of the stack.

        Returns:
            str: A string representation of the stack.

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> str(stack)
            '[1, 2]'
        """
        return str(self.stack)

    def __repr__(self):
        """Get a detailed string representation of the stack.

        Returns:
            str: A detailed string representation of the stack.

        Examples:
            >>> stack = Stack()
            >>> stack.push(1)
            >>> stack.push(2)
            >>> repr(stack)
            '[1, 2]'
        """
        return self.__str__()
