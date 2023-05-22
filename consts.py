GRID_SIZE = 7
CELL_SIZE = 50
BOMB_AMOUNT = int((GRID_SIZE ** 2) / 8)

TOP_SIZE = 75
BLUE = (132, 196, 209)
GREEN = (50, 144, 143)
GRAY = (232, 246, 238)
RED = (200, 25, 25)
DARK_GRAY = (128, 128, 128)

DIFFICULTIES = {
    "easy": {"grid_size": 10, "cell_size": 50},
    "medium": {"grid_size": 15, "cell_size": 35},
    "hard": {"grid_size": 20, "cell_size": 30}
}
difficulty = "easy"

grid_size = 10
cell_size = 50
bomb_amount = int((GRID_SIZE ** 2) / 8)


def set_grid_size(val):
    print(val)
    global grid_size
    grid_size = val
    return grid_size

def set_cell_size(val):
    print(val)
    global cell_size
    cell_size = val
    return cell_size

def set_bomb_amount(val):
    global bomb_amount
    bomb_amount = val
    return bomb_amount

