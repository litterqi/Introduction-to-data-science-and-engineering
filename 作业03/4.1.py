def is_prime(a):
    if a <= 1:
        return False
    elif a == 2:
        return True
    elif a % 2 == 0:
        return False
    else:
        for i in range(3, int(a**0.5) + 1, 2):
            if a % i == 0:
                return False
        return True
num = int(input("请输入一个正整数："))
if is_prime(num):
    print(f"{num} 是质数")
else:
    print(f"{num} 不是质数")