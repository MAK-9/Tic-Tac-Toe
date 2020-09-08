text = '_________'


def table_printer():
    print('---------')
    print('|', matrix[0][2], matrix[1][2], matrix[2][2], '|')
    print('|', matrix[0][1], matrix[1][1], matrix[2][1], '|')
    print('|', matrix[0][0], matrix[1][0], matrix[2][0], '|')
    print('---------')


# create a matrix for future use
matrix = [[text[6], text[3], text[0]],
          [text[7], text[4], text[1]],
          [text[8], text[5], text[2]]]
game_finished = False
# print table
table_printer()
current_player = 'X'
# Check if coords are valid
moves = 0
# GAME LOOP
while not game_finished:
    # Ask player for coords
    coords = input('Enter coordinates: ')
    coords = coords.split()
    while True:
        if not ''.join(coords).isnumeric():
            print('You should enter numbers!')
        elif len(coords) != 2:
            print('Use 2 coordinates!')
        elif int(coords[0]) > 3 or int(coords[0]) < 1 or int(coords[1]) > 3 or int(coords[1]) < 1:
            print('Coordinates should be from 1 to 3!')
        elif matrix[int(coords[0]) - 1][int(coords[1]) - 1] != '_':
            print('This cell is occupied! Choose another one!')
        else:
            break
        coords = input('Try again: ').split()
    coords = [int(i) - 1 for i in coords]
    matrix[coords[0]][coords[1]] = current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    table_printer()
    moves += 1
    # check board status
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != '_':
            print(matrix[i][0], 'wins')
            game_finished = True
            break
        elif matrix[0][i] == matrix[1][i] == matrix[2][i] != '_':
            print(matrix[0][i], 'wins')
            game_finished = True
            break
        elif matrix[0][0] == matrix[1][1] == matrix[2][2] != '_':
            print(matrix[0][0], 'wins')
            game_finished = True
            break
        elif matrix[0][2] == matrix[1][1] == matrix[2][0] != '_':
            print(matrix[0][2], 'wins')
            game_finished = True
            break
        elif moves > 8:
            print('Draw')
            game_finished = True
            break
