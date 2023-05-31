#Objetivo: Criar um programa que printe os numeros de uma lista e, depois, eles multiplicados por 2
#Bonus: Colocar os numeros multiplicados em uma outra lista e printa-la


lista = [2, 3, 7, 12, 2]
lista_multiplicada = []

for num in lista:
    print(f"O número da lista é {num}")
    num_multiplicado = num * 2
    lista_multiplicada.append(num_multiplicado)

print("Lista original:", lista)
print("Lista multiplicada:", lista_multiplicada)