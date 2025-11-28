import random

# Populate with 0's. For now the function works, but need to write one better
def dead_state(db_width, db_height) -> list[list[int]]:
    board = []
    for _ in range(db_height):
        board.append([])
    for item in board:
        while len(item) < db_width:
            item.append(0)
    
    return board


# Randomly assign states to each of the cell
def random_state(b_width, b_height) -> list[list[int | bool]]:
    state = dead_state(db_width=b_width, db_height=b_height)

    for row in state:
        for elem in range(len(row)):
            row[elem] = random.getrandbits(1)
    
    return state

# Render the plain bit-list
def render(b_state) -> None:
    to_render = b_state
    for row in to_render:
        row_str = ''
        for elem in range(len(row)):
            if row[elem] == 0:
                row_str += '□'
            else:
                row_str += '■'
        print(row_str)


a_random_state = random_state(100, 40)
render(a_random_state)
# print(random_state(7, 5))


# ■
# □
