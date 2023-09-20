def f():
    c=2
    ans=c/4
    while(abs(ans*ans-c)>0.00000000001):
        ans=(ans+c/ans)/2
    return ans    
print("g=c/4:",f())