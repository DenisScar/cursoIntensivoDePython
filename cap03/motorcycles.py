motorcycles1 = ['honda', 'yamaha', 'suzuki']
print(motorcycles1)

# Inserindo elemenos no final de uma lista
motorcycles1.append('ducati')
print(motorcycles1)

motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print(motorcycles2)

# Inserindo elementos em qualquer posição da lista
motorcycles2.insert(0, 'ducati')
print(motorcycles2)

# Removendo elementos de qualquer posição da lista
del motorcycles2[0]
print(motorcycles2)

del motorcycles2[0]
print(motorcycles2)

# Removendo o último elemento da lista (ou topo da pilha)
motorcycles3 = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles3.pop()
print(last_owned)

# Removendo itens de qualquer posição de uma lista
first_owned = motorcycles3.pop(0)
print(first_owned)

# Removendo item de acordo com o valor
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f'{too_expensive.title()} is too expensive for me.')
