import sys

N = int(sys.stdin.readline().rstrip())
words = []

for _ in range(N):
    words.append(sys.stdin.readline().rstrip())

alphas = ""
for word in words:
    alphas += word
alphas = set(alphas)
counts = {}
for alpha in alphas:
    counts[alpha] = 0

for word in words:
    s = 0
    for i in reversed(range(len(word))):
        counts[word[i]] += 10**s
        s += 1

sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

ans = 0
cur_num = 9
for i in range(len(sorted_counts)):
    ans += cur_num * sorted_counts[i][1]
    cur_num -= 1

print(ans)
