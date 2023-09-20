def find_max_product(n):
    quotient = n // 3
    remainder = n % 3
    if remainder == 1:
        quotient -= 1
        remainder += 3
    elif remainder==0:
        return [3] * quotient    
    return [3] * quotient + [remainder]
n=int(input("请输入一个数字："))
ans=find_max_product(n)
print(ans)