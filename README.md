# This is a draft
# Python Data Structures Project

This project contains implementations of common data structures in Python, 
including a Queue and a Stack class.
Each class is thoroughly 
documented and includes examples of usage.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Queue Class](#queue-class)
- [Stack Class](#stack-class)
- [Singly Linked List Class](#singly-linked-list-class)
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
Here is an example of how to use the `Queue` and `Stack` classes:

### Queue Class

```python
from queue import  Queue

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.peek())     # Output: 2
```

### Stack Class

```python
from stack import Stack

s = Stack()
s.push(1)
s.push(2)
print(s.pop())   # Output: 2
print(s.peek())  # Output: 1
```
### Singly Linked List Class

```python
from singly_linked_list import Node, SinglyLinkedList
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
print(sll)  # Output: 1 -> 2 -> None
```

## Queue Class

For detailed documentation on the `Queue` class, please refer to [Queue_Docs.md](Queue_Docs.md).

## Stack Class

For detailed documentation on the `Stack` class, please refer to [Stack_Docs.md](Stack_Docs.md).

## Singly Linked List Class

for detailed documentation on the `SinglyLinkedList` class, please refer to [SinglyLinkedList_Docs.md](SinglyLinkedList_Docs.md).

## Testing

This project includes unit tests for the `Queue` and `Stack` classes. 
To run the tests, you will need to have `pytest` installed. 
You can install `pytest` using `pip`:


```sh
pip install pytest
```

To run the tests, navigate to the project directory and run:

```sh
pytest test_queue.py
pytest test_stack.py
```

```zsh
pytest test_queue.py
pytest test_stack.py
```

```bash
pytest test_queue.py
pytest test_stack.py
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
