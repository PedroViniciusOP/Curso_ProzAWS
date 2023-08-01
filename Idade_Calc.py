# ***Desafio 11***
#
# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
# Caso o usuário não digite um número ou apareça um inválido no campo do ano,
# o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

print("Bem vindo! Vamos descobrir sua idade?\n")
print("Para começar responda:\n")

def calcular_idade(ano_nasc):
  """Calcula a idade de uma pessoa com base no ano de nascimento."""
  ano_atual = 2022
  while ano_nasc < 1922 or ano_nasc > 2021:
    print("Ano inválido. Digite um ano entre 1922 e 2021.")
    ano_nasc = int(input("Informe seu ano de nascimento: "))

  try:
    idade = ano_atual - ano_nasc
  except ValueError:
    print("Ano inválido. Digite um ano em nº inteiro ex:'2000'.")
    ano_nasc = int(input("Informe seu ano de nascimento: "))

  return idade


def main():
  nome = input("Digite seu nome completo: \n")
  ano_nasc = int(input("Digite seu ano de nascimento: \n"))

  idade = calcular_idade(ano_nasc)

  if idade is not None:
    print(f"Olá {nome}! Você tem ou completará {idade} anos de idade em 2022.")


if __name__ == "__main__":
  main()