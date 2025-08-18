number_of_wires = int(input())
birds_on_wires = list(map(int, input().split()))
shots = int(input())
sequence = []
for i in range(shots):
    l, o = map(int, input().split())
    sequence.append((l, o))

for j in range(shots):
    wire = sequence[j][0]
    bird = sequence[j][1]
    if wire != 1 and wire != number_of_wires:
        up_added = bird - 1
        down_added = birds_on_wires[wire - 1] - bird
        birds_on_wires[wire - 2] += up_added   
        birds_on_wires[wire] += down_added    
        birds_on_wires[wire - 1] = 0
    elif wire == 1:
        down_added = birds_on_wires[wire - 1] - bird
        if number_of_wires > 1:
            birds_on_wires[wire] += down_added 
        birds_on_wires[wire - 1] = 0
    elif wire == number_of_wires:
        up_added = bird - 1
        birds_on_wires[wire - 2] += up_added  
        birds_on_wires[wire - 1] = 0
for x in birds_on_wires:
    print(x)
