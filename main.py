import pygame, hud.hud as hud, hud.menu as menu, game
from consts import *

pygame.init()
pygame.display.set_caption("Démineur")

menu = menu.Menu(DIFFICULTIES)
window = menu.load()

clock = pygame.time.Clock()


# HUD VARIABLE
difficulty_select_list = hud.SelectList(window, DIFFICULTIES, (cell_size // 2, TOP_SIZE // 2), (130, TOP_SIZE // 2))
chronometer = hud.Chronometer(window)

police = pygame.font.Font("fonts/Orbitron.ttf", 36)
first = True
clock.tick(30)

while menu.isLoaded:
    menu.display()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONUP:
            (x, y) = pygame.mouse.get_pos()

            menu.clic((x, y))
        

    pygame.display.flip()


if menu.difficulty_selected == "Quitter":
    pygame.quit()
    exit()

game = game.Game(window, DIFFICULTIES[menu.difficulty_selected])
chronometer.setup_position()
chronometer.restart()

while game.playing:  # Main loops
    hud.render_hud(window, difficulty_select_list, chronometer)

    # Display difficulties
    if difficulty_select_list.open :
        difficulty_select_list.display_difficulties()
    else:
        game.render()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.playing = False

        if event.type == pygame.MOUSEBUTTONUP:
            (x, y) = pygame.mouse.get_pos()

            if not difficulty_select_list.open:
                game.click(x, y, event)
            
            difficulty_select_list.mouse_clic((x, y))
        

    pygame.display.flip()

pygame.quit()
