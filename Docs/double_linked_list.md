# Double Linked List Implementation

## Node Class

The `Node` class represents a single node in a doubly linked list.

### Attributes

- `data`: The data stored in the node.
- `prev`: Reference to the previous node in the list.
- `next`: Reference to the next node in the list.

### Methods

#### `__init__(self, data)`

Initializes a new node.

- **Parameters:**
  - `data`: The data to be stored in the node.

## DoubleLinkedList Class

The `DoubleLinkedList` class implements a doubly linked list, where each node contains references to both the next and previous nodes in the list.

### Attributes

- `head`: The first node in the list.
- `tail`: The last node in the list.

### Methods

#### `__init__(self)`

Initializes an empty doubly linked list.

#### `insert_at_beginning(self, data)`

Inserts a new node with the given data at the beginning of the list.

- **Parameters:**
  - `data`: The data to be inserted.

#### `insert_at_end(self, data)`

Inserts a new node with the given data at the end of the list.

- **Parameters:**
  - `data`: The data to be inserted.

#### `delete_node(self, key)`

Deletes the first occurrence of a node with the given key.

- **Parameters:**
  - `key`: The data value to search for and delete.

#### `display_forward(self)`

Displays the list contents from head to tail.

#### `display_backward(self)`

Displays the list contents from tail to head.

## Usage Examples

Here are some examples demonstrating how to use the `DoubleLinkedList` class:

### Creating and Populating a List

```python
# Create a new double linked list
dll = DoubleLinkedList()

# Insert elements at the beginning
dll.insert_at_beginning(10)
dll.insert_at_beginning(5)

```

### Deleting Nodes

```python
# Delete a node
dll.delete_node(15)

# Display the updated list
print("List after deleting 15:")
dll.display_forward()
# Output: 5 -> 10 -> 20
```

### Working with an Empty List

```python
# Create an empty list
empty_list = DoubleLinkedList()

# Try to delete from an empty list
empty_list.delete_node(5)  # This should handle the empty list case gracefully

# Insert into an empty list
empty_list.insert_at_end(100)
print("Empty list after insertion:")
empty_list.display_forward()
# Output: 100
```
