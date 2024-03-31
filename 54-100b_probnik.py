a = open('24.txt').read()
w = 'RSQ'
d = []
n = 0
c = 1

for f in range(n, len(a)-1) :
    g = w.index(a[f])

    for s in range(f+1, len(a)) :
        if g == 2 :
            g = 0
        else:
            g += 1
            
        if a[s] == w[g] :
            c+=1
        else:
            d.append(c)
            c =  1
            n = s
            break
        
print(max(d))


    
    
    
    
