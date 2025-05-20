# Referred from
# https://leetcode.com/problems/design-add-and-search-words-data-structure/solutions/3313633/python-simple-solution-easy-to-understand
class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            curr_node = curr_node.children.setdefault(char, Node())

        curr_node.end = True

    def search(self, word: str) -> bool:
        def dfs(node, index) -> bool:
            if index == len(word):
                return node.end
            
            if word[index] == ".":
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True

            if word[index] in node.children:
                return dfs(node.children[word[index]], index+1)

            return False

        return dfs(self.root, 0)
