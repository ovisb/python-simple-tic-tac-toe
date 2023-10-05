"""Hello module"""

def generate_matrix(text: str) -> list[list[str]]:
    """
    Generate 3x3 Matrix
    :param text: text containing X, 0 or _
    :return: matrix list
    """
    matrix = []
    max_col = 3
    for i in range(0, len(text), max_col):
        row = [ text[j] for j in range(i, max_col + i) ]
        matrix.append(row)

    return matrix

def print_matrix(matrix: list[list[str]]) -> None:
    """
    Print Matrix
    :param matrix:
    :return: None
    """
    print("---------")
    for i, row in enumerate(matrix):
        print("|", end=" ")
        for j, col in enumerate(row):
            item = row[j]
            print(item, end=" ")
        print("|", end=" ")
        print()
    print("---------")

