figtotal, carimbadastotal, qtstenho = input().split(' ')
carimbadas = input().split(' ')[0: int(carimbadastotal)]
quaistenho = input().split(' ')[0: int(qtstenho)]

    #tenho que ver se as carimbadas estao nas que eu tenho

for carimbada in carimbadas:
    for tenho in quaistenho:
        if (carimbada == tenho):
            carimbadastotal = int(carimbadastotal)-1
            break
print(carimbadastotal)