# def solution(words, queries):
#     dictionary = dict()
#     count = 0 
#     for word in words:
#         front_word = ""
#         end_word = ""
#         for i in range(len(word)-1, 0, -1):
#             front_word = front_word + word[-i-1]
#             end_word = word[i] + end_word
#             try:
#                 dictionary[("?"*i+end_word)] += 1
#             except:
#                 dictionary[("?"*i+end_word)] = 1
#             try:
#                 dictionary[(front_word+"?"*i)] += 1
#             except:
#                 dictionary[(front_word+"?"*i)] = 1
#         try:
#             dictionary[("?"*len(word))] += 1
#         except:
#             dictionary[("?"*len(word))] = 1
#     answer = []
#     for query in queries:
#         try:
#             answer.append(dictionary[query])
#         except:
#             answer.append(0)
#     return answer

## 위 풀이는 시간초과로 이하 Trie구조를 통해 다시 구현해봄..

class Node(object):
    def __init__(self, key, data=None, count=0):
        self.key = key
        self.children = {}
        self.data = data
        self.count = count

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            current_node.count += 1
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]            
        current_node.data = string

    def starts_with(self, prefix):
        current_node = self.head

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return 0

        return current_node.count

def solution(words, queries):
    tries = [Trie() for _ in range(10001)]
    tries_reversed = [Trie() for _ in range(10001)]
    for word in words:
        length = len(word)
        tries[length].insert(word)
        tries_reversed[length].insert(word[::-1])

    answer = []
    for query in queries:
        length = len(query)
        if query[0] != "?":
            prefix = query.replace("?", "")
            answer.append(tries[length].starts_with(prefix))
        elif query[0] == "?":
            suffix = query.replace("?", "")[::-1]
            answer.append(tries_reversed[length].starts_with(suffix))
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao", "kaist"], ["fro??", "????o", "fr???", "fro???", "pro?", "???st"]))


