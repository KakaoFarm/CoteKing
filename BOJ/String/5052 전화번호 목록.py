class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, string):
        cur_node = self.root
        for char in string:
            if char not in cur_node:
                cur_node[char] = {}
            cur_node = cur_node[char]
            if "*" in cur_node:
                return False
        cur_node["*"] = True
        if len(cur_node) > 1:
            return False
        return True
    
T = int(input())
for _ in range(T):
    book = Trie()
    N = int(input())
    answer = "YES"
    for _ in range(N):
        if not book.insert(input()):
            answer = "NO"
    print(answer)
