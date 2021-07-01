# N이 피보나치 수가 아닐 경우 제켄도르프 분해로 구한다
from math import sqrt, log, floor

phi = (1 + sqrt(5)) / 2
phi_ = 1 - phi


# 비네의 공식으로 피보나치 수 구하기
def Binet(i):
    return round((phi ** i - phi_ ** i) / sqrt(5))


# 피보나치 역함수: 피보나치 수를 넣으면 인덱스가 나온다
def inverse_fibonacci(N):
    return round(log(sqrt(5) * N) / log(phi))


# 완전제곱수인지 판단 - 피보나치 수인지 판단할 때 사용된다
def is_perfect(n):
    rootn = floor(sqrt(n))
    return True if rootn * rootn == n else False


# 피보나치 수인지 판단
def is_fibonacci(N):
    x, y = 5 * N * N + 4, 5 * N * N - 4
    return is_perfect(x) or is_perfect(y)


def FibonaChicken(N):
    if N <= 2:  # N이 1과 2일 경우 1을 리턴
        return 1
    i = inverse_fibonacci(N)
    if is_fibonacci(N):
        return Binet(i - 1)
    else:
        while N > Binet(i):
            i += 1
        return Binet(i - 2) + FibonaChicken(N - Binet(i - 1))


for N in range(15, 65):
    print(N, FibonaChicken(N))
