# Stack class

## Methods:
    
- push: Adds a new element to the stack.
```python
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
# outputs: 1 -> 2 -> 3 -> None
```
- pop: Removes the top element from the stack.
       Raises an exception if the stack is empty.

```python
stack = Stack()
stack.push(1)
stack.push(2)
# outputs:1 -> 2 -> None
stack.pop()
# outputs:1 -> None
```


- is_empty: Returns True if the stack is empty, False otherwise.
```python
stack = Stack()
stack.is_empty()
# Outputs:True
stack.push(1)
stack.is_empty()
# Outputs:False
```

- peek: Returns the top element of the stack.
        Raises an exception if the stack is empty.
```python
stack = Stack()
stack.push(1)
stack.push(2)
stack.peek()
# Outputs:2
stack.pop()
# Outputs:1
```
- dump: Returns all elements in the stack and clears the stack.
```python
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
str(stack)
# Outputs:1 -> 2 -> 3 -> None
tmp = stack.dump()
stack.is_empty()
# Outputs:True
print(tmp)
# Outputs:1 -> 2 -> 3 -> None
```

- size: Returns the number of elements in the stack.
```python
stack = Stack()
stack.size()
# Outputs:0
stack.push(1)
stack.push(2)
stack.size()
# Outputs:2
```

- clear: Clear all items from the stack.
```python
stack = Stack()
stack.push(1)
stack.push(2)
str(stack)
# Outputs:1 -> 2 -> None
stack.clear()
stack.is_empty()
# Outputs:True
str(stack)
# Outputs:None
```
- contains: Checks if the stack contains a specific item.

```python
stack = Stack()
stack.push(1)
stack.push(2)
stack.contains(1)
# Outputs:True
stack.contains(3)
# Outputs:False
```

- reverse: Reverses the order of items in the stack.

```python
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
# Outputs:1 -> 2 -> 3 -> None
stack.reverse()
print(stack)
# Outputs:1 -> 2 -> 3 -> None
print(stack)
# Outputs:3 -> 2 -> 1 -> None
```

- clone: Create a shallow copy of the stack, keeping the original stack intact.

```python
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
# Outputs:1 -> 2 -> 3 -> None
clone = stack.clone()
print(clone)
# Outputs:1 -> 2 -> 3 -> None
print(stack)
# Outputs:1 -> 2 -> 3 -> None
```


- swap: Swap the top two elements of the stack.
        Raises an exception if the stack has fewer than two elements.

```python
stack = Stack()
stack.push(1)
stack.push(2)
print(stack)
# Outputs:1 -> 2 -> None
stack.swap()
print(stack)
# Outputs:2 -> 1 -> None
```

- __iter__: Returns an iterator for the stack.

```python
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
iter_stack = iter(stack)
next(iter_stack)
# Outputs:1
next(iter_stack)
# Outputs:2
next(iter_stack)
# Outputs:3
```



- __len__: Returns the number of elements in the stack.

```python 
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
len(stack)
# Outputs:3
```

- __str__: Returns a string representation of the stack.

```python
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
# Outputs:1 -> 2 -> 3 -> None
```

StackException: 

Base exception class for the stack.

message: A message describing the exception.    
        
Raises:
"Stack is empty."
If you use the method pop or peek at an empty stack.

Raises:
"Stack has fewer than two elements."
If a stack has fewer than two elements and someone calls swap.
