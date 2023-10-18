# write your code here
from simple_tic_tac_toe import create_grid, is_game_finished, print_grid


def main() -> None:
    """Main function"""
    blank_grid = "_________"
    players = ("X", "O")
    i = 0

    grid = create_grid(blank_grid)
    print_grid(grid)

    while True:
        coordinates = input("Enter coordinates: ").split()
        try:
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

        grid[a - 1][b - 1] = players[i % len(players)]
        print_grid(grid)
        if is_game_finished(grid):
            break
        i += 1


if __name__ == "__main__":
    main()
