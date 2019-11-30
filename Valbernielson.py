import pickle
import datetime

def periodo(data, comeco, fim):
    dataComeco = datetime.datetime(1, 1, 1)
    dataFim = datetime.datetime(9999, 12, 31)
    dataPedido = datetime.datetime(1, 1, 1)

    if comeco != 0:
        dataComeco = datetime.datetime(comeco%10000, (comeco//10000)%100, comeco//1000000)

    if fim != 0:
        dataFim = datetime.datetime(fim%10000, (fim//10000)%100, fim//1000000)

    aux1, aux2 = data.split(" ")
    dia, mes, ano = aux1.split("/")
    dataPedido = datetime.datetime(int(ano), int(mes), int(dia))

    if (dataPedido >= dataComeco) and (dataPedido <= dataFim):
        return True
    else:
        return False

def mostrarMenu():
    id = menu["id"]
    nome = menu["item"]
    preco = menu["preco"]

    tamanho = len(id)

    print("---+----------------------+--------"
          "\n # | NOME", " "*15, "| PREÇO"
          "\n---+----------------------+--------")
    for i in range(1, tamanho):
        if nome[i] != "-":
            print("{:>2} | {:<20} | $ {:>5.2f}".format(id[i], nome[i], preco[i]))
    print("---+----------------------+--------")

def mostrarClientes():
    id = clientes["id"]
    nome = clientes["nome"]
    telefone = clientes["telefone"]
    endereco = clientes["endereco"]
    numero = clientes["numero"]

    tamanho = len(id)

    print("----+----------------------------------------+-----------------+--------------------------------------------------"
          "\n ID | NOME", " "*33, "|    TELEFONE     | ENDEREÇO", " "*41,
          "\n----+----------------------------------------+-----------------+--------------------------------------------------")
    for i in range(1, tamanho):
        print("{:>3} | {:<38} | {:>15} | {}, {}".format(id[i], nome[i], telefone[i], endereco[i], numero[i]))
    print("----+----------------------------------------+-----------------+--------------------------------------------------")

def mostrarStatus():
    id = pedido["id"]
    cliente = pedido["cliente"]
    nomes = clientes["nome"]
    data = pedido["data"]
    preparo = pedido["preparo"]
    entrega = pedido["entrega"]
    fechado = pedido["fechado"]
    cancelado = pedido["cancelado"]

    tamanho = len(id)

    print("-------+----------------------------------------+----------------+------------------"
          "\nPEDIDO | CLIENTE", " "*30, "| DATA DE INCLUSÃO | STATUS"
          "\n-------+----------------------------------------+----------------+------------------")
    for i in range(1, tamanho):
        if cancelado[i] == True:
            status = "CANCELADO"
        elif fechado[i] == True:
            status = "PEDIDO ENTREGUE"
        elif entrega[i] == True:
            status = "SAIU PARA ENTREGA"
        elif preparo[i] == True:
            status = "SENDO PREPARADO"
        else:
            status = "AGUARDANDO"

        nome = nomes[cliente[i]]

        print("{:>6} | {:<38} | {:18} | {}".format(id[i], nome, data[i], status))
    print("-------+----------------------------------------+----------------+------------------")

def mostrarFiltro(tipo,comeco,fim,buscado):
    id = pedido["id"]
    cliente = pedido["cliente"]
    nomes = clientes["nome"]
    data = pedido["data"]
    preparo = pedido["preparo"]
    entrega = pedido["entrega"]
    fechado = pedido["fechado"]
    cancelado = pedido["cancelado"]

    tamanho = len(id)

    print("-------+----------------------------------------+------------------+------------------"
          "\nPEDIDO | CLIENTE", " "*30, "|  DATA DE INCLUSÃO  | STATUS"
          "\n-------+----------------------------------------+------------------+------------------")
    for i in range(1, tamanho):
        if cancelado[i] == True:
            status = "CANCELADO"
        elif fechado[i] == True:
            status = "PEDIDO ENTREGUE"
        elif entrega[i] == True:
            status = "SAIU PARA ENTREGA"
        elif preparo[i] == True:
            status = "SENDO PREPARADO"
        else:
            status = "AGUARDANDO"

        nome = nomes[cliente[i]]

        if tipo == "aberto":
            if status != "PEDIDO ENTREGUE" and status != "CANCELADO" and periodo(data[i],comeco,fim):
                print("{:>6} | {:<38} | {:18} | {}".format(id[i], nome, data[i], status))

        if tipo == "preparo":
            if status == "SENDO PREPARADO" and periodo(data[i],comeco,fim):
                print("{:>6} | {:<38} | {:18} | {}".format(id[i], nome, data[i], status))

        if tipo == "entrega":
            if status == "SAIU PARA ENTREGA" and periodo(data[i],comeco,fim):
                print("{:>6} | {:<38} | {:18} | {}".format(id[i], nome, data[i], status))

        if tipo == "cancelado":
            if status == "CANCELADO" and periodo(data[i],comeco,fim):
                print("{:>6} | {:<38} | {:18} | {}".format(id[i], nome, data[i], status))

        if tipo == "todos" and periodo(data[i],comeco,fim):
            if nomes[buscado] == nome:
                print("{:>6} | {:<38} | {:18} | {}".format(id[i], nome, data[i], status))
    print("-------+----------------------------------------+------------------+------------------")

def mostrarPedido(id):
    itens = detalhes["itens"]
    qtd = detalhes["qtd"]
    parcial = detalhes["parcial"]
    total = detalhes["total"]
    nomes = menu["item"]
    cliente = clientes["nome"]
    fone = clientes["telefone"]
    endereco = clientes["endereco"]
    numero = clientes["numero"]

    itens = itens[id]
    qtd = qtd[id]
    parcial = parcial[id]

    tamanho = len(itens)

    print("-------+", "-"*40, "+", "-"*15,
          "\nPEDIDO | CLIENTE", " "*32, "| TELEFONE"
          "\n-------+", "-"*40, "+", "-"*15)
    print("{:>6} | {:<40} | {:>15}".format(id, cliente[pedido["cliente"][id]], fone[pedido["cliente"][id]]))
    print("-------+", "-"*40, "+", "-"*15)
    print("{}, {}".format(endereco[pedido["cliente"][id]], numero[pedido["cliente"][id]]))
    print("-"*67)

    for i in range(tamanho):
        print("{:>5}x {:<44} = $ {:>10.2f}".format(qtd[i], nomes[itens[i]], parcial[i]))
    print(" "*45, "TOTAL = $ {:>10.2f}".format(total[id]))

def salvarAlteracoes():
    pickle.dump(clientes, open("valbernielson_clientes.bin", "wb"))
    pickle.dump(menu, open("valbernielson_menu.bin", "wb"))
    pickle.dump(pedido, open("valbernielson_pedido.bin", "wb"))
    pickle.dump(detalhes, open("valbernielson_detalhes.bin", "wb"))

#-----------------------------------------------

def incluirCardapio():
    print("\n== Menu Principal == Cardápio == INCLUIR NOVO ITEM")
    print("-- Digite o nome do novo item e seu preço\n")

    item = input("Nome: ").upper()
    preco = float(input("Preço: "))

    aux = menu["id"]
    id = len(aux)
    aux.append(id)
    menu["id"] = aux

    aux = menu["item"]
    aux.append(item)
    menu["item"] = aux

    aux = menu["preco"]
    aux.append(preco)
    menu["preco"] = aux

    salvarAlteracoes()

    print("\nNovo item adicionado ao cardápio.")

def editarCardapio():
    print("\n== Menu Principal == Cardápio == EDITAR ITEM EXISTENTE")
    print("-- Escreva o número do item que deseja alterar o preço\n")

    mostrarMenu()

    procurar = int(input("\nAlterar qual item: "))
    itens = menu["id"]

    if procurar in itens:
        preco = float(input("Novo preço: "))

        posicao = 0
        for i in range(len(itens)):
            if itens[i] != procurar:
                posicao += 1
            else:
                break

        aux = menu["preco"]
        aux[posicao] = preco
        menu["preco"] = aux

        salvarAlteracoes()

        print("\nO valor de {} foi alterado.".format(procurar))

    else:
        print("\nItem não presente no cardápio.")

def removerCardapio():
    print("\n== Menu Principal == Cardápio == REMOVER ITEM EXISTENTE")
    print("-- Digite o número do item que deseja remover\n")

    mostrarMenu()

    procurar = int(input("\nRemover qual item: "))
    item = menu["id"]

    if procurar in item:
        confirma = input("Remover este item? [S/N] ").upper()

        if confirma == "S":
            posicao = 0
            for i in range(len(item)):
                if item[i] != procurar:
                    posicao += 1
                else:
                    break

            id = menu["id"]
            preco = menu["preco"]

            item[posicao] = "-"
            id[posicao] = "-"
            preco[posicao] = "-"

            menu["item"] = item
            menu["id"] = id
            menu["preco"] = preco

        salvarAlteracoes()

        print("\n{} foi removido do cardápio.".format(procurar))

    else:
        print("\nItem não presente no cardápio.")

def incluirCliente():
    print("\n== Menu Principal == Clientes == INCLUIR NOVO CLIENTE")
    print("-- Digite os dados conforme solicitado\n")

    novoNome = input("Nome: ").upper()
    novoTelefone = input("Telefone: ").upper()
    novoEndereco = input("Endereço (sem o número): ").upper()
    novoNumero = input("Número e complemento (se houver): ").upper()

    nome = clientes["nome"]
    nome.append(novoNome)
    clientes["nome"] = nome

    telefone = clientes["telefone"]
    telefone.append(novoTelefone)
    clientes["telefone"] = telefone

    endereco = clientes["endereco"]
    endereco.append(novoEndereco)
    clientes["endereco"] = endereco

    numero = clientes["numero"]
    numero.append(novoNumero)
    clientes["numero"] = numero

    id = clientes["id"]
    id.append(len(id))
    clientes["id"] = id

    salvarAlteracoes()

    print("\nNovo cliente adicionado ao cadastro.")

def editarCliente():
    print("\n== Menu Principal == Clientes == ALTERAR CADASTRO")
    print("-- Digite o número [ID] do cadastro que deseja alterar\n")

    mostrarClientes()

    procurar = int(input("Alterar qual cadatro: "))

    id = clientes["id"]

    if procurar in id:
        while True:
            escolha = int(input("\nO que deseja alterar?\n"
                                "1 - Nome\n"
                                "2 - Telefone\n"
                                "3 - Endereço\n"
                                "4 - Número e complemento\n"
                                "0 - Cancelar alteração\n"
                                "\nESCOLHA: "))
            if escolha == 1:
                novoNome = input("\nNovo nome: ").upper()

                nome = clientes["nome"]
                nome[procurar] = novoNome
                clientes["nome"] = nome

                print("\nCliente atualizado.")

            if escolha == 2:
                novoTelefone = input("\bNovo telefone: ").upper()

                telefone = clientes["telefone"]
                telefone[procurar] = novoTelefone
                clientes["telefone"] = telefone

                print("\nCliente atualizado.")

            if escolha == 3:
                novoEndereco = input("\bNovo endereço: ").upper()

                endereco = clientes["endereco"]
                endereco[procurar] = novoEndereco
                clientes["endereco"] = endereco

                print("\nCliente atualizado.")

            if escolha == 4:
                novoNumero = input("\bNovo número e complemento: ").upper()

                numero = clientes["numero"]
                numero[procurar] = novoNumero
                clientes["numero"] = numero

                print("\nCliente atualizado.")

            salvarAlteracoes()

            if escolha == 0:
                break
    else:
        print("\nID não encontrado no cadastro.")

def incluirPedido():
    print("\n== Menu Principal == Pedidos == FAZER NOVO PEDIDO")
    print("-- Digite os números dos itens e suas quantidades conforme solicitado\n")

    mostrarMenu()

    posicao = len(pedido["id"])

    pedidoItem = []
    pedidoQtd = []
    pedidoParcial = []
    while True:
        while True:
            adicionar = int(input("\nQual o número do item? "))
            qtd = int(input("Quantos? "))

            confirma = input("\nAdicionar ao pedido {}x {}? [S/N]".format(qtd, menu["item"][adicionar])).upper()
            if confirma == "S":
                break
        pedidoItem.append(adicionar)
        pedidoQtd.append(qtd)
        pedidoParcial.append(qtd * menu["preco"][adicionar])

        confirma = input("Adicionar mais itens? [S/N]").upper()
        if confirma == "N":
            break

    aux = detalhes["id"]
    aux.append(posicao)
    detalhes["id"] = aux

    aux = detalhes["itens"]
    aux.append(pedidoItem)
    detalhes["itens"] = aux

    aux = detalhes["qtd"]
    aux.append(pedidoQtd)
    detalhes["qtd"] = aux

    aux = detalhes["parcial"]
    aux.append(pedidoParcial)
    detalhes["parcial"] = aux

    aux = detalhes["total"]
    aux.append(sum(pedidoParcial))
    detalhes["total"] = aux

    cliente = int(input("\nQual seu código de cliente? "))

    aux = pedido["cliente"]
    aux.append(cliente)
    pedido["cliente"] = aux

    datahora = datetime.datetime.now()
    datahora = datahora.strftime("%d/%m/%Y %H:%M")
    aux = pedido["data"]
    aux.append(datahora)
    pedido["data"] = aux

    aux = pedido["preparo"]
    aux.append(False)
    pedido["preparo"] = aux

    aux = pedido["entrega"]
    aux.append(False)
    pedido["entrega"] = aux

    aux = pedido["fechado"]
    aux.append(False)
    pedido["fechado"] = aux

    aux = pedido["cancelado"]
    aux.append(False)
    pedido["cancelado"] = aux

    aux = pedido["id"]
    aux.append(posicao)
    pedido["id"] = aux

    salvarAlteracoes()

    print("\nPedido #{} registrado com sucesso".format(posicao))

def editarPedido():
    print("\n== Menu Principal == Pedidos == ALTERAR PEDIDO")
    print("-- Digite o número do pedido a ser alterado\n")

    mostrarStatus()

    alterar = int(input("\nQual pedido deseja alterar? "))

    pedidos = pedido["id"]

    if alterar in pedidos:
        print(" ")
        mostrarPedido(alterar)

        acao = int(input("\n1 - Refazer pedido\n"
                         "2 - Cancelar pedido\n"
                         "0 - Voltar ao menu anterior\n"
                         "\nESCOLHA: "))

        if acao == 1:
            aux = pedido["preparo"]
            if aux[alterar] == True:
                print("Este pedido já  preparado, saiu para entrega ou foi cancelado, e não pode ser alterado.")
            else:
                print(" ")
                mostrarMenu()

                # posicao = len(pedido["id"])

                pedidoItem = []
                pedidoQtd = []
                pedidoParcial = []
                while True:
                    while True:
                        adicionar = int(input("\nQual o número do item? "))
                        qtd = int(input("Quantos? "))

                        confirma = input(
                            "\nAdicionar ao pedido {}x {}? [S/N]".format(qtd, menu["item"][adicionar])).upper()
                        if confirma == "S":
                            break
                    pedidoItem.append(adicionar)
                    pedidoQtd.append(qtd)
                    pedidoParcial.append(qtd * menu["preco"][adicionar])

                    confirma = input("Adicionar mais itens? [S/N]").upper()
                    if confirma == "N":
                        break

                aux = detalhes["itens"]
                aux[alterar] = pedidoItem
                detalhes["itens"] = aux

                aux = detalhes["qtd"]
                aux[alterar] = pedidoQtd
                detalhes["qtd"] = aux

                aux = detalhes["parcial"]
                aux[alterar] = pedidoParcial
                detalhes["parcial"] = aux

                aux = detalhes["total"]
                aux[alterar] = sum(pedidoParcial)
                detalhes["total"] = aux

                print("\nPedido #{} refeito com sucesso".format(alterar))

        if acao == 2:
            confirma = input("Cancelar este pedido? [S/N] ").upper()

            if confirma == "S":
                aux = pedido["cancelado"]
                aux[alterar] = True
                pedido["cancelado"] = aux

            print("\nPedido #{} foi cancelado.".format(alterar))

        if acao == 0:
            print("")

        salvarAlteracoes()

    else:
        print("\nPedido não localizado.")

def atualizarPedido():
    print("\n== Menu Principal == Pedidos == ATUALIZAR ESTADO DE PEDIDO")
    print("-- Digite o número do pedido e confirme se estiver em ordem\n")

    mostrarStatus()

    atualizar = int(input("\nAlterar status de qual pedido? "))

    try:
        detalhe = pedido["cancelado"]
        if detalhe[atualizar] == True:
            print("\nPedido já cancelado. Não é possível alterar.")
        else:
            detalhe = pedido["preparo"]
            if detalhe[atualizar] == False:
                confirma = input("Confirmar começo do preparo? [S/N] ").upper()
                if confirma == "S":
                    aux = pedido["preparo"]
                    aux[atualizar] = True
                    pedido["preparo"] = aux
            else:
                detalhe = pedido["entrega"]
                if detalhe[atualizar] == False:
                    confirma = input("Confirmar saída para entrega? [S/N] ").upper()
                    if confirma == "S":
                        aux = pedido["entrega"]
                        aux[atualizar] = True
                        pedido["entrega"] = aux
                else:
                    detalhe = pedido["fechado"]
                    if detalhe[atualizar] == False:
                        confirma = input("Confirmar recebimento pelo cliente? [S/N] ").upper()
                        if confirma == "S":
                            aux = pedido["fechado"]
                            aux[atualizar] = True
                            pedido["fechado"] = aux
    except:
        print("\nAlgum erro aconteceu, tente novamente.")
    salvarAlteracoes()

def procurarPedido():
    print("\n== Menu Principal == Pedidos == EXIBIR PEDIDOS")
    print("-- Digite a exibição desejada\n")

    acao = int(input("1 - Todos os pedidos\n"
                     "2 - Filtrar pedidos\n"
                     "0 - Voltar ao menu anterior\n"
                     "\nESCOLHA: "))

    if acao == 1:
        print(" ")
        mostrarStatus()

    if acao == 2:
        filtro = int(input("1 - Pedidos em aberto\n"
                           "2 - Pedidos sendo preparados\n"
                           "3 - Pedidos sendo entregues\n"
                           "4 - Pedidos cancelados\n"
                           "5 - Pedidos de um cliente\n"
                           "6 - Detalhar pedido em específico\n"
                           "0 - Voltar ao menu anterior\n"
                           "\nESCOLHA: "))

        if filtro == 1:
            print("\n[Escreva só os números, no formato dd/mm/aaaa. Insira 0 para não definir uma data]")
            comeco = int(input("Data inicial (só números, formato dd/mm/aaaa): "))
            fim = int(input("Data final (só números, formato dd/mm/aaaa): "))
            print("")
            mostrarFiltro("aberto", comeco, fim, 0)

        if filtro == 2:
            print("\n[Escreva só os números, no formato dd/mm/aaaa. Insira 0 para não definir uma data]")
            comeco = int(input("Data inicial (só números, formato dd/mm/aaaa): "))
            fim = int(input("Data final (só números, formato dd/mm/aaaa): "))
            print("")
            mostrarFiltro("preparo", comeco, fim, 0)

        if filtro == 3:
            print("\n[Escreva só os números, no formato dd/mm/aaaa. Insira 0 para não definir uma data]")
            comeco = int(input("Data inicial (só números, formato dd/mm/aaaa): "))
            fim = int(input("Data final (só números, formato dd/mm/aaaa): "))
            print("")
            mostrarFiltro("entrega", comeco, fim, 0)

        if filtro == 4:
            print("\n[Escreva só os números, no formato dd/mm/aaaa. Insira 0 para não definir uma data]")
            comeco = int(input("Data inicial (só números, formato dd/mm/aaaa): "))
            fim = int(input("Data final (só números, formato dd/mm/aaaa): "))
            print("")
            mostrarFiltro("cancelado", comeco, fim, 0)

        if filtro == 5:
            print("\n[Escreva só os números, no formato dd/mm/aaaa. Insira 0 para não definir uma data]")
            comeco = int(input("Data inicial (só números, formato dd/mm/aaaa): "))
            fim = int(input("Data final (só números, formato dd/mm/aaaa): "))
            buscado = int(input("Qual o ID do cliente? "))

            aux = clientes["id"]
            if buscado > len(aux):
                print("\nCliente não localizado.")
            else:
                print("")
                mostrarFiltro("todos", comeco, fim, buscado)

        if filtro == 6:
            mostrar = int(input("\nQual o número do pedido para detalhar? "))

            pedidos = pedido["id"]

            if mostrar in pedidos:
                print(" ")
                mostrarPedido(mostrar)
            else:
                print("\nPedido não localizado.")

        if filtro == 0:
            print(" ")

    if acao == 0:
        print("")

clientes = {"id": [0],
            "nome": [0],
            "telefone": [0],
            "endereco": [0],
            "numero": [0]}

menu = {"id": [0],
        "item": [0],
        "preco": [0]}

pedido = {"id": [0],
          "cliente": [0],
          "data": [0],
          "preparo": [False],
          "entrega": [False],
          "fechado": [False],
          "cancelado": [True]}

detalhes = {"id": [0],
            "itens": [[0]],
            "qtd": [[0]],
            "parcial": [[0]],
            "total": [0]}

try:
    clientes = pickle.load(open("valbernielson_clientes.bin", "rb"))
    menu = pickle.load(open("valbernielson_menu.bin", "rb"))
    pedido = pickle.load(open("valbernielson_pedido.bin", "rb"))
    detalhes = pickle.load(open("valbernielson_Detalhes.bin", "rb"))
except:
    print("Primeira inicialização do programa."
          "\nAconselha-se preencher pelo menos um item no cadastro de clientes e no cardápio.")

while True:
    print("\n== MENU PRINCIPAL")
    print("-- Digite a opção desejada e pressione ENTER\n")

    opcao = int(input("1 - Acesso ao Cardápio\n"
                      "2 - Acesso ao Cadastro de Clientes\n"
                      "3 - Acesso aos Pedidos\n"
                      "0 - Sair do programa\n"
                      "\nESCOLHA: "))

    if opcao == 1:
        while True:
            print("\n== Menu Principal == CARDÁPIO")
            print("-- Digite a opção desejada e pressione ENTER\n")

            acao = int(input("1 - Incluir novo item ao cardápio\n"
                             "2 - Editar item existente\n"
                             "3 - Remover item do cardápio\n"
                             "4 - Exibir o cardápio\n"
                             "0 - Voltar ao menu anterior\n"
                             "\nESCOLHA: "))

            if acao == 1:
                incluirCardapio()

            if acao == 2:
                editarCardapio()

            if acao == 3:
                removerCardapio()

            if acao == 4:
                print(" ")
                mostrarMenu()

            if acao == 0:
                break

    if opcao == 2:
        while True:
            print("\n== Menu Principal == CLIENTES")
            print("-- Digite a opção desejada e pressione ENTER\n")

            acao = int(input("1 - Incluir novo cadastro de cliente\n"
                             "2 - Editar cadastro existente\n"
                             "3 - Exibir cadastro de clientes\n"
                             "0 - Voltar ao menu anterior\n"
                             "\nESCOLHA: "))
            if acao == 1:
                incluirCliente()

            if acao == 2:
                editarCliente()

            if acao == 3:
                print(" ")
                mostrarClientes()

            if acao == 0:
                break

    if opcao == 3:
        while True:
            print("\n== Menu Principal == PEDIDOS")
            print("-- Digite a opção desejada e pressione ENTER\n")

            acao = int(input("1 - Fazer novo pedido\n"
                             "2 - Alterar ou cancelar pedido\n"
                             "3 - Atualizar estado de pedido\n"
                             "4 - Exibir pedidos\n"
                             "0 - Voltar ao menu anterior\n"
                             "\nESCOLHA: "))

            if acao == 1:
                incluirPedido()

            if acao == 2:
                editarPedido()

            if acao == 3:
                atualizarPedido()

            if acao == 4:
                procurarPedido()

            if acao == 0:
                break

    if opcao == 0:
        salvarAlteracoes()
        exit()