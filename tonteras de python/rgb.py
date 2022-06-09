#Imagen en forma de pixeles RGB
import numpy
imagen = [
    [[58,23,125], [150,255,0], [0,0,0], [14,0,99] ],
    [[0,0,200] , [34,25,0] , [0,65,0] , [8,0,45] ],
    [[58,0,1] , [70,25,0], [0,80,165], [255,255,255]]
    ]
def invertir_imagen(imagen):
    filas = len(imagen)
    columnas = len(imagen[0])
    index,sublista,lista = 0,0,0
    lista_final = []
    for x in range(filas):
        for y in range(columnas):
            rgb = []
            for z in range(3):
                rgb.append(abs(imagen[lista][sublista][index] - 255))
                index += 1
            lista_final.append(rgb)
            print("")
            index = 0
            sublista += 1
        sublista = 0
        lista += 1
    return lista_final
def rotar_derecha(imagen):
    return numpy.rot90(imagen,3)
inversa = invertir_imagen(imagen)
rotar = rotar_derecha(imagen)
print(inversa)
print(rotar)
