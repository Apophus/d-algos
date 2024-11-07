class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        
    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True
        
class Solution:
    def findWords(self, board, words):
        
        root = TrieNode()
        for w in words:
            root.add_word(w)
            
        rows, columns = len(board), len(board[0])
        res, visited = set(), set()
        
        def dfs(r,c, node, word):
            if(r<0 or c<0 
               or r>=rows or c>=columns 
               or (r,c)in visited
               or board[r][c] not in node.children):
                return
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end_of_word:
                res.add(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visited.remove((r,c))
            
        for r in range(rows):
            for c in range(columns):
                dfs(r,c, root, "")
            
        return list(res)