# Game state
board_spots = []
board = ""
board_width = 0
board_height = 0
player = "X"
score = {
    "X": 0,
    "O": 0
}

def board_clear():
    global board_spots, board, board_width, board_height, player
    board_spots = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    board = (
      "   |   |   \n"
      "---+---+---\n"
      "   |   |   \n"
      "---+---+---\n"
      "   |   |   "
    )
    board_width = 12
    board_height = 5
    player = "X"

def board_set(x, y, c):
    global board, board_width, board_height
    board_chars = list(board)
    board_chars[(y * board_width) + x] = c
    board = "".join(board_chars)

def board_show():
    global board, score
    print("[Score X: %d vs O: %d]" % (score["X"], score["O"]))
    print(board)

def board_draw_spots():
    for row in range(3):
        for col in range(3):
            player = board_spots[row][col]
            c = " "
            if player == "X":
                c = "X"
            elif player == "O":
                c = "O"
            board_set(col * 4 + 1 , row * 2, c)

def board_set_spot(spot, player):
    global board_spots
    row = int(spot / 3)
    col = spot % 3
    if board_spots[row][col] == " ":
        board_spots[row][col] = player
        return True
    return False

def board_get_winner():
    global board_spots
    # Check horizontal
    for row in range(3):
        # Check center, left, and right
        if (board_spots[row][1] != " " and
                board_spots[row][1] == board_spots[row][0] and
                board_spots[row][1] == board_spots[row][2]):
            return (board_spots[row][1], "h", row)
    # Check vertical
    for col in range(3):
        # Check center, up, and down
        if (board_spots[1][col] != " " and
                board_spots[1][col] == board_spots[0][col] and
                board_spots[1][col] == board_spots[2][col]):
            return (board_spots[1][col], "v", col)
    # Diagonal left
    if (board_spots[1][1] != " " and
            board_spots[1][1] == board_spots[0][0] and
            board_spots[1][1] == board_spots[2][2]):
        return (board_spots[1][1], "d", "left")
    # Diagonal right
    if (board_spots[1][1] != " " and
            board_spots[1][1] == board_spots[0][2] and
            board_spots[1][1] == board_spots[2][0]):
        return (board_spots[1][1], "d", "right")
    return (None, None, None)

def board_is_full():
    for row in range(3):
        for col in range(3):
            if board_spots[row][col] == " ":
                return False
    return True


if __name__ == '__main__':
    # Setup and game loop
    board_clear()
    done = False
    while not done:
        board_draw_spots()
        board_show()
        print("It's %s's turn.  Enter 1-9 or q to quit then <enter>." % (player))
        option = input("> ")
        if option == "q":
            done = True
        else:
            if board_set_spot(int(option) - 1, player):
                game_over = False
                winner, win_type, win_spot = board_get_winner()
                if winner != None:
                    print("%s won!" % (winner))
                    score[winner] += 1
                    if win_type == "h":
                        print("Horizontal on row %d" % (win_spot + 1))
                    elif win_type == "v":
                        print("Vertical on col %d" % (win_spot + 1))
                    else:
                        print("Diagonal to the %s" % (win_spot))
                    game_over = True
                elif board_is_full():
                    print("No winner.")
                    game_over = True
                else:
                    if player == "X":
                        player = "O"
                    else:
                        player = "X"
                if game_over:
                    board_draw_spots()
                    board_show()
                    play_again = input("Play again (y or n then <enter>)? ")
                    if play_again == "y":
                        game_over = False
                        board_clear()
                    else:
                        done = True
            else:
                print("That spot is taken!  Try again.")
