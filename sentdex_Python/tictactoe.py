game = [[1,0,2],
        [0,2,2],
        [2,1,1]]


def win(current_game):
    for col in range(len(game)):
        check = []
        for row in current_game: 
            check.append(row[col])

        if check.count(check[0]) == len(check) and check[0] != 0:
            print("winner!")
  
    for row in current_game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("winner!")
    
    diagonals = []
    other_diagonal = []  
    for index in range(len(game)):
        diagonals.append(game[index][index])
    for index in range(len(game)):
        other_diagonal.append(game[len(game)-1-index][index])

    if diagonals.count(diagonals[0]) == len(diagonals):
        print("winner!")
    if other_diagonal.count(other_diagonal[0]) == len(other_diagonal):
        print("winner!")

win(game)

'''
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try: 
        print("   a  b  c")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map

    except IndexError as e: 
        print("Error: make sure you input row/column as 0 1 or 2", e)
    
    except Exception as e:
        print("Something went very wrong", e)


game = game_board(game, just_display=True)
game = game_board(game, player=1, row=3, column=1)
'''