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
