import networkx as nx
import matplotlib.pyplot as plt
import treelib
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
        print("Estado Atual:", estadoAtual)
    else:
        print("Estado Atual:", estadoAtual, "(Estado Objetivo e fim da busca)")
    if (fila != 0):
        print("Fila:", fila)
    print("Abertos:", abertos)
    print("Fechados:", fechados, "\n")

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

# obs: pode colocar um if se noDestino < 1 ou > 36
def buscaLargura(DG, noInicial, noDestino):
    fila = []
    abertos = []
    fechados = []
    tree = Tree()
    abertos.append(noInicial)
    fila.append(noInicial)
    tree.create_node(noInicial, noInicial)
    i = 1

    # Enquanto existir vertices na lista de abertos
    while(len(abertos) != 0):
        # Primeiro da fila de abertos como estado atual
        estadoAtual = abertos[0]

        # Sucesso
        if (estadoAtual == noDestino):
            printIteracao(estadoAtual, abertos, fechados, i, [], 1)
            return estadoAtual, fechados, abertos, len(fechados), tree
        else:
            # Geracao dos filhos do estado atual com tecnica de poda
            filhosDoEstadoAtual, regrasDeTransicaoAplicadas = retornaSucessores(DG, estadoAtual)
            filhosDoEstadoAtual = retornaEstadosFilhoValidos(filhosDoEstadoAtual, fechados)
            filhosDoEstadoAtual = retornaEstadosFilhoValidos(filhosDoEstadoAtual, abertos)
            # Atualiza fila
            fila = filhosDoEstadoAtual
            # Print da interacao: estado atual, fila de abertos, fila de fechados, iteracao, fila
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

def buscaProfundidade(DG, noInicial, noDestino):
    abertos = []
    fechados = []
    abertos.append(noInicial)

    # Enquanto existir vertices na pilha de abertos
    while(len(abertos) != 0):
        # Topo da pilha de abertos como estado atual
        estadoAtual = abertos[(len(abertos)-1)]

        # Sucesso
        if (estadoAtual == noDestino):
            return estadoAtual, fechados, abertos, len(fechados)
        else:
            # Geracao dos filhos do estado atual com tecnica de poda
            filhosDoEstadoAtual, regrasDeTransicaoAplicadas = retornaSucessores(DG, estadoAtual)
            filhosDoEstadoAtual = retornaEstadosFilhoValidos(filhosDoEstadoAtual, fechados)
            filhosDoEstadoAtual = retornaEstadosFilhoValidos(filhosDoEstadoAtual, abertos)
            # Atualiza pilha de abertos com os filhos validos do estado atual
            abertos.extend(filhosDoEstadoAtual)
            # Retira-se o estado atual da pilha de abertos e coloca na pilha de fechados
            abertos.remove(estadoAtual)
            fechados.append(estadoAtual)

    return False

def buscaOrdenada(DG, noInicial, noDestino):
    pass

def buscaGulosa(DG, noInicial, noDestino):
    pass

def buscaAEstrela(DG, noInicial, noDestino):
    pass

NO_INICIAL = 33

# tree = buscaLargura(DG, NO_INICIAL, 36)[4]
# print(tree.paths_to_leaves())
# print(buscaProfundidade(DG, NO_INICIAL, 20))

# print(nx.shortest_path(DG, 13, 36))
# Heuristica para o estado destino 36
heuristica = nx.single_target_shortest_path_length(DG, 36)
for key, value in heuristica:
    print(key, '-->', value)




# print(list(DG.successors(1)))
# print(DG.edges[1, 3]['weight'])
# print(DG.edges[1, 2]['weight'])

# if __name__ == "__main__":

# print(DG.out_degree(1, weight='weight'))

# subax1 = plt.subplot(121)
# nx.draw_shell(DG, nlist=[range(0, 5), range(5, 11), range(11, 17), range(17, 23), range(23, 30), range(30, 37)], with_labels=True, font_weight='bold')
# plt.show()