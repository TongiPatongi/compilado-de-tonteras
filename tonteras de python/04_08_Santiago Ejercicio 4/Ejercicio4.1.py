archivo = open("alumnos.txt", "r") 

vertical = open("vertical.txt", "a")  

Arreglo = (archivo.readline()).split() 

personas = len(Arreglo) 
for x in range(personas): 
    text = Arreglo[x] 
    vertical.write(text+"\n")
archivo.close()
vertical.close()
