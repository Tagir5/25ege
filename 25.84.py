for n in range(87921, 88188):
    s = 0
    m = 1
    n = str(n)
    for i in range(0, len(n)):
        s += int(str(n)[i])
        m *= int(str(n)[i])
    
    if (s % 14 == 0) and (m % 18 == 0) and (m != 0):
        print(s, m)
    
        
        