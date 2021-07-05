my_list = ["a", "b", "c", "d", "e", "f", "g"]

# 위 예제와 같은 결과
result_list = [(i, j) for i in range(2) for j in my_list]

print(result_list)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# if 조건문 사용
even_squares = [x ** 2 for x in a if x % 2 == 0]
print(even_squares)

# for 반복문과 if 조건문 여러 개 사용하기
a = [i * j for j in range(2, 10) for i in range(1, 10)]  # 뒤에서부터 앞으로
print(a)

# 이중 리스트 만들기
a = [[0 for _ in range(4)] for _ in range(4)]
print(a)

a = [[0] * 4 for _ in range(4)]
print(a)

