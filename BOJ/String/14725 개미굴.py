N = int(input())

class Node:
    def __init__(self, data, depth):
        self.data = data
        self.depth = depth
        self.children = dict()

class Trie:
    def __init__(self):
        self.head = Node("", -1)

    def insert(self, foods):
        cur = self.head
        depth = -1

        for food in foods:
            depth += 1
            if food not in cur.children:
                cur.children[food] = Node(food, depth)
            cur = cur.children[food]    
    
    def read(self, node):
        if (node.depth >= 0):       
            print("--"*(node.depth), end="")
            print(node.data)
        keys = sorted(node.children.keys())
        for child in keys:
            self.read(node.children[child])

trie = Trie()
for _ in range(N):
    K, *foods = input().split()
    trie.insert(foods)

trie.read(trie.head)
