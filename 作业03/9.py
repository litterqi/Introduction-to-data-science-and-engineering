A=[]
B=[]
front=[]
back=[]
n=int(input("请输入正整数n:"))
for i in range(0,n):
    t=int(input())
    A.append(t)
front.append(A[0])
back.append(A[n-1])
for i in range(1,n):
    front.append(A[i]*front[i-1])
    back.append(A[n-i-1]*back[i-1])
B.append(back[n-2])
for i in range(1,n-1):
    B.append(front[i-1]*back[n-i-2])
B.append(front[n-2])    
print(B)