class TrieNode():
    def __init__(self): 

        self.children = {}
        self.end_of_word = False


    
    
    
    

        

    

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None: #insert
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_of_word = True
        
    def search(self, word: str) -> bool: #needs to be a recursive function that splits into multiple searches at a .
        def dfs(node, word, index):
            if index >= len(word):
                return node.end_of_word
            c = word[index]
            if c == ".":
                for child in node.children:
                    return any(dfs(child, word, index + 1) for child in node.children.values())
            if c not in node.children:
                return False
            return dfs(node.children[c], word, index + 1)
        return dfs(self.root, word, 0)





        

    
