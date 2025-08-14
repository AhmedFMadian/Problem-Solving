n=int(input())
the_crimes=list(map(int,input().split()))
untreated=0
officers=0
for i in range(n):
    if the_crimes[i]==1:
        officers+=1
    else:
        if the_crimes[i]+officers>=0:
            officers=the_crimes[i]+officers
        else:
            untreated+=1
print(untreated)
