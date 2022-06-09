
##binarios
def binarios(numero):
    ceros=0
    unos=0
    for j in numero:
        if j=="0":

            ceros+=1
        elif j=="1":
            unos+=1
    print("la cantidad de ceros es:",ceros,"\nla cantidad de unos es:",unos)
numero=input("ingrese un numero:")
print(binarios(numero))

def binarios_creciente(numero):
    ceros=0
    unos=0
    for j in numero:
        if j=="0":
            ceros+=1
        elif j=="1":
            unos+=1
    print("0"*ceros,"1"*unos)
numero=input("ingrese un numero:")
print("el orden de los numeros es:",binarios_creciente(numero))


    
