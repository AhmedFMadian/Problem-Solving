n=int(input())
the_list = list(map(int,input().split()))
Sereja=0
Dima=0
for i in range(n):
    if i%2==0:
      if the_list[0]>the_list[-1]:
         Sereja+=the_list[0]
         the_list.remove(the_list[0])
      else:
         Sereja+=the_list[-1]
         the_list.remove(the_list[-1])
    else:
       if the_list[0]>the_list[-1]:
         Dima+=the_list[0]
         the_list.remove(the_list[0])
       else:
         Dima+=the_list[-1]
         the_list.remove(the_list[-1])
       
print(Sereja,Dima)





