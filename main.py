import pygame, random, time, hud.hud as hud, hud.menu as menu, game
from consts import *

pygame.init()
pygame.display.set_caption("Démineur")

menu = menu.Menu(DIFFICULTIES)
window = menu.load()

clock = pygame.time.Clock()

def bomb_generation(x, y):
    bombs_pos = []
    while len(bombs_pos) < BOMB_AMOUNT:
        bx = random.randint(0, GRID_SIZE - 1)
        by = random.randint(0, GRID_SIZE - 1)
        if bx > x-1 and bx < x+1 and by > y-1 and by < y+1:
            bombs_pos.append((bx, by))
            # bomb_list[by][bx] = -1
    
    proximity_values(bombs_pos)
    

def proximity_values(bombs_pos):
    for bx, by in bombs_pos:
        for i in range(9):
            lx = i % 3
            ly = i // 3
            print(bx - lx, by - ly)
            # if b
            # x - lx >= 0 and by - ly >= 0:
                # if(bomb_list[by - ly][bx - lx] != -1):
                #     bomb_list[by - ly][bx - lx] += 1

game = game.Game(window, DIFFICULTIES[DIFFICULTY])

# HUD VARIABLE
difficulty_select_list = hud.SelectList(window, DIFFICULTIES, (CELL_SIZE // 2, TOP_SIZE // 2), (130, TOP_SIZE // 2))
chronometer = hud.Chronometer(window, (GRID_SIZE * CELL_SIZE // 2, TOP_SIZE // 2))

police = pygame.font.Font("fonts/Orbitron.ttf", 36)
playing = True
first = True
clock.tick(30)
while playing:  # Main loop
    hud.render_hud(window, difficulty_select_list, chronometer)
    if menu.isLoaded:
        menu.display()

    # Display difficulties
    if difficulty_select_list.open :
        difficulty_select_list.display_difficulties()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if event.type == pygame.MOUSEBUTTONUP:
            (x, y) = pygame.mouse.get_pos()

            if menu.isLoaded:
                menu.clic((x, y))
            else:
                difficulty_select_list.mouse_clic((x, y))
                y -= TOP_SIZE

                if y < 0:
                    break

                # cell_value = game.grid[int(y / CELL_SIZE)][int(x / CELL_SIZE)]

                if event.button == 1:
                    if cell_value == -1:
                        if first:
                            print("Hey yo")
                            bomb_generation(x, y)
                            first = False
                        game.grid[int(y / CELL_SIZE)][int(x / CELL_SIZE)] = 1
                elif event.button == 3:
                    if cell_value == -1:
                        game.grid[int(y / CELL_SIZE)][int(x / CELL_SIZE)] = 2
                    else:
                        game.grid[int(y / CELL_SIZE)][int(x / CELL_SIZE)] = -1

    pygame.display.flip()

pygame.quit()
