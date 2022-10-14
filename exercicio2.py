lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(lista)

print(lista[0:9])
print(lista[8:13])
print(lista[0:15:2])
print(lista[1:16:2])

for num in lista:
    if num % 2 == 0 or num % 3 == 0 or num % 4 == 0:
        print(num)


listaInversa = list(reversed(lista))

print(listaInversa)

soma1 = 0

for i in lista[10:15]:
    soma1 = soma1 + lista[i]

soma2 = 0

for i in lista[3:9]:
    soma2 = soma2 + lista[i]

print(int(soma1)/int(soma2))