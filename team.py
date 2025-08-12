n=int(input())
solution=0
for i in range(n):
    a=list(map(int, input().split()))
    b=a.count(1)
    if b>=2:
        solution+=1
print(solution)
