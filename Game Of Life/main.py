from board import Board

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
    brd = Board(90, 90)
    render(brd.assign_random_state())
    print("Delimiter here!")
    render(brd.next_board_state())
    print("Delimiter here!")
    render(brd.next_board_state())