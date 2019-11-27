"""
Trabalho Pratico - Sistemas de Apoio a Decisão
Algoritmo A_Priori
Gabriel
Marcos
Maycon Muller
Philipe Rocha
"""

data = []
itens_data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-17]
supMin = 0.42

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
        data.append(lineSet)

    ref.close()
    new.close()
    return 1


# suporte de cada item/ pensei em usar uma estrutura de (chave:valor) para armazenar isso;
def sigma(citem):
    sig = 0
    sc = set(citem)
    for d in data:
        ld = set(d)
        if sc.issubset(ld):
            sig += 1

    return sig

def conf(regra):
    lr = list(regra)
    return sigma(lr)/sigma([lr[0]])


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
    t = set(t)
    for c in C:
        if t.issuperset(c):
            lc.append(c)
    return lc

def uniList(l1, l2):
    lr = l2.copy()
    for x in l1:
        if x not in lr:
            if len(x) > 1:
                lr.append(x)
    return lr

def apriori(supMin, transacoes, itens):
    k: int = 1
    f_list = [{i} for i in itens if sigma([i])/len(data) >= supMin]  # itemset de 1 elemento -> funciona, basta a função sigma
    f = f_list
    fk_list = []
    while True:
        k += 1
        ck = genCandidatos(f)

        for t in transacoes:
            ct = subSet(ck, t)
            # for c in ct:
            #     c
            #     # incrementa o suporte -> fiquei com dúvida nessa parte..
            fk_list = [c for c in ct if sigma(list(c))/len(data) >= supMin]
        if len(fk_list) == 0: break
        f = uniList(f, fk_list)
        fk_list.clear()

    return f


def main():
    norData()
    x = apriori(supMin, data, itens_data)

    print(x)
    for i in x:
        li = list(i)
        print("{"+str(li[0])+"}-> {"+str(li[1])+"}")
        print("Confiança:"+str(conf(i)))
        li.reverse()
        ir = set(li)
        print("{"+str(li[0])+"}-> {"+str(li[1])+"}")
        print("Confiança:"+str(conf(ir)))


main()
