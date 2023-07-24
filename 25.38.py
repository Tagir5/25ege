summ = 0
for i in range(268220, 270335):
    divs = []
    c = 0
    for d in range(1, i+1):
        if i % d == 0:
            divs.append(d)
            c+=1
        if c >4:
            break
    if c >4:
        continue
    else:
        if summ < sum(divs):
            summ =sum(divs)
            print(summ, c, divs)