import pygame
pygame.display.set_caption('ejercicio 3')
pygame.init()
surface = pygame.display.set_mode((1920,1080))
color = (140,84,17)
color_2 = (17,140,32)
colo=pygame.image.load("colo.png")
while True:
    pygame.draw.rect(surface, color, pygame.Rect(500, 720, 300, 300))
    pygame.draw.rect(surface, color_2, pygame.Rect(10, 1020, 1920, 230))
    surface.blit(colo,(500,720))
    pygame.display.flip()
