# Singly Linked List Implementation in Python

This document showcases a Python-based singly linked list implementation. 
The implementation consists of two classes: Node and SinglyLinkedList. 
The Node class represents an element of the list. 
The SinglyLinkedList class provides methods to manipulate and interact with the list.



## Node Class

Developers use the Node class to create individual nodes in the linked list.
Each node contains data and a reference to the next node in the list.

### Constructor

```python
def __init__(self, data=None):
    self.data = data
    self.next = None
```

- **data**: The value stored in the node.
- **next**: A reference to the next node in the list (default is `None`).

### Representation

```python
def __repr__(self):
    return str(self.data)
```

Returns a string representation of the node's data.

## SinglyLinkedList Class

The `SinglyLinkedList` class provides methods to manage and manipulate a singly linked list.

### Constructor

```python
def __init__(self):
    self.head = None
```

Initializes an empty singly linked list with no head node.

### Append Method

```python
def append(self, data):
    ...
```

Appends a new node with the specified data to the end of the list.

**Examples**:


```python

sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
print(sll)  # Output: 1 → 2 → 3 → None
```

### Prepend Method

```python
def prepend(self, data):
    ...
```

Prepends a new node with the specified data to the beginning of the list.

**Examples**:

```python
sll = SinglyLinkedList()
sll.prepend(1)
sll.prepend(2)
sll.prepend(3)
print(sll)  # Output: 3 → 2 → 1 → None
```

### Delete with Value Method

```python
def delete_with_value(self, data):
    ...
```

Deletes the first node in the list with the specified value.

**Examples**:

```python
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.delete_with_value(2)
print(sll)  # Output: 1 → 3 → None
```

### Find Method

```python
def find(self, data):
    ...
```

Checks if a node with the specified value exists in the list.

**Returns**: `True` if the value exists, `False` otherwise.

**Examples**:

```python
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.find(2)  # Output: True
```

### Reverse Method

```python
def reverse(self):
    ...
```

Reverses the linked list in place.

**Examples**:

```python
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.reverse()
print(sll)  # Output: 3 → 2 → 1 → None
```

### Sort Method

```python
def sort(self, order="ascending"):
    ...
```

Sorts the linked list in either ascending or descending order.

**Arguments**:

- **order**: A string specifying the sort order. Acceptable values are `"ascending"` (default) or `"descending"`.

**Examples**:

```python
sll = SinglyLinkedList()
sll.append(3)
sll.append(1)
sll.append(2)
sll.sort()
print(sll)  # Output: 1 → 2 → 3 → None
sll.sort("descending")
print(sll)  # Output: 3 → 2 → 1 → None
```

### Iterator Method

```python
def __iter__(self):
    ...
```

Returns an iterator for the linked list.

**Examples**:

```python
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
iter_sll = iter(sll)
next(iter_sll)  # Output: 1
next(iter_sll)  # Output: 2
```

### Length Method

```python
def __len__(self):
    ...
```

Returns the length of the linked list.

**Examples**:

```python
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
len(sll)  # Output: 2
```

### String Representation Method

```python
def __repr__(self):
    ...
```

Returns a string representation of the linked list.

**Examples**:

```python
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
print(sll)  # Output: 1 → 2 → 3 → None
```


[Previous](../Docs/stack.md) | [Next](../Docs/double_linked_list.md)
