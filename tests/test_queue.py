import pytest
from queue import Queue


def test_is_empty():
    q = Queue()
    assert q.is_empty() == True
    q.enqueue(1)
    assert q.is_empty() == False


def test_enqueue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert str(q) == '[1, 2]'


def test_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert str(q) == '[2]'
    with pytest.raises(IndexError):
        empty_q = Queue()
        empty_q.dequeue()


def test_peek():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.peek() == 1
    q.dequeue()
    assert q.peek() == 2
    with pytest.raises(IndexError):
        empty_q = Queue()
        empty_q.peek()


def test_size():
    q = Queue()
    assert q.size() == 0
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2


def test_str():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert str(q) == '[1, 2]'


def test_iter():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    iter_q = iter(q)
    assert next(iter_q) == 1
    assert next(iter_q) == 2
    with pytest.raises(StopIteration):
        next(iter_q)


def test_next():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.next() == 1
    assert str(q) == '[2]'
    with pytest.raises(IndexError):
        empty_q = Queue()
        empty_q.next()


if __name__ == "__main__":
    pytest.main()
