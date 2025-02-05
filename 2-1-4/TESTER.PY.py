def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player_index = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player = players[current_player_index]
        print(f"{player}'s turn. Enter your move as row and column (e.g., 1 1 for the center):")

        try:
            row, col = map(int, input().split())
            if board[row][col] != " ":
                print("Cell is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column numbers between 0 and 2.")
            continue

        board[row][col] = player
        print_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        current_player_index = 1 - current_player_index  # Switch player

if __name__ == "__main__":
    main()
