# UM MÊS DE AULA, POUCAS AULAS DE PYTHON E ALGORITMOS... TERMINADO DIA 02/03/2019
# FOI UMA COMPETIÇÃO COM OUTRO ALUNO

# DEFINE A PALAVRA E PARÂMETROS
word = input("O que deve ser adivinhado? ") # DEFINE A PALAVRA
final = word # GUARDA A PALAVRA PRA MOSTRAR NO FINAL
word_list = list(word)
full = 19 # MÁXIMO DE CARACTERES, MENOS 1... AQUI TEM QUE TER O MESMO NÚMERO DE ESPAÇOS QUE O FIELD
fill = len(word)-1 # CONTA QUANTOS CARACTERES TEM... -1, PRA INCLUIR O 0
fill0 = len(word)-1 # NÚMERO ORIGINAL DE CARACTERES... -1 PRA INCLUIR O 0
miss = 0 # É A CONTAGEM DE ERROS
miss_check = 0 # É A CORREÇÃO DA CONTAGEM DE ERROS
fig1 = " " # CABEÇA
fig2 = " " # CORPO
fig3 = " " # BRAÇO
fig4 = " " # BRAÇO
fig5 = " " # PERNA
fig6 = " " # PERNA
check = ["_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ "]
        # PALAVRA ESCRITA EM LISTA... AQUI TEM QUE TER O TANTO DE FULL
field = ["_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ "]
        # MESMA COISA, MAS PARA MOSTRAR

while(full > fill): # SOME COM OS ESPAÇOS NÃO UTILIZADOS
    check[full] = ""
    full -= 1
full = 19
while(full > fill):
    field[full] = ""
    full -= 1

while(fill != -1): # ESCREVE AS LETRAS NOS ESPAÇOS CORRETOS PARA CONFERÊNCIA
    check[fill] = word_list[fill]
    fill -= 1
fill = fill0

# JOGO PROPRIAMENTE DITO
while(miss != 6):
    # MOSTRA OS CAMPOS
    print("+-+")
    print("| {:s} ".format(fig1))
    print("|{:s}{:s}{:s}".format(fig3, fig2, fig4))
    print("|{:s} {:s}".format(fig5, fig6))
    print("|")
    print("---- \n")
    print(*field) # PRINTA A LISTA COMO STRING

    # ESCOLHE LETRA
    choice = input("\nQual letra você chuta? ")
    while(fill != -1): # CHECAR EM CADA ESPAÇO SE TEM A LETRA
        if(check[fill] == choice): # SE SIM, SUBSTITUIR
            field[fill] = choice
            fill -= 1
        else: # SE NÃO, CORREÇÃO DA CONTAGEM DE ERROS +1
            miss_check += 1
            fill -= 1
    if(miss_check > fill0): # SE PASSOU POR TODOS E NÃO ACHOU A LETRA
        miss += 1

    miss_check = 0 # RESETA PARA REPETIR
    fill = fill0 # RESETA PARA REPETIR

    # DESENHA O ERRO
    if (miss == 1):
        fig1 = "O"
    if (miss == 2):
        fig2 = "|"
    if (miss == 3):
        fig3 = "/"
    if (miss == 4):
        fig4 = "\ "
    if (miss == 5):
        fig5 = "/"
    if (miss == 6):
        fig6 = "\ "


    # CHECA VITÓRIA
    if(field == check):
        print("Parabéns, você adivinou {:s}!!".format(final))
        exit(print("Pressione ENTER para sair."))

# DERROTA
print("+-+")
print("| {:s} ".format(fig1))
print("|{:s}{:s}{:s}".format(fig3,fig2,fig4))
print("|{:s} {:s}".format(fig5,fig6))
print("|")
print("----")
print("Oh, não!! Você perdeu!!")
