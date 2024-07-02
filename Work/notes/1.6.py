#1.6 File Management
import os
import gzip
os.getcwd()

with open('Work/Data/portfolio.csv', 'rt') as arquivo:
    for line in arquivo:
        x = arquivo.read()
    
print(x)

#Exercisess

with open('Work/Data/portfolio.csv', 'rt') as file:
    data = file.read()

print(data)



with open('Work/Data/portfolio.csv', 'rt') as file:
    headers = next(file).split(',') #skip the first line of column headers
    for line in file:
        print(line.split(','), end='')
        
print(headers)

# Exercise 1.28: Other kinds of “files”

with gzip.open('Work/Data/portfolio.csv.gz', 'rt') as file:
    for line in file:
        print(line, end='')