# Stack class

## Methods:
    
- push: Adds a new element to the stack.

- pop: Removes the top element from the stack.
       Raises an exception if the stack is empty.

- is_empty: Returns True if the stack is empty, False otherwise.

- peek: Returns the top element of the stack.
        Raises an exception if the stack is empty.

- dump: Returns all elements in the stack.
        Resets the stack to an empty state.

- size: Returns the number of elements in the stack.

- clear: Clears all items from the stack.

- contains: Checks if the stack contains a specific item.

- reverse: Reverses the order of items in the stack.

- clone: Creates a shallow copy of the stack.

- __iter__: Returns an iterator for the stack.

- swap: Swaps the top two elements of the stack.
        Raises an exception if the stack has fewer than two elements.

- __len__: Returns the number of elements in the stack.

- __str__: Returns a string representation of the stack.

Raises:
    StackException: Base exception class for the stack.
    message: A message describing the exception.    
        
    The following messages are used in the Stack class:
        "Stack is empry": If the stack is empty when pop or peek is called.
        "Stack has fewer than two elements.": If the stack has fewer than two elements when swap is called.

Examples:
```python
>>> stack = Stack()
>>> stack.push(1)
>>> stack.push(2)
>>> stack.push(3)
>>> stack.size()
3
>>> stack.pop()
3
>>> stack.peek()
2
>>> stack.is_empty()
False
>>> stack.dump()
[1, 2]
>>> stack.size()
0
>>> stack.is_empty()
True
>>> stack.push(1)
>>> stack.push(2)
>>> stack.contains(1)
True
>>> stack.contains(3)
False
>>> stack.reverse()
>>> str(stack)
'[2, 1]'
>>> stack_clone = stack.clone()
>>> str(stack_clone)
'[2, 1]'
>>> stack.clear()
>>> stack.is_empty()
True
>>> stack.push(1)
>>> stack.push(2)
>>> stack.push(3)
>>> for item in stack:
...     print(item)
1
2
3
>>> stack.swap()
>>> stack.pop()
2
>>> stack.pop()
3
