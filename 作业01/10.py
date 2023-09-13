s=input("请输入一个字符串：")
l=len(s)
flag=0
for i in range(0,l-1):
    if s[i]==s[i+1] :
        print("Yes")
        flag=1
        break
if flag==0 :
    print("No")    