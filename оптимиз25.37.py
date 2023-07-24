n = 0
for i in range(248015, 251575, 2):
    l = 0
    divs = []
    dr = 0
    for d in range(1, i+1, 2):
        if i % d == 0:
            divs.append(d)
            if d**2 == i:
                dr = d
            l += 1
    if len(divs) % 2 != 0:
        n+=1
        print(n, i, len(divs), dr )
    