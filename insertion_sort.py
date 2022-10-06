import pygame
import random
import pygame_gui
import sys

WIDTH = 1000
TOTAL_COLS = 100
FPS = 400
GAP = WIDTH / TOTAL_COLS
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Insertion Sort Algorithm Visualizer!')
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
DARK_AQUA = (38, 70, 83)
YELLOW = (233, 196, 106)
DARK_ORANGE = (231, 111, 81)

CURSOR_COLOR = DARK_ORANGE
BACKGROUND_COLOR = DARK_AQUA
COLUMN_COLOR = YELLOW

# ------

# MANAGER = pygame_gui.UIManager((WIDTH, WIDTH))

# TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(
#     (350, 275), (900, 50)), manager=MANAGER, object_id="#main_text_entry")

# ------


class Col(object):
    def __init__(self, col_number, height):
        self.col_number = col_number
        self.height = height
        self.color = WHITE
        self.x = GAP * col_number

    def __lt__(self, other):
        # is reversed because height is space from top not height of column
        return self.height > other.height

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.height, GAP, WIDTH-self.height))

    def change_color(self, color):
        if color == DARK_AQUA:
            self.color = DARK_AQUA
        elif color == YELLOW:
            self.color = YELLOW
        elif color == DARK_ORANGE:
            self.color = DARK_ORANGE


def draw(win, layout):
    win.fill(BACKGROUND_COLOR)
    for i in range(len(layout)):
        layout[i].draw(win)
    pygame.display.update()


def insertion_sort():
    run = True

    # ------

    # UI_REFRESH_RATE = clock.tick(60)/1000

    # ------

    layout = []
    heights = []
    for i in range(TOTAL_COLS):
        # padding so columns aren't too high
        rand_int = random.randint(int(WIDTH * .05), int(WIDTH - WIDTH * .05))
        heights.append(rand_int)
    for i in range(TOTAL_COLS):
        layout.append(Col(i, heights[i]))
    draw(WIN, layout)
    step = 0
    forward = 1
    while run:
        if step == 0:
            backward = forward
            step += 1
        elif step == 1:
            try:
                if layout[backward] < layout[backward - 1] and backward > 0:
                    temp = layout[backward - 1]
                    layout[backward - 1] = layout[backward]
                    layout[backward] = temp
                    backward -= 1
                else:
                    step -= 1
                    forward += 1
            except IndexError:
                pass
            for n in range(len(layout)):
                layout[n].x = n * GAP
        try:
            for k in range(forward):
                layout[k].change_color(COLUMN_COLOR)
            layout[backward].change_color(CURSOR_COLOR)
        except IndexError:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    blank_page()
        draw(WIN, layout)
        clock.tick(FPS)
    pygame.quit()


def blank_page():
    clock.tick(FPS)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    insertion_sort()

        WIN.fill("white")
        pygame.display.update()


def main():
    insertion_sort()


if __name__ == '__main__':
    main()
