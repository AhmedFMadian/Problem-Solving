n=int(input())
the_str=list(input())
the_count=0
for i in range(1,n):
    if the_str[i]==the_str[i-1]:
        the_count+=1
print(the_count)
    






