import pygame


class Image_sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.all_sprite = pygame.sprite.Group()
        self.sprite_hero = pygame.sprite.Sprite(self.all_sprite)
        self.sprite_hero.image = pygame.image.load("data/gameover.png")
        self.sprite_hero.rect = self.sprite_hero.image.get_rect()
        self.sprite_hero.rect.x = -600
        self.sprite_hero.rect.y = 0


class Game_sprite(Image_sprite):
    pygame.init()

    def __init__(self):
        super().__init__()
        self.running = True
        self.fps = 20
        self.screen = pygame.display.set_mode((600, 300))
        self.screen_2 = pygame.Surface(self.screen.get_size())
        self.screen_2.fill(pygame.Color("#0000ff"))
        self.clock = pygame.time.Clock()
        self.num = 0
        self.sprite()

    def sprite(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.sprite_hero.rect.x < -20 and self.num != 11:
                self.sprite_hero.rect.x += 10
            if self.sprite_hero.rect.x == -20 and self.num != 11:
                self.num += 1
            if self.num == 10:
                self.sprite_hero.rect.x += 20
                self.num += 1

            self.screen.blit(self.screen_2, (0, 0))
            self.all_sprite.draw(self.screen)
            self.clock.tick(self.fps)
            pygame.display.flip()
        pygame.quit()


Game_sprite()