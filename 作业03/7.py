def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
num1 = int(input("请输入第一个正整数："))
num2 = int(input("请输入第二个正整数："))
result = gcd(num1, num2)
print(f"最大公约数为：{result}")