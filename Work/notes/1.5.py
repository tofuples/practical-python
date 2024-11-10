
list_names = [ 'Will Graham', 'Alana Bloom', 'Hannibal Lecter']
list_nums = [40, 39, 78, 50, 101]
line = 'GOOG,100,490.90,JULIE'

row = line.split(',')
print(row)

#List operations
list_names.append('Abigail Hobbs')
list_names.insert(3, 'Jack Crawford')
print(list_names)

print(list_names+list_nums)

#List Iteration and Search
for name in list_names:
    print(name)

list_names.sort()
list_names.sort(reverse=True) # Reverse order
print(list_names)

##EXERCISES
symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG' 
symlist = symbols.split(',') #Split it into a list of names
print(symlist)

#Exercise 1.19
symlist[2]
symlist[1] = 'AIG'
print(symlist)

mysyms = []
mysyms.append('GOOG')
mysyms

#Exercise 1.20: Looping over list items
for s in symlist:
    print('s =',s)
    
#Exercise 1.22: Appending, inserting, and deleting items
symlist.append('RHT')
symlist.insert(1,'AA')
symlist.remove('MSFT')
symlist

symlist.append('YHOO')
symlist.index('YHOO') #first index
symlist.count('YHOO')
symlist.remove('YHOO')
symlist

a = ':'.join(symlist)
a

#Exercise 1.25: Lists of anything
items = [list_nums, list_names, 'etc']
items #list with 3 elementes (1 string and 2 lists)

items[1]
items[1][2]
