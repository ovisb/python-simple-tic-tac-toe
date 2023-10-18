"""Main module"""
from simple_tic_tac_toe import (
    create_grid,
    get_player_diff,
    is_cell_empty,
    is_col_winner,
    is_diag_winner,
    is_row_winner,
    print_grid,
)


def main() -> None:
    """Main function"""
    user_input = input()

    grid = create_grid(user_input)
    print_grid(grid)

    if (
        is_row_winner(grid, "X")
        and is_row_winner(grid, "O")
        or is_col_winner(grid, "X")
        and is_col_winner(grid, "O")
    ) or get_player_diff(grid) >= 2:
        print("Impossible")
    elif (
        is_row_winner(grid, "X")
        or is_col_winner(grid, "X")
        or is_diag_winner(grid, "X")
    ):
        print("X wins")
    elif (
        is_row_winner(grid, "O")
        or is_col_winner(grid, "O")
        or is_diag_winner(grid, "O")
    ):
        print("O wins")
    elif is_cell_empty(grid):
        print("Game not finished")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
