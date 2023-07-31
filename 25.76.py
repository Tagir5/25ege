def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return (sorted(d))[:-1]
num = [g for g in range(2, 30_001)]
for i in range(2, 30_001):
    if (sum(divs(i)) in num) and (sum(divs(i))>i):
        print(i,sum(divs(i)) )