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