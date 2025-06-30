distancia_percorrida= float(input("Digite a distância percorrida em km, por favor:"))
tempo= float(input("Digite a quantidade de dias que ficou com o carro, por favor:"))
preco=(60*tempo)+(0.15*distancia_percorrida)
print(f"O valor a ser pago é de R${preco:.2f}")