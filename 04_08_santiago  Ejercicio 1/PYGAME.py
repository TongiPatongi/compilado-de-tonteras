import pygame
pygame.display.set_caption('ejercicio 1')
pygame.init()
surface = pygame.display.set_mode((600,400))
color_puerta = (59,50,51)
color_ventana = (113,217,208)
color_techo = (204,118,20)
color_paredes = (214,209,191)
color_piso = (16,69,18)
color_fondo = (71,98,230)
montaña=pygame.image.load("montaña.png")
arbol=pygame.image.load("arbol.png")
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if running==False:
        pygame.quit()
    pygame.draw.rect(surface, color_fondo, pygame.Rect(0, 0, 600, 400))
    surface.blit(montaña,(-100,-100))
    pygame.draw.rect(surface, color_paredes, pygame.Rect(200, 200, 200, 200))
    pygame.draw.rect(surface, color_puerta, pygame.Rect(265, 300, 50, 180))
    pygame.draw.rect(surface, color_ventana, pygame.Rect(340, 320, 40, 40))
    pygame.draw.rect(surface, color_ventana, pygame.Rect(235, 220, 140, 50))
    pygame.draw.rect(surface, color_piso, pygame.Rect(0, 380, 600, 20))
    pygame.draw.rect(surface, color_techo, pygame.Rect(200, 150, 200, 50))
    surface.blit(arbol,(400,130))
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    pygame.display.flip() 
