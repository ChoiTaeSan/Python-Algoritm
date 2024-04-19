def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 중간 원소를 피벗으로 선택
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == '__main__':
    unsorted_array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quick_sort(unsorted_array)
    print(sorted_array)
