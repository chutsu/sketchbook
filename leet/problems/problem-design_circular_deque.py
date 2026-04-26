#!/usr/bin/env python3
"""
LeetCode 641: Design Circular Deque

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

    MyCircularDeque(int k)
      Initializes the deque with a maximum size of k.

    boolean insertFront()
      Adds an item at the front of Deque. Returns true if the operation is
      successful, or false otherwise.

    boolean insertLast()
      Adds an item at the rear of Deque. Returns true if the operation is
      successful, or false otherwise.

    boolean deleteFront()
      Deletes an item from the front of Deque. Returns true if the operation is
      successful, or false otherwise.

    boolean deleteLast()
      Deletes an item from the rear of Deque. Returns true if the operation is
      successful, or false otherwise.

    int getFront()
      Returns the front item from the Deque. Returns -1 if the deque is empty.

    int getRear()
      Returns the last item from Deque. Returns -1 if the deque is empty.

    boolean isEmpty()
      Returns true if the deque is empty, or false otherwise.

    boolean isFull()
      Returns true if the deque is full, or false otherwise.

-------------------------------------------------------------------------------

Example:

  MyCircularDeque myCircularDeque = new MyCircularDeque(3);
  myCircularDeque.insertLast(1);  // return True
  myCircularDeque.insertLast(2);  // return True
  myCircularDeque.insertFront(3); // return True
  myCircularDeque.insertFront(4); // return False, the queue is full.
  myCircularDeque.getRear();      // return 2
  myCircularDeque.isFull();       // return True
  myCircularDeque.deleteLast();   // return True
  myCircularDeque.insertFront(4); // return True
  myCircularDeque.getFront();     // return 4

"""


class MyCircularDeque:
  def __init__(self, k):
    self.data = [-1 for _ in range(k + 1)]
    self.capacity = k + 1
    self.head = 0
    self.tail = 1

  def _next(self, index):
    return (index + 1) % self.capacity

  def _prev(self, index):
    return (index - 1) % self.capacity

  def isfull(self):
    return self.head == self.tail

  def isempty(self):
    return self._next(self.head) == self.tail

  def front(self):
    if self.isempty():
      return -1
    return self.data[self._next(self.head)]

  def rear(self):
    if self.isempty():
      return -1
    return self.data[self._prev(self.tail)]

  def insert_front(self, val):
    if self.isfull():
      return False
    self.data[self.head] = val
    self.head = self._prev(self.head)
    return True

  def insert_last(self, val):
    if self.isfull():
      return False
    self.data[self.tail] = val
    self.tail = self._next(self.tail)
    return True

  def delete_front(self):
    if self.isempty():
      return False
    self.data[self.head] = -1
    self.head = self._next(self.head)
    return True

  def delete_last(self):
    if self.isempty():
      return False
    self.data[self.tail] = -1
    self.tail = self._prev(self.tail)
    return True

  def print(self):
    print(self.data)
    print(f"head: {self.head}, tail: {self.tail}")
    print(f"front: {self.front()}, rear: {self.rear()}")


if __name__ == "__main__":
  deque = MyCircularDeque(3)
  assert deque.insert_last(1) is True
  assert deque.insert_last(2) is True
  assert deque.insert_front(3) is True
  assert deque.insert_front(4) is False
  assert deque.rear() == 2
  assert deque.front() == 3
  assert deque.isfull() is True
  assert deque.delete_last() is True
  assert deque.insert_front(4) is True
  assert deque.front() == 4
  deque.print()
