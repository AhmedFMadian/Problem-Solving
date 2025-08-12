n=input()
s=list(input())
A=0
D=0
for i in range(len(s)):
    if s[i]=="A":
        A+=1
    else:
        D+=1
if A>D:
    print("Anton")
elif D>A:
    print("Danik")
else:
    print("Friendship")
