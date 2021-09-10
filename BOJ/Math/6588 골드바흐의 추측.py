N = 1000000
is_prime_number = [False, False] + [True]*(N-1)
prime_nums = []

for i in range(2, N+1):
    if is_prime_number[i]:
        prime_nums.append(i)
        for j in range(2*i, N+1, i):
            is_prime_number[j] = False

def answer(N):
    for i in prime_nums:
        if is_prime_number[N - i]:
            return f'{N} = {i} + {N - i}'
        if i > N / 2:
            break
    return "Goldbach's conjecture is wrong."


while True:
    N = int(input())
    if N == 0:
        break
    print(answer(N))
