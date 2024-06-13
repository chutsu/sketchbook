## Stable Sort

A stable sort means that the implementation preserves the input order of equal
elements in the sorted output.


## Quick Sort

- Not stable
- Time complexity: Best: O(n log n) Worst: O(n^2)
- Space complexity: Best: O(log n)

**Algorithm**

    # choose pivot
    swap a[1, rand(1,n)]

    # 2-way partition
    k = 1
    for i = 2:n, if a[i] < a[1], swap a[++k, i]
    swap a[1,k]
    invariant: a[1 .. k - 1] < a[k] <= a[k + 1 .. n]

    # recursive sorts
    sort a[1 .. k-1]
    sort a[k + 1, n]

**Procedure**

1. Pick a "pivot point". Picking a good pivot point can greatly affect the
   running time.
2. Break the list into two lists: those elements less than the pivot
   element, and those elements greater than the pivot element.
3. Recursively sort each of the smaller lists.
4. Make one big list: the 'smallers' list, the pivot points, and the
   'biggers' list.

Picking a random pivot point will not eliminate the O(n^2) worst-case time, but
it will usually transform the worst case into a less frequently occurring
permutation. In practice, the sorted list usually comes up more often than any
other permutation, so this improvement is often used.

Quick sort with in-place and unstable partitioning uses only constant additional
space before making any recursive call. Quick sort must store a constant amount
of information for each nested recursive call. Since the best case makes at
most O(log n) nested recursive calls, it uses O(log n) space. However, without
Sedgewick's trick to limit the recursive calls, in the worst case quick sort
could make O(n) nested recursive calls and need O(n) auxiliary space.

Practically speaking, O(log n) memory is nothing. For instance, if you were
to sort 1 billion ints, storing them would require 4 GB, but the stack
would only require about 30 stack frames, at something like 40 bytes, so
about 1200 Bytes in total.

Quick sort is typically faster than merge sort when the data is stored in
memory. However, when the data set is huge and is stored on external devices
such as a hard drive, merge sort is the clear winner in terms of speed. It
minimizes the expensive reads of the external drive and also lends itself well
to parallel computing.



## Merge Sort

- Stable
- Space complexity: Arrays: O(n) Linked-List: O(log n)
- Time complexity: O(n log n)

**Algorithm**

    # split in half
    m = n / 2

    # recursive sorts
    sort a[1..m]
    sort a[m+1..n]

    # merge sorted sub-arrays using temp array
    b = copy of a[1..m]
    i = 1, j = m+1, k = 1
    while i <= m and j <= n,
        a[k++] = (a[j] < b[i]) ? a[j++] : b[i++]
        invariant: a[1..k] in final position

    while i <= m,
        a[k++] = b[i++]
        invariant: a[1..k] in final position

Given two separate lists A and B, construct a list C by repeatedly comparing
the least value of A to the least value of B, removing the lesser value, and
appending it onto C. When one list is exhausted, append the remaining items in
the other list onto C in order.  The list C is then also a sorted list.

If you work this out by hand a few times, you'll see that it's correct. For
example:

    A = 1, 3
    B = 2, 4
    C = min(min(A), min(B)) = 1

    A = 3
    B = 2, 4
    C = 1 min(min(A), min(B)) = 2

    A = 3
    B = 4
    C = 1, 2 min(min(A), min(B)) = 3

    A =
    B = 4
    C = 1, 2, 3

Now A is exhausted, so extend C with the remaining values from B:

    C = 1, 2, 3, 4


## Why is Quicksort better than Mergesort most of the time?

Quicksort has O(n^2) worst-case runtime and O(n log n) average case runtime.
However, it’s superior to merge sort in many scenarios because many factors
influence an algorithm's runtime, and, when taking them all together, quicksort
wins out. Quicksort has O(n^2) worst-case runtime and O(n log n) average case
runtime.  However, it's superior to merge sort in many scenarios because many
factors influence an algorithm's runtime, and, when taking them all together,
quick sort wins out.

In particular, the often-quoted runtime of sorting algorithms refers to the
number of comparisons or the number of swaps necessary to perform to sort the
data. This is indeed a good measure of performance, especially since it's
independent of the underlying hardware design. However, other things – such as
locality of reference (i.e. do we read lots of elements which are probably in
cache?) – also play an important role on current hardware. Quicksort in
particular requires little additional space and exhibits good cache locality,
and this makes it faster than merge sort in many cases.

In addition, it's very easy to avoid quicksort's worst-case run time of O(n^2)
almost entirely by using an appropriate choice of the pivot – such as picking
it at random (this is an excellent strategy).

In practice, many modern implementations of quicksort (in particular
libstdc++'s std::sort) are actually introsort, whose theoretical worst-case is
O(n log n), same as merge sort. It achieves this by limiting the recursion
depth, and switching to a different algorithm (heapsort) once it exceeds log n.



## Insertion Sort

- Stable
- Time complexity: O(n^2) comparisons and swaps
- Space complexity: O(1) extra space
- Adaptive: O(n) time when nearly sorted
- Very low overhead

**Procedure**

    1. Iterate through the array, starting from the second element:

        1. Note the element at this index.
        2. Walk back through the previous elements until you find a smaller
           element (or the beginning of the array), moving each element up by
           one.
        3. Insert the noted element at this point.

**Algorithm**

    for i from 1 to N
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key
            a[j+1] = a[j]
            j = j - 1

        a[j+1] = key


Although it is one of the elementary sorting algorithms with O(n^2) worst-case
time, insertion sort is the algorithm of choice either when the data is nearly
sorted (because it is adaptive) or when the problem size is small (because it
has low overhead).

For these reasons, and because it is also stable, insertion sort is often used
as the recursive base case (when the problem size is small) for higher overhead
divide-and-conquer sorting algorithms, such as merge sort or quick sort.



## Selection Sort

- Not Stable
- Space complexity: O(1) extra space
- Time complexity: O(n^2)
- Not Adaptive

**Procedure**

    1. At each iteration find the smallest entry (the "key") in the unsorted
       portion of the array.
    2. Swap the "key" with the i-th entry

**Algorithm**

    func selection_sort(list)
        max = length(list) - 1

        for i from 0 to max
            key = list[i]
            keyj = i

            for j from i+1 to max
                if list[j] < key
                    key = list[j]
                    keyj = j

            list[keyj] = list[i]
            list[i] = key

        return list
    end func


From the comparisons presented here, one might conclude that selection should
never be used. It does not adapt to the data in any way, so its runtime is
always quadratic.

However, selection sort has the property of minimizing the number of swaps. In
applications where the cost of swapping items is high, selection sort very well
may be the algorithm of choice.



## Bubble Sort

- Stable
- Space complexity: O(1) extra space
- Time complexity: O(n^2) comparisons and swaps
- Adaptive: O(n) when nearly sorted

**Algorithm**

    func bubblesort(var a as array)
        for i from 1 to N
            for j from 0 to N - 1
            if a[j] > a[j + 1]
                swap(a[j], a[j + 1])
    end func

At each step, if two adjacent elements of a list are not in order, they will be
swapped. Thus, smaller elements will "bubble" to the front, (or bigger elements
will be "bubbled" to the back, depending on implementation) and hence the name

Bubble sort has many of the same properties as insertion sort, but has slightly
higher overhead. In the case of nearly sorted data, bubble sort takes O(n)
time, but requires at least 2 passes through the data, whereas insertion sort
requires something more like 1 pass).



## Heap Sort

- Not stable
- Space complexity: O(1) extra space
- Time complexity: O(n log n)
- Not really adaptive

**Algorithm**

    Heapify(A as array, i as int)
        left = 2i
        right = 2i+1

        # check if left is bigger than parent
        if (left <= n) and (A[left] > A[i])
            max = left
        else
            max = i

        # check if right is bigger than parent
        if (right<=n) and (A[right] > A[max])
            max = right

        # swap parent with new max
        if (max != i)
            swap(A[i], A[max])
            Heapify(A, max)

    BuildHeap(A as array)
        n = elements_in(A)
        for i = floor(n/2) to 1
            Heapify(A,i)

    Heapsort(A as array)
        BuildHeap(A)
        for i = n to 1
            swap(A[1], A[i])
            n = n - 1
            Heapify(A, 1)


**Procedure**

    1. Build a heap with the sorting array, using recursive insertion
    2. Iterate to extract n times the maximum or minimum element in heap and
       heapify the heap.
    3. The extracted elements from a sorted subsequence.

Heap sort is simple to implement, performs an O(n log n) in-place sort, but is
not stable. It can be thought of as an improved selection sort: like that
algorithm, it divides its input into a sorted and an unsorted region, and it
iteratively shrinks the unsorted region by extracting the smallest element and
moving that to the sorted region. The improvement consists of the use of a heap
data structure rather than a linear-time search to find the minimum.

Although somewhat slower in practice on most machines than a well-implemented
quicksort, it has the advantage of a more favorable worst-case O(n log n)
runtime.  Heapsort is an in-place algorithm, but it is not a stable sort.


## Summary

**Quick sort**: When you don't need a stable sort and average case performance
matters more than worst case performance. A quick sort is O(n log n) on
average, O(n^2) in the worst case. A good implementation uses O(log n)
auxiliary storage in the form of stack space for recursion.

**Merge sort**: When you need a stable, O(n log n) sort, this is about your
only option. The only downsides to it are that it uses O(n) auxiliary space and
has a slightly larger constant than a quick sort. There are some in-place merge
sorts, but AFAIK they are all either not stable or worse than O(n log n). Even
the O(n log n) in place sorts have so much larger a constant than the plain old
merge sort that they're more theoretical curiosities than useful algorithms.

**Heap sort**: When you don't need a stable sort and you care more about worst
case performance than average case performance. It's guaranteed to be O(n log
n), and uses O(1) auxiliary space, meaning that you won't unexpectedly run out
of heap or stack space on very large inputs.

**Introsort**: This is a quick sort that switches to a heap sort after a
certain recursion depth to get around quick sort's O(n^2) worst case. It's
almost always better than a plain old quick sort, since you get the average
case of a quick sort, with guaranteed O(n log n) performance. Probably the only
reason to use a heap sort instead of this is in severely memory constrained
systems where O(log n) stack space is practically significant.

**Insertion sort**: When n is guaranteed to be small, including as the base
case of a quick sort or merge sort. While this is O(n^2), it has a very small
constant and is a stable sort.

**Bubble sort, selection sort**: When you're doing something quick and dirty
and for some reason you can't just use the standard library's sorting
algorithm. The only advantage these have over insertion sort is being slightly
easier to implement.

**non-comparison sorts**: Under some fairly limited conditions it's possible to
break the O(n log n) barrier and sort in O(n). Here are some cases where that's
worth a try:

**Counting sort**: When you are sorting integers with a limited range.

**Radix sort**: When log(n) is significantly larger than K, where K is the
number of radix digits.

**Bucket sort**: When you can guarantee that your input is approximately
uniformly distributed.
