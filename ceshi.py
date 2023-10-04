import sys
import pygame

pygame.init()
win = pygame.display.set_mode((150, 150))
img_2 = pygame.image.load("./file/2.png")
clock = pygame.time.Clock()
clock.tick(20)
a = 0
while True:
    a += 0.01
    img_2_rect = pygame.Rect([a, 0, 0, 0])
    win.blit(img_2, img_2_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
