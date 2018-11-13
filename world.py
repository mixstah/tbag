import pygame
from random import randint

change = True

new_world = []

n = 10

w = 0
x = n - 1
z = (n * n) - 1
y = z - x

world = []

# 0000 0001 0010 0011 0100 0101 0110 0111
# 1000 1001 1010 1011 1100 1101 1110 1111


directions = ['w', 's', 'sw', 'e', 'ew', 'es', 'esw', 'n', 'nw', 'ns', 'nsw', 'ne', 'new', 'nes', 'nesw']
top = ['w', 's', 'sw', 'e', 'ew', 'es', 'esw']
right = ['w', 's', 'sw', 'n', 'nw', 'ns', 'nsw']
left = ['s', 'e', 'es', 'n', 'ns', 'ne', 'nes']
bottom = ['w', 'e', 'ew', 'n', 'nw', 'ne', 'new']

tl = ['e', 'es', 's']
tr = ['w', 'ws', 's']
bl = ['n', 'ne', 'e']
br = ['n', 'nw', 'w']

print(w, x, y, z)

for i in range(w, z + 1):
    # Top Left
    if i == w:
        world.append(tl[randint(0, 2)])
    # Top Right
    elif i == x:
        world.append(tr[randint(0, 2)])
    # Bottom Left
    elif i == y:
        world.append(bl[randint(0, 2)])
    # Bottom Right
    elif i == z:
        world.append(br[randint(0, 2)])
    # Top row
    elif i > 0 and i < x:
        world.append(top[randint(0, 6)])
    # Bottom row
    elif i >= y and i < z:
        world.append(bottom[randint(0, 6)])
    # Left column
    elif i > x and i < y and i % n == 0:
        world.append(left[randint(0, 6)])
    # Right column
    elif i > x and i < z and (i + 1) % n == 0:
        world.append(right[randint(0, 6)])
    # Center Piece
    else:
        world.append(directions[randint(0, 6)])


def getImage():
    global world
    for room in world:
        fin = ''
        
        if 'n' in room:
            fin+='n'
        if 'e' in room:
            fin+='e'
        if 's' in room:
            fin+='s'
        if 'w' in room:
            fin+='w'
        print('FIN: ',fin)
        new_world.append(fin)

def check():
    change = False
    for c, r in enumerate(world):
        if c > 0:
            # Check east
            if 'e' in world[c - 1]:
                if 'w' in r:
                    continue
                else:
                    world[c] += 'w'
                    change = True
    for c, r in enumerate(world):
        if c < z:
            # Check east
            if 'w' in world[c + 1]:
                if 'e' in r:
                    continue
                else:
                    world[c] += 'e'
                    change = True

    for c, r in enumerate(world):
        if c < y:
            # Check east
            if 'n' in world[c + n]:

                if 's' in r:

                    continue
                else:
                    world[c] += 's'

                    change = True
    for c, r in enumerate(world):
        if c > n-1:
            # Check east
            if 's' in world[c - n]:
                if 'n' in r:
                    continue
                else:
                    world[c] += 'n'
                    change = True

    if change == True: check()



check()
print()
getImage()

def getWorld():
    
    global new_world
    return new_world




