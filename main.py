import networkx as nx
import matplotlib.pyplot as plt
from treelib import Node, Tree

# Criacao da classe no representando um estado da torre de londres associado a um custo/heuristica
class No:
    def __init__(self, no, custo):
        self.no = no
        self.custo = custo

# Criacao de um grafo direcionado
DG = nx.DiGraph()

# Adicionando 36 nos ao grafo direcionado representando os 36 estados possiveis da torre de londres
for i in range(36):
    DG.add_node(i+1)

# Adicionando as arestas do grafo: (no , noDestino , regra de transicao utilizada)
# Na primeira linha, por exemplo, temos o "Estado 1" da torre de londres que a partir da regra de transicao "1"
# Atinge o "Estado 3" da torre de londres
DG.add_weighted_edges_from([(1, 3, 1)])
DG.add_weighted_edges_from([(1, 2, 2)])
DG.add_weighted_edges_from([(2, 11, 1)])
DG.add_weighted_edges_from([(2, 1, 5)])
DG.add_weighted_edges_from([(2, 3, 6)])
DG.add_weighted_edges_from([(3, 4, 1)])
DG.add_weighted_edges_from([(3, 35, 2)])
DG.add_weighted_edges_from([(3, 1, 3)])
DG.add_weighted_edges_from([(3, 2, 4)])
DG.add_weighted_edges_from([(4, 36, 2)])
DG.add_weighted_edges_from([(4, 3, 3)])
DG.add_weighted_edges_from([(4, 35, 4)])
DG.add_weighted_edges_from([(5, 36, 1)])
DG.add_weighted_edges_from([(5, 26, 3)])
DG.add_weighted_edges_from([(5, 33, 5)])
DG.add_weighted_edges_from([(5, 6, 6)])
DG.add_weighted_edges_from([(6, 34, 2)])
DG.add_weighted_edges_from([(6, 33, 3)])
DG.add_weighted_edges_from([(6, 5, 4)])
DG.add_weighted_edges_from([(7, 9, 1)])
DG.add_weighted_edges_from([(7, 8, 2)])
DG.add_weighted_edges_from([(8, 35, 1)])
DG.add_weighted_edges_from([(8, 7, 5)])
DG.add_weighted_edges_from([(8, 9, 6)])
DG.add_weighted_edges_from([(9, 10, 1)])
DG.add_weighted_edges_from([(9, 11, 2)])
DG.add_weighted_edges_from([(9, 7, 3)])
DG.add_weighted_edges_from([(9, 8, 4)])
DG.add_weighted_edges_from([(10, 18, 2)])
DG.add_weighted_edges_from([(10, 9, 3)])
DG.add_weighted_edges_from([(10, 11, 4)])
DG.add_weighted_edges_from([(11, 12, 1)])
DG.add_weighted_edges_from([(11, 2, 3)])
DG.add_weighted_edges_from([(11, 9, 5)])
DG.add_weighted_edges_from([(11, 10, 6)])
DG.add_weighted_edges_from([(12, 11, 3)])
DG.add_weighted_edges_from([(12, 16, 5)])
DG.add_weighted_edges_from([(13, 15, 1)])
DG.add_weighted_edges_from([(13, 14, 2)])
DG.add_weighted_edges_from([(14, 23, 1)])
DG.add_weighted_edges_from([(14, 13, 5)])
DG.add_weighted_edges_from([(14, 15, 6)])
DG.add_weighted_edges_from([(15, 16, 1)])
DG.add_weighted_edges_from([(15, 17, 2)])
DG.add_weighted_edges_from([(15, 13, 3)])
DG.add_weighted_edges_from([(15, 14, 4)])
DG.add_weighted_edges_from([(16, 12, 2)])
DG.add_weighted_edges_from([(16, 15, 3)])
DG.add_weighted_edges_from([(16, 17, 4)])
DG.add_weighted_edges_from([(17, 18, 1)])
DG.add_weighted_edges_from([(17, 20, 3)])
DG.add_weighted_edges_from([(17, 15, 5)])
DG.add_weighted_edges_from([(17, 16, 6)])
DG.add_weighted_edges_from([(18, 17, 3)])
DG.add_weighted_edges_from([(18, 10, 5)])
DG.add_weighted_edges_from([(19, 21, 1)])
DG.add_weighted_edges_from([(19, 20, 2)])
DG.add_weighted_edges_from([(20, 17, 1)])
DG.add_weighted_edges_from([(20, 19, 5)])
DG.add_weighted_edges_from([(20, 21, 6)])
DG.add_weighted_edges_from([(21, 22, 1)])
DG.add_weighted_edges_from([(21, 23, 2)])
DG.add_weighted_edges_from([(21, 19, 3)])
DG.add_weighted_edges_from([(21, 20, 4)])
DG.add_weighted_edges_from([(22, 30, 2)])
DG.add_weighted_edges_from([(22, 21, 3)])
DG.add_weighted_edges_from([(22, 23, 4)])
DG.add_weighted_edges_from([(23, 24, 1)])
DG.add_weighted_edges_from([(23, 14, 3)])
DG.add_weighted_edges_from([(23, 21, 5)])
DG.add_weighted_edges_from([(23, 22, 6)])
DG.add_weighted_edges_from([(24, 23, 3)])
DG.add_weighted_edges_from([(24, 28, 5)])
DG.add_weighted_edges_from([(25, 27, 1)])
DG.add_weighted_edges_from([(25, 26, 2)])
DG.add_weighted_edges_from([(26, 5, 1)])
DG.add_weighted_edges_from([(26, 25, 5)])
DG.add_weighted_edges_from([(26, 27, 6)])
DG.add_weighted_edges_from([(27, 28, 1)])
DG.add_weighted_edges_from([(27, 29, 2)])
DG.add_weighted_edges_from([(27, 25, 3)])
DG.add_weighted_edges_from([(27, 26, 4)])
DG.add_weighted_edges_from([(28, 24, 2)])
DG.add_weighted_edges_from([(28, 27, 3)])
DG.add_weighted_edges_from([(28, 29, 4)])
DG.add_weighted_edges_from([(29, 30, 1)])
DG.add_weighted_edges_from([(29, 32, 3)])
DG.add_weighted_edges_from([(29, 27, 5)])
DG.add_weighted_edges_from([(29, 28, 6)])
DG.add_weighted_edges_from([(30, 29, 3)])
DG.add_weighted_edges_from([(30, 22, 5)])
DG.add_weighted_edges_from([(31, 33, 1)])
DG.add_weighted_edges_from([(31, 32, 2)])
DG.add_weighted_edges_from([(32, 29, 1)])
DG.add_weighted_edges_from([(32, 31, 5)])
DG.add_weighted_edges_from([(32, 33, 6)])
DG.add_weighted_edges_from([(33, 6, 1)])
DG.add_weighted_edges_from([(33, 5, 2)])
DG.add_weighted_edges_from([(33, 31, 3)])
DG.add_weighted_edges_from([(33, 32, 4)])
DG.add_weighted_edges_from([(34, 35, 3)])
DG.add_weighted_edges_from([(34, 6, 5)])
DG.add_weighted_edges_from([(35, 34, 1)])
DG.add_weighted_edges_from([(35, 8, 3)])
DG.add_weighted_edges_from([(35, 3, 5)])
DG.add_weighted_edges_from([(35, 4, 6)])
DG.add_weighted_edges_from([(36, 5, 3)])
DG.add_weighted_edges_from([(36, 4, 5)])

# Funcao para printar cada iteracao das buscas em largura e profundidade
def printIteracao(estadoAtual, abertos, fechados, iteracao, fila = 0, solucao = 0):
    print("ITERACAO:", iteracao)
    if (solucao == 0):
        print("Novo Estado Atual:", estadoAtual)
    else:
        print("Novo Estado Atual:", estadoAtual, "(Estado Objetivo e fim da busca)")
    if (fila != 0):
        print("Fila:", fila)
    print("Abertos:", abertos)
    print("Fechados:", fechados, "\n")

# Funcao para printar o caminho solucao
def printCaminhoSolucao(caminhoSolucao, i = 0):
    # Print dos estados
    print("Caminho Solucao:", end=" ")
    for estado in caminhoSolucao:
        if (estado == caminhoSolucao[len(caminhoSolucao)-1]):
            print(estado)
        else:
            print(estado, end=" -> ")
    print("Numero de movimentos do caminho solucao:", (len(caminhoSolucao)-1))
    if i != 0:
        print("Numero de iteracoes:", i, "\n")

# Funcao que retorna o caminho solucao (raiz -> ... -> folha) dado a arvore de busca e o estado destino
def retornaCaminhoSolucao(tree, estadoDestino):
    indexDoCaminho = None
    # Retorna uma lista contendo listas dos caminhos da arvore para cada no folha
    caminhos = tree.paths_to_leaves()
    # Passa por cada lista de caminhos e descobre o index da lista com o caminho solucao
    for index in range(len(caminhos)):
        caminho = caminhos[index]
        if (caminho[len(caminho)-1] == estadoDestino):
            indexDoCaminho = index
    # Atribuicao do caminho solucao
    caminhoSolucao = caminhos[indexDoCaminho]
    
    return caminhoSolucao

# Funcao que insere na arvore os filhos validos do estado atual da busca
def insereFilhosNaArvore(tree, filhosDoEstadoAtual, estadoAtual):
    for estado in filhosDoEstadoAtual:
        tree.create_node(estado, estado, estadoAtual)

# Funcao que gera como filhos do estado atual apenas estados validos e os retorna
def retornaEstadosFilhoValidos(filhosDoEstadoAtual, listaDeFechadosAbertos):
    for estado in listaDeFechadosAbertos:
        if estado in filhosDoEstadoAtual:
            filhosDoEstadoAtual.remove(estado)

    return filhosDoEstadoAtual

# Retorna uma lista dos filhos de um estado aplicando-se as regras de transicao possiveis
def retornaSucessores(DG, no):
    listaSucessores = list(DG.successors(no))
    listaRegrasTransicao = []
    for i in listaSucessores:
        listaRegrasTransicao.append(DG.edges[no, i]['weight'])
    
    return listaSucessores, listaRegrasTransicao

# BUSCA EM LARGURA
def buscaLargura(DG, noInicial, noDestino):
    print("-----"*20)
    print("BUSCA EM LARGURA:", "Estado inicial:", noInicial, "/ Estado destino:", noDestino, "\n")
    fila = []
    abertos = []
    fechados = []
    tree = Tree()
    tree.create_node(noInicial, noInicial)
    abertos.append(noInicial)
    fila.append(noInicial)
    i = 1

    # Enquanto existir vertices na lista de abertos
    while(len(abertos) != 0):
        # Primeiro da fila de abertos como estado atual
        estadoAtual = abertos[0]

        # Sucesso
        if (estadoAtual == noDestino):
            printIteracao(estadoAtual, abertos, fechados, i, [], 1)
            printCaminhoSolucao(retornaCaminhoSolucao(tree, estadoAtual), i)
            tree.show()
            return estadoAtual, fechados, abertos, len(fechados), tree
        else:
            # Geracao dos filhos do estado atual com tecnica de poda
            filhosDoEstadoAtual, regrasDeTransicaoAplicadas = retornaSucessores(DG, estadoAtual)
            filhosDoEstadoAtual = retornaEstadosFilhoValidos(filhosDoEstadoAtual, fechados)
            filhosDoEstadoAtual = retornaEstadosFilhoValidos(filhosDoEstadoAtual, abertos)
            # Atualiza fila
            fila = filhosDoEstadoAtual
            # Print da iteracao: estado atual, fila de abertos, fila de fechados, iteracao, fila
            printIteracao(estadoAtual, abertos, fechados, i, fila)
            # Insere os filhos validos do estado atual na arvore
            insereFilhosNaArvore(tree, filhosDoEstadoAtual, estadoAtual)
            # Atualiza fila de abertos com os filhos validos do estado atual
            abertos.extend(filhosDoEstadoAtual)
            # Retira-se estado atual da fila de abertos e coloca na lista de fechados
            abertos.remove(estadoAtual)
            fechados.append(estadoAtual)
            i += 1

    return False

# BUSCA EM PROFUNDIDADE
def buscaProfundidade(DG, noInicial, noDestino):
    print("-----"*20)
    print("BUSCA EM PROFUNDIDADE:", "Estado inicial:", noInicial, "/ Estado destino:", noDestino, "\n")
    abertos = []
    fechados = []
    tree = Tree()
    tree.create_node(noInicial, noInicial)
    abertos.append(noInicial)
    i = 1

    # Enquanto existir vertices na pilha de abertos
    while(len(abertos) != 0):
        # Topo da pilha de abertos como estado atual
        estadoAtual = abertos[(len(abertos)-1)]

        # Sucesso
        if (estadoAtual == noDestino):
            printIteracao(estadoAtual, abertos, fechados, i, 0, 1)
            printCaminhoSolucao(retornaCaminhoSolucao(tree, estadoAtual), i)
            tree.show()
            return estadoAtual, fechados, abertos, len(fechados), tree
        else:
            # Geracao dos filhos do estado atual com tecnica de poda
            filhosDoEstadoAtual, regrasDeTransicaoAplicadas = retornaSucessores(DG, estadoAtual)
            filhosDoEstadoAtual = retornaEstadosFilhoValidos(filhosDoEstadoAtual, fechados)
            filhosDoEstadoAtual = retornaEstadosFilhoValidos(filhosDoEstadoAtual, abertos)
            # Print da iteracao: estado atual, pilha de abertos, pilha de fechados, iteracao
            printIteracao(estadoAtual, abertos, fechados, i)
            # Insere os filhos validos do estado atual na arvore
            insereFilhosNaArvore(tree, filhosDoEstadoAtual, estadoAtual)
            # Atualiza pilha de abertos com os filhos validos do estado atual
            abertos.extend(filhosDoEstadoAtual)
            # Retira-se o estado atual da pilha de abertos e coloca na pilha de fechados
            abertos.remove(estadoAtual)
            fechados.append(estadoAtual)
            i += 1

    return False

################## FUNÇÕES EXCLUSIVAS DA PARTE 2 DO TRABALHO ##################

# Dado um estado destino, calcula e retorna as heuristicas de cada estado da busca gulosa
def retornaHeuristica(DG, estadoDestino):
    estadosOrdenadosHeuristica = [None] * 36
    heuristica = nx.single_target_shortest_path_length(DG, estadoDestino)
    for key, value in heuristica:
        estadosOrdenadosHeuristica[key-1] = value
    return estadosOrdenadosHeuristica

# Funcao que recebe uma lista de estados e seus custos ou heuristicas
# E cria-se uma lista de classes No para cada estado de forma ordenada
def retornaListaDeNos(estados, custosOuHeuristicas):
    listaNos = []
    for estado in estados:
        novoNo = No(estado, custosOuHeuristicas[estado-1])
        listaNos.append(novoNo)
    listaNos.sort(key = lambda x: x.custo)
    return listaNos

# Ordena lista de Nos com base no custo / heuristica
def ordenaListaDeNos(listaNos):
    listaNos.sort(key = lambda x: x.custo)

# Funcao para printar uma lista de nos da forma: Estado(custo) ou Estado(heuristica)
def printListaNos(listaNos):
    print("[", end="")
    for no in listaNos:
        if (no == listaNos[len(listaNos)-1]):
            print("{}({})".format(no.no, no.custo), end="")
        else:
            print("{}({}), ".format(no.no, no.custo), end="")
    print("]")

# Print das iteracoes nas buscas em que se usa a Classe No (listas compostas pela Classe No representando cada estado)
def printIteracaoComListaDeNos(estadoAtual, abertos, fechados, iteracao, fila = 0, solucao = 0):
    print("ITERACAO:", iteracao)
    if (solucao == 0):
        print("Estado Atual:", estadoAtual)
    else:
        print("Estado Atual:", estadoAtual, "(Estado Objetivo e fim da busca)")
    if (fila != 0):
        print("Fila:", end="")
        printListaNos(fila)
    print("Abertos:", end="")
    printListaNos(abertos)
    print("Fechados:", end="")
    printListaNos(fechados)
    print('')

# Funcao que gera como filhos do estado atual apenas estados validos e os retorna
def retornaEstadosFilhoValidosComListaDeNos(filhosDoEstadoAtual, listaDeNosFechadosAbertos):
    for estado in listaDeNosFechadosAbertos:
        if estado.no in filhosDoEstadoAtual:
            filhosDoEstadoAtual.remove(estado.no)

    return filhosDoEstadoAtual

# Funcao para atualizar o custo dos filhos (descendo o caminho da arvore de busca)
def atualizaCustosDosFilhos(nosFila, custoDoPai):
    for filho in nosFila:
        filho.custo += custoDoPai

# Funcao que gera como filhos do estado atual apenas estados validos com base no custo e lista de abertos (tecnica de poda)
def tecnicaDePodaComRelacaoAoCustoDosFilhos(nosFila, listaDeNosAbertos):
    for noEstado in listaDeNosAbertos:
        for noFila in nosFila:
            if noEstado.no == noFila.no and noFila.custo >= noEstado.custo:
                nosFila.remove(noFila)

# Funcao que insere na arvore os nos de filhos validos do estado atual da busca informando tambem seus custos
def insereNosFilhosNaArvore(tree, nosFila, estadoAtual):
    for estado in nosFila:
        tree.create_node("{}({})".format(estado.no, estado.custo), "{}({})".format(estado.no, estado.custo), "{}({})".format(estadoAtual.no, estadoAtual.custo))

# Funcao que retorna o caminho solucao (raiz -> ... -> folha) dado a arvore de busca composta por nos e o no do estado destino
def retornaCaminhoSolucaoDeNos(tree, noEstadoDestino):
    indexDoCaminho = None
    # Retorna uma lista contendo listas dos caminhos da arvore para cada no folha
    caminhos = tree.paths_to_leaves()
    # Passa por cada lista de caminhos e descobre o index da lista com o caminho solucao
    for index in range(len(caminhos)):
        caminho = caminhos[index]
        if (caminho[len(caminho)-1] == "{}({})".format(noEstadoDestino.no, noEstadoDestino.custo)):
            indexDoCaminho = index
    # Atribuicao do caminho solucao
    caminhoSolucao = caminhos[indexDoCaminho]
    
    return caminhoSolucao

# Funcao que retorna o custo de um caminho na arvore da raiz ao estado enviado por parâmetro
def retornaCustoDoCaminhoDeNos(tree, no, custos):
    indexDoCaminho = None
    # Retorna uma lista contendo listas dos caminhos da arvore para cada no folha
    caminhos = tree.paths_to_leaves()
    # Passa por cada lista de caminhos e descobre o index da lista com o caminho da raiz ateh o no
    for index in range(len(caminhos)):
        caminho = caminhos[index]
        if (caminho[len(caminho)-1] == "{}({})".format(no.no, no.custo)):
            indexDoCaminho = index
    # Atribuicao do caminho solucao
    caminhoNoEmString = caminhos[indexDoCaminho]
    caminhoNoInteiros = []
    for no in caminhoNoEmString:
        a = no.split('(')
        caminhoNoInteiros.append(int(a[0]))

    custoDoCaminho = 0
    for no in caminhoNoInteiros:
        custoDoCaminho += custos[no-1]

    return custoDoCaminho

# Printa o custo real do caminho solucao para busca ordenada e A*
def printCustoCaminhoSolucao(estadoSolucao):
    a = estadoSolucao.split('(')
    custoSolucao = int(a[1].replace(")", ""))
    print("Custo do Caminho Solucao:", custoSolucao)

# BUSCA ORDENADA
def buscaOrdenada(DG, noInicial, noDestino, custos):
    print("-----"*20)
    print("BUSCA ORDENADA:", "Estado inicial:", noInicial, "/ Estado destino:", noDestino, "\n")
    abertos = []
    tree = Tree()
    tree.create_node("{}({})".format(noInicial, 0), "{}({})".format(noInicial, 0))
    abertos.append(noInicial)
    # Criando listas de nos: abertos, fechados, fila
    nosAbertos = retornaListaDeNos(abertos, custos)
    nosFechados = []
    nosFila = nosAbertos
    i = 1

    # Enquanto existir vertices na lista de abertos
    while(len(nosAbertos) != 0):
        # Primeiro da fila de abertos como estado atual
        noAtual = nosAbertos[0]

        # Sucesso
        if (noAtual.no == noDestino):
            printIteracaoComListaDeNos(noAtual.no, nosAbertos, nosFechados, i, [], 1)
            caminhoSolucaoDeNos = retornaCaminhoSolucaoDeNos(tree, noAtual)
            printCustoCaminhoSolucao(caminhoSolucaoDeNos[len(caminhoSolucaoDeNos)-1])
            printCaminhoSolucao(caminhoSolucaoDeNos, i)
            tree.show()
            return noAtual.no, nosFechados, nosAbertos, len(nosFechados), tree
        else:
            # Geracao dos filhos do estado atual
            filhosDoEstadoAtual, regrasDeTransicaoAplicadas = retornaSucessores(DG, noAtual.no)
            filhosDoEstadoAtual = retornaEstadosFilhoValidosComListaDeNos(filhosDoEstadoAtual, nosFechados)
            nosFilhosDoEstadoAtual = retornaListaDeNos(filhosDoEstadoAtual, custos)
            # Atualiza fila
            nosFila = nosFilhosDoEstadoAtual
            atualizaCustosDosFilhos(nosFila, noAtual.custo)
            tecnicaDePodaComRelacaoAoCustoDosFilhos(nosFila, nosAbertos)
            # Print da iteracao: estado atual, fila de abertos, fila de fechados, iteracao, fila
            printIteracaoComListaDeNos(noAtual.no, nosAbertos, nosFechados, i, nosFila)
            # Insere os filhos validos do estado atual na arvore
            insereNosFilhosNaArvore(tree, nosFila, noAtual)
            # Retira-se estado atual da fila de abertos e coloca na lista de fechados
            nosAbertos.pop(0)
            nosFechados.append(noAtual)
            # Atualiza fila de abertos com os filhos validos do estado atual
            nosAbertos.extend(nosFila)
            ordenaListaDeNos(nosAbertos)
            i += 1

    return False

# BUSCA GULOSA
def buscaGulosa(DG, noInicial, noDestino, heuristicas):
    print("-----"*20)
    print("BUSCA GULOSA:", "Estado inicial:", noInicial, "/ Estado destino:", noDestino, "\n")
    abertos = []
    tree = Tree()
    tree.create_node(noInicial, noInicial)
    abertos.append(noInicial)
    # Criando listas de nos: abertos, fechados, fila
    nosAbertos = retornaListaDeNos(abertos, heuristicas)
    nosFechados = []
    nosFila = nosAbertos
    heuristica = heuristicas[noInicial-1]
    i = 1

    # Enquanto existir vertices na lista de abertos
    while(len(nosAbertos) != 0):
        # Primeiro da fila de abertos como estado atual
        noAtual = nosAbertos[0]

        # Sucesso
        if (noAtual.no == noDestino):
            printIteracaoComListaDeNos(noAtual.no, nosAbertos, nosFechados, i, [], 1)
            print("Heuristica da Busca Gulosa:", heuristica)
            printCaminhoSolucao(retornaCaminhoSolucao(tree, noAtual.no), i)
            tree.show()
            return noAtual.no, nosFechados, nosAbertos, len(nosFechados), tree
        else:
            # Geracao dos filhos do estado atual com tecnica de poda
            filhosDoEstadoAtual, regrasDeTransicaoAplicadas = retornaSucessores(DG, noAtual.no)
            filhosDoEstadoAtual = retornaEstadosFilhoValidosComListaDeNos(filhosDoEstadoAtual, nosFechados)
            filhosDoEstadoAtual = retornaEstadosFilhoValidosComListaDeNos(filhosDoEstadoAtual, nosAbertos)
            nosFilhosDoEstadoAtual = retornaListaDeNos(filhosDoEstadoAtual, heuristicas)
            # Atualiza fila
            nosFila = nosFilhosDoEstadoAtual
            # Print da iteracao: estado atual, fila de abertos, fila de fechados, iteracao, fila
            printIteracaoComListaDeNos(noAtual.no, nosAbertos, nosFechados, i, nosFila)
            # Insere os filhos validos do estado atual na arvore
            insereFilhosNaArvore(tree, filhosDoEstadoAtual, noAtual.no)
            # Retira-se estado atual da fila de abertos e coloca na lista de fechados
            nosAbertos.pop(0)
            nosFechados.append(noAtual)
            # Atualiza fila de abertos com os filhos validos do estado atual
            nosAbertos.extend(nosFilhosDoEstadoAtual)
            ordenaListaDeNos(nosAbertos)
            i += 1

    return False

def buscaAEstrela(DG, noInicial, noDestino, custosHeuristicas, custos):
    print("-----"*20)
    print("BUSCA A*:", "Estado inicial:", noInicial, "/ Estado destino:", noDestino, "\n")
    abertos = []
    tree = Tree()
    tree.create_node("{}({})".format(noInicial, custosHeuristicas[noInicial-1]), "{}({})".format(noInicial, custosHeuristicas[noInicial-1]))
    abertos.append(noInicial)
    # Criando listas de nos: abertos, fechados, fila
    nosAbertos = retornaListaDeNos(abertos, custosHeuristicas)
    nosFechados = []
    nosFila = nosAbertos
    i = 1

    # Enquanto existir vertices na lista de abertos
    while(len(nosAbertos) != 0):
        # Primeiro da fila de abertos como estado atual
        noAtual = nosAbertos[0]

        # Sucesso
        if (noAtual.no == noDestino):
            printIteracaoComListaDeNos(noAtual.no, nosAbertos, nosFechados, i, [], 1)
            caminhoSolucaoDeNos = retornaCaminhoSolucaoDeNos(tree, noAtual)
            printCustoCaminhoSolucao(caminhoSolucaoDeNos[len(caminhoSolucaoDeNos)-1])
            printCaminhoSolucao(caminhoSolucaoDeNos, i)
            tree.show()
            return noAtual.no, nosFechados, nosAbertos, len(nosFechados), tree
        else:
            # Geracao dos filhos do estado atual
            filhosDoEstadoAtual, regrasDeTransicaoAplicadas = retornaSucessores(DG, noAtual.no)
            filhosDoEstadoAtual = retornaEstadosFilhoValidosComListaDeNos(filhosDoEstadoAtual, nosFechados)
            nosFilhosDoEstadoAtual = retornaListaDeNos(filhosDoEstadoAtual, custosHeuristicas)
            # Atualiza fila
            nosFila = nosFilhosDoEstadoAtual
            custoDoCaminho = retornaCustoDoCaminhoDeNos(tree, noAtual, custos)
            atualizaCustosDosFilhos(nosFila, custoDoCaminho)
            tecnicaDePodaComRelacaoAoCustoDosFilhos(nosFila, nosAbertos)
            # Print da iteracao: estado atual, fila de abertos, fila de fechados, iteracao, fila
            printIteracaoComListaDeNos(noAtual.no, nosAbertos, nosFechados, i, nosFila)
            # Insere os filhos validos do estado atual na arvore
            insereNosFilhosNaArvore(tree, nosFila, noAtual)
            # Retira-se estado atual da fila de abertos e coloca na lista de fechados
            nosAbertos.pop(0)
            nosFechados.append(noAtual)
            # Atualiza fila de abertos com os filhos validos do estado atual
            nosAbertos.extend(nosFila)
            ordenaListaDeNos(nosAbertos)
            i += 1

    return False

NO_INICIAL = 33

menu_opcoes = {
    1: 'Trabalho 1: Busca em Largura / Busca em Profundidade',
    2: 'Trabalho 2: Busca Ordenada / Busca Gulosa / Busca A*',
    3: 'Sair do Programa'
}

menu_trabalho_1 = {
    1: 'Executar Busca em Largura',
    2: 'Executar Busca em Profundidade',
    3: 'Voltar'
}

menu_trabalho_2 = {
    1: 'Executar Busca Ordenada',
    2: 'Executar Busca Gulosa',
    3: 'Executar Busca A*',
    4: 'Voltar'
}

def chamaBuscaLargura():
    # BUSCA LARGURA
    estadoDestino = int(input("Digite um estado destino (1, ..., 36): "))
    buscaLargura(DG, NO_INICIAL, estadoDestino)

def chamaBuscaProfundidade():
    # BUSCA PROFUNDIDADE
    estadoDestino = int(input("Digite um estado destino (1, ..., 36): "))
    buscaProfundidade(DG, NO_INICIAL, estadoDestino)

def chamaBuscaOrdenada():
    # BUSCA ORDENADA
    custos = []
    estadoDestino = 0
    problemaDaBusca = int(input("Escolha um dos problemas da Torre de Londres (1, ..., 15): "))
    if problemaDaBusca == 1:
        custos = [6, 4, 3, 2, 1, 3, 6, 4, 4, 4, 3, 4, 6, 4, 4, 4, 2, 3, 6, 3, 4, 3, 3, 4, 6, 3, 4, 4, 3, 3, 6, 4, 0, 3, 2, 1]
        estadoDestino = 36
    elif problemaDaBusca == 2:
        custos = [6, 3, 4, 4, 2, 3, 6, 4, 4, 4, 2, 3, 6, 4, 4, 4, 3, 4, 6, 4, 3, 3, 2, 3, 5, 3, 2, 2, 0, 2, 5, 2, 0, 4, 3, 4]
        estadoDestino = 29
    elif problemaDaBusca == 3:
        custos = [6, 4, 4, 4, 2, 3, 5, 3, 3, 4, 3, 4, 6, 4, 4, 4, 3, 4, 6, 4, 3, 3, 2, 3, 4, 2, 1, 2, 1, 3, 5, 3, 0, 4, 3, 4]
        estadoDestino = 27
    elif problemaDaBusca == 4:
        custos = [4, 2, 1, 2, 2, 3, 5, 3, 3, 3, 2, 4, 6, 4, 4, 4, 3, 4, 5, 3, 3, 4, 3, 4, 6, 4, 4, 4, 3, 4, 6, 4, 0, 3, 1, 3]
        estadoDestino = 3
    elif problemaDaBusca == 5:
        custos = [4, 2, 1, 2, 2, 3, 5, 3, 3, 3, 2, 4, 6, 4, 4, 4, 3, 4, 5, 3, 3, 4, 3, 4, 6, 4, 4, 4, 3, 4, 6, 4, 0, 3, 1, 3]
        estadoDestino = 3
    elif problemaDaBusca == 6:
        custos = [6, 4, 4, 3, 3, 4, 6, 4, 4, 4, 3, 4, 5, 3, 3, 3, 2, 4, 5, 3, 2, 1, 1, 3, 6, 4, 3, 3, 2, 2, 6, 4, 0, 4, 3, 3]
        estadoDestino = 22
    elif problemaDaBusca == 7:
        custos = [5, 3, 3, 3, 3, 4, 4, 1, 2, 3, 2, 4, 6, 3, 4, 4, 3, 4, 6, 4, 4, 4, 2, 3, 5, 3, 3, 4, 3, 4, 6, 4, 0, 3, 1, 4]
        estadoDestino = 8
    elif problemaDaBusca == 8:
        custos = [6, 4, 4, 4, 3, 4, 6, 3, 4, 3, 3, 4, 6, 3, 4, 4, 3, 3, 6, 4, 3, 3, 1, 1, 6, 4, 3, 2, 2, 3, 6, 4, 0, 3, 2, 4]
        estadoDestino = 24
    elif problemaDaBusca == 9:
        custos = [3, 2, 2, 3, 3, 4, 5, 3, 3, 3, 2, 4, 6, 4, 4, 4, 3, 4, 5, 3, 3, 4, 3, 4, 6, 4, 4, 4, 3, 4, 5, 4, 0, 4, 2, 4]
        estadoDestino = 1
    elif problemaDaBusca == 10:
        custos = [5, 3, 3, 3, 3, 4, 3, 2, 2, 3, 2, 3, 5, 4, 4, 4, 3, 4, 6, 4, 4, 4, 3, 4, 5, 3, 3, 4, 3, 4, 6, 4, 0, 4, 2, 4]
        estadoDestino = 7
    elif problemaDaBusca == 11:
        custos = [5, 3, 3, 4, 3, 4, 6, 4, 4, 4, 3, 4, 5, 3, 3, 3, 2, 3, 4, 2, 1, 2, 1, 3, 6, 4, 3, 3, 2, 3, 6, 4, 0, 4, 3, 4]
        estadoDestino = 21
    elif problemaDaBusca == 12:
        custos = [6, 4, 4, 4, 3, 4, 6, 3, 4, 4, 3, 4, 5, 2, 3, 3, 2, 4, 5, 3, 2, 2, 0, 2, 6, 4, 3, 3, 2, 3, 6, 4, 0, 3, 2, 4]
        estadoDestino = 23
    elif problemaDaBusca == 13:
        custos = [6, 4, 4, 4, 1, 3, 5, 3, 3, 4, 3, 4, 6, 4, 4, 4, 2, 3, 6, 3, 4, 4, 3, 4, 4, 1, 2, 3, 2, 4, 5, 3, 0, 4, 3, 3]
        estadoDestino = 26
    elif problemaDaBusca == 14:
        custos = [5, 3, 3, 3, 3, 4, 4, 2, 1, 2, 1, 3, 6, 4, 3, 3, 2, 3, 6, 4, 4, 4, 3, 4, 5, 3, 3, 4, 3, 4, 6, 4, 0, 4, 2, 4]
        estadoDestino = 9
    else:
        custos = [6, 4, 4, 4, 3, 4, 6, 3, 4, 4, 3, 4, 4, 1, 2, 3, 2, 4, 5, 3, 3, 3, 1, 3, 6, 4, 4, 4, 3, 4, 5, 3, 0, 3, 2, 3]
        estadoDestino = 14
    buscaOrdenada(DG, NO_INICIAL, estadoDestino, custos)

def chamaBuscaGulosa():
    # BUSCA GULOSA
    estadoDestino = int(input("Digite um estado destino (1, ..., 36): "))
    heuristicas = retornaHeuristica(DG, estadoDestino)
    buscaGulosa(DG, NO_INICIAL, estadoDestino, heuristicas)

def chamaBuscaAEstela():
    # BUSCA A*
    custos = []
    estadoDestino = 0
    problemaDaBusca = int(input("Escolha um dos problemas da Torre de Londres (1, ..., 15): "))
    if problemaDaBusca == 1:
        custos = [6, 4, 3, 2, 1, 3, 6, 4, 4, 4, 3, 4, 6, 4, 4, 4, 2, 3, 6, 3, 4, 3, 3, 4, 6, 3, 4, 4, 3, 3, 6, 4, 0, 3, 2, 1]
        estadoDestino = 36
    elif problemaDaBusca == 2:
        custos = [6, 3, 4, 4, 2, 3, 6, 4, 4, 4, 2, 3, 6, 4, 4, 4, 3, 4, 6, 4, 3, 3, 2, 3, 5, 3, 2, 2, 0, 2, 5, 2, 0, 4, 3, 4]
        estadoDestino = 29
    elif problemaDaBusca == 3:
        custos = [6, 4, 4, 4, 2, 3, 5, 3, 3, 4, 3, 4, 6, 4, 4, 4, 3, 4, 6, 4, 3, 3, 2, 3, 4, 2, 1, 2, 1, 3, 5, 3, 0, 4, 3, 4]
        estadoDestino = 27
    elif problemaDaBusca == 4:
        custos = [4, 2, 1, 2, 2, 3, 5, 3, 3, 3, 2, 4, 6, 4, 4, 4, 3, 4, 5, 3, 3, 4, 3, 4, 6, 4, 4, 4, 3, 4, 6, 4, 0, 3, 1, 3]
        estadoDestino = 3
    elif problemaDaBusca == 5:
        custos = [4, 2, 1, 2, 2, 3, 5, 3, 3, 3, 2, 4, 6, 4, 4, 4, 3, 4, 5, 3, 3, 4, 3, 4, 6, 4, 4, 4, 3, 4, 6, 4, 0, 3, 1, 3]
        estadoDestino = 3
    elif problemaDaBusca == 6:
        custos = [6, 4, 4, 3, 3, 4, 6, 4, 4, 4, 3, 4, 5, 3, 3, 3, 2, 4, 5, 3, 2, 1, 1, 3, 6, 4, 3, 3, 2, 2, 6, 4, 0, 4, 3, 3]
        estadoDestino = 22
    elif problemaDaBusca == 7:
        custos = [5, 3, 3, 3, 3, 4, 4, 1, 2, 3, 2, 4, 6, 3, 4, 4, 3, 4, 6, 4, 4, 4, 2, 3, 5, 3, 3, 4, 3, 4, 6, 4, 0, 3, 1, 4]
        estadoDestino = 8
    elif problemaDaBusca == 8:
        custos = [6, 4, 4, 4, 3, 4, 6, 3, 4, 3, 3, 4, 6, 3, 4, 4, 3, 3, 6, 4, 3, 3, 1, 1, 6, 4, 3, 2, 2, 3, 6, 4, 0, 3, 2, 4]
        estadoDestino = 24
    elif problemaDaBusca == 9:
        custos = [3, 2, 2, 3, 3, 4, 5, 3, 3, 3, 2, 4, 6, 4, 4, 4, 3, 4, 5, 3, 3, 4, 3, 4, 6, 4, 4, 4, 3, 4, 5, 4, 0, 4, 2, 4]
        estadoDestino = 1
    elif problemaDaBusca == 10:
        custos = [5, 3, 3, 3, 3, 4, 3, 2, 2, 3, 2, 3, 5, 4, 4, 4, 3, 4, 6, 4, 4, 4, 3, 4, 5, 3, 3, 4, 3, 4, 6, 4, 0, 4, 2, 4]
        estadoDestino = 7
    elif problemaDaBusca == 11:
        custos = [5, 3, 3, 4, 3, 4, 6, 4, 4, 4, 3, 4, 5, 3, 3, 3, 2, 3, 4, 2, 1, 2, 1, 3, 6, 4, 3, 3, 2, 3, 6, 4, 0, 4, 3, 4]
        estadoDestino = 21
    elif problemaDaBusca == 12:
        custos = [6, 4, 4, 4, 3, 4, 6, 3, 4, 4, 3, 4, 5, 2, 3, 3, 2, 4, 5, 3, 2, 2, 0, 2, 6, 4, 3, 3, 2, 3, 6, 4, 0, 3, 2, 4]
        estadoDestino = 23
    elif problemaDaBusca == 13:
        custos = [6, 4, 4, 4, 1, 3, 5, 3, 3, 4, 3, 4, 6, 4, 4, 4, 2, 3, 6, 3, 4, 4, 3, 4, 4, 1, 2, 3, 2, 4, 5, 3, 0, 4, 3, 3]
        estadoDestino = 26
    elif problemaDaBusca == 14:
        custos = [5, 3, 3, 3, 3, 4, 4, 2, 1, 2, 1, 3, 6, 4, 3, 3, 2, 3, 6, 4, 4, 4, 3, 4, 5, 3, 3, 4, 3, 4, 6, 4, 0, 4, 2, 4]
        estadoDestino = 9
    else:
        custos = [6, 4, 4, 4, 3, 4, 6, 3, 4, 4, 3, 4, 4, 1, 2, 3, 2, 4, 5, 3, 3, 3, 1, 3, 6, 4, 4, 4, 3, 4, 5, 3, 0, 3, 2, 3]
        estadoDestino = 14
    heuristicas = retornaHeuristica(DG, estadoDestino)
    custosHeuristicasZip = zip(custos, heuristicas)
    custosHeuristicas = [x + y for (x, y) in custosHeuristicasZip]
    buscaAEstrela(DG, NO_INICIAL, estadoDestino, custosHeuristicas, custos)

def print_menu(menuOpcoes):
    for key in menuOpcoes.keys():
        print (key, '--', menuOpcoes[key] )

def menuTrabalho1():
    while(True):
        print("-"*10, "Menu Trabalho 1", "-"*10)
        print_menu(menu_trabalho_1)
        opcao = ''
        try:
            opcao = int(input('\nEscolha uma opcao: '))
            print("")
        except:
            print('Entrada errada. Por favor, digite um numero ...')
        if opcao == 1:
            chamaBuscaLargura()
        elif opcao == 2:
            chamaBuscaProfundidade()
        elif opcao == 3:
            break
        else:
            print('Opcao invalida. Por favor, digite um numero entre 1 e 3.\n')

def menuTrabalho2():
    while(True):
        print("-"*10, "Menu Trabalho 2", "-"*10)
        print_menu(menu_trabalho_2)
        opcao = ''
        try:
            opcao = int(input('\nEscolha uma opcao: '))
            print("")
        except:
            print('Entrada errada. Por favor, digite um numero ...')
        if opcao == 1:
            chamaBuscaOrdenada()
        elif opcao == 2:
            chamaBuscaGulosa()
        elif opcao == 3:
            chamaBuscaAEstela()
        elif opcao == 4:
            break
        else:
            print('Opcao invalida. Por favor, digite um numero entre 1 e 4.\n')

if __name__ == "__main__":
    while(True):
        print("-"*10, "Menu Principal", "-"*10)
        print_menu(menu_opcoes)
        opcao = ''
        try:
            opcao = int(input('\nEscolha uma opcao: '))
            print("")
        except:
            print('Entrada errada. Por favor, digite um numero ...')
        if opcao == 1:
            menuTrabalho1()
        elif opcao == 2:
            menuTrabalho2()
        elif opcao == 3:
            exit()
        else:
            print('Opcao invalida. Por favor, digite um numero entre 1 e 3.\n')

# subax1 = plt.subplot(121)
# nx.draw_shell(DG, nlist=[range(0, 5), range(5, 11), range(11, 17), range(17, 23), range(23, 30), range(30, 37)], with_labels=True, font_weight='bold')
# plt.show()