import random

def print_board(board):
    display = [
        board[i] if board[i] != " " else str(i)
        for i in range(9)
    ]
    print()
    print(f" {display[0]} | {display[1]} | {display[2]} ")
    print("---+---+---")
    print(f" {display[3]} | {display[4]} | {display[5]} ")
    print("---+---+---")
    print(f" {display[6]} | {display[7]} | {display[8]} ")
    print()

def check_winner(board, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8], #rows
        [0,3,6], [1,4,7], [2,5,8], #cols
        [0,4,8], [2,4,6]           #diagonals
    ]

    return any(all(board[i] == player for i in combo) for combo in win_combos)

def computer_move(board):
    available_moves = [i for i in range(9) if board[i] == " "]
    return random.choice(available_moves)

def tic_tac_toe():
    board = [" " for _ in range(9)]

    print("Tic Tac Toe")
    print("1 - Play against another human")
    print("2 - Play against the computer")

    mode = input("Choose game mode (1 or 2): ")

    if mode == "1":
        players = ["X", "O"]
        print("Player 1 is X, Player 2 is O")
    elif mode == "2":
        players = ["X", "O"]
        print("You are X. Computer is O")
    else:
        print("Invalid choice.")
        return

    turn = 0
    while turn < 9:
        current_player = players[turn % 2]
        print_board(board)

        if mode == "2" and current_player == "O":
            move = computer_move(board)
            print(f"Computer chooses {move}")
        else:
            try:
                move = int(input(f"Player {current_player}, choose position (0-8): "))
                if board[move] != " ":
                    print("That spot is taken. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Enter a number 0-8.")
                continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            if mode == "2" and current_player == "O":
                print("Computer wins!")
            elif mode == "2":
                print("You win!")
            else:
                print(f"Player {current_player} wins!")
            return

        turn += 1

    print_board(board)
    print("It's a tie!")

tic_tac_toe() 