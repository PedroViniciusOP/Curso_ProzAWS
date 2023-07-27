"""
** Desafio 07 **

Desenvolva um código que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação
para o veículo informado a partir das condições:

A: Veículos com duas ou três rodas;
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
E: Veículos com quatro rodas ou mais e com mais de 6000 kg.
"""
print("***Definindo Categoria de Habilitacao para Veiculo***\n")
print("Bem vindo! Para começar responda as questões: \n")
qntd_rodas=int(input("Qual a quantidade de rodas do Veiculo? "))
peso_bruto=int(input("Qual o peso bruto aproximado do Veiculo em (Kg)? 'ex:1000.': "))
qntd_ocupantes=int(input("Qual a quantidade maxima de ocupantes no Veiculo? "))

if qntd_rodas <= 3 and qntd_ocupantes <=3:
    print("\nHabilitação necessaria para Veículos com duas ou três rodas é: 'A'.")
elif qntd_rodas == 4 and peso_bruto <= 3499 and qntd_ocupantes <= 8:
    print("\nHabilitação necessaria para Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg é: 'B'.")
elif qntd_rodas >= 4 and peso_bruto <= 5999 and qntd_ocupantes <= 8:
    print("\nHabilitação necessaria para Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg é: 'C'.")
elif qntd_rodas >= 4 and qntd_ocupantes > 8:
    print("\nHabilitação necessaria para Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas é: 'D'.")
else:
    print("\nHabilitação necessaria para Veículos com quatro rodas ou mais e com mais de 6000 kg é: 'E'.")
