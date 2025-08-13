the_str=list(input())
upper=0
lower=0
for litter in the_str:
    if litter.isupper():
        upper += 1
    elif litter.islower():
        lower += 1
if upper>lower:
    print("".join([litter.upper()for litter in the_str]))
elif lower>upper:
    print("".join([litter.lower()for litter in the_str]))
else:
    print("".join([litter.lower() for litter in the_str]))
