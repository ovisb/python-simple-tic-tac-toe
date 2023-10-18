"""Main module"""
from simple_tic_tac_toe import (  # get_player_diff,; is_cell_empty,; is_col_winner,; is_diag_winner,; is_row_winner,
    create_grid,
    print_grid,
)


def main() -> None:
    """Main function"""
    # user_input = input()
    user_input = "X_X_O____"
    grid = create_grid(user_input)
    print_grid(grid)

    while True:
        try:
            coordinates = input("Enter coordinates: ").split()
            a = int(coordinates[0])
            b = int(coordinates[1])
        except ValueError:
            print("You should enter numbers!")
            continue
        except IndexError:
            print("You should enter two numbers delimited by a space!")
            continue

        if a < 1 or b < 1 or a > 3 or b > 3:
            print("Coordinates should be from 1 to 3!")
            continue

        if grid[a - 1][b - 1] != "_":
            print("This cell is occupied! Choose another one!")
            continue

        grid[a - 1][b - 1] = "X"
        print_grid(grid)
        break

    # if (
    #     is_row_winner(grid, "X")
    #     and is_row_winner(grid, "O")
    #     or is_col_winner(grid, "X")
    #     and is_col_winner(grid, "O")
    # ) or get_player_diff(grid) >= 2:
    #     print("Impossible")
    # elif (
    #     is_row_winner(grid, "X")
    #     or is_col_winner(grid, "X")
    #     or is_diag_winner(grid, "X")
    # ):
    #     print("X wins")
    # elif (
    #     is_row_winner(grid, "O")
    #     or is_col_winner(grid, "O")
    #     or is_diag_winner(grid, "O")
    # ):
    #     print("O wins")
    # elif is_cell_empty(grid):
    #     print("Game not finished")
    # else:
    #     print("Draw")


if __name__ == "__main__":
    main()
