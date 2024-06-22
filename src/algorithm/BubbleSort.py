def BubbleSort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(i,n):
      if arr[i] > arr[j] :
        arr[i], arr[j] = arr[j], arr[i]

arr = [5, 2, 4, 3, 1]
BubbleSort(arr)
print(arr[0:])  