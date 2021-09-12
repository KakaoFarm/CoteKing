def prime_numbers(n):
    is_prime = [True for i in range(n+1)]
    for i in range(2, int(n**(1/2)) + 1):
        j = 2
        while i * j <= n:
            is_prime[i * j] = False
            j += 1
    return [i for i in range(2, n+1) if is_prime[i]]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

def knary(n, k):
    answer = ""
    while n > 0:
        n, mod = divmod(n, k)
        answer += str(mod)
    return(answer[::-1])


def solution(n, k):
    answer = 0
    knaried = knary(n, k)
    nums = knaried.split("0")
    candidates = []
    for num in nums:
        if num != "":
            candidates.append(int(num))
    for num in candidates:
        if is_prime(num):
            answer += 1
    return answer

