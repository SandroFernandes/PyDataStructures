# This is a draft
# Python Data Structures Project

This project contains implementations of common data structures in Python, 
including Queue, Stack, Singly Linked List, and Doubly Linked List classes.
Each class is thoroughly documented and includes examples of usage.

## Table of Contents

- [This is a draft](#this-is-a-draft)
- [Python Data Structures Project](#python-data-structures-project)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Queue Class](#queue-class)
    - [Stack Class](#stack-class)
    - [Singly Linked List Class](#singly-linked-list-class)
    - [Doubly Linked List Class](#doubly-linked-list-class)
  - [Testing](#testing)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

To use the classes in this project, clone the repository:

```sh
git clone https://github.com/SandroFernandes/PyDataStructures.git
```

Navigate to the project directory:

```sh
cd PyDataStructures
```

## Usage

You can import and use the classes in your own Python scripts.
Here are examples of how to use the `Queue`, `Stack`, `SinglyLinkedList`, and `DoublyLinkedList` classes:

### Queue Class

(my_queue.py does not clash with standard library queue)

```python
from my_queue import Queue

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.peek())     # Output: 2
```
For detailed documentation on the [`Queue`](queue.md) class, 

### Stack Class

```python
from stack import Stack

s = Stack()
s.push(1)
s.push(2)
print(s.pop())   # Output: 2
print(s.peek())  # Output: 1
```
For detailed documentation on the `Stack` class, please refer to [Stack_Docs.md](Stack_Docs.md).


### Singly Linked List Class

```python
from singly_linked_list import Node, SinglyLinkedList

sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
print(sll)  # Output: 1 -> 2 -> None
```
For detailed documentation on the `SinglyLinkedList` class, please refer to [SinglyLinkedList_Docs.md](SinglyLinkedList_Docs.md).



### Doubly Linked List Class

```python
from doubly_linked_list import Node, DoublyLinkedList

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
print(dll)  # Output: 1 <-> 2 <-> None
```
For detailed documentation on the `DoublyLinkedList` class, please refer to [DoublyLinkedList_Docs.md](DoublyLinkedList_Docs.md).



## Testing

This project includes unit tests for all classes (`Queue`, `Stack`, `SinglyLinkedList`, and `DoublyLinkedList`). 
To run the tests, you will need to have `pytest` installed. 
You can install `pytest` using `pip`:


```sh
pip install pytest
```

To run all tests, navigate to the project directory and execute:

```sh
pytest
```

If you want to run tests for a specific class, you can use:

```sh
pytest test_queue.py
pytest test_stack.py
pytest test_singly_linked_list.py
pytest test_doubly_linked_list.py
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
