import copy


#Representação do Nó(vértice)
class No:
    def __init__(self):
        self.tabuleiro = []
        self.custo_g = 0 #custo que é incrementado 1 cada vez que é gerado um nivel na "arvore"
        self.custo_h = 0 #custo da heurística
        self.custo_f = 0 # f + g
        self.pai = None


#Funções auxiliares

def f_menor_valor(conj):
    menor = conj[0]
    for i in range(len(conj)):
        if conj[i].custo_f <= menor.custo_f:
            menor = conj[i]
    return menor

def pos(elem,aux):
    for i in range(len(aux)):
        for j in range(len(aux)):
            if elem == aux[i][j]:
                return i,j

def pos_sucessoras(tabuleiro):
    i,j = pos(0,tabuleiro)
    aux = list()
    if i == 0:
        if j == 0:
            aux.append(tabuleiro[i][j + 1])
            aux.append(tabuleiro[i + 1][j])
        elif j == 3:
            aux.append(tabuleiro[i][j - 1])
            aux.append(tabuleiro[i + 1][j])
        else:
            aux.append(tabuleiro[i + 1][j])
            aux.append(tabuleiro[i][j + 1])
            aux.append(tabuleiro[i][j - 1])
    elif i == 3:
        if j == 0:
            aux.append(tabuleiro[i - 1][j])
            aux.append(tabuleiro[i][j + 1])
        elif j == 3:
            aux.append(tabuleiro[i - 1][j])
            aux.append(tabuleiro[i][j - 1])
        else:
            aux.append(tabuleiro[i - 1][j])
            aux.append(tabuleiro[i][j + 1])
            aux.append(tabuleiro[i][j - 1])
    else:
        if j == 0:
            aux.append(tabuleiro[i + 1][j])
            aux.append(tabuleiro[i - 1][j])
            aux.append(tabuleiro[i][j + 1])
        elif j == 3:
            aux.append(tabuleiro[i + 1][j])
            aux.append(tabuleiro[i - 1][j])
            aux.append(tabuleiro[i][j - 1])        
        else:
            aux.append(tabuleiro[i + 1][j])
            aux.append(tabuleiro[i - 1][j])
            aux.append(tabuleiro[i][j + 1])
            aux.append(tabuleiro[i][j - 1])
    return aux

def geraSucessores(v,aux):
    tabuleiro = v.tabuleiro
    i,j = pos(0,tabuleiro)
    sucessores = list()
    for k in range(len(aux)):
        a,b = pos(aux[k],tabuleiro)
        m_auxiliar = copy.deepcopy(tabuleiro)
        auxilio = m_auxiliar[i][j] 
        m_auxiliar[i][j] = m_auxiliar[a][b] 
        m_auxiliar[a][b] = auxilio

        no = No()
        no.tabuleiro = copy.deepcopy(m_auxiliar)
        no.custo_h = h1(no.tabuleiro)
        no.pai = v
        no.custo_g = v.custo_g + 1
        no.custo_f = no.custo_g + no.custo_h
        sucessores.append(no)
    return sucessores


def verifica_tabuleiros_iguais(tab_m,conj):
    for k in conj:
        if tab_m == k.tabuleiro:
            return True
    return False

def busca_elem(tabuleiro,conj):
    for k in conj:
        if tabuleiro == k.tabuleiro:
            return k

#Implementação das Heurísticas:

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
    p1,p2,p3 = 0.5,0.2,0.3
    return (p1 * h1(tabuleiro)) + (p2 * h2(tabuleiro)) + (p3 * h3(tabuleiro))

def h5(tabuleiro):
    return max(h1(tabuleiro),h2(tabuleiro),h3(tabuleiro))






#Implementação do A*
def a_star(inicial,final):
    conj_a = list()
    conj_f = list()
    conj_a.append(inicial)
    v = f_menor_valor(conj_a)
    sucessores = list()
    while len(conj_a) != 0 and v.tabuleiro != final.tabuleiro:
        conj_f.append(v)
        conj_a.remove(v)
        sucessores = geraSucessores(v,pos_sucessoras(v.tabuleiro))
        
        for m in sucessores:
            verificado = verifica_tabuleiros_iguais(m.tabuleiro,conj_a)
            if verificado == True:
                k = busca_elem(m.tabuleiro,conj_a)
                if m.custo_g < k.custo_g:
                    conj_a.remove(k)
            if m not in conj_a and m not in conj_f:
                conj_a.append(m)
        v = f_menor_valor(conj_a)
    if v.tabuleiro == final.tabuleiro:
        print(v.custo_g)
    else:
        print('Wrong')








def main():
    inicial = No()
    final = No()
    m_tabuleiro = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    
    print('Digitar os valores da matriz do tabuleiro: ')
    for i in range(0,4):
        for j in range(0,4):
            m_tabuleiro[i][j] = int(input())
    inicial.tabuleiro = m_tabuleiro
    final.tabuleiro = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]

    a_star(inicial,final)

    
    
 

if __name__ == '__main__':
    main()





    '''
    #Teste para ver se os sucessores vieram como nós
    
    
    suc = geraSucessores(inicial,pos_sucessoras(inicial.tabuleiro))
    
    for i in suc:
        print( 'Tipo do elemento: ' + str(type(i)))
        print('Tabuleiro: ' + str(i.tabuleiro))
        print('G: ' + str(i.custo_g))
        print('H: ' + str(i.custo_h))
        print('F: ' + str(i.custo_f))
        print('Tabuleiro pai: ' + str(i.pai.tabuleiro))
    '''













 