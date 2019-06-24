Ai, Bi, Af, Bf = input().split(' ')
fim = 0

if (Bi == Bf):
    if (Ai == Af):
        fim = 0
    else:
        fim = 1

if (Ai == Af):      # muda B e desmuda A
    fim = 2
else:
    fim = 1

print(fim)





