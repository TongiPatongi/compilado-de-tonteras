#menu
print("Bienvenido al ring de combate")
class personaje:
    def __init__(self,nombre,vida,poder,velocidad,resistencia):
        self.nombre = nombre; self.vida = vida; self.poder = poder
        self.velocidad = velocidad; self.resistencia = resistencia
    def golpear(self,g):
        g.daño=abs(self.poder/self.resistencia)
        g.vida -=g.daño
        print("golpe crítico", self.nombre)   
#batalla
def simular_batalla(j1,j2):
    golpeador,receptor = j1,j2
    if(j1.velocidad < j2.velocidad): 
	    golpeador,receptor = j2,j1
    while(j1.vida > 0 and j2.vida > 0):
	    print("\n" + j1.nombre,j1.vida,"vs",j2.vida,j2.nombre)
	    golpeador.golpear(receptor)
	    golpeador,receptor = receptor,golpeador
    print("\n" + j1.nombre,j1.vida,"vs",j2.vida,j2.nombre)
    print("Ganador:",receptor.nombre)
#personajes
chavo = personaje("chavo",100,20,30,90)
paredes = personaje("paredes",100,40,50,60)
lanzadardos = personaje("lanzadardos",100,40,90,10)
pou = personaje("pou",100,60,20,60)                          
simular_batalla(pou,paredes)
