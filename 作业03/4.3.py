def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  
        j = i - 1  
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]  
            j -= 1
        arr[j+1] = key  
arr = []
n=int(input("请输入数组长度："))
for i in range(0,n):
    t=int(input())
    arr.append(t)
insertion_sort(arr)
print("排序结果：", arr)