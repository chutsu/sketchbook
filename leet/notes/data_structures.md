# Data Structures

## Array

+ Quick Inserts
+ Fast access if index is known
+ Attractive for its simplicity
- Fixed size
- Slow search
- Slow deletes
- Usually only hold one kind of data

Most efficient use of memory, used in cases where data size is fixed. Arrays
are continuous blocks of memory, good for data where the size is known, or
relatively static. Can be built at compile time, or dynamically at run-time.

**Insertion is expensive** since it can involve moving many elements around or
even using `malloc` to obtain more memory to fit the new element in.

**Look ups can be made very fast** since the array can be sorted and a binary
search algorithm applied, for instance, by using the standard C library
functions `qsort` and `bsearch`.



## List

+ Quick Inserts
+ Fast access if index is known
+ Attractive for its simplicity
+ Dynamic size
- Slow search
- Slow deletes

Lists are built dynamically, and inserting elements is cheap at the beginning,
while storage exactly fits the data. Therefore, lists are good for dynamic
small sets of data.



## Linked List

+ Quick inserts
+ Quick deletes
+ Dynamic size
+ Can grow dynamically
- Slow search

## When to use linked list over an array
### Linked lists are preferable over arrays when

- Constant-time insertions/deletions from list
- You don't know how many items will be in the list
- You don't need random access to any elements
- You want to be able to insert items in the middle of the list (such as a
  priority queue)

### Arrays are preferable when

- You need index/random access to elements
- You know the number of elements in the array ahead of time so that you can
  allocate the correct amount of memory for the array
- You need speed when iterating through all the elements in sequence. You can
  use pointer math on the array to access each element, whereas you need to
  lookup the node based on the pointer for each element in the linked list,
  which may result in page faults which may result in performance hits.
- Memory is a concern. Filled arrays take up less memory than linked lists.
  Each element in the array is just the data. Each linked list node requires
  the data as well as one (or more) pointers to the other elements in the
  linked list.



## Hash Table

+ Very fast access if key is known
+ Quick insert
- Slow deletes
- Access slow if key is not known
- Inefficient memory usage



## Heap

- Quick insert
- Quick deletes
- Access slow if key is not known
- Inefficient memory usage

A Heap is a tree where a parent node's value is larger than that of any of its
descendant nodes, additionally the lower value of the two children must be on
the left. e.g.

       100
       / \
      53  60

There are generally two types of heaps, the min-heap and max-heap, where the
min and the max are at the root of the tree. It should be noted that the tree
is only partially sorted, thus instance access is only possible to the smallest
or largest item. Inserts are fast, so its a good way to deal with incoming
events or data and always have access to the earliest/biggest. Example
applications include priority queues and schedulers.



## Binary Tree

+ Quick search
+ Quick insert
+ Quick deletes
- Delete is complex

A binary tree is made of nodes, where each node contains a "left" pointer, a
"right" pointer, and a data element. The "root" pointer points to the topmost
node in the tree. The left and right pointers recursively point to smaller
"subtrees" on either side. A null pointer represents a binary tree with no
elements.


## Difference between Binary Tree and Binary Search Tree

- Binary tree: Tree where each node has up to two leaves

        1
       / \
      2   3


- Binary search tree: Used for searching. A binary tree where the left child
  contains only nodes with values less than the parent node, and where the
  right child only contains nodes with values greater than or equal to the
  parent.

        2
       / \
      1   3

## Difference between Binary Search Tree and Heap

Heap just guarantees that elements on higher levels are greater (for max-heap)
or smaller (for min-heap) than elements on lower levels, whereas BST guarantees
order (from "left" to "right"). If you want sorted elements, go with BST.



## Red-Black Tree

+ Quick search
+ Quick insert
+ Quick deletes
- Complex to implement

A red-black tree is a data structure which is a type of self balancing binary
search tree, balance is preserved by painting each node of the tree with one of
two colors (red or black) in a way that satisfies certain properties, which
collectively constrain how unbalanced the tree can become in the worst case
.When the tree is modified, the new tree is subsequently rearranged and
repainted to restore the coloring properties. The properties are designed in
such a way that this rearranging and recoloring can be performed efficiently.

The following properties must be satisfied:

- Node is either black or red
- Root is black
- All leaves (nil) nodes are black
- Every red node must have two black child nodes
- Every path from a given node to any of its descendant leaves contains the
  same number of black nodes

**Example**
A simple example to understand balancing is, a chain of 3 nodes is not possible
in red black tree. We can try any combination of colors and see all of them
violate Red-Black tree property.

A chain of 3 nodes is nodes is not possible in Red-Black Trees.
Following are NOT Red-Black Trees

         30               30                  30
        /  \            /    \              /    \
       20  NIL         20(R)  NIL         20(R)   NIL
      /  \            /  \               /    \
     10  NIL         10  NIL          10(R)   NIL

    Violates         Violates         Violates
    Property 4.      Property 4       Property 3

Following are different possible Red-Black Trees with above 3 keys

          20                           20
        /    \                       /    \
      10      30                   10(R)   30(R)
     /  \    /  \                 /  \     /  \
    NIL NIL NIL NIL              NIL NIL  NIL NIL


From the above examples, we get some idea how Red-Black trees ensure balance.



# AVL Tree

AVL tree is another self-balancing binary search tree. It was the first such data
structure to be invented. In an AVL tree, the heights fo the two child subtrees
of any node differ by at most one; if at any time they differ by more than one,
rebalancing is done to restore this property. Look up, insertion and deletion
all take O(log n) time in both the average and worst cases, where n is the
number of nodes in the tree prior to the operation. Insertions and deletions
may require the tree to be rebalanced by one or more tree rotations.



