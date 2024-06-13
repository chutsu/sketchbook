#!/usr/bin/env python3
"""
LeetCode 622: Design Ciruclar Queue

Design your implementation of the circular queue. The circular queue is a
linear data structure in which the operations are performed based on FIFO
(First In First Out) principle, and the last position is connected back to the
first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces
in front of the queue. In a normal queue, once the queue becomes full, we
cannot insert the next element even if there is a space in front of the queue.
But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

    MyCircularQueue(k)
      Initializes the object with the size of the queue to be k.

    int Front()
      Gets the front item from the queue. If the queue is empty, return -1.

    int Rear()
      Gets the last item from the queue. If the queue is empty, return -1.

    boolean enQueue(int value)
      Inserts an element into the circular queue. Return true if the operation
      is successful.

    boolean deQueue()
      Deletes an element from the circular queue. Return true if the operation
      is successful.

    boolean isEmpty()
      Checks whether the circular queue is empty or not.

    boolean isFull()
      Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in
your programming language.


-------------------------------------------------------------------------------

Example:

  MyCircularQueue myCircularQueue = new MyCircularQueue(3);
  myCircularQueue.enQueue(1); // return True
  myCircularQueue.enQueue(2); // return True
  myCircularQueue.enQueue(3); // return True
  myCircularQueue.enQueue(4); // return False
  myCircularQueue.Rear();     // return 3
  myCircularQueue.isFull();   // return True
  myCircularQueue.deQueue();  // return True
  myCircularQueue.enQueue(4); // return True
  myCircularQueue.Rear();     // return 4

"""


class MyCircularQueue:
  def __init__(self, k):
    self.data = [-1] * k
    self.capacity = k
    self.size = 0
    self.head = 0

  def isfull(self):
    return self.size == self.capacity

  def isempty(self):
    return self.size == 0

  def front(self):
    if self.isempty():
      return -1
    return self.data[self.head]

  def rear(self):
    if self.isempty():
      return -1
    return self.data[(self.head + self.size - 1) % self.capacity]

  def enqueue(self, val):
    if self.isfull():
      return False
    self.data[(self.head + self.size) % self.capacity] = val
    self.size += 1
    return True

  def dequeue(self):
    if self.isempty():
      return False
    self.data[self.head] = -1
    self.head = (self.head + 1) % self.capacity
    self.size -= 1
    return True

  def print(self):
    print(self.data)
    print(f"head: {self.head}, size: {self.size}")
    print(f"front: {self.front()}, rear: {self.rear()}")


if __name__ == "__main__":
  queue = MyCircularQueue(3)
  assert queue.enqueue(1) is True
  assert queue.enqueue(2) is True
  assert queue.enqueue(3) is True
  assert queue.enqueue(4) is False
  assert queue.front() == 1
  assert queue.rear() == 3
  assert queue.isfull() is True
  assert queue.dequeue() is True
  assert queue.enqueue(4) is True
  assert queue.rear() == 4
  queue.print()
