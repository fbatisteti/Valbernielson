# JOGO DA VELHA

import random

# DEFININDO OS JOGADORES E A ORDEM
player_X = input("Qual é o nome do jogador usando X? ")
player_O = input("Qual é o nome do jogador usando O? ")
coin_toss = random.randint(0,1)
if(coin_toss == 0):
    print("{:s} joga primeiro!".format(player_X))
    turn = 0
else:
    print("{:s} joga primeiro!".format(player_O))
    turn = 1

# DEFININDO OS NÚMEROS
c1 = 1
c2 = 2
c3 = 3
c4 = 4
c5 = 5
c6 = 6
c7 = 7
c8 = 8
c9 = 9
cX = "X"
cO = "@"

# MOSTRANDO O CAMPO
print("")
print(" ",c1," | ",c2," | ",c3," ")
print("-----+-----+-----")
print(" ",c4," | ",c5," | ",c6," ")
print("-----+-----+-----")
print(" ",c7," | ",c8," | ",c9," ")
print("")

# MOVIMENTO
if (turn == 0):
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_X)))
    if (choice == 1):
        c1 = cX
    elif (choice == 2):
        c2 = cX
    elif (choice == 3):
        c3 = cX
    elif (choice == 4):
        c4 = cX
    elif (choice == 5):
        c5 = cX
    elif (choice == 6):
        c6 = cX
    elif (choice == 7):
        c7 = cX
    elif (choice == 8):
        c8 = cX
    elif (choice == 9):
        c9 = cX

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()

    turn = 1
else:
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_O)))
    if (choice == 1):
        c1 = cO
    elif (choice == 2):
        c2 = cO
    elif (choice == 3):
        c3 = cO
    elif (choice == 4):
        c4 = cO
    elif (choice == 5):
        c5 = cO
    elif (choice == 6):
        c6 = cO
    elif (choice == 7):
        c7 = cO
    elif (choice == 8):
        c8 = cO
    elif (choice == 9):
        c9 = cO

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()

    turn = 0

# MOSTRANDO O CAMPO
print("")
print(" ",c1," | ",c2," | ",c3," ")
print("-----+-----+-----")
print(" ",c4," | ",c5," | ",c6," ")
print("-----+-----+-----")
print(" ",c7," | ",c8," | ",c9," ")
print("")

# MOVIMENTO
if (turn == 0):
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_X)))
    if (choice == 1):
        c1 = cX
    elif (choice == 2):
        c2 = cX
    elif (choice == 3):
        c3 = cX
    elif (choice == 4):
        c4 = cX
    elif (choice == 5):
        c5 = cX
    elif (choice == 6):
        c6 = cX
    elif (choice == 7):
        c7 = cX
    elif (choice == 8):
        c8 = cX
    elif (choice == 9):
        c9 = cX

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()

    turn = 1
else:
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_O)))
    if (choice == 1):
        c1 = cO
    elif (choice == 2):
        c2 = cO
    elif (choice == 3):
        c3 = cO
    elif (choice == 4):
        c4 = cO
    elif (choice == 5):
        c5 = cO
    elif (choice == 6):
        c6 = cO
    elif (choice == 7):
        c7 = cO
    elif (choice == 8):
        c8 = cO
    elif (choice == 9):
        c9 = cO

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()

    turn = 0

# MOSTRANDO O CAMPO
print("")
print(" ",c1," | ",c2," | ",c3," ")
print("-----+-----+-----")
print(" ",c4," | ",c5," | ",c6," ")
print("-----+-----+-----")
print(" ",c7," | ",c8," | ",c9," ")
print("")

# MOVIMENTO
if (turn == 0):
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_X)))
    if (choice == 1):
        c1 = cX
    elif (choice == 2):
        c2 = cX
    elif (choice == 3):
        c3 = cX
    elif (choice == 4):
        c4 = cX
    elif (choice == 5):
        c5 = cX
    elif (choice == 6):
        c6 = cX
    elif (choice == 7):
        c7 = cX
    elif (choice == 8):
        c8 = cX
    elif (choice == 9):
        c9 = cX

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()

    turn = 1
else:
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_O)))
    if (choice == 1):
        c1 = cO
    elif (choice == 2):
        c2 = cO
    elif (choice == 3):
        c3 = cO
    elif (choice == 4):
        c4 = cO
    elif (choice == 5):
        c5 = cO
    elif (choice == 6):
        c6 = cO
    elif (choice == 7):
        c7 = cO
    elif (choice == 8):
        c8 = cO
    elif (choice == 9):
        c9 = cO

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()

    turn = 0

# MOSTRANDO O CAMPO
print("")
print(" ",c1," | ",c2," | ",c3," ")
print("-----+-----+-----")
print(" ",c4," | ",c5," | ",c6," ")
print("-----+-----+-----")
print(" ",c7," | ",c8," | ",c9," ")
print("")

# MOVIMENTO
if (turn == 0):
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_X)))
    if (choice == 1):
        c1 = cX
    elif (choice == 2):
        c2 = cX
    elif (choice == 3):
        c3 = cX
    elif (choice == 4):
        c4 = cX
    elif (choice == 5):
        c5 = cX
    elif (choice == 6):
        c6 = cX
    elif (choice == 7):
        c7 = cX
    elif (choice == 8):
        c8 = cX
    elif (choice == 9):
        c9 = cX

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()

    turn = 1
else:
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_O)))
    if (choice == 1):
        c1 = cO
    elif (choice == 2):
        c2 = cO
    elif (choice == 3):
        c3 = cO
    elif (choice == 4):
        c4 = cO
    elif (choice == 5):
        c5 = cO
    elif (choice == 6):
        c6 = cO
    elif (choice == 7):
        c7 = cO
    elif (choice == 8):
        c8 = cO
    elif (choice == 9):
        c9 = cO

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()

    turn = 0

# MOSTRANDO O CAMPO
print("")
print(" ",c1," | ",c2," | ",c3," ")
print("-----+-----+-----")
print(" ",c4," | ",c5," | ",c6," ")
print("-----+-----+-----")
print(" ",c7," | ",c8," | ",c9," ")
print("")

# MOVIMENTO
if (turn == 0):
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_X)))
    if (choice == 1):
        c1 = cX
    elif (choice == 2):
        c2 = cX
    elif (choice == 3):
        c3 = cX
    elif (choice == 4):
        c4 = cX
    elif (choice == 5):
        c5 = cX
    elif (choice == 6):
        c6 = cX
    elif (choice == 7):
        c7 = cX
    elif (choice == 8):
        c8 = cX
    elif (choice == 9):
        c9 = cX

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()

    turn = 1
else:
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_O)))
    if (choice == 1):
        c1 = cO
    elif (choice == 2):
        c2 = cO
    elif (choice == 3):
        c3 = cO
    elif (choice == 4):
        c4 = cO
    elif (choice == 5):
        c5 = cO
    elif (choice == 6):
        c6 = cO
    elif (choice == 7):
        c7 = cO
    elif (choice == 8):
        c8 = cO
    elif (choice == 9):
        c9 = cO

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()

    turn = 0

# MOSTRANDO O CAMPO
print("")
print(" ",c1," | ",c2," | ",c3," ")
print("-----+-----+-----")
print(" ",c4," | ",c5," | ",c6," ")
print("-----+-----+-----")
print(" ",c7," | ",c8," | ",c9," ")
print("")

# MOVIMENTO
if (turn == 0):
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_X)))
    if (choice == 1):
        c1 = cX
    elif (choice == 2):
        c2 = cX
    elif (choice == 3):
        c3 = cX
    elif (choice == 4):
        c4 = cX
    elif (choice == 5):
        c5 = cX
    elif (choice == 6):
        c6 = cX
    elif (choice == 7):
        c7 = cX
    elif (choice == 8):
        c8 = cX
    elif (choice == 9):
        c9 = cX

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()

    turn = 1
else:
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_O)))
    if (choice == 1):
        c1 = cO
    elif (choice == 2):
        c2 = cO
    elif (choice == 3):
        c3 = cO
    elif (choice == 4):
        c4 = cO
    elif (choice == 5):
        c5 = cO
    elif (choice == 6):
        c6 = cO
    elif (choice == 7):
        c7 = cO
    elif (choice == 8):
        c8 = cO
    elif (choice == 9):
        c9 = cO

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()

    turn = 0

# MOSTRANDO O CAMPO
print("")
print(" ",c1," | ",c2," | ",c3," ")
print("-----+-----+-----")
print(" ",c4," | ",c5," | ",c6," ")
print("-----+-----+-----")
print(" ",c7," | ",c8," | ",c9," ")
print("")

# MOVIMENTO
if (turn == 0):
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_X)))
    if (choice == 1):
        c1 = cX
    elif (choice == 2):
        c2 = cX
    elif (choice == 3):
        c3 = cX
    elif (choice == 4):
        c4 = cX
    elif (choice == 5):
        c5 = cX
    elif (choice == 6):
        c6 = cX
    elif (choice == 7):
        c7 = cX
    elif (choice == 8):
        c8 = cX
    elif (choice == 9):
        c9 = cX

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()

    turn = 1
else:
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_O)))
    if (choice == 1):
        c1 = cO
    elif (choice == 2):
        c2 = cO
    elif (choice == 3):
        c3 = cO
    elif (choice == 4):
        c4 = cO
    elif (choice == 5):
        c5 = cO
    elif (choice == 6):
        c6 = cO
    elif (choice == 7):
        c7 = cO
    elif (choice == 8):
        c8 = cO
    elif (choice == 9):
        c9 = cO

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()

    turn = 0

# MOSTRANDO O CAMPO
print("")
print(" ",c1," | ",c2," | ",c3," ")
print("-----+-----+-----")
print(" ",c4," | ",c5," | ",c6," ")
print("-----+-----+-----")
print(" ",c7," | ",c8," | ",c9," ")
print("")

# MOVIMENTO
if (turn == 0):
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_X)))
    if (choice == 1):
        c1 = cX
    elif (choice == 2):
        c2 = cX
    elif (choice == 3):
        c3 = cX
    elif (choice == 4):
        c4 = cX
    elif (choice == 5):
        c5 = cX
    elif (choice == 6):
        c6 = cX
    elif (choice == 7):
        c7 = cX
    elif (choice == 8):
        c8 = cX
    elif (choice == 9):
        c9 = cX

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()

    turn = 1
else:
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_O)))
    if (choice == 1):
        c1 = cO
    elif (choice == 2):
        c2 = cO
    elif (choice == 3):
        c3 = cO
    elif (choice == 4):
        c4 = cO
    elif (choice == 5):
        c5 = cO
    elif (choice == 6):
        c6 = cO
    elif (choice == 7):
        c7 = cO
    elif (choice == 8):
        c8 = cO
    elif (choice == 9):
        c9 = cO

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()

    turn = 0

# MOSTRANDO O CAMPO
print("")
print(" ",c1," | ",c2," | ",c3," ")
print("-----+-----+-----")
print(" ",c4," | ",c5," | ",c6," ")
print("-----+-----+-----")
print(" ",c7," | ",c8," | ",c9," ")
print("")

# MOVIMENTO
if (turn == 0):
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_X)))
    if (choice == 1):
        c1 = cX
    elif (choice == 2):
        c2 = cX
    elif (choice == 3):
        c3 = cX
    elif (choice == 4):
        c4 = cX
    elif (choice == 5):
        c5 = cX
    elif (choice == 6):
        c6 = cX
    elif (choice == 7):
        c7 = cX
    elif (choice == 8):
        c8 = cX
    elif (choice == 9):
        c9 = cX

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_X,player_O))
        input()

    turn = 1
else:
    choice = int(input("{:s}, escolha a primeira marcação: ".format(player_O)))
    if (choice == 1):
        c1 = cO
    elif (choice == 2):
        c2 = cO
    elif (choice == 3):
        c3 = cO
    elif (choice == 4):
        c4 = cO
    elif (choice == 5):
        c5 = cO
    elif (choice == 6):
        c6 = cO
    elif (choice == 7):
        c7 = cO
    elif (choice == 8):
        c8 = cO
    elif (choice == 9):
        c9 = cO

    # CONDIÇÕES DE VITÓRIA
    if((c1 == c2) and (c2 == c3)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c4 == c5) and (c5 == c6)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c7 == c8) and (c8 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c4) and (c4 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c2 == c5) and (c5 == c8)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c6) and (c6 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c1 == c5) and (c5 == c9)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()
    if((c3 == c5) and (c5 == c7)):
        print("Parabéns, {:s}, você venceu de {:s}!!".format(player_O,player_X))
        input()

    turn = 0

# MOSTRANDO O CAMPO
print("")
print(" ",c1," | ",c2," | ",c3," ")
print("-----+-----+-----")
print(" ",c4," | ",c5," | ",c6," ")
print("-----+-----+-----")
print(" ",c7," | ",c8," | ",c9," ")
print("")

print("Deu velha!")