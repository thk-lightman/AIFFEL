my_list = ["a", "b", "c", "d", "e", "f", "g"]

for i, value in enumerate(my_list):
    print("Index: ", i, ", Value: ", value)


result_list = []
for i in range(2):
    for j in my_list:
        result_list.append((i, j))

print(result_list)
