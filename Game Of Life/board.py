import random

class Board:
    def __init__(self, board_height, board_width):
        self.board_height = board_height
        self.board_width = board_width
        self.current_state = None
        self.generation = 0

    def create_dead_state(self) -> list[list[int | bool]]:
        empty_board = []
        for _ in range(self.board_height):
            empty_board.append([])
        for lst in empty_board:
            while len(lst) < self.board_width:
                lst.append(0)
        
        return empty_board
    
    # Randomly assign states to each of the cell
    def assign_random_state(self) -> list[list[int | bool]]:
        self.current_state = self.create_dead_state()

        for row in self.current_state:
            for elem in range(len(row)):
                row[elem] = random.getrandbits(1)
        
        return self.current_state

    def next_board_state(self):
        new_state = self.create_dead_state()

        # The following matrix is used to get the coordinates of the neighbors
        neighbors_coords = ((-1, -1), (0, -1), (1, -1),
                            (-1, 0),            (1, 0),
                            (-1, 1),   (0, 1),  (1, 1))
        
        for i in range(self.board_width):
            for j in range(self.board_height):
                # curr_cell = self.current_state[i][j]
                live_neighbor_count = 0
                for di,dj in neighbors_coords:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < self.board_width and 0 <= nj < self.board_height:
                        if self.current_state[ni][nj] == 1:
                            live_neighbor_count += 1
                if live_neighbor_count <= 1 or live_neighbor_count > 3:
                    new_state[i][j] = 0
                else:
                    if live_neighbor_count == 3:
                        new_state[i][j] = 1
                    elif live_neighbor_count == 2:
                        if self.current_state[i][j] == 0:
                            new_state[i][j] = 0
                        else:
                            new_state[i][j] = 1
        
        print(self.current_state)

        self.current_state = new_state
        self.generation += 1
        return self.current_state

