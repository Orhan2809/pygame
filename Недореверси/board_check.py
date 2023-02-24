import pygame


class BoardCheck:
    def __init__(self):
        self.running = True
        self.coor = 0, 0

    def check_quit(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.coor = event.pos
                    self.position(self.coor)
        pygame.quit()