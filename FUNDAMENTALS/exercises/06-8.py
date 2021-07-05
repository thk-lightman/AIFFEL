list_data = [30, 20, 10, 40, 50]


def minmax_function(x_list):
    def inner_min_function(x):
        return min(x)

    def inner_max_function(x):
        return max(x)

    x_min = inner_min_function(x_list)
    x_max = inner_max_function(x_list)

    return x_min, x_max


min_value, max_value = minmax_function(list_data)

print("최솟값은 : ", min_value)
print("최댓값은 : ", max_value)
