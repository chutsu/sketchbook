#!/usr/bin/env python3

if __name__ == "__main__":
  list1 = [1, 2, 4]
  list2 = [1, 3, 4]

  merge = []
  while True:
    if len(list1) == 0 or len(list2) == 0:
      break

    if list1[0] > list2[0]:
      merge.append(list2[0])
      list2.pop(0)

    elif list1[0] < list2[0]:
      merge.append(list1[0])
      list1.pop(0)

    elif list1[0] == list2[0]:
      merge.append(list1[0])
      list1.pop(0)

  merge += list1
  merge += list2

  print(merge)
