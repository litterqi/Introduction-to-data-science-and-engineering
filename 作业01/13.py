num=int(input("请输入一个正整数：")) #使用递归方法求解阶乘
def f(num):
    if num==1 :
        return 1
    return num*f(num-1)
print(f(num))
