a = 0 
 
for i in range(2945, 18294+1):
    answ = True
    for h in range(2, int(i**0.5)+1):
        if i%(h*h) != 0:
            answ = False
            break
    if answ:
        for m in str(i):
            a+=m
        
            
print(a)