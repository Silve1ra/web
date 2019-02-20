#procurar padroes em strings python
import re

patterns = ['term1', 'term2']

text = 'this is a string with term1, but not the other!'

# funcao simples para buscar algo em uma string
'''
for pattern in patterns:
    print("i am searching for: "+pattern)

    if re.search(pattern, text):
        print("MATCH!")
    else:
        print("NO MATCH!")
        
'''

'''
#se quer a localização e não o booleano
match = re.search('term1', text)

print(type(match))
print(match.start())
'''

'''
split_term = '@'
email = 'user@gmail.com'
#email = 'user@gmail.com'.split('@')
match = re.split(split_term, email)

print(match)
'''

'''
# encontrar todas as instancias de um padrão
a = re.findall('match', 'test phrase match in match middle')
print(a)
print(len(a))
'''

'''
def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("searching for patter {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dsssss...sddddd'
test_patterns = ['s[sd]+'] 
#ssd* sd sdd sddd sdddd sdddddd...
#sd+ sd sddd sdddd sddd ...
#sd? s sd 
#sd{3} sddd
#sd{1,3} sd sddd
#s[sd]+ s s seguido por um ou mais s ou por um ou mais d

multi_re_find(test_patterns, test_phrase)
'''

def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("searching for patter {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')

test_phrase = 'This is a string! But it has punctuation. And numbers 1233232. And a symbol #hashtag How can we remote it?'
#test_patterns = ['[^!.?]+'] 
# ^ to exclude terms
test_patterns = [r'\W+'] 
#r'\w+' alfanumericos
#r'\w+' não alfanumericos
#r'\s+' espacos
#r'\S+' sem espacos
#r'\d+' sequencia de numeros
#r'\D+' sequencia sem numeros
#[a-z]+ lower cases
#[A-Z]+ upper cases
multi_re_find(test_patterns, test_phrase)