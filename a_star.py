import copy
import heapq


class No:
    def __init__(self):
        self.tabuleiro = []
        self.custo_g = 0 
        self.custo_h = 0 
        self.custo_f = 0 
        self.pai = None
    
    def __eq__(self, other):
        return self.tabuleiro == other.tabuleiro 
    
    def __lt__(self, other):
        return self.custo_f < other.custo_f
    
    def __hash__(self):
        return hash(str(self.tabuleiro))
    
   

def arr_int(entrada):
    arr = list()
    for i in range(len(entrada)):
        if entrada[i] != '':
            arr.append(int(entrada[i]))
    return arr

def gerar_vet_proximos(tabuleiro,est_final):
    prox_do_tab = list()
    prox_do_est_final = list()
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if i == 3 and j == 3:
                continue
            elif i < 3 and j == 3:
                prox_do_tab.append(tabuleiro[i + 1][0])
            else:
                prox_do_tab.append(tabuleiro[i][j + 1])
    for i in range(len(est_final)):
        for j in range(len(est_final)):
            if i == 3 and j == 3:
                continue
            elif i < 3 and j == 3:
                prox_do_est_final.append(est_final[i + 1][0])
            else:
                prox_do_est_final.append(est_final[i][j + 1])
    return prox_do_tab, prox_do_est_final


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
    for k in range(len(aux)):
        a,b = pos(aux[k],tabuleiro)
        m_auxiliar = copy.deepcopy(tabuleiro)
        auxilio = m_auxiliar[i][j] 
        m_auxiliar[i][j] = m_auxiliar[a][b] 
        m_auxiliar[a][b] = auxilio

        no = No()
        no.tabuleiro = copy.deepcopy(m_auxiliar)
        no.custo_h = h3(no.tabuleiro)
        no.pai = v
        no.custo_g = v.custo_g + 1
        no.custo_f = no.custo_g + no.custo_h
        yield no


def h1(tabuleiro):
    est_final = [[1,2,3,4], [12,13,14,5], [11,0,15,6], [10,9,8,7]]
    peca_fora_lugar = 0    
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j] != est_final[i][j]:
                peca_fora_lugar += 1
    return peca_fora_lugar

def h2(tabuleiro):
    est_final = [[1,2,3,4], [12,13,14,5], [11,0,15,6], [10,9,8,7]]
    seq_fora_lugar = 0
    
    prox_do_tab,prox_do_est_final = gerar_vet_proximos(tabuleiro,est_final)
    
    for i in range(len(prox_do_tab)):
        if prox_do_tab[i] != prox_do_est_final[i]:
                seq_fora_lugar += 1
    return seq_fora_lugar

def h3(tabuleiro):
    est_final = [[1,2,3,4], [12,13,14,5], [11,0,15,6], [10,9,8,7]]
    manhattan = 0
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j] != est_final[i][j]:
                x1,y1 = i,j
                x2,y2 = pos(est_final[i][j],tabuleiro)
                manhattan += abs(x1 - x2) + abs(y1 - y2)
    return manhattan

def h4(tabuleiro):
    p1,p2,p3 = 0.5,0.2,0.3
    return (p1 * h1(tabuleiro)) + (p2 * h2(tabuleiro)) + (p3 * h3(tabuleiro))

def h5(tabuleiro):
    return max(h1(tabuleiro),h2(tabuleiro),h3(tabuleiro))



def a_star(inicial,final):
    conj_a = []
    conj_f = set()
    heapq.heappush(conj_a,inicial)
    v = heapq.heappop(conj_a)
    while v.tabuleiro != final.tabuleiro:
        conj_f.add(v)
        for m in geraSucessores(v,pos_sucessoras(v.tabuleiro)):
            if m not in conj_f:
                heapq.heappush(conj_a,m)
        v = heapq.heappop(conj_a)
    print(v.custo_g)





def main():
    
    inicial = No()
    final = No()
    m_tabuleiro = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    
    entrada = input().split(' ')
    aux = arr_int(entrada) 
 
    m_tabuleiro[0][0] = aux[0]
    m_tabuleiro[0][1] = aux[1]
    m_tabuleiro[0][2] = aux[2]
    m_tabuleiro[0][3] = aux[3]
    m_tabuleiro[1][0] = aux[4]
    m_tabuleiro[1][1] = aux[5]
    m_tabuleiro[1][2] = aux[6]
    m_tabuleiro[1][3] = aux[7]
    m_tabuleiro[2][0] = aux[8]
    m_tabuleiro[2][1] = aux[9]
    m_tabuleiro[2][2] = aux[10]
    m_tabuleiro[2][3] = aux[11]
    m_tabuleiro[3][0] = aux[12]
    m_tabuleiro[3][1] = aux[13]
    m_tabuleiro[3][2] = aux[14]
    m_tabuleiro[3][3] = aux[15]
    

    inicial.tabuleiro = m_tabuleiro
    final.tabuleiro = [[1,2,3,4], [12,13,14,5], [11,0,15,6], [10,9,8,7]]
    
    a_star(inicial,final)   
    
if __name__ == '__main__':
    main()








 




 
