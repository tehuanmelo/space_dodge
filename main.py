import pygame
import random
import time

from os.path import join

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")
BG_ORIGIN = pygame.image.load(join("assets/images", "bg.jpeg"))
BG = pygame.transform.scale(BG_ORIGIN, (WIDTH, HEIGHT))

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 40
PLAYER_SPEED = 5

def draw(player):
    WIN.blit(BG, (0,0)) 
    pygame.draw.rect(WIN, 'orange', player)
     
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    
    player = pygame.Rect(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
    player.midbottom = player.midbottom = (WIDTH/2, HEIGHT)
    
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                running = False
                break
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and player.x + PLAYER_WIDTH + PLAYER_SPEED < WIDTH:
            player.x += PLAYER_SPEED
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= PLAYER_SPEED
                
        draw(player)
        
    pygame.quit()


if __name__ == "__main__":
    main()