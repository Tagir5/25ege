a = [True] * (20000 + 1)
a[0] = a[1] = False

for i in range(2, int(len(a) ** 0.5) + 1):
    if a[i]:
        for j in range(i ** 2, len(a), i):
            a[j] = False

primes = {i for i in range(len(a)) if a[i]}
print(len(primes))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def simpl_nmbers(N):
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
    
    return [i for i in primes if i != 0]
