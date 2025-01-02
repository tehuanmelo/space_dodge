import pygame
import random
import time

from os.path import join

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")
BG_ORIGIN = pygame.image.load(join("assets/images", "bg.jpeg"))
BG = pygame.transform.scale(BG_ORIGIN, (WIDTH, HEIGHT))

def draw():
    WIN.blit(BG, (0,0))  
    pygame.display.update()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                running = False
                break
        draw()
    pygame.quit()


if __name__ == "__main__":
    main()