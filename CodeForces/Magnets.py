n=int(input())
the_list = []
for i in range(n):
    the_list.append(input())
sets=1
for i in range(n-1):
    if the_list[i]!=the_list[1+i]:
        sets += 1
print(sets)
