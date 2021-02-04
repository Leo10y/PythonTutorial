game = [[1, 1, 1],
		[2, 2, 2],
		[2, 2, 0],]

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")								# hardcoded, fix in p14
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2",e)

    except Exception as e:
        print("Something went very wrong!",e)




#Diagonal
'''diags = []
for col, row in enumerate(reversed(range(len(game)))):
	diags.append(game[row][col])

diags = []
for ix in range(len(game)):
	diags.append(game[ix][ix])'''
#TODO: set winning conidition


#Vertical
'''#columns = [0, 1, 2]    das können wir auch mit range(len(game)) erstellen (siehe unten)

for col in range(len(game)):
	check = []

	for row in game:
		# print(row[0])					 prints first element of first row
		check.append(row[col])

	if check.count(check[0]) == len(row) and check[0] != 0:
		print("Winner!")'''


#Horizontal
'''def win(current_game):
	for row in game:
		print(row)
		if row.count(row[0]) == len(row) and row[0] != 0:
			print("Winner!")

win(game)'''
