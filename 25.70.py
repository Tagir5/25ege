def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
        if len(d) > 3:
            break
    return sorted(d)
a = []
for i in range(2, 10001):
    if sum(divs(i)[:-1]) == i:
        a.append(i)
        a.append(int(len(divs(i))-1))
        
print(a)
    
    
