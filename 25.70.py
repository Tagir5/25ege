def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
        if len(d) > 3:
            break
    return sorted(d)
array_of_answer = []
for number in range(2, 10001):
    if sum(divs(number)[:-1]) == number:
        a.append(number)
        a.append(int(len(divs(number))-1))
        
print(array_of_answer)
    
    
