# Space Dodge 

import pygame
import random
import time

from os.path import join

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Dodge")
BG_ORIGIN = pygame.image.load(join("assets/images", "bg.jpeg"))
BG = pygame.transform.scale(BG_ORIGIN, (WINDOW_WIDTH, WINDOW_HEIGHT))

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
PLAYER_SPEED = 5

STAR_WIDTH, STAR_HEIGHT, STAR_SPEED = 10, 20, 5

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.original_image = pygame.image.load(join("assets/images", "rocket.png"))
        self.image = pygame.transform.scale(self.original_image, (self.original_image.get_width() // 4, self.original_image.get_height() // 5))
        self.rect = self.image.get_frect(midbottom=(WINDOW_WIDTH/2, WINDOW_HEIGHT-5))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x + self.width + self.speed < WINDOW_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        

class Missile(pygame.sprite.Sprite):
    def __init__(self, missile, groups, pos):
        super().__init__(groups)
        self.original_image = missile
        self.image = pygame.transform.rotate(self.original_image, 180)  # Rotate the scaled image by 180 degrees
        self.rect = self.image.get_rect(midbottom=pos)
        # self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5
        
    def update(self):
        self.rect.bottom += self.speed
        if self.rect.top > WINDOW_HEIGHT + 100:
            self.kill()
            
        
def timer_display(start_time):
    font = pygame.font.Font(join("assets/fonts", "chopsic.otf"), 40)
    current_time = (pygame.time.get_ticks() - start_time) // 1000
    font_surf = font.render(f"Time: {current_time:3}", True, "white")
    font_rect = font_surf.get_rect(topleft=(10,10))
    WIN.blit(font_surf, font_rect)


def colision(player, all_missiles, custom_font, game_music):
    if pygame.sprite.spritecollide(player, all_missiles, True, pygame.sprite.collide_mask):
        lost_text = custom_font.render("You lost", True, "white")
        lost_text_rect = lost_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        WIN.blit(lost_text, lost_text_rect)
        pygame.display.update()
        game_music.stop()
        pygame.time.delay(4000)
        return True
    return False
    
       
def game():
    pygame.init()
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    
    # imports 
    all_sprites = pygame.sprite.Group()
    all_missiles = pygame.sprite.Group()
    player = Player(all_sprites)
    missiles = [pygame.image.load(join("assets/images/laser", f"{i}.png")) for i in range(1,17)]
    game_music = pygame.mixer.Sound(join("assets/audio", "mountainclimbing.wav"))
    game_music.play(loops=-1)
    custom_font = pygame.font.Font(join("assets/fonts", "chopsic.otf"), 40)
    
    missile_timer_cooldown = 2000
    missile_timer_creation = 0
    
    running = True
    while running:
        
        missile_timer_creation += clock.tick(60)
        
        if missile_timer_creation >= missile_timer_cooldown:
            for _ in range(3):
                x = random.randint(0, WINDOW_WIDTH)
                Missile(random.choice(missiles), (all_sprites, all_missiles), (x, -10))
            missile_timer_creation = 0
            missile_timer_cooldown = max(200, missile_timer_cooldown - 50)
            
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                running = False
                break
       
        all_sprites.update()
        
        WIN.blit(BG, (0,0))
        
        timer_display(start_time)
        
        all_sprites.draw(WIN)
        
        if colision(player, all_missiles, custom_font, game_music):
            break
        
        pygame.display.update()
        
    return running
        
        
def main():
    while True:
        if not game():
            break   
    pygame.quit()


if __name__ == "__main__":
    main()