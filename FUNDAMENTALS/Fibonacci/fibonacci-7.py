# final solution
from math import sqrt, log, floor

phi = (1 + sqrt(5)) / 2
phi_ = 1 - phi


def Binet(i):
    """
    비네의 공식으로 피보나치 수를 구해준다
    """
    return round((phi ** i - phi_ ** i) / sqrt(5))


def inverse_fibonacci(N):
    """
    피보나치 수열의 역함수:
    
    피보나치 수를 넣어주면 인덱스가 나온다
    """
    return round(log(sqrt(5) * N) / log(phi))


def is_perfect(n):
    """
    완전 제곱수인지 판단

    피보나치 수인지 판단할 때 사용된다.
    """
    rootn = floor(sqrt(n))
    return True if rootn * rootn == n else False


def is_fibonacci(N):
    """
    N이 피보나치 수인지 판단
    """
    x, y = 5 * N * N + 4, 5 * N * N - 4
    return is_perfect(x) or is_perfect(y)


def FibonaChicken(N):
    """
    피보나 치킨 함수
    
    N: 사람 수
    리턴 값 : 치킨 수
    """
    if N <= 2:  # N이 1과 2라면 리턴 1
        return 1
    i = inverse_fibonacci(N)
    if is_fibonacci(N):  # 사람 수가 피보나치 수라면 사람 수 - 1의 피보나치 값을 반환해준다
        return Binet(i - 1)
    else:  # 사람 수가 피보나치수가 아니라면
        while N > Binet(i):  # N보다 큰 첫 번째 피보나치 수의 i 확인
            i += 1
        return Binet(i - 2) + FibonaChicken(
            N - Binet(i - 1)
        )  # i - 2번째 [피보나치 수] + 재귀 호출로 i - 1번째 [피보나 치킨 수] 호출


N = int(input("자애로운 자여, 몇 명이나 먹이려고 하는고? "))
C = FibonaChicken(N)
print("그렇다면", C, "마리를 시키거라")
print("능히", N, "명을 먹이는데 부족함이 없느니라.")
