import pytest
from src.singly_linked_list import SinglyLinkedList, Node


def test_node_initialization():
    node = Node(10)
    assert node.data == 10
    assert node.next is None


def test_node_default_initialization():
    node = Node()
    assert node.data is None
    assert node.next is None


def test_node_repr():
    node = Node(10)
    assert repr(node) == "10"


def test_append():
    sll = SinglyLinkedList()
    assert sll.append(1) == "1 → None"
    sll.append(2)
    assert sll.append(3) == "1 → 2 → 3 → None"


def test_prepend():
    sll = SinglyLinkedList()
    assert sll.prepend(1) == "1 → None"
    sll.prepend(2)
    assert sll.prepend(3) == "3 → 2 → 1 → None"


def test_delete_with_value():
    sll = SinglyLinkedList()
    # Testing deletion from an empty list
    sll.delete_with_value(1)
    assert sll is None
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)

    assert sll.delete_with_value(2) == "1 → 3 → None"
    assert sll.delete_with_value(1) == "3 → None"
    assert sll.delete_with_value(3) is None
    # Testing deletion of a non-existent value
    assert sll.delete_with_value(4) is None


def test_find():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    # found
    assert sll.find(2)
    # not found
    assert not sll.find(4)


def test_reverse():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.reverse()
    assert str(sll) == "3 → 2 → 1 → None"


def test_sort_ascending():
    sll = SinglyLinkedList()
    sll.append(3)
    sll.append(1)
    sll.append(2)
    sll.sort(order="ascending")
    assert str(sll) == "1 → 2 → 3 → None"


def test_sort_descending():
    sll = SinglyLinkedList()
    sll.append(3)
    sll.append(1)
    sll.append(2)
    sll.sort(order="descending")
    assert str(sll) == "3 → 2 → 1 → None"


def test_sort_empty_list():
    sll = SinglyLinkedList()
    sll.sort(order="ascending")
    assert str(sll) == "None"


def test_sort_invalid_order():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    with pytest.raises(ValueError) as excinfo:
        sll.sort(order="invalid")
    assert str(excinfo.value) == "Invalid order value. Use 'ascending' or 'descending'."


@pytest.mark.parametrize("data_type", [
    (1, 2, 3),  # integers
    ("a", "b", "c"),  # strings
    (1.1, 2.2, 3.3),  # floats
    ((1, 2), (3, 4), (5, 6)),  # tuples
])
def test_append(data_type):
    sll = SinglyLinkedList()
    for data in data_type:
        sll.append(data)
    assert str(sll) == " → ".join(map(str, data_type)) + " → None"


@pytest.mark.parametrize("data_type", [
    (1, 2, 3),  # integers
    ("a", "b", "c"),  # strings
    (1.1, 2.2, 3.3),  # floats
    ((1, 2), (3, 4), (5, 6)),  # tuples
])
def test_prepend(data_type):
    sll = SinglyLinkedList()
    for data in data_type:
        sll.prepend(data)
    assert str(sll) == " → ".join(map(str, reversed(data_type))) + " → None"


def test_insert_after_data():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.insert_after_data(2, 4)
    assert str(sll) == "1 → 2 → 4 → 3 → None"


def test_insert_after_data_not_found():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.insert_after_data(5, 4)
    assert str(sll) == "1 → 2 → 3 → None"


def test_insert_after_data_empty():
    sll = SinglyLinkedList()
    sll.insert_after_data(5, 4)
    assert str(sll) == "None"


def test_insert_after_data_head():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.insert_after_data(1, 2)
    assert str(sll) == "1 → 2 → None"


def test_insert_before_data():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.insert_before_data(2, 4)
    assert str(sll) == "1 → 4 → 2 → 3 → None"


def test_insert_before_data_not_found():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.insert_before_data(5, 4)
    assert str(sll) == "1 → 2 → 3 → None"


def test_insert_before_data_empty():
    sll = SinglyLinkedList()
    sll.insert_before_data(5, 4)
    assert str(sll) == "None"


def test_insert_before_data_head():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.insert_before_data(1, 2)
    assert str(sll) == "2 → 1 → None"


@pytest.mark.parametrize("data_type", [
    (1, 2, 3),  # integers
    ("a", "b", "c"),  # strings
    (1.1, 2.2, 3.3),  # floats
    ((1, 2), (3, 4), (5, 6)),  # tuples
])
def test_delete_with_value(data_type):
    sll = SinglyLinkedList()
    for data in data_type:
        sll.append(data)
    sll.delete_with_value(data_type[1])
    expected_list = [data_type[0], data_type[2]]
    assert str(sll) == " → ".join(map(str, expected_list)) + " → None"


def test_delete_empty():
    sll = SinglyLinkedList()
    assert sll.delete_with_value(1) is None


def test_delete_head():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.delete_with_value(1)
    assert sll.delete_with_value(1) is None


def test_delete_item():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    assert sll.delete_with_value(4) is None


@pytest.mark.parametrize("data_type", [
    (1, 2, 3),  # integers
    ("a", "b", "c"),  # strings
    (1.1, 2.2, 3.3),  # floats
    ((1, 2), (3, 4), (5, 6)),  # tuples
])
def test_find(data_type):
    sll = SinglyLinkedList()
    for data in data_type:
        sll.append(data)
    # found
    assert sll.find(data_type[1])
    # not found
    assert not sll.find("not_in_list")


@pytest.mark.parametrize("data_type", [
    (1, 2, 3),  # integers
    ("a", "b", "c"),  # strings
    (1.1, 2.2, 3.3),  # floats
    ((1, 2), (3, 4), (5, 6)),  # tuples
])
def test_reverse(data_type):
    sll = SinglyLinkedList()
    for data in data_type:
        sll.append(data)
    sll.reverse()
    assert str(sll) == " → ".join(map(str, reversed(data_type))) + " → None"


@pytest.mark.parametrize("data_type, sorted_ascending, sorted_descending", [
    ([3, 1, 2], [1, 2, 3], [3, 2, 1]),  # integers
    (["c", "a", "b"], ["a", "b", "c"], ["c", "b", "a"]),  # strings
    ([3.3, 1.1, 2.2], [1.1, 2.2, 3.3], [3.3, 2.2, 1.1]),  # floats
    ([(3, 4), (1, 2), (5, 6)], [(1, 2), (3, 4), (5, 6)], [(5, 6), (3, 4), (1, 2)]),  # tuples
])
def test_sort(data_type, sorted_ascending, sorted_descending):
    sll = SinglyLinkedList()
    for data in data_type:
        sll.append(data)
    sll.sort()
    assert str(sll) == " → ".join(map(str, sorted_ascending)) + " → None"
    sll.sort("descending")
    assert str(sll) == " → ".join(map(str, sorted_descending)) + " → None"


def test_len():
    sll = SinglyLinkedList()
    assert len(sll) == 0
    sll.append(1)
    assert len(sll) == 1
    sll.append("a")
    sll.append(3.3)
    assert len(sll) == 3


def test_iter():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append("a")
    sll.append(3.3)
    iter_sll = iter(sll)
    assert next(iter_sll) == 1
    assert next(iter_sll) == "a"
    assert next(iter_sll) == 3.3
    with pytest.raises(StopIteration):
        next(iter_sll)
