l = [int(input()) for i in range(0, int(input()))]

'''
prim = l[0]
ult = l[len(l)-1]
cheias = 0

for secao in l:
    if ((secao < prim) & (secao < ult)):
        cheias = cheias + 1
    if (secao >= prim):
        prim = secao

print(cheias)
'''

maiorDir = []
maiorEsq = []
maior = 0
cheias = 0

for i in range(0, len(l)):
    if (l[i] > maior):
        maior = l[i]
        maiorEsq.append(l[i])
    else:
        maiorEsq.append(maior)

maior = 0

for j in range(len(l)-1, -1, -1):
    if (l[j] < maior):
        maiorDir.append(maior)
    else:
        maior = l[j]
        maiorDir.append(l[j])


for secao in l:
    if ((secao < maiorDir[secao]) & (secao < maiorEsq[secao])):
        cheias = cheias + 1

print(cheias)
