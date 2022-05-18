empleado = open("empleados.txt", "r") 

correo = open("correos.txt", "a")  

personas = len(empleado.readlines()) - 1 

empleado.seek(0) 

for x in range(personas): 

    Nombre = empleado.readline() 
    arregloNombre = Nombre.split() 
    largoNombre = len(arregloNombre) 

    for x in range(largoNombre): 
        correo.write(arregloNombre[x])
        correo.write(" ") 
    correo.write("\n"+"\n") 

    nom = arregloNombre[1]
    ape = arregloNombre[2]
    mail = nom[0].lower() + ape[0].lower() + arregloNombre[0].lower() 

    if largoNombre == 4:
        mail = mail + "@gerenciaempresa.cl"
    elif largoNombre == 3:
        mail = mail + "@empresa.cl"

    correo.write(mail+"\n"+"\n")
empleado.close()
correo.close()
