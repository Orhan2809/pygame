import pygame
from board import Board
from board_check import BoardCheck

class BoardPosition(Board, BoardCheck):
    def __init__(self, columns, rows):
        super().__init__(columns, rows)
        self.check_quit()

    def position(self, pos):
        x = -1
        y = -1
        pos_x = pos[0]
        pos_y = pos[1]

        if self.side <= pos_y <= self.position_y and self.side <= pos_x <= self.position_x:
            for _ in range(self.number_of_columns):
                if pos_x >= self.side:
                    pos_x -= self.side
                    x += 1
            for t in range(self.number_of_rows):
                if pos_y >= self.side:
                    pos_y -= self.side
                    y += 1
            pos_white_y = self.side * (y + 1)
            pos_white_x = self.side * (x + 1)
            self.x = self.side
            self.y = self.side
            check_pos_y = 0
            coor = self.white_list[y][x]
            if self.rgb_check != coor:
                for h in range(self.number_of_columns):
                    check_pos_y += self.side
                    if coor == 1:
                        color = "#ff0000"
                    else:
                        color = "#0000ff"
                    if coor == 1 or check_pos_y == pos_white_x:
                        pygame.draw.circle(self.screen, pygame.Color(color),
                                           (self.x + self.side // 2, pos_white_y + self.side // 2), 23)
                    else:
                        pygame.draw.circle(self.screen, pygame.Color(color),
                                           (self.x + self.side // 2, pos_white_y + self.side // 2), 23)
                    self.white_list[y][h] = coor
                    self.x += self.side
                for g in range(self.number_of_rows):
                    if coor == 1:
                        color = "#ff0000"
                    else:
                        color = "#0000ff"
                    if coor == 1:
                        pygame.draw.circle(self.screen, pygame.Color(color),
                                           (pos_white_x + self.side // 2, self.y + self.side // 2), 23)
                    else:
                        pygame.draw.circle(self.screen, pygame.Color(color),
                                           (pos_white_x + self.side // 2, self.y + self.side // 2), 23)
                    self.white_list[g][x] = coor
                    self.y += self.side

                    pygame.display.flip()
                self.rgb_check = coor
        for j in range(len(self.white_list)):
            for i in range(len(self.white_list)):
                self.white_list_check.add(self.white_list[j][i])
        if len(self.white_list_check) == 1:
            self.running = False
            print(self.win_color[int(str(*self.white_list_check)) - 1],"выиграли!")