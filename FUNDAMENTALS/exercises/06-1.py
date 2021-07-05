import time

start = time.time()  # 시작 시간 저장

a = 1
for i in range(10000000):
    a += 1

# 작업 코드
print("time : ", time.time() - start)  # 결과는 '초' 단위
