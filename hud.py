import pygame

pygame.init()

class SelectList:
  def __init__(self, window, options, position, size):
    self.window = window
    self.options = options
    self.position = position
    self.size = size
    self.open = False
    self.selected_option = None
    self.police = pygame.font.Font("./fonts/Orbitron.ttf", int(size[1]/2))

  def display(self):
    bc_color = (210, 210, 210)
    txt_color = (50, 50, 50)
    width = self.size[0]
    height = self.size[1]
    x = self.position[0]
    y = self.position[1]

    pygame.draw.rect(self.window, bc_color, (x, y - height // 2, width, height))

    txt = "Difficultée"
    txt_area = self.police.render(txt, True, txt_color)
    self.window.blit(txt_area, (x + width // 2 - txt_area.get_width() // 2, y - txt_area.get_height() // 2))

  def display_difficulties(self):
    # Box
    bc_color = (50, 50, 50)
    x_box = self.position[0]
    y_box = self.position[1] // 2 + self.size[1] + 5
    width = self.size[0]
    height = self.size[1] * len(self.options) + (len(self.options) + 1) * 2

    pygame.draw.rect(self.window, bc_color, (x_box, y_box, width, height))

    # Element
    bc_element = (210, 210, 210)
    txt_color = (50, 50, 50)
    for difficulty in range(len(self.options)):
      x = x_box + 2
      y = y_box + (difficulty + 1) * 2 + difficulty * self.size[1]
      width = self.size[0] - 4
      height = self.size[1]
      police = pygame.font.Font("./fonts/Orbitron.ttf", int(height/2.2))

      txt_difficulty = str(list(self.options.keys())[difficulty])
      txt_difficulty_area = police.render(txt_difficulty, True, txt_color)

      pygame.draw.rect(self.window, bc_element, (x, y, width, height))

      self.window.blit(txt_difficulty_area, (x + (width - txt_difficulty_area.get_width()) // 2, 
                                             y + (height - txt_difficulty_area.get_height()) // 2))

  def mouse_clic(self, mouse_position):
    if mouse_position[0] >= self.position[0] and mouse_position[0] <= self.position[0] + self.size[0]:
      if mouse_position[1] >= self.position[1] // 2 and mouse_position[1] <= self.position[1] + self.size[1] // 2:
        self.open = not self.open
      elif self.open:
        for difficulty in range(len(self.options)):
          x = self.position[0] + 2
          y = self.position[1] // 2 + self.size[1] + 5 + \
              (difficulty + 1) * 2 + difficulty * self.size[1]
          width = self.size[0] - 4
          height = self.size[1]

          if mouse_position[0] >= x and mouse_position[0] <= x + width and mouse_position[1] >= y and mouse_position[1] <= y + height:
            self.selected_option = list(self.options.keys())[difficulty]
            # self.open = False
            print(self.selected_option)
            break

class Chronometer:

  def __init__(self, window, position):
    self.window = window
    self.position = position
    self.time = 0
    self.txt_time = ''

  def display(self):
    police = pygame.font.Font("fonts/SpaceMono-Regular.ttf", 36)
    self.time = int(pygame.time.get_ticks() / 1000)

    self.txt_time = f"0:{self.time}"
    if self.time > 60:
        self.txt_time = f"{int(self.time / 60)} : {self.time % 60}"

    txt_time_area = police.render(str(self.txt_time).encode(), True, (255, 255, 255))

    self.window.blit(txt_time_area, 
                     (self.position[0] // 2 - (txt_time_area.get_width() // 2), 
                      self.position[1] // 2 - (txt_time_area.get_height() // 2)))
    
  def restart(self):
    self.time = 0


def render_hud(window):
    window.fill("black")
    window.fill(DARK_GRAY, (0, 0, CELL_SIZE * GRID_SIZE, TOP_SIZE))

    difficulty_select_list.display()
    chronometer.display()
