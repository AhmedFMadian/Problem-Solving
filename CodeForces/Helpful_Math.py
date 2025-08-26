n=input().split("+")
n.sort()
if len(n)==1:
    print("".join(n))
else:
    print("+".join(n))