import pygame
running = True
fps = 20


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.coor = 0
        self.all_sprite = pygame.sprite.Group()
        self.sprite_hero = pygame.sprite.Sprite(self.all_sprite)
        self.image = pygame.image.load("data/car2.png")
        self.sprite_hero.image = self.image
        self.sprite_hero.rect = self.sprite_hero.image.get_rect()
        self.sprite_hero.rect.x = 0
        self.sprite_hero.rect.y = 0


class Drive(Car):
    pygame.init()

    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((600, 95))
        self.screen_2 = pygame.Surface(self.screen.get_size())
        self.screen_2.fill(pygame.Color("#ffffff"))
        self.num, self.number = 0, 0
        self.clock = pygame.time.Clock()
        self.driver()

    def driver(self):
        global running
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if (self.sprite_hero.rect.x == 450 or self.sprite_hero.rect.x == 0) and self.number == 1:
                self.image = pygame.transform.flip(self.image, True, False)
                self.sprite_hero.image = self.image

            if self.sprite_hero.rect.x == 450:
                self.num = 1

            if self.sprite_hero.rect.x == 0:
                self.num, self.number = 0, 1

            if self.num == 1:
                self.sprite_hero.rect.x -= 9
            else:
                self.sprite_hero.rect.x += 9
            self.screen.blit(self.screen_2, (0, 0))
            self.all_sprite.draw(self.screen)
            self.clock.tick(fps)
            pygame.display.flip()
        pygame.quit()


Drive()
