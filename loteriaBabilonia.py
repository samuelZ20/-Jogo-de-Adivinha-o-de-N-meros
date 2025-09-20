#CONSTRUA UM PROGRAMA QUE REALIZA O SORTEIO DE UM NUMERO ENTRE 1 E 15
#O USUARIO TERÁ 3 CHANCES DE ACERTAR O VALOR
#A CADA TENTATIVA VOCE DEVE INFORMAR SE O CHUTE E MAIOR OU MENOR QUE O NUMERO SORTEADO
#CASO O USUARIO ACERTE, DE OS PARABENS

import random

def get_input():
    
    while True:
        try:
            numero_usuario = input("Entre com um número: ")
            numero_usuario= int(numero_usuario)

        except ValueError as err:
            print("Valor inválido")
            continue

        if 1 <= numero_usuario <= 15:
            return numero_usuario

        print("O valor deve ser entre 1 e 15")


def check_numbers(numero_sorteio, numero_usuario):
    if numero_sorteio == numero_usuario:
        print("Parabéns!Você é o ganhador da Loteria da Babilônia!!!") 
        return True

    elif numero_usuario > numero_sorteio:
         print("Numero muito alto, tente um menor!")
         return False

    else:
        print("Numero muito baixo. Tente um numero maior!")
        return False


numero_sorteio = random.randint(1,15)

for i in range(3):
    
    numero_usuario = get_input()

    if check_numbers(numero_sorteio=numero_sorteio, numero_usuario=numero_usuario):
        break

else:
    print("Suas tentativas acabaram!")
    