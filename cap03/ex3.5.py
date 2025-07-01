guests = ['bozo', 'vovó mafalda', 'patati', 'patata', 'piolin']

print(f'Olá, criançada, o {guests[0].title()} chegou!')
print(f'O Mundo Divertido da {guests[1].title()}.')
print(f'Circo do {guests[2].title()} & {guests[3].title()}.')
print(f'O Dia do Palhaço foi inspirado no palhaço {guests[4].title()}.')

print(guests[1].title())

guests[1] = 'tiririca'

print(f'Olá, criançada, o {guests[0].title()} chegou!')
print(f'O Mundo Divertido da {guests[1].title()}.')
print(f'Circo do {guests[2].title()} & {guests[3].title()}.')
print(f'O Dia do Palhaço foi inspirado no palhaço {guests[4].title()}.')