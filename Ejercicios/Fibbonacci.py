#Algoritmo fibonacci
na2 = 0
na1 = 1
cantNum = int(input("Cuantos numeros quiere calcular?: "))
print(na2)
for i in range(cantNum):
    nf = na1 + na2
    na2 = na1
    na1 = nf
    print(nf)

