#Algoritmo adivina_el_numero
import random
print('Bienvenido a "Adivina el número"! Elije un numero al azar y yo te frio o caliente')
print("Tienes 5 intentos para adivinar el número")

num_ingresado = abs(int(input()))
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
num_azar = random.choice(numeros)

i = 1
while i < 5:
    if num_ingresado == num_azar:
        print("Adivinaste el número!")
        break
    elif num_ingresado != num_azar:
        acercamiento = abs(num_ingresado - num_azar)
        if acercamiento >= 10:
            print("Frio!")
            i = i + 1
            num_ingresado = abs(int(input()))
            
        elif acercamiento <= 10 and acercamiento >= 4:
            print("caliente")
            i = i + 1
            num_ingresado = abs(int(input()))
            
        elif acercamiento <= 4:
            print("Muy caliente!")
            i = i + 1
            num_ingresado = abs(int(input()))
if i >= 5:
    print("Perdiste :(")