"""

"""
class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = None




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


        def insert(word):
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word #end of word, stores word itself


        for w in words: #create Trie
            insert(w)

        res = set()

        def search(r, c, node, seen):
          
            char = board[r][c] #easier to work with char
            if char not in node.children: #if the character that we believe is next character no exist, then return
                return
            if node.children[char].word:
                res.add(node.children[char].word)
            seen.add((r, c))
            for dr, dc in directions: #xplore every direction from this letter
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0]) or (nr, nc) in seen:
                    continue
                search(nr, nc, node.children[char], seen)

            seen.remove((r, c)) #I have to backtrack.

        for i in range(len(board)):
            for j in range(len(board[0])):
                seen = set()
                search(i, j, root, seen)
            
        return list(res)
            

        

