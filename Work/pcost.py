# pcost.py
#
# Exercise 1.27
import os
import csv
import sys


cost = 0.0
with open('Work/Data/portfolio.csv', 'rt') as file:  # rt reading text
    headers = next(file)
    for line in file:
        row = line.split(',')
        shares = int(row[1])
        price = float(row[2])
        cost += shares * price

print(f'Total cost {cost}')  



#Exercise 1.30

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except ValueError:
                print("Couldn't parse", line)
            
    print('Total cost:', total_cost)

portfolio_cost('Work/Data/portfolio.csv')
#portfolio_cost('Work/Data/missing.csv')

# Exercise 1.32

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except ValueError:
                print("Couldn't parse", line)
    return total_cost
                
if len(sys.argv) == 2:  #verificação da quantidade de argumentos
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv' 
               
cost = portfolio_cost(filename)
print('Total cost:', cost)

# In bash: python3 pcost.py Data/portfolio.csv