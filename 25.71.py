N = int(20000)
primes = [i for i in range( N + 1)]
primes[1] = 0
i = 2

while i <= N:
    
    if primes[i] != 0:
        j = i + i
        
        while j <= N:
            primes[j] = 0
            j = j + i
            
    i += 1
    
primes = [i for i in primes if i != 0]

answer = 0

for number in range(2, 20_001):
    
    count_of_simp_divs = 0
    
    if number in primes[1:]:
        continue
    
    for division in primes:
        
        if number % division != 0:
            count_of_simp_divs += 1
            
            if count_of_simp_divs == 4:
                answer += 1
                break

print(answer)