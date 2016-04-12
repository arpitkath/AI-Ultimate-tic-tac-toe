from random import randint


def score(game_state):
    if game_state == "O":
        return 10
    elif game_state == "X":
        return -10
    else:
        return 0


def get_game_status(board):
        draw_count = 0

        # Checking if game is horizontally or vertically complete?
        for i in range(3):
            x_count_hor = x_count_ver = o_count_hor = o_count_ver = 0
            for j in range(3):
                if board[i][j] == "X":
                    x_count_hor += 1
                elif board[i][j] == "O":
                    o_count_hor += 1
                if board[j][i] == "X":
                    x_count_ver += 1
                elif board[j][i] == "O":
                    o_count_ver += 1
                if board[i][j] == "":
                    draw_count += 1
            if x_count_ver == 3 or x_count_hor == 3:
                return "X"
            elif o_count_ver == 3 or o_count_hor == 3:
                return "O"

        # Checking if game is diagonally complete.
        x_d1_count = x_d2_count = o_d1_count = o_d2_count = 0
        for i in range(3):
            if board[i][i] == "X":
                x_d1_count += 1
            elif board[i][i] == "O":
                o_d1_count += 1
            if board[i][3 - i - 1] == "X":
                x_d2_count += 1
            elif board[i][3 - i - 1] == "O":
                o_d2_count += 1
        if x_d1_count == 3 or x_d2_count == 3:
            return "X"
        if o_d1_count == 3 or o_d2_count == 3:
            return "O"

        # Check if the game is a "draw".
        if draw_count == 0:
            return "draw"

        # Else continue the game, i.e. no one has won yet.
        return "continue"


def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                moves.append((i, j))
    return moves


def alpha_beta(board, game_state, alpha, beta, game_turn):
    if game_state != "continue":
        return score(game_state)

    scores = []
    moves = get_available_moves(board)

    # To get available moves.

    for move in moves:
        board[move[0]][move[1]] = game_turn
        if game_turn == "X":
            new_turn = "O"
        else:
            new_turn = "X"
        val = alpha_beta(board, get_game_status(board), alpha, beta, new_turn)
        board[move[0]][move[1]] = ""
        if game_turn == "O":
            if val > alpha:
                alpha = val
            if alpha >= beta:
                return beta
        if game_turn == "X":
            if val < beta:
                beta = val
            if beta <= alpha:
                return alpha
    if game_turn == "O":
        return alpha
    else:
        return beta


def determine_move(board, game_turn):
    a = -2
    choices = [(0, 0), (0, 2), (2, 0), (2, 2)]
    moves = get_available_moves(board)
    if len(moves) == 9:
        return choices[randint(0, len(choices)-1)]
    elif len(moves) == 0:
        return -1, -1
    choices = []
    for move in moves:
        board[move[0]][move[1]] = game_turn
        if game_turn == "X":
            new_turn = "O"
        else:
            new_turn = "X"
        val = alpha_beta(board, get_game_status(board), -2, 2, new_turn)
        board[move[0]][move[1]] = ""
        if val > a:
            a = val
            choices = [move]
        elif val == a:
            choices.append(move)
    return choices[randint(0, len(choices)-1)]