n=list(map(int,input().split()))
the_str=list(map(int,input()))
the_dict=dict()
final_value=0
for i in range(len(n)):
    the_dict.update({i+1:n[i]})
for i in range(len(the_str)):
    final_value+=(the_dict[the_str[i]])
print(final_value)