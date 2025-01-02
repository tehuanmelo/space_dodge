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
    
    player = pygame.Rect(WIDTH/2-PLAYER_WIDTH/2, HEIGHT-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                running = False
                break
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            x = player.x + PLAYER_SPEED
            if x < WIDTH - PLAYER_WIDTH:
                player.x += PLAYER_SPEED
        if keys[pygame.K_LEFT]:
            x = player.x - PLAYER_SPEED
            if x > 0:
                player.x -= PLAYER_SPEED
                
        draw(player)
        
    pygame.quit()


if __name__ == "__main__":
    main()