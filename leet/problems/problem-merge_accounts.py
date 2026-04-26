#!/usr/bin/env python3
from collections import defaultdict
import pprint


def dfs(i, emails, email_map, accounts, visited):
  if visited[i]:
    return

  visited[i] = True
  for j in range(1, len(accounts[i])):
    email = accounts[i][j]
    emails.add(email)

    for neighbor in email_map[email]:
      dfs(neighbor, emails, email_map, accounts, visited)


def accounts_merge(accounts):
  # Build email map
  email_map = defaultdict(list)
  for i, account in enumerate(accounts):
    for j in range(1, len(account)):
      email = account[j]
      email_map[email].append(i)

  # Traverse accounts (DFS)
  result = []
  visited = [False] * len(accounts)
  for i, account in enumerate(accounts):
    if visited[i]:
      continue

    name = account[0]
    emails = set()
    dfs(i, emails, email_map, accounts, visited)
    result.append([name] + sorted(emails))

  return result


# accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
#             ["John", "johnsmith@mail.com", "john00@mail.com"],
#             ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]

accounts = [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]

pprint.pprint(accounts_merge(accounts))
