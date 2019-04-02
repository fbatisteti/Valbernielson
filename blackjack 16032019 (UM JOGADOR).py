# UM MÊS E MEIO DE AULA, EU QUERIA QUE QUERIA FAZER UM JOGO DE 21... TERMINADO DIA 16/03/2019

import random

pick1 = 0
pick2 = 0
pick3 = 1
draw = 0
sum = 0

# CARTAS
# 0 CORINGA / 1 - 13 COPAS / 14 - 26 PAUS / 27 - 39 OUROS / 40 - 53 ESPADAS
card_face = ["Coringa","Ás de Copas","2 de Copas","3 de Copas","4 de Copas","5 de Copas","6 de Copas",
             "7 de Copas","8 de Copas","9 de Copas","10 de Copas","Valete de Copas","Rainha de Copas",
             "Rei de Copas","Ás de Paus","2 de Paus","3 de Paus","4 de Paus","5 de Paus","6 de Paus",
             "7 de Paus","8 de Paus","9 de Paus","10 de Paus","Valete de Paus","Rainha de Paus","Rei de Paus",
             "Ás de Ouros","2 de Ouros","3 de Ouros","4 de Ouros","5 de Ouros","6 de Ouros","7 de Ouros",
             "8 de Ouros","9 de Ouros","10 de Ouros","Valete de Ouros","Rainha de Ouros","Rei de Ouros",
             "Ás de Espadas","2 de Espadas","3 de Espadas","4 de Espadas","5 de Espadas","6 de Espadas",
             "7 de Espadas","8 de Espadas","9 de Espadas","10 de Espadas","Valete de Espadas","Rainha de Espadas",
             "Rei de Espadas"]
card_value = [0,11,2,3,4,5,6,7,8,9,10,10,10,10,
              11,2,3,4,5,6,7,8,9,10,10,10,10,
              11,2,3,4,5,6,7,8,9,10,10,10,10,
              11,2,3,4,5,6,7,8,9,10,10,10,10]
discard = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,0,0,0,0,0]
# CARTAS

print("Vamos testar a sorte!! \n\nVocê escolhe comprar uma carta ou encerrar. Chegue na soma de 21!"
      "\nSe passar de 21, você perde! Ás vale 1 ou 11, figuras valem 10.")

print()

player = input("Quem está jogando? ")

print()

while (pick1 == 0):  # COMPRA E CHECA SE É O CORINGA A PRIMEIRA CARTA
    pick1 = random.randint(0,53)
    if (card_value[pick1] == 0):
        pick1 = 0
sum += card_value[pick1]
card_value[pick1] = 0
discard[pick1] = 1

while (pick2 == 0):  # COMPRA E CHECA SE É O CORINGA A SEGUNDA CARTA
    pick2 = random.randint(0,53)
    if (card_value[pick2] == 0):
        pick2 = 0
if (pick2 == 1 or pick2 == 14 or pick2 == 27 or pick2 == 40): # CHECA O VALOR QUE O ÁS ASSUME
    if ((sum + card_value[pick2]) > 21):
        card_value[pick2] = 1
sum += card_value[pick2]
card_value[pick2] = 0
discard[pick2] = 1

print("{:s}, você comprou as cartas {:s} e {:s}.".format(player,card_face[pick1],card_face[pick2]))
print("Sua mão inicial soma {}.".format(sum))

print()

draw = input("Você quer comprar mais uma carta? S/N >>> ")
if (draw == "S"):
    pick3 = 0
else:
    print("Você desistiu...")

while (pick3 == 0):
    while (pick3 == 0):  # COMPRA CARTA
        pick3 = random.randint(0, 53)
        if (card_value[pick3] == 0):
            print("Você comprou o Coringa! Ele não vale pontos. Devolva-o ao baralho e compre outra carta.")
            pick3 = 0
    if (pick3 == 1 or pick3 == 14 or pick3 == 27 or pick3 == 40):  # CHECA O VALOR QUE O ÁS ASSUME
        if ((sum + card_value[pick3]) > 21):
            card_value[pick3] = 1
    sum += card_value[pick3]
    card_value[pick3] = 0
    discard[pick3] = 1

    print("{:s}, você comprou a carta {:s}.".format(player,card_face[pick3]))
    print("Suas cartas somam {}.".format(sum))

    print()

    if (sum > 21):  # VITÓRIA E DERROTA
        print("Você perdeu!! Suas cartas somam {}!".format(sum))
        exit()
    if (sum == 21):
        print("Parabéns!! Você venceu, somando {}!!".format(sum))
        exit()

    draw = input("Deseja comprar outra carta? S / N >>> ")  # COMPRAR NOVA CARTA?
    if (draw == "S"):
        pick3 = 0
    elif (draw == "N"):
        print("Você desistiu...")

    print()
