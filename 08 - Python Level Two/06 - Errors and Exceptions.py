#try
#except
#finally

'''
try:
    f = open('simple.txt', 'r')
    f.write("Test write to simple text")

except IOError: #InputOutputError
    print("ERROR: Não achou/sobrescrever o arquivo")

else:
    print("Success!")
    f.close()

print("hello world")
#com o try ele não para aonde errou, continua o codigo

f = open('simple.txt', 'r')
f.write("Test write to simple text")
print("hello world")
'''

'''
#não precisa necessariamente saber o tipo exato de erro, deixar generico
try:
    f = open('simple.txt', 'r')
    f.write("Test write to simple text")

except: #InputOutputError
    print("ERROR: Não achou/sobrescrever o arquivo")

else:
    print("Success!")
    f.close()

print("hello world")
'''

try:
    f = open('simple.txt', 'r')
    f.write("Test write to simple text")

except: #InputOutputError
    print("ERROR: Não achou/sobrescrever o arquivo")

else:
    print("Success!")
    f.close()
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")