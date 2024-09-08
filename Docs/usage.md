## Usage

You can import and use the classes in your own Python scripts.
Here are examples of how to use the `Queue`, `Stack`, `SinglyLinkedList`, and `DoublyLinkedList` classes:

### Queue

```python
from PyDataStructures import Queue

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue)  # Output: 1 -> 2 -> None
```

### Stack

```python
from PyDataStructures import Stack

stack = Stack()
stack.push(1)
stack.push(2)
print(stack)  # Output: 2 -> 1 -> None
```

### Singly Linked List

```python
from PyDataStructures import SinglyLinkedList

ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
print(ll)  # Output: 1 -> 2 -> None
```

### Doubly Linked List

```python
from PyDataStructures import DoublyLinkedList

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
print(dll)  # Output: 1 <-> 2 <-> None
```

---

[Previous](../Docs/installation.md) | [Next](../Docs/queue.md)
