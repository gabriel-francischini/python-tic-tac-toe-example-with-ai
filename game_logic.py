def has_winner(board):
    extended_board = board + [list(i) for i in zip(*board)] 
    for line in extended_board:        
        if (line[0] != ' '
            and all([symbol == line[0] for symbol in line])):
            return line[0]

    for coords in [
            [(0, 0), (1, 1), (2,2)],
            [(0,2), (1,1), (2,0)]
            ]:

        coord_0, coord_1, coord_2 = coords
        ex_x, ex_y = coord_0
        symbol = board[ex_x][ex_y]

        is_won = True
        for x, y in coords:
            is_won = is_won and board[x][y] == symbol

        if is_won and symbol != ' ':
            return symbol

    xs = 0
    for line in board:
        for symbol in line:
            if symbol == 'X':
                xs += 1

    if xs >= 4:
        return '-'
