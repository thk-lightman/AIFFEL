from math import sqrt, floor


# 완전 제곱수인지 판별
def is_perfect(n):
    rootn = floor(sqrt(n))
    if rootn * rootn == n:
        return True
    return False


def is_fibonacci(N):
    x, y = 5 * N * N + 4, 5 * N * N - 4
    return is_perfect(x) or is_perfect(y)  # x 혹은 y가 완전제곱수이면 피보나치 수열이다


N = 1000

F = []
for i in range(N + 1):
    if is_fibonacci(i):
        F.append(i)
print(F)
