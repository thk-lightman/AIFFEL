my_list = ["a", "b", "c", "d", "e", "f", "g"]

# 인자로 받은 리스트로부터 데이터를 하나씪 가져오는 제너레이터를 리턴하는 함수
def get_dataset_generatr(my_list):
    result_list = []
    for i in range(2):
        for j in my_list:
            yield (i, j)
            print(">> 1 data loaded..")


dataset_generator = get_dataset_generatr(my_list)
for X, y in dataset_generator:
    print(X, y)

