def f():
    c=10
    ans=c/2
    while(abs(ans*ans*ans-c)>0.00000000001):
        ans=(2*ans+c/(ans*ans))/3
    return ans    
print(f())