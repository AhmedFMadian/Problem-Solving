n,t,k,d=map(int,input().split())
time1=0
cooked=n
if n-k<=k:
    time1=t*2
else:
    while cooked-k>k:
        time1+=t
        cooked-=k
    time1=time1+t
time2=0    
if d<t and k<n:
    print("YES")
elif d>=t and n-k<=k:
    print("NO")
elif k>n:
    print("NO")
elif n-k>k and d<time1:
    print("YES")
elif n-k>k and d>=time1:
    print("NO")
elif n==k:
    print("NO")
