import sys
import heapq

N = int(sys.stdin.readline().rstrip())
decks = []
for _ in range(N):
    decks.append(int(sys.stdin.readline().rstrip()))
heapq.heapify(decks)

answer = 0
while len(decks) > 1:
    smallest_deck = heapq.heappop(decks)
    second_smallest_deck = heapq.heappop(decks)
    new_deck = smallest_deck + second_smallest_deck
    answer += new_deck
    heapq.heappush(decks, new_deck)

print(answer)