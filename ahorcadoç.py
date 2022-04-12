#ahorcado
import random
import time
palabras=["peru","fuerza","llave","cilindro","paraguas","bymatrix","moreno","scout"]
print("hola :v")
time.sleep(1)
print("Intenta no morir")
time.sleep(1)
print("puedes fallar 5 veces")
time.sleep(1)
vidas=5
while True:

    while True:
        letra_adivinada = input("Adivina una letra: ")
        if(len(letra_adivinada)!=1 and letra_adivinada.isnumeric()):
            print("Eso no es una letra intenta con una sola letra")
        else:
            if letra_adivinada.lower() in lista_letras_adivinadas:
                print("Ya habias intentado con esa letra intenta con otra por favor")
            else:
                lista_letras_adivinadas.append(letra_adivinada)
 
                if letra_adivinada.lower() in palabra_secreta:
                    print("Felicidades adivinaste una letra")
                    break
                else:
                    vidas = vidas-1
                    print("Te haz equivocado y perdido una vida")
                    print("Te quedan " + str(vidas) + " vidas")
                    break
i

