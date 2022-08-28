# Print game board
board=["-","-","-","-","-","-","-","-","-"]

current_player="X"
winner= ""
gamerunning=True

def game_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"-----------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"-----------")
    print(f"{board[6]} | {board[7]} | {board[8]}")


# Take player input

def player_input(board):
    imp=int(input("Choose a number from range 1-9"))
    if imp >=1 and imp <=9 and board[imp-1]=="-":
        board[imp-1]=current_player
    else:
        print("Player is already in that spot")


# check for win or tie

def horizontal_win(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner=board[6]
        return True

def diagnal_win(board):
    global winner
    if board[0]==board[4]==board[8] and board!="-":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!="-":
        winner=board[2]
        return True

def vertical_win(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[6] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
def tie(board):
    global gamerunning
    if "-" not in board:
        game_board(board)
        print("Its a tie")
        gamerunning=False
    else:
        current_player="X"

def check_win():

    global gamerunning

    if horizontal_win(board) or vertical_win(board) or diagnal_win(board):
        print(f"The winner is {winner}")
        gamerunning=False




# switch the player
def switch_player():
    global current_player
    if current_player=="X":
        current_player="0"
    else:
        current_player="X"










# Check for win or tie again
while gamerunning:
    game_board(board)
    player_input(board)
    switch_player()
    check_win()
    tie(board)



