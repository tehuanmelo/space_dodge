# Space Dodge 

import pygame
import random
import time

from os.path import join

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")
BG_ORIGIN = pygame.image.load(join("assets/images", "bg.jpeg"))
BG = pygame.transform.scale(BG_ORIGIN, (WIDTH, HEIGHT))

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
PLAYER_SPEED = 5


    
def draw(start_time, player, font, stars):
    WIN.blit(BG, (0,0)) 
    
    for star in stars:
        pygame.draw.rect(WIN, "lightblue", star)
        
    pygame.draw.rect(WIN, 'orange', player)
    
    current_time = (pygame.time.get_ticks() - start_time) // 1000
    font_surf = font.render(f"Time: {current_time:3}", True, "white")
    font_rect = font_surf.get_rect(topleft=(10,10))
    WIN.blit(font_surf, font_rect)
    
    pygame.display.update()


def game():
    print("start")
    pygame.init()
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    
    hit = False
    
    player = pygame.Rect(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
    player.midbottom = player.midbottom = (WIDTH/2, HEIGHT)
    
    custom_font = pygame.font.Font(join("assets/fonts", "chopsic.otf"), 40)
    
    star_timer_cooldown = 2000
    star_timer_creation = 0
    STAR_WIDTH, STAR_HEIGHT, STAR_SPEED = 10, 20, 5
    stars = []
    
    running = True
    while running:
        star_timer_creation += clock.tick(60)
        
        if star_timer_creation >= star_timer_cooldown:
            for _ in range(3):
                x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            star_timer_creation = 0
            star_timer_cooldown = max(200, star_timer_cooldown - 50)
            
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                running = False
                break
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and player.x + PLAYER_WIDTH + PLAYER_SPEED < WIDTH:
            player.x += PLAYER_SPEED
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= PLAYER_SPEED
            
        for star in stars[:]:
            star.y += STAR_SPEED
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + STAR_WIDTH >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                
        if hit:
            lost_text = custom_font.render("You lost", True, "white")
            lost_text_rect = lost_text.get_rect(center=(WIDTH/2, HEIGHT/2))
            WIN.blit(lost_text, lost_text_rect)
            pygame.display.update()
            pygame.time.delay(4000)
            break
                
        draw(start_time, player, custom_font, stars)
        
    return running
        
        
def main():
    while True:
        if not game():
            break   
    pygame.quit()


if __name__ == "__main__":
    main()