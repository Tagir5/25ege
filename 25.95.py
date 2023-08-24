a = 0
for n in range(1395, 22718):
    t = True
    q = str(n)[0]
    
    for g in range(len(str(n))-1):
        if str(n)[g] <= q:
            t = False
            break
        else:
            q = str(n)[g]
    
    if t:
        a += n

print(a)
            
        
        
