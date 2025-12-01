from board import Board
import time
import os

# Simple rendering function
def render(board_param) -> None:
    to_render = board_param
    for row in to_render:
        row_str = ''
        for elem in range(len(row)):
            if row[elem] == 0:
                row_str += '□'
            else:
                row_str += '■'
        print(row_str)

if __name__ == "__main__":
    brd = Board(50, 40)
    # Initialize the board by assigning a random state
    os.system('cls' if os.name == 'nt' else 'clear')
    brd.assign_random_state()
    render(brd.current_state)
    while True:
        time.sleep(0.6)
        os.system('cls' if os.name == 'nt' else 'clear')
        brd.next_board_state()
        print("Current generations passed:",brd.generation)
        render(brd.current_state)

