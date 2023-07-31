# **Desafio 09**
#
# Faça uma função calculadora de dois números com três parâmetros:
# os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada.
# Considera a seguinte definição:
# 1 Soma
# 2 Subtração
# 3 Multiplicação
# 4 Divisão
#
# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.


print("Olá, vamos fazer uns calculos simples:")

num_1 = float(input("Digite o primeiro numero para calcularmos: \n"))
num_2 = float(input("Digite o segundo numero para calcularmos: \n"))
operador = input("Escolha o operador - (+)Soma, (-)Sub, (*) Multi, (/) Div: \n")


def Calcular(num_1, num_2, operador):
    if operador == "+":
        return num_1 + num_2
    elif operador == "-":
        return num_1 - num_2
    elif operador == "*":
        return num_1 * num_2
    elif operador == "/":
        return num_1 / num_2
    else:
        print("Operação invalida!")
    exit(1)


result = Calcular(num_1, num_2, operador)

print("\nO resultado do seu calcaulo é: ", result)
