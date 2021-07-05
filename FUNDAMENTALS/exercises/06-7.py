list_data = [30, 20, 10, 40, 50]


def minmax_function(x_list):
    def inner_min_function(x):
        return min(x)

    def inner_max_function(x):
        return max(x)

    x_min = inner_min_function(x_list)
    x_max = inner_max_function(x_list)

    minmax_list = [x_min, x_max]

    return minmax_list


print("최솟값, 최댓값은 : ", minmax_function(list_data))
print("최솟값은 : ", minmax_function(list_data)[0])
print("최댓값은 : ", minmax_function(list_data)[1])
