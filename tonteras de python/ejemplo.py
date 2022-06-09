import pygame
import math
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# some helpful vector math functions
def normalize(v):
    vmag = magnitude(v)
    return [v[i]/vmag  for i in range(len(v))]
def magnitude(v):
    return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))
def add(u, v):
    return [ u[i]+v[i] for i in range(len(u)) ]

class Paddle(pygame.sprite.Sprite):
    def __init__(self, start_pos, up_key, down_key):
        pygame.sprite.Sprite.__init__(self)
        # the image is just a white rect
        self.image = pygame.surface.Surface((20, 100))
        self.image.fill(pygame.color.Color('White'))
        self.image.set_colorkey(pygame.color.Color('Black'))
        self.rect = self.image.get_rect(topleft=start_pos)
        # using a mask so we can use pixel perfect collision
        self.mask = pygame.mask.from_surface(self.image)
        self.up_key, self.down_key = up_key, down_key
    def update(self, pressed):
        if pressed[self.up_key]:   self.rect.move_ip(0, -3)
        if pressed[self.down_key]: self.rect.move_ip(0,  3)
        # keep the paddle inside the screen
        self.rect.clamp_ip(pygame.display.get_surface().get_rect())

class Ball(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        pygame.sprite.Sprite.__init__(self)
        # the image is just a white ball
        self.image = pygame.surface.Surface((20, 20))
        self.rect = self.image.get_rect(center=start_pos)
        pygame.draw.circle(self.image, pygame.color.Color('White'), self.image.get_rect().center, 10)
        self.image.set_colorkey(pygame.color.Color('Black'))
        # using a mask so we can use pixel perfect collision
        self.mask = pygame.mask.from_surface(self.image)
        # the vector we use to move the ball
        self.move_v = (1, 0.7)
        # store the absolute position in self.pos
        # because a rect can only use integers
        self.pos = self.rect.center
    def update(self, pressed):
        # check if the ball collides with any other sprite
        collide = [s for s in pygame.sprite.spritecollide(self, self.groups()[0], False, pygame.sprite.collide_mask) if s != self]
        if collide:
            # warning: this does not handle the case of the ball hits 
            # the top or bottom of the paddle, only the sides.
            self.move_v = [-self.move_v[0], self.move_v[1]]

        # check if the ball would go out of screen
        display = pygame.display.get_surface().get_rect()
        if self.rect.top < display.top and self.move_v[1] < 0 or \
           self.rect.bottom > display.bottom and self.move_v[1] > 0:
            self.move_v = [self.move_v[0], -self.move_v[1]]

        # apply a constant speed and update the position
        move_vector = [c * 4 for c in normalize(self.move_v)]
        self.pos = add(self.rect.center, move_vector)
        self.rect.center = map(int, self.pos)

player1 = Paddle((30,  190), pygame.K_w , pygame.K_s)
player2 = Paddle((590, 190), pygame.K_UP, pygame.K_DOWN)
ball = Ball(screen.get_rect().center)
sprites = pygame.sprite.Group(player1, player2, ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: break
    else:
        pressed = pygame.key.get_pressed()
        sprites.update(pressed)
        screen.fill(pygame.color.Color('black'))
        sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        continue
    break
pygame.quit()
