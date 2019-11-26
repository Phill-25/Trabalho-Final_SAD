"""
Trabalho Pratico - Sistemas de Apoio a Decisão
Algoritmo A_Priori
Gabriel
Marcos
Maycon Muller
Philipe Rocha
"""



# suporte de cada item/ pensei em usar uma estrutura de (chave:valor) para armazenar isso;
def sigma(item):
    item
    return 0


# função para gerar os candidatos a partir de F -> funcionando

def genCandidatos(f):
    l = []
    fc = f.copy()
    while fc:
        t = fc.pop()
        for c in fc:
            u = c | t
            if len(u) == len(c)+1:
                l.append(u)
    return l


# função que gera o set com os conjuntos que estão nas transações -> funcionando

def subSet(C, t):
    lc = []
    for c in C:
        if (t.issuperset(c)):
            lc.append(c)
    return lc


def apriori(supMin, transacoes, itens):
    k: int = 1
    f_list = [{i} for i in itens if sigma(i) >= supMin]  # itemset de 1 elemento -> funciona, basta a função sigma
    f = fk = set(f_list)
    while len(fk) != 0:
        ++k
        ck = genCandidatos(f)
        for t in transacoes:
            ct = subSet(ck, t)
            for c in ct:
                c
                # incrementa o suporte -> fiquei com dúvida nessa parte..
        fk_list = [{c} for c in ck if sigma(c) >= supMin]
        fk = set(fk_list)
        f.union(fk)

    return f


t = {'pao', 'leite', 'cafe'}

t1 = [{'pao'}, {'leite'}, {'cafe'}]
x = [{'pao', 'leite'}, {'leite', 'cafe'}, {'ovo', 'cafe'}]
print(subSet(x, t))
print(genCandidatos(t1))
