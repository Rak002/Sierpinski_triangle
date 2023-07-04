import sys
import time
from pygame import display, image, init, gfxdraw
import pygame
import random


def draw_point(x, y):
    xx = pygame.Rect(x, y, 1, 1)
    dist_a = ((x - init_pnt[0][0]) ** 2 + (y - init_pnt[0][1]) ** 2) ** (1 / 2)
    dist_b = ((x - init_pnt[1][0]) ** 2 + (y - init_pnt[1][1]) ** 2) ** (1 / 2)
    dist_c = ((x - init_pnt[2][0]) ** 2 + (y - init_pnt[2][1]) ** 2) ** (1 / 2)
    s = dist_a + dist_b + dist_c
    color = (int(255 * (s - dist_a) / s), int(255 * (s - dist_b) / s), int(255 * (s - dist_c) / s))
    pygame.draw.rect(screen, color, xx)
    pygame.display.update(xx)


init()
screen = display.set_mode((1100, 780))
x_len, y_len = screen.get_size()
display.set_caption("Sierpinski Triangle(Chaotic)")
font1 = pygame.font.Font('lib/AlexBrush-Regular.ttf', 50)
font2 = pygame.font.Font('lib/request_coffee.ttf', 32)
# font3 = pygame.font.Font('freesansbold.ttf', 32)
fst_tm = True
init_pnt = ((0+70, 775-15), (500+70, 68-15), (1000+70, 775-15))
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(init_pnt[0][0]-1, init_pnt[0][1]-1, 3, 3))
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(init_pnt[1][0]-1, init_pnt[1][1]-1, 3, 3))
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(init_pnt[2][0]-1, init_pnt[2][1]-1, 3, 3))
screen.blit(pygame.font.Font('lib/request_coffee.ttf', 20).render('A', True, (255, 255, 255), (0, 0, 0)), (init_pnt[1][0]-7, init_pnt[1][1]-28))
screen.blit(pygame.font.Font('lib/request_coffee.ttf', 20).render('B', True, (255, 255, 255), (0, 0, 0)), (init_pnt[0][0]-18, init_pnt[0][1]-23))
screen.blit(pygame.font.Font('lib/request_coffee.ttf', 20).render('C', True, (255, 255, 255), (0, 0, 0)), (init_pnt[2][0]+2, init_pnt[2][1]-23))
screen.blit(pygame.font.Font('lib/request_coffee.ttf', 25).render('      Click to Start!', True, (255, 255, 255), (0, 0, 0)), (425,400))

text1 = font1.render(' Sierpinski Triangle', True, (255, 200, 100), (0, 0, 0))
screen.blit(text1, (30, 20))
pygame.display.update()
cur_point = (0, 0)
running = False
x_n = 2
c = 0
while True:
    if not fst_tm:
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
                    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(425, 400, 400, 100))
                    pygame.display.update()

            if event.button == 5:
                sys.exit()
    if c % 1000000:
        pygame.display.update()
    c += 1
