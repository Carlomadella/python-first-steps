# stampare qualcosa in console
# print("Ciao")


# VARIABILI

# possibili metodi per scrivere una variabile

# metodo consigliato (snake case)
peso_persona = 7
# altri metodi legali
# pesopersona
# _peso_persona
# pesoPersona
# PESOPERSONA #diverso da pesopersona perchè Python è case sensitive

# metodi illegali

# 2peso_persona # NON si può iniziare con un numero
# peso-persona # NO trattini nel nome
# peso persona # NO spazi nel nome

# In Python si può assegnare multipli valori ad una singola variabile
x, y, z = 8, 22, 34

print(x, y, z)
# oppure
# print(x)
# print(y)
# print(z)
# in console appariranno comunque 8,22,34

# se vogliamo che più variabili abbiano lo stesso valore possiamo scrivere così
e = l = i = 88
print(e, l, i)
# in console apparirà 3 volte 88

# COLLECTION
citta = ["Milano", "Genova", "Palermo"]
a, b, c = citta
print(a, b, c)
# in console apparirà Milano Genova Palermo
