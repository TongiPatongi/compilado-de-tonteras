#problema 5
#mcm = minimo comun multiplo
# % = lo que sobra de una division
#test=30 % 7
# en el in range es uno menos
#print(test)
def mcm(numero):
        for i in range (1,21):
                if numero % i !=0:
                        return False       
        return True
numero=1
while True:
        if mcm(numero):
                break
        numero +=1
print(numero)
#verificar las divisiones
for i in range (1,21):
        print(232792560 / i)
