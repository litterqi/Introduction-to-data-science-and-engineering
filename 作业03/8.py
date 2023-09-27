import random
import time
# 选择排序
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
# 归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(left)
    merged.extend(right)
    return merged

lengths = [100, 1000, 5000, 10000] 
for length in lengths:
    arr = list(range(length))
    random.shuffle(arr)
    start_time = time.time()
    selection_sort(arr)
    end_time = time.time()
    selection_time = end_time - start_time
    random.shuffle(arr)
    start_time = time.time()
    arr = merge_sort(arr)
    end_time = time.time()
    merge_time = end_time - start_time
    print(f"长度为 {length} 的数列：选择排序耗时 {selection_time:.6f}s，归并排序耗时 {merge_time:.6f}s")