#2.1 Datatypes and Data structures

import csv

x = 'GOOG', 100, 490.1

print(type(x)) #tuple -> usually a collection of distinct items, usually all of the same type. A good analogy: A tuple is like a single row in a database table.

name, shares, price = x

print(name, shares, price)
print(name, shares*price)
print(f'${shares*price}')

#tuples vs lists:

record = ('GOOG', 100, 490.1) #tuple -> informações sobre o mesmo objeto, tendo diferentes tipos como string, integer, float
symbols = ['GOOG', 'IBM', 'AAPL'] # lista -> geralmente é uma coleção de coisas do mesmo tipo 

#Dictionaries (mapeia keys to values)

prices = {'GOOG': 100, 'IBM': 200, 'AAPL': 300}
prices['GOOG']
# atualizar valor
prices['IBM'] = 250
prices
#adicionar valor
prices['HPQ'] = 350
prices
#deletar valor
del prices['HPQ']
prices
#listar apenas as keys
list(prices)


############EXERCISES



