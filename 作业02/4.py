def f():
    c=2
    ans=0
    for i in range(0,c+1):
        if (i*i)>c and ans==0:
            ans=i-1
    while(abs(ans*ans-c)>0.0001):
        ans+=0.00001
    return ans            
print(f())