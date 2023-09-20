def f():
    c=2000
    ans=c/2
    while(abs(ans*ans-c)>0.00000000001):
        ans=(ans+c/ans)/2
    return ans    
print("c=2000:",f())