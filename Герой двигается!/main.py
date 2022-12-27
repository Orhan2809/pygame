import pygame

running = True

all_sprite = pygame.sprite.Group()
sprite_hero = pygame.sprite.Sprite(all_sprite)
sprite_hero.image = pygame.image.load("data/creature.png")
sprite_hero.rect = sprite_hero.image.get_rect()
sprite_hero.rect.x = 200
sprite_hero.rect.y = 200

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    screen_2 = pygame.Surface(screen.get_size())
    screen_2.fill(pygame.Color("#ffffff"))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sprite_hero.rect.y = sprite_hero.rect.y - 10
                if event.key == pygame.K_DOWN:
                    sprite_hero.rect.y = sprite_hero.rect.y + 10
                if event.key == pygame.K_LEFT:
                    sprite_hero.rect.x = sprite_hero.rect.x - 10
                if event.key == pygame.K_RIGHT:
                    sprite_hero.rect.x = sprite_hero.rect.x + 10
        screen.blit(screen_2, (0, 0))
        all_sprite.draw(screen)
        pygame.display.flip()
    pygame.quit()