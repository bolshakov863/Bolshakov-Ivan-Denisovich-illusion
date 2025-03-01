import pygame
import random
from all_colors import *
pygame.init()
screen_width = 1280
screen_height = 720
pygame.display.set_caption('Квадрат_иллюзия')
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0)]
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x = screen_width
    y = screen_height
    pygame.draw.rect(screen, COLORS, (x, y, 100, 100))
    pygame.draw.rect(screen, COLORS, (x + 25, y + 25, 50, 50))
    pygame.display.flip()