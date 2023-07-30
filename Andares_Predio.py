#Desafio 08
#
#Precisamos imprimir um número para cada andar de um hotel de 20 andares.
#Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
#
#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.
#
#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

print("Seja bem vindo ao Hotel!\n")
print("A sequencia abaixo imprime os andares do predio que irá visitar: \n")
print("**Sequência utilizando laço 'For'.**\n")

andar = 20

for andar in range(20):
    andar = andar + 1
    if (andar == 13):
        continue
    print(str(andar) + "° Andar")

print("\nEm seguida a sequencia inververtada de andares: \n")

for andar in range((andar), 0, -1):
    if (andar == 13):
        continue
    print(str(andar) + "° Andar")

print("\n**Sequência utilizando laço 'While'.**\n")
print("A sequencia abaixo imprime os andares do predio que irá visitar: \n")

andar=0
while andar < 20:
    andar += 1

    if andar == 13:
        continue

    print(str(andar) + "° Andar")


