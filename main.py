import pygame, random, time
import hud

class Spritesheet:
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error as message:
            print('Unable to load spritesheet image:', filename)
            raise SystemExit(message)

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey="white"):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey=None):
        "Loads multiple images, supply a list of coordinates"
        return [self.image_at(rect, colorkey) for rect in rects]

    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey=None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

GRID_SIZE = 7
CELL_SIZE = 50
BOMB_AMOUNT = int((GRID_SIZE ** 2) / 8)

TOP_SIZE = 75

BLUE = (132, 196, 209)
GREEN = (50, 144, 143)
GRAY = (232, 246, 238)
DARK_GRAY = (128, 128, 128)

DIFFICULTIES = { 
    "easy": {"grid_size": 10, "cell_size": 50}, 
    "medium": {"grid_size": 15, "cell_size": 35}, 
    "hard": {"grid_size": 20, "cell_size": 30}
}


DIFFICULTY = DIFFICULTIES[input("Difficulty ? ")]

GRID_SIZE = DIFFICULTY["grid_size"]
CELL_SIZE = DIFFICULTY["cell_size"]
BOMB_AMOUNT = int((GRID_SIZE ** 2) / 8)


def get_grid(default):
    return [[default for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]


bomb_list = get_grid(0)  # A list that will contains the bombs (-1) and the number of bomb around
grid = get_grid(-1)

pygame.init()
window = pygame.display.set_mode((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE + TOP_SIZE))
pygame.display.set_caption("Démineur")
clock = pygame.time.Clock()

sheet = Spritesheet("sprites/flag.png")

animation_frame = 0

# HUD VARIABLE
difficulty_select_list = hud.SelectList(window, DIFFICULTIES, (CELL_SIZE // 2, TOP_SIZE // 2), (130, TOP_SIZE // 2))
police = pygame.font.Font("fonts/Orbitron.ttf", 36)
chronometer_start = 0

def render_hud():
    window.fill("black")
    window.fill(DARK_GRAY, (0, 0, CELL_SIZE * GRID_SIZE, TOP_SIZE))

    difficulty_select_list.display()

    chronometer_time = int((pygame.time.get_ticks() - chronometer_start) / 1000)
    if chronometer_time > 60 :
        chronometer_time = f"{int(chronometer_time / 60)} : {chronometer_time % 60}"
    chronometer_text = police.render(str(chronometer_time).encode(), True, (255, 255, 255))

    window.blit(chronometer_text,
                (CELL_SIZE * GRID_SIZE / 2 - (chronometer_text.get_width()/2)
                 , TOP_SIZE / 2 - (chronometer_text.get_height() / 2))
                )

def bomb_generation(x, y):
    bombs_pos = []
    while len(bombs_pos) < BOMB_AMOUNT:
        
        pass

print(bomb_list)

def render():
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

        y += 1

        animation_frame = (animation_frame + 0.0003) % 4

playing = True
first = True
clock.tick(30)
while playing:  # Main loop
    render_hud()
    render()

    # Display difficulties
    if difficulty_select_list.open :
        difficulty_select_list.display_difficulties()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if event.type == pygame.MOUSEBUTTONUP:
            (x, y) = pygame.mouse.get_pos()
            difficulty_select_list.mouse_clic((x, y))
            y -= TOP_SIZE

            if y < 0:
                break

            cell_value = grid[int(y / CELL_SIZE)][int(x / CELL_SIZE)]

            if event.button == 1:
                if cell_value == -1:
                    # if first:
                        # bomb_generation(x, y)
                    grid[int(y / CELL_SIZE)][int(x / CELL_SIZE)] = 1
            elif event.button == 3:
                if cell_value == -1:
                    grid[int(y / CELL_SIZE)][int(x / CELL_SIZE)] = 2
                else:
                    grid[int(y / CELL_SIZE)][int(x / CELL_SIZE)] = -1

    pygame.display.flip()

pygame.quit()
