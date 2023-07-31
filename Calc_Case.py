#** Desafio 10 **
#
#Faça uma função calculadora que os números e as operações serão feitas pelo usuário.
# O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:
# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair
# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro,
# o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.
# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada.
# Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.
# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.

print("Olá, vamos fazer calculos simples:")
print("\nOpções: [1 = (+)Soma, 2 = (-)Sub, 3 = (*) Multi, 4 = (/) Div, 0 = Sair]\n")
num_1 = float(input("Informe o primeiro nº para calcularmos: \n"))
num_2 = float(input("Informe o segundo nº para calcularmos: \n"))
operador = int(input("Escolha o nº correspondente a operação [1 = (+)Soma, 2 = (-)Sub, 3 = (*) Multi, 4 = (/) Div, 0 = Sair]: \n"))

def Calc_Case(num_1, num_2, operador):
    match (operador):
        case 1:
            print("\nSoma é: \n", num_1 + num_2)
        case 2:
            print("\nSubtracao é: \n", num_1 - num_2)
        case 3:
            print("\nMultiplicacao é: \n", num_1 * num_2)
        case 4:
            print("\nDivisão é: \n", num_1 / num_2)
    if operador >= 5:
        print("Operação não existe!")


while operador != 0:
    result = Calc_Case(num_1, num_2, operador)
    print("\n***Novo Calculo***")
    print("\nOpções: [1 = (+)Soma, 2 = (-)Sub, 3 = (*) Multi, 4 = (/) Div, 0 = Sair]")
    num_1 = float(input("\nInforme o primeiro nº para calcularmos: \n"))
    num_2 = float(input("Informe o segundo nº para calcularmos: \n"))
    operador = int(input("Escolha o nº correspondente a operação [1 = (+)Soma, 2 = (-)Sub, 3 = (*) Multi, 4 = (/) Div, 0 = Sair]: \n"))
else:
    print("\nVocê saiu, obrigado por calcular!")

