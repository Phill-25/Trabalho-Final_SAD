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
    listC = []
    fc = f.copy()
    while fc:
        t = fc.pop()
        for c in fc:
            u = c | t
            if len(u) == len(c) + 1:
                listC.append(u)
    return listC


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
        k += 1
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


def norData():
    ref = open("house_votes_84.data", "r")
    new = open("house_votes_nor.data", "w")

    for line in ref:
        sline = line.split(",")
        lineSet = []
        for i in range(len(sline)):
            x = i + 1
            if i == 0:
                if sline[i].__eq__('republican'):
                    lineSet.append(x)
                else:
                    lineSet.append(x * -1)
            else:
                if sline[i] == "?":
                    lineSet.append("?")
                else:
                    if i == 16:
                        lineSet.append(sline[i])

                    else:
                        if sline[i] == "y":
                            lineSet.append(x)
                        else:
                            lineSet.append(x * -1)


        strSet = lineSet.__str__()
        new.write(strSet)
        new.write("\n")

    ref.close()
    new.close()
    return 1


def main():
    t = {1, -2, 3}

    t1 = [{1}, {-2}, {-3}]
    x = [{'pao', 'leite'}, {'leite', 'cafe'}, {'ovo', 'cafe'}]

    print(subSet(genCandidatos(x), t))
    print(subSet(t1, t))
    print(genCandidatos(x))

    norData()
    print("END!")


main()
