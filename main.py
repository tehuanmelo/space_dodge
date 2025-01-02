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
        self.image = pygame.image.load(join("assets/images", "spaceship.png"))
        self.rect = self.image.get_frect(midbottom=(WINDOW_WIDTH/2, WINDOW_HEIGHT))
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
        

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.width = 10
        self.height = 20
        self.image = pygame.Surface((self.width, self.height)).convert_alpha()
        self.rect = self.image(midbottom=pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = pygame.Vector2(0,1)
        self.speed = 5
        
    def update(self):
        self.rect.center += self.direction * self.speed
        if self.rect.bottom == WINDOW_HEIGHT - 100:
            self.kill()

    
# def draw(start_time, player, self.rect, font, stars):
#     WIN.blit(BG, (0,0)) 
    
#     for star in stars:
#         WIN.blit()
        
#     # pygame.draw.rect(WIN, 'orange', player)
#     WIN.blit(player, self.rect)
    
#     current_time = (pygame.time.get_ticks() - start_time) // 1000
#     font_surf = font.render(f"Time: {current_time:3}", True, "white")
#     font_rect = font_surf.get_rect(topleft=(10,10))
#     WIN.blit(font_surf, font_rect)
    
#     pygame.display.update()


def game():
    pygame.init()
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    
    hit = False
    
    all_sprites = pygame.sprite.Group()
    player = Player(all_sprites)
    
    # game_music = pygame.mixer.Sound(join("assets/audio", "mountainclimbing.wav"))
    # game_music.play(loops=-1)
    
    # # player = pygame.Rect(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
    # # player.midbottom = (WIDTH/2, HEIGHT)
    # player = pygame.image.load(join("assets/images", "spaceship.png")).convert_alpha()
    # self.rect = player.get_frect(midbottom=(WIDTH/2, HEIGHT))
    # player_mask = pygame.mask.from_surface(player)
    
    # custom_font = pygame.font.Font(join("assets/fonts", "chopsic.otf"), 40)
    
    # star_timer_cooldown = 2000
    # star_timer_creation = 0
    
    # stars = []
    
    running = True
    while running:
        pass
        dt = clock.tick(60) / 1000
        
        # if star_timer_creation >= star_timer_cooldown:
        #     for _ in range(3):
        #         x = random.randint(0, WIDTH - STAR_WIDTH)
        #         # star = pygame.Rect(x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
        #         star_surface = pygame.Surface((STAR_WIDTH, STAR_HEIGHT)).convert_alpha()
        #         star_surface.fill("lightblue")  # Assuming white stars for simplicity
        #         star_rect = star_surface.get_frect(midbottom=(x, -STAR_HEIGHT))
        #         star_mask = pygame.mask.from_surface(star_surface)
        #         stars.append((star, star_rect, star_mask))
        #     star_timer_creation = 0
        #     star_timer_cooldown = max(200, star_timer_cooldown - 50)
            
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                running = False
                break
            
        
            
        # for star in stars[:]:
        #     star.y += STAR_SPEED
        #     if star.y > HEIGHT:
        #         stars.remove(star)
        #     elif star.y + STAR_WIDTH >= self.rect.y and player_mask.overlap():
        #         stars.remove(star)
        #         hit = True
                
        # if hit:
        #     lost_text = custom_font.render("You lost", True, "white")
        #     lost_text_rect = lost_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        #     WIN.blit(lost_text, lost_text_rect)
        #     pygame.display.update()
        #     game_music.stop()
        #     pygame.time.delay(4000)
        #     break
                
        # draw(start_time, player, self.rect, custom_font, stars)
        all_sprites.update()
        WIN.blit(BG, (0,0))
        all_sprites.draw(WIN)
        pygame.display.update()
        
    return running
        
        
def main():
    while True:
        if not game():
            break   
    pygame.quit()


if __name__ == "__main__":
    main()