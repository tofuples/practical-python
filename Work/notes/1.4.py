import re

#1.14: String concatenation
symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
symbols[0]
symbols[2]
symbols = symbols + ',GOOG'
symbols = symbols + ',HPQ'

'IBM' in symbols


#1.16: String Methods
symbols.lower()
symbols.upper()

symbols.find('Y') 
symbols.replace('SCO', 'DOA')

name = '  IBM  \n'
name.strip()  # Remove surrounding whitespace
 
#1.17: f-strings
name = 'IBM'
shares = 100
price = 95

a = f'{shares} shares of {name} at ${price}'
#print(a)

#Raw
#print(r'\tTab')
#print('\tTab')


#1.18: Regular Expressions  (buscas, validação, substituções)
string = 'abcdefghijklmnopq'
nome = 'Olá, meu nome é tofuples'

pattern = re.compile(r'abc') #cria um padrão de string
pattern2 = re.compile(r'tofu....')

x = re.fullmatch(pattern, string)
print(x) #None

y = re.search(pattern, string)
print(y) #<re.Match object; span=(0, 3), match='abc'>

z = re.search(pattern2, nome)
print(z) #<re.Match object; span=(16, 24), match='tofuples'>  

text =  'today is 6/27/2024 and tomorrow is 7/27/2024'

a = re.findall('\d+/\d+/\d+',text)
b = re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\2-\1',text)
print(text, a, b)

