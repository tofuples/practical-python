#1.6 File Management
import os
import gzip
os.getcwd() #file directory

with open('Work/Data/portfolio.csv', 'rt') as arquivo:
    x = arquivo.read()

x  #raw string
print(x) #formatado, linha por linha 

#quando o arquivo é grande é conveniente ler linha por linha com loop
with open('Work/Data/portfolio.csv', 'rt') as arquivo:
    for line in arquivo:
        print(line, end="") 


with open('Work/Data/portfolio.csv', 'rt') as file:
    data = file.read()

print(data)



with open('Work/Data/portfolio.csv', 'rt') as file:
    headers = next(file).split(',') #skip the first line of column headers
print(headers)


#Pula o header e depois lê linha por linha, separando a string em pequenas strings
with open('Work/Data/portfolio.csv', 'rt') as file:
    headers = next(file).split(',') #skip the first line of column headers
    for line in file:
        print(line.split(',')) 
        
# Exercise 1.28: Other kinds of “files”

with gzip.open('Work/Data/portfolio.csv.gz', 'rt') as file:
    for line in file:
        print(line, end='')
        
# end='' ends the output with a space. by default, the value of this parameter is ‘\n’, i.e. the new line character.