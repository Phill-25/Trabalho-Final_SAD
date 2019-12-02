"""
Trabalho Pratico - Sistemas de Apoio a Decisão
Algoritmo A_Priori
Gabriel
Marcos
Maycon Muller
Philipe Rocha
"""

data = []
itens_data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16]
supMin = 0.48
def norData():
    ref = open("house_votes_84.data", "r")
    new = open("house_votes_nor.data", "w")

    for line in ref:
        sline = line.split(",") # incluir cada elemento da base de dados de forma individual
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
    if type(lr[0]) == int:
        z0 = [lr[0]]
        return sigma(z0) / sigma(lr[1])
    if type(lr[1]) == int:
        z1 = [lr[1]]
        return sigma(lr[0]) / sigma(z1)
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
                if u not in listC and u not in fc:
                    listC.append(u)
    return listC


# função que gera o set com os conjuntos que estão nas transações -> funcionando

def subSet(C, t):
    lc = []
    t = set(t)
    for c in C:
        if t.issuperset(c):
            if c not in lc:
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
    f = [{i} for i in itens if sigma([i])/len(transacoes) >= supMin]  # itemset de 1 elemento -> funciona, basta a função sigma
    while True:
        k += 1
        ck = genCandidatos(f)
        for t in transacoes:# não é utilizado!
            ct = subSet(ck, t)
        fk_list = [c for c in ck if sigma(list(c))/len(transacoes) >= supMin]
        if len(fk_list) == 0: break
        f = uniList(f, fk_list)
        fk_list.clear()

    return f

def regra(lista):
  rt = []
  for i in lista:
    for e in i:
      lc = list(i)
      lc.remove(e)
      c1 = [e]
      c1.append(lc)
      c2 = [lc]
      c2.append(e)
      if c1 not in rt:
        rt.append(c1)
      if c2 not in rt:
        rt.append(c2)
  return list(rt)




def main():
    norData()
    x = apriori(supMin, data, itens_data)

    #print(x[0])
    print("Resultado Apriori")
    print(x)

    reg = regra(x)
    print("Combinações de Conjuntos")
    print(reg)

    print("*************************************************")
    print("************     Regras         *****************")
    print("*************************************************")
    for i in reg:


        #Não conseguimos calcular a confiaça para as regras

        li = list(i)

        print("{" + str(li[0]) + "} -> {" + str(li[1]) + "}")
        print("Confiança:"+str(conf(i)))
        #----------codigo anterior (Gera confiança para conjuntos de dois elementos) não funciona pra lista de lista------------
        # li = list(i)
        # print("{"+str(li[0])+"}-> {"+str(li[1])+"}")
        # print("Confiança:"+str(conf(i)))
        # li.reverse()
        # ir = set(li)
        # print("{"+str(li[0])+"}-> {"+str(li[1])+"}")
        # print("Confiança:"+str(conf(ir)))
        #-------------------------------------------------------------------------------------------------------------------
main()
