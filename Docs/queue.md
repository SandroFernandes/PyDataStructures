# Queue Class

## Methods:

- **__init__**: Initializes an empty queue.

    Example:
    ```python
    >>> q = Queue()
    >>> q.is_empty()
    True
    ```

- **is_empty**: Checks if the queue is empty.

    Returns:
        bool: True if the queue is empty, False otherwise.

    Example:
    ```python
    >>> q = Queue()
    >>> q.is_empty()
    True
    >>> q.enqueue(1)
    >>> q.is_empty()
    False
    ```

- **enqueue**: Adds an item to the end of the queue.

    Args:
        item: The item to be added to the queue.

    Example:
    ```python
    >>> q = Queue()
    >>> q.enqueue(1)
    >>> q.enqueue(2)
    >>> str(q)
    '[1, 2]'
    ```

- **dequeue**: Removes and returns the item from the front of the queue.

    Returns:
        The item from the front of the queue.

    Raises:
        IndexError: If the queue is empty.

    Example:
    ```python
    >>> q = Queue()
    >>> q.enqueue(1)
    >>> q.enqueue(2)
    >>> q.dequeue()
    1
    >>> str(q)
    '[2]'
    ```

- **peek**: Returns the item at the front of the queue without removing it.

    Returns:
        The item at the front of the queue.

    Raises:
        IndexError: If the queue is empty.

    Example:
    ```python
    >>> q = Queue()
    >>> q.enqueue(1)
    >>> q.enqueue(2)
    >>> q.peek()
    1
    ```

- **size**: Returns the number of items in the queue.

    Returns:
        int: The number of items in the queue.

    Example:
    ```python
    >>> q = Queue()
    >>> q.enqueue(1)
    >>> q.enqueue(2)
    >>> q.size()
    2
    ```

- **__str__**: Returns a string representation of the queue.

    Returns:
        str: A string representation of the queue.

    Example:
    ```python
    >>> q = Queue()
    >>> q.enqueue(1)
    >>> q.enqueue(2)
    >>> str(q)
    '[1, 2]'
    ```

- **__iter__**: Returns the iterator object itself.

    Returns:
        self: The iterator object.

    Example:
    ```python
    >>> q = Queue()
    >>> q.enqueue(1)
    >>> q.enqueue(2)
    >>> iter_q = iter(q)
    >>> next(iter_q)
    1
    ```

- **__next**: Returns the next item from the queue during iteration.

    Returns:
        The next item in the queue.

    Raises:
        StopIteration: If all items have been iterated.

    Example:
    ```python
    >>> q = Queue()
    >>> q.enqueue(1)
    >>> q.enqueue(2)
    >>> iter_q = iter(q)
    >>> next(iter_q)
    1
    >>> next(iter_q)
    2
    >>> next(iter_q)
    Traceback (most recent call last):
        ...
    StopIteration
    ```

- **next**: Removes and returns the item from the front of the queue.

    Returns:
        The item from the front of the queue.

    Raises:
        IndexError: If the queue is empty.

    Example:
    ```python
    >>> q = Queue()
    >>> q.enqueue(1)
    >>> q.enqueue(2)
    >>> q.next()
    1
    >>> str(q)
    '[2]'
    ```
