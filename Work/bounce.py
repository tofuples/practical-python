# bounce.py
#
# Exercise 1.5



#######  Usando for 

#h = 100 #meters
#b = 0.6*h
#
#for i in range(10):
#    print(i, round(b, 4))
#    b = (0.6)*b
   

####### Usando while

h = 100
b = 1

while b <= 10:
    h = 0.6*h
    print(b, round(h, 4))
    b = b + 1
    
    
#22/10/24


h = 100
b = 1

while b<=10: 
    h = h*0.6
    if b == 1:
        print(f'A  bola caiu {b} vez e alcançou {h} altura.')
    else:
        print(f'A  bola caiu {b} vezes e alcançou {h} altura.')
    b += 1
    