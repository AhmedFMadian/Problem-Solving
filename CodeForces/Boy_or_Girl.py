the_str=list(input().lower())
the_count=len(set(the_str))
if the_count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
