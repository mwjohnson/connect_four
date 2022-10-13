#!/usr/bin/env python
# -*- coding: utf-8 -*-


def valid_user(user):
    if len(user) == 1:
        return True


def create_user(user_id):
    user = input(f'Player {user_id}, please choose an integer or letter to represent your player: ')
    while not valid_user(user):
        print('Your username must be 1 character long!')
        user = input(f'Player {user_id}, please choose an integer or letter to represent your player: ')
    return user


def valid_user_2(user1, user2):
    if user2 == user1:
        print('That username is already taken!')
        return False
    return True


def print_board(board, options):
    print('  '.join(options)+'\n'+'\n'.join(map('  '.join, board))+'\n')


def valid_spot(spot, board, board_width):
    return spot.isdigit() and 0 < int(spot) <= board_width and board[0][int(spot)-1] == '*'


def choose_spot(board, letter):
    s = input('Choose your spot: ')
    while not valid_spot(s, board, len(board[0])):
        s = input('Choose your spot: ')
    s = int(s)

    print('\n')
    x = len(board)-1
    while board[x][s - 1] != '*':
        x -= 1
    board[x][s - 1] = letter
    return True


def vert_win(board, letter):
    for x in range(6, -1, -1):
        for y in range(7):
            try:
                if board[x][y] == board[x - 1][y] == board[x - 2][y] == board[x - 3][y] == letter:
                    return True, f'{letter}, won vertically! Congratulations'
                else:
                    continue
            except IndexError:
                continue
    return False, None


def horiz_win(board, letter):
    for x in range(6, -1, -1):
        for y in range(7):
            try:
                if board[x][y] == board[x][y + 1] == board[x][y + 2] == board[x][y + 3] == letter:
                    return True, f'{letter}, won horizontally! Congratulations'
                else:
                    continue
            except IndexError:
                continue
    return False, None


def diag_win(board, letter):
    for x in range(6, -1, -1):
        for y in range(7):
            try:
                if board[x][y] == board[x - 1][y + 1] == board[x - 2][y + 2] == board[x - 3][y + 3] == letter or \
                        board[x][y] == board[x - 1][y - 1] == board[x - 2][y - 2] == board[x - 3][y - 3] == letter:
                    return True, f'{letter}, won diagonally! Congratulations'
            except IndexError:
                continue
    return False, None


def check_win(board, letter):
    result, message = vert_win(board, letter)
    if result:
        print(message)
        return True
    result, message = horiz_win(board, letter)
    if result:
        print(message)
        return True
    result, message = diag_win(board, letter)
    if result:
        print(message)
        return True


def main():
    board_width = 9
    board_height = 6
    options = [str(i) for i in range(1, board_width+1)]
    board = [['*' for _ in range(0, board_width)] for _ in range(0, board_height)]

    one = create_user(1)
    two = create_user(2)

    letter = None
    turns = 0

    while True:
        print_board(board, options)
        if check_win(board, letter):
            break

        if turns % 2 == 0:
            letter = one
        else:
            letter = two
        if choose_spot(board, letter):
            turns += 1


if __name__ == "__main__":
    main()
