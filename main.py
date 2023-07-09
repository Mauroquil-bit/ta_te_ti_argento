def print_grid(grid):
    print("---------")
    print("|", grid[0][0], grid[0][1], grid[0][2], "|")
    print("|", grid[1][0], grid[1][1], grid[1][2], "|")
    print("|", grid[2][0], grid[2][1], grid[2][2], "|")
    print("---------")

def check_win(grid):
    # check rows
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != " ":
            return grid[i][0]
    # check columns
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != " ":
            return grid[0][i]
    # check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != " ":
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != " ":
        return grid[0][2]
    return False

def check_draw(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                return False
    return True

def check_impossible(grid):
    x_count = 0
    o_count = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] == "X":
                x_count += 1
            elif grid[i][j] == "O":
                o_count += 1
    if abs(x_count - o_count) >= 2:
        return True
    return False

def check_state(grid):
    if check_impossible(grid):
        return "Impossible"
    if check_win(grid) == "X":
        return "X wins"
    if check_win(grid) == "O":
        return "O wins"
    if check_draw(grid):
        return "Draw"
    return "Game not finished"

def check_coordinates(grid, x, y):
    if not x.isdigit() or not y.isdigit():
        print("You should enter numbers!")
        return False
    x = int(x)
    y = int(y)
    if x < 1 or x > 3 or y < 1 or y > 3:
        print("Coordinates should be from 1 to 3!")
        return False
    if grid[x - 1][y - 1] != " ":
        print("This cell is occupied! Choose another one!")
        return False
    return True

def play_game():
    grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print_grid(grid)
    while True:
        x, y = input("Enter the coordinates: ").split()
        if check_coordinates(grid, x, y):
            x = int(x)
            y = int(y)
            grid[x - 1][y - 1] = "X"
            print_grid(grid)
            if check_state(grid) != "Game not finished":
                print(check_state(grid))
                break
            while True:
                x, y = input("Enter the coordinates: ").split()
                if check_coordinates(grid, x, y):
                    x = int(x)
                    y = int(y)
                    grid[x - 1][y - 1] = "O"
                    print_grid(grid)
                    if check_state(grid) != "Game not finished":
                        print(check_state(grid))
                        break
                    break

play_game()
