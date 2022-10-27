nome = input("Digite seu nome: ")
print(f"Boa noite, seu nome é {nome}")

print("Quantos anos você tem?")
idade = int(input("Digite a sua idade: "))
print(f"Olá {nome} você tem {idade} anos")

dobro = idade * 2
print(f"O dobro da idade informada é {dobro}")

if idade >= 18:
  print("Você é maior de idade, ótimo! já pode beber e dirigir")
else:
  print("Você é menor de idade")


genero = input("Informe o genero M=Masculino, F=Femino")
if idade >= 18 and genero == 'M':
  print("Você precisa prestar o serviço militar obrigatório")
  