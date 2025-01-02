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


    
def draw(player, font):
    WIN.blit(BG, (0,0)) 
    pygame.draw.rect(WIN, 'orange', player)
    
    current_time = pygame.time.get_ticks() // 1000
    font_surf = font.render(f"Time: {current_time:3}", True, "white")
    font_rect = font_surf.get_rect(topleft=(10,10))
    WIN.blit(font_surf, font_rect)
    
    pygame.display.update()


def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    player = pygame.Rect(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
    player.midbottom = player.midbottom = (WIDTH/2, HEIGHT)
    
    font = pygame.font.Font(join("assets/fonts/chopsic", "Chopsic.otf"), 40)
    
    
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
                
        draw(player, font)
        
        
        
    pygame.quit()


if __name__ == "__main__":
    main()