n=int(input())
skills=list(map(int,input().split()))
the_min=min(skills.count(1),skills.count(2),skills.count(3))
w=the_min
ones_indices=[]
twos_indices=[]
threes_indices=[]
if skills.count(1)==0 or skills.count(2)==0 or skills.count(3)==0:
    print(0)
else:
 for i, val in enumerate(skills) :
    if val==1:
        ones_indices.append(i+1)
    elif val==2:
        twos_indices.append(i+1)
    elif val==3:
        threes_indices.append(i+1)
 print(w)
 for i in range(w):
    print(ones_indices[i],twos_indices[i],threes_indices[i],sep=" ")

