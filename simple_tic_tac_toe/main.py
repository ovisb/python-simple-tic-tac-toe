"""Main module"""
from simple_tic_tac_toe import generate_matrix, print_matrix  # type: ignore


def main() -> None:
    """Main function"""

    text = input()

    matrix = generate_matrix(text)
    # print(matrix)
    print_matrix(matrix)


if __name__ == "__main__":
    main()
