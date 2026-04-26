#!/usr/bin/env python3
"""
Segment Tree
============

Segment tree is a data structure used for storing information about intervals
or segments. It allows querying which of the stored segments contain a given
point. Segment trees can be used to solve:

- Range min / max
- Sum queries
- Range update queries

Segment trees only has three operations:

- Building the tree
- Updating the tree
- Querying the tree

In a segment tree, the array is stored at the leaves of the tree, while the
internal nodes store information about the segments represented by its children.
The internal nodes are formed in a bottom-up manner by merging the information
from its children nodes.


Why is 1-index preferred in Segment trees?
------------------------------------------

= The trick: children via bit shifts

When you store a segment tree in an array with the root at index 1:

```
left child  of node i  =  2*i      (i << 1)
right child of node i  =  2*i + 1  (i << 1 | 1)
parent      of node i  =  i // 2   (i >> 1)
```

These are just bit operations — extremely fast, and dead simple to remember.

= Why 0-index breaks this

If you put the root at index 0:

```
left child  of node i  =  2*i + 1
right child of node i  =  2*i + 2
parent      of node i  =  (i - 1) // 2
```

It still works, but you lose the elegance. The parent formula is messier, and
you can't use the clean i >> 1 shift anymore.

= Visualizing the 1-indexed layout

```
Index:         1
            /     \
           2       3
          / \     / \
         4   5   6   7
```

Notice the pattern — all nodes at the same depth are contiguous, and the index
literally encodes the path from root to node in binary:

```
node 6  =  110 in binary
            │└─ went right at depth 2
            └── went left  at depth 1
```

This binary encoding of the path is a deeper reason the math works out so
cleanly — each bit tells you which branch was taken.

= Bottom line

0-indexed trees work fine and some implementations use them. But 1-indexed
trees let you navigate with i*2, i*2+1, and i/2, which are branchless,
cache-friendly, and trivially memorable. It's a case where a small convention
pays off everywhere else in the code.

"""
import time
import random


class SegmentTree:
  def __init__(self, arr):
    self.n = len(arr)
    self.tree = [0] * self.n + arr
    for i in range(self.n - 1, 0, -1):
      self.tree[i] = self.tree[2 * i + 0] + self.tree[2 * i + 1]

  def update(self, i, value):
    i += self.n
    self.tree[i] = value

    while i > 1:
      i //= 2
      self.tree[i] = self.tree[2 * i + 0] + self.tree[2 * i + 1]

  def query(self, l, r):
    result = 0
    l += self.n
    r += self.n

    while l < r:
      if l % 2 == 1: # l is right child, include it and move right
        result += self.tree[l]
        l += 1
      if r % 2 == 1: # r is right child, include its left sibling
        r -= 1
        result += self.tree[r]
      l //= 2
      r //= 2

    return result


if __name__ == "__main__":
  arr = [1, 3, 5, 7, 9, 11]

  stree = SegmentTree(arr)
  print(stree.query(0, 6))

  n = len(arr)
  for start in range(n):
    for end in range(n):
      assert stree.query(start, end) == sum(arr[start:end])
