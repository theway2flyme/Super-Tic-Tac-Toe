import random
from detect_computer_marker_fn import detect_computer_marker
from detect_player_marker_fn import detect_player_marker

#rows that list board is made of.
row_1 = {'ulhc': '|BB|', 'A-4': 'A-4_', 'A-3': 'A-3_', 'A-2': 'A-2_', 'A-1': 'A-1_', 'X10': 'X10_', 'A1': 'A1__', 'A2': 'A2__', 'A3': 'A3__', 'A4': 'A4__', 'urhc': '|BB|'}
row_2 = {'B4': 'B4__', 'B4_A-4': '|CC|', 'B4_A-3': '|CC|', 'B4_A-2': '|CC|', 'B4_A-1': '|CC|', 'B4_X10': '|CC|', 'B4_A1': '|CC|', 'B4_A2': '|CC|', 'B4_A3': '|CC|', 'B4_A4': '|CC|', 'D4': 'D4__'}
row_3 = {'B3': 'B3__', 'B3_A-4': '|CC|', 'B3_A-3': '|CC|', 'B3_A-2': '|CC|', 'B3_A-1': '|CC|', 'B3_X10': '|CC|', 'B3_A1': '|CC|', 'B3_A2': '|CC|', 'B3_A3': '|CC|', 'B3_A4': '|CC|', 'D3': 'D3__'}
row_4 = {'B2': 'B2__', 'B2_A-4': '|CC|', 'B2_A-3': '|CC|', 'B2_A-2': '|CC|', 'B2_A-1': '|CC|', 'B2_X10': '|CC|', 'B2_A1': '|CC|', 'B2_A2': '|CC|', 'B2_A3': '|CC|', 'B2_A4': '|CC|', 'D2': 'D2__'}
row_5 = {'B1': 'B1__', 'B1_A-4': '|CC|', 'B1_A-3': '|CC|', 'B1_A-2': '|CC|', 'B1_A-1': '|CC|', 'B1_X10': '|CC|', 'B1_A1': '|CC|', 'B1_A2': '|CC|', 'B1_A3': '|CC|', 'B1_A4': '|CC|', 'D1': 'D1__'}
row_6 = {'Y-10': 'Y-10', 'Y-10_A-4': '|CC|', 'Y-10_A-3': '|CC|', 'Y-10_A-2': '|CC|', 'Y-10_A-1': '|CC|', 'Y-10_X10': '|CC|', 'Y-10_A1': '|CC|', 'Y-10_A2': '|CC|', 'Y-10_A3': '|CC|', 'Y-10_A4': '|CC|', 'Y10': 'Y10_'}
row_7 = {'B-1': 'B-1_', 'B-1_A-4': '|CC|', 'B-1_A-3': '|CC|', 'B-1_A-2': '|CC|', 'B-1_A-1': '|CC|', 'B-1_X10': '|CC|', 'B-1_A1': '|CC|', 'B-1_A2': '|CC|', 'B-1_A3': '|CC|', 'B-1_A4': '|CC|', 'D-1': 'D-1_'}
row_8 = {'B-2': 'B-2_', 'B-2_A-4': '|CC|', 'B-2_A-3': '|CC|', 'B-2_A-2': '|CC|', 'B-2_A-1': '|CC|', 'B-2_X10': '|CC|', 'B-2_A1': '|CC|', 'B-2_A2': '|CC|', 'B-2_A3': '|CC|', 'B-2_A4': '|CC|', 'D-2': 'D-2_'}
row_9 = {'B-3': 'B-3_', 'B-3_A-4': '|CC|', 'B-3_A-3': '|CC|', 'B-3_A-2': '|CC|', 'B-3_A-1': '|CC|', 'B-3_X10': '|CC|', 'B-3_A1': '|CC|', 'B-3_A2': '|CC|', 'B-3_A3': '|CC|', 'B-3_A4': '|CC|', 'D-3': 'D-3_'}
row_10 = {'B-4': 'B-4_', 'B-4_A-4': '|CC|', 'B-4_A-3': '|CC|', 'B-4_A-2': '|CC|', 'B-4_A-1': '|CC|', 'B-4_X10': '|CC|', 'B-4_A1': '|CC|', 'B-4_A2': '|CC|', 'B-4_A3': '|CC|', 'B-4_A4': '|CC|', 'D-4': 'D-4_'}
row_11 = {'llhc': '|BB|', 'C-4': 'C-4_', 'C-3': 'C-3_', 'C-2': 'C-2_', 'C-1': 'C-1_', 'X-10': 'X-10', 'C1': 'C1__', 'C2': 'C2__', 'C3': 'C3__', 'C4': 'C4__', 'lrhc': '|BB|'}

coordinate_row_1 = {'ulhc': 'ulhc', 'A-4': 'A-4_', 'A-3': 'A-3_', 'A-2': 'A-2_', 'A-1': 'A-1_', 'X10': 'X10_', 'A1': 'A1__', 'A2': 'A2__', 'A3': 'A3__', 'A4': 'A4__', 'urhc': '|BB|'}
coordinate_row_2 = {'B4': 'B4__', 'B4_A-4': 'B4_A-4', 'B4_A-3': 'B4_A-3', 'B4_A-2': 'B4_A-2', 'B4_A-1': 'B4_A-1', 'B4_X10': 'B4_X10', 'B4_A1': 'B4_A1', 'B4_A2': 'B4_A2', 'B4_A3': 'B4_A3', 'B4_A4': 'B4_A4', 'D4': 'D4__'}
coordinate_row_3 = {'B3': 'B3__', 'B3_A-4': 'B3_A-4', 'B3_A-3': 'B3_A-3', 'B3_A-2': 'B3_A-2', 'B3_A-1': 'B3_A-1', 'B3_X10': 'B3_X10', 'B3_A1': 'B3_A1', 'B3_A2': 'B3_A2', 'B3_A3': 'B3_A3', 'B3_A4': 'B3_A4', 'D3': 'D3__'}
coordinate_row_4 = {'B2': 'B2__', 'B2_A-4': 'B2_A-4', 'B2_A-3': 'B2_A-3', 'B2_A-2': 'B2_A-2', 'B2_A-1': 'B2_A-1', 'B2_X10': 'B2_X10', 'B2_A1': 'B2_A1', 'B2_A2': 'B2_A2', 'B2_A3': 'B2_A3', 'B2_A4': 'B2_A4', 'D2': 'D2__'}
coordinate_row_5 = {'B1': 'B1__', 'B1_A-4': 'B1_A-4', 'B1_A-3': 'B1_A-3', 'B1_A-2': 'B1_A-2', 'B1_A-1': 'B1_A-1', 'B1_X10': 'B1_X10', 'B1_A1': 'B1_A1', 'B1_A2': 'B1_A2', 'B1_A3': 'B1_A3', 'B1_A4': 'B1_A4', 'D1': 'D1__'}
coordinate_row_6 = {'Y-10': 'Y-10', 'Y-10_A-4': 'Y-10_A-4', 'Y-10_A-3': 'Y-10_A-3', 'Y-10_A-2': 'Y-10_A-2', 'Y-10_A-1': 'Y-10_A-1', 'Y-10_X10': 'Y-10_X10', 'Y-10_A1': 'Y-10_A1', 'Y-10_A2': 'Y-10_A2', 'Y-10_A3': 'Y-10_A3', 'Y-10_A4': 'Y-10_A4', 'Y10': 'Y10_'}
coordinate_row_7 = {'B-1': 'B-1_', 'B-1_A-4': 'B-1_A-4', 'B-1_A-3': 'B-1_A-3', 'B-1_A-2': 'B-1_A-2', 'B-1_A-1': 'B-1_A-1', 'B-1_X10': 'B-1_X10', 'B-1_A1': 'B-1_A1', 'B-1_A2': 'B-1_A2', 'B-1_A3': 'B-1_A3', 'B-1_A4': 'B-1_A4', 'D-1': 'D-1_'}
coordinate_row_8 = {'B-2': 'B-2_', 'B-2_A-4': 'B-2_A-4', 'B-2_A-3': 'B-2_A-3', 'B-2_A-2': 'B-2_A-2', 'B-2_A-1': 'B-2_A-1', 'B-2_X10': 'B-2_X10', 'B-2_A1': 'B-2_A1', 'B-2_A2': 'B-2_A2', 'B-2_A3': 'B-2_A3', 'B-2_A4': 'B-2_A4', 'D-2': 'D-2_'}
coordinate_row_9 = {'B-3': 'B-3_', 'B-3_A-4': 'B-3_A-4', 'B-3_A-3': 'B-3_A-3', 'B-3_A-2': 'B-3_A-2', 'B-3_A-1': 'B-3_A-1', 'B-3_X10': 'B-3_X10', 'B-3_A1': 'B-3_A1', 'B-3_A2': 'B-3_A2', 'B-3_A3': 'B-3_A3', 'B-3_A4': 'B-3_A4', 'D-3': 'D-3_'}
coordinate_row_10 = {'B-4': 'B-4_', 'B-4_A-4': 'B-4_A-4', 'B-4_A-3': 'B-4_A-3', 'B-4_A-2': 'B-4_A-2', 'B-4_A-1': 'B-4_A-1', 'B-4_X10': 'B-4_X10', 'B-4_A1': 'B-4_A1', 'B-4_A2': 'B-4_A2', 'B-4_A3': 'B-4_A3', 'B-4_A4': 'B-4_A4', 'D-4': 'D-4_'}
coordinate_row_11 = {'llhc': '|BB|', 'C-4': 'C-4_', 'C-3': 'C-3_', 'C-2': 'C-2_', 'C-1': 'C-1_', 'X-10': 'X-10', 'C1': 'C1__', 'C2': 'C2__', 'C3': 'C3__', 'C4': 'C4__', 'lrhc': '|BB|'}

board = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10, row_11]
coordinate_board = [coordinate_row_1, coordinate_row_2, coordinate_row_3, coordinate_row_4, coordinate_row_5, coordinate_row_6, coordinate_row_7, coordinate_row_8, coordinate_row_9, coordinate_row_10, coordinate_row_11]
board_to_print = ''
ended = False
player_turn = True

def print_board(board):
    board_to_print = ''
    row_count = 0
    for row in board:
        value_count = 0
        row_count += 1
        for value in row:
            value_count += 1
            if value_count < 11 and row_count < 11:
                board_to_print += row[value]
            if value_count == len(row):
                board_to_print += '\n'
    print(board_to_print)

def tie_calculator(board):
    row_count = 0
    value_count = 0
    marker_count = 0
    tie = False
    for row in board:
        row_count += 1
        for value in row:
            value_count += 1
            if value_count > 1 and value_count < 11 and row_count > 1 and row_count < 11:
                if board[row_count - 1][value] == player_marker or board[row_count - 1][value] == computer_marker:
                    marker_count += 1
    if marker_count == 90:
        tie = True
    return tie

def place_player_marker(coordinate, board, player_marker):
    for row in board:
        if coordinate in row:
            row[coordinate] = player_marker 
    return board

def place_computer_marker(coordinate, board, computer_marker):
    for row in board:
        if coordinate in row:
             row[coordinate] = computer_marker
    return board

def get_coordinate():
    possible_coordinate_1 = ['B4', 'B3', 'B2', 'B1', 'Y-10', 'B-1', 'B-2', 'B-3', 'B-4']
    possible_coordinate_2 = ['A4', 'A3', 'A2', 'A1', 'X10', 'A-1', 'A-2', 'A-3', 'A-4']
    getting_coordinate = True
    while getting_coordinate == True:
        coordinate_1 = input('What is the first coordinate value where you would like to place your marker?  a value that starts with B or Y. ')
        if coordinate_1 not in possible_coordinate_1:
            print('Sorry I didn\'t get that')
        else:
            coordinate_2 = input('What is the second coordinate value where you would like to place your marker? Name a value that starts with A or X. ')
            if coordinate_2 not in possible_coordinate_2:
                print('Sorry I didn\'t get that')
            else:
                coordinate = coordinate_1 + '_' + coordinate_2
                getting_coordinate = False
    return coordinate

def get_computer_coordinate(coordinate):
    b_value = random.randrange(-4, 5)
    a_value = random.randrange(-4, 5)
    if b_value != 0 and a_value != 0:
        coordinate.append('B' + str(b_value) + '_' + 'A' + str(a_value))
    elif b_value == 0:
        coordinate.append('Y' + str(-10) + '_' + 'A' + str(a_value))
    else:
        coordinate.append('B' + str(b_value) + '_' + 'X' + str(10))
    return coordinate

def computer_spot_picker(board, player_marker, computer_marker):
    coordinate = []
    row_count = 0
    computer_coordinate = get_computer_coordinate(coordinate)
    for row in board:
        row_count += 1
        if computer_coordinate[len(coordinate) - 1] in row:
            while board[row_count - 1][computer_coordinate[len(coordinate) - 1]] == player_marker or board[row_count - 1][computer_coordinate[len(coordinate) - 1]] == computer_marker or board[row_count - 1][computer_coordinate[len(coordinate) - 1]] == '|BB|':
                computer_coordinate = get_computer_coordinate(coordinate)
            if board[row_count - 1][computer_coordinate[len(coordinate) - 1]] == '|CC|':
                place_computer_marker(computer_coordinate[len(coordinate) - 1], board, computer_marker)
    return coordinate[len(coordinate) - 1]

def rock_paper_scissors():
    options = {1: 'rock', 2: 'paper', 3: 'scissors'}
    choices_differ = False
    computer_first = False
    print('To determine who will play first we will play a game of Rock Paper' + '\n' + 'Scissors. In case you don\'t know how to play rock beats scisors,' + '\n' + ' paper beats rock and scissors beats paper. Select scisors, rock' + '\n' + ' or paper. The computer will select one of those options as well ' + '\n' + 'and who ever wins will go first. \n')
    while choices_differ == False:
        player_choice = input('Which will you decide to use; rock, paper or scissors? Type in ' + '\n' + 'an option as written here. ')
        computer_picker = random.randrange(1, 4)
        if computer_picker == 1:
            computer_choice = options[1]
        elif computer_picker == 2:
            computer_choice = options[2]
        else:
            computer_choice = options[3]
        if (player_choice == 'rock' or player_choice == 'paper' or player_choice == 'scissors') and player_choice != computer_choice:
            choices_differ = True
            if player_choice == 'rock' and computer_choice == 'scissors':
                print('The player will go first')
            elif player_choice == 'scissors' and computer_choice == 'rock':
                print('The player will go first')
            elif player_choice == 'paper' and computer_choice == 'rock':
                print('The player will go first')
            elif computer_choice == 'rock' and player_choice == 'scissors':
                print('The computer will go first')
                computer_first = True
            elif computer_choice == 'scissors' and player_choice == 'rock':
                print('The computer will go first')
                computer_first = True
            elif computer_choice == 'paper' and player_choice == 'rock':
                print('The computer will go first')
                computer_first = True
            
        elif (player_choice == 'rock' or player_choice == 'paper' or player_choice == 'scissors') and player_choice == computer_choice:
            print('You and the computer both picked ' + player_choice + ' so the player that will play first has not been determined. Try again.')
        else:
            print('Sorry I didn\t get that.')
    return computer_first

def game_state(coordinate, coordinate_board, board, player_turn, ended):
    if player_turn == True:
        player_tic_tac_toe_checker = detect_player_marker(coordinate, coordinate_board, board)
        value_count_5 = 0
        for tic_tac_toe in player_tic_tac_toe_checker:
            value_count_5 += 1
            if tic_tac_toe == 5:
                ended = True
                print('You got Tic Tac Toe! You win!')
                break
    else:
        computer_tic_tac_toe_checker = detect_computer_marker(coordinate, coordinate_board, board)
        value_count_5 = 0
        for tic_tac_toe in computer_tic_tac_toe_checker:
            value_count_5 += 1
            if tic_tac_toe == 5:
                ended = True
                print('The computer got Tic Tac Toe. You lose.')
                break
    return ended


def game_start():
    declared_marker = False
    print_board(board)
    while declared_marker == False:
        player_marker_kind = input('Will you play as x or o? Type your answer in lowercase letters. ')
        if player_marker_kind == 'x':
            player_marker = '|_X|'
            computer_marker = '|_O|'
            declared_marker = True
        elif player_marker_kind == 'o':
            player_marker = '|_O|'
            computer_marker = '|_X|'
            declared_marker = True
        elif player_marker_kind != 'x' or player_marker_kind != 'o':
            print('Sorry I didn\'t get that.')
        print('\n' + 'This is Super Tic Tac Toe. Allgn five markers, of the kind which ' + '\n' + 'you have selected, consecutivly before the computer does to win.' + '\n' + 'Please note that for each coordinate which you select you may' + '\n' + 'only select one half of the value at a time. For example the' + '\n' + 'coordinate B3 A2 is selected first by typing in B3 and then A2' + '\n' + 'as directed; both of which can be found on the farthest row left' + '\n' + 'on the board and the top row just like every other coordinate' + '\n' + 'Good luck!' + '\n')
    return player_marker
            

def game_loop(player_marker):
    if player_marker == '|_X|':
        computer_marker = '|_O|'
    first_to_play = rock_paper_scissors()
    if first_to_play == True:
        print('Computer\'s turn.')
        player_turn = False
        computer_choice = computer_spot_picker(board, player_marker, computer_marker)
        computer_game_state = game_state(computer_choice, coordinate_board, board, player_turn, ended)
        print_board(board)   

    while ended == False:
        print('Your turn.')
        player_turn = True
        coordinate = get_coordinate()
        place_player_marker(coordinate, board, player_marker)

        player_game_state = game_state(coordinate, coordinate_board, board, player_turn, ended)  
        tie = tie_calculator(board)
        if tie == True:
            print('Tie.')
        print_board(board)
        if player_game_state == True:
            break
        print('Computer\'s turn.')
        player_turn = False
        computer_choice = computer_spot_picker(board, player_marker, computer_marker)
        computer_game_state = game_state(computer_choice, coordinate_board, board, player_turn, ended)   
        tie = tie_calculator(board)
        if tie == True:
            print('Tie.')
        print_board(board)
        if computer_game_state == True:
            break

game_loop(game_start())