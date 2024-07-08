#!/usr/bin/env python3

# Append to end of array
arr = [None] * 6
for i in range(len(arr)):
  arr[i] = i
print(arr)

# Prepend at the start of array
arr = [i for i in range(6)]
# -- Create space for new element
arr.append(None)
# -- Shift everything to the right by one
for i in range(len(arr) - 1, 0, -1):
  arr[i] = arr[i - 1]
# -- Prepend new value
arr[0] = 99
print(arr)

# Insert anywhere
insert_idx = 3
insert_val = 8
arr = [i for i in range(6)]
# -- Create space for new element
arr.append(None)
# -- Shift
for i in range(len(arr) - 1, insert_idx, -1):
  arr[i] = arr[i - 1]
# -- Insert
arr[insert_idx] = insert_val
print(arr)
