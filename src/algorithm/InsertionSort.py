def Insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # 현재 비교할 요소를 선택합니다.
        j = i - 1

        # key보다 큰 요소들을 오른쪽으로 이동시킵니다.
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # key를 올바른 위치에 삽입합니다.
        arr[j + 1] = key

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    Insertion_sort(arr)
    print("정렬된 리스트:", arr)


