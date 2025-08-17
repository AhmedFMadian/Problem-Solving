k,r=map(int,input().split())
count=1
flag=True
while flag:
    total=count*k
    The_list=[int(d) for d in str(total)]
    if The_list[-1]==r or The_list[-1]==0:
        print(count)
        flag=False
    else:
        count+=1
