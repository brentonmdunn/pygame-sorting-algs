import pygame
import random

WIDTH = 500
TOTAL_COLS = 100
FPS = 400
GAP = WIDTH / TOTAL_COLS
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Selection Sort Algorithm Visualizer!')
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
DARK_AQUA = (38, 70, 83)
YELLOW = (233, 196, 106)
DARK_ORANGE = (231, 111, 81)
AQUA = (42, 157, 143)

CURSOR_COLOR = DARK_ORANGE
BACKGROUND_COLOR = DARK_AQUA
COLUMN_COLOR = YELLOW
TEMP = AQUA


class Col(object):
    def __init__(self, col_number, height):
        self.col_number = col_number
        self.height = height
        self.color = WHITE
        self.x = GAP * col_number

    def __lt__(self, other):
        return self.height > other.height       # is reversed because height is space from top not height of column

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.height, GAP, WIDTH-self.height))

    def change_color(self, color):
        if color == DARK_AQUA:
            self.color = DARK_AQUA
        elif color == DARK_ORANGE:
            self.color = DARK_ORANGE
        elif color == AQUA:
            self.color = AQUA
        elif color == YELLOW:
            self.color = YELLOW
        elif color == WHITE:
            self.color = WHITE


def draw(win, layout):
    win.fill(BACKGROUND_COLOR)
    for i in range(len(layout)):
        layout[i].draw(win)
    pygame.display.update()


def main():
    run = True
    layout = []
    heights = []
    for i in range(TOTAL_COLS):
        rand_int = random.randint(int(WIDTH * .05), int(WIDTH - WIDTH * .05))       # padding so columns aren't too high
        heights.append(rand_int)
    for i in range(TOTAL_COLS):
        layout.append(Col(i, heights[i]))
    draw(WIN, layout)
    next_sort = 0
    step = 0
    first = True
    min_index = layout[0]
    min_index.change_color(TEMP)
    while run:
        if first:
            cursor = next_sort + 1
            first = False
        min_index = next_sort

        if step == 0:
            try:
                if cursor - 1 != next_sort:
                    layout[cursor-1].change_color(WHITE)                 # change color back to white after cursor
                layout[cursor].change_color(CURSOR_COLOR)                # color of leading cursor
                if layout[cursor] < layout[next_sort]:
                    layout[min_index].change_color(WHITE)
                    min_index = cursor
                    layout[min_index].change_color(TEMP)
                cursor += 1
            except IndexError:
                first = True
                step += 1
            try:
                temp = layout[next_sort]
                layout[next_sort] = layout[min_index]
                layout[min_index] = temp
            except IndexError:
                pass
        if step == 1:
            try:
                layout[min_index].change_color(COLUMN_COLOR)
                for n in range(len(layout)):
                    layout[n].x = n * GAP
                draw(WIN, layout)
                next_sort += 1
                step = 0
            except IndexError:
                pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw(WIN, layout)
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
