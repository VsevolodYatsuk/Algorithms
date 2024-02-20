def find_max_min(arr):
    if not arr:
        return None, None

    max_elem = arr[0]
    min_elem = arr[0]

    for num in arr:
        if num > max_elem:
            max_elem = num
        elif num < min_elem:
            min_elem = num

    return max_elem, min_elem

array = [3, 1, 7, 4, 2, 9, 5]
max_num, min_num = find_max_min(array)
print("Максимальный элемент:", max_num)
print("Минимальный элемент:", min_num)