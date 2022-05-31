import pygame
pygame.init()
win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Moving rectangle")
x = 500
y = 500
width = 50
height = 50
vel = 25
run = True
while run:
	pygame.time.delay(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and x>0:
		x -= vel
	if keys[pygame.K_RIGHT] and x<1000-width:
		x += vel
	if keys[pygame.K_UP] and y>0:
		y -= vel
	if keys[pygame.K_DOWN] and y<1000-height:
		y += vel
	win.fill((0, 0, 0))
	pygame.draw.rect(win, (5, 180, 120), (x, y, width, height))
	pygame.display.update()
pygame.quit()