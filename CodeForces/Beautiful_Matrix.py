row=5
arr=[list(map(int,input().split())) for _ in range(row)]
for i,row in enumerate(arr):
    if 1 in row:
        j=row.index(1)
        break
print(abs(2-i)+abs(2-j))


