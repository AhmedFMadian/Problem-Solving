n,x=map(int,input().split())
icecream=x
distressed=0
for _ in range(n):
    op,number=input().split()
    number=int(number)
    if op=="+":
        icecream+=number
    elif op=="-":
        if icecream>=number:
            icecream-=number
        else:
            distressed+=1
print(icecream,distressed)