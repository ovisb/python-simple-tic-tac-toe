import pytest

from simple_tic_tac_toe.simple_tic_tac_toe import (
    create_grid,
    get_player_diff,
    is_cell_empty,
    is_col_winner,
    is_diag_winner,
    is_row_winner,
)


@pytest.mark.parametrize(
    "test_inp_, expected",
    [
        (("XXXOO__O_", "X"), True),
        (("___XXX___", "X"), True),
        (("___OO_XXX", "X"), True),
        (("OOOXX__O_", "O"), True),
        (("___OOO___", "O"), True),
        (("___XX_OOO", "O"), True),
        (("XXXOO__O_", "O"), False),
        (("___XXX___", "O"), False),
        (("___OO_XXX", "O"), False),
        (("OOOXX__O_", "X"), False),
        (("___OOO___", "X"), False),
        (("___XX_OOO", "X"), False),
    ],
)
def test_row_winner(test_inp_, expected):
    text, player = test_inp_
    grid = create_grid(text)
    assert is_row_winner(grid, player) == expected


@pytest.mark.parametrize(
    "test_inp_, expected",
    [
        (("X__XOXXO_", "X"), True),
        (("_X_OXO_X_", "X"), True),
        (("__X_OXO_X", "X"), True),
        (("O__OXOOX_", "O"), True),
        (("_O_XOX_O_", "O"), True),
        (("__O_XO_XO", "O"), True),
        (("X__XOXXO_", "O"), False),
        (("_X_OXO_X_", "O"), False),
        (("__X_OXO_X", "O"), False),
        (("O__OXOOX_", "X"), False),
        (("_O_XOX_O_", "X"), False),
        (("__O_XO_XO", "X"), False),
    ],
)
def test_col_winner(test_inp_, expected):
    text, player = test_inp_
    grid = create_grid(text)
    assert is_col_winner(grid, player) == expected


@pytest.mark.parametrize(
    "test_inp_, expected",
    [
        (("X__OX_OOX", "X"), True),
        (("O__XO_X_O", "O"), True),
        (("X__OX_OO_", "X"), False),
        (("__XOX_XOX", "X"), True),
        (("__O_OOOX_", "O"), True),
        (("__XOX_OO_", "X"), False),
    ],
)
def test_diag_winner(test_inp_, expected):
    text, player = test_inp_
    grid = create_grid(text)
    assert is_diag_winner(grid, player) == expected


@pytest.mark.parametrize(
    "test_inp_, expected",
    [
        ("X__OXOOOX", True),
        ("OXXXO_XOO", True),
        ("XXXOXOXO_", True),
        ("XXXOXOXOX", False),
    ],
)
def test_cell_empty(test_inp_, expected):
    grid = create_grid(test_inp_)
    assert is_cell_empty(grid) == expected


@pytest.mark.parametrize(
    "test_inp_, expected",
    [("_O_X__X_X", 2), ("_OOOO_X_X", 2)],
)
def test_get_player_diff(test_inp_, expected):
    grid = create_grid(test_inp_)
    assert get_player_diff(grid) == expected
