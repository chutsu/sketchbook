#!/usr/bin/env python3
"""
Union Find
==========

Think of Union-Find (also known as a Disjoint Set Union or DSU) as a way to
keep track of "who belongs to which group" in a room full of people. It’s a
data structure that excels at handling two specific questions very quickly:

1. Union: Can you merge these two groups into one?
2. Find: Which group does this specific person belong to?


Path Compression Example
------------------------

```
# parent array: { 1:2, 2:3, 3:4, 4:4 }
find(parent, 1)
```

The calls stack up *before* any assignments happen:

```
find(1)  -> parent[1] != 1, so calls find(2)
  find(2)  -> parent[2] != 2, so calls find(3)
    find(3)  -> parent[3] != 3, so calls find(4)
      find(4)  -> parent[4] == 4, BASE CASE, returns 4
```

Now the stack **unwinds**, and this is where compression happens:

```
    find(3): parent[3] = 4  <- 3 now points to root
             returns 4
  find(2): parent[2] = 4    <- 2 now points to root
           returns 4
find(1): parent[1] = 4      <- 1 now points to root
         returns 4
```

The key insight is that `find(parent, parent[x])` **returns the root**, so
assigning `parent[x] = find(...)` is the same as `parent[x] = root`. Every
frame on the call stack does this as it unwinds.

## Before vs. after
```
BEFORE             AFTER
1 -> 2 -> 3 -> 4   1 -> 4
                   2 -> 4
                   3 -> 4

"""

class UnionFind:
  def __init__(self, n):
    self.parents = [i for i in range(n)]
    self.rank = [1] * n

  def find(self, x):
    if self.parents[x] != x:
      self.parents[x] = self.find(self.parents[x])
    return self.parents[x]

  def union(self, x, y):
    root1 = self.find(x)
    root2 = self.find(y)

    if root1 == root2:
      return 0

    if self.rank[root1] < self.rank[root2]:
      self.parents[root1] = root2
      self.rank[root2] += self.rank[root1]
    else:
      self.parents[root2] = root1
      self.rank[root1] += self.rank[root2]

    return 1


uf = UnionFind(9)

uf.union(0, 2)
uf.union(1, 4)
uf.union(1, 5)
uf.union(2, 3)
uf.union(2, 7)
uf.union(4, 8)
uf.union(5, 8)
