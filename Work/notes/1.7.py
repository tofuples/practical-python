#Functions

def hb(name, age):
    print(f'Happy birthday, {name}! You are {age} years old.')
    
hb('Julie', 24)
hb('Maria', 27)

def sum(n): 
    total = 0  
    while n > 0:
        total += n   
        n -= 1      
    return total    

sum(3)

#Exercise 1.29

def greeting(name):
    print('Hello', name)

greeting('Guido')
help(greeting)

