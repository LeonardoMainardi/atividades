nomes = ["Alexandre", "Alice", "André", "Arthur", "Arthur", "Artur", "Augusto", "Bernardo", "Bernardo", "Bruno", "Davi", "Diego", "Eduardo", "Fabrício", "Felipe", "Fernando", "Francisco", "Francisco", "Gabriel", "Gabriel", "Giovanna", "Giovanni", "Guilherme", "Guilherme", "Hector", "Henrique", "Inácio", "João", "João", "Joaquim", "Júlia", "Lauren", "Leonardo", "Leonardo", "Lucas", "Marina", "Matheus", "Matheus", "Paula", "Pedro", "Pedro", "Pedro", "Pedro", "Rafael", "Regis", "Sofia", "Stella", "Thiago", "Valentina", "Vicente", "Lucas"]

# Organizar por ordem alfabética
nomes_ordenados = sorted(nomes)

print("Nomes em ordem alfabética:")
for nome in nomes_ordenados:
    print(nome)

# Organizar por ordem alfabética da última letra
nomes_ordenados_ultima_letra = sorted(nomes, key=lambda x: x[-1])

print("\nNomes em ordem alfabética da última letra:")
for nome in nomes_ordenados_ultima_letra:
    print(nome)