import time
def calculate(n):
    result = sum([i**2 for i in range(1, n+1)])
    return result
start_time = time.time()
result = calculate(1000000)
end_time = time.time()
print(f"结果为 {result}，用时：{end_time - start_time:.6f}s")