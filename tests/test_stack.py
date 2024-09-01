import pytest
from ..stack import (Stack,
                     StackException,
                     STACK_IS_EMPTY,
                     STACK_IS_LESS_THAN_TWO)


def test_stack_is_empty_exception():
    with pytest.raises(StackException) as excinfo:
        raise StackException("Stack is empty")
    assert str(excinfo.value) == "Stack is empty"


def test_stack_is_too_small_exception():
    with pytest.raises(StackException) as excinfo:
        raise StackException("Stack is too small")
    assert str(excinfo.value) == "Stack is too small"


def test_push():
    stack = Stack()
    stack.push(1)
    assert len(stack) == 1
    assert stack.peek() == 1


def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert len(stack) == 1
    assert stack.pop() == 1
    assert stack.is_empty()


def test_pop_empty():
    stack = Stack()
    with pytest.raises(StackException):
        stack.pop()


def test_is_empty():
    stack = Stack()
    assert stack.is_empty()
    stack.push(1)
    assert not stack.is_empty()
    stack.pop()
    assert stack.is_empty()


def test_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    stack.pop()
    assert stack.peek() == 1


def test_peek_empty():
    stack = Stack()
    with pytest.raises(StackException):
        stack.peek()


def test_dump():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    dumped_stack = stack.dump()
    assert dumped_stack == [1, 2, 3]
    assert stack.is_empty()


def test_size():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.size() == 3
    stack.pop()
    assert stack.size() == 2
    stack.pop()
    assert stack.size() == 1
    stack.pop()
    assert stack.size() == 0
    assert stack.is_empty()


def test_len():
    stack = Stack()
    assert len(stack) == 0
    stack.push(1)
    assert len(stack) == 1
    stack.pop()
    assert len(stack) == 0


def test_clear():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.clear()
    assert stack.is_empty()


def test_contains():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.contains(1)
    assert stack.contains(2)
    assert stack.contains(3)
    assert not stack.contains(4)


def test_reverse():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.reverse()
    assert stack.pop() == 1
    assert stack.pop() == 2
    assert stack.pop() == 3
    assert stack.is_empty()


def test_clone():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    cloned_stack = stack.clone()
    assert cloned_stack.pop() == 3
    assert cloned_stack.pop() == 2
    assert cloned_stack.pop() == 1
    assert cloned_stack.is_empty()
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty()


def test_str_repr():
    stack = Stack()
    assert str(stack) == '[]'
    assert repr(stack) == '[]'
    stack.push(1)
    stack.push(2)
    assert str(stack) == '[1, 2]'
    assert repr(stack) == '[1, 2]'


def test_iter():
    stack = Stack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    for i, item in enumerate(stack):
        assert item == i
    # Check if the stack is still intact
    assert list(stack) == [0, 1, 2]


def test_swap():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.swap()
    assert stack.pop() == 2
    assert stack.pop() == 3
    assert stack.pop() == 1


def test_swap_empty():
    stack = Stack()
    with pytest.raises(StackException):
        stack.swap()


def test_next():
    stack = Stack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    iterator = iter(stack)
    assert next(iterator) == 0
    assert next(iterator) == 1
    assert next(iterator) == 2
    with pytest.raises(StopIteration):
        next(iterator)


def test_push_pop_dict():
    stack = Stack()
    data = {'key1': 'value1', 'key2': 'value2'}
    stack.push(data)
    assert len(stack) == 1
    assert stack.pop() == data
    assert stack.is_empty()


def test_push_pop_list():
    stack = Stack()
    data = [1, 2, 3, 4, 5]
    stack.push(data)
    assert len(stack) == 1
    assert stack.pop() == data
    assert stack.is_empty()


def test_push_pop_tuple():
    stack = Stack()
    data = (1, 2, 3)
    stack.push(data)
    assert len(stack) == 1
    assert stack.pop() == data
    assert stack.is_empty()


def test_push_pop_object():
    class TestObject:
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return self.value == other.value

    stack = Stack()
    obj = TestObject(10)
    stack.push(obj)
    assert len(stack) == 1
    assert stack.pop() == obj
    assert stack.is_empty()


def test_nested_stacks():
    stack1 = Stack()
    stack2 = Stack()
    stack1.push(1)
    stack1.push(2)
    stack2.push(stack1)
    assert len(stack2) == 1
    nested_stack = stack2.pop()
    assert len(nested_stack) == 2
    assert nested_stack.pop() == 2
    assert nested_stack.pop() == 1


def test_push_pop_large_number():
    stack = Stack()
    large_number = 10 ** 100  # A very large number
    stack.push(large_number)
    assert len(stack) == 1
    assert stack.pop() == large_number
    assert stack.is_empty()


def test_push_none():
    stack = Stack()
    stack.push(None)
    assert len(stack) == 1
    assert stack.pop() is None
    assert stack.is_empty()


def test_pop_empty_stack_multiple_times():
    stack = Stack()
    with pytest.raises(StackException):
        stack.pop()
    with pytest.raises(StackException):
        stack.pop()
    with pytest.raises(StackException):
        stack.pop()


def test_push_pop_recursive_structure():
    stack = Stack()
    recursive_list = []
    recursive_list.append(recursive_list)
    stack.push(recursive_list)
    assert len(stack) == 1
    popped_value = stack.pop()
    assert popped_value is recursive_list
    assert popped_value[0] is popped_value  # Check if it's still recursive
    assert stack.is_empty()


def test_push_pop_large_stack():
    stack = Stack()
    large_size = 100000  # A large number of elements
    for i in range(large_size):
        stack.push(i)
    assert len(stack) == large_size
    for i in range(large_size - 1, -1, -1):
        assert stack.pop() == i
    assert stack.is_empty()


def test_concurrent_modification():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack_copy = stack.dump()
    stack.push(4)
    assert stack_copy == [1, 2, 3]
    assert len(stack) == 1  # Only the new element should remain
    assert stack.pop() == 4
    assert stack.is_empty()


def test_nested_stack_operations():
    stack1 = Stack()
    stack2 = Stack()
    for i in range(5):
        stack1.push(i)
    stack2.push(stack1)
    assert len(stack2) == 1
    nested_stack = stack2.pop()
    assert isinstance(nested_stack, Stack)
    assert len(nested_stack) == 5
    for i in range(4, -1, -1):
        assert nested_stack.pop() == i


if __name__ == "__main__":
    pytest.main()
