import pygame, spritesheet
from consts import *

def get_grid(default):
    return [[default for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]

class Game:
    def __init__(self, window, difficulty):
        self.window = window
        self.difficulty = difficulty
        self.bomb_grid = get_grid(0)
        self.grid = get_grid(-1)
        self.animation_frame = 0
        self.sheet = spritesheet.Spritesheet("sprites/flag.png")


    def render(self, ):
        global animation_frame

        y = 0
        for i in range(len(grid)):

            for x in range(len(grid[y])):
                cell_value = grid[y][x]
                if cell_value == 1:
                    window.fill(GRAY, (x * CELL_SIZE, y * CELL_SIZE + TOP_SIZE, CELL_SIZE, CELL_SIZE + TOP_SIZE))

                elif cell_value == 2:
                    window.fill(BLUE if (x + y) % 2 == 0 else GREEN,
                                (x * CELL_SIZE, y * CELL_SIZE + TOP_SIZE, CELL_SIZE, CELL_SIZE + TOP_SIZE))
                    window.blit(
                        pygame.transform.scale(
                            sheet.image_at((
                                int(animation_frame) * 16, 0, 16, 16
                            )),
                            (CELL_SIZE, CELL_SIZE)
                        ), (x * CELL_SIZE, y * CELL_SIZE + TOP_SIZE)
                    )
                else:
                    window.fill(BLUE if (x + y) % 2 == 0 else GREEN,
                                (x * CELL_SIZE, y * CELL_SIZE + TOP_SIZE, CELL_SIZE, CELL_SIZE + TOP_SIZE))

                pol = pygame.font.Font("fonts/Orbitron.ttf", 46)
                txt = pol.render(str(bomb_list[y][x]), True, (0, 0, 0))
                window.blit(pygame.transform.scale(txt, (CELL_SIZE, CELL_SIZE)), (x * CELL_SIZE, y * CELL_SIZE + TOP_SIZE, CELL_SIZE, CELL_SIZE + TOP_SIZE))

            y += 1

            animation_frame = (animation_frame + 0.0003) % 4
