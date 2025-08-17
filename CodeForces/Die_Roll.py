from math import gcd
n = list(map(int, input().split()))
the_max = max(n[0], n[1])
The_percent = (6 - the_max) + 1
g = gcd(The_percent, 6)
print(The_percent//g, 6//g, sep='/')
