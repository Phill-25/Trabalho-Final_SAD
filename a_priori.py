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


# função para gerar os candidatos a partir de F

def genCandidatos(f, k):
    return {{'bla'}}


# função que gera o set com os conjuntos que estão nas transações

def subSet(C, t):
    sc = set()
    for c in C:
        cs = set(c)
        if (t.issuperset(cs)):
            print(cs)
    return sc #buscar uma forma de gerar um set unico de retorno!!!


# def apriori(supMin, transacoes, itens):
#     k: int = 1
#     f_list = [{i} for i in itens if sigma(i) >= supMin] #itemset de 1 elemento
#     f = fk = set(f_list)
#     while(len(fk) != 0):
#         ++k
#         ck = genCandidatos(F, k-1)
#         for t in transacoes:
#             ct = subSet(ck, t)
#             for c in ct:
#                 #incrementa o suporte -> fiquei com dúvida nessa parte..
#         fk_list = [{c} for c in ck if sigma(c) >= supMin]
#         fk = set(fk_list)
#         f.union(fk)
#
#     return f

#comentei a apriori pq esta dando erro de identação

y = {'pao', 'leite', 'cafe'}
x = [{'pao', 'leite'}, {'leite', 'cafe'}]
subSet(x, y)
