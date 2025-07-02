# Ordenando uma lista de forma permanente - sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(cars)

cars.sort()

print(cars)

# Ordenando a lista na ordem inversa
cars.sort(reverse=True)
print(cars)

# Ordenando uma lista temporariamente - sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('\nHere is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

# Exibindo uma lisa em ordem inversa
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

# Descobrindo o tamanho da lista
print(len(cars))
