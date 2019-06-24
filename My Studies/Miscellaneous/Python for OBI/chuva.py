#l = [int(input()) for i in range(0, int(input()))]
n = input()
l = []
for i in range(0, int(n)):
        l.append(input())


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
cheias = 0
for x in l:
        if ((l[int(x)] < max(l[0:int(x)])) & (l[int(x)] < max(l[int(x)+1:]))):
                cheias = cheias + 1
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

maiorDir.reverse()
for secao in l[maior]:
    if ((l[secao - 1] < maiorDir[secao - 1]) and (l[secao - 1] < maiorEsq[secao - 1])):
        cheias = cheias + 1
print(cheias)
'''