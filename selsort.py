def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        
        min_idx = i
        for j in range(i + 1, n):
            
            if arr[j] < arr[min_idx]:
                min_idx = j
       
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
n=[1,3,2,2,5,4,2,7,6]
x=selection_sort(n)
print(n)