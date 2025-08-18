n,b,d=map(int,input().split())
m=list(map(int,input().split()))
waste=0
counter=0
for i in range(len(m)):
    if m[i]<=b:
        waste+=m[i]
        if waste>d:
            counter+=1
            waste=0
    else:
        continue
print(counter)
    
