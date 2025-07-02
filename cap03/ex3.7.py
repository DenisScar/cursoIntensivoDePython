guests = ['bozo', 'vovó mafalda', 'patati', 'patata', 'piolin']

print(f'Olá, criançada, o {guests[0].title()} chegou!')
print(f'O Mundo Divertido da {guests[1].title()}.')
print(f'Circo do {guests[2].title()} & {guests[3].title()}.')
print(f'O Dia do Palhaço foi inspirado no palhaço {guests[4].title()}.')

print('Ei, seus palhaços! Encontrei uma mesa maior! Vou convidar mais uma galera')

guests.insert(0, 'gretchen')
guests.insert(int(len(guests)/2), 'frota')
guests.append('silvio santos')

print(f'Olá, criançada, o {guests[0].title()} chegou!')
print(f'O Mundo Divertido da {guests[1].title()}.')
print(f'Circo do {guests[2].title()} & {guests[3].title()}.')
print(f'O Dia do Palhaço foi inspirado no palhaço {guests[4].title()}.')
print(f'Não condeço {guests[5].title()}.')
print(f'{guests[6].title()} é legal.')
print(f'{guests[7].title()} vem aí!.')

print(len(guests))
print(guests.pop())
print(guests.pop())
print(guests.pop())
print(guests.pop())
print(guests.pop())
print(guests.pop())

del guests[1]
del guests[0]

print(guests)
