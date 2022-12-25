import pygame

running = True
fps = 60


def display_mouse(coor):
    if coor > 0:
        sprite_group.draw(screen)


if __name__ == "__main__":
    pygame.init()
    sprite_group = pygame.sprite.Group()
    sprite_mouse = pygame.sprite.Sprite(sprite_group)
    sprite_mouse.image = pygame.image.load("data/arrow.png")
    sprite_mouse.rect = sprite_mouse.image.get_rect()
    screen = pygame.display.set_mode((500, 500))
    screen2 = pygame.Surface(screen.get_size())
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    x, y = 0, 0
    coor = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
        if pygame.mouse.get_focused():
            sprite_mouse.rect.x = x
            sprite_mouse.rect.y = y
            coor = 1
        else:
            coor = 0
        screen.blit(screen2, (0, 0))
        display_mouse(coor)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()