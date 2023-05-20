import pygame
from consts import *

pygame.init()

WIDTH = 400
HEIGHT = 550

def load_difficulties(window, difficulties):
  dico_return = {}

  police = pygame.font.Font('./fonts/Orbitron.ttf', 30)
  bc_color = (220, 220, 220)
  txt_color = (50, 50, 50)

  x = WIDTH // 2
  width_difficulty = 150
  height_difficulty = 70
  for difficulty in range(len(difficulties)):
    y = HEIGHT // 2 - ((len(difficulties) - difficulty) * height_difficulty) // 2 + 70 * difficulty
    
    txt = str(list(difficulties.keys())[difficulty])
    txt_area = police.render(txt, True, txt_color)

    pygame.draw.rect(window, bc_color, (x - width_difficulty // 2, y - height_difficulty // 2, width_difficulty, height_difficulty))
    window.blit(txt_area, (x - txt_area.get_width() // 2, y - txt_area.get_height() // 2))

    dico_return[f'{txt}'] = [x - width_difficulty // 2, x + width_difficulty // 2, y - height_difficulty // 2, y + height_difficulty // 2]

  return dico_return

def clic_menu(position_clic, dico_position):
  for difficulty, position in dico_position.items():
    if position[0] <= position_clic[0] <= position[1] and position[2] <= position_clic[1] <= position[3]:
      print(difficulty)

def load_menu():
  menu = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Démineur")

  img_bc = pygame.image.load("img/background.png").convert()

  clock = pygame.time.Clock()
  running = True
  x_bc = 1
  direction = 1
  last_tick = pygame.time.get_ticks()
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
    
    # Background Image
    menu.blit(img_bc, (x_bc, 0))

    # Mouving Image
    current_tick = pygame.time.get_ticks()
    elapsed_time = current_tick - last_tick

    if elapsed_time >= 4:
      x_bc += direction

      if x_bc <= -360:
        direction = 1
      elif x_bc >= 0:
        direction = -1

    last_tick = current_tick

    # Loader
    difficulties_position = load_difficulties(menu, DIFFICULTIES)

    # Clic
    if event.type == pygame.MOUSEBUTTONUP:
        (x, y) = pygame.mouse.get_pos()
        clic_menu((x, y), difficulties_position)

    pygame.display.flip()
    clock.tick(60)

  pygame.quit()

if __name__ == "__main__":
  load_menu()