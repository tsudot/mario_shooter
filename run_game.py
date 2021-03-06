import pygame, os, sys
from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print "Cannot load image:"
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


class Bullet(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('bullet.png', -1)

	def shoot(self, startpos):
		self.rect.center = startpos
		
	def update(self):	
		self.rect.move_ip(5,0)
		 
		
class Mario(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('mario2.png', -1)
		self.movx = 0
		self.movy = 0

	def update(self):
		newpos = self.rect.move(self.movx, self.movy)
#		self.image = pygame.transform.flip(self.image,0,0)
		self.rect = newpos

	def fire(self):
		return self.rect.center
	
	def change(self, x, y):
		self.movx+=(2*x)
		self.movy+=(2*y)
			


class Gun(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.startpos = (0,0)
		
	def update(self):
		bullet = Bullet()
		bullet.shoot(self.startpos)
		
	def g_fire(self,startpos):	
		self.startpos = startpos


pygame.init()
screen = pygame.display.set_mode((468,500))
pygame.display.set_caption('Mario Shooter')
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((50,50,50))

screen.blit(background, (0,0))
pygame.display.flip()

	
mario = Mario()
bullet = Bullet()
#gun = Gun()
allsprites = pygame.sprite.RenderPlain(mario,bullet)
clock = pygame.time.Clock()

while 1 :
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit(0)
		elif event.type == KEYDOWN:
			if event.key == K_RIGHT:
				mario.change(1,0)
			elif event.key == K_LEFT:
				mario.change(-1,0)
			elif event.key == K_UP:
				mario.change(0,-1)
			elif event.key == K_DOWN:
				mario.change(0,1)
			elif event.key == K_f:
				bullet.shoot(mario.fire())
		elif event.type == KEYUP:
			if event.key == K_RIGHT:
				mario.change(-1,0) 
			elif event.key == K_LEFT:
				mario.change(1,0)
			elif event.key == K_UP:
				mario.change(0,1)
			elif event.key == K_DOWN:
				mario.change(0,-1)
#	allsprites = pygame.sprite.RenderPlain(mario, bullet)
	allsprites.update()
	screen.blit(background, (0,0))
	allsprites.draw(screen)
	pygame.display.flip()

	
