import pygame, time
from consts import *

WIDTH = 400
HEIGHT = 550

class Menu:
  def __init__(self, difficulties, path_img_bc = "img/background.png"):
    self.difficulties = difficulties
    self.path_img_bc = path_img_bc
    self.isLoaded = False
    self.difficulty_selected = False

  def load(self):
    self.isLoaded = True
    self.window = pygame.display.set_mode((WIDTH, HEIGHT))
    self.img_bc = pygame.image.load(self.path_img_bc).convert()

    self.x_bc = 1
    self.direction = 1

    self.last_tick = time.time()

    return self.window

  def display(self):
    if self.isLoaded:
      # Background Image
      self.window.blit(self.img_bc, (self.x_bc, 0))

      # Mouving Image
      current_tick = time.time()
      elapsed_time = current_tick - self.last_tick

      if elapsed_time >= 0.03:
        self.x_bc += self.direction

        if self.x_bc <= -360:
          self.direction = 1
        elif self.x_bc >= 0:
          self.direction = -1

        self.last_tick = current_tick

      self.load_difficulties()

  def load_difficulties(self):
    if self.isLoaded:
      self.dico_position = {}

      police = pygame.font.Font('./fonts/Orbitron.ttf', 30)
      bc_color = (220, 220, 220)
      txt_color = (50, 50, 50)

      x = WIDTH // 2
      width_difficulty = 150
      height_difficulty = 70
      for difficulty in range(len(self.difficulties) + 1):
        y = HEIGHT // 2 - (((len(self.difficulties) + 1) - difficulty) * height_difficulty) // 2 + 60 * difficulty
        
        if difficulty < len(self.difficulties):
          txt = str(list(self.difficulties.keys())[difficulty])
        else:
          txt = "Quitter"
          width_difficulty = 120
          height_difficulty = 55
          bc_color = RED
          txt_color = (220, 220, 220)
          police = pygame.font.Font('./fonts/Orbitron.ttf', 25)

        txt_area = police.render(txt, True, txt_color)

        pygame.draw.rect(self.window, bc_color, (x - width_difficulty // 2,
                        y - height_difficulty // 2, width_difficulty, height_difficulty))
        self.window.blit(txt_area, (x - txt_area.get_width() //
                        2, y - txt_area.get_height() // 2))

        self.dico_position[f'{txt}'] = [x - width_difficulty // 2, x +
                                      width_difficulty // 2, y - height_difficulty // 2, y + height_difficulty // 2]

  def clic(self, position_clic):
    if self.isLoaded:
      for difficulty, position in self.dico_position.items():
        if position[0] <= position_clic[0] <= position[1] and position[2] <= position_clic[1] <= position[3]:
          self.difficulty_selected = difficulty
          self.isLoaded = False

if __name__ == "__main__":
  pass