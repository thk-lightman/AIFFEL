import multiprocessing  # multiprocessing
import time

num_list = ["p1", "p2", "p3", "p4"]
start = time.time()


def count(name):
    for i in range(0, 100000000):
        a = 1 + 2

    print("finish : ", name)


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    pool.map(count, num_list)  # 병렬화 시키기, count 함수에 num_list 원소 넣는다
    pool.close()  # 더 이상 새로운 작업을 추가하지 않을 때 사용
    pool.join()  # 병렬처리 작업이 끝날 때까지 기다린다


print("time : ", time.time() - start)
