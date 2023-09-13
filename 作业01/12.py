num=int(input("请输入一个数："))
left=0
right=num
while left<right :
    mid=(left+right)//2
    tmp=mid*mid*mid
    if tmp==num :
        print(mid)
        import sys
        sys.exit()
    elif tmp>num :
        right=mid-1
    else :
        left=mid+1    
if left*left*left>num :        
    print(left-1)
else :
    print(left)    