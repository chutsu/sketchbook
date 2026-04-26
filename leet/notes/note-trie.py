#/usr/bin/env python3
"""
A prefix tree (trie) is a tree-based data structure used to efficiently store
and retrieve strings by breaking them into characters and sharing common
prefixes. Each node represents a single character, and paths from the root to a
node spell out prefixes or full words; typically, nodes also store a flag
indicating whether a complete word ends there.

To insert a word, you traverse (or create) nodes for each character in
sequence, and to search, you follow the same path, checking the end-of-word
marker if needed.

This structure allows fast operations—O(L) time for insert and lookup, where L
is the length of the word—making tries especially useful for tasks like
autocomplete, spell checking, and dictionary lookups.
"""

class TrieNode:
  def __init__(self, is_word=False):
    self.is_word = is_word
    self.children = {}


class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    node = self.root
    for c in word:
      if c not in node.children:
        node.children[c] = TrieNode()
      node = node.children[c]
    node.is_word = True

  def search(self, word):
    node = self.root
    for c in word:
      if c not in node.children:
        return False
      node = node.children[c]
    return node.is_word

  def starts_with(self, word):
    node = self.root
    for c in word:
      if c not in node.children:
        return False
      node = node.children[c]
    return True


if __name__ == "__main__":
  trie = Trie()
  trie.insert("apple")
  trie.insert("app")
  print(trie.search("apple"))
  print(trie.search("ap"))
  print(trie.starts_with("ap"))
