#!/usr/bin/env python3
"""
A circular buffer (ring buffer) is a fixed-size buffer that wraps around - when
you reach the end, you loop back to the start.

Core Idea
---------

Use an array with two pointers, head and tail:

- tail is where you write next
- head is where you read next
- Both wrap around using modulo

```
tail = (tail + 1) % capacity
head = (head + 1) % capacity
```


Tracing Through
---------------

Capacity = 4:

```
write(a): buffer=[a,_,_,_]  head=0, tail=1
write(b): buffer=[a,b,_,_]  head=0, tail=2
write(c): buffer=[a,b,c,_]  head=0, tail=3
read():   buffer=[_,b,c,_]  head=1, tail=3  → returns a
write(d): buffer=[_,b,c,d]  head=1, tail=0  ← tail wrapped!
write(e): buffer=[e,b,c,d]  head=1, tail=1  ← wrote to front
read():   returns b, head=2
```

## Why Track `size` Separately?

Without `size`, you cannot distinguish between full and empty — both states
have `head == tail`:

```
empty: head=2, tail=2
full:  head=2, tail=2  <- ambiguous!
```

"""

class CircularBuffer:
  def __init__(self, capacity):
    self.buffer = [None] * capacity
    self.capacity = capacity
    self.head = 0  # read pointer
    self.tail = 0  # write pointer
    self.size = 0

  def write(self, val):
    if self.size == self.capacity:
      raise Exception("Buffer full")
    self.buffer[self.tail] = val
    self.tail = (self.tail + 1) % self.capacity
    self.size += 1

  def read(self):
    if self.size == 0:
      raise Exception("Buffer empty")
    val = self.buffer[self.head]
    self.head = (self.head + 1) % self.capacity
    self.size -= 1
    return val

  def is_full(self):
    return self.size == self.capacity

  def is_empty(self):
    return self.size == 0
