#/usr/bin/env python3

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
