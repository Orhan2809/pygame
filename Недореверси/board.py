import random
import pygame


def rect(screen, color, rect_pos_x, rect_pos_y, side, thickness):
    pygame.draw.rect(screen, pygame.Color(color),
                     (rect_pos_x, rect_pos_y, side, side), width=thickness)


class Board:

    def __init__(self, columns, rows):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("Клетчатое поле")
        self.one_click = 0
        self.win_color = "Красные", "Синие"
        self.running = True
        self.rgb_check = 0
        self.white_list_check = set()
        self.x, self.y = 50, 0
        self.side = 50
        self.position_x, self.position_y = 0, 0
        self.coor = None
        self.number_of_columns, self.number_of_rows = columns, rows
        self.white_list = []
        self.cellular_field()

    def cellular_field(self):
        for i in range(self.number_of_rows):
            self.y += self.side
            self.x = 50
            columns_list = []
            for j in range(self.number_of_columns):
                rect(self.screen, pygame.Color("#ffffff"), self.x, self.y, self.side, 1)
                if random.randint(1, 2) == 1:
                    columns_list.append(1)
                    color = "#ff0000"
                else:
                    columns_list.append(2)
                    color = "#0000ff"
                pygame.draw.circle(self.screen, pygame.Color(color),
                                   (self.x + 25, self.y + 25), 23)
                self.x += self.side
                pygame.display.flip()
            self.position_x = self.x
            self.white_list.append(columns_list)
        self.position_y = self.y + self.side
