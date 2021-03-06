# 피보나치 수를 이용해서 피보나 치킨 수 구하기
from math import sqrt, log, floor

phi = (1 + sqrt(5)) / 2
phi_ = 1 - phi


def Binet(i):
    return round((phi ** i - phi_ ** i) / sqrt(5))


def inverse_fibonacci(N):
    return round(log(sqrt(5) * N) / log(phi))


def is_perfect(n):
    rootn = floor(sqrt(n))
    return True if rootn * rootn == n else False


def is_fibonacci(N):
    x, y = 5 * N * N + 4, 5 * N * N - 4
    return is_perfect(x) or is_perfect(y)


def FibonaChicken(N):
    if is_fibonacci(N):
        return Binet(inverse_fibonacci(N) - 1)


N = int(input("자애로운 자여, 몇 명이나 먹이려고 하는고? "))
C = FibonaChicken(N)
print("그렇다면", C, "마리를 시키거라")
print("능히", N, "명을 먹이는데 부족함이 없느니라.")
