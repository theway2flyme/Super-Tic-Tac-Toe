def detect_player_marker(coordinate, coordinate_board, board):
    row_count_2 = 0
    value_count_2 = 0
    tic_tac_toe_final_check = []

    def u_r_checker(coordinate, board, coordinate_board):
        tic_tac_toe_check = 1
        value_count = 0
        row_count_3 = 0
        value_count_3 = 0
        row_count_4 = 0
        value_count_4 = 0
        b_value = [] 
        a_value = [] 
        for row in coordinate_board:
            row_count_3 += 1
            for value in row:
                value_count_3 += 1
                if value == coordinate:
                    for value_3 in coordinate_board[0]:
                        value_count += 1
                        if value_count == value_count_3 + 4:
                            ac1 = value_3 
                            a_value.append(ac1)
                        if value_count == value_count_3 + 3:
                            ac2 = value_3
                            a_value.append(ac2)
                        if value_count == value_count_3 + 2:
                            ac3 = value_3
                            a_value.append(ac3)
                        if value_count == value_count_3 + 1:
                            ac4 = value_3
                            a_value.append(ac4)
                    for row_2 in coordinate_board:
                        row_count_4 += 1
                        for value_2 in row_2:
                            value_count_4 += 1
                            if value_count_4 == len(coordinate_board[row_count_4 - 1]):
                                value_count_4 = 0
                            if row_count_4 == row_count_3 - 4 and value_count_4 == 1:
                                bc1 = value_2
                                b_value.append(bc1)
                            if row_count_4 == row_count_3 - 3 and value_count_4 == 1:
                                bc2 = value_2
                                b_value.append(bc2)
                            if row_count_4 == row_count_3 - 2 and value_count_4 == 1:
                                bc3 = value_2
                                b_value.append(bc3)
                            if row_count_4 == row_count_3 - 1 and value_count_4 == 1:
                                bc4 = value_2
                                b_value.append(bc4)
        if len(b_value) >= 1 and len(a_value) >= 1:
            value_1 = b_value[0] + '_' + a_value[0]
            if board[row_count_3 - 2][value_1] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 2 and len(a_value) >= 2:
            value_2 = b_value[1] + '_' + a_value[1]
            if board[row_count_3 - 3][value_2] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 3 and len(a_value) >= 3:
            value_3 = b_value[2] + '_' + a_value[2]
            if board[row_count_3 - 4][value_3] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 4 and len(a_value) >= 1:
            value_4 = b_value[3] + '_' + a_value[3]
            if board[row_count_3 - 5][value_4] == player_marker:
                tic_tac_toe_check += 1
        return tic_tac_toe_check

    def top_checker(coordinate, board, coordinate_board):
        tic_tac_toe_check = 1 
        value_count  = 0
        row_count_3 = 0
        value_count_3 = 0
        row_count_4 = 0
        value_count_4 = 0
        b_value = [] 
        a_value = [] 
        for row in coordinate_board:
            row_count_3 += 1
            for value in row:
                value_count_3 += 1
                if value == coordinate:
                    for value_3 in coordinate_board[0]:
                        value_count += 1
                        if value_count_3 == value_count:
                            ac1 = value_3
                            a_value.append(ac1)
                        if value_count == value_count_3:
                            ac2 = value_3
                            a_value.append(ac2)
                        if value_count == value_count_3:
                            ac3 = value_3
                            a_value.append(ac3)
                        if value_count == value_count_3:
                            ac4 = value_3
                            a_value.append(ac4)
                    for row_2 in coordinate_board:
                        row_count_4 += 1
                        for value_2 in row_2:
                            value_count_4 += 1
                            if value_count_4 == len(coordinate_board[row_count_4 - 1]):
                                value_count_4 = 0
                            if row_count_4 == row_count_3 - 4 and value_count_4 == 1:
                                bc1 = value_2
                                b_value.append(bc1)
                            if row_count_4 == row_count_3 - 3 and value_count_4 == 1:
                                bc2 = value_2
                                b_value.append(bc2)
                            if row_count_4 == row_count_3 - 2 and value_count_4 == 1:
                                bc3 = value_2
                                b_value.append(bc3)
                            if row_count_4 == row_count_3 - 1 and value_count_4 == 1:
                                bc3 = value_2
                                b_value.append(bc3)

        if len(b_value) >= 1 and len(a_value) >= 1:
            value_1 = b_value[0] + '_' + a_value[0]
            if board[row_count_3 - 2][value_1] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 2 and len(a_value) >= 2:
            value_2 = b_value[1] + '_' + a_value[1]
            if board[row_count_3 - 3][value_2] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 3 and len(a_value) >= 3:
            value_3 = b_value[2] + '_' + a_value[2]
            if board[row_count_3 - 4][value_3] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 4 and len(a_value) >= 1:
            value_4 = b_value[3] + '_' + a_value[3]
            if board[row_count_3 - 5][value_4] == player_marker:
                tic_tac_toe_check += 1
        return tic_tac_toe_check
        
    def u_l_checker(coordinate, board, coordinate_board):
        tic_tac_toe_check = 1 
        value_count = 0
        row_count_3 = 0
        value_count_3 = 0
        row_count_4 = 0
        value_count_4 = 0
        b_value = [] 
        a_value = [] 
        for row in coordinate_board:
            row_count_3 += 1
            for value in row:
                value_count_3 += 1
                if value == coordinate:
                    for value_3 in coordinate_board[0]:
                        value_count + 1
                        if value_count == value_count_3 - 4:
                            ac1 = value_3
                            a_value.append(ac1)
                        if value_count == value_count_3 - 3:
                            ac2 = value_3
                            a_value.append(ac2)
                        if value_count == value_count_3 - 2:
                            ac3 = value_3
                            a_value.append(ac3)
                        if value_count == value_count_3 - 1:
                            ac4 = value_3
                            a_value.append(ac4)
                    for row_2 in coordinate_board:
                        row_count_4 += 1
                        for value_2 in row_2:
                            value_count_4 += 1
                        if value_count_4 == len(coordinate_board[row_count_4 - 1]):
                            value_count_4 = 0
                        if row_count_4 == row_count_3 - 4 and value_count_4 == 1:
                            bc1 = value_2
                            b_value.append(bc1)
                        if row_count_4 == row_count_3 - 3 and value_count_4 == 1:
                            bc2 = value_2
                            b_value.append(bc2)
                        if row_count_4 == row_count_3 - 2 and value_count_4 == 1:
                            bc3 = value_2
                            b_value.append(bc3)
                        if row_count_4 == row_count_3 - 1 and value_count_4 == 1:
                            bc4 = value_2
                            b_value.append(bc4)
        
        if len(b_value) >= 1 and len(a_value) >= 1:
            value_4 = b_value[0] + '_' + a_value[0]
            if board[row_count_3 - 5][value_4] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 2 and len(a_value) >= 2:
            value_3 = b_value[1] + '_' + a_value[1]
            if board[row_count_3 - 4][value_3] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 3 and len(a_value) >= 3:
            value_2 = b_value[2] + '_' + a_value[2]
            if board[row_count_3 - 3][value_2] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 4 and len(a_value) >= 1:
            value_1 = b_value[3] + '_' + a_value[3]
            if board[row_count_3 - 2][value_1] == player_marker:
                tic_tac_toe_check += 1

        return tic_tac_toe_check

    def left_checker(coordinate, board, coordinate_board):
        tic_tac_toe_check = 1
        value_count = 0
        row_count_3 = 0
        value_count_3 = 0
        row_count_4 = 0
        value_count_4 = 0
        b_value = [] 
        a_value = [] 
        for row in coordinate_board:
            row_count_3 += 1
            for value in row:
                value_count_3 += 1
                if value_count == coordinate:
                    for value_3 in coordinate_board[0]:
                        value_count + 1
                        if value_count == value_count_3 - 4:
                            ac1 = value_3
                            a_value.append(ac1)
                        if value_count == value_count_3 - 3:
                            ac2 = value_3
                            a_value.append(ac2)
                        if value_count == value_count_3 - 2:
                            ac3 = value_3
                            a_value.append(ac3)
                        if value_count == value_count_3 - 1:
                            ac4 = value_3
                            a_value.append(ac4)
                    for row_2 in coordinate_board:
                        row_count_4 += 1
                        if value_count_4 == len(coordinate_board[row_count_4 - 1]):
                            value_count_4 = 0
                        if row_count_4 == row_count_3 - 1 and value_count_4 == 1:
                            bc1 = value_2
                            b_value.append(bc1)
                        if row_count_4 == row_count_3 and value_count_4 == 1:
                            bc2 = value_2
                            b_value.append(bc2)
                        if row_count_4 == row_count_3 and value_count_4 == 1:
                            bc3 = value_2
                            b_value.append(bc3)
                        if row_count_4 == row_count_3 and value_count_4 == 1:
                            bc4 = value_2
                            b_value.append(bc4)
        
        if len(b_value) >= 1 and len(a_value) >= 1:
           value_1 = b_value[3] + '_' + a_value[3]
           if board[row_count_3 - 1][value_1] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 2 and len(a_value) >= 2:
            value_2 = b_value[2] + '_' + a_value[2]
            if board[row_count_3 - 1][value_2] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 3 and len(a_value) >= 3:
            value_3 = b_value[1] + '_' + a_value[1]
            if board[row_count_3 - 1][value_3] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 4 and len(a_value) >= 1:
            value_4 = b_value[0] + '_' + a_value[0]
            if board[row_count_3 - 1][value_4] == player_marker:
                tic_tac_toe_check += 1
        return tic_tac_toe_check

    def right_checker(coordinate, board, coordinate_board):
        tic_tac_toe_check = 1 
        value_count = 0
        row_count_3 = 0
        value_count_3 = 0
        row_count_4 = 0
        value_count_4 = 0
        b_value = [] 
        a_value = [] 
        for row in coordinate_board:
            row_count_3 += 1
            for value in row:
                value_count_3 += 1
                if value == coordinate:
                    for value_3 in coordinate_board[0]:
                        value_count += 1
                        if value_count == value_count_3 + 4:
                            ac1 = value_3 
                            a_value.append(ac1)
                        if value_count == value_count_3 + 3:
                            ac2 = value_3
                            a_value.append(ac2)
                        if value_count == value_count_3 + 2:
                            ac3 = value_3
                            a_value.append(ac3)
                        if value_count == value_count_3 + 1:
                            ac4 = value_3
                            a_value.append(ac4)
                    for row_2 in coordinate_board:
                        row_count_4 += 1
                        for value_2 in row_2:
                            value_count_4 += 1
                            if value_count_4 == len(coordinate_board[row_count_4 - 1]):
                                value_count_4 = 0
                            if row_count_4 == row_count_3 and value_count_4 == 1:
                                bc1 = value_2
                                b_value.append(bc1)
                            if row_count_4 == row_count_3 and value_count_4 == 1:
                                bc2 = value_2
                                b_value.append(bc2)
                            if row_count_4 == row_count_3 and value_count_4 == 1:
                                bc3 = value_2
                                b_value.append(bc3)
                            if row_count_4 == row_count_3 and value_count_4 == 1:
                                bc4 = value_2
                                b_value.append(bc4)
        
        if len(b_value) >= 1 and len(a_value) >= 1:
            value_1 = b_value[0] + '_' + a_value[0]
            if board[row_count_3 - 1][value_1] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 2 and len(a_value) >= 2:
            value_2 = b_value[1] + '_' + a_value[1]
            if board[row_count_3 - 1][value_2] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 3 and len(a_value) >= 3:
            value_3 = b_value[2] + '_' + a_value[2]
            if board[row_count_3 - 1][value_3] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 4 and len(a_value) >= 1:
            value_4 = b_value[3] + '_' + a_value[3]
            if board[row_count_3 - 1][value_4] == player_marker:
                tic_tac_toe_check += 1
        return tic_tac_toe_check

    def l_l_checker(coordinate, board, coordinate_board):
        tic_tac_toe_check = 1 
        value_count = 0
        row_count_3 = 0
        value_count_3 = 0
        row_count_4 = 0
        value_count_4 = 0
        b_value = [] 
        a_value = [] 
        for row in coordinate_board:
            row_count_3 += 1
            for value in row:
                value_count_3 += 1
                if value_count == coordinate:
                    for value_3 in coordinate_board[0]:
                        value_count + 1
                        if value_count == value_count_3 - 4:
                            ac1 = value_3
                            a_value.append(ac1)
                        if value_count == value_count_3 - 3:
                            ac2 = value_3
                            a_value.append(ac2)
                        if value_count == value_count_3 - 2:
                            ac3 = value_3
                            a_value.append(ac3)
                        if value_count == value_count_3 - 1:
                            ac4 = value_3
                            a_value.append(ac4)
                    for row_2 in coordinate_board:
                        row_count_4 += 1
                        for value_2 in row_2:
                            value_count_4 += 1
                        if value_count_4 == len(coordinate_board[row_count_4 - 1]):
                            value_count_4 = 0
                        if row_count_4 == row_count_3 + 4 and value_count_4 == 1:
                            bc1 = value_2
                            b_value.append(bc1)
                        if row_count_4 == row_count_3 + 3 and value_count_4 == 1:
                            bc2 = value_2
                            b_value.append(bc2)
                        if row_count_4 == row_count_3 + 2 and value_count_4 == 1:
                            bc3 = value_2
                            b_value.append(bc3)
                        if row_count_4 == row_count_3 + 1 and value_count_4 == 1:
                            bc4 = value_2
                            b_value.append(bc4)
        
        if len(b_value) >= 1 and len(a_value) >= 1:
            value_4 = b_value[0] + '_' + a_value[0]
            if board[row_count_3][value_4] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 2 and len(a_value) >= 2:
            value_3 = b_value[1] + '_' + a_value[1]
            if board[row_count_3 + 1][value_3] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 3 and len(a_value) >= 3:
            value_2 = b_value[2] + '_' + a_value[2]
            if board[row_count_3 + 2][value_2] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 4 and len(a_value) >= 1:
            value_1 = b_value[3] + '_' + a_value[3]
            if board[row_count_3 + 3][value_1] == player_marker:
                tic_tac_toe_check += 1
        return tic_tac_toe_check

    def bottom_checker(coordinate, board, coordinate_board):
        tic_tac_toe_check = 1 
        value_count  = 0
        row_count_3 = 0
        value_count_3 = 0
        row_count_4 = 0
        value_count_4 = 0
        b_value = [] 
        a_value = [] 
        for row in coordinate_board:
            row_count_3 += 1
            for value in row:
                value_count_3 += 1
                if value == coordinate:
                    for value_3 in coordinate_board[0]:
                        value_count += 1
                        if value_count_3 == value_count:
                            ac1 = value_3
                            a_value.append(ac1)
                        if value_count == value_count_3:
                            ac2 = value_3
                            a_value.append(ac2)
                        if value_count == value_count_3:
                            ac3 = value_3
                            a_value.append(ac3)
                        if value_count == value_count_3:
                            ac4 = value_3
                            a_value.append(ac4)
                    for row_2 in coordinate_board:
                        row_count_4 += 1
                        for value_2 in row_2:
                            value_count_4 += 1
                            if value_count_4 == len(coordinate_board[row_count_4 - 1]):
                                value_count_4 = 0
                            if row_count_4 == row_count_3 + 4 and value_count_4 == 1:
                                bc1 = value_2
                                b_value.append(bc1)
                            if row_count_4 == row_count_3 + 3 and value_count_4 == 1:
                                bc2 = value_2
                                b_value.append(bc2)
                            if row_count_4 == row_count_3 + 2 and value_count_4 == 1:
                                bc3 = value_2
                                b_value.append(bc3)
                            if row_count_4 == row_count_3 + 1 and value_count_4 == 1:
                                bc4 = value_2
                                b_value.append(bc4)

        if len(b_value) >= 1 and len(a_value) >= 1:
            value_1 = b_value[0] + '_' + a_value[0]
            if board[row_count_3][value_1] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 2 and len(a_value) >= 2:
            value_2 = b_value[1] + '_' + a_value[1]
            if board[row_count_3 + 1][value_2] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 3 and len(a_value) >= 3:
            value_3 = b_value[2] + '_' + a_value[2]
            if board[row_count_3 + 2][value_3] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 4 and len(a_value) >= 1:
            value_4 = b_value[3] + '_' + a_value[3]
            if board[row_count_3 + 3][value_4] == player_marker:
                tic_tac_toe_check += 1
        return tic_tac_toe_check

    def l_r_checker(coordinate, board, coordinate_board):
        tic_tac_toe_check = 1 
        value_count = 0
        row_count_3 = 0
        value_count_3 = 0
        row_count_4 = 0
        value_count_4 = 0
        b_value = [] 
        a_value = [] 
        for row in coordinate_board:
            row_count_3 += 1
            for value in row:
                value_count_3 += 1
                if value == coordinate:
                    for value_3 in coordinate_board[0]:
                        value_count += 1
                        if value_count == value_count_3 + 4:
                            ac1 = value_3
                            a_value.append(ac1)
                        if value_count == value_count_3 + 3:
                            ac2 = value_3
                            a_value.append(ac2)
                        if value_count == value_count_3 + 2:
                            ac3 = value_3
                            a_value.append(ac3)
                        if value_count == value_count_3 + 1:
                            ac4 = value_3
                            a_value.append(ac4)
                    for row_2 in coordinate_board:
                        row_count_4 += 1
                        for value_2 in row_2:
                            value_count_4 += 1
                            if value_count_4 == len(coordinate_board[row_count_4 - 1]):
                                value_count_4 = 0
                            if row_count_4 == row_count_3 + 4 and value_count_4 == 1:
                                bc1 = value_2
                                b_value.append(bc1)
                            if row_count_4 == row_count_3 + 3 and value_count_4 == 1:
                                bc2 = value_2
                                b_value.append(bc2)
                            if row_count_4 == row_count_3 + 2 and value_count_4 == 1:
                                bc3 = value_2
                                b_value.append(bc3)
                            if row_count_4 == row_count_3 + 1 and value_count_4 == 1:
                                bc4 = value_2
                                b_value.append(bc4)
        
        if len(b_value) >= 1 and len(a_value) >= 1:
            value_1 = b_value[0] + '_' + a_value[0]
            if board[row_count_3][value_1] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 2 and len(a_value) >= 2:
            value_2 = b_value[1] + '_' + a_value[1]
            if board[row_count_3 + 1][value_2] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 3 and len(a_value) >= 3:
            value_3 = b_value[2] + '_' + a_value[2]
            if board[row_count_3 + 2][value_3] == player_marker:
                tic_tac_toe_check += 1
        if len(b_value) >= 4 and len(a_value) >= 1:
            value_4 = b_value[3] + '_' + a_value[3]
            if board[row_count_3 + 3][value_4] == player_marker:
                tic_tac_toe_check += 1
        return tic_tac_toe_check

    u_r = u_r_checker(coordinate, board, coordinate_board)
    top = top_checker(coordinate, board, coordinate_board)
    u_l = u_l_checker(coordinate, board, coordinate_board)
    left = left_checker(coordinate, board, coordinate_board) 
    right = right_checker(coordinate, board, coordinate_board) 
    l_l = l_l_checker(coordinate, board, coordinate_board) 
    bottom = bottom_checker(coordinate, board, coordinate_board) 
    l_r = l_r_checker(coordinate, board, coordinate_board)



    # for row in coordinate_board:
    #     row_count += 1
    #     print(row_count)
    #     for value in coordinate_board:
    #         value_count += 1
    #         if value in coordinate_board == coordinate:
    # for row_2 in board:
    #     row_count_2 += 1
    #     print(row_count_2)
    #     for value_2 in board:
    #         value_count_2 += 1
    #         if value_2 == coordinate:
    tic_tac_toe_final_check = [u_r, top, u_l, left, right, l_l, bottom, l_r]
                                                    
    return tic_tac_toe_final_check