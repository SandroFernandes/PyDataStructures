import pytest
from double_linked_list import DoubleLinkedList

@pytest.fixture
def empty_list():
    return DoubleLinkedList()

@pytest.fixture
def populated_list():
    dll = DoubleLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    return dll

def test_insert_at_beginning(empty_list):
    empty_list.insert_at_beginning(1)
    assert empty_list.head.data == 1
    assert empty_list.tail.data == 1

def test_insert_at_end(empty_list):
    empty_list.insert_at_end(1)
    assert empty_list.head.data == 1
    assert empty_list.tail.data == 1

def test_insert_multiple_elements(empty_list):
    empty_list.insert_at_beginning(2)
    empty_list.insert_at_beginning(1)
    empty_list.insert_at_end(3)
    assert empty_list.head.data == 1
    assert empty_list.tail.data == 3

def test_delete_node(populated_list):
    populated_list.delete_node(2)
    assert populated_list.head.next.data == 3

def test_delete_head(populated_list):
    populated_list.delete_node(1)
    assert populated_list.head.data == 2

def test_delete_tail(populated_list):
    populated_list.delete_node(3)
    assert populated_list.tail.data == 2

def test_display_forward(populated_list, capsys):
    populated_list.display_forward()
    captured = capsys.readouterr()
    assert captured.out.strip() == "1 <-> 2 <-> 3 <-> None"

def test_display_backward(populated_list, capsys):
    populated_list.display_backward()
    captured = capsys.readouterr()
    assert captured.out.strip() == "3 <-> 2 <-> 1 <-> None"

def test_empty_list_operations(empty_list):
    empty_list.delete_node(1)  # Should not raise an error
    empty_list.display_forward()  # Should not raise an error
    empty_list.display_backward()  # Should not raise an error
