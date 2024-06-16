#Exercise 1
def max_kernel(num_list, k):
    result = []
    n = len(num_list)

    for i in range(n - k + 1):
        sliding_window = num_list[i:i + k]
        max_value = max(sliding_window)
        result.append(max_value)

    return result

# Kiểm tra kết quả với ví dụ đã cho
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))