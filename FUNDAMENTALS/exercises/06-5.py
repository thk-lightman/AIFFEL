import time

num_list = ["p1", "p2", "p3", "p4"]
start = time.time()


def count(name):
    for i in range(0, 100000000):
        a = 1 + 2

    print("finish : ", name)


for num in num_list:
    count(num)

print("time : ", time.time() - start)
