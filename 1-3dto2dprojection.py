# 3D to 2d Projection

import pygame
import math
import time

(width, height) = (600, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()


running = True

K = 8   # view plane distance
cz = 10 # z location of circle initially.

def translate_coords_to_center(x , y):
    return (width/2 - x, height/2 - y)

def pixel(x,y,color=(10,20,100)):
    s = pygame.Surface((1,1))
    s.fill(color)
    r,r.x,r.y = s.get_rect(),x,y
    screen.blit(s,r)

def circle(cx, cy, cz, radius):
    N = 100
    PI = 3.14
    angle = 360 / N


    # plot the circle around translated (x,y)
    for i in range(N):
        x2 = cx + radius * math.cos(PI* angle * i / 180)
        y2 = cy + radius * math.sin(PI* angle * i / 180)

        # Do a 2d projection
        x2 = K* x2 / cz
        y2 = K* y2 / cz
        sx, sy = translate_coords_to_center(x2, y2)

        pixel(sx, sy)

x = 0
y = 0
while running:
    circle(x,y, cz, 100)
    cz += 1
    time.sleep(0.5)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
