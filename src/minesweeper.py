# Introduction to Programming
# Project
# Minesweeper
# Student ID and name: s2058280 Nicholas Brodbeck

import random


difficulties = {
    "easy": [5, 5],
    "medium": [8, 13],
    "hard": [10, 20]
}


def blank_map(size, char):
    game_map = []
    for column in range(size):
        row = []
        for i in range(size):
            row.append(char)
        game_map.append(row)
    return game_map


def fill_map(game_map, bombs=3):
    size = len(game_map)
    for bomb in range(bombs):
        while True:
            row = random.randint(0, size-1)
            column = random.randint(0, size-1)
            if game_map[row][column] != "X":
                game_map[row][column] = "X"
                break
        # Fill numbers around bomb:
        if row >= 1:
            if game_map[row - 1][column] != "X":
                game_map[row - 1][column] += 1
            if column >= 1:
                if game_map[row - 1][column - 1] != "X":
                    game_map[row - 1][column - 1] += 1
            if column <= size-2:
                if game_map[row - 1][column + 1] != "X":
                    game_map[row - 1][column + 1] += 1
        if row <= size-2:
            if game_map[row + 1][column] != "X":
                game_map[row + 1][column] += 1
            if column >= 1:
                if game_map[row + 1][column - 1] != "X":
                    game_map[row + 1][column - 1] += 1
            if column <= size-2:
                if game_map[row + 1][column + 1] != "X":
                    game_map[row + 1][column + 1] += 1
        if column >= 1:
            if game_map[row][column - 1] != "X":
                game_map[row][column - 1] += 1
        if column <= size-2:
            if game_map[row][column + 1] != "X":
                game_map[row][column + 1] += 1


def display_map(map):
    for row in map:
        s = ""
        for column in row:
            s += "{}\t".format(column)
        print(s)


def open_spot_surroundings(column, row, game_map, player_map):
    size = len(game_map)
    if column >= 1:
        if game_map[row][column - 1] == 0 and player_map[row][column - 1] != 0:
            player_map[row][column - 1] = 0
            open_spot_surroundings(column - 1, row, game_map, player_map)
        else:
            player_map[row][column - 1] = game_map[row][column - 1]
    if column <= size-2:
        if game_map[row][column + 1] == 0 and player_map[row][column + 1] != 0:
            player_map[row][column + 1] = 0
            open_spot_surroundings(column + 1, row, game_map, player_map)
        else:
            player_map[row][column + 1] = game_map[row][column + 1]
    if row >= 1:
        if game_map[row-1][column] == 0 and player_map[row-1][column] != 0:
            player_map[row-1][column] = 0
            open_spot_surroundings(column, row - 1, game_map, player_map)
        else:
            player_map[row-1][column] = game_map[row-1][column]
    if row <= size-2:
        if game_map[row + 1][column] == 0 and player_map[row + 1][column] != 0:
            player_map[row + 1][column] = 0
            open_spot_surroundings(column, row + 1, game_map, player_map)
        else:
            player_map[row + 1][column] = game_map[row + 1][column]


def open_spot(column, row, game_map, player_map):
    val = game_map[row][column]
    player_map[row][column] = val
    if val == 0:
        open_spot_surroundings(column, row, game_map, player_map)
    lost = val == "X" and True or False
    return lost, check_win(game_map, player_map)


def check_win(game_map, player_map):
    y = 0
    for row in player_map:
        x = 0
        for column in row:
            if column == "-" and game_map[y][x] != "X":
                return False
            x += 1
        y += 1
    return True


def input_int(prompt):
    while True:
        choice = input(prompt)
        try:
            choice = int(choice)
            return choice
        except ValueError:
            print("Input must be a valid integer!")


def input_range(prompt, minimum, maximum):
    while True:
        choice = input_int(prompt)
        if minimum <= choice <= maximum:
            return choice
        else:
            print("Input must be between {} and {}!".format(minimum, maximum))


def game(size, bombs):
    game_map = blank_map(size, 0)
    fill_map(game_map, bombs)
    player_map = blank_map(size, "-")
    print("There are {} mines!".format(bombs))
    while True:
        print("Input an integer representing the column and row, or 0 to quit.")
        display_map(player_map)
        column = input_range("Column: ", 0, size)
        if column == 0:
            print("Exiting!")
            return False
        row = input_range("Row: ", 0, size)
        if row == 0:
            print("Exiting!")
            return False
        print("({}, {})".format(column, row))
        lost, won = open_spot(column-1, row-1, game_map, player_map)
        if lost:
            display_map(game_map)
            print("You lost!")
            break
        elif won:
            display_map(game_map)
            print("You won!")
            break


def main():
    print("Minesweeper!")
    print("Note: When opening cells, counting starts from top left corner as (1, 1)")
    while True:
        choice = input("Choose a difficulty, (e)asy, (m)edium or (h)ard: ").lower()
        if choice == "easy" or choice == "e":
            size = difficulties["easy"][0]
            bombs = difficulties["easy"][1]
            game(size, bombs)
        elif choice == "medium" or choice == "m":
            size = difficulties["medium"][0]
            bombs = difficulties["medium"][1]
            game(size, bombs)
        elif choice == "hard" or choice == "h":
            size = difficulties["hard"][0]
            bombs = difficulties["hard"][1]
            game(size, bombs)
        else:
            print("Invalid choice!")
            continue
        choice2 = input("Play again? y/n: ").lower()
        if not (choice2 == "y" or choice2 == "yes"):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
