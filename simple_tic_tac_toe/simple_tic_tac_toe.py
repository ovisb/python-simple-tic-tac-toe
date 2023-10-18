MAX_GRID = 3


def create_grid(user_input: str) -> list[list[str]]:
    """
    Create 3x3 Game Grid
    @param user_input: string containing X's / O's and/or empty lines
    @return: 3X3 Game Grid
    """
    grid = []

    for i in range(0, len(user_input), MAX_GRID):
        row = [user_input[j] for j in range(i, MAX_GRID + i)]
        grid.append(row)

    return grid


def is_row_winner(grid: list[list[str]], player: str) -> bool:
    """
    Check if X or O has won in any of the rows
    @param grid: 2d 3x3 list
    @param player: X or O
    @return: true if player has won else false
    """
    for row in grid:
        if row.count(player) == MAX_GRID:
            return True

    return False


def is_col_winner(grid: list[list[str]], player: str) -> bool:
    """
    Check if X or O has won in any of the columns
    @param grid: 2d 3x3 list
    @param player: X or O
    @return: true if player has won else false
    """
    for i in range(len(grid)):
        count = 0
        for j in range(len(grid[i])):
            if grid[j][i] == player:
                count += 1
        if count == MAX_GRID:
            return True

    return False


def is_diag_winner(grid: list[list[str]], player: str) -> bool:
    """
    Check if X or O has won in any of the diagonals
    @param grid: 2d 3x3 list
    @param player: X or O
    @return: true if player won diag else false
    """
    count = 0
    # check diag
    for i in range(MAX_GRID):
        if grid[i][i] == player:
            count += 1

    if count == 3:
        return True

    # check reverse diag
    count = 0
    for i in range(MAX_GRID):
        if grid[i][MAX_GRID - 1 - i] == player:
            count += 1

    return count == 3


def is_cell_empty(grid: list[list[str]]) -> bool:
    """
    Check if cell is empty
    @param grid: 2d 3x3 list
    @return: true if cell is empty else false
    """
    for row in grid:
        for col in row:
            if col == "_":
                return True

    return False


def get_player_diff(grid: list[list[str]]) -> int:
    """
    Get difference between X or O / O or X
    @param grid: 2d 3x3 list
    @return: difference
    """
    player_x = 0
    player_o = 0

    for row in grid:
        for col in row:
            if col == "X":
                player_x += 1
            elif col == "O":
                player_o += 1

    return player_x - player_o if player_x > player_o else player_o - player_x


def print_grid(grid: list[list[str]]) -> None:
    """
    Print Game state / grid
    @param grid: 3x3 grid
    """
    print("-" * len(grid) * MAX_GRID)
    for row in grid:
        print("|", end=" ")
        for col in row:
            print(f"{col}", end=" ")
        print("|", end=" ")
        print()
    print("-" * len(grid) * MAX_GRID)
