board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")


def check_win(board, player):

    for row in board:
        if row == [player, player, player]:
            return True

    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def player_move(board, player):
    while True:
        row = int(input(f"{player} - Linha (0-2): "))
        col = int(input(f"{player} - Coluna (0-2): "))

        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Essa posição já está ocupada.")
        else:
            print("Posição inválida. Use 0, 1 ou 2.")


def play():
    current_player = 'X'

    while True:
        display_board(board)

        player_move(board, current_player)

        if check_win(board, current_player):
            display_board(board)
            print(f"{current_player} ganhou!")
            break

        if board_full(board):
            display_board(board)
            print("Empate!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


play()