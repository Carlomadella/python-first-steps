# CASTING
# con casting si indica il modo per convertire un tipo di dato in un altro
# si utilizza perchè, ad esempio, a differenza di Javascript in Python non è possibile concatenare una stringa ad un numero
# per fare il casting si usano int(), float(), str()


# CONCATENAZIONE DI STRINGHE

# ERRORE
x = "Ciao sono "
y = 5

# print(x + y)
# in console apparirà il messaggio: TypeError: can only concatenate str (not "int") to str

# METODO CORRETTO con il casting
x = "Ciao sono"
y = str(5)

print(x, y)
# in console apparirà Ciao sono 5


# OPERAZIONI MATEMATICHE

# ERRORE
a = 8
b = "24"

# print(a + b)
# in console apparirà il messaggio TypeError: unsupported operand type(s) for +: 'int' and 'str'

# METODO CORRETTO con il casting
a = 8
b = int("24")

print(a + b)
# in console apparirà 32
