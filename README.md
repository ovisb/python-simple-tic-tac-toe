# EDU project

## Project

This is _Simple Tic Tac Toe_ project that is part of Hyperskill platform from Jetbrains Academy.

'Python Core' track

## Technologies and tools used

- Python 3.11
- pytest
- mypy
- isort
- black
- flake8
- make

## Project description

Simple Tic Tac Toe game which can be played by two players via coordinates inputs in the format of:

(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)

These represent the location of X or O on the grid, first tuple item being the row while the second is the place on the column.

Both players take turns and game ends once one of players wins or there is a draw(no winners and no empty cells left in the grid). 

## Changelog

17.10.2023

- Added method for creating 3x3 Grid based on string input of X's and/or O's and/or empty cells
- Added method for printing the current game status

Added the following game states:

- Game not finished when neither side has three in a row but the grid still has empty cells.
- Draw when no side has a three in a row and the grid has no empty cells.
- X wins when the grid has three X’s in a row (including diagonals).
- O wins when the grid has three O’s in a row (including diagonals).
0 Impossible when the grid has three X’s in a row as well as three O’s in a row, or there are a lot more X's than O's or vice versa (the difference should be 1 or 0; if the difference is 2 or more, then the game state is impossible).

18.10.2023

- Added validations where user will be re prompted if any of the bellow happen
    - inputs are not valid numbers
    - inputs are out of array bounds
    - inputs were already set in the grid
    - Update Grid with user input, for now updating only 'X'
    - Added main game loop, where user can input either X or O
    - Game ends if there is a winner or it's a draw.
  
- Added unit tests for all functions

#### Project status
Completed 5/5 stages

#### Install steps

Install everything (main + dev packages except optional groups)

```sh
peotry install
```

Install main packages only

```sh
peotry install --only main

```

If you need pre-commit

```sh
poetry install --with commit
```

If you decided to install pre-commit you can install .pre-commit files in your repo

```sh
peotry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
```

If the files are git staged, you can trigger pre-commit manually

```sh
poetry run pre-commit run --all-files
poetry run pre-commit run --hook-stage push -v
```

#### Makefile

Added 'Makefile' to make it easy to validate files
Check bellow command on usage

```sh
make help
```
