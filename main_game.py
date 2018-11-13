import pygame
import world
import math

# initialize game engine
pygame.init()
# set screen width/height and caption
size = [800, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')
world = world.getWorld()
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

class Tile(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        print(x)
        super().__init__()

        self.image = pygame.image.load(image)
        

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

world_map = pygame.sprite.Group()
x =150
y = 100
s = math.sqrt(len(world))
count = 0
for room in world:
    cell = Tile(room+'.png',x,y)
    world_map.add(cell)
    x+=31
    count +=1
    if count == s:
        count = 0
        x = 150
        y+=31


# Loop until the user clicks close button
done = False
while done == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    world_map.draw(screen)

    pygame.display.update()
    clock.tick(20)

pygame.quit()
