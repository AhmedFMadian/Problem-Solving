s = input().strip().lower()   
t = input().strip().lower()   

pos = 0                       
for i in t:
    if pos < len(s) and s[pos] == i:
        pos += 1


print(pos + 1)
