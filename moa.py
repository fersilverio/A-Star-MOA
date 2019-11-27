import copy

#Representação do Nó(vértice)
class No:
    def __init__(self):
        tabuleiro = []
        custo_g = 0
        custo_h = 0
        pai = None

#Representações dos conjuntos A e F
conj_A = list()
conj_F = list()


#Implementação das heurísticas

def h1(tabuleiro):
    peca_fora_lugar = 0
    peca_atual = 0
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j] == peca_atual:
                peca_atual += 1
            else:
                peca_fora_lugar += 1
                peca_atual += 1 
    return peca_fora_lugar


def h2(tabuleiro):
    seq_fora_lugar = 0
    aux = list()
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            aux.append(tabuleiro[i][j])
    for i in range(0,(len(aux) - 1)):
        if aux[i + 1] != aux[i] + 1:
            if aux[i] == 0:
                continue
            else:
                seq_fora_lugar += 1    
    return seq_fora_lugar



def pos(elem,aux):
    for i in range(len(aux)):
        for j in range(len(aux)):
            if elem == aux[i][j]:
                return i,j


# 5 1 2 3 9 6 7 4 13 10 11 8 0 14 15 12 ----> manhattan = 12

def h3(tabuleiro):
    m_aux = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]
    manhattan = 0
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j] != m_aux[i][j]:
                x1,y1 = i,j
                x2,y2 = pos(m_aux[i][j],tabuleiro)
                manhattan += abs(x1 - x2) + abs(y1 - y2)
    return manhattan



def h4(tabuleiro,p1,p2,p3):
    return (p1 * h1(tabuleiro)) + (p2 * h2(tabuleiro)) + (p3 * h3(tabuleiro))


def h5(tabuleiro):
    return max(h1(tabuleiro),h2(tabuleiro),h3(tabuleiro))


def pos_sucessoras(tabuleiro):
    i,j = pos(0,tabuleiro)
    aux = list()
    if i == 0:
        if j == 0:
            aux.append(tabuleiro[i][j + 1])
            aux.append(tabuleiro[i - 1][j])
        elif j == 3:
            aux.append(tabuleiro[i][j - 1])
            aux.append(tabuleiro[i - 1][j])
        else:
            aux.append(tabuleiro[i + 1][j])
            aux.append(tabuleiro[i][j + 1])
            aux.append(tabuleiro[i][j - 1])
    elif i == 3:
        if j == 0:
            aux.append(tabuleiro[i + 1][j])
            aux.append(tabuleiro[i][j + 1])
        elif j == 3:
            aux.append(tabuleiro[i + 1][j])
            aux.append(tabuleiro[i][j - 1])
        else:
            aux.append(tabuleiro[i + 1][j])
            aux.append(tabuleiro[i][j + 1])
            aux.append(tabuleiro[i][j - 1])
    else:
        aux.append(tabuleiro[i + 1][j])
        aux.append(tabuleiro[i - 1][j])
        aux.append(tabuleiro[i][j + 1])
        aux.append(tabuleiro[i][j - 1])
    return aux

def geraSucessores(tabuleiro,aux):
    i,j = pos(0,tabuleiro)
    sucessores = list()
    for k in range(len(aux)):
        a,b = pos(aux[k],tabuleiro)
        m_auxiliar = copy.deepcopy(tabuleiro)
        m_auxiliar[i][j],m_auxiliar[a][b] = m_auxiliar[a][b],m_auxiliar[i][j]
        sucessores.append(m_auxiliar)
    return sucessores
        

def main ():
    node = No()
    m_tabuleiro = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    print('Digitar os valores da matriz do tabuleiro: ')
    for i in range(0,4):
        for j in range(0,4):
            m_tabuleiro[i][j] = int(input())
    node.tabuleiro = m_tabuleiro
    k = geraSucessores(m_tabuleiro,pos_sucessoras(m_tabuleiro))
    for i in k:
        print(i)




main()





