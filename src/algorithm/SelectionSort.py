def SelectionSort(arr):
    n = len(arr)
    cnt = 1
    
    print("원본 데이터",arr,"\n")
    for i in range(n - 1, 0, -1):
      boolean = False
      max = 0
      for j in range(1, i + 1):
        if arr[max] < arr[j]:
          max = j
          boolean = True
      if(boolean): 
        arr[i], arr[max] = arr[max], arr[i]
      print(cnt,"회차",arr)
      cnt += 1


arr = [10,9,8,7,6,5,4,3,2,1]
SelectionSort(arr)
print("\n최종 데이터",arr)
