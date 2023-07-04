import sys
import time
from pygame import display, image, init, gfxdraw
import pygame
import random


def draw_point(x,y):
    #    gfxdraw.pixel(screen, x, y, (255, 255, 255))
    xx = pygame.Rect(x, y, 1, 1)
    # color = ((255*x)//x_len, (255*y)//y_len, 255)
    dist_a = ((x-init_pnt[0][0])**2+(y-init_pnt[0][1])**2)**(1/2)
    dist_b = ((x-init_pnt[1][0])**2+(y-init_pnt[1][1])**2)**(1/2)
    dist_c = ((x-init_pnt[2][0])**2+(y-init_pnt[2][1])**2)**(1/2)
    s = dist_a + dist_b + dist_c
    color = (int(255*(s - dist_a)/s), int(255*(s - dist_b)/s), int(255*(s - dist_c)/s))
    # color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # for random color of pixels
    pygame.draw.rect(screen, color, xx)
    pygame.display.update(xx)


init()
screen = display.set_mode((1000, 710))
x_len, y_len = screen.get_size()
display.set_caption("Sierpinski Triangle(Chaotic)")

fst_tm = True
init_pnt = ((0, 707), (500, 0), (1000, 707))
cur_point = (0,0)
running = False
x_n = 2
c = 0
while True:
    if not fst_tm:
        """if x_n == 0:
            x_n = 1
        elif x_n == 1:
            x_n = 2
        elif x_n == 2:
            x_n = 0"""
        x_n = random.choice((0, 1, 2))
        x = init_pnt[x_n]
        nxt_point = ((x[0] + cur_point[0]) // 2, (x[1] + cur_point[1]) // 2)
        draw_point(nxt_point[0], nxt_point[1])
        cur_point = nxt_point
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            tp = pygame.mouse.get_pressed()
            if tp[0] and fst_tm:
                print("Started making points")
                if fst_tm:
                    draw_point(init_pnt[0][0], init_pnt[0][1])
                    draw_point(init_pnt[1][0], init_pnt[1][1])
                    draw_point(init_pnt[2][0], init_pnt[2][1])
                    cur_point = (500, 707)
                    fst_tm = False
                    pygame.display.update()

            if event.button == 5:
                sys.exit()
    if c % 1000000:
        pygame.display.update()
    c += 1
