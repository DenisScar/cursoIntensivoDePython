name = "ada lovelace"

print(name.title()) # Método que apresenta cada palavra com inicial maiúscula
print(name.upper()) # Método que apresenta todos os caracteres maiúsculos
print(name.lower()) # Método que apresenta todos os caracteres minúsculos


first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name # Concatenação de strings
message = "Hello, " + full_name.title() + "!"

print(message)

# Adicionando espaços em branco (com tabulações e quebras de linha)
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Removendo espaços em branco
favorite_language = 'python '
print(len(favorite_language))
print(len(favorite_language.rstrip())) # rstrip() remove espaços em branco à direita

favorite_language = '  python'
print(len(favorite_language))
print(len(favorite_language))
print(len(favorite_language.lstrip())) # rstrip() remove espaços em brsnco à esquerda
